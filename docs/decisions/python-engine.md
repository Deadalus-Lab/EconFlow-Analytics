<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# The Python engine, and how the layer boundary is enforced

**Date:** 2026-08-16 · **Status:** decided

The compute engine is Python. This document records the two structural
consequences that follow: how the top-level layout is justified when both server
layers share one toolchain, and what enforces the project's central rule when no
file name can.

---

## 1. One directory per LAYER, not per language

One directory per *toolchain* would be the obvious rule, and it is the wrong one
here: `engine/` and `backend/` are both Python and share one toolchain, so that
rule would argue for merging them. They are separate because they answer to
different concerns — one computes a number, the other moves it around — and a
researcher looking for the econometrics should not have to read the platform
code to find it.

| Layer | Root | Owns |
|---|---|---|
| Compute engine | `engine/` | **Every statistic and every validation gate** |
| Platform integration | `backend/` | Job execution, scheduling, data management, users, provenance |
| Integration layer | `frontend/packages/` | Graph ↔ workflow translation, typed API client, state mapping |
| Web canvas | `frontend/web/` | All rendering, including every chart |

The boundary that matters was never between languages. It is between *a thing
that computes a number* and *a thing that moves a number around*, and that
boundary is worth a directory whether or not the two sides speak the same
language. A researcher auditing the econometrics reads `engine/` and nothing
else; that property is unchanged and is the whole reason for the split.

## 2. One uv workspace, two members

```
EconFlow-Analytics/
├── pyproject.toml        [tool.uv.workspace] members = ["engine", "backend"]
├── uv.lock               ONE resolution, covering both members
├── engine/pyproject.toml  member: econflow-engine
└── backend/pyproject.toml member: econflow-backend
```

**One lockfile, at the root.** The engine defines the wire contract in
`econflow_engine.kinds` and the backend consumes it. Two independent resolutions
could put them on different builds of `pydantic` or `pyarrow`, and the symptom
would be a validation failure on one side of a boundary that both sides believe
they agree on. A workspace resolves both members together, so that cannot
happen. A member never declares `[tool.uv.workspace]` itself.

`assert-inventory` asserts the negative form of this directly: if
`engine/uv.lock` ever exists, the workspace has been split by accident and the
gate fails.

**The dated package snapshot is gone, and nothing replaces it.** The previous
lockfile needed a dated-mirror variable beside it, because that index rebuilds
binaries under an unchanged version number — so version equality was not byte
equality, and the date had to be repeated in a second file to keep continuous
integration restoring what the lockfile pinned. PyPI artifacts are **immutable**:
a released filename and its hash can never be replaced, and `uv.lock` records
those hashes. The pin is therefore stronger than the dated snapshot was, and it
lives in one file instead of two. The script that existed only to keep those two
copies of one date in agreement was deleted with them.

## 3. The rule survives; its enforcement had to be rebuilt

> **No statistic is ever computed outside `engine/`.**

`backend/` and `engine/` are the same language, so nothing about a file's name
says which layer may compute a statistic. One `import statsmodels` in a Galaxy
tool wrapper moves a statistic out of the engine, and no toolchain would notice.
That would be discovered the first time somebody computed a mean in a tool
wrapper "just to fill in a metadata field" — which is to say, far too late.

**The rule is therefore a checked contract, not a convention.**

**The replacement is `.github/scripts/check-engine-boundary.sh`**, run by the
`engine-boundary` job in `ci.yml`. It asserts that no numerical or statistical
distribution appears in **any** dependency group of `backend/`: not
`project.dependencies`, not an optional extra, not a `dependency-groups` entry,
not a `requirements*.txt`. The forbidden set is `numpy`, `scipy`,
`statsmodels`, `pandas`, `patsy`, `formulaic`, `scikit-learn`, `pyarrow`,
`polars`, `arch` and `linearmodels`.

Three choices in that design are deliberate:

| Choice | Why |
|---|---|
| It checks **declarations**, not `import` statements | A dependency cannot be smuggled past a lockfile, whereas an import can be spelled `__import__("numpy")`. The declaration is also the reviewable artifact: it appears in a diff. |
| It carries a **positive control** | `backend/` holds no code yet, so a detector pointed at it finds nothing and looks exactly like a detector pointed at a clean tree. The script plants a manifest declaring `statsmodels` outside the working tree and fails if that is not caught — the same discipline as the gitleaks canary. Without it this gate would go green forever from the day it broke. |
| It lists `pyarrow` as forbidden | Arrow is the serialisation format at the boundary, so the temptation to add it to the backend is real. The backend moves *files*; it does not open them. If that ever has to change, it is a decision with a diff, not a dependency somebody added on a Tuesday. |

The single sanctioned exception to the rule is unchanged: the TypeScript port of
`recommend()`, validated against **114 fixtures generated for
implementation**, running as a *post-hoc judge* — never as a tool a model may
call, because a tool can be left uncalled.

## 4. Pins

| What | Pin | Where |
|---|---|---|
| Python version | **3.12** | `engine/.python-version`, `backend/.python-version` |
| Packages | by version **and hash** | `uv.lock` at the repository root |
| Linear algebra | every thread pool set to **1** | `Dockerfile`, `engine-suite.yml` |
| Lint | `ruff`, floor of 300 candidate files | `engine/ruff.toml` |
| Format | **none, deliberately** | see `.pre-commit-config.yaml` |

**On the linear-algebra pin.** The the engine image installed reference netlib BLAS
because the base image shipped a multithreaded OpenBLAS that perturbed sensitive
fits. NumPy and
SciPy ship a threaded OpenBLAS *inside their wheels*, so the same hazard exists
and there is no `update-alternatives` to switch it. What is available instead is
the thread count: OpenBLAS's reduction order depends on how work was split
across threads, so pinning every pool to one removes that variation. It is a
weaker guarantee than swapping the library — two different wheel builds can
still differ — and `engine-suite.yml` says so in place rather than implying the
old guarantee carried over.

**On the absence of a formatter.** `ruff format` and `black` are forbidden here
for exactly the reason `styler` and `formatR` were: a formatting pass would
rewrite the 64-module generated tier, putting it out of step with the generator
that emits it, turning `artifact-drift` red and forcing a regeneration whose
diff nobody can review. The hazard did not change with the language; only the
tool's name did.

---

## What this document does not decide

- Which Galaxy release line is pinned (`U8`), and therefore whether the backend
  member's floor can stay at 3.12.
- Whether `patsy` or `formulaic` is adopted for formula handling. Both evaluate
  in a caller-supplied namespace, which is a **new** security surface rather
  than the engine one carried over; `SECURITY.md` records the gap explicitly and owes
  a section the moment either is admitted.
- The TypeScript component library, state management and routing (`U31`–`U33`).

See [`repository-layout.md`](repository-layout.md) for where each layer's files
live and how the public root surface is enforced.
