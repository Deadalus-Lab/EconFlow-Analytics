<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# EconFlow Analytics

A node-based canvas for econometric analysis. You wire methods into a graph, one method to a node,
and the graph runs as a durable directed acyclic graph.

**Licence:** AGPL-3.0-only for this project's own work. One set of third-party material in the
tree keeps its own terms, and [`NOTICE`](NOTICE) states what it requires of you.

## Status: the contract is finished, and the first methods compute

Two of the engine's 1456 method wrappers carry a body; the other 1454 are typed stubs that
raise. What is written and green is the argument contract, the schemas generated from it, the
sealed artifacts and the verification suite. The platform, integration, canvas and agent layers
are specified and not built.

Every figure below is reproduced by the command beside it, run from `engine/`.

| Quantity | Value | Command |
|---|---:|---|
| Wrapper modules | **598** | `find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' \| wc -l` |
| Category packages | **46** | `find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' \| wc -l` |
| Methods (nodes) in the contract | **1456** | `python3 -c "import json;print(json.load(open('artifacts/node-specs.json'))['engine']['n_nodes'])"` |
| Methods carrying an implementation | **2** | `python3 -c "import ast,pathlib;body=lambda f:[s for s in f.body if not(isinstance(s,ast.Expr) and isinstance(s.value,ast.Constant) and isinstance(s.value.value,str))];stub=lambda b:len(b)==1 and isinstance(b[0],ast.Raise) and isinstance(getattr(b[0].exc,'func',b[0].exc),ast.Name) and getattr(b[0].exc,'func',b[0].exc).id=='NotImplementedError';print(sum(1 for p in pathlib.Path('src/econflow_engine/wrappers').rglob('*.py') if p.name!='__init__.py' for n in ast.walk(ast.parse(p.read_text())) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and not n.name.startswith('_') and not stub(body(n))))"` |
| Method cards | **600** | `python3 -c "import json;print(json.load(open('artifacts/method-cards.json'))['source']['n_cards'])"` |
| Python version | **3.12** | `cat .python-version` |

Read the fourth row first. It walks the syntax tree of every wrapper module and counts the public
functions whose body is anything other than a docstring followed by a `NotImplementedError` raise.
It counts two: the binomial GLM of method card #83, which reproduces a coefficient published in
1989, and the count model of card #524, which reproduces a log-likelihood published in Stata's
own reference manual. Both are double-run on every build to prove each returns the same bytes
twice.

There are more cards than modules because two modules carry two cards each. Name them with
`python3 -c "import json,collections;c=collections.Counter(x['wrapper_file'] for x in json.load(open('artifacts/method-cards.json'))['cards']);print([k for k,n in c.items() if n>1])"`.

Every figure is re-measured on each pull request by the `assert-inventory` action against
[`.github/inventory.json`](.github/inventory.json), so a number moves only in a diff a reviewer sees.
The counts this table does not carry — parity verdicts, recommendation fixtures, decision trees,
SPDX coverage — are published once, in [`ARCHITECTURE.md`](ARCHITECTURE.md).

Trust the suite rather than any line above:

```bash
cd engine && ./run_verifications.sh
```

## The design claim

Correctness here is structural rather than probabilistic. Four mechanisms carry that claim, and each
is stated beside how much of it runs today, because a design commitment and a running check are not
the same thing.

| Mechanism | What it does | What runs today |
|---|---|---|
| **Rule-based method selection** | Sourced decision trees decide which method suits which data. A language model never decides. | The trees are sealed in `engine/artifacts/method-trees.json`. Nothing walks them yet. |
| **Hard validation gates** | A method refuses rather than return a doubtful number, and the refusal names the rule and what it requires. | The argument half. Every call crosses a generated pydantic model, and a failure raises a `GateError` carrying one of a closed set of reason codes. |
| **Generated typed schemas** | Node schemas are generated from the committed node-specification artifact, never hand-copied, so the contract cannot drift. | All of it. `scripts/gen_schemas.py --check` rebuilds the generated tier and fails on one byte of drift. |
| **Pinned computation** | Python version, package versions, package hashes and the linear-algebra thread count are pinned, so the same input gives the same number. | All of it, and the container build enforces it. |

