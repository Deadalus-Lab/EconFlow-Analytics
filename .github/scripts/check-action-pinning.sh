#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-action-pinning.sh -- every third-party action is a reviewed commit, not
# a name somebody else can repoint.
#
# WHY. `uses: owner/action@v5` resolves a TAG, and a tag is a mutable pointer in
# a repository this project does not control. Whoever owns it can move it to any
# commit at any time, and every workflow run after that executes code nobody
# here reviewed -- with whatever permissions the job was granted. This is not
# hypothetical: it is the mechanism behind the tj-actions/changed-files
# compromise, where a moved tag turned a widely used action into a credential
# exfiltrator across tens of thousands of repositories in a single afternoon.
# A forty-character commit SHA cannot be repointed, so a review of it stays true.
#
# WHAT IT REQUIRES OF EVERY `uses:` REFERENCE
#   1. a local action (`./path`) -- which is this repository's own code at this
#      repository's own commit, and therefore already reviewed -- or
#   2. `owner/repo[/subdir]@<40 lowercase hex>` , or
#   3. a container reference pinned by digest (`docker://image@sha256:...`)
#
# AND A HUMAN-READABLE VERSION COMMENT after the SHA. A bare forty-character hex
# string tells a reviewer nothing: `# v5` is what makes the diff of a Dependabot
# bump legible, and it is what lets anybody confirm the pin against the upstream
# release without resolving the hash by hand. Dependabot writes and maintains
# this comment itself, so requiring it costs nothing and losing it would mean
# the pins were edited by something that does not understand them.
#
# WHY THE MATCHING IS DONE IN PYTHON. A `uses:` value can be quoted or bare, can
# carry a trailing comment, and appears in both `.github/workflows/*.yml` and
# `.github/actions/**/action.yml`. Parsing that with a shell pipeline of `grep`
# and `sed` is how a gate ends up silently matching nothing -- and on a
# maintainer machine `grep` resolves to ugrep, whose `--include` and
# `--exclude-dir` do not behave as the GNU flags of the same name do, so a scan
# written with them undercounts on one host and not the other without saying so.
# Confirm which grep is in play with `grep --version | head -1`. Every file here
# is reached through an explicit glob instead.
#
# THREE ANTI-VACUITY GUARDS, because a scan that examined nothing must never
# read as a scan that passed:
#   1. floors on both the number of files opened and the number of references
#      found, below which the globs are wrong rather than the tree being clean
#   2. a POSITIVE CONTROL -- a table of references that MUST be rejected,
#      including the floating tag, the short SHA and the missing comment
#   3. a NEGATIVE CONTROL -- references that MUST be accepted, so the pattern
#      cannot pass by tightening into "reject everything"
#
#   usage: check-action-pinning.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
command -v python3 >/dev/null 2>&1 || {
  echo "FAIL: python3 is required by this gate and is not on PATH." >&2
  exit 1
}

python3 - "$ROOT" <<'PY'
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1])

# The floors. They are literals here rather than in .github/inventory.json only
# because no key measures them yet. This gate prints both figures on every green
# run, so the current pair is one invocation away:
#   bash .github/scripts/check-action-pinning.sh .
# Measured 2026-08-22: 5 files, 46 references. The floors sit below that so an
# ordinary addition does not trip them, and far enough above zero that a glob
# that stopped matching cannot pass. The file floor fell from 5 to 4 with the
# measurement, because a floor standing at its own measurement turns the next
# ordinary deletion into a red gate and teaches people to edit the number.
MIN_FILES = 4
MIN_REFERENCES = 20

# `uses:` as a step key: optional list dash, the key, the value, an optional
# trailing comment. The value may be quoted.
USES = re.compile(r"""^\s*(?:-\s+)?uses:\s*(?P<q>["']?)(?P<ref>[^"'#\s]+)(?P=q)\s*(?P<comment>#.*)?$""")

