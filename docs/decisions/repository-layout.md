<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Repository layout and the public root surface

**Date:** 2026-08-15 · **Revised:** 2026-08-16 · **Status:** decided and applied

---

## Decision

Three things, taken together:

1. **One top-level directory per LAYER.** `engine/` (compute), `backend/` (platform integration),
   `frontend/` (integration libraries and canvas). Named for the layer each owns rather than for a
   language, which is what lets `engine/` and `backend/` both be Python without the layout becoming
   incoherent — see [`python-engine.md`](python-engine.md) §1.
2. **`.gitignore` is an explicit deny-list.** It names what is not published — working files
   (`CLAUDE.md`, `todo.md`, `.private/`), local tool caches, virtual
   environments and ordinary build output. Everything else is published.
   `.github/root-manifest.txt` declares the resulting root surface and
   `.github/scripts/check-root-visibility.sh` fails on a difference in either direction.
3. **`CLAUDE.md` is not published.** `docs/ROADMAP.md` carries the public plan.

## Why

**The boundary that earns a directory is the layer boundary, not the language boundary.** An earlier
revision of this document justified the split by giving each toolchain one unambiguous home, which
worked while the three roots held three languages. It stopped working the moment `engine/` and
`backend/` became the same language sharing one workspace, and the layout survives on the better
argument: a researcher auditing the econometrics reads `engine/` and nothing else, whatever language
the platform layer happens to be written in.

**Everything the project is, is published.** All 251 wrapper modules, the 64-module generated tier,
every artifact, every fixture, the CI and the docs. Measured, not asserted — see the verification
table below.

**The generated tier is committed, and that is the counter-intuitive part.** The reflex with
machine-written code is to ignore it. `engine/src/econflow_engine/generated/` is committed
deliberately: the generated form is what gets reviewed in a diff, and the `artifact-drift` gate
re-emits it in `--check` mode and compares byte for byte. Ignoring it would delete the review surface
and leave the gate comparing a generator against itself.

**An earlier revision of this file specified deny-by-default at the root** — `/*` followed by
re-admission by name. It was replaced with the explicit deny-list above on the maintainer's
instruction. The published result is identical; what changed is that the file now reads as a list of
what is withheld rather than a list of what is permitted, which is the standard form and does not
invite the reader to wonder whether source is being hidden.

## Consequences

- Working files are named explicitly: `CLAUDE.md`, `todo.md`, `.private/`,
  plus the local tool caches `.fastembed_cache/` and `.token-optimizer/`. A new tool cache will need
  a new line — the trade accepted when moving off deny-by-default.
- **The workspace manifest and its lockfile are root files**, because `engine/` and `backend/` are
  two members of one `uv` workspace. They are therefore two more entries on the public root surface,
  and adding them means editing `.github/root-manifest.txt` in the same commit.
- `backend/`, `frontend/` and `deploy/` each hold one `README.md` saying the layer is not built.

## Alternatives rejected

| Option | Why not |
|---|---|
| Literal language names `python/` `typescript/` | Two of the three layers are Python. A `python/` root would have to contain both the compute engine and the platform integration, which is precisely the boundary the layout exists to draw |
| Merge `engine/` into `backend/` now that both are Python | The rule *no statistic is ever computed outside `engine/`* would lose the directory it names. The check that enforces it works by asking which dependency group a package appears in, and one merged manifest has only one |
| One lockfile per member | The engine defines the wire contract and the backend consumes it. Two resolutions can put them on different builds of `pydantic` or `pyarrow`, and the symptom is a validation failure on a boundary both sides believe they agree on |
| Keep `web/` and `packages/` as separate roots | TypeScript in two top-level directories; one pnpm workspace spanning both |
| Deny-by-default across the entire tree | A new wrapper module would be invisible to `git status`; at 251 wrappers a contributor would eventually open a pull request omitting the file they just wrote |
| Deny-by-default at the root only | Adopted first, then replaced: the published result was identical, but a `.gitignore` opening with `/*` reads as "hide everything" and obscures that all source is published |
| Publish `CLAUDE.md` | It is agent operating instructions, not project documentation |

## Two traps measured during execution

Recorded because both fail *green*, which is the only failure mode this repository treats as urgent.

**The Docker build context must stay the repository root.** A design proposed moving it to `engine/`,
claiming this would let `COPY` sources stay bare. `Dockerfile` step 2a `COPY`s `LICENSE` — the licence
requires its text to accompany the binaries — and step 1 `COPY`s the root `pyproject.toml` and
`uv.lock`. Docker cannot reach outside its context; a symlink does not work either. So the context is
the root, `COPY` sources carry `engine/` prefixes, and `Dockerfile` and `.dockerignore` stay at the
root beside it.

**The engine-suite path selector is cwd-relative, and making it look more explicit breaks it.**
`engine-suite.yml`'s subset step sets `working-directory: engine`, and **git pathspecs resolve
against the current directory**. So the correct pathspec is `'src/**/*.py'`. The seemingly more
careful `'engine/src/**/*.py'` matches **nothing** from there — the changed-file list comes back
empty, the step exits 0, and a green run means the selector found no changes rather than that the
changes passed. Measured in a throwaway repository under the previous layout and unchanged by the
layout, which only alters the extension in the pattern.

## Verification

| Claim | Evidence |
|---|---|
| Every measurable inventory constant holds | `assert.sh engine .github/inventory.json` re-measures each with the command recorded beside it: 251 wrappers / 30 categories / 913 methods / 3 generators / 23 infrastructure modules / 3 test modules / 1 conftest / Python 3.12; artifacts 913 / 30 / 252 / 4855 / 114 / 6 sidecars; SPDX 380 of 380; 0 of 913 methods implemented |
| Two constants are deliberately unmeasurable, and read red | `py_packages` and `sbom_components` are marked `unmeasured` in the manifest, because the root `uv.lock` and a Python-derived SBOM are not in the tree yet. `assert.sh` prints `OWED` and exits 1 for each. An unmeasurable constant must never read as a verified one |
| The ignore rule does what it claims | `check-root-visibility.sh .` → `ok: public root surface matches the manifest (25 entries)` |
| The gate can go red | Three negative controls: an unreviewed file appearing, a tracked file vanishing, and a truncated manifest. All exit 1 |
| The engine boundary is enforced, not merely stated | `check-engine-boundary.sh .` passes its own positive control — a planted `backend/pyproject.toml` declaring `statsmodels` is caught — before reporting on the real tree |
| The required-context coupling holds | `check-required-contexts.sh .` → 2 of 2 contexts resolve; `ci-gate needs 9 of 9 leaf jobs`; no paths filter on a required workflow |
| No `COPY` path is stale | `check-dockerfile-paths.sh Dockerfile .` → 15 of 19 resolve. The four that do not are `pyproject.toml`, `uv.lock`, `backend/pyproject.toml` and `engine/README.md`, all owed by the workspace change. This is the gate working, not the gate broken |
| Every `CODEOWNERS` path resolves | 13 of 15. The two outstanding are `/pyproject.toml` and `/uv.lock`, the same owed pair |
| The lint floor still holds | `ruff check --show-files .` → 315 candidate files from `engine/`, floor is 300 |
