#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-private-refs.sh -- no tracked file cites a file a reader cannot open.
#
# WHAT IT ENFORCES. Five paths are ignored by git and are never published:
# CLAUDE.md, todo.md, .private/, .claude/ and .migration/. A tracked file may
# NAME one of them inside an ignore or exclusion list -- that is what such a list
# is for -- but it may not CITE one as a source. A citation sends the reader to a
# document that does not exist for them, and it publishes the shape of a private
# tree at the same time.
#
# WHY THIS GATE EXISTS. On 2026-08-23 a header comment in a workflow and a
# sentence in a method card both pointed a reader at a section of a private file.
# Both survived a full review cycle and sat on main, because every gate in this
# repository looked at something else: the vocabulary gate SKIPS these names by
# design (it must not read private prose), the link checker EXCLUDES those paths,
# and the spelling and register gates never see a path at all. The leak was found
# by hand. A rule enforced by memory is not enforced.
#
# WHY A SIBLING OF check-vocabulary.sh AND NOT AN EXTENSION OF IT. The two gates
# are opposite in both traversal and polarity. That one walks the FILESYSTEM with
# rglob and must skip .private/, .claude/, CLAUDE.md and todo.md so it never
# reads private prose; this one walks the TRACKED SET from git's index and must
# FLAG those same names wherever they appear. Folding the second subject into the
# first would put a skip rule and a match rule for the same five strings in one
# script, with two floors and two pairs of controls, and the first reader to
# simplify it would delete the wrong half.
#
# WHY THE EXEMPTION IS BY EXACT PATH, AND WHY IT IS ITSELF CHECKED. A prefix
# exemption is how a list quietly widens into "match nothing": a new file under
# an exempted directory inherits the exemption nobody granted it. Each path below
# is exact, and each was taken from an audit of the tree rather than from
# recollection -- .vale.ini and .pre-commit-config.yaml were proposed for this
# list and are absent from it, because neither names any of the five and an
# exemption that protects nothing is a hole with no floor under it.
#
# THREE ANTI-VACUITY GUARDS, because a scan that examined nothing must never read
# as a scan that passed:
#   1. it asserts it examined at least the floor in .github/inventory.json
#   2. a POSITIVE control, one per name, so the decay of a single token is caught
#      rather than hidden by the four that still work
#   3. a NEGATIVE control in two halves: text that merely resembles these paths
#      (.claude-mpm/, claude.yml) must NOT match, and every exempted path must
#      still be tracked AND still contain a real match -- an exemption whose file
#      no longer needs it is removed here, not left to widen
#
#   usage: check-private-refs.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

MANIFEST=".github/inventory.json"
[ -f "$MANIFEST" ] || {
  echo "FAIL: no manifest at $MANIFEST" >&2
  exit 2
}

python3 - "$MANIFEST" <<'PY'
import json
import pathlib
import re
import subprocess
import sys

manifest_path = sys.argv[1]

# ---------------------------------------------------------------- the names
# Each is anchored on the left so a longer name cannot carry one in: MY_CLAUDE.md
# and .claude-mpm/ are not these paths. The directories keep their trailing
# slash for the same reason. Matching is case-insensitive: a citation written
# `claude.md` sends the reader to exactly the same place.
NAMES = ("CLAUDE.md", "todo.md", ".private/", ".claude/", ".migration/")
PATTERN = re.compile(
    "|".join(r"(?<![\w.-])" + re.escape(n) for n in NAMES), re.IGNORECASE
)

