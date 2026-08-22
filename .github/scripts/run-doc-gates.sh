#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# run-doc-gates.sh -- the documentation suite, runnable before you push.
#
# WHY THIS EXISTS. `engine/run_verifications.sh` runs the engine's gates and
# prints "All verifications passed". It runs NONE of the documentation gates:
# those live in a separate continuous-integration job, so a contributor can see a
# green suite locally and be entirely unverified on every document they touched.
# That is exactly how a set of stale figures survived: the engine was green the
# whole time. This script is the missing half, and it is deliberately NOT folded
# into the engine suite -- two of these gates need the network, and the engine
# suite is meant to be reproducible offline.
#
# A MISSING TOOL IS A FAILURE, NEVER A SKIP. Each gate below either runs or turns
# this script red with the exact command that installs it. A documentation suite
# that quietly skipped what it could not start would report success while checking
# nothing, which is the failure every gate in this repository is written to refuse.
#
# EACH GATE ANSWERS A DIFFERENT QUESTION, and none can answer another's:
#   typos          is it spelled correctly?
#   markdownlint   is the Markdown well formed?
#   vale           does it read in the published register?
#   lychee         does every link resolve?
#   doc-claims     is it TRUE? -- the only one that re-runs the evidence
#
#   usage: run-doc-gates.sh [repo-root]
set -uo pipefail

ROOT="${1:-.}"
# `set -e` is deliberately absent above: every gate below must run so the report
# is complete, and one red gate must not hide the next. That makes an unguarded
# command a fail-open, so this one carries its own guard. Without it a failed
# `cd` left the script running in the INVOKER's directory, where the .vale.ini
# check below passed on the wrong tree and the suite printed "All documentation
# gates passed" about a tree it never entered.
cd "$ROOT" || {
  echo "FAIL: cannot enter '$ROOT'." >&2
  echo "      This suite runs inside the repository root. Pass a directory that exists," >&2
  echo "      or run it with no argument from the root." >&2
  exit 2
}
[ -f .vale.ini ] || {
  echo "FAIL: '$ROOT' holds no .vale.ini, so it is not the repository root." >&2
  echo "      Run this from the root, or pass the root as the first argument." >&2
  exit 2
}

failed=0
missing=0

need() {  # need <binary> <install command>
  if command -v "$1" >/dev/null 2>&1; then return 0; fi
  printf '  MISSING  %-14s install with: %s\n' "$1" "$2"
  missing=$((missing + 1))
  return 1
}

run() {   # run <label> <command...>
  local label="$1"; shift
  if "$@" >/tmp/docgate.$$ 2>&1; then
    printf '  ok       %-14s %s\n' "$label" "$(tail -1 /tmp/docgate.$$ | cut -c1-96)"
  else
    printf '  FAIL     %-14s\n' "$label"
    sed 's/^/             /' /tmp/docgate.$$ | head -25
    failed=$((failed + 1))
  fi
  rm -f /tmp/docgate.$$
}

echo "== the documentation suite =="

if need typos "uv tool install typos==1.29.4"; then
  run "typos" typos --config typos.toml
fi

if need npx "install Node.js; markdownlint-cli2 is fetched by npx"; then
  run "markdownlint" npx --yes markdownlint-cli2@0.17.2
fi

