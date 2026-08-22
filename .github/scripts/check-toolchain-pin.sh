#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
# ==============================================================================
# check-toolchain-pin.sh — the interpreter and the dependency snapshot are pinned
# in more than one file, and every copy of a pin is a copy that rots.
#
# WHAT IT ASSERTS
#   1. Every `.python-version` in the tree carries the same value.
#   2. That value satisfies `requires-python` in every pyproject.
#   3. `PYTHON_VERSION` in ci.yml is that same value.
#   4. `exclude-newer` exists, is a well-formed instant, and the instant appears
#      EXACTLY ONCE in the tree. A second copy is the failure this script exists
#      to catch.
#
# WHY 4 IS PHRASED THAT WAY. The dependency snapshot used to live in two files in
# two different shapes, and the gate that preceded this one asserted the two
# agreed. Keeping one copy is strictly better than checking two, so this asserts
# the stronger property: that a second copy has not appeared.
#
# WHAT A COPY IS. The value, not the key: an authored `exclude-newer = "..."`, or
# the instant standing on its own. Naming the key in prose is not a copy. The
# earlier form of this check matched the key name, which had both faults at once
# -- it refused a decision record for naming the real field, and it let a date
# pasted into a document with no key beside it through untouched. Both cases are
# now controls, and both run on every invocation.
#
# PORTABILITY. `grep` on a contributor machine may be ugrep, which ignores
# --exclude-dir and --include. Every search here uses `find` and plain patterns.
# ==============================================================================
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}
checks=0
scanned=0

# ---- 1. every .python-version agrees ----------------------------------------
mapfile -t pv_files < <(find . -name '.python-version' -not -path './.git/*' -not -path './.venv/*' | sort)
[ "${#pv_files[@]}" -ge 2 ] || fail "found ${#pv_files[@]} .python-version file(s); this workspace has one at the root and one per member. The find path is wrong, not the tree"

pinned=""
for f in "${pv_files[@]}"; do
  v="$(tr -d '[:space:]' <"$f")"
  [ -n "$v" ] || fail "$f is empty, so it pins nothing. Write the interpreter version into it, matching every other .python-version in the tree"
  if [ -z "$pinned" ]; then
    pinned="$v"
  elif [ "$v" != "$pinned" ]; then
    fail "$f pins $v but ${pv_files[0]} pins $pinned. Every copy of this pin must carry the same value; change them together, in one commit"
  fi
  checks=$((checks + 1))
done
echo "  ok    ${#pv_files[@]} .python-version files all pin $pinned"

# ---- 2. requires-python is satisfied by that value ---------------------------
mapfile -t projects < <(find . -name 'pyproject.toml' -not -path './.git/*' -not -path './.venv/*' | sort)
for f in "${projects[@]}"; do
  req="$(sed -n 's/^requires-python *= *"\(.*\)"/\1/p' "$f" | head -1)"
  [ -n "$req" ] || continue
  floor="$(printf '%s' "$req" | sed -n 's/^>=\([0-9.]*\).*/\1/p')"
  [ -n "$floor" ] || fail "$f: cannot read a floor out of requires-python '$req'. This gate reads a '>=X.Y' floor; write the constraint that way"
  lowest="$(printf '%s\n%s\n' "$floor" "$pinned" | sort -V | head -1)"
  [ "$lowest" = "$floor" ] || fail "$f requires-python '$req' is not satisfied by $pinned"
  checks=$((checks + 1))
  echo "  ok    $f requires-python '$req' satisfied by $pinned"
done

# ---- 3. CI pins the same interpreter -----------------------------------------
CI=".github/workflows/ci.yml"
if [ -f "$CI" ]; then
  ci_v="$(sed -n 's/^ *PYTHON_VERSION: *"\{0,1\}\([0-9.]*\)"\{0,1\} *$/\1/p' "$CI" | head -1)"
  [ -n "$ci_v" ] || fail "$CI declares no PYTHON_VERSION. Every Python-dependent job reads it, so add it to the workflow env and set it to the value in .python-version"
  [ "$ci_v" = "$pinned" ] || fail "$CI pins PYTHON_VERSION $ci_v but the tree pins $pinned. CI must run the interpreter the tree declares: set them to the same value in one commit"
  checks=$((checks + 1))
  echo "  ok    $CI PYTHON_VERSION $ci_v"
fi