LOCAL = re.compile(r"^\./")
DIGEST = re.compile(r"^docker://[^@]+@sha256:[0-9a-f]{64}$")
PINNED = re.compile(r"^[A-Za-z0-9._-]+/[A-Za-z0-9._/-]+@(?P<sha>[0-9a-f]{40})$")


def verdict(ref: str, comment: str | None) -> str | None:
    """Return None if the reference is acceptable, else why it is not."""
    if LOCAL.match(ref):
        return None  # this repository's own code, at this repository's commit
    if DIGEST.match(ref):
        return None
    if "@" not in ref:
        return "no version at all; a bare action name floats on its default branch"
    if not PINNED.match(ref):
        _, _, rev = ref.partition("@")
        if re.fullmatch(r"[0-9a-f]{7,39}", rev):
            return f"pinned to the abbreviated SHA {rev!r}; git abbreviations are ambiguous, use all forty characters"
        return f"pinned to {rev!r}, which is a tag or branch -- a mutable pointer in a repository this project does not control"
    if not comment:
        return "pinned by SHA but carries no `# version` comment, so no reviewer can tell what was pinned"
    return None


files = sorted(root.glob(".github/workflows/*.yml")) + sorted(root.glob(".github/actions/*/action.yml"))

references = 0
findings = []
for path in files:
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        m = USES.match(line)
        if not m:
            continue
        references += 1
        why = verdict(m.group("ref"), m.group("comment"))
        if why:
            findings.append((path, n, m.group("ref"), why))

# --- anti-vacuity 1: the floors ------------------------------------------
if len(files) < MIN_FILES:
    sys.exit(f"FAIL: opened {len(files)} workflow/action files, below the floor {MIN_FILES}. "
             "The glob is wrong, not the tree.")
if references < MIN_REFERENCES:
    sys.exit(f"FAIL: found {references} `uses:` references, below the floor {MIN_REFERENCES}. "
             "The pattern stopped matching; it did not find a clean tree.")

# --- anti-vacuity 2: the positive control ---------------------------------
MUST_REJECT = [
    ("actions/checkout@v5", "# v5"),                       # the floating tag
    ("actions/checkout@main", None),                       # a branch
    ("actions/checkout@fbc6f39", "# v5"),                  # an abbreviated SHA
    ("actions/checkout", None),                            # no version at all
    ("actions/checkout@fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09", None),  # no comment
]
for ref, comment in MUST_REJECT:
    if verdict(ref, comment) is None:
        sys.exit(f"FAIL: the positive control was NOT caught -- {ref!r} was accepted. "
                 "The pattern is broken and every green run of this gate proved nothing.")

# --- anti-vacuity 3: the negative control ---------------------------------
MUST_ACCEPT = [
    ("actions/checkout@fbc6f3992d24b796d5a048ff273f7fcc4a7b6c09", "# v5"),
    ("./.github/actions/assert-inventory", None),
]
for ref, comment in MUST_ACCEPT:
    why = verdict(ref, comment)
    if why is not None:
        sys.exit(f"FAIL: the negative control was rejected -- {ref!r}: {why}. "
                 "The pattern has tightened into 'reject everything'.")

if findings:
    for path, n, ref, why in findings:
        print(f"UNPINNED  {path}:{n}")
        print(f"    {ref}")
        print(f"    {why}")
    print()
    print(f"FAIL: {len(findings)} of {references} action references are not pinned to a "
          "full commit SHA.", file=sys.stderr)
    print("Resolve the tag to its commit and keep the version as a comment:", file=sys.stderr)
    print("  gh api repos/<owner>/<repo>/commits/<tag> --jq .sha", file=sys.stderr)
    print("Never write a hash you did not resolve.", file=sys.stderr)
    sys.exit(1)

print(f"ok: all {references} action references across {len(files)} files are pinned to a "
      "full commit SHA with a version comment (both controls fired).")
PY