# ------------------------------------------------------------ the exemptions
# Derived from an audit of the tracked tree on 2026-08-23, not from memory. Every
# one is a list whose PURPOSE is to name these paths.
EXEMPT = {
    ".gitignore",                            # the ignore rules themselves
    ".dockerignore",                         # kept out of the build context
    "typos.toml",                            # spelling: files never published
    "lychee.toml",                           # link checking: paths not followed
    ".markdownlint-cli2.yaml",               # Markdown lint: files not linted
    ".github/scripts/check-vocabulary.sh",   # its SKIP_DIRS and SKIP_NAMES
    ".github/scripts/check-toolchain-pin.sh",  # its find -not -path exclusions
    ".github/scripts/check-private-refs.sh",  # this gate: the names above
    ".github/scripts/check-skill-citations.sh",  # the directory it walks
}

tracked = [
    p for p in subprocess.run(
        ["git", "ls-files", "-z"], capture_output=True, check=True
    ).stdout.decode().split("\0") if p
]

examined = 0
findings = []
for rel in sorted(tracked):
    if rel in EXEMPT:
        continue
    try:
        text = pathlib.Path(rel).read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue  # binary, or tracked and deleted in the working tree
    examined += 1
    hits = [(n, line) for n, line in enumerate(text.splitlines(), 1)
            if PATTERN.search(line)]
    if hits:
        findings.append((rel, hits))

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(pathlib.Path(manifest_path).read_text())
            .get("private_refs", {}).get("min_files_scanned", 0))
if floor <= 0:
    sys.exit("FAIL: no private_refs.min_files_scanned in the manifest; "
             "a floor of zero is not a floor.")
if examined < floor:
    sys.exit(f"FAIL: examined {examined} tracked files, below the floor {floor}. "
             "The scan is wrong, not the tree.")

# --- anti-vacuity 2: the positive control --------------------------------
# One assertion per name. A single joined control would still pass with four of
# the five tokens broken.
for name in NAMES:
    if not PATTERN.search(f"the rule is written up in {name} near the top"):
        sys.exit(f"FAIL: the positive control for {name} was NOT detected; "
                 "the name list is broken.")

# --- anti-vacuity 3a: the negative control, on near-misses ----------------
NEGATIVE = ("the .claude-mpm/ cache, the claude.yml workflow, MY_CLAUDE.md, "
            "a private note, and the migration/ directory of the backend")
flagged = [m.group(0) for m in PATTERN.finditer(NEGATIVE)]
if flagged:
    sys.exit("FAIL: the negative control was flagged on "
             f"{flagged}; a longer name is not one of these paths.")

# --- anti-vacuity 3b: the negative control, on the exemptions -------------
# Each exempted path must still exist, still be tracked, and still contain a real
# match. An exemption whose file no longer needs one is deleted from the list
# above, never left in place: that is how an exemption list widens into one that
# exempts the tree.
tracked_set = set(tracked)
for rel in sorted(EXEMPT):
    if rel not in tracked_set:
        sys.exit(f"FAIL: exempted path {rel} is not tracked. Remove it from "
                 "EXEMPT rather than leaving an exemption nothing needs.")
    if not PATTERN.search(pathlib.Path(rel).read_text(encoding="utf-8")):
        sys.exit(f"FAIL: exempted path {rel} no longer names any of these "
                 "paths, so its exemption protects nothing. Remove it from "
                 "EXEMPT.")

if findings:
    for rel, hits in findings:
        print(f"CITES A PRIVATE PATH  {rel}")
        for n, line in hits[:5]:
            print(f"    {n}:{line.strip()[:150]}")
    total = sum(len(h) for _, h in findings)
    print()
    print(f"FAIL: a path a reader cannot open is cited {total} time(s) in "
          f"{len(findings)} file(s), examined {examined}.", file=sys.stderr)
    print("Describe the mechanism on its own terms instead. If the file is an "
          "ignore or exclusion list, naming these paths is its purpose -- add "
          "its exact path to EXEMPT in this script.", file=sys.stderr)
    sys.exit(1)

print(f"ok: no tracked file cites a path a reader cannot open "
      f"(examined {examined} tracked files, floor {floor}, "
      f"{len(NAMES)} positive and {len(EXEMPT) + 1} negative controls fired).")
PY
