#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Re-measure the engine and compare against .github/inventory.json.
#
# Kept as a real script rather than inline YAML deliberately: this is the gate
# every other gate depends on, and a script can be run and tested locally,
# exactly as it runs in continuous integration. Inline shell inside YAML cannot.
#
#   usage: assert.sh <engine-dir> <manifest-path>
set -euo pipefail

ENGINE_DIR="${1:-.}"
MANIFEST="${2:-.github/inventory.json}"

# A GATE THAT CANNOT START MUST NOT LOOK LIKE A GATE THAT PASSED.
# This script is the anti-vacuity backstop every other gate depends on, and it is
# driven by python3. Without this check a missing interpreter surfaces as a bare
# "python3: command not found" from inside a command substitution -- which reads
# like a missing file, not like an unmet requirement. Fail loudly and name it.
# Minimum is documented in docs/decisions/python-engine.md; only the standard
# library is used, so any supported CPython satisfies it.
if ! command -v python3 >/dev/null 2>&1; then
  echo "FAIL: python3 is REQUIRED by this gate and was not found on PATH." >&2
  echo "      assert-inventory reads .github/inventory.json with python3 and" >&2
  echo "      cannot verify a single constant without it. This is an unmet" >&2
  echo "      requirement, NOT a passing check." >&2
  echo "      See docs/decisions/python-engine.md." >&2
  exit 1
fi

MANIFEST_ABS="$(cd "$(dirname "$MANIFEST")" && pwd)/$(basename "$MANIFEST")"
cd "$ENGINE_DIR"

# Read every expected value in ONE pass and expose them as EXP_* variables.
# A single read means the manifest cannot be half-applied if it is malformed.
eval "$(python3 - "$MANIFEST_ABS" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
flat = {}
for section in ("engine", "spdx", "artifacts", "suite"):
    for k, v in d.get(section, {}).items():
        if not k.startswith("_"):
            flat[k] = v
for k, v in flat.items():
    print('EXP_%s=%s' % (k.upper(), json.dumps(str(v))))
PY
)"

fail=0
check() { # check <label> <expected> <actual>
  if [ "$2" = "unmeasured" ]; then
    printf '  OWED  %-24s no measurable artifact in the tree yet\n' "$1"
    fail=1
    return
  fi
  if [ "$2" = "$3" ]; then
    printf '  ok    %-24s %s\n' "$1" "$3"
  else
    printf '  FAIL  %-24s expected %s, measured %s\n' "$1" "$2" "$3"
    fail=1
  fi
}

# Read one field out of a committed artifact by EXPLICIT DOTTED PATH.
#
# python3 rather than the old `tr ',' '\n' | grep -m1 <key>` pipeline, for two
# reasons. That pipeline matched the first occurrence of a SUBSTRING anywhere in
# a 2.7 MB file, so any node whose text happened to contain the key could answer
# for the header. And it concealed the real shape of these documents: n_nodes is
# not top level, it sits under `engine`, and n_cards sits under `source`. A path
# that does not resolve raises here instead of quietly yielding a wrong number.
afield() { # afield <file> <dotted.path>
  python3 -c 'import json,sys,functools;print(functools.reduce(lambda d,k: d[k], sys.argv[2].split("."), json.load(open(sys.argv[1]))))' "$1" "$2"
}

# COUNT .py FILES WITH find, NEVER WITH `grep -r --include`.
# Measured on a maintainer machine: `grep` resolves to ugrep 7.5.0, whose
# --include reported 315 of 379 files where GNU grep reported 379. CI runners
# ship GNU grep, so a gate written that way UNDERCOUNTS silently on that host
# and passes here -- the failure direction CONTRIBUTING.md forbids.
py_count() { find "$@" -name '*.py' -not -path '*__pycache__*' | wc -l | tr -d ' '; }

echo "== engine inventory =="
check wrappers        "$EXP_WRAPPERS" \
  "$(find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' | wc -l | tr -d ' ')"
check categories      "$EXP_CATEGORIES" \
  "$(find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' | wc -l | tr -d ' ')"
# methods is READ FROM THE ARTIFACT, not grepped out of source. Historically
# engine it was grepped from the spec sources; the specs are generated now, so
# the artifact is upstream of the code rather than downstream of it. Grepping
# the generated tier would only prove the generator ran.
check methods         "$EXP_METHODS"         "$(afield artifacts/node-specs.v1.json engine.n_nodes)"
# generators is asserted so that artifact-drift's `ran != N` floor has a single
# reviewed home. Adding a generator is a one-line bump here, and the drift job
# then expects it -- rather than the floor and the loop drifting apart in silence.
check generators      "$EXP_GENERATORS" \
  "$(find scripts -maxdepth 1 -name '*.py' -type f | wc -l | tr -d ' ')"
check infra_py_files  "$EXP_INFRA_PY_FILES" \
  "$(find src -name '*.py' -not -path '*__pycache__*' \
       -not -path 'src/econflow_engine/wrappers/*' \
       -not -path 'src/econflow_engine/generated/*' | wc -l | tr -d ' ')"
check test_files      "$EXP_TEST_FILES" \
  "$(find tests -name 'test_*.py' -not -path '*__pycache__*' | wc -l | tr -d ' ')"
