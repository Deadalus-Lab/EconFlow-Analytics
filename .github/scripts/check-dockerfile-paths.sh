#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Assert that every `COPY <src>` in the Dockerfile resolves to something that
# actually exists in the build context.
#
# WHY THIS EXISTS. The real proof that the container definition is correct is a
# full `docker build`, which restores the locked environment and runs the whole
# suite inside the image. That proof belongs on the release path, not on every
# pull request.
#
# This script is the cheap half: it catches the single most likely error, a COPY
# whose source path no longer exists, in well under a second. It does NOT prove
# the image builds, and it is not presented as if it did.
#
#   usage: check-dockerfile-paths.sh [dockerfile] [build-context]
set -euo pipefail

DOCKERFILE="${1:-Dockerfile}"
CONTEXT="${2:-.}"

[ -f "$DOCKERFILE" ] || {
  echo "FAIL: no Dockerfile at $DOCKERFILE"
  exit 1
}

fail=0
checked=0

# Read COPY instructions, skipping --from=<stage> copies: those resolve inside a
# previous build stage, not in the build context, so the filesystem cannot
# answer for them.
while IFS= read -r line; do
  case "$line" in
    *--from=*) continue ;;
  esac

  # Strip the leading COPY, drop any flags, and drop the final argument, which
  # is the destination inside the image rather than a source path.
  args="${line#*COPY }"
  # shellcheck disable=SC2086
  set -- $args
  [ "$#" -ge 2 ] || continue
  n=$#
  i=0
  for src in "$@"; do
    i=$((i + 1))
    [ "$i" -lt "$n" ] || break           # last argument is the destination
    case "$src" in --*) continue ;; esac # a flag, not a path

    # A COPY source may be a glob; let the shell resolve it.
    # shellcheck disable=SC2086
    matches=$(cd "$CONTEXT" && ls -d $src 2>/dev/null | wc -l || true)
    checked=$((checked + 1))
    if [ "$matches" -eq 0 ]; then
      echo "  FAIL  COPY source does not exist in the build context: $src"
      fail=1
    else
      printf '  ok    %s\n' "$src"
    fi
  done
done < <(
  # Join backslash line-continuations FIRST -- a multi-line COPY is one
  # instruction -- then select COPY lines and squeeze runs of spaces and tabs.
  # Note: squeezing [:space:] here would also collapse newlines and fold the
  # whole file onto a single line, which silently reduces this gate to nothing.
  sed -e ':a' -e '/\\$/{N;s/\\\n//;ba' -e '}' "$DOCKERFILE" |
    grep -E '^[[:space:]]*COPY[[:space:]]' |
    tr -s ' \t' ' '
)

# Anti-vacuity: a Dockerfile whose COPY lines stopped matching the grep would
# otherwise "pass" without a single path having been checked.
if [ "$checked" -lt 5 ]; then
  echo "FAIL: only $checked COPY sources were checked; the parser is wrong, not the Dockerfile"
  exit 1
fi

if [ "$fail" -ne 0 ]; then
  echo
  echo "Dockerfile COPY paths are stale relative to the build context."
  echo "This is what a half-finished directory move looks like."
  exit 1
fi

echo
echo "All $checked COPY sources resolve in the build context ($CONTEXT)."
echo "NOTE: this does not prove the image builds -- only that no COPY path is stale."
