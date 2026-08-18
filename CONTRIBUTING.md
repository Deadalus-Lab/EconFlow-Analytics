<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Contributing

Thank you for considering a contribution. This document is specific rather than generic, because the
project has a few rules that are genuinely unusual and are easy to violate in good faith.

## The one rule everything else follows from

**A gate is a refusal to compute, not a suggestion.** Every documented requirement of every method
raises and stops. If you find yourself softening a gate into a warning, adding a `skip`, or loosening
an assertion so that something passes, stop and reconsider — that is the one change this project
cannot accept, because it converts a structural guarantee into a probabilistic one, which is
precisely what the product claims not to be.

## Sign your work

This project uses the **Developer Certificate of Origin**, not a contributor agreement. Under a
uniform copyleft licence with no relicensing intent, an agreement buys nothing the licence does not
already give, and it is a real barrier to academic contributors.

Every commit needs a sign-off:

```bash
git commit --signoff        # or -s
git config --global format.signOff true    # set it once, never think about it again
```

By signing off you certify the [DCO 1.1](https://developercertificate.org/): that you wrote the
change, or have the right to submit it under this project's licence. The `dco` check enforces it.

## Setting up

You need **Python 3.12** and **uv**. The version is part of the reproducibility guarantee.

```bash
uv sync --locked --all-extras   # from the REPOSITORY ROOT -- see the warning below
cd engine
./run_verifications.sh          # must exit 0 before you start
```

> **Sync from the repository root, not from `engine/`.** `engine/` and `backend/` are the two members
> of **one `uv` workspace**, and the workspace manifest and its single `uv.lock` live at the root.
> Running `uv sync` inside `engine/` would treat that directory as its own project and resolve it
> independently, producing a second environment that satisfies the engine's manifest but not the
> lockfile that governs both members. Nothing would look wrong; the two layers would simply be free
> to land on different builds of `pydantic` or `pyarrow`.

> **Use `--locked`, always.** A plain `uv sync` will happily re-resolve when the lockfile does not
> satisfy the manifests, and quietly install something the lockfile does not describe. `--locked`
> fails instead. When it fails, the fix is to work out why the manifests moved — never to re-lock so
> that the error goes away, which would redefine the pinned set to whatever your machine wanted.

Start from a green suite. If it is red before you have changed anything, that is the bug worth
reporting.

## Anatomy of a wrapper

All 251 wrapper modules follow the same shape, and the uniformity is load-bearing: it is what makes
generated tooling possible across the whole catalogue. A new wrapper has six parts.

1. **A module docstring** naming the upstream package and the methods this module exposes.
2. **Arguments taken only from the upstream documentation**, each carrying its documented default.
   Constrained choices are a typed literal enumeration and are validated. Never invent an argument,
   and never guess a default.
3. **Gates.** Every documented hard requirement raises a typed engine error with a message that says
   what the rule requires. These are blockers.
4. **A structured result** — documented fields plus the fitted object. Never printing, never
   plotting. The engine emits chart *data*; the browser draws.
5. **Examples in the docstring**, never at module scope, so importing a module never runs one.
6. **An implementation-note footer** recording the functions used, what was deliberately omitted, the
   gates added, and any project-specific addition.

> **One old rule is gone, and you may have heard it.** Wrappers used to need a *uniquely named* call
> helper, because every wrapper file was loaded into one shared global environment and two files
> defining the same helper name meant the last one loaded silently won. Modules have their own
> namespaces. Two wrappers defining a private `_call` is now unremarkable, and the review
> configuration no longer flags it.

Gates are frequently *additions* rather than pass-throughs. A recurring finding while building this
catalogue was that libraries silently accept invalid input and return a plausible-looking object —
dropping missing rows with only a warning, broadcasting a mis-shaped argument, fitting a model on a
column of constants. Every such case became an explicit gate. Assume your package does this until you
have checked.

## Things that will fail review

- **Hand-editing anything under `engine/artifacts/`.** Those files are frozen inputs — the node
  specifications, the method cards, and 4855 parity verdicts that this engine is checked *against*.
  They are not regenerated from the code and must not be edited to make a test pass. If an edit is
  genuinely unavoidable, it is recorded in `engine/artifacts/PROVENANCE.md` with its reason and its
  new digest, and the sidecar is regenerated in the same change — see the one entry already there.
- **Hand-editing anything under `engine/src/econflow_engine/generated/`.** That tier is emitted by
  `scripts/gen_schemas.py`. Change the generator, re-run it, and commit what it produced — the
  `artifact-drift` gate re-emits it in `--check` mode and compares byte for byte, so a hand edit is
  caught on the next run rather than discovered later.
- **A network call in a wrapper.** The engine makes none: 0 of 251, and that is a verified property.
- **`eval`, `exec`, or `pickle` on anything a user supplied**, and `getattr` resolving a user-supplied
  string to a callable.
- **A stochastic method without a mandatory seed.**
- **Rendering a chart in the engine.** `matplotlib` is one import away, which makes this easier to
  break.
- **A statistical dependency in `backend/`** — see the next section.
- **Changing the lockfile or the linear-algebra thread settings** as a side effect of something else.
  Both are load-bearing for reproducibility; either is its own deliberate, measured change.
- **A dependency published under GPL-2.0-only.** This repository is AGPL-3.0-only, and the two
  are not compatible. Permissive licences and GPL-3.0-or-later combine without difficulty.

## Where code goes, and the rule that lost its enforcement

One top-level directory per **layer**. `engine/` owns **every statistic and every gate**; `backend/`
is platform integration; `frontend/` is the integration layer and the canvas.

> **No statistic is ever computed outside `engine/`.**

**This rule does not enforce itself and no longer does, which is worth understanding before you add a
dependency.** While the engine was the only place a statistical library could load, a tool wrapper
*could not* compute a mean even if its author wanted to. `backend/` and `engine/` are now the same
language and share one workspace, so nothing in the toolchain stops you.

What stops you is `.github/scripts/check-engine-boundary.sh`, run by the `engine-boundary` job. It
fails if `numpy`, `scipy`, `statsmodels`, `pandas`, `patsy`, `formulaic`, `scikit-learn`, `pyarrow`,
`polars`, `arch` or `linearmodels` appears in **any** dependency group of `backend/`. It checks
declarations rather than imports, because a dependency cannot be smuggled past a lockfile and the
declaration is what shows up in a diff.

The single sanctioned exception to the rule is a TypeScript port of `recommend()`, which exists only
to be validated against 114 committed fixtures. Zod schemas are **generated** from the engine
artifact and are never hand-written, because the contract can only be prevented from drifting if
nobody is allowed to type it out by hand.

**`.gitignore` names what is withheld**, and everything else is published — all 251 wrappers, the
generated tier, every artifact and fixture. What is withheld: working files (`CLAUDE.md`,
`.private/`), local tool caches, virtual environments and ordinary build
output. `.github/root-manifest.txt` declares the resulting root surface and
`check-root-visibility.sh` fails if a root entry appears **or** silently disappears.

Adding a file at the repository root therefore takes **two** edits in the same commit — the file and
its manifest entry. That diff is the review, and it is deliberate: this repository is public from its
first commit and its history cannot be rewritten.

Inside `engine/`, `backend/` and `frontend/` tracking is normal — a new wrapper needs no rule.

## Commits and pull requests

Conventional commits, with the vocabulary in `.github/semantic.yml`:

```
feat(engine): add the Hamilton regression filter wrapper
fix(engine): reject a mis-shaped weight matrix before the estimator sees it
```

The repository squash-merges and takes the commit subject **from the pull request title**, so the PR
title is the message that lands on `main`. The `semantic-pull-requests` check validates it.

Write the body in English, in a professional register, with bullet points describing what changed
and why.

## What runs on your pull request

| Check | What it proves | Required |
|---|---|---|
| **`ci-gate`** | **Every gate below reported `success`.** The only required check besides the DCO one | **yes** |
| `inventory` | The engine is the size we think it is — every other gate depends on this | via ci-gate |
| `spdx` | All 380 Python files declare `AGPL-3.0-only`, and any other identifier fails | via ci-gate |
| `artifact-drift` | Every generator reproduces its committed output byte for byte | via ci-gate |
| `py-lint` | `ruff`, with an assertion that it actually examined the corpus | via ci-gate |
| `engine-boundary` | No statistical dependency escaped into `backend/` | via ci-gate |
| `workflow-lint`, `container-lint`, `secrets`, `pip-audit` | Gates on the gates | via ci-gate |
| `dependency-review` | A pull request cannot add a `GPL-2.0-only` package or a high-severity advisory | via ci-gate |
| root-surface, required-contexts (inside `workflow-lint`) | The public root matches its manifest; no job rename has silently un-required a gate | via ci-gate |
| **`every commit carries Signed-off-by`** | DCO on every commit | **yes** |
| `engine-suite` | A path-selected subset of the suite | not required |
| CodeRabbit, `claude-review` | AI review | **no — advisory** |

### Adding a gate

> **A new gate joins `ci-gate`'s `needs:` list. It never joins the ruleset.**

The ruleset names exactly **two** contexts: `ci-gate` and the DCO check. That is not tidiness, it is
the fix for a specific failure. GitHub treats a required check it has never observed as permanently
*"Expected — waiting for status"*, so every separately-required leaf is an independent way to
deadlock `main` forever: skip one, rename one, or add a `paths:` filter to one, and no pull request
can ever merge again. GitHub's own guidance is *"avoid requiring workflows that can be skipped."*

`ci-gate` fails on any need whose result is not exactly `success` — **`skipped` and `cancelled` fail
it exactly like `failure` does**, because a gate that did not run has not passed. It also asserts
that all **nine** leaves reported, so a truncated `needs:` list cannot pass by examining almost
nothing. Adding a gate therefore means editing the `needs:` list **and** that number, in the same
commit.

`.github/scripts/check-required-contexts.sh` runs inside `workflow-lint` and enforces the coupling
that nothing in git otherwise expresses: a required context is matched by a job's **name string**, so
renaming a job for readability would silently stop the ruleset protecting anything. It also refuses a
`paths:` filter on a required workflow, and fails if any leaf job is missing from `ci-gate`'s needs.

**A marketplace app can never become a required check here**, and that is structural rather than a
policy: `needs:` can only name jobs in the same workflow, and an app reports its own check run. Four
apps had their verdict reversed on 2026-08-16 and are being enabled; every one of them is advisory.

### Writing a gate script

**Do not use `grep --exclude-dir`, `--include`, or `grep -P` in a gate script.** They are GNU
extensions, and `grep` is not always GNU grep — on one developer machine here it resolves to
**ugrep**, which silently ignores `--exclude-dir` and treats `--include` differently.

This is not theoretical, and the measurement is worth quoting because it is the exact failure this
rule exists to prevent. On this tree:

```
grep  -rl 'SPDX-License-Identifier' src scripts tests --include='*.py' | wc -l   # 315
/bin/grep -rl 'SPDX-License-Identifier' src scripts tests --include='*.py' | wc -l   # 380
```

The first is ugrep and it omits the entire 64-module generated tier without a word. CI runners ship
GNU grep, so a counting gate written that way passes there while **undercounting** locally — the
direction that lets a real gap through. Count with `find` and `xargs` instead:

```bash
find src scripts tests -name '*.py' -not -path '*__pycache__*' -print0 \
  | xargs -0 grep -l 'SPDX-License-Identifier' | wc -l
```

To scope to the published surface, use git — portable *and* checking exactly what would be published
rather than everything on disk:

```bash
git ls-files --others --exclude-standard --cached | grep -v '^docs/' | xargs -r grep -l 'PATTERN'
```

If you genuinely need a GNU-only flag, call `/bin/grep` explicitly and say why in a comment.

**Neither AI review is ever a required check.** They are non-deterministic, and a check that can
answer differently on a re-run is not a gate. The deterministic gates decide what is correct.

**A note for contributors working from a fork.** `claude-review` does not run on your pull request,
by design: fork pull requests receive no secrets, and the usual workaround
(`pull_request_target`) would run with write permissions against untrusted code — the standard route
to leaking a repository's secrets. You still get CodeRabbit, which works on forks through its own
app, and every deterministic gate. This is a deliberate trade, not an oversight.

**One honest gap**, also recorded in `ARCHITECTURE.md` §11.4: the per-pull-request suite run is
path-selected, so a change touching a wrapper whose tests are not matched by basename can merge
green. The full suite runs on every push to `main` and opens a `broken-main` issue if it fails. If
your change is broad, add the `full-suite` label and get the whole thing on your PR.

## Reporting a bug

Open an issue with the template. For a numerical discrepancy, include your interpreter version, the
output of `uv sync --locked --dry-run`, and a minimal reproducible example — the smallest series that
shows the problem. The second of those matters more than it looks: an environment that has drifted
from the lockfile still passes the suite, it just stops demonstrating the pinned numbers.

Security issues go through [`SECURITY.md`](SECURITY.md), never a public issue.