# vale: the exit code is not enough either. Run with NO file arguments, vale
# prints its usage and EXITS ZERO, so an empty `git ls-files` reads as a pass on
# a register nobody checked. The file count is compared against the manifest
# floor first, exactly as ci.yml's docs job does and for the same reason. The
# floor lives in .github/inventory.json and is read from there, so the number is
# stated in one place and a reviewer sees it move.
if need vale "curl -fsSL https://github.com/errata-ai/vale/releases/download/v3.17.1/vale_3.17.1_Linux_64-bit.tar.gz | tar -xz vale"; then
  mapfile -t docs < <(git ls-files '*.md')
  # int() IS THE GUARD, NOT DECORATION. A floor that is present but not a number
  # -- this manifest documents "unmeasured" as a value a constant may legitimately
  # hold -- leaves the test below with a non-empty operand that `[ -lt ]` still
  # refuses, and a refused test falls through to the else branch, so the floor
  # silently stops applying. int() turns that into a non-zero exit the guard here
  # already catches.
  if ! floor=$(python3 -c \
      "import json;print(int(json.load(open('.github/inventory.json'))['docs']['min_markdown_files']))" 2>/dev/null); then
    printf '  FAIL     %-14s cannot read docs.min_markdown_files from .github/inventory.json; the floor is what stops a vacuous pass, so restore that key before running this suite\n' \
           "vale"
    failed=$((failed + 1))
  elif [ "${#docs[@]}" -lt "$floor" ]; then
    printf '  FAIL     %-14s %s Markdown file(s) to examine, below the floor %s; the git pathspec is wrong, not the tree\n' \
           "vale" "${#docs[@]}" "$floor"
    failed=$((failed + 1))
  else
    run "vale" vale --config .vale.ini "${docs[@]}"
  fi
fi

# lychee: the exit code is not enough. lychee.toml records that a mis-anchored
# exclude_path once made it report "no files found" while EXITING ZERO, so the
# link count is compared against the manifest floor exactly as the workflow does.
if need lychee "cargo install lychee --version 0.18.1 --locked"; then
  if lychee --config lychee.toml --no-progress --format json \
            --output /tmp/lychee.$$ . >/dev/null 2>&1; then
    # GUARDED EXACTLY AS THE VALE FLOOR ABOVE IS, AND FOR THE SAME REASON. This
    # read used to be a bare `read -r total floor < <(python3 ...)`. The script
    # carries no `set -e`, so when that python3 raised -- a missing key, an
    # unreadable report -- both variables were left empty, `[ "" -lt "" ]` printed
    # "integer expression expected" and returned non-zero, and the else branch
    # below printed "ok lychee" having compared nothing. One idiom for this job in
    # this file: `if ! var=$(...)`, once per number, int() at the boundary.
    if ! total=$(python3 -c \
        "import json;print(int(json.load(open('/tmp/lychee.$$'))['total']))" 2>/dev/null) ||
       ! floor=$(python3 -c \
        "import json;print(int(json.load(open('.github/inventory.json'))['docs']['min_links_checked']))" 2>/dev/null); then
      printf '  FAIL     %-14s cannot read the checked-link total from the lychee report, or docs.min_links_checked from .github/inventory.json; the floor is what stops a vacuous pass, so restore that key as an integer before running this suite\n' \
             "lychee"
      failed=$((failed + 1))
    elif [ "$total" -lt "$floor" ]; then
      printf '  FAIL     %-14s checked %s links, below the floor %s; the glob or exclude_path is wrong, not the tree\n' \
             "lychee" "$total" "$floor"
      failed=$((failed + 1))
    else
      printf '  ok       %-14s %s link(s) resolve (floor %s)\n' "lychee" "$total" "$floor"
    fi
  else
    printf '  FAIL     %-14s broken link(s); re-run for the list\n' "lychee"
    failed=$((failed + 1))
  fi
  rm -f /tmp/lychee.$$
fi

# No tool to install: this one is ours.
run "doc-claims" bash .github/scripts/check-doc-claims.sh .

echo
if [ "$missing" -gt 0 ]; then
  echo "FAIL: $missing tool(s) are not installed, so this suite did NOT check what they cover." >&2
  echo "      A gate that cannot start must never read as a gate that passed." >&2
fi
[ "$failed" -gt 0 ] && echo "FAIL: $failed documentation gate(s) are red." >&2
if [ "$missing" -gt 0 ] || [ "$failed" -gt 0 ]; then exit 1; fi
echo "All documentation gates passed."
