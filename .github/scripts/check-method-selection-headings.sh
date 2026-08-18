#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-method-selection-headings.sh -- the corpus's section structure is real.
#
# METHOD-SELECTION.md is navigated BY SECTION: a reader, a retrieval index and
# the category guides all ask "which methods are in this category?" and answer
# it from the heading a card sits under. When a card is nested under the wrong
# section that answer is wrong, and nothing else in the tree notices, because
# every other consumer reads the machine mirror instead.
#
# This asserts the two agree: for every `### #NN` card heading, the category of
# the enclosing `## §` section must equal the category the sealed cards give
# for that id.
#
# ANTI-VACUITY: it asserts it examined at least the manifest's card count, so a
# parser that stopped matching headings fails instead of reporting agreement.
#
#   usage: check-method-selection-headings.sh [repo-root]
set -euo pipefail
cd "${1:-.}"

python3 - <<'PY'
import json, re, pathlib, sys

ENGINE = pathlib.Path("engine")
cards = {c["id"]: c["category"]
         for c in json.loads((ENGINE / "artifacts" / "method-cards.v1.json").read_text())["cards"]}
expected_total = json.loads(pathlib.Path(".github/inventory.json").read_text())["artifacts"]["n_cards"]

if len(cards) != expected_total:
    sys.exit(f"FAIL: read {len(cards)} cards, manifest says {expected_total}.")

section = None
examined = 0
wrong = []
missing_heading = set(cards.values())

for line in (ENGINE / "METHOD-SELECTION.md").read_text(encoding="utf-8").splitlines():
    if line.startswith("## "):
        # the category package the section names, e.g. `c01_preparation_prechecks`
        m = re.search(r"\bc([0-9]{2})_([a-z_]+)", line)
        section = f"{m.group(1)}-{m.group(2).replace('_', '-')}" if m else None
        missing_heading.discard(section)
        continue
    m = re.match(r"^### #(\d+)", line)
    if not m:
        continue
    cid = int(m.group(1))
    if cid not in cards:
        continue
    examined += 1
    if section != cards[cid]:
        wrong.append((cid, section, cards[cid]))

if examined < expected_total:
    sys.exit(f"FAIL: examined {examined} card headings, below the manifest's {expected_total}. "
             "The parser is wrong, not the document.")

if missing_heading:
    print(f"  {len(missing_heading)} category with no section heading: {sorted(missing_heading)}")
if wrong:
    print(f"FAIL: {len(wrong)} of {examined} cards are nested under the wrong section.")
    by = {}
    for cid, got, want in wrong:
        by.setdefault((got, want), []).append(cid)
    for (got, want), ids in sorted(by.items(), key=lambda kv: -len(kv[1])):
        print(f"  {len(ids):>3} cards under {got!r} belong to {want!r}  e.g. {sorted(ids)[:6]}")
    sys.exit(1)

print(f"ok: every one of {examined} cards is nested under its own category "
      f"({expected_total - len(missing_heading)} categories have a section heading).")
PY
