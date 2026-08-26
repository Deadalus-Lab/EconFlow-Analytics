#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-skill-citations.sh -- no skill cites a path that is not in the tree.
#
# WHAT IT ENFORCES. A skill under .claude/skills/ is a binding process document:
# econflow-wrapper is the eight-step framework every one of the 598 wrapper
# bodies in phase 2.2 is written under. Its facts carry a path, and often a
# `file:line`. This gate resolves every one of them against the repository and
# refuses a citation that lands nowhere.
#
# WHY THIS GATE EXISTS. Measured on 2026-08-26, the econflow-wrapper skill cited
# five paths that do not exist -- engine/tests/README.md, engine/fixtures/README.md,
# two artifacts under their retired versioned filenames, and engine/METHOD-SELECTION.yaml
# -- plus six `file:line` spans into an ARCHITECTURE.md that has since been cut
# from roughly 800 lines to 119, so every one of those spans was past the end of
# the file. Nothing in this repository looked: the link checker follows URLs and
# excludes these paths, the vocabulary gate must not read them at all, and the
# skill is not tracked, so no gate that walks git's index can see it either. The
# rot was found by hand. A rule enforced by memory is not enforced.
#
# WHY A SIBLING OF check-private-refs.sh AND NOT AN EXTENSION OF IT. The two are
# opposite in traversal and in polarity, which is the same argument that script's
# own header makes for staying separate from check-vocabulary.sh. That one walks
# the TRACKED SET from git's index and must FLAG the string ".claude/" wherever it
# appears; this one walks the FILESYSTEM UNDER .claude/skills/ and must READ those
# same files and resolve what they say. Folding the second subject into the first
# would put a flag-rule and a read-rule for one path in a single script, with two
# floors and two pairs of controls, and the first reader to simplify it would
# delete the wrong half.
#
# THE ONE LIMITATION, STATED RATHER THAN HIDDEN. .claude/ is in .gitignore, so a
# fresh clone and every CI job hold no skills at all. This gate therefore cannot
# run there, and it says so on stdout and exits 0 rather than reporting a pass it
# did not earn. It bites where the skills actually live: the maintainer's
# checkout, on every commit, through .pre-commit-config.yaml.
#
# THREE ANTI-VACUITY GUARDS, because a scan that examined nothing must never read
# as a scan that passed:
#   1. it asserts it examined at least the floor in .github/inventory.json
#   2. a POSITIVE control: a planted dead path must be flagged, and a planted
#      line number past the end of a real file must be flagged too -- two
#      separate failures, so the decay of either half is caught on its own
#   3. a NEGATIVE control in two halves: a real path and a real `file:line` must
#      NOT be flagged, and every exempted name must still appear in a skill --
#      an exemption nothing needs is removed here, not left to widen
#
#   usage: check-skill-citations.sh [repo-root]
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
import sys

manifest = pathlib.Path(sys.argv[1])
ROOT = pathlib.Path.cwd()
SKILLS = ROOT / ".claude" / "skills"

#: THE SKILLS THIS PROJECT AUTHORS, NAMED EXACTLY. .claude/skills/ also holds
#: around a hundred vendored reference skills about other ecosystems -- Django,
#: Tailwind, Phoenix -- whose paths are claims about THEIR trees and resolve
#: nowhere here by design. Judging those would fill this gate with findings
#: nobody can act on, which is how a gate stops being read. Each name below is
#: asserted to exist, so a rename turns this red rather than quietly leaving the
#: set covering nothing; widening the set is a one-line diff here.
PROJECT_SKILLS = ("econflow-wrapper",)

if not SKILLS.is_dir():
    print("check-skill-citations: no .claude/skills/ in this checkout, so nothing "
          "was examined. .claude/ is in .gitignore and never reaches a clone or a "
          "CI job; this gate runs against the tree the skills live in.")
    raise SystemExit(0)

roots = []
for name in PROJECT_SKILLS:
    d = SKILLS / name
    if not d.is_dir():
        sys.exit(f"FAIL: PROJECT_SKILLS names {name}, and .claude/skills/{name}/ is "
                 "not there. A named skill that has moved leaves this gate covering "
                 "one skill fewer while still reporting success.")
    roots.append(d)

# A citation is a backticked run that looks like a path: it carries a slash or a
# known file extension, optionally followed by :N or :N-M.
CITE = re.compile(
    r"`([A-Za-z0-9_./<>*-]+?"
    r"(?:\.(?:py|json|md|yaml|yml|sh|toml|xml|txt|lock|cfg|ini))"
    r"|[A-Za-z0-9_./<>*-]*?/[A-Za-z0-9_./<>*-]+)"
    r"(?::(\d+)(?:-(\d+))?)?`"
)

#: A slash command is not a path, and neither is a file belonging to somebody
#: else's tree. Each name is EXACT rather than a prefix, for the reason
#: check-private-refs.sh gives: a prefix exemption is how a list quietly widens
#: into one that exempts everything under it.
EXEMPT = {
    "/simplify": "a slash command, not a path",
    "/security-review": "a slash command, not a path",
    "macros.xml": "Galaxy's own file, authored in the tool tree and not here",
    "tool_conf.xml": "Galaxy's own panel file, not a file of this repository",
}

