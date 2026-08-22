#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Assert that the repository's GitHub-side settings still match what was
# decided. Settings are not in git: a click in the web UI, an organisation
# policy change or a token with the wrong scope can silently undo them, and
# nothing in the tree would notice. This script is that notice.
#
# It runs LOCALLY (pre-flight, todo 1.6.1) or from any shell with `gh` logged in
# as a repository admin -- reading Actions permissions needs admin, so it
# cannot run under the workflow's own GITHUB_TOKEN. Every expectation here is a
# decision recorded either in ARCHITECTURE.md under "Decisions already made" --
# chiefly that no third-party service is ever a required check -- or in
# .github/rulesets/*.json; change the decision first, then the line.
#
#   usage: check-repo-settings.sh [owner/repo]
set -euo pipefail

REPO="${1:-Deadalus-Lab/EconFlow-Analytics}"
command -v gh >/dev/null 2>&1 || {
  echo "FAIL: gh is required." >&2
  exit 1
}
command -v python3 >/dev/null 2>&1 || {
  echo "FAIL: python3 is required." >&2
  exit 1
}

fail=0
expect() { # expect <label> <actual> <expected>
  if [ "$2" = "$3" ]; then
    printf '  ok    %-52s %s\n' "$1" "$2"
  else
    printf '  FAIL  %-52s got %s, expected %s\n' "$1" "$2" "$3"
    fail=1
  fi
}

echo "repository settings audit: ${REPO}"

# --- Actions supply chain (G1) ---------------------------------------------
perms=$(gh api "repos/${REPO}/actions/permissions")
expect "actions.allowed_actions" "$(printf '%s' "$perms" | python3 -c 'import json,sys;print(json.load(sys.stdin)["allowed_actions"])')" "selected"
expect "actions.sha_pinning_required" "$(printf '%s' "$perms" | python3 -c 'import json,sys;print(json.load(sys.stdin)["sha_pinning_required"])')" "True"
wf=$(gh api "repos/${REPO}/actions/permissions/workflow")
expect "actions.default_workflow_permissions" "$(printf '%s' "$wf" | python3 -c 'import json,sys;print(json.load(sys.stdin)["default_workflow_permissions"])')" "read"
expect "actions.can_approve_pull_request_reviews" "$(printf '%s' "$wf" | python3 -c 'import json,sys;print(json.load(sys.stdin)["can_approve_pull_request_reviews"])')" "False"

# Every third-party action the workflows use must be on the allowlist, or the
# first run after this check fails with "is not allowed". Transitive actions
# (one action calling another) are NOT visible here -- add them when a run
# names them; that is why oven-sh/setup-bun sits beside claude-code-action.
sel=$(gh api "repos/${REPO}/actions/permissions/selected-actions")
expect "actions.github_owned_allowed" "$(printf '%s' "$sel" | python3 -c 'import json,sys;print(json.load(sys.stdin)["github_owned_allowed"])')" "True"
# `^[^#]*uses:` SKIPS COMMENTS, and that is not tidiness. The previous pattern
# matched `uses:` anywhere on a line, so the prose example in ci.yml explaining
# why `uses: owner/action@v5` is unsafe was read as a real dependency -- and this
# audit demanded that a repository allowlist an action called `owner/action`,
# which cannot exist. A gate that fails on a sentence teaches people to ignore it.
used=$(grep -rhE '^[^#]*uses: [^ ]+' .github/workflows .github/actions 2>/dev/null |
  grep -oE 'uses: [^ ]+' | sed 's/uses: //' | grep -v '^\./' | grep -v '^actions/' | cut -d@ -f1 | sort -u)
for a in $used; do
  if printf '%s' "$sel" | python3 -c 'import json,sys;a=sys.argv[1];pats=json.load(sys.stdin)["patterns_allowed"];sys.exit(0 if any(p.split("@")[0]==a for p in pats) else 1)' "$a"; then
    printf '  ok    %-52s %s\n' "actions.allowlist covers" "$a"
  else
    printf '  FAIL  %-52s %s is used by a workflow and not allowlisted\n' "actions.allowlist covers" "$a"
    fail=1
  fi
done

# --- Merge and branch hygiene ----------------------------------------------
repo=$(gh api "repos/${REPO}")
rf() { printf '%s' "$repo" | python3 -c 'import json,sys;print(json.load(sys.stdin)[sys.argv[1]])' "$1"; }
expect "merge.allow_squash_merge" "$(rf allow_squash_merge)" "True"
expect "merge.allow_merge_commit" "$(rf allow_merge_commit)" "False"
expect "merge.allow_rebase_merge" "$(rf allow_rebase_merge)" "False"
expect "merge.delete_branch_on_merge" "$(rf delete_branch_on_merge)" "True"
expect "merge.squash_merge_commit_title" "$(rf squash_merge_commit_title)" "PR_TITLE"

# --- Security features -----------------------------------------------------
sa() { printf '%s' "$repo" | python3 -c 'import json,sys;print(json.load(sys.stdin)["security_and_analysis"][sys.argv[1]]["status"])' "$1"; }
expect "security.secret_scanning" "$(sa secret_scanning)" "enabled"
expect "security.secret_scanning_push_protection" "$(sa secret_scanning_push_protection)" "enabled"
expect "security.dependabot_security_updates" "$(sa dependabot_security_updates)" "enabled"
expect "security.private_vulnerability_reporting" "$(gh api "repos/${REPO}/private-vulnerability-reporting" -q .enabled)" "true"
expect "security.codeql_default_setup" "$(gh api "repos/${REPO}/code-scanning/default-setup" -q .state)" "configured"

# --- Rulesets: every JSON in .github/rulesets exists live, same target -----
live=$(gh api "repos/${REPO}/rulesets")
for f in .github/rulesets/*.json; do
  name=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["name"])' "$f")
  target=$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1]))["target"])' "$f")
  got=$(printf '%s' "$live" | python3 -c 'import json,sys;n=sys.argv[1];m=[r for r in json.load(sys.stdin) if r["name"]==n];print(m[0]["target"]+"/"+m[0]["enforcement"] if m else "absent")' "$name")
  case "$got" in
    "${target}/active") printf '  ok    %-52s %s\n' "ruleset ${name}" "$got" ;;
    "${target}/evaluate") printf '  WARN  %-52s %s (allowed only until the first push; todo 1.6.5 flips it)\n' "ruleset ${name}" "$got" ;;
    *)
      printf '  FAIL  %-52s %s\n' "ruleset ${name}" "$got"
      fail=1
      ;;
  esac
done

# --- Topics: the languages actually used ---------------------------------
topics=$(rf topics)
case "$topics" in
  *"'r'"*)
    printf '  FAIL  %-52s %s\n' "topics" "still advertise 'r'"
    fail=1
    ;;
  *python*) printf '  ok    %-52s %s\n' "topics" "$topics" ;;
  *)
    printf '  FAIL  %-52s %s (python missing)\n' "topics" "$topics"
    fail=1
    ;;
esac

if [ "$fail" -eq 0 ]; then
  echo "repository settings match the decisions."
else
  echo "repository settings DRIFTED from the decisions." >&2
  exit 1
fi
