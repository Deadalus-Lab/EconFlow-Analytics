#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# ==============================================================================
# run_verifications.sh — the correctness gate for the compute engine.
#
# It is also a BUILD gate: the container runs it during the image build, so an
# image that has not proven itself cannot exist. Keep it that way. A gate that
# can be skipped is a gate that will be.
#
# Run from `engine/`. Exit 0 = everything passed; anything else = do not ship.
#
# EVERY STEP HERE ASSERTS A FLOOR. A check that examines nothing must never read
# as a check that passed — that is the failure mode this whole file exists to
# make impossible, and the one the `spdx` job came closest to hitting.
# ==============================================================================
set -euo pipefail

cd "$(dirname "$0")"
ROOT="$(cd .. && pwd)"

# Thread pinning. Determinism is bought with the thread count:
# the nondeterminism mechanism was never the library, it was the reduction order
# across threads. NumPy/SciPy ship OpenBLAS with no netlib equivalent worth
# building, so determinism is bought with the thread count instead — and, unlike
# the distro BLAS, the wheel's OpenBLAS build is hash-pinned in ../uv.lock.
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export PYTHONHASHSEED=0
# TIME ZONE AND LOCALE, for the same reason and with the same status as the
# thread counts. A date rendered through the machine's local zone and a string
# sorted through the machine's collation are both machine-dependent inputs to
# committed bytes. Measured before setting them: all four generators reproduce
# byte for byte under TZ=UTC and under TZ=Pacific/Kiritimati, so the artifacts do
# not depend on either today -- which is precisely when to pin them, before
# something starts depending on them by accident.
export TZ=UTC
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

RUN="uv run --project ${ROOT}"
command -v uv >/dev/null 2>&1 || {
  echo "FAIL: uv is not on PATH. This engine is a member of the workspace at ${ROOT}." >&2
  exit 1
}

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

# Every asserted quantity in this file comes from ../.github/inventory.json and
# from nowhere else, so that weakening one is a visible one-line diff in the
# manifest rather than an edit buried in a shell script.
#
# NO except-and-print-zero HERE. Swallowing the error is what made the collected
# floor vacuous inside the image for its whole existence: .dockerignore excluded
# .github/, the read raised, the floor became 0, the comparison was skipped and
# the step still printed a cheerful "collected N (floor 0)".
inventory() {
  python3 - "$1" "$2" <<'PY'
import json, pathlib, sys
inv = pathlib.Path("../.github/inventory.json")
section, key = sys.argv[1], sys.argv[2]
try:
    print(int(json.loads(inv.read_text())[section][key]))
except Exception as exc:
    sys.exit(f"cannot read {section}.{key} from {inv}: {exc}")
PY
}

echo "== 1. the generated tier reproduces from the frozen artifacts =="
$RUN python scripts/gen_schemas.py --check || fail "generated schemas drifted from node-specs.json"
# THE MESSAGE NAMES ONLY WHAT run_check READS. It asserts two things and no
# others: every module the plan names exists and parses, and every stub signature
# equals the one node-specs.json specifies. It compares no Markdown -- there is
# none under wrappers/ and the generator emits none, so a failure message
# promising documentation coverage promised a check that cannot exist.
$RUN python scripts/gen_wrappers.py --check ||
  fail "a wrapper module is missing, or a stub signature differs from node-specs.json; regenerate with scripts/gen_wrappers.py --write"

echo "== 2. static analysis =="
$RUN ruff check src scripts tests api-baseline || fail "ruff"
$RUN mypy || fail "mypy --strict"

# THE SECOND TYPE CHECKER, and the file count is what makes it a check. pyright
# reports "0 errors" just as cheerfully over an empty include glob as over the
# whole engine, and [tool.pyright] in pyproject.toml is one typo away from
# exactly that. The floor is the wrapper count from the manifest: losing the
# wrapper tier from the include drops the figure from 765 files to 120 and turns
# this red, which is the mistake worth catching. Both numbers were measured on
# 2026-08-21 by running pyright against a config with, and without, the wrapper
# tree in `include`.
pyright_report="$($RUN pyright --outputjson --level error)" || {
  printf '%s\n' "$pyright_report" >&2
  fail "pyright"
}
pyright_files="$(printf '%s' "$pyright_report" | python3 -c \
  'import json,sys; print(json.load(sys.stdin)["summary"]["filesAnalyzed"])')" ||
  fail "pyright produced no parseable summary"