#: Where a relative or bare citation may legitimately resolve, in this order.
PREFIXES = ("", "engine/", "engine/scripts/", "engine/tests/", "engine/artifacts/",
            "engine/src/econflow_engine/", "engine/src/econflow_engine/node/",
            "engine/src/econflow_engine/mcp/", ".github/", ".github/scripts/",
            ".github/workflows/")


def resolve(raw: str, origin: pathlib.Path) -> pathlib.Path | None:
    """The file a citation names, or None. Skill-relative first, then anchored."""
    cand = origin.parent / raw
    if cand.exists():
        return cand
    stripped = raw.lstrip("/")
    for pre in PREFIXES:
        c = ROOT / (pre + stripped)
        if c.exists():
            return c
    return None


def judge(text: str, origin: pathlib.Path) -> list[tuple[int, str, str]]:
    """Every citation in ``text`` that lands nowhere, as (line, citation, why)."""
    faults = []
    for n, line in enumerate(text.splitlines(), 1):
        for m in CITE.finditer(line):
            raw, lo, hi = m.group(1), m.group(2), m.group(3)
            span = f":{lo}-{hi}" if hi else (f":{lo}" if lo else "")
            if raw in EXEMPT or "<" in raw or "*" in raw:
                continue
            target = resolve(raw, origin)
            if target is None:
                faults.append((n, raw + span, "names no file in this tree"))
                continue
            if lo:
                total = len(target.read_text(errors="replace").splitlines())
                if int(hi or lo) > total:
                    faults.append((n, raw + span,
                                   f"{target.relative_to(ROOT)} has {total} lines"))
    return faults


docs = sorted(p for root in roots for p in root.rglob("*.md"))
examined = 0
findings = []
for doc in docs:
    text = doc.read_text(encoding="utf-8", errors="replace")
    examined += sum(1 for line in text.splitlines() for _ in CITE.finditer(line))
    faults = judge(text, doc)
    if faults:
        findings.append((doc.relative_to(ROOT), faults))

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(manifest.read_text())
            .get("skill_refs", {}).get("min_citations_scanned", 0))
if floor <= 0:
    sys.exit("FAIL: no skill_refs.min_citations_scanned in the manifest; "
             "a floor of zero is not a floor.")
if examined < floor:
    sys.exit(f"FAIL: examined {examined} citation(s) across {len(docs)} skill "
             f"document(s), below the floor {floor}. The scan is wrong, not the tree.")

# --- anti-vacuity 2: the positive controls, one per failure mode ----------
planted = SKILLS / "__control__.md"
dead = judge("a rule written up in `engine/tests/README.md` near the top", planted)
if len(dead) != 1 or "names no file" not in dead[0][2]:
    sys.exit("FAIL: the positive control for a DEAD PATH was not flagged; the "
             "resolver admits a path that does not exist.")
past = judge("the rule at `/ARCHITECTURE.md:99999` says so", planted)
if len(past) != 1 or "has " not in past[0][2]:
    sys.exit("FAIL: the positive control for a LINE PAST THE END OF A FILE was "
             "not flagged; the line check has stopped running.")

# --- anti-vacuity 3a: the negative control, on citations that resolve -----
sound = judge("`/ARCHITECTURE.md:1` and `.github/inventory.json` and "
              "`engine/artifacts/node-specs.json`", planted)
if sound:
    sys.exit(f"FAIL: the negative control was flagged on {sound}; this gate has "
             "decayed into one that refuses citations a reader can open.")

# --- anti-vacuity 3b: the negative control, on the exemptions -------------
# An exemption whose name no skill still uses is deleted from EXEMPT, never left
# in place: that is how an exemption list widens into one that exempts the tree.
prose = "\n".join(d.read_text(encoding="utf-8", errors="replace") for d in docs)
for name, why in sorted(EXEMPT.items()):
    if f"`{name}`" not in prose:
        sys.exit(f"FAIL: exempted citation {name} ({why}) appears in no skill, so "
                 "its exemption protects nothing. Remove it from EXEMPT.")

if findings:
    for rel, faults in findings:
        print(f"CITES A PATH A READER CANNOT OPEN  {rel}")
        for n, cite, why in faults[:10]:
            print(f"    {n}: `{cite}` -- {why}")
    total = sum(len(f) for _, f in findings)
    print()
    print(f"FAIL: {total} citation(s) in {len(findings)} skill document(s) land "
          f"nowhere, examined {examined}.", file=sys.stderr)
    print("Repoint each one at the file that holds the fact today. If the file "
          "belongs to another project, add its exact name to EXEMPT in this "
          "script with the reason.", file=sys.stderr)
    sys.exit(1)

print(f"ok: every citation in {len(docs)} skill document(s) resolves "
      f"(examined {examined} citations, floor {floor}, "
      f"2 positive and {len(EXEMPT) + 1} negative controls fired).")
PY
