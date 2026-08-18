#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-only
#
# Assert that every context named in .github/rulesets/main.json actually exists
# as a job in a workflow, and that ci-gate needs every leaf gate.
#
# WHY. A required status check is matched by a job's NAME STRING. Rename a job
# for readability and the ruleset silently stops protecting anything: GitHub
# waits forever for a context nothing will ever report, or -- worse, once the
# rule is later relaxed -- the gate is simply gone and no one notices. Nothing
# in git connects the two files. This script is that connection.
#
# It checks three things:
#   1. every required context resolves to a real job `name:`
#   2. ci-gate's `needs:` covers every other job in ci.yml (no gate left out)
#   3. no REQUIRED workflow carries a paths filter (GitHub's own guidance:
#      "avoid requiring workflows that can be skipped" -- a skipped required
#      check is `Expected` forever, which is a permanent merge deadlock)
#
#   usage: check-required-contexts.sh [repo-root]
set -euo pipefail

ROOT="${1:-.}"
command -v python3 >/dev/null 2>&1 || {
  echo "FAIL: python3 is required by this gate and is not on PATH." >&2; exit 1; }

python3 - "$ROOT" <<'PY'
import json, sys, pathlib
try:
    import yaml
except ImportError:
    sys.exit("FAIL: PyYAML is required by this gate and is not installed.")

root = pathlib.Path(sys.argv[1])
wf_dir = root / ".github/workflows"
ruleset = root / ".github/rulesets/main.json"

for f in (wf_dir, ruleset):
    if not f.exists():
        sys.exit(f"FAIL: missing {f}")

# ---- collect every job name across every workflow -------------------------
names, workflows = {}, {}
for wf in sorted(wf_dir.glob("*.yml")):
    doc = yaml.safe_load(wf.read_text()) or {}
    workflows[wf.name] = doc
    for jid, job in (doc.get("jobs") or {}).items():
        names[job.get("name", jid)] = (wf.name, jid)

required = []
for rule in json.loads(ruleset.read_text()).get("rules", []):
    if rule["type"] == "required_status_checks":
        required = [c["context"] for c in rule["parameters"]["required_status_checks"]]

# ANTI-VACUITY: an empty ruleset would pass every check below trivially.
if len(required) < 1:
    sys.exit("FAIL: the ruleset names no required status checks at all.")
if not names:
    sys.exit("FAIL: no workflow jobs found; the glob is wrong, not the repo.")

bad = 0

# ---- 1. every required context is a real job name -------------------------
print(f"required contexts ({len(required)}):")
for ctx in required:
    if ctx in names:
        wf, jid = names[ctx]
        print(f"  ok       {ctx!r}  <- {wf}:{jid}")
    else:
        print(f"  MISSING  {ctx!r} matches no job `name:` in any workflow")
        bad = 1

# ---- 2. ci-gate needs every other job in ci.yml ---------------------------
ci = workflows.get("ci.yml", {})
jobs = ci.get("jobs") or {}
gate = jobs.get("ci-gate")
if gate is None:
    print("  MISSING  ci.yml has no ci-gate job")
    bad = 1
else:
    needs = set(gate.get("needs") or [])
    leaves = {j for j in jobs if j != "ci-gate"}
    missing = leaves - needs
    extra = needs - leaves
    print(f"\nci-gate needs {len(needs)} of {len(leaves)} leaf jobs")
    if missing:
        print(f"  NOT COVERED by ci-gate: {sorted(missing)}")
        print("  A gate outside ci-gate's needs is a gate nothing requires.")
        bad = 1
    if extra:
        print(f"  needs a job that does not exist: {sorted(extra)}")
        bad = 1
    if not missing and not extra:
        print("  ok       every leaf gate is covered")

# ---- 3. no required workflow can be skipped by a paths filter -------------
print("\npaths filters on required workflows:")
required_wfs = {names[c][0] for c in required if c in names}
for wf in sorted(required_wfs):
    on = workflows[wf].get(True) or workflows[wf].get("on") or {}
    hits = []
    if isinstance(on, dict):
        for ev, cfg in on.items():
            if isinstance(cfg, dict) and ({"paths", "paths-ignore"} & set(cfg)):
                hits.append(ev)
    if hits:
        print(f"  FILTERED {wf} has a paths filter on {hits}")
        print("  A required workflow that can be skipped deadlocks main permanently.")
        bad = 1
    else:
        print(f"  ok       {wf}")

sys.exit(bad)
PY

echo "required contexts match the workflows."