pyright_floor="$(inventory engine wrappers)" || fail "the pyright floor is unreadable"
[ "$pyright_files" -ge "$pyright_floor" ] ||
  fail "pyright analysed ${pyright_files} files, below the floor ${pyright_floor}; the include glob is wrong, not the tree"
echo "   pyright: 0 errors over ${pyright_files} files (floor ${pyright_floor})"

echo "== 3. the architectural boundary =="
# Both layers are Python, so nothing answers "is this the engine?" for free.
# See [tool.importlinter] in ../pyproject.toml.
$RUN lint-imports --config "${ROOT}/pyproject.toml" || fail "an import contract is broken"

echo "== 4. the suite =="
# NOT `-q`. pytest-randomly prints "Using --randomly-seed=N" in the header, and
# -q removes the header: a reproducer for an order-dependent failure would be
# generated on every run and shown on none of them.
$RUN pytest

echo "== 5. anti-vacuity: the suite actually collected something =="
collected="$($RUN pytest -q --collect-only 2>/dev/null | grep -c '::' || true)"
floor="$(inventory suite min_tests)" ||
  fail "the anti-vacuity floor is unreadable; the manifest must travel with the suite"
[ -n "$collected" ] && [ "$collected" -gt 0 ] || fail "pytest collected 0 tests; the paths are wrong, not the code"
if [ "$floor" -gt 0 ] && [ "$collected" -lt "$floor" ]; then
  fail "pytest collected ${collected}, below the floor ${floor} in .github/inventory.json"
fi
echo "   collected ${collected} (floor ${floor})"

echo "== 6. every import is declared, and every declaration is imported =="
# The failure this catches only ever appears on a machine that has never run
# anything else: an import satisfied by a package that happens to be in the
# environment as somebody else's transitive dependency works perfectly until a
# clean install, and then fails at import time rather than in any test. It found
# exactly that here -- kinds.py imports annotated_types, which arrived only
# because pydantic needs it.
#
# deptry reads the [project] table beside it, so it has to be run INSIDE each
# member: `deptry engine` from the root exits with
# DependencySpecificationNotFoundError rather than checking anything.
deptry_report="$($RUN deptry . 2>&1)" || {
  printf '%s\n' "$deptry_report" >&2
  fail "deptry (engine)"
}
deptry_files="$(printf '%s' "$deptry_report" | sed -n 's/^Scanning \([0-9]*\) file.*/\1/p')"
deptry_floor="$(inventory engine wrappers)" || fail "the deptry floor is unreadable"
[ -n "$deptry_files" ] && [ "$deptry_files" -ge "$deptry_floor" ] ||
  fail "deptry scanned '${deptry_files:-no}' files in engine/, below the floor ${deptry_floor}"
echo "   engine: no dependency issues over ${deptry_files} files (floor ${deptry_floor})"
# The backend is one module today, so there is no honest floor to assert on it
# beyond "it ran at all" -- which is what the exit status already says.
(cd "${ROOT}/backend" && $RUN deptry .) || fail "deptry (backend)"
echo "   backend: no dependency issues"

echo "== 7. every wrapper is documented =="
# gen_wrappers.py writes a docstring for every documentable object under
# wrappers/ from the node spec, so the floor is 100 % and this reads as trivially
# true today. It stops being trivial with the first hand-written body that
# replaces a generated docstring with nothing.
#
# `-c pyproject.toml` IS LOAD-BEARING, not tidiness. interrogate looks for its
# configuration by walking up from the TARGET PATH, not from the working
# directory: measured against a copy of the wrapper tree outside engine/, it
# found no [tool.interrogate], fell back to its OWN default floor of 80 % and
# reported PASSED at 99.9 %. A gate that silently swaps in a weaker threshold is
# the failure this whole file exists to prevent, so the floor is named here and
# the run is checked below for having actually used it.
interrogate_report="$($RUN interrogate -c pyproject.toml -v src/econflow_engine/wrappers)" ||
  {
    printf '%s\n' "$interrogate_report" >&2
    fail "docstring coverage below the floor in [tool.interrogate]"
  }
