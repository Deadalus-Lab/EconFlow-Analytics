<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# The first push — commands to run

Every command below is yours to run. Nothing in this repository has been committed or pushed.

**The order matters.** Two steps depend on it, and both are called out where they occur.

---

## Before anything: the blocker is closed

`NOTICE` and `CODE_OF_CONDUCT.md` previously carried a placeholder marker where a contact belonged.
`NOTICE` was the legally meaningful one: the written offer of corresponding source requires a real
contact.

**Resolved 2026-08-15.** Both now name a GitHub channel rather than an email address — an issue
titled "AGPL source request" for the source offer, and private vulnerability reporting for conduct and
security. A published address is permanently harvested, and git authorship already uses GitHub's
routed no-reply address for the same reason. The obligation is unaffected: the channel is monitored
and a request through it is answered on the stated terms.

```bash
# Scope the check to the surface that actually gets published, and exclude docs/,
# which describes the marker rather than carrying one. Returns nothing when clean.
git ls-files --others --exclude-standard --cached \
  | grep -v '^docs/' \
  | xargs -r grep -l "SET BEFORE FIRST PUSH"
```

> **Two notes for whoever writes the Phase 0 exit gate.**
>
> 1. The gate as originally drafted was `grep -rn 'SET BEFORE FIRST PUSH' .` returning nothing —
>    which this file would fail forever, since documenting a marker requires naming it. It has to
>    exclude `docs/`.
>
> 2. **Do not write that exclusion with `--exclude-dir`.** Measured on this machine: `grep` resolves
>    to **ugrep 7.5.0**, not GNU grep (`/bin/grep` is GNU 3.11), and ugrep does **not** honour
>    `--exclude-dir=docs` — nor `docs/`, `*/docs/*` or `^docs/`. The same divergence bites
>    `--include`: measured on this tree, `grep -rl 'SPDX-License-Identifier' src scripts tests
>    --include='*.py'` reported **315** files where GNU grep reported **379**, silently omitting the
>    whole generated tier. CI runners ship GNU grep, so a gate written either way passes in CI while
>    misreporting locally — and in the `--include` case it undercounts, which is the direction that
>    lets a real gap through. The forms used in this repository avoid both flags entirely.

---

## 1. Confirm the baseline is green

```bash
(cd engine && ./run_verifications.sh)                    # must exit 0
bash .github/actions/assert-inventory/assert.sh engine .github/inventory.json
bash .github/scripts/check-dockerfile-paths.sh Dockerfile .
bash .github/scripts/check-root-visibility.sh .
bash .github/scripts/check-required-contexts.sh .
bash .github/scripts/check-engine-boundary.sh .
bash .github/scripts/check-toolchain-pin.sh .
bash .github/scripts/check-vocabulary.sh .
bash .github/scripts/check-repo-settings.sh          # local, needs an admin gh login
pre-commit run --all-files
docker build -t econflow-engine:preflight .          # the in-image suite is a build gate
docker run --rm econflow-engine:preflight python -m econflow_engine --help
```

> **All of these are green as of 2026-08-18.** Nothing prints `OWED`: the workspace lockfile, the
> bill of materials and the licence register all exist, and every constant in
> `.github/inventory.json` re-measures from the command recorded beside it. A constant that cannot
> be measured must never read as a constant that was verified, so if any line here prints `OWED`,
> stop and land the artifact rather than pushing past it.

---

## 2. Two commits

The licence goes in **first, alone**. `ARCHITECTURE.md` §11 opens with *"the project is open source
from its first commit"* — making the licence literally commit #1 turns that from approximately true
into true, and GitHub's licence detection works from the outset.

```bash
git add LICENSE NOTICE CITATION.cff .gitignore .gitattributes
git commit -s -m "chore: initialize repository under AGPL-3.0-only" -m "\
- Uniform AGPL-3.0-only across the whole repository. Copyleft here is a
  choice rather than an inheritance: the Python scientific stack is BSD,
  Apache-2.0 and MIT throughout, so no dependency compels any licence at all.
- The Affero variant is chosen for section 13. The deployed form of this
  project is a hosted compute engine, and under GPL-2 or GPL-3 an operator
  could modify it, run it as a service and owe nothing back. Section 13
  attaches the obligation to operation rather than to shipping a binary.
- One consequence, recorded rather than discovered later: AGPL-3.0 is not
  compatible with GPL-2.0-only, so a GPL-2.0-only dependency can no longer be
  admitted to this tree.
- NOTICE carries the attribution summary and the written offer for
  corresponding source.
- CITATION.cff provides citation metadata for the academic audience.
- .gitattributes normalises line endings to LF. This is load-bearing rather
  than cosmetic: the artifact generators compare committed files byte for
  byte, so a CRLF checkout would fail all of them."

git add -A
git commit -s -m "feat(engine): import the compute engine" -m "\
The complete Layer 1 engine, verified against ARCHITECTURE.md section 4.1.
Every figure below is reproduced by the command beside it, run from engine/.

- 251 wrapper modules, 0 of 913 methods implemented -- every body still raises
- 251 wrapper modules   find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' | wc -l
- 30 category packages  find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' | wc -l
- 913 executable methods, 30 categories, 252 method cards and 4855 frozen
  parity verdicts, all read from the committed artifacts rather than counted
  from source. Those five figures are language-neutral and did not move.
- 380 of 380 Python files carry an SPDX identifier, all AGPL-3.0-only
- Python 3.12, dependencies pinned by version AND hash in a single uv.lock

Re-run engine/run_verifications.sh rather than trusting any line above.

Also included: continuous-integration gates, marketplace app configuration,
and governance documents. Every gate asserts a minimum quantity of work done,
so that a gate which examined nothing cannot report success."

git log --oneline
git push -u origin main
```

