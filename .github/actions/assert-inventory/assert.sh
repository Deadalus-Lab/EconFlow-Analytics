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
# Only the standard library is used, and `tomllib` sets the floor at 3.11, so any
# interpreter at or above the version pinned in .python-version satisfies this.
if ! command -v python3 >/dev/null 2>&1; then
  echo "FAIL: python3 is REQUIRED by this gate and was not found on PATH." >&2
  echo "      assert-inventory reads .github/inventory.json with python3 and" >&2
  echo "      cannot verify a single constant without it. This is an unmet" >&2
  echo "      requirement, NOT a passing check." >&2
  echo "      WHAT IT REQUIRES: a CPython reachable as python3. This gate imports" >&2
  echo "      only the standard library, and tomllib puts the floor at 3.11." >&2
  echo "      engine/.python-version pins the version this tree is built against." >&2
  echo "      TO SATISFY IT: install that interpreter, put it on PATH, and run" >&2
  echo "      this script again." >&2
  exit 1
fi

MANIFEST_ABS="$(cd "$(dirname "$MANIFEST")" && pwd)/$(basename "$MANIFEST")"
cd "$ENGINE_DIR"

# Read every expected value in ONE pass and expose them as EXP_* variables.
# A single read means the manifest cannot be half-applied if it is malformed.
eval "$(
  python3 - "$MANIFEST_ABS" <<'PY'
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
# and passes here. A gate must never fail in the quiet direction: if it cannot
# examine what it claims to, it reports red, never a smaller number.
py_count() { find "$@" -name '*.py' -not -path '*__pycache__*' | wc -l | tr -d ' '; }

echo "== engine inventory =="
check wrappers "$EXP_WRAPPERS" \
  "$(find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' | wc -l | tr -d ' ')"
check categories "$EXP_CATEGORIES" \
  "$(find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' | wc -l | tr -d ' ')"
# methods is READ FROM THE ARTIFACT, not grepped out of source. Historically
# engine it was grepped from the spec sources; the specs are generated now, so
# the artifact is upstream of the code rather than downstream of it. Grepping
# the generated tier would only prove the generator ran.
check methods "$EXP_METHODS" "$(afield artifacts/node-specs.json engine.n_nodes)"
# generators is asserted so that artifact-drift's `ran != N` floor has a single
# reviewed home. Adding a generator is a one-line bump here, and the drift job
# then expects it -- rather than the floor and the loop drifting apart in silence.
#
# `gen_*.py`, NOT every file in scripts/. contract_hash.py lives beside them and
# is not a generator -- it takes a required `artifact` positional and computes a
# hash, and it has no committed output to drift against. Counting it made this
# constant 5 while artifact-drift's loop ran 4, and that comparison is exact, so
# the job was red before it had ever run on a runner. The glob here and the loop
# in ci.yml now describe the same set.
check generators "$EXP_GENERATORS" \
  "$(find scripts -maxdepth 1 -name 'gen_*.py' -type f | wc -l | tr -d ' ')"
check infra_py_files "$EXP_INFRA_PY_FILES" \
  "$(find src -name '*.py' -not -path '*__pycache__*' \
    -not -path 'src/econflow_engine/wrappers/*' \
    -not -path 'src/econflow_engine/generated/*' | wc -l | tr -d ' ')"
check test_files "$EXP_TEST_FILES" \
  "$(find tests -name 'test_*.py' -not -path '*__pycache__*' | wc -l | tr -d ' ')"
check test_helpers "$EXP_TEST_HELPERS" \
  "$(find tests -maxdepth 1 -name 'conftest.py' | wc -l | tr -d ' ')"
check python_version "$EXP_PYTHON_VERSION" "$(tr -d ' \n' <.python-version)"

# THE PROGRESS LEDGER. Every wrapper body is a generated stub until somebody
# writes one, and nothing else in this manifest distinguishes a catalogue of 913
# METHODS from a catalogue of 913 STUBS. This walks the syntax tree and counts
# the node functions whose body is NOT the emitted raise, so the figure cannot
# be talked up in prose. It lives here rather than in engine/scripts/ because
# that directory's file count IS the `generators` constant asserted above.
#
# ONE WALK, THREE ANSWERS, AND THAT IS DELIBERATE. It prints the implemented
# count, the stub count and the names of the implemented functions, because the
# payload sentinel below spends all three. A second walk written beside this one
# would be free to disagree with it in silence -- which is exactly what README.md
# did while it carried its own spelling of this definition, and the disagreement
# was found by measuring the two against a planted stub rather than by reading
# them. There is one definition of an implemented body in this repository.
ledger="$(
  python3 - <<'AST'
import ast, pathlib
written, stubs, names = 0, 0, []
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
        if isinstance(name, ast.Name) and name.id == "NotImplementedError":
            stubs += 1
        else:
            written += 1
            names.append(node.name)
print(written, stubs, ",".join(sorted(names)[:5]) or "-")
AST
)"
read -r measured_written measured_stubs measured_names <<EOF
$ledger
EOF
# A WALK THAT RETURNED SOMETHING OTHER THAN TWO COUNTS HAS NOT MEASURED THE TREE.
# Without this the two counts arrive empty, every later comparison silently reads
# as a string mismatch, and the premise below would be evaluated on nothing.
case "$measured_written:$measured_stubs" in
  *[!0-9]*:* | *:*[!0-9]*)
    echo "  FAIL  n_implemented            the wrapper walk returned '${ledger}', not two counts"
    fail=1
    measured_written=-1
    measured_stubs=-1
    ;;
esac
check n_implemented "$EXP_N_IMPLEMENTED" "$measured_written"