# ---- 4. the dependency snapshot: one author, and the lock agrees with it -----
# `pyproject.toml` is where a human sets it. `uv.lock` carries uv's resolved copy.
# The lock's copy is not a second pin -- it is a witness that the lock was built
# from the current manifest. If they disagree, someone moved the date and did not
# re-lock, and `uv sync --locked` would then resolve against a snapshot nobody
# chose. That is exactly the drift this check exists for, so the two are compared
# rather than one of them being ignored.
snap="$(sed -n 's/^ *exclude-newer *= *"\(.*\)"/\1/p' pyproject.toml | head -1)"
[ -n "$snap" ] || fail "pyproject.toml sets no exclude-newer. The dependency snapshot is what makes a resolution reproducible; set tool.uv.exclude-newer to an RFC-3339 instant"
printf '%s' "$snap" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$' ||
  fail "exclude-newer '$snap' is not an RFC-3339 instant"
checks=$((checks + 1))

if [ -f uv.lock ]; then
  lock_snap="$(sed -n 's/^ *exclude-newer *= *"\(.*\)"/\1/p' uv.lock | head -1)"
  [ -n "$lock_snap" ] || fail "uv.lock records no exclude-newer; re-run 'uv lock'"
  [ "$lock_snap" = "$snap" ] ||
    fail "pyproject.toml pins $snap but uv.lock was built against $lock_snap; run 'uv lock'"
  checks=$((checks + 1))
fi

# Anywhere else is a hand-written third copy, and those rot.
#
# WHAT COUNTS AS A COPY: an authored assignment, or the instant itself. Naming
# the key in prose is not a copy. A document that says where the pin lives
# carries no value that can rot, and the writing framework requires naming the
# real key rather than a placeholder, so matching the bare key name refused a
# document for being accurate. Matching the instant is also strictly stronger
# than matching the key: a date pasted into a document with no key beside it is
# exactly the rot this gate exists to catch, and the key-name pattern missed it.
copy_re="exclude-newer[[:space:]]*=[[:space:]]*\"|$snap"

others=""
while IFS= read -r f; do
  case "$f" in
    ./pyproject.toml | ./uv.lock | ./.github/scripts/check-toolchain-pin.sh) continue ;;
  esac
  if grep -qE "$copy_re" "$f" 2>/dev/null; then
    others="$others $f"
  fi
  scanned=$((scanned + 1))
done < <(find . -type f \
  -not -path './.git/*' -not -path './.venv/*' -not -path '*/__pycache__/*' \
  -not -path './node_modules/*' -not -path '*/.mypy_cache/*' -not -path '*/.ruff_cache/*' \
  -not -path '*/.pytest_cache/*' -not -path '*/.import_linter_cache/*' \
  -not -path './.private/*' -not -path './.claude/*' | sort)

[ -z "$others" ] || fail "the dependency snapshot is authored once, in pyproject.toml, and witnessed by uv.lock. A third copy rots. A copy of the instant appears in:$others -- delete the date there and point at pyproject.toml instead. Naming the key without a date is fine; a date is not"
checks=$((checks + 1))

# ---- controls: this search must be able to fail, and able to pass ------------
probe="$(mktemp -d)"
trap 'rm -rf "$probe"' EXIT
printf 'exclude-newer = "2020-01-01T00:00:00Z"\n' >"$probe/assignment"
printf 'the resolution is bounded at %s in this tree\n' "$snap" >"$probe/bare-instant"
printf 'The date lives under `[tool.uv]` as `exclude-newer` in the root manifest.\n' >"$probe/prose"

if ! grep -qE "$copy_re" "$probe/assignment"; then
  fail "positive control: an authored 'exclude-newer = \"...\"' was not detected. The pattern is broken, so this gate is examining nothing"
fi
if ! grep -qE "$copy_re" "$probe/bare-instant"; then
  fail "positive control: a bare copy of $snap was not detected. The pattern is broken, so a pasted date would pass"
fi
if grep -qE "$copy_re" "$probe/prose"; then
  fail "negative control: prose naming the key with no date beside it was flagged. Accurate documentation must survive this gate"
fi
checks=$((checks + 1))

[ "$scanned" -ge 200 ] || fail "the snapshot search examined only $scanned file(s); the find path is wrong, not the tree"
echo "  ok    dependency snapshot $snap, authored once, lock agrees (${scanned} files scanned, both controls fired)"

# ---- anti-vacuity -------------------------------------------------------------
[ "$checks" -ge 5 ] || fail "only $checks assertions ran; the tree does not look like this project"
echo "ok: toolchain pins agree ($checks assertions)"
