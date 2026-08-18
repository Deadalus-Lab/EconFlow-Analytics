<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Marketplace apps: what is on, what is off, and why

**Date:** 2026-08-15 · **Re-decided:** 2026-08-16 · **Status:** decided

Eleven GitHub apps are installed on the `Deadalus-Lab` organisation, all with
`repository_selection: all`, so each one attaches to this repository
automatically unless it is excluded.

**Four are configured. Four are deliberately disabled. Three had their verdict
reversed on 2026-08-16 and are being enabled.** None is left installed-but-inert,
because an app that is installed and does nothing is worse than one that is
absent: it looks like coverage.

The recurring reason for disabling *was* the **anti-vacuity** rule in
`ARCHITECTURE.md` §11.1 — *a gate that passes because it examined zero files has
not passed*. Several of these apps do not support that language. Pointed at a single-language
repository they analysed nothing, found nothing, and reported a green quality
gate: not a neutral outcome, but a false claim of coverage on the pull-request
page.

**That reason expired with the language.** The compute engine is Python, which
every one of those apps analyses as a first-class language. Leaving them off now
would be the opposite error — declining real coverage on the strength of an
argument that has stopped being true.

---

## The re-decision, and the one verdict that did not move

| App | Old reason | Does it survive? |
|---|---|---|
| **sonarqubecloud** | "the engine's language was not analysed" | **No.** Python is among its best-supported languages. Verdict reversed. |
| **sonarqube-agent** | The AI companion to the above, same reasoning | **No.** Reversed with it. |
| **endor-labs-github-agenthq** | The engine's lockfile was not in a supported ecosystem | **No.** Endor Labs covers Python explicitly, and `uv.lock` is a lockfile it resolves. Verdict reversed. |
| **CodeQL** | Deferred until TypeScript existed | **No.** Python is a CodeQL language. Verdict reversed. |
| **codspeed-hq** | "Supports Python, Rust, Node and Go — **no the engine**" *and* "the thesis of this project is correctness, not speed" | **Partly.** The language half is void; the second half is not, and it was always the stronger of the two. **Stays disabled.** |
| **keploynavigator** | Generates API tests from recorded HTTP traffic, against an architecture with no HTTP surface | **Yes, and more firmly.** The router is gone rather than merely deprecated. Stays disabled. |
| **cla-bot** | Redundant beside a DCO sign-off | **Yes.** Unaffected by the language. Stays disabled. |
| **giscus** | Needs a documentation site that does not exist | **Yes.** Stays disabled. |

`codspeed-hq` is the entry worth pausing on. Four of these were disabled on a
language argument alone, and all four reverse. CodSpeed was disabled on a
language argument **and** a product argument, and only one of the two expired.
The only timing figure that means anything here is the full suite, which is not
a microbenchmark. Re-enabling it because "it supports Python now" would be
reversing a decision on a premise that was never load-bearing.

---

## Configured

| App | Config | Role |
|---|---|---|
| **coderabbitai** | `.coderabbit.yaml` | AI review. **Advisory, never required.** Generated artifacts are excluded by path filter — a 2.7 MB diff of machine-written JSON would crowd out every comment about code a human wrote. Those files are gated far more strictly elsewhere, by the `--check` generators and their SHA-256 sidecars. Works on fork pull requests, which makes it the review layer outside contributors actually get. |
| **gitguardian** | `.gitguardian.yaml` | Secret scanning, second opinion beside GitHub's native push protection. **Advisory.** The authoritative secret gate is the `secrets` job in `ci.yml`, because that one carries a positive control: it plants a known-fake credential and fails if detection does not catch it. An app whose verdict we cannot force cannot host a control like that. |
| **pre-commit-ci** | `.pre-commit-config.yaml` | Runs the same hooks in CI that run locally, and auto-fixes trivial issues. Free for public repositories. Every hook now runs there, because `ruff` is a single binary — under the engine the engine's lint had to stay local-only. |
| **semantic-pull-requests** | `.github/semantic.yml` | Validates the pull-request title. This matters more than it looks: the repository squash-merges with the subject taken from the PR title, so validating the title *is* validating the commit subject that lands on `main`. |

## Verdict reversed — enabling

Each is a change of its own, because each brings a configuration file and a
first run that has to be read before anyone trusts it. **Until that change
lands, each provides nothing**, and this table is a decision rather than a claim
of coverage — the distinction `ARCHITECTURE.md` §11.1 exists to keep.

