#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# check-vocabulary.sh -- the engine documents itself in its own terms.
#
# WHAT IT ENFORCES. Documentation, argument names and error messages describe
# THIS implementation: Python types, this contract's argument kinds, and the
# statistical method itself. It refuses vocabulary borrowed from another
# ecosystem -- a foreign namespace operator, a foreign package index, a foreign
# package manager or test runner, a source-file extension this tree does not
# use. A wrapper that documents itself in somebody else's dialect sends the
# reader somewhere this repository cannot take them.
#
# WHAT IT DELIBERATELY PERMITS, and why the exemption list is explicit rather
# than guessed at:
#   * MATHEMATICS. R-hat, R^2, R*beta = q, the Kalman covariances Q and R, the
#     correlation matrix R_t, the cointegration rank r. Renaming any of these
#     would corrupt the econometrics.
#   * AN AUTHOR'S INITIAL. The catalogue cites Hyndman, R.J. and Tsay, R. among
#     many others. Stripping an initial misattributes a real researcher's work,
#     which is a far worse defect than any wording this gate exists to catch.
#
# THE MATCHING IS DONE IN PYTHON, AND THAT IS LOAD-BEARING. An earlier version
# stripped the exemptions with `sed -E "s/${ALLOWED}//g"`. The list contains a
# `/`, which is sed's own delimiter, so sed exited with an error, printed
# nothing, and the gate reported a clean tree while examining nothing at all. A
# planted defect did not turn it red. No helper that can fail into silence may
# sit between this gate and its input.
#
# THE PATTERNS ARE UNICODE-AWARE. `[A-Za-z]` does not contain an umlaut or an
# acute accent, so a naive class flags the initial inside a name like Roehmel or
# Renyi. `[^\W\d_]` is any Unicode letter.
#
# THREE ANTI-VACUITY GUARDS, because a scan that examined nothing must never
# read as a scan that passed:
#   1. it asserts it examined at least the floor in .github/inventory.json
#   2. a positive control it must catch on every invocation
#   3. a NEGATIVE control -- a line of mathematics and a citation it must NOT
#      flag -- so the exemption cannot silently widen into "match nothing"
#
# Binary files are skipped: there is no prose in a parquet fixture to fix.
#
#   usage: check-vocabulary.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

ALLOWLIST=".github/vocabulary-allowlist.txt"
MANIFEST=".github/inventory.json"
[ -f "$ALLOWLIST" ] || { echo "FAIL: no allowlist at $ALLOWLIST" >&2; exit 2; }
[ -f "$MANIFEST" ] || { echo "FAIL: no manifest at $MANIFEST" >&2; exit 2; }

python3 - "$ALLOWLIST" "$MANIFEST" <<'PY'
import json
import pathlib
import re
import sys

allowlist_path, manifest_path = sys.argv[1], sys.argv[2]

# Mathematics. Stripped from a line before the search.
ALLOWED = re.compile(
    r"R-hat|split-R|R\^2|R2D2|R2LOG|AD2R|R2|pseudo R|R\*beta|covariance R|"
    r"count of R|R1|Q/R|Q and R|adj_r_squared|r_squared|"
    # R_t is a correlation matrix at time t; Rank_M is the model-confidence-set
    # rank statistic. Both are notation.
    r"R_t|Rank_M|Rank_R|R_\{|"
    # `pkg::fn` and `foo::bar` are the GENERIC FORM the formula gate refuses,
    # named in its own error message and in the payload that proves it. They
    # are placeholders, not a real namespace.
    r"pkg::fn|foo::bar|"
    # AN AUTHOR'S INITIAL IS A PERSON'S NAME, NOT A LANGUAGE. The catalogue cites
    # Hyndman, R.J. · Tsay, R. · D'Agostino, R.B. · Nelson, C. R. · Pindyck, R.S.
    # Stripping the initial would misattribute real researchers' work, which is a
    # far worse defect than any residue this gate exists to catch.
    r"R\.[A-Z]\.|[A-Z]\.\s?R\.|,\s?R\.|\bR\.\s?(?=[0-9(])|\bR\.[A-Z]|&\s?R\.|\(R\)"
)

