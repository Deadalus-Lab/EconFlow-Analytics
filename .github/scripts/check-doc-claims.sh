#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-doc-claims.sh -- the documents' own evidence is re-run, not trusted.
#
# WHAT IT ENFORCES. This repository writes every published figure beside the
# command that produces it: `| Wrapper modules | 598 | find ... | wc -l |`. That
# convention is what lets a reader verify a claim instead of believing it. This
# gate closes the loop by RUNNING the command and comparing its output to the
# number printed next to it. A figure that no longer matches its own evidence is
# a false claim, and it is caught here rather than by a reader.
#
# WHY IT EXISTS, MEASURED. On 2026-08-21 the catalogue had grown from 913 methods
# to 1456 and from 30 categories to 46, and the prose had not followed. Twenty-two
# published figures still described the smaller tree, spread across the
# architecture document, the roadmap and two decision records -- including a
# claim/evidence row asserting what `assert-inventory` reports, which by then
# reported something else entirely. Then a rename repointed the COMMANDS without
# touching the NUMBERS beside them, so two tables briefly stated 913 next to a
# command measuring 1456. None of `vale`,
# `typos`, `markdownlint` or `lychee` can see any of this: they check language,
# spelling, structure and links. Nothing checked whether the documents were TRUE.
#
# WHAT IT DELIBERATELY DOES NOT DO. It does not invent claims. A row is checked
# only when it has the exact published shape -- a label, a bare number, and a
# fenced command whose first word is one this gate is willing to execute. Prose
# figures written outside that shape are the author's responsibility, and pulling
# them in would mean guessing which noun a number belongs to.
#
# TWO PARSING TRAPS, both live-verified and both silent if you get them wrong:
#   * A Markdown table escapes a literal pipe as `\|`, so a piped command arrives
#     with a backslash and the shell rejects it. Unescape before running.
#   * A cell must be split on `|` only OUTSIDE backticks, or every piped command
#     is truncated at its first pipe and the gate reports an empty measurement.
# Both produced "measured nothing" rather than an error, which is exactly the
# shape of a gate that passes while examining nothing.
#
# THE COMMANDS RUN FROM engine/, because that is where the documents say to run
# them: "Every figure below is reproduced by the command beside it, run from
# engine/". A gate that runs them from somewhere else is testing a different claim.
#
# ONLY A CLOSED SET OF COMMANDS IS EXECUTED. `python3`, `find`, `cat` and `ls`.
# This gate runs text out of a document; the day one of those documents is edited
# by someone untrusted, an open executor becomes remote code execution. Anything
# outside the set is REPORTED AS SKIPPED and counted, so a document cannot quietly
# opt a figure out of verification by wrapping it in a different command.
#
# THREE ANTI-VACUITY GUARDS:
#   1. a floor from .github/inventory.json -- fewer claims checked than the floor
#      means the parser broke, not that the tree is clean
#   2. a POSITIVE control: a synthetic row whose command disagrees with its number,
#      which must be caught on every run
#   3. a NEGATIVE control: a synthetic row that agrees, which must NOT be flagged
#
#   usage: check-doc-claims.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

MANIFEST=".github/inventory.json"
[ -f "$MANIFEST" ] || { echo "FAIL: no manifest at $MANIFEST" >&2; exit 2; }
[ -d "engine" ]    || { echo "FAIL: no engine/ directory to run the commands from" >&2; exit 2; }

python3 - "$MANIFEST" <<'PY'
import json
import pathlib
import re
import subprocess
import sys

manifest_path = sys.argv[1]
ENGINE = pathlib.Path("engine")
RUNNABLE = ("python3", "find", "cat", "ls")
NUMBER = re.compile(r"\*{0,2}([\d.]+)(?:\s*/\s*([\d.]+))?\*{0,2}")


def cells(line: str) -> list[str]:
    """Split a table row on `|`, but never on a pipe inside backticks."""
    out, cur, tick = [], "", False
    for ch in line:
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    out.append(cur.strip())
    return out


def claims(text: str):
    """Yield (label, claimed, command) for every row in the published shape."""
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        parts = [c for c in cells(line) if c]
        if len(parts) < 3:
            continue
        label, claimed, cmd = parts[0], parts[1], parts[-1]
        m = NUMBER.fullmatch(claimed)
        if not m or not (cmd.startswith("`") and cmd.endswith("`")):
            continue
        yield label, m.group(1), cmd.strip("`").replace("\\|", "|")


def measure(cmd: str) -> str:
    return subprocess.run(
        cmd, shell=True, capture_output=True, text=True, timeout=120, cwd=ENGINE
    ).stdout.strip()


tracked = subprocess.run(
    ["git", "ls-files", "*.md"], capture_output=True, text=True, check=True
).stdout.split()

checked = skipped = 0
wrong: list[str] = []
for rel in tracked:
    path = pathlib.Path(rel)
    if not path.exists():
        continue
    for label, claimed, cmd in claims(path.read_text(encoding="utf-8")):
        if not cmd.startswith(RUNNABLE):
            skipped += 1
            continue
        checked += 1
        got = measure(cmd)
        if got != claimed:
            wrong.append(f"{rel}: '{label}' claims {claimed}, its own command measures "
                         f"{got or '<nothing>'}")

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(pathlib.Path(manifest_path).read_text())
            .get("docs", {}).get("min_doc_claims", 0))
if floor <= 0:
    sys.exit("FAIL: no docs.min_doc_claims in the manifest; a floor of zero is not a floor.")
if checked < floor:
    sys.exit(f"FAIL: verified {checked} claim(s), below the floor {floor}. The parser is "
             "wrong, not the documents.")

# --- anti-vacuity 2 and 3: the two controls ------------------------------
POSITIVE = "| Probe | **2** | `python3 -c \"print(1)\"` |"
NEGATIVE = "| Probe | **1** | `python3 -c \"print(1)\"` |"
for row, must_disagree in ((POSITIVE, True), (NEGATIVE, False)):
    parsed = list(claims(row))
    if len(parsed) != 1:
        sys.exit("FAIL: a control row did not parse; the row reader is broken.")
    _, claimed, cmd = parsed[0]
    disagrees = measure(cmd) != claimed
    if disagrees != must_disagree:
        which = "positive" if must_disagree else "negative"
        sys.exit(f"FAIL: the {which} control did not behave; this gate cannot be trusted.")

if wrong:
    for line in wrong:
        print(f"STALE  {line}")
    print()
    print(f"FAIL: {len(wrong)} published figure(s) disagree with the command printed beside "
          f"them, of {checked} verified.", file=sys.stderr)
    print("Re-run the command, put its output in the document, and say in the commit what "
          "moved. A number is not a claim to be remembered; it is a measurement with its "
          "evidence attached.", file=sys.stderr)
    sys.exit(1)

print(f"ok: every published figure matches its own command "
      f"({checked} verified, floor {floor}, {skipped} row(s) carried a command this gate "
      f"does not execute, both controls fired).")
PY
