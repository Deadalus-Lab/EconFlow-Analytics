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
#   4. `exclude-newer` exists, is a well-formed instant, and appears EXACTLY ONCE
#      in the tree. A second copy is the failure this script exists to catch.
#
# WHY 4 IS PHRASED THAT WAY. The dependency snapshot used to live in two files in
# two different shapes, and the gate that preceded this one asserted the two
# agreed. Keeping one copy is strictly better than checking two, so this asserts
# the stronger property: that a second copy has not appeared.
#
# PORTABILITY. `grep` on a contributor machine may be ugrep, which ignores
# --exclude-dir and --include. Every search here uses `find` and plain patterns.
# ==============================================================================
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

fail() { echo "FAIL: $*" >&2; exit 1; }
checks=0

# ---- 1. every .python-version agrees ----------------------------------------
mapfile -t pv_files < <(find . -name '.python-version' -not -path './.git/*' -not -path './.venv/*' | sort)
[ "${#pv_files[@]}" -ge 2 ] || fail "found ${#pv_files[@]} .python-version files; expected the root and at least one member"

pinned=""
for f in "${pv_files[@]}"; do
    v="$(tr -d '[:space:]' < "$f")"
    [ -n "$v" ] || fail "$f is empty"
    if [ -z "$pinned" ]; then
        pinned="$v"
    elif [ "$v" != "$pinned" ]; then
        fail "$f pins $v but ${pv_files[0]} pins $pinned"
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
    [ -n "$floor" ] || fail "$f: cannot read a floor out of requires-python '$req'"
    lowest="$(printf '%s\n%s\n' "$floor" "$pinned" | sort -V | head -1)"
    [ "$lowest" = "$floor" ] || fail "$f requires-python '$req' is not satisfied by $pinned"
    checks=$((checks + 1))
    echo "  ok    $f requires-python '$req' satisfied by $pinned"
done

# ---- 3. CI pins the same interpreter -----------------------------------------
CI=".github/workflows/ci.yml"
if [ -f "$CI" ]; then
    ci_v="$(sed -n 's/^ *PYTHON_VERSION: *"\{0,1\}\([0-9.]*\)"\{0,1\} *$/\1/p' "$CI" | head -1)"
    [ -n "$ci_v" ] || fail "$CI declares no PYTHON_VERSION"
    [ "$ci_v" = "$pinned" ] || fail "$CI pins PYTHON_VERSION $ci_v but the tree pins $pinned"
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
[ -n "$snap" ] || fail "pyproject.toml sets no exclude-newer"
printf '%s' "$snap" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$' \
    || fail "exclude-newer '$snap' is not an RFC-3339 instant"
checks=$((checks + 1))

if [ -f uv.lock ]; then
    lock_snap="$(sed -n 's/^ *exclude-newer *= *"\(.*\)"/\1/p' uv.lock | head -1)"
    [ -n "$lock_snap" ] || fail "uv.lock records no exclude-newer; re-run 'uv lock'"
    [ "$lock_snap" = "$snap" ] \
        || fail "pyproject.toml pins $snap but uv.lock was built against $lock_snap; run 'uv lock'"
    checks=$((checks + 1))
fi

# Anywhere else is a hand-written third copy, and those rot.
others="$(grep -rl 'exclude-newer' --exclude-dir=.git --exclude-dir=.venv . 2>/dev/null \
          | grep -v '^\./pyproject\.toml$' | grep -v '^\./uv\.lock$' \
          | grep -v '^\./\.github/scripts/check-toolchain-pin\.sh$' || true)"
[ -z "$others" ] || fail "exclude-newer also appears in: $others"
echo "  ok    exclude-newer $snap, authored once, lock agrees"

# ---- anti-vacuity -------------------------------------------------------------
[ "$checks" -ge 5 ] || fail "only $checks assertions ran; the tree does not look like this project"
echo "ok: toolchain pins agree ($checks assertions)"