check test_helpers    "$EXP_TEST_HELPERS" \
  "$(find tests -maxdepth 1 -name 'conftest.py' | wc -l | tr -d ' ')"
check python_version  "$EXP_PYTHON_VERSION"  "$(tr -d ' \n' < .python-version)"

# THE PROGRESS LEDGER. Every wrapper body is a generated stub until somebody
# writes one, and nothing else in this manifest distinguishes a catalogue of 913
# METHODS from a catalogue of 913 STUBS. This walks the syntax tree and counts
# the node functions whose body is NOT the emitted raise, so the figure cannot
# be talked up in prose. It lives here rather than in engine/scripts/ because
# that directory's file count IS the `generators` constant asserted above.
check n_implemented   "$EXP_N_IMPLEMENTED" "$(python3 - <<'AST'
import ast, pathlib
written = 0
for path in sorted(pathlib.Path("src/econflow_engine/wrappers").rglob("*.py")):
    if path.name == "__init__.py":
        continue
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if node.name.startswith("_"):
            continue
        body = [s for s in node.body
                if not (isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant)
                        and isinstance(s.value.value, str))]
        exc = body[0].exc if (len(body) == 1 and isinstance(body[0], ast.Raise)) else None
        name = getattr(exc, "func", exc)
        if not (isinstance(name, ast.Name) and name.id == "NotImplementedError"):
            written += 1
print(written)
AST
)"

# THE LOCKFILE IS AT THE WORKSPACE ROOT, NOT IN THIS DIRECTORY.
# engine/ and backend/ are the two members of ONE uv workspace, so there is one
# uv.lock and it sits beside the root pyproject.toml. A member never carries its
# own lock; if one appears here, the workspace has been split by accident and the
# two members can drift onto different pydantic/pyarrow builds.
if [ -f uv.lock ]; then
  echo "  FAIL  engine/uv.lock exists; the workspace lock belongs at the repository root"
  fail=1
fi
if [ -f ../uv.lock ]; then
  check py_packages "$EXP_PY_PACKAGES" \
    "$(python3 -c "import tomllib;print(len(tomllib.load(open('../uv.lock','rb'))['package']))")"
else
  echo "  OWED  py_packages              no uv.lock at the repository root"
  fail=1
fi

echo "== committed artifacts =="
check n_nodes              "$EXP_N_NODES"              "$(afield artifacts/node-specs.v1.json engine.n_nodes)"
check n_categories         "$EXP_N_CATEGORIES"         "$(afield artifacts/node-specs.v1.json engine.n_categories)"
check n_cards              "$EXP_N_CARDS"              "$(afield artifacts/method-cards.v1.json source.n_cards)"
check n_parity_cases       "$EXP_N_PARITY_CASES"       "$(afield artifacts/parity-fixtures.v1.json n_cases)"
check n_recommend_fixtures "$EXP_N_RECOMMEND_FIXTURES" "$(afield artifacts/recommend-fixtures.v1.json source.n_fixtures)"
check sbom_components      "$EXP_SBOM_COMPONENTS" \
  "$(python3 -c "import json;print(len(json.load(open('sbom.cdx.json'))['components']))" 2>/dev/null || echo "no-sbom")"

echo "== SPDX coverage =="
check py_files_total       "$EXP_PY_FILES_TOTAL"       "$(py_count src scripts tests)"
check py_files_with_header "$EXP_PY_FILES_WITH_HEADER" \
  "$(find src scripts tests -name '*.py' -not -path '*__pycache__*' -print0 \
     | xargs -0 grep -l 'SPDX-License-Identifier' | wc -l | tr -d ' ')"

echo "== artifact sidecar integrity =="
sidecars=0
for s in artifacts/*.sha256; do
  [ -e "$s" ] || continue
  base="${s%.sha256}.json"
  exp="$(awk '{print $1}' "$s")"
  act="$(sha256sum "$base" | awk '{print $1}')"
  if [ "$exp" = "$act" ]; then
    printf '  ok    sidecar %s\n' "$(basename "$base")"
    sidecars=$((sidecars + 1))
  else
    printf '  FAIL  sidecar %s drifted\n' "$(basename "$base")"
    fail=1
  fi
done
# Anti-vacuity on the loop itself: a glob matching nothing would otherwise
# "verify" every sidecar without having checked one. EXACT, not a floor: a floor
# of four would accept two artifacts silently losing their seals, which is
# precisely the accident it exists to catch.
check sidecars "$EXP_SIDECARS" "$sidecars"

if [ "$fail" -ne 0 ]; then
  cat <<'MSG'

Inventory assertion FAILED.

A line marked OWED is a constant this manifest cannot yet measure, because the
artifact that answers for it is not in the tree. It is deliberately red: an
unmeasurable constant must never read as a verified one. Land the artifact, run
the command from the "commands" block, and replace the word with the figure.

A line marked FAIL is a real disagreement. If the change was intentional, re-run
the relevant command from the "commands" block of .github/inventory.json and
update the number there in its own commit, so that the change is reviewed rather
than silently absorbed.
MSG
  exit 1
fi

echo
echo "Inventory verified."