# THE MISSED COUNT IS THE ASSERTION, AND THE PERCENTAGE IS NOT. MEASURED.
# interrogate's TOTAL row is `| total | missed | covered | percent |`, and the
# percentage is ROUNDED TO ONE DECIMAL before it is compared with fail-under. At
# 2101 documentable objects one missing docstring is 99.952 %, which prints as
# `100.0%` and is reported `RESULT: PASSED (minimum: 100.0%, actual: 100.0%)`.
# Exactly the case this gate exists for -- a hand-written body arriving with the
# generated docstring deleted -- therefore passed, and the count floor below could
# not see it either, because that column is the TOTAL (2101) and not the covered
# one. Asserting `missed == 0` is exact and does not round.
#
# Reproduce: delete one node docstring under wrappers/ and run interrogate -v.
missed="$(printf '%s' "$interrogate_report" | sed -n 's/^| TOTAL *| *[0-9]* *| *\([0-9]*\) .*/\1/p')"
[ -n "$missed" ] ||
  fail "interrogate printed no TOTAL row; its output format changed and this gate is not reading it"
[ "$missed" -eq 0 ] ||
  fail "${missed} documentable object(s) under wrappers/ carry no docstring"
documented="$(printf '%s' "$interrogate_report" | sed -n 's/^| TOTAL *| *\([0-9]*\) .*/\1/p')"
documented_floor="$(inventory engine methods)" || fail "the docstring floor is unreadable"
[ -n "$documented" ] && [ "$documented" -ge "$documented_floor" ] ||
  fail "interrogate examined '${documented:-no}' objects, below the floor ${documented_floor}; it did not see the wrapper tier"
# THE PERCENTAGE IS ASSERTED FROM THE MANIFEST, not from interrogate's own output.
# Grepping the printed 'minimum: 100.0%' proved only that the run used 100 -- it
# could not notice [tool.interrogate] being lowered, because the report would then
# truthfully print the lower number and the grep would simply stop matching, which
# reads as a broken gate rather than a weakened one. Reading BOTH and comparing
# them makes lowering the floor a visible one-line diff in .github/inventory.json,
# which is where every asserted constant in this repository lives.
percent_declared="$($RUN python -c \
  "import tomllib;print(tomllib.load(open('pyproject.toml','rb'))['tool']['interrogate']['fail-under'])")" ||
  fail "[tool.interrogate] declares no fail-under"
percent_floor="$(inventory engine docstring_coverage_percent)" ||
  fail "the docstring percentage floor is unreadable"
[ "$percent_declared" = "$percent_floor" ] ||
  fail "[tool.interrogate] fail-under is ${percent_declared}, the manifest says ${percent_floor}"
printf '%s' "$interrogate_report" | grep -q "minimum: ${percent_floor}\.0%" ||
  fail "interrogate ran against a floor other than ${percent_floor} %; it did not read [tool.interrogate]"
echo "   ${documented} documentable objects, ${missed} missing (floor ${documented_floor}, at ${percent_floor} %)"

echo "== 8. the public API still matches its committed baseline =="
# A saved graph names a node's arguments. Renaming one breaks every graph that
# used it and breaks no test, because the stub raises NotImplementedError under
# either name. See api-baseline/check_api.py for why this is not `griffe check`.
$RUN python api-baseline/check_api.py || fail "the wrapper API drifted from api-baseline/wrappers.json"

echo "== 9. no wrapper reaches the network =="
# Published in five places and called "Verified", with nothing re-measuring it
# until 2026-08-21. The figure quoted was taken by hand when the tree held 251
# wrapper modules and was never taken again while the tree more than doubled.
# A claim without a gate is a memory.
bash ../.github/scripts/check-no-network.sh .. ||
  fail "a wrapper reaches the network; fetching belongs to the external-data node"

