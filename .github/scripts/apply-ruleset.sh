#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Apply the `main` branch ruleset.
#
# ---------------------------------------------------------------------------
# RUN THIS AFTER THE FIRST PUSH, NOT BEFORE. THE ORDER MATTERS.
# ---------------------------------------------------------------------------
# The ruleset requires a pull request before anything reaches `main`, and it
# requires named status checks to pass. Applied to an EMPTY repository that has
# no commits, it would:
#
#   * block the initial push to main outright, and
#   * require status checks that have never run, so the first pull request could
#     never go green either.
#
# Correct order:
#
#   1. push the initial commits to main directly (the branch is unprotected)
#   2. open one throwaway pull request so every check runs at least once and
#      GitHub learns the check names
#   3. run this script
#
# Step 2 is not optional. A required status check whose name has never been seen
# is simply "expected" forever, and the pull request can never merge.
#
# A note on the zero approvals. A solo maintainer cannot approve their own pull
# request, so `required_approving_review_count` is 0 and enforcement rests on
# the status checks instead. That is deliberate. The alternative -- setting it
# to 1 and then bypassing it -- would be a gate that never bites, which is worse
# than no gate because it looks like one.
set -euo pipefail

DRY_RUN=0
ARGS=()
for a in "$@"; do
  case "$a" in
    --dry-run) DRY_RUN=1 ;;
    *) ARGS+=("$a") ;;
  esac
done
REPO="${ARGS[0]:-Deadalus-Lab/EconFlow-Analytics}"
RULESET="$(dirname "$0")/../rulesets/main.json"   # script lives in .github/scripts/

[ -f "$RULESET" ] || { echo "no ruleset at $RULESET"; exit 1; }

echo "Repository: $REPO"

# NOTE ON THIS GUARD. It used to ask for a commit count via `--jq length`, but on
# an EMPTY repository that endpoint returns HTTP 409 with a JSON error object,
# not an empty list -- so the variable held a JSON blob, `[ "$blob" -eq 0 ]`
# raised "integer expression expected", and because the test sat inside an `if`
# the `set -e` did not stop the script. It went on to create the ruleset on the
# empty repository: precisely the outcome this guard exists to prevent.
#
# The fix asks a question with an unambiguous answer instead of parsing a body.
if ! gh api "repos/${REPO}/commits?per_page=1" >/dev/null 2>&1; then
  cat <<'MSG'
REFUSING: the repository has no commits.

Applying the ruleset now would block the initial push to main. Push first, open
one throwaway pull request so the checks run once, then re-run this script.
MSG
  exit 1
fi

# Report which required checks GitHub has actually observed. A check it has
# never seen stays "expected" forever and blocks every merge.
echo
echo "Required checks named in the ruleset, and whether GitHub has seen them:"
seen="$(gh api "repos/${REPO}/commits/HEAD/check-runs" --jq '.check_runs[].name' 2>/dev/null || true)"
# NOTE ON THE PLUMBING. `python3 -` reads its PROGRAM from stdin, so stdin is
# already spoken for by the heredoc. The observed check names must therefore
# arrive as an ARGUMENT, not on stdin. Two earlier versions of this got it
# wrong -- one had a heredoc AND a herestring (the herestring won, so python
# tried to execute the check names), the other piped the names in (same result).
# Both failed silently behind `|| true`, so the preflight printed nothing real.
missing=0
python3 - "$RULESET" "$seen" <<'PY' || missing=$?
import json, sys
rs = json.load(open(sys.argv[1]))
observed = {l.strip() for l in sys.argv[2].splitlines() if l.strip()}
required = [c["context"]
            for rule in rs["rules"] if rule["type"] == "required_status_checks"
            for c in rule["parameters"]["required_status_checks"]]
if not required:
    sys.exit("  the ruleset names NO required status checks -- refusing to apply it.")
unseen = 0
for name in required:
    if name in observed:
        print("  seen      " + name)
    else:
        print("  NOT SEEN  " + name)
        unseen += 1
if unseen:
    print(f"\n  {unseen} of {len(required)} required contexts have never been observed.")
    print("  GitHub keeps an unobserved required check as 'Expected' forever, so")
    print("  applying the ruleset now would block every merge permanently.")
sys.exit(1 if unseen else 0)
PY

if [ "$missing" -ne 0 ]; then
  echo
  echo "REFUSING: not every required context has been observed on this repository."
  echo "Open one throwaway pull request so every check runs once, then re-run."
  exit 1
fi

if [ "$DRY_RUN" -eq 1 ]; then
  echo
  echo "--dry-run: stopping before any write. Nothing was applied."
  exit 0
fi

echo
existing="$(gh api "repos/${REPO}/rulesets" --jq '.[] | select(.name=="main") | .id' 2>/dev/null || true)"
if [ -n "$existing" ]; then
  echo "Updating existing ruleset $existing"
  gh api -X PUT "repos/${REPO}/rulesets/${existing}" --input "$RULESET" --jq '{id,name,enforcement}'
else
  echo "Creating ruleset"
  gh api -X POST "repos/${REPO}/rulesets" --input "$RULESET" --jq '{id,name,enforcement}'
fi

echo
echo "Applied. Verify with:  gh api repos/${REPO}/rulesets --jq '.[].name'"
