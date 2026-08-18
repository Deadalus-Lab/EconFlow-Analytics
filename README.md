<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# EconFlow Analytics

A node-based canvas for end-to-end macroeconomic analysis. You wire nodes on a graph, each node is a
rigorously gated econometric method, and the graph executes as a durable directed acyclic graph. The
reference point is KNIME, narrowed to macroeconomics.

**Licence:** AGPL-3.0-only, the entire repository, without exception.

> **Status: the compute engine is complete; the platform around it is not.**
> This repository currently contains Layer 1 — the Python engine, its 251 wrappers, its gates and its
> suite. The Galaxy integration, the web canvas and the agent subsystem are specified in
> [`ARCHITECTURE.md`](ARCHITECTURE.md) and not yet built. That document marks precisely what exists
> and what does not; nothing here is described as finished when it is not.

## The claim

**Correctness is structural, not probabilistic.** Four mechanisms, each doing one job:

| Mechanism | Effect |
|---|---|
| **Rule-based method selection** | Which method suits which data is decided by sourced decision trees, not by a language model's judgement. |
| **Hard validation gates** | Every documented requirement of every method is an explicit refusal to compute. An invalid result cannot escape; it becomes a blocked node with a stated reason. |
| **Generated typed schemas** | Node schemas are generated from the committed node-specification artifact, never hand-copied, so the contract cannot drift from the implementation. |
| **Pinned computation** | Python version, package versions, package *hashes*, and the linear-algebra thread count are all pinned. The same input produces the same number. |

Where a language model is used at all, it wires and configures nodes. It never computes a statistic
and never overrides a gate — and that boundary is enforced by construction rather than by
instruction. See [`ARCHITECTURE.md` §8](ARCHITECTURE.md).

A gate is not an error. When a wrapper refuses to run because its documented preconditions are not
met, the system is working. The user is shown *which rule* blocked the node and *what that rule
requires* — not a stack trace.

## Verified inventory

Every figure below is reproduced by the command beside it, **run from `engine/`**. No number in this repository is quoted
from memory, and none is restated in a second place — a second copy of a number is a number that
rots.

| Quantity | Value | Command |
|---|---:|---|
| Wrapper modules | **251** | `find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' \| wc -l` |
| Category packages | **30** | `find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' \| wc -l` |
| Executable methods (nodes) | **913** | `python3 -c "import json;print(json.load(open('artifacts/node-specs.v1.json'))['engine']['n_nodes'])"` |
| Method cards | **252** | `python3 -c "import json;print(json.load(open('artifacts/method-cards.v1.json'))['source']['n_cards'])"` |
| Frozen parity verdicts | **4855** | `python3 -c "import json;print(json.load(open('artifacts/parity-fixtures.v1.json'))['n_cases'])"` |
| Python files carrying an SPDX header | **380 / 380** | `find src scripts tests -name '*.py' -not -path '*__pycache__*' \| wc -l` |
| Python version | **3.12** | `cat .python-version` |

Those figures are asserted on every pull request by
[`.github/inventory.json`](.github/inventory.json) and its `assert-inventory` action, which
re-measures each one with the command recorded beside it. Changing a number means editing that file,
where a reviewer sees it.

Run the suite rather than trusting any line above:

```bash
cd engine && ./run_verifications.sh
```

## Repository layout

One top-level directory per **layer**, so a researcher can find the econometrics without reading
anything else:

```
engine/       Python      the compute core -- 251 wrappers, 913 methods, all statistics and gates
backend/      Python      Galaxy platform integration            (specified, not built)
frontend/     TypeScript  integration layer and the web canvas   (specified, not built)
deploy/                   Compose, proxy and service definitions (specified, not built)
docs/                     decision records and the roadmap
.github/                  continuous integration and its manifests
```

The three unbuilt directories say so in their own `README.md`, naming what will live there and
which open decisions block it. `frontend/` and `deploy/` hold nothing else. `backend/` also carries
a `pyproject.toml`, a `.python-version` and an empty `econflow_backend` package, because it is the
second member of the workspace and `uv` must be able to load it to honour the single lockfile.
Nothing in any of them is a placeholder for code.

`engine/` and `backend/` are both Python and are the two members of **one `uv` workspace**, resolved
by a single `uv.lock` at the repository root. The split between them is not a language boundary; it
is the boundary between a thing that computes a number and a thing that moves a number around. See
[`docs/decisions/python-engine.md`](docs/decisions/python-engine.md).

**No statistic is ever computed outside `engine/`.** Nothing about a file's name enforces that, so
it is a checked contract rather than a convention. It is asserted by
the engine being the only place a statistical library could be loaded. It is now enforced by a
continuous-integration check that asserts no numerical package appears in any `backend/` dependency
group — and that check carries a positive control, so it cannot pass by examining nothing. The single
sanctioned exception is a TypeScript port of `recommend()`, validated against 114 fixtures generated
by the engine.

The public root surface is asserted: [`.github/root-manifest.txt`](.github/root-manifest.txt)
declares it and `check-root-visibility.sh` fails if a root entry appears **or** silently disappears.

## Reproducibility

Four independent mechanisms, all required:

- **A hash-pinned lockfile.** `uv.lock` records a hash per artifact, and PyPI artifacts are
  immutable — a released filename and its hash can never be replaced. Version equality *is* byte
  equality here, which is stronger than the dated-snapshot arrangement it replaces.
- **Single-threaded linear algebra.** The container pins every BLAS thread pool to one. A
  multithreaded backend's reduction order depends on how work was split across threads, so the same
  input can land on a different last bit from one run to the next. This must be preserved.
- **Mandatory seeds** on every stochastic method.
- **An in-image test suite as a build gate** — a failing suite fails the image, so an image that has
  not proven itself cannot exist.

## Security

No wrapper makes a network call. Verified: **0 of 251**. User-supplied model formulae are parsed by a
default-deny allowlist with a depth limit and are never evaluated in a caller's namespace.
File-path arguments pass a structural gate rejecting traversal, absolute paths and control
characters. Full model in [`ARCHITECTURE.md` §10](ARCHITECTURE.md); reporting process in
[`SECURITY.md`](SECURITY.md).

## Documentation

| Document | What it is |
|---|---|
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | The authoritative description: every layer, every dependency, and every decision **not yet made**, named in §14 rather than silently omitted. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Wrapper anatomy, the gates, and how to get a change merged. |
| [`SECURITY.md`](SECURITY.md) | Reporting a vulnerability. |
| [`docs/decisions/python-engine.md`](docs/decisions/python-engine.md) | The workspace, the lockfile, and the check that replaced the file extension. |

## Licence and citation

AGPL-3.0-only, uniformly. Copyleft here is a **choice, not an inheritance**: the Python
scientific stack is BSD, Apache-2.0 and MIT throughout, so no dependency compels any licence at all.
The Affero variant is chosen because the deployed form of this project is a hosted compute engine,
and section 13 is what obliges an operator who modifies it to offer corresponding source to the users
who reach it over a network. `LICENSE` argues that in full before the licence text. One consequence:
a GPL-2.0-only dependency can no longer be admitted to this tree.

Third-party attribution is in [`engine/THIRD-PARTY-LICENSES.md`](engine/THIRD-PARTY-LICENSES.md) with
a machine-readable bill of materials in `engine/sbom.cdx.json`.

If you use this software in published work, cite it via [`CITATION.cff`](CITATION.cff).
