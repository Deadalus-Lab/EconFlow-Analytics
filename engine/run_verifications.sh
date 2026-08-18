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

RUN="uv run --project ${ROOT}"
command -v uv >/dev/null 2>&1 || {
    echo "FAIL: uv is not on PATH. This engine is a member of the workspace at ${ROOT}." >&2
    exit 1
}

fail() { echo "FAIL: $*" >&2; exit 1; }

echo "== 1. the generated tier reproduces from the frozen artifacts =="
$RUN python scripts/gen_schemas.py --check  || fail "generated schemas drifted from node-specs.v1.json"
$RUN python scripts/gen_wrappers.py --check || fail "wrapper stubs or category guides drifted"

echo "== 2. static analysis =="
$RUN ruff check src scripts tests            || fail "ruff"
$RUN mypy                                    || fail "mypy --strict"

echo "== 3. the architectural boundary =="
# Both layers are Python, so nothing answers "is this the engine?" for free.
# See [tool.importlinter] in ../pyproject.toml.
$RUN lint-imports --config "${ROOT}/pyproject.toml" || fail "an import contract is broken"

echo "== 4. the suite =="
$RUN pytest -q

echo "== 5. anti-vacuity: the suite actually collected something =="
collected="$($RUN pytest -q --collect-only 2>/dev/null | grep -c '::' || true)"
floor="$(python3 - <<'PY'
import json, pathlib, sys
inv = pathlib.Path("../.github/inventory.json")
# NO except-and-print-zero HERE. Swallowing the error is what made this gate
# vacuous inside the image for its whole existence: .dockerignore excluded
# .github/, the read raised, the floor became 0, the comparison was skipped and
# the step still printed a cheerful "collected N (floor 0)".
try:
    print(int(json.loads(inv.read_text())["suite"]["min_tests"]))
except Exception as exc:
    sys.exit(f"cannot read the test floor from {inv}: {exc}")
PY
)" || fail "the anti-vacuity floor is unreadable; the manifest must travel with the suite"
[ -n "$collected" ] && [ "$collected" -gt 0 ] || fail "pytest collected 0 tests; the paths are wrong, not the code"
if [ "$floor" -gt 0 ] && [ "$collected" -lt "$floor" ]; then
    fail "pytest collected ${collected}, below the floor ${floor} in .github/inventory.json"
fi
echo "   collected ${collected} (floor ${floor})"

echo
echo "All verifications passed."