echo "== 10. running a method twice returns the same bytes =="
# BOX 2.1.14. Zero methods qualify today -- engine.n_implemented is 0 and every
# wrapper body is a typed stub that raises -- so a harness that iterated the
# implemented set and printed "all match" would have examined NOTHING. The proof
# is therefore carried by planted controls: three that MUST be caught (the wall
# clock, a live object's address, an unseeded draw) and two that MUST NOT be (a
# constant, and a draw from a generator seeded inside the call). Both counts are
# printed, and the method count is compared EXACTLY against the manifest so it
# rises on its own with the first body in 2.2.
$RUN python -m tests.controls.double_run ||
  fail "the double-run determinism harness failed; a method or a planted control did not reproduce"

echo "== 11. doctests, counted rather than exit-coded =="
# BOX 2.1.18. `pytest --doctest-modules` over a tree with no examples collects
# zero and EXITS 0 -- green, having run nothing. Wired in as
# `pytest --doctest-modules src/ || fail` it would be a gate that can never fail
# over 1456 modules. This asserts the COLLECTED COUNT instead, with a wrapper
# floor that reads engine.n_implemented, and proves itself on three controls: a
# deliberately wrong example that MUST fail, a correct one that MUST pass, and a
# prose-only docstring that must collect 0 without erroring.
$RUN python -m tests.controls.doctest_gate ||
  fail "the doctest gate failed; see the collected counts above"

echo "== 11b. a published table reaches the body it is delivered to =="
# BOX 2.1.1.4. A `{"$fixture": "<name>"}` value in an oracle case builds a
# published table and delivers it through registry_put -> adapt_args ->
# resolve_handle. Nothing about a green case proves the body READ it: a body
# returning a constant passes any comparison whose expected value happens to
# match. Every wrapper body is a stub, so no real body can be watched reading a
# dataset either -- the proof is carried by four planted controls driven down
# the real path against a real node's contract. Two MUST be flagged (a constant,
# and a payload that reads only the frame's length) and two MUST NOT (a sum over
# the values, and a payload that declares no dependence on them).
$RUN python -m tests.controls.fixture_reach ||
  fail "the fixture-reach harness failed; a planted control reached the wrong verdict"

echo "== 12. the planted control sets are the size the manifest claims =="
# The counts are EXACT, not floors. A harness quietly left with fewer controls
# than it claims is indistinguishable from one that has stopped proving itself,
# and both of the harnesses above are only as good as their controls. Deleting
# one is therefore a visible one-line diff in .github/inventory.json.
for pair in "determinism_controls:determinism.py" "property_controls:property_controls.py" \
  "fixture_controls:fixture_reach.py"; do
  key="${pair%%:*}"
  module="tests/controls/${pair#*:}"
  planted="$(grep -cE '"""(POSITIVE|NEGATIVE)\.' "$module" || true)"
  expected="$(inventory suite "$key")" || fail "the ${key} floor is unreadable"
  [ "$planted" -eq "$expected" ] ||
    fail "${module} plants ${planted} control(s), the manifest says ${expected}"
  echo "   ${module}: ${planted} planted control(s)"
done

echo "== 13. every inventory constant still measures what the manifest claims =="
# THE GATE THE OTHER GATES DEPEND ON, and until now it ran only in continuous
# integration -- so a contributor could see this suite green while every published
# figure had moved. It is offline, it re-measures rather than trusts, and it is
# fast, so there is no reason it was not here.
bash ../.github/actions/assert-inventory/assert.sh . ../.github/inventory.json ||
  fail "an inventory constant no longer measures what .github/inventory.json claims"

echo
echo "All verifications passed."
echo
echo "NOTE: this suite does NOT check documentation. Spelling, Markdown structure,"
echo "      the prose register, links and whether a published figure is still TRUE"
echo "      are covered by .github/scripts/run-doc-gates.sh, which needs four"
echo "      tools this suite deliberately does not depend on."