---

## 3. One throwaway pull request — **do not skip this**

The ruleset names required status checks. GitHub treats a check it has *never observed* as
permanently "expected", so a required check that has not run once will block every merge forever.
This pull request is what teaches GitHub the names.

```bash
git switch -c ci/canary
printf '\n<!-- canary -->\n' >> docs/decisions/first-push.md
git commit -s -am "ci: prove the gate set fires"
git push -u origin ci/canary
gh pr create --title "ci: prove the gate set fires" --body "Throwaway. Verifies every gate runs."
gh pr checks --watch
```

While it runs, confirm on the checks page:

- All ten `ci.yml` leaf jobs green, plus `ci-gate` reporting `all 10 gates reported success` and `dco`
- The `secrets` log shows **the planted canary was detected** — that line is what makes the job
  trustworthy
- The `engine-boundary` log shows **its own positive control passed** — that line is what makes the
  gate trustworthy while `backend/` still holds no code
- The `spdx` log shows a scan of **380** files, not of 316: the lower figure would mean the generated
  tier was skipped
- CodeRabbit posted a review; GitGuardian reported clean; pre-commit.ci ran
- **No check from the four disabled apps** (codspeed, keploy, cla-bot, giscus). If any appears, its
  installation scope still needs narrowing — see `marketplace-apps.md`. Note that four apps had their
  verdict *reversed* on 2026-08-16 and are being enabled, so checks from SonarQube, its agent, Endor
  Labs or CodeQL are expected once each is configured, and are **advisory**.

Then merge and delete the branch.

---

## 4. Apply the ruleset — **only now**

```bash
bash .github/scripts/apply-ruleset.sh
```

It refuses to run against a repository with no commits, and prints which required checks GitHub has
actually seen. If any says `NOT SEEN`, that check did not run on the canary pull request; fix that
before applying, or it will block merges.

Note: `required_approving_review_count` is **0**. A solo maintainer cannot approve their own pull
request, so enforcement rests on the status checks. Setting it to 1 and then bypassing it would be a
gate that never bites — worse than no gate, because it looks like one.

**Nothing from a marketplace app joins the ruleset.** It names exactly two contexts, `ci-gate` and
the DCO check. A third-party app can be renamed, rate-limited or fail to report, and each of those
is a permanent merge deadlock. See `marketplace-apps.md`.

---

## 5. Claude — two manual steps

Neither can be scripted: the local token has no `admin:org`, and app installation is an interactive
OAuth flow.

1. Install the **Claude GitHub App** on `Deadalus-Lab`, scoped to **only** `EconFlow-Analytics`.
2. Add a **repository** secret (not an organisation secret — repository scope confines the blast
   radius):

```bash
gh secret set ANTHROPIC_API_KEY --repo Deadalus-Lab/EconFlow-Analytics
```

Then verify Claude is in **no** required check:

```bash
gh api repos/Deadalus-Lab/EconFlow-Analytics/rulesets --jq \
  '.[].rules[]? | select(.type=="required_status_checks")
   | .parameters.required_status_checks[].context' | grep -i claude || echo "correct: claude is not required"
```

It must never be required: it is non-deterministic, it depends on a third-party API, and it cannot
run on fork pull requests. See the header of `.github/workflows/claude.yml`.

---

## Still open after this

| Item | Why it waits |
|---|---|
| Repairing `METHOD-SELECTION.md`'s section structure | 106 of 252 cards are nested under the wrong `##` section and one category has no heading at all. `check-method-selection-headings.sh` reports it exactly and is deliberately not wired into CI until the document is repaired, which happens as the corpus is rewritten one category at a time |
| Publishing the engine image | It is the only environment with a fixed numerical backend, which is what makes a green suite mean what it says |
| Enabling the four re-decided marketplace apps | Each needs its configuration file and a first run somebody reads. Until then each provides nothing, and `marketplace-apps.md` says so rather than implying coverage |