A gate is a refusal, not an error. When a method's documented preconditions are not met it declines
to compute and names the rule that stopped it, rather than raising a stack trace;
`engine/src/econflow_engine/errors.py` holds the closed set of reason codes every refusal carries.

Where a language model is used at all it wires and configures nodes. It never computes a statistic
and never overrides a gate. [`ARCHITECTURE.md`](ARCHITECTURE.md#the-five-layers) draws that boundary,
and marks the agent layer as not built, so today the boundary is a commitment and not yet a check.

## Repository layout

One top-level directory per layer, so a researcher can find the econometrics without reading
anything else.

```text
engine/       Python      the compute core -- every wrapper, every method, every gate
backend/      Python      Galaxy platform integration            (specified, not built)
frontend/     TypeScript  integration layer and the web canvas   (specified, not built)
deploy/                   Compose, proxy and service definitions (specified, not built)
.github/                  continuous integration and its manifests
```

The three unbuilt directories are empty or nearly so, and the emptiness is the honest report rather
than an oversight: no placeholder stands in for code. `deploy/` is completely empty, `frontend/`
holds an `.nvmrc`, and `backend/` holds a `pyproject.toml`, a `.python-version` and an empty package,
because `uv` has to load the workspace's second member to honour the single lockfile. List every file
the three hold with `find backend deploy frontend -type f -not -path '*__pycache__*'`.

There is no `docs/` directory and no per-layer `README.md`. [`ARCHITECTURE.md`](ARCHITECTURE.md) is
the one place the design is written down, and it marks each layer as built or not built.

`engine/` and `backend/` are both Python, and are the two members of one `uv` workspace resolved by a
single `uv.lock` at the root. The split is not a language boundary. It is the boundary between a
thing that computes a number and a thing that moves a number around.

**No statistic is ever computed outside `engine/`.** No filename enforces that, so it is checked
rather than assumed: `check-engine-boundary.sh` counts every dependency `backend/` can declare and
refuses unless the count equals the figure in [`.github/inventory.json`](.github/inventory.json),
which is zero. A positive control fires on every run, so the gate cannot pass by examining nothing.

The public root surface is asserted the same way:
[`.github/root-manifest.txt`](.github/root-manifest.txt) declares it, and `check-root-visibility.sh`
fails if a root entry appears **or** silently disappears.

## Reproducibility and security

Reproducibility rests on four mechanisms, all of them required: a hash-pinned lockfile,
single-threaded linear algebra, a seed wherever a method exposes one, and a test suite that runs as a
hard gate inside the container build. [`ARCHITECTURE.md`](ARCHITECTURE.md) sets out what each buys,
and counts the stochastic methods that expose no seed at all.

No wrapper reaches the network, and a gate re-parses every module on each pull request rather than
trusting it. A model formula is read by a default-deny parser with a depth limit and is never
evaluated in a caller's namespace. Data arrives as a `store://bucket/key` pointer whose parser
refuses traversal, an absolute key, a backslash or a control character.

To report a vulnerability, use GitHub's private advisory form on this repository rather than opening
a public issue.

## Licence and citation

This project's own work is AGPL-3.0-only, by choice rather than inheritance: the Python scientific
stack is BSD, Apache-2.0 and MIT throughout, so no dependency compels any licence at all. The Affero
variant is chosen because the deployed form of this project is a hosted compute engine, and section
13 is what obliges an operator who modifies it to offer corresponding source to the users who reach
it over a network. [`LICENSE`](LICENSE) argues that in full.

One set of third-party material sits inside the tree under its own terms: the vendored proselint
prose rules, which are BSD-3-Clause. [`NOTICE`](NOTICE) states the obligation that carries;
`uvx --from "reuse==6.2.0" reuse lint` lists every licence in the tree. Attribution for the packages
the runtime image ships is the bill of materials in `engine/sbom.cdx.json`.

Nothing here computes a statistic yet, so there is nothing to cite. A `CITATION.cff` lands with the
first working method.
