#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Assert that the repository's PUBLIC ROOT SURFACE is exactly what
# .github/root-manifest.txt declares.
#
# WHY THIS EXISTS. .gitignore denies everything at the root and re-admits by
# name. That is only a guarantee if something checks it. Two failure modes,
# and this script refuses BOTH:
#
#   appeared -- a root file became public that nobody reviewed. Permanent, on
#               a repository whose history cannot be rewritten.
#   vanished -- a root file silently stopped being tracked. A deny-by-default
#               rule makes this SILENT: `git status` shows nothing at all.
#
# The second is why a one-directional check is not enough.
#
#   usage: check-root-visibility.sh [repo-root] [manifest]
set -euo pipefail

ROOT="${1:-.}"
MANIFEST="${2:-$ROOT/.github/root-manifest.txt}"

[ -f "$MANIFEST" ] || {
  echo "FAIL: no manifest at $MANIFEST" >&2
  exit 1
}

expected="$(grep -vE '^\s*(#|$)' "$MANIFEST" | LC_ALL=C sort)"

# Top-level entries git considers trackable: staged/committed plus untracked
# that survive .gitignore. Works before the first commit and after it.
actual="$(cd "$ROOT" && git ls-files --cached --others --exclude-standard |
  cut -d/ -f1 | LC_ALL=C sort -u)"

# ANTI-VACUITY: a comparison against an empty manifest would pass trivially.
n=$(printf '%s\n' "$expected" | grep -c . || true)
if [ "$n" -lt 10 ]; then
  echo "FAIL: manifest declares only $n entries; a root this small means the" >&2
  echo "      manifest is truncated, not that the repository shrank." >&2
  exit 1
fi

if diff_out=$(diff <(printf '%s\n' "$expected") <(printf '%s\n' "$actual")); then
  echo "ok: public root surface matches the manifest ($n entries)."
  exit 0
fi

echo "FAIL: the public root surface does not match .github/root-manifest.txt" >&2
echo >&2
printf '%s\n' "$diff_out" | sed 's/^</  VANISHED (in manifest, not tracked): /; s/^>/  APPEARED  (tracked, not in manifest): /' >&2
echo >&2
echo "If the change is intended, update .github/root-manifest.txt in the SAME" >&2
echo "commit. That diff is the review." >&2
exit 1
