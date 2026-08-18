<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `.github/` — the gate architecture

Five workflows, sixteen jobs, eight shell scripts and one composite action. This file says what each is
for, which of them can block a merge, and — for every gate — what stops it passing because it
examined nothing.

> **Nothing here has ever run against the remote.** There are no commits and nothing has been
> pushed, so every job below is a description of intent until it has been observed passing on correct
> input *and* failing on planted-defect input. The shell gates in `scripts/` have each been run
> locally against a planted defect and observed to refuse it; the workflow jobs have not, and cannot
> be until the first push.

---

## One required check, and only one

`.github/rulesets/main.json` names exactly two required contexts:

| Context | From |
|---|---|
| `ci-gate` | `ci.yml` |
| `every commit carries Signed-off-by` | `dco.yml` |

**A new gate joins `ci-gate`'s `needs:`. Nothing joins the ruleset.** GitHub treats a required check
it has never observed as permanently *"Expected — waiting for status"*, so every required context is
an independent way to deadlock `main` forever: skip it, rename it, or add a `paths:` filter to its
workflow and no pull request can merge again. This ruleset used to name nine leaf jobs — nine such
risks. `check-required-contexts.sh` enforces the arrangement mechanically.

`ci-gate` carries `if: always()`, which is load-bearing rather than defensive: without it the
aggregate is itself skipped when a leaf fails, which is the deadlock it exists to prevent. It fails
on any leaf result that is not exactly `success` — `skipped` and `cancelled` fail like `failure` —
and it asserts how many leaf results it saw, so a truncated `needs:` cannot pass by examining almost
nothing.

---

## Workflows

| File | Trigger | Jobs | Required |
|---|---|---|---|
| `ci.yml` | pull request, push to `main`, dispatch | 10 | `ci-gate` only |
| `dco.yml` | pull request | 1 | yes |
| `engine-suite.yml` | pull request, push to `main`, nightly, dispatch | 2 | no |
| `claude-review.yml` | pull request | 1 | **never** |
| `claude.yml` | `@claude` mention on an issue or comment | 1 | **never** |

The two Claude workflows are advisory by design and by three independent arguments: they are
non-deterministic, so a required check could answer differently on a re-run; they depend on a
third-party API whose outage would block every release; and they cannot run on fork pull requests,
which receive no secrets, so requiring them would permanently exclude outside contributors.
`claude-review.yml` skips fork pull requests deliberately and does **not** use
`pull_request_target` — that trigger exposes secrets to code an untrusted contributor wrote, which is
the standard route to exfiltrating a public repository's secrets.

`engine-suite.yml` runs a path-selected subset per pull request, the full suite on every push to
`main`, an opt-in `full-suite` label for a risky branch, and a nightly full run. What that does *not*
buy is stated plainly in ARCHITECTURE §11.4: a pull request touching a wrapper whose tests the path
selector misses can still merge green. The post-merge run turns *silently* broken into *loudly*
broken, which is a real improvement and is not the same as per-pull-request protection.

---

## The eleven `ci.yml` jobs

Every job asserts a minimum quantity of work done, because a gate that passed because it examined
zero files has not passed (ARCHITECTURE §11.1). The floors themselves belong in
`.github/inventory.json` rather than in the workflow — see
See the floors recorded in `.github/inventory.json` for the ones that are
still literals.

| Job | Asserts | Anti-vacuity floor |
|---|---|---|
| `inventory` | every manifest constant re-measured from the tree | `"unmeasured"` is a hard failure, never a pass |
| `spdx` | every `.py` file declares `AGPL-3.0-only`, and only that | scanned-file count, below which the glob is wrong |
| `artifact-drift` | each generator re-run in `--check` mode reproduces its committed bytes | generators run must equal `engine.generators` |
| `py-lint` | `ruff` at a pinned version, zero findings | ruff's own `--show-files` count |
| `workflow-lint` | actionlint, shellcheck, root surface, required contexts | workflow count, script count |
| `engine-boundary` | `backend/` declares no statistical dependency | plants a manifest declaring one and fails if uncaught |
| `secrets` | gitleaks over the whole history | a runtime-synthesised credential must be detected |
| `container-lint` | hadolint, and every `COPY` source resolves | Dockerfile count |
| `pip-audit` | OSV scan of the workspace lockfile | package count must equal `engine.py_packages` |
| `dependency-review` | the pull request's dependency diff: no `GPL-2.0-only` licence, no high-severity advisory | runs only where a diff exists (`pull_request`); on `push` it states that and passes — the canary PR must show it examining a non-empty diff |
| `ci-gate` | every leaf reported exactly `success` | leaf-result count |

Three of these carry a **positive control** — a planted defect the job must catch before its verdict
counts. `secrets` synthesises a known-fake credential outside the working tree, because a
`.gitleaks.toml` missing `[extend] useDefault = true` defines zero rules and passes forever, green
and useless. `engine-boundary` plants a backend manifest declaring `statsmodels`, which is what keeps
it honest while `backend/` still holds no code. `inventory` earns the same status differently: it
refuses to treat an unmeasurable constant as a verified one.