# Vocabulary borrowed from another ecosystem.
PATTERN = re.compile(
    r"\brenv\b|\bRscript\b|\btestthat\b|\broxygen\b|\bplumber\b|\.Rprofile|\.lintr|"
    r"install\.packages|\bR CMD\b|\bCRAN\b|[Rr]-project|[Rr]-lib\.org|"
    r"\bported from\b|\ba port of\b|engine/R/|\bWrappers/|"
    # a namespace call, but NOT a workflow command such as ::warning:: --
    # the lookbehind rejects a match that itself begins after a colon
    r"(?<![:\w])[A-Za-z][A-Za-z0-9._]*::[A-Za-z_.]|"
    r"\.R(?![A-Za-z0-9_])|"
    r"\bts_handle\b|\bmts_handle\b|\bzoo_handle\b|\br_version\b|"
    # UNICODE-AWARE. `[A-Za-z]` does not contain o-umlaut or e-acute, so a naive
    # class flags the R inside Roehmel and Renyi -- real mathematicians whose
    # names a purge must never touch. `[^\W\d_]` is any Unicode letter.
    r"(?<![^\W\d_])R(?![^\W\d_])"
)

SKIP_DIRS = (".git", ".venv", "__pycache__", ".mypy_cache", ".ruff_cache",
             ".pytest_cache", ".import_linter_cache", ".private", ".claude",
             ".fastembed_cache", ".token-optimizer")
SKIP_NAMES = ("todo.md", "CLAUDE.md")

exempt = [line.strip() for line in pathlib.Path(allowlist_path).read_text().splitlines()
          if line.strip() and not line.startswith("#")]


def is_exempt(rel: str) -> bool:
    return any(rel.startswith(e) for e in exempt)


def scan(text: str):
    for n, line in enumerate(text.splitlines(), 1):
        stripped = ALLOWED.sub("", line)
        if PATTERN.search(stripped):
            yield n, line


examined = 0
findings = []
for path in sorted(pathlib.Path(".").rglob("*")):
    if not path.is_file():
        continue
    rel = str(path)
    if any(part in SKIP_DIRS for part in path.parts) or path.name in SKIP_NAMES:
        continue
    if is_exempt(rel):
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue  # binary: no prose to fix
    examined += 1
    hits = list(scan(text))
    if hits:
        findings.append((rel, hits))

# --- anti-vacuity 1: the floor -------------------------------------------
floor = int(json.loads(pathlib.Path(manifest_path).read_text())
            .get("residue", {}).get("min_files_scanned", 0))
if floor <= 0:
    sys.exit("FAIL: no residue.min_files_scanned in the manifest; a floor of zero is not a floor.")
if examined < floor:
    sys.exit(f"FAIL: examined {examined} files, below the floor {floor}. "
             "The scan is wrong, not the tree.")

# --- anti-vacuity 2: the positive control --------------------------------
if not PATTERN.search(ALLOWED.sub("", "this was a port of an R module using renv")):
    sys.exit("FAIL: the positive control was NOT detected; the pattern is broken.")

# --- anti-vacuity 3: the negative control --------------------------------
# Pure mathematics must survive the exemption without being flagged. If this
# fires, the exemption has widened into "match nothing".
if PATTERN.search(ALLOWED.sub("", "the R-hat is 1.01, the pseudo R^2 is 0.8, and R*beta = q")):
    sys.exit("FAIL: the negative control was flagged; the mathematics exemption is broken.")

if findings:
    for rel, hits in findings:
        print(f"RESIDUE  {rel}")
        for n, line in hits[:5]:
            print(f"    {n}:{line.strip()[:150]}")
    total = sum(len(h) for _, h in findings)
    print()
    print(f"FAIL: foreign vocabulary appears {total} time(s) in {len(findings)} file(s), "
          f"examined {examined}.", file=sys.stderr)
    print("Either remove the mention, or -- if it is mathematics -- add it to the ALLOWED "
          "list in this script with the notation it stands for.", file=sys.stderr)
    sys.exit(1)

print(f"ok: the vocabulary is this project's own "
      f"(examined {examined} files, floor {floor}, both controls fired).")
PY
