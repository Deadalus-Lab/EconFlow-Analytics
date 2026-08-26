<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Architecture

**One of five layers exists, and inside it nothing computes yet.** The compute engine has a finished
typed contract, generated schemas, sealed artifacts and a green test suite. Not one method body is
written, and the other four layers have no code at all.

[`README.md`](README.md) counts what exists. This document says how the engine is built, and which
decisions are settled so that they do not get reopened.

## The five layers

| Layer | What it does | State |
|---|---|---|
| **Engine** (`engine/`) | Every statistic. The only place a number is computed. | Contract, schemas, artifacts and suite done. No method body written. |
| **Platform** (`backend/`) | Runs graphs, stores results, handles users. | Not built. Galaxy is the intended host. |
| **Integration** | Translates a canvas graph into a platform workflow. | Not built. |
| **Canvas** | The node editor a researcher actually uses. | Not built. |
| **Agents** | Optional help wiring a graph. Never computes. | Not built. |

## How the engine is built

Everything derives from one hand-written source, and nothing downstream is edited by hand.

```text
engine/corpus/*.json          one file per category: the method cards and the node contracts
        │  gen_artifacts.py
        ▼
engine/artifacts/*.json       sealed, each with a SHA-256 sidecar
        │  gen_schemas.py
        ▼
generated/args|docs/*.py      pydantic models and descriptions, one pair per category
        │  gen_wrappers.py
        ▼
wrappers/c*/*.py              typed stubs -- the only files a human fills in
```

Editing a wrapper signature by hand does not survive: the next `--write` restores it from the
artifact. Editing an artifact does not survive either, because `gen_artifacts.py --check` rebuilds it
from the corpus and compares byte for byte. The corpus is the only writable surface.

A method's arguments are hashed into a `contract_hash` that deliberately excludes every description,
so prose can be rewritten without moving a single contract.

Every call crosses a generated pydantic model before dispatch, so a bad argument is refused with a
reason code rather than computed on. That is the half of the gate story that runs today. A method's
own statistical preconditions are recorded on its card, and become refusals when its body lands.

### Verified figures

Run from `engine/`.

| Quantity | Value | Command |
|---|---:|---|
| Generated-tier modules | **96** | `find src/econflow_engine/generated -name '*.py' \| wc -l` |
| Generators | **4** | `find scripts -maxdepth 1 -name 'gen_*.py' -type f \| wc -l` |
| Infrastructure modules | **29** | `find src -name '*.py' -not -path '*__pycache__*' -not -path 'src/econflow_engine/wrappers/*' -not -path 'src/econflow_engine/generated/*' \| wc -l` |
| Test modules | **25** | `find tests -name 'test_*.py' -not -path '*__pycache__*' \| wc -l` |
| Frozen parity verdicts | **4855** | `python3 -c "import json;print(json.load(open('artifacts/parity-fixtures.json'))['n_cases'])"` |
| Recommendation fixtures | **114** | `python3 -c "import json;print(json.load(open('artifacts/recommend-fixtures.json'))['source']['n_fixtures'])"` |
| Decision trees | **10** | `python3 -c "import json;print(len(json.load(open('artifacts/method-trees.json'))['trees']))"` |
| Python files with an SPDX header | **819** | `find src scripts tests -name '*.py' -not -path '*__pycache__*' -print0 \| xargs -0 grep -l 'SPDX-License-Identifier' \| wc -l` |

The catalogue's own headline counts — wrapper modules, categories, methods, cards, implementations
written — are published in [`README.md`](README.md) instead, each beside its own command.

## Decisions already made

**Python throughout, one directory per layer rather than one per language.** The engine was rewritten
from R, which cost the layout two free signals: a directory named after a language, and a file
extension that said which layer may compute. Both are now checked instead of assumed, by
`check-engine-boundary.sh` and its positive control.

**AGPL-3.0-only for this project's own work,** with no dual licence. Third-party material inside the
tree keeps its own terms, and the vendored proselint rules carry a BSD-3-Clause notice that travels
with any redistribution. `LICENSE` argues the choice; [`NOTICE`](NOTICE) states every obligation a
redistributor takes on.

**No third-party service is ever a required check.** Analysis apps may comment; none may block a
merge. A required check that an outside service stops reporting deadlocks the repository forever.

**Generated output is committed.** The alternative is a build step before anything is reviewable.
This costs repository size and buys a readable diff when a contract moves.

## Reproducibility

Four mechanisms, all of them required.

- **A hash-pinned lockfile.** `uv.lock` records a hash per artifact, and PyPI artifacts are
  immutable, so a released filename and its hash can never be replaced. Version equality is byte
  equality here.
- **Single-threaded linear algebra.** The container pins every BLAS thread pool to one. A
  multithreaded backend splits a reduction differently from run to run, so the same input can land
  on a different last bit. This pin has to be preserved.
- **A seed wherever a method exposes one, and a named list of the ones that do not.** The
  node-specification artifact records per node whether a seed argument exists and whether it is
  required. It also names the stochastic methods that expose no seed at all; reproducing a run of one
  of those needs more than this repository provides today. Count them from `engine/` with
  `python3 -c "import json;print(len(json.load(open('artifacts/node-specs.json'))['vocabulary']['stochastic_unseeded_fns']))"`.
- **The test suite as a build gate.** It runs inside the container build, so an image that has not
  proven itself cannot exist.

## Security

No wrapper reaches the network, and `check-no-network.sh` re-measures that on every run by parsing
each module rather than grepping it. A model formula is read by a default-deny parser with an
allowlist of calls and a depth limit, and is never evaluated in a caller's namespace. Data arrives as
a `store://bucket/key` pointer, and `parse_store_uri` refuses a key holding `..`, a leading slash, a
backslash or a control character before anything opens it.

While no method body exists these properties are cheap to hold. The gates exist to make them
expensive to break later.

## Not yet decided

The platform host (Galaxy, or an embeddable canvas such as Orange3), the canvas stack, how a result
is displayed, and how methods are versioned once implementations exist. None of these blocks writing
a method body, which is the next thing that has to happen.