Every Python-dependent job pins its interpreter with `actions/setup-python` reading
`engine/.python-version`. Every third-party action is pinned by full commit SHA, and every downloaded
binary is verified against its published checksums — keeping the archive's published filename,
because `sha256sum -c` resolves the name written in the checksum line and renaming the download makes
verification fail to find its own file.

---

## `.github/inventory.json` — the single home for every asserted constant

Every quantity any gate asserts lives here, once, beside the command that reproduces it. That is the
whole mechanism: **a legitimate change to the engine becomes a visible one-line diff in this file**,
reviewed on its own merits, and a gate can never be weakened silently because weakening it means
editing a number where a reviewer will see it. Comparisons are exact equality, not `>=`.

Two properties are easy to miss. `"unmeasured"` is a **hard failure**, not a placeholder: it marks a
constant whose measuring artifact is not in the tree yet, and a gate that cannot start must never
look like a gate that passed. And the file's `_note_on_grep` records a measured host divergence —
`grep` resolving to ugrep 7.5.0, whose `--include` saw 315 files where GNU grep saw 380 — which is
why every count uses `find | xargs` and never `grep -r --include`.

`assert.sh` inside the composite action is what re-measures all of it. It is a real script rather
than inline YAML so a human can run it before editing a constant:

```sh
bash .github/actions/assert-inventory/assert.sh engine .github/inventory.json
```

---

## Shell gates

Eight scripts, kept out of YAML so each can be run and negative-controlled locally.

| Script | What it refuses |
|---|---|
| `check-required-contexts.sh` | a required context with no matching job `name:`; a leaf missing from `ci-gate`'s `needs:`; a `paths:` filter on a required workflow |
| `check-root-visibility.sh` | any difference between the tracked root surface and `root-manifest.txt`, in **either** direction |
| `check-engine-boundary.sh` | a numerical distribution in any dependency group of `backend/` |
| `check-dockerfile-paths.sh` | a `COPY` source that does not exist in the build context |
| `check-vocabulary.sh` | vocabulary borrowed from another ecosystem outside `vocabulary-allowlist.txt`; a scan that examined fewer files than the manifest's floor; a pattern that fails its own planted positive control |
| `check-toolchain-pin.sh` | disagreement between the `.python-version` files, the `requires-python` floors and `ci.yml`'s `PYTHON_VERSION`; a dependency snapshot date authored in more than one place |
| `apply-ruleset.sh` | applying the ruleset against contexts GitHub has never observed |
| `check-repo-settings.sh` | drift in the GitHub-side settings that git cannot see: Actions restricted to GitHub-owned plus an explicit allowlist with SHA pinning required, read-only workflow token, squash-only merges, secret scanning and push protection, CodeQL default setup, every ruleset in `rulesets/` live with the same target, the languages actually used in the topics. Runs locally with an admin `gh` login (pre-flight), not under `GITHUB_TOKEN` |

`apply-ruleset.sh` is an applier rather than a gate, and it is the one thing here that changes a
repository *setting*. It runs **after** the canary pull request, never before: GitHub will not accept
a required context it has not seen. Three bugs in it were found by running it — a path that broke
when the script moved into `.github/scripts/`, a `--dry-run` flag silently swallowed as the repository
name, and a doubled stdin redirection that made its NOT-SEEN preflight print nothing at all.

**No gate script may use `--exclude-dir`, `--include` or `grep -P`.** On a maintainer machine `grep`
is ugrep 7.5.0, which ignores `--exclude-dir` outright; a sweep written that way reported a clean
tree while skipping 55 lines of untranslated text. Scope to the published surface with
`git ls-files … | xargs grep -l`, or call `/bin/grep` explicitly with a stated reason.

---

## Everything else in this directory

| Path | Purpose |
|---|---|
| `actions/assert-inventory/` | the composite action wrapping `assert.sh` |
| `rulesets/main.json` | the branch ruleset; two contexts, applied by `apply-ruleset.sh` |
| `root-manifest.txt` | the complete public root surface, one entry per line |
| `dependabot.yml` | GitHub Actions and pip, grouped, with a 14-day cooldown |
| `CODEOWNERS` | review routing; the artifacts sit on their own line by design |
| `ISSUE_TEMPLATE/` | bug report, method request (which asks a proposed package's licence) |
| `PULL_REQUEST_TEMPLATE.md`, `semantic.yml` | pull-request shape and accepted scopes |

The method-request template asks for a package's licence because ARCHITECTURE §13 has a hard edge:
AGPL-3.0 is **not** compatible with GPL-2.0-only, so a GPL-2.0-only dependency can never be admitted
to this tree whatever its merits.