| App | What it needs | What it adds |
|---|---|---|
| **sonarqubecloud** | the SonarQube project file naming `engine/src` and `backend/`, plus a `SONAR_TOKEN` repository secret | Quality gate over roughly 315 lint-eligible Python files. Configure the generated tier as an exclusion: it is machine-written and its findings would be the emitter's, not ours. |
| **sonarqube-agent** | Nothing beyond the above | AI companion to that analysis. |
| **endor-labs-github-agenthq** | Repository access, pointed at `uv.lock` | Dependency and reachability analysis. It **overlaps** the `pip-audit` job rather than replacing it: that job asserts the package count before trusting a verdict, which is a control an app we cannot force cannot host. |
| **CodeQL** | `.github/workflows/codeql.yml`, `security-events: write` | Static application-security analysis — one of the items `ARCHITECTURE.md` §11.3 lists as decided but not built (`U54`). This closes the Python half of it. |

### The interaction with `check-required-contexts.sh`

Re-enabling four analyses adds four or more check runs to every pull request.
That is the part worth stating explicitly, because it touches the gate
architecture:

- **None of them joins `.github/rulesets/main.json`.** The ruleset names exactly
  two contexts, `ci-gate` and the DCO check. A required check GitHub has never
  observed stays `Expected` forever, and a third-party app can be renamed,
  rate-limited or fail to report entirely — every one of those is a permanent
  merge deadlock. `check-required-contexts.sh` fails if a ruleset context does
  not resolve to a job `name:` in a workflow, so adding an app context there
  would turn that gate red immediately. That is the gate working.
- **None of them can join `ci-gate` either**, and this is structural rather than
  a policy choice: `ci-gate` aggregates `needs:`, and `needs:` can only name
  jobs in the same workflow. An app that reports its own check run is not a job
  in `ci.yml`, so there is no mechanism by which it could ever become required.
- **The consequence is the correct one.** These four are advisory, exactly like
  CodeRabbit, for exactly the same reason: a non-deterministic verdict that can
  differ on a re-run is not a gate. They tell a reviewer where to look. The
  deterministic gates in `ci.yml` decide what is correct.
- **CodeQL is the one that could become required** if it is written as a
  workflow in this repository rather than delivered as an app check, since a job
  in a workflow can join `ci-gate`'s `needs:`. Whether it should is `U54`. Note
  the arithmetic if it does: `ci-gate` asserts a leaf count, so adding it means
  editing that number and the `needs:` list in the same commit.

## Disabled

| App | Why |
|---|---|
| **cla-bot** | Redundant. The contribution instrument is a **DCO sign-off** (`U3`), enforced by `.github/workflows/dco.yml`. Under a uniform AGPL-3.0-only licence with no relicensing intent, a contributor agreement buys nothing the licence does not already provide, and it is a documented barrier to the academic contributors §1 names as an audience. |
| **codspeed-hq** | The language objection expired; the product objection did not. The thesis of this project is correctness, not speed (§1). The only timing figure that means anything here is the full suite, which is not a microbenchmark. Revisit if a benchmark suite is ever written with a reason to track it — and only then. |
| **keploynavigator** | **Actively contrary to the architecture.** Keploy generates API tests from recorded HTTP traffic. `ARCHITECTURE.md` §2 states that the engine is not a service, and §6.3 records that the HTTP router and its 913 routes are gone, because Galaxy's job runner supersedes them. This app exists to test precisely the design this project rejected. Leaving it installed would create a standing incentive to keep an HTTP surface alive so that it has something to record. |
| **giscus** | Discussions-backed comments for a documentation site. Neither `web/` nor a docs site exists yet. Revisit at v1.0; it needs Discussions enabled and a category, and no repository config file. |

---

## How they are disabled

Installation scope is an **organisation-level** setting and needs the
`admin:org` scope, so it is done through the web interface rather than scripted:

> Organisation → Settings → GitHub Apps → *app* → Repository access →
> **Only select repositories** → exclude `EconFlow-Analytics`

Until that is done, a disabled app may still post checks. The canary pull
request verifies the end state: it must show the configured apps and **no** check
from the four above.

## Revisit points

| When | Re-enable |
|---|---|
| A documentation site exists | giscus |
| A benchmark suite exists with a reason to track it | codspeed-hq — but only then |
| Never, unless the architecture changes | keploynavigator |
| Never | cla-bot, unless the licensing posture changes |