# THE ARGUMENTS A METHOD IS RUN WITH, WHICH THIS DIRECTORY IS ONE OF TWO SOURCES
# OF. The double-run gate hashes a method's output twice, and it cannot call one
# without arguments. parity-fixtures.json holds argument-adapter verdicts and
# node-specs.json holds argument kinds; neither is a call. Two things in the tree
# ARE: a file under engine/tests/payloads/, which this constant counts, and an
# admissible oracle case under engine/tests/oracle/, which it does not -- the
# gate takes the union and this figure measures one half of it. That is why the
# checks below are worded as a premise about bodies rather than as a claim that
# no method can be run. This constant reads "unmeasured" and therefore OWED,
# deliberately: the directory below does not exist, so the count does not come
# back zero -- it comes back not at all, which is the difference between a
# measurement and the absence of one. The shape of a payload, where it goes and
# what produces it are written down in engine/tests/controls/double_run.py, so
# that the first body author in 2.2 reads the contract rather than inventing one
# against a red gate. NOT a bare `find` with its error swallowed: a missing tree
# must say so in the report, exactly as the absent lockfile and the absent SBOM
# do below.
#
# THE WORD IS CONDITIONAL ON A PREMISE THIS SCRIPT MEASURES, AND THE LINE STAYS.
# A hard failure needed no premise: it could only ever be cleared by landing the
# artifact. Green resting on a counter is a weaker thing, so the counter is
# fenced on both sides. The OWED line is printed in every one of these branches
# -- its visibility is the point, and only the exit code follows the premise.
#
#   the two counts must account for the whole catalogue -- a walk that stopped
#     finding wrapper files would otherwise report an empty implemented set, and
#     the premise would read true for the worst reason available;
#   no method may carry a body -- an empty implemented set is the one state in
#     which the absent payload tree provably costs nothing, because there is
#     nothing for either half of the union to be missing a call for.
if [ "$EXP_INVOCATION_PAYLOADS" = "unmeasured" ] && [ ! -d tests/payloads ]; then
  measured_catalogue=$((measured_written + measured_stubs))
  if [ "$measured_catalogue" != "$EXP_METHODS" ]; then
    printf '  FAIL  %-24s %s implemented + %s stub = %s, manifest counts %s methods\n' \
      invocation_payloads "$measured_written" "$measured_stubs" \
      "$measured_catalogue" "$EXP_METHODS"
    echo "        The wrapper walk did not see the whole catalogue, so it cannot answer"
    echo "        for the implemented set this marker's premise rests on."
    fail=1
  elif [ "$measured_written" -ne 0 ]; then
    printf '  FAIL  %-24s %s method(s) carry a body: %s\n' \
      invocation_payloads "$measured_written" "$measured_names"
    echo "        A body may already be double-run: the gate reaches one through an"
    echo "        admissible oracle case as well as through engine/tests/payloads/,"
    echo "        and it refuses to go green while skipping any implemented method."
    echo "        What is stale here is the WORD, whose premise was that no method"
    echo "        carries a body. Retire it in its own reviewed diff: land the"
    echo "        payload of any body that has no oracle case, then replace"
    echo "        engine.invocation_payloads with the count its command returns."
    fail=1
  else
    printf '  OWED  %-24s no measurable artifact in the tree yet\n' invocation_payloads
    printf '        premise holds: 0 of %s methods carry a body\n' "$EXP_METHODS"
  fi
elif [ -d tests/payloads ]; then
  check invocation_payloads "$EXP_INVOCATION_PAYLOADS" \
    "$(find tests/payloads -name '*.json' -not -name '_*' | wc -l | tr -d ' ')"
else
  check invocation_payloads "$EXP_INVOCATION_PAYLOADS" "no-payload-tree"
fi

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
check n_nodes "$EXP_N_NODES" "$(afield artifacts/node-specs.json engine.n_nodes)"
check n_categories "$EXP_N_CATEGORIES" "$(afield artifacts/node-specs.json engine.n_categories)"
check n_cards "$EXP_N_CARDS" "$(afield artifacts/method-cards.json source.n_cards)"
check n_parity_cases "$EXP_N_PARITY_CASES" "$(afield artifacts/parity-fixtures.json n_cases)"
check n_recommend_fixtures "$EXP_N_RECOMMEND_FIXTURES" "$(afield artifacts/recommend-fixtures.json source.n_fixtures)"
# THE CONTINUITY PAIR. The counts above measure the live catalogue and move when
# it grows. These two describe the contract retired on 2026-08-21 and must never
# move: a continuity constant that drifts was never one. They are read from
# legacy-inventory.json, which is the only place the retired contract still
# exists, and gen_artifacts.py --continuity asserts the catalogue still contains
# every entry they count.
check n_legacy_nodes "$EXP_N_LEGACY_NODES" "$(afield artifacts/legacy-inventory.json n_nodes)"
check n_legacy_cards "$EXP_N_LEGACY_CARDS" "$(afield artifacts/legacy-inventory.json n_cards)"
check sbom_components "$EXP_SBOM_COMPONENTS" \
  "$(python3 -c "import json;print(len(json.load(open('sbom.cdx.json'))['components']))" 2>/dev/null || echo "no-sbom")"

echo "== SPDX coverage =="
check py_files_total "$EXP_PY_FILES_TOTAL" "$(py_count src scripts tests)"
check py_files_with_header "$EXP_PY_FILES_WITH_HEADER" \
  "$(find src scripts tests -name '*.py' -not -path '*__pycache__*' -print0 |
    xargs -0 grep -l 'SPDX-License-Identifier' | wc -l | tr -d ' ')"

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
