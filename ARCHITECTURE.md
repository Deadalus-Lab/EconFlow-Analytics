<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Architecture

This document is the authoritative description of the system: what each layer is, what it is
responsible for, which third-party features it relies on, and what has not yet been decided.

It is written for three audiences: analysts and researchers who want to know what the tool computes
and whether they can trust it; academics who need to reproduce and cite a result; and contributors
who need to know where code belongs.

Two rules govern this document. Every quantity carries the command that produced it, so no number is
quoted from memory. Every decision that has not been made is named and described in
[§14 Open decisions](#14-open-decisions), never silently omitted — an unanswered question is a
register entry, not a gap.

---

## 1. Purpose and correctness thesis

The product is a node-based canvas for end-to-end macroeconomic analysis. A user wires nodes on a
graph, each node is a rigorously gated econometric method, and the graph executes as a durable
directed acyclic graph. The reference point is KNIME, narrowed to macroeconomics.

The central claim is that **correctness is structural, not probabilistic**:

| Mechanism | Effect |
|---|---|
| Rule-based method selection | Which method suits which data is decided by sourced decision trees, not by a language model's judgement. |
| Hard validation gates | Every documented requirement of every method is an explicit refusal to compute. An invalid result cannot escape; it becomes a blocked node with a stated reason. |
| Generated typed schemas | Node input schemas are generated from the committed node-specification artifact, never hand-copied, so the contract cannot drift from the implementation. |
| Pinned computation | Python version, package versions, package hashes and the linear-algebra thread count are all pinned. The same input produces the same number. |

A language model, where used, wires and configures nodes. It never computes a statistic and never
overrides a gate. This boundary is enforced structurally — see [§8](#8-layer-5--agent-subsystem).

---

## 2. System overview

Four layers, each with one responsibility:

| Layer | Language | Responsibility |
|---|---|---|
| **Compute engine** | Python | Executes econometric methods. Owns all statistics and all validation gates. |
| **Platform** | Python, XML, YAML | Galaxy. Owns job execution, scheduling, data management, users, provenance. |
| **Integration** | TypeScript | Translates between the canvas graph model and Galaxy's workflow model. |
| **Web canvas** | TypeScript | The user interface. Owns all rendering, including every chart. |

The lifecycle of one analysis:

```
   file upload
        │
        ▼
  Galaxy dataset  ──────────────────────────────┐
        │                                       │
        ▼                                       │
  user wires nodes on the canvas                │
        │                                       │
        ▼                                       │
  graph translated to a Galaxy workflow         │
        │                                       │
        ▼                                       │
  workflow invocation ──► job per node          │
        │                     │                 │
        │                     ▼                 │
        │              container starts,        │
        │              one method runs,         │
        │              wrapper, cold            │
        │                     │                 │
        │           ┌─────────┴─────────┐       │
        │           ▼                   ▼       │
        │      gate blocks          result      │
        │      (structured          written     │
        │       reason)             as dataset ─┘
        │           │                   │
        ▼           ▼                   ▼
  server-sent events stream state back to the canvas
        │
        ▼
  node turns red-with-reason, or renders a chart
```

Three properties of this design are worth stating explicitly, because they were each chosen against
a plausible alternative:

- **The engine is not a service, and the reason had to be re-argued.** There is no long-running
  engine process. Each job starts a container, runs one method, and exits.

  The reason is not that a warm process would be slow. Python can serve concurrent requests
  perfectly well — with threads for anything releasing the global interpreter lock, which the
  numerical stack largely does, or with multiple worker processes behind one socket. A warm engine
  would be a
  competent service. If the case rested on the old sentence, it would now be a case for building one.

  It does not, and the surviving reasons are the ones that always did the work:

  - **Execution belongs to Galaxy's job runner.** A daemon would take it back, and with it
    cancellation, resource accounting, retry, crash containment and the per-job provenance record.
    Those are not conveniences; they are most of what §5 says we are adopting Galaxy *for*.
  - **A process that persists accumulates state, and this engine must not.** The correctness claim is
    that the same input produces the same number. A warm process carries interpreter state,
    fitted-model caches, thread pools and whatever a numerical library memoised — every one of which
    is an input that no reproducibility manifest records. A cold start has exactly the state the
    lockfile and the image describe.
  - **Memory-class routing needs the boundary.** Nodes are tagged `light`, `heavy` or `mcmc` and
    routed to appropriately sized destinations. That is a per-job scheduling decision, and it cannot
    be made about work already inside a shared daemon.

  Concurrency was never the load-bearing reason. It was the most visible one while the language made
  it unanswerable.
- **Galaxy is a dependency, not a fork.** The upstream source is never vendored or patched. We add
  tools, datatypes and configuration; all of that lives in `backend/` and is ours.
- **Charts are never drawn by the engine.** It emits numeric chart data and a chart specification.
  Rendering happens exclusively in the browser. No image ever crosses the boundary — and note that
  this is now a rule with a real temptation behind it, since `matplotlib` is one `import` away in a
  way that a device-based plotting model made more conspicuous.

---

## 3. Repository layout

A monorepo containing only our own code, with **one top-level directory per layer**. Compute,
platform integration and the user-facing layer each own exactly one root — so a researcher can find
the econometrics without reading anything else.

The split is deliberately *not* a language split. `engine/` and `backend/` are both Python and are
the two members of one `uv` workspace; the boundary between them is between a thing that computes a
number and a thing that moves a number around, which is worth a directory whether or not the two
sides speak the same language. `docs/decisions/python-engine.md` records that reasoning and the
check that now enforces it.

```
EconFlow-Analytics/
├── ARCHITECTURE.md  README.md  LICENSE  NOTICE  CITATION.cff
├── CONTRIBUTING.md  SECURITY.md  CODE_OF_CONDUCT.md  CHANGELOG.md
├── Dockerfile  .dockerignore   # build context is the ROOT — see below
├── pyproject.toml  uv.lock     # ONE uv workspace, ONE resolution, two members
│
├── engine/                    # ── the compute core
│   ├── src/econflow_engine/
│   │   ├── wrappers/          #   30 category packages, 251 wrapper modules
│   │   ├── generated/         #   64 machine-written modules — committed, not ignored
│   │   ├── mcp/  node/        #   discovery surface, memory class, executability
│   │   ├── kinds.py  gates.py  serialize.py  chart_spec.py  formula.py
│   │   └── naming.py  loader.py  errors.py  __main__.py
│   ├── METHOD-SOURCES.json    #   which library or paper implements each module
│   ├── tests/                 #   pytest suite
│   ├── scripts/               #   code generators (gen_*.py)
│   ├── fixtures/              #   cross-language contract fixtures
│   ├── artifacts/             #   committed JSON contracts — FROZEN INPUTS, see 4.4
│   ├── pyproject.toml  ruff.toml  .python-version  run_verifications.sh
│   └── METHOD-SELECTION.md  METHOD-SELECTION.yaml  METHOD-SELECTION-TREES.yaml
│
├── backend/                   # ── platform integration ── NOT BUILT
│   ├── pyproject.toml  .python-version   #   the workspace's second member
│   └── src/econflow_backend/  #   an empty package; the lockfile must load it
│
├── frontend/                  # ── TypeScript ── NOT BUILT (README and .nvmrc only)
├── deploy/                    # ── Compose, proxy, services ── NOT BUILT (README only)
├── docs/                      # decision records and the roadmap
└── .github/                   # YAML — CI, its manifests and its scripts
```

**Every path drawn above exists.** The three unbuilt layers are drawn at the depth they actually
occupy rather than at the depth they will occupy, because a tree that shows planned directories as
though they were present is the same defect as a gate that passes without examining anything. What
each will contain is in that layer's own `README.md`. A testing-strategy document is planned and
does not exist yet; until it does, `engine/tests/README.md` and `CONTRIBUTING.md` are where the
suite's rules are written.

**Why the Dockerfile is at the root and not in `deploy/`.** The build context must be the repository
root for two independent reasons. The image `COPY`s `LICENSE` — the licence requires its text to
accompany the binaries — and it `COPY`s the workspace `pyproject.toml` and `uv.lock`, both root files
because the workspace root is where a `uv` workspace keeps them. Docker cannot reach outside its
context, and a symlink does not work either. `deploy/` therefore holds Compose and the proxy; the
engine image definition stays where its context is.

**The generated tier is committed, not ignored.** `engine/src/econflow_engine/generated/` is 64
modules emitted by `scripts/gen_schemas.py` from `artifacts/node-specs.v1.json`. The reflex with
machine-written code is a `.gitignore` line, and that would be a mistake here: the generated form is
what gets reviewed in a diff, and the `artifact-drift` gate re-emits it in `--check` mode and compares
byte for byte. Ignoring it would delete the review surface and reduce the gate to comparing a
generator with itself. It is marked `linguist-generated` so it does not dominate the language
breakdown, which is a display decision and not a tracking one.

**The public root surface is asserted in both directions.** `.gitignore` names what is withheld;
`.github/root-manifest.txt` declares the resulting root, and `check-root-visibility.sh` fails on a
difference either way — an entry that appeared without review, and an entry that silently stopped
being tracked. Working files — `CLAUDE.md`, `todo.md`, `.private/` and any
tool cache — are named explicitly. This repository is public from its first commit and its history
cannot be rewritten, so a root entry is permanent from the moment it lands.

**Why a monorepo.** The engine and the TypeScript layer share a code-generated contract: schemas and
parity fixtures live in `engine/` and are consumed in `packages/`. Splitting these across
repositories would require publishing an intermediate artifact version on every engine change, for no
benefit at this team size. One repository, one version, one CI run that can prove both sides agree.

---

## 4. Layer 1 — the compute engine

### 4.1 Verified inventory

Every figure below is reproduced by the command beside it, run from the engine directory. Each one is
also re-measured on every pull request by `.github/actions/assert-inventory`, against the same command
recorded in `.github/inventory.json` — so a number here that has gone stale turns a gate red rather
than merely misinforming a reader.

| Quantity | Value | Command |
|---|---:|---|
| Wrapper modules | **251** | `find src/econflow_engine/wrappers -name '*.py' -type f -not -name '__init__.py' \| wc -l` |
| Category packages | **30** | `find src/econflow_engine/wrappers -mindepth 1 -maxdepth 1 -type d -not -name '__pycache__' \| wc -l` |
| Executable methods (nodes) | **913** | `python3 -c "import json;print(json.load(open('artifacts/node-specs.v1.json'))['engine']['n_nodes'])"` |
| Generators | **3** | `find scripts -maxdepth 1 -name '*.py' -type f \| wc -l` |
| Infrastructure modules | **24** | `find src -name '*.py' -not -path '*__pycache__*' -not -path 'src/econflow_engine/wrappers/*' -not -path 'src/econflow_engine/generated/*' \| wc -l` |
| Generated modules | **64** | `find src/econflow_engine/generated -name '*.py' -not -path '*__pycache__*' \| wc -l` |
| Python files, total / with an SPDX header | **380 / 380** | `find src scripts tests -name '*.py' -not -path '*__pycache__*' \| wc -l` |
| Python version | **3.12** | `cat .python-version` |

**The methods figure is read from the artifact, not counted from source.**
`artifacts/node-specs.v1.json` is a frozen input, and the code that declares those 913 methods is
generated *from* it. Counting the
generated tier would prove only that the generator ran.

**Two constants in the manifest currently read `unmeasured`, and the gate is red because of it.**
`py_packages` and `sbom_components` have no artifact to measure: the workspace `uv.lock` is not in the
tree yet, and `sbom.cdx.json` has not been regenerated from it. `assert.sh` prints `OWED` and exits
non-zero for each. This is the anti-vacuity rule applied to the manifest itself — a constant that
cannot be measured must never read as a constant that was verified, and the way to clear it is to land
the artifact and run the command, not to soften the check.

Run the suite rather than quoting any figure from it:

```bash
cd engine && ./run_verifications.sh
```

### 4.2 Wrapper anatomy

Every one of the 251 wrapper modules follows the same shape. The uniformity is load-bearing: it is
what makes generated tooling possible across the whole catalogue.

1. A module docstring naming the upstream package and the methods the module exposes.
2. Arguments taken **only** from the upstream documentation, each carrying its documented default.
   Constrained choices are typed as a literal enumeration and validated. Arguments are never invented.
3. **Gates.** Every documented hard requirement becomes an explicit refusal to compute, raising a
   typed engine error with a clear message. These are blockers, not warnings.
4. A structured result — documented fields plus the fitted object. Never printing, never plotting.
5. Examples in the docstring, never at module scope, so importing a module never executes one.
6. An implementation-note footer recording the functions used, what was deliberately omitted, the
   gates added, and any project-specific addition.

**Call helpers need no unique naming convention.** A shared global namespace would make two files
defining the same helper name a silent collision, where the last one loaded wins. Modules have their
own namespaces, so that collision cannot occur; no such rule exists
from the review configuration rather than carried forward as ritual. It is worth recording that it
existed, because "two files define `_call`" now looks like a defect to anyone who remembers it and
is not one.

Gates are frequently additions rather than pass-throughs. A recurring finding while building the
catalogue was that libraries silently accept invalid input and return a plausible-looking object —
dropping missing rows with only a warning, silently broadcasting a mis-shaped argument, or fitting a
model on a column of constants. Each such case became an explicit gate.

### 4.3 Three internal layers

| Layer | Contents | Rule |
|---|---|---|
| **L1** | `wrappers/**` | Domain wrappers returning rich structured results of real objects. No serialisation, no transport, no orchestration. |
| **L2** | `serialize.py`, `chart_spec.py` | One shared serialiser turning any wrapper output into JSON-safe data, and one chart-specification builder. Pure and total. |
| **L3** | `mcp/**`, `generated/**` | Declarative specs, argument adaptation, allowlists, and the shared handler path. |

The L1/L2 split is what allows the same wrapper to be driven by different callers without change.

### 4.4 The generation chain

**The direction of generation reversed with the language, and this is the single most important thing
to understand about the engine's contracts.**

The artifacts are the **frozen input**. `node-specs.v1.json`, `method-cards.v1.json`,
`parity-fixtures.v1.json` and `recommend-fixtures.v1.json` are committed to this repository and are
never regenerated by the build; they were produced by the
implementation and are the oracle this engine is checked *against*. Python cannot re-derive them:
`parity-fixtures.v1.json` in particular records 4855 accept/reject verdicts from the reference
argument adapter, which is the whole point of having them.

They are not edited to make anything pass. If one ever must be edited, the rule is recorded in
`engine/artifacts/PROVENANCE.md`: the change is written down with its reason and its new digest, or
it did not happen.

```
artifacts/node-specs.v1.json      913 nodes / 30 categories + vocabulary  (FROZEN INPUT)
        │
        ├─ scripts/gen_schemas.py  ──►  src/econflow_engine/generated/**   64 modules
        │                                 tier 1  manifest.py    913 entries, no descriptions
        │                                 tier 2  args/<cat>.py  models + defaults
        │                                 tier 3  docs/<cat>.py  descriptions + examples
        │
        ├─ scripts/gen_wrappers.py ──►  src/econflow_engine/wrappers/**   251 modules + 30 READMEs
        │
        ├──► Galaxy Tool XML          (backend/tools/)
        └──► Zod schemas              (frontend/packages/node-schemas/)
```

Committed artifacts, each verified by the command shown:

| Artifact | Contents | Command |
|---|---|---|
| `node-specs.v1.json` | 913 nodes, 30 categories, argument kinds, allowlists, memory classes | `python3 -c "import json;print(json.load(open('artifacts/node-specs.v1.json'))['engine']['n_nodes'])"` |
| `method-cards.v1.json` | **252** method cards covering all 913 nodes; 1 card lacks a source | `python3 -c "import json;print(json.load(open('artifacts/method-cards.v1.json'))['source']['n_cards'])"` |
| `method-trees.v1.json` | The master decision trees | — |
| `parity-fixtures.v1.json` | **4855** frozen verdicts pinning argument-adaptation behaviour, seed `20260727` | `python3 -c "import json;print(json.load(open('artifacts/parity-fixtures.v1.json'))['n_cases'])"` |
| `recommend-fixtures.v1.json` | **114** fixtures covering every recommendation status | `python3 -c "import json;print(json.load(open('artifacts/recommend-fixtures.v1.json'))['source']['n_fixtures'])"` |
| `intentional-divergences.json` | Deliberate schema divergences, all in the safe direction | — |

Six carry a `.sha256` sidecar and `assert-inventory` verifies each against the exact count in the
manifest — a glob that matched nothing would otherwise "verify" every sidecar without having
opened one. `parity-fixtures.v1.json` needs none: the parity suite reads it in full, which is
strictly stronger than comparing a hash. `intentional-divergences.json` is a hand-maintained input,
so there is nothing to re-derive it from.

**A comment change in a generator still shifts every file it emits.** That property did not go away
with the corpus; it moved from the specification sources to `scripts/gen_*.py`. It is the reason no
auto-formatter may run over this tree — see `.pre-commit-config.yaml`.

### 4.5 Method selection

`METHOD-SELECTION.md`, its machine mirror `METHOD-SELECTION.yaml`, and `METHOD-SELECTION-TREES.yaml`
hold the rule-based reasoning that decides which method fits which data. Each of the 252 cards is
sourced to a vignette, manual page, textbook or paper.

The trees encode routing that must not be re-derived case by case — for example the stationarity →
cointegration-rank → model chain that determines whether a vector autoregression, a vector error
correction model, or a bounds-testing approach is appropriate, and the polarity rule that augmented
Dickey-Fuller and Phillips-Perron rejections mean stationarity while a KPSS rejection means the
opposite. Encoding this once, with sources, is what makes selection auditable.

### 4.6 Determinism

Four independent mechanisms, all required:

| Mechanism | What it pins |
|---|---|
| `uv.lock` | Package **versions and hashes**. PyPI artifacts are immutable — a released filename and its hash can never be replaced — so version equality *is* byte equality. This is a stronger guarantee than the dated-mirror arrangement it replaces, and it lives in one file rather than two. |
| Single-threaded linear algebra | Floating-point results. Every BLAS thread pool is pinned to one in the image and in CI. |
| Mandatory seeds | Stochastic methods. Nodes whose method is stochastic and unseeded are enumerated in the artifact vocabulary. |
| Galaxy job cache | Recomputation. Identical tool version, parameters and input content reuse the previous result. |

> **What the thread pin does and does not buy.** Pinning the exact linear-algebra library would
> need it to be installed by the image and switchable. NumPy and SciPy ship a threaded OpenBLAS
> *inside their wheels*, and there is no alternative to switch. What remains controllable is the
> thread count, and it is the
> larger of the two effects: OpenBLAS's reduction order depends on how work was split across threads,
> so an unpinned build can produce different last bits on the same machine with the same seed. Pinning
> `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` to one removes that. It does **not**
> make two different wheel builds agree. Only the published image, where the wheel set is fixed by the
> lockfile, closes that half — which is why §11.4 refuses to read a green CI suite as proof of
> numerical reproducibility.

> **A trap this table does not protect against.** An interpreter can resolve some packages from a
> system library the lockfile does not describe, so a recorded suite figure demonstrates that the
> tests *pass* rather
> than that they produce the *pinned numbers*. The Python equivalent is a virtual environment that has
> drifted from `uv.lock` — installed once, then updated by hand, and never re-synchronised. The
> defence is the same in shape: `uv sync --locked` refuses to re-resolve and fails if the lockfile does
> not already satisfy the manifests, and CI uses that form rather than a plain `uv sync`. The fix is
> always to re-sync, never to re-lock; re-locking would redefine the pinned set to whatever the host
> happened to want.

---

## 5. Layer 2 — the Galaxy platform

Galaxy is a mature, actively developed workflow platform (MIT licence since 2026-02-25; previously
Academic Free License 3.0, which is why both are cited in circulation). It supplies job execution,
data management, users and provenance — everything between the canvas and the engine that we would
otherwise have built and maintained ourselves.

**The maintenance case, measured rather than assumed** (2026-08-15): the project is roughly two
decades old; the core repository took **over 100 commits in the past thirty days**, the most recent
the day before this measurement; it has **100+ contributors and 1160 forks**; and the surrounding
repositories move at the same rate — `tools-iuc` and `planemo` within the last two days, Total
Perspective Vortex the same day. Release 26.1.1 shipped on 2026-08-04 with a matching typed client
published to npm the same day.

This matters for how the rest of this section should be read. Several entries below record missing
formal guarantees — no published API deprecation window, 102 endpoints not yet ported to the typed
schema, a tool-registration API still in beta. **Those are the ordinary characteristics of a large,
fast-moving, community-governed codebase, not symptoms of neglect.** They are recorded because we
must engineer against them, not as criticism of the project we are choosing to build on. A
dependency this active is an asset; it simply means our contract tests, not an upstream promise, are
what protect us from churn.

This section names every feature the system relies on. For each: what it is, what it does, how it is
configured, and whether it is core or optional.

### 5.1 Tools

A "tool" in Galaxy is one executable step. Each of our 913 methods becomes one tool.

| Feature | What it is and does | Configuration | Status |
|---|---|---|---|
| **Tool XML** | The declarative description of a tool: identifier, version, inputs, outputs, and the command template that runs it. | one file per tool | core |
| **`param`, `conditional`, `repeat`, `section`** | Input primitives: a single input; inputs shown or hidden based on another input's value; a user-repeatable block; a visual grouping. | inside `<inputs>` | core |
| **`validator`** | Constrains a parameter before submission — regular expression, numeric range, dataset metadata. Rejects bad input at the form, not at runtime. | on a `param` | core |
| **`command` + Cheetah** | The shell invocation, templated. Parameter values are substituted in. | `<command>` | core |
| **`configfiles`** | Writes a generated file into the job directory before the command runs. This is how a method's arguments reach the engine as one JSON document instead of hundreds of positional flags. | `<configfiles>` | core |
| **`stdio`** | Maps exit codes and standard-error patterns to job success or failure. Our gate-blocked state is distinguished here. | `<stdio>` | core |
| **`version_command`** | A shell command whose output records which version of the underlying software actually ran, per job. | `<version_command>` | core |
| **`macros`** | XML fragment reuse across tool files. Essential at 913 tools: the shared container requirement, standard outputs and common parameters are declared once. | `<macros>` | core |
| **`citations`** | Digital object identifiers or BibTeX for the method's source. Galaxy renders these on the tool form and can emit a complete reference list for an entire analysis. | `<citations>` | core |
| **Tool panel** | The catalogue as the user browses it, organised into sections. Our 30 categories map onto sections. | `tool_conf.xml` | core |
| **Planemo** | The command-line tool for authoring, linting and testing tools and workflows. Produces machine-readable test reports for continuous integration. | developer tool | core |
| **Dependency resolvers** | How Galaxy satisfies a tool's declared software requirements — by default a chain ending in Conda. | `galaxy.yml` | core |
| **Container resolvers** | Resolve a tool's requirements to a container image instead. The `explicit` resolver lets a tool name its own image directly. | `container_resolvers_conf` | **core to us** |
| **`use_cached_dependency_manager`** | Caches resolved environments instead of rebuilding them per job. | `galaxy.yml` | optional |
| **Tool Shed** | A companion server distributing versioned tool repositories, installable without restarting. | `shed_tool_conf.xml` | optional |
| **Data managers** | A tool class that downloads or builds reference datasets and registers them in tables. | `data_manager_conf.xml` | not used |

**The container decision.** Our engine pins every dependency by version *and hash* in one `uv.lock`,
and fixes the linear-algebra thread count. Galaxy's default dependency path is Conda, which would
resolve packages independently and silently break both guarantees — and the risk is sharper now than
it was, because Conda resolves Python natively and would look like it was doing the right thing. The
`explicit` container resolver removes the conflict entirely: each generated tool declares our own
engine image, Galaxy runs the job inside it, and Conda is never consulted. The lockfile remains the
sole authority over what code runs.

### 5.2 Workflows

| Feature | What it is and does | Status |
|---|---|---|
| **Workflow formats** | Two: a native JSON format, and a human-writable YAML format that follows common-workflow conventions. Our canvas graph is translated into one of these. | core |
| **Invocation** | One execution of a workflow. Carries its own identifier and state, and is the object our canvas polls or subscribes to. States include `new`, `ready`, `scheduled`, `cancelling`, `cancelled`, `failed`, `completed`. | core |
| **Subworkflows** | A workflow embedded as a step inside another. Enables reusable analysis fragments. | optional |
| **Conditional steps** | A step can carry a `when` expression and be skipped, emitting nulls on its outputs. | optional |
| **Workflow reports** | A Markdown document stored with the workflow and rendered per invocation, embedding datasets, figures and job metrics. Retrievable as a document or a PDF. | optional |
| **Best-practice linting** | Checks a workflow declares licence, authorship, annotation and labelled outputs. Runs in the editor and in continuous integration. | optional |
| **Workflow testing** | A test format plus the ability to generate a test from a real invocation. | core to CI |
| **Collection operations** | Built-in tools that filter, relabel, sort, flatten, merge and zip collections without custom code. | optional |
| **Workflow versioning** | Stored workflows keep versions; a step can pin a specific tool version. | core |

### 5.3 Data

| Feature | What it is and does | Status |
|---|---|---|
| **History** | An ordered container of datasets for one line of work. The largest API surface in Galaxy. | core |
| **Dataset** | One data object with a state (`queued`, `running`, `ok`, `empty`, `error`, `paused`, `discarded`, and others) and typed metadata. | core |
| **Collections** | Structured groups of datasets — a list, a pair, a list of pairs, or arbitrary nesting — over which a tool can be mapped automatically. This is the native expression of our producer/consumer node chaining. | core |
| **Datatypes framework** | Registers file formats as classes with sniffers that auto-detect format on upload, typed metadata elements, and converters. A macroeconomic time series (values, start, frequency) becomes a custom datatype here. | core |
| **Object store** | Where dataset bytes live. Supports local disk, S3-compatible, and distributed or hierarchical arrangements. | core |
| **Upload paths** | Regular browser upload; FTP; remote file sources browsable as a hierarchy; and a rule-based uploader that builds many datasets or a collection from a pasted table. | core |
| **Data libraries** | Administrator-curated shared datasets, optionally linked rather than copied. | optional |
| **Provenance** | Per dataset, the tool, parameters and job that produced it, retrievable through the API. | core |

### 5.4 Execution

| Feature | What it is and does | Status |
|---|---|---|
| **Job configuration** | Declares runners, destinations and limits. Absent it, Galaxy runs jobs locally with a small concurrency cap. | core |
| **Job runners** | Local execution; cluster schedulers; Kubernetes; and Pulsar, which runs jobs on remote machines without a shared filesystem by staging inputs and results. | core |
| **Handlers** | Processes that claim and monitor jobs, coordinated through the database. Adding handlers is how concurrent execution scales. | core |
| **Destinations and dynamic mapping** | A destination binds a runner to resource settings and container options. A rule can select the destination at submission time. | core |
| **Total Perspective Vortex** | A routing layer mapping tools, users and roles to destinations with explicit processor and memory allocations, driven by a YAML rule file. The engine already tags every node `light`, `heavy` or `mcmc`; those tags feed this directly. | optional, adopted |
| **Job metrics** | Records runtime, processor count, memory and control-group statistics per job. | optional |
| **Job cache** | Reuses the outputs of a previous identical job — same tool version, same parameters, same input content. A canvas re-runs graphs constantly, so this is substantial free memoisation. | core to us |
| **Limits and resubmission** | Per-user and per-destination concurrency caps, walltime and output-size limits, and automatic retry — optionally onto a larger destination — after a memory or walltime failure. | core |

### 5.5 Application programming interface and authentication

| Feature | What it is and does | Status |
|---|---|---|
| **REST API** | The complete control surface: histories, workflows, invocations, jobs, datasets, collections, tools, datatypes, users, roles, groups, quotas, libraries and more. Our canvas drives this directly. | core |
| **OpenAPI schema** | Every instance serves its own machine-readable schema and interactive documentation. Our typed client is generated from it rather than hand-written. | core |
| **Authentication** | Internal accounts; API keys; OpenID Connect against an external identity provider; directory-service integration; or trusted upstream-proxy authentication. | core |
| **Cross-origin configuration** | An allow-list of origins permitted to call the API. Required, because our canvas is served from a different origin than Galaxy. | **required** |
| **Server-sent events** | A long-lived stream carrying history changes and notifications, backed by database notification. This is how the canvas learns a node finished without polling. Requires the proxy to disable response buffering on that route. ⚠️ **The route is present from 26.1 and absent from the 26.0 LTS**, which makes this row and the version pin a single joined decision rather than two — see `U8`. | core to us, **conditional on the pin** |
| **Polling fallback** | With the event stream disabled, clients poll history and job state on a documented interval. Our client keeps this as a degradation path. | fallback |
| **Standards endpoints** | Implementations of community workflow-execution and data-repository standards, offering a vendor-neutral alternative to the native API. | optional |
| **Dynamic tools** | An API for registering tools at runtime rather than from files on disk. Evaluated as a replacement for the 913 generated files and **rejected** — see `U10` for the measured reasons. | **evaluated, rejected** |

### 5.6 Administration and operations

| Feature | What it is and does |
|---|---|
| **Main configuration** | One file carrying both process-management and application settings. |
| **Configuration inventory** | Separate files govern tools, datatypes, jobs, dependency and container resolution, object stores, authentication, file sources and metrics. |
| **Database migrations** | Schema evolution is managed by the upstream migration tool and applied through a supplied script. Galaxy owns its own schema; we do not write migrations against it. |
| **Background task queue** | A worker system with a message broker handles asynchronous work and fans events out across processes. |
| **Process manager** | Supervises the web processes, handlers and workers as one unit. |
| **Administration panel** | Users, roles, groups, quotas, jobs and tool installation. Note that quotas are inert until one is created. |
| **Cleanup** | Deleted data is not physically removed until purge scripts run. Retention is therefore an operational decision, not an automatic behaviour. |
| **Monitoring** | Counters for connections, dispatch and job state are exported for collection. |

### 5.7 Interface extension points

Documented because they exist and constrain what we must build ourselves, though the end user never
sees Galaxy's own interface (see [§7](#7-layer-4--the-web-canvas)):

**Visualisation plugins** (dataset viewers registered with the platform), **interactive tools**
(container-backed sessions such as a notebook or a statistics environment exposed live in the
browser), **display applications** (external viewer links attached to a datatype), **webhooks**
(interface extension points), **themes** (colour and branding), and **tours** (guided walkthroughs).

### 5.8 Reproducibility and provenance

This is the strongest argument for building on Galaxy rather than on our own orchestrator, and it is
what an academic audience will judge the system by:

| Feature | What it gives us |
|---|---|
| **Dataset provenance** | For any result, the exact tool, version and parameters that produced it. |
| **Research object export** | An entire workflow invocation — definition, inputs, outputs and metadata — exported as a standard, self-describing archive. |
| **Structured regulatory export** | A second export format aimed at regulated and clinical reproducibility contexts. |
| **History export and archive** | A complete analysis, datasets included, exportable and re-importable on any other installation. |
| **Citation aggregation** | A complete reference list for every method used in an analysis, in both a prose citation style and BibTeX. |
| **Tool version pinning** | Per-job record of which software version ran. |

None of this requires code from us. It requires that our tools declare their citations and versions
honestly.

---

## 6. Layer 3 — the integration layer

The canvas and Galaxy have different models. This layer is the translation, and it is genuinely our
code — the one place where the two systems must be reconciled.

### 6.1 Responsibilities

| Concern | Description |
|---|---|
| **Graph translation** | A React Flow graph — nodes with positions, edges with typed handles — becomes a Galaxy workflow definition. Node identity, parameter values and edge connectivity all map across. |
| **State mapping** | Galaxy job and invocation states map onto canvas node states. This mapping is deliberately not one-to-one: several Galaxy states collapse into "running", and one Galaxy failure state splits into "failed" versus "blocked by a gate". |
| **Event consumption** | Subscribing to the server-sent event stream, applying updates to canvas state, and falling back to polling if the stream is unavailable. |
| **Gate surfacing** | Turning a wrapper's `GateError` into a first-class, educational canvas state rather than a generic error. |

### 6.2 The gate contract

This is the most important contract in the system, because it is where the correctness thesis becomes
visible to a user.

A gate is not an error. When a wrapper refuses to run because its documented preconditions are not
met, that is the system working. The user must see *which rule* blocked the node and *what the rule
requires* — not a stack trace.

```
wrapper: raises GateError("... requires a series with frequency > 1 ...")
        │
        ▼
tool entrypoint catches, emits structured output + distinct exit code
        │
        ▼
Galaxy: job fails, stderr pattern matched by <stdio>
        │
        ▼
canvas: node enters "blocked" state, displays the rule and the requirement
```

The exact structure of that output is not yet fixed — see `U24`.

### 6.3 What happens to the existing node layer

The engine carries a `node/` package built for the previous architecture, in which a TypeScript
orchestrator called a long-running compute service over HTTP. Under Galaxy most of it is superseded,
because Galaxy provides the same capability at the platform level.

> **Decided, and now done.** There is no HTTP router. Galaxy's job runner already provides
> execution, scheduling, cancellation, resource accounting and crash containment — the things a
> bespoke HTTP layer in front of the engine does worse. This closes that half of `U25`; what replaces
> the container entrypoint remains `U21`.
>
> **The sequencing caveat that used to sit here has expired.** It said the router's files were still
> sourced by the suite and named by the container's healthcheck and command, so removing them would
> move the exact constants the gates assert — and that the removal was therefore sequenced *after*
> the gates existed. The reimplementation absorbed that removal: the 913 HTTP routes, the inbound
> authentication layer, the healthcheck and the router entrypoint are all simply absent, and the
> constants in §4.1 were measured on the tree without them. There is no pre-computed delta left to
> apply.

| Component | Previous role | Fate |
|---|---|---|
| `memory_class` | Per-node memory class for a weighted concurrency limiter | **Kept.** Feeds destination routing. |
| `executability` | Executability tags and contract hash | **Kept**, repurposed toward tool versioning. |
| `cache` | Input-hash idempotency | **Superseded** by the platform job cache. |
| `store_pointers` | Content-addressed object-store pointers | **Largely superseded**; Galaxy owns datasets and the object store. |
| `auth` | Inbound request authentication | **Removed.** The engine is not a network service. |
| The HTTP router | 913 routes | **Gone.** |

The fate of the six-function discovery gateway in `mcp/` is a separate question — it remains valuable
as a reasoning surface for the agent subsystem even though it is no longer an execution path. See
`U26`.

---

## 7. Layer 4 — the web canvas

The user-facing application. Galaxy's own interface is retained for administration and debugging
only; end users never see it, and never encounter its vocabulary.

| Concern | Choice |
|---|---|
| Build and framework | Vite with React, a single-page application. No server-side rendering. |
| Canvas | React Flow, with typed connection handles so an invalid edge cannot be drawn. |
| Forms | Generated from the node schemas, so a form cannot accept what the engine would reject. |
| Charts | Apache ECharts, rendering client-side only. |
| Live state | The platform event stream, with polling as a fallback. |

**The rendering invariant.** The engine produces chart *data* and a chart *specification*; the browser draws.
No image, no widget and no rendered artefact crosses the boundary. This keeps the engine free of
graphics dependencies and makes every chart interactive and themeable without re-running an analysis.

Substantial parts of the interface remain unspecified — component library, state management, routing,
authentication flow, accessibility target — recorded as `U31` through `U40`.

---

## 8. Layer 5 — the agent subsystem

An optional layer that helps a user assemble a graph. It is bound by one rule: **the model wires and
configures; it never computes and never overrides a gate.**

### 8.1 Structural isolation

The guarantee is enforced by construction, not by instruction. Five agents each run as a separate
loop with its own tool map. A tool that is absent from an agent's map does not exist for that agent —
which is categorically stronger than telling a model not to call something.

| Agent | Tools available |
|---|---|
| Orchestrator | The other four agents, as tools. No retrieval tools. |
| Reasoning | Causal-graph retrieval only. |
| Data and execution | Node search and execution only. |
| Narrative | None. |
| Critic | Causal-graph retrieval and identification-strategy validation. |

### 8.2 The deterministic guardrail

`recommend()` — the TypeScript port of the engine's rule-based selection, validated against 114
fixtures committed in `recommend-fixtures.v1.json` — runs **after** a proposal, as a judge. It is never
exposed as a tool the model may call, because a tool can be left uncalled. As a post-hoc check it
cannot be bypassed.

### 8.3 Retrieval

Two retrieval tools: one searching the 252 method cards by vector similarity, one searching a causal
knowledge graph. Embeddings are computed locally on the processor; no external service is required
and no analysis data leaves the machine.

Provider configuration is bring-your-own-key with no default. Which providers are documented as known
good is `U45`.

---

## 9. Determinism and reproducibility, end to end

The complete chain, and what each link guarantees:

| Link | Guarantee |
|---|---|
| Hash-pinned lockfile | The same package *bytes*, not merely the same version numbers. |
| Single-threaded linear algebra | Stability of numerical results against thread-scheduling variation. |
| Container image per tool | The same operating system, interpreter build and environment on every host. |
| Mandatory seeds | Stochastic methods reproduce exactly. |
| Tool version and version command | A per-job record of what actually ran. |
| Job cache | Identical re-runs return the identical prior result rather than recomputing. |
| Provenance and research-object export | A third party can reconstruct the analysis from the archive alone. |
| Citation aggregation | The methods used can be credited correctly and completely. |

A claim of reproducibility that stopped at "same package versions" would once have been false, and
the wording of this chain has changed accordingly. Under a mirror that rebuilt binaries under an
unchanged version number, version equality was not byte equality and a dated snapshot was the
mitigation. PyPI artifacts are immutable, so `uv.lock`'s recorded hashes make version equality *be*
byte equality — the link is stronger, not weaker.

**The link that got weaker is the one above it, and pretending otherwise would be the exact
misstatement this document exists to prevent.** Bit-level stability *across machines* would need the
numerical library itself to be fixed by the image. It is vendored inside the wheels instead, so what
is pinned is the thread count rather than the library. Two hosts running the identical locked wheel set agree; two different wheel
builds of the same version are not guaranteed to. Only the published image fixes the wheel set, which
is why §11.4 declines to read a green CI suite as proof of numerical reproducibility.

---

## 10. Security model

| Boundary | Enforcement |
|---|---|
| **Authorisation** | Galaxy's role-based access control. Users, roles, groups and quotas are the platform's responsibility, not ours. |
| **Job isolation** | Every job runs in a container as an unprivileged user. |
| **Formula parsing** | User-supplied model formulae are parsed into a restricted syntax tree by a default-deny allowlist of permitted calls with a depth limit. They never reach `eval`, `exec`, or a formula library that evaluates terms in a caller-supplied namespace. Adopting `patsy` or `formulaic` would introduce that surface and owes `SECURITY.md` a new section first. |
| **Path arguments** | File-path arguments pass a structural gate rejecting traversal, absolute paths, control characters and disallowed extensions. |
| **Function-name arguments** | Arguments naming a function to apply are restricted to a closed enumeration mapped internally to fixed callables — never resolved through `getattr` on a user-supplied string. |
| **Network** | No wrapper makes a network call. Verified: **0 of 251**. The single deliberate exception is the external-data node, which lives outside the wrapper set — see `U52`. |
| **The engine boundary** | No numerical or statistical distribution may appear in any dependency group of `backend/`. This is not guaranteed by `backend/` and `engine/` being different languages; both being Python removed the mechanism, so it is now a continuous-integration gate carrying its own positive control. |
| **Cross-origin access** | An explicit allow-list; the canvas origin must be named. |
| **Deserialisation** | `pickle` is never used on any input. Tabular data crosses the boundary as Arrow or CSV, both data-only formats that cannot carry executable content. |

---

## 11. Continuous integration and delivery

The project is open source from its first commit; every gate below is public and runs on every pull
request unless stated otherwise.

This section distinguishes **implemented** gates — carried forward from a working configuration — from
**decided but not built**. Presenting the second group as if it existed would be exactly the kind of
false claim this document exists to prevent.

### 11.1 Specified, and written — but not yet proven

> **A `.github/` directory exists, and nothing in it has ever run.** Five workflow files are present
> — `ci.yml`, `engine-suite.yml`, `dco.yml`, `claude.yml`, `claude-review.yml` — together with a
> composite inventory action, a ruleset definition and the repository templates. The repository has
> **zero commits**, so not one of these gates has executed against a pull request.
>
> That distinction is the whole point of this section. A workflow file is not a gate. A gate is a
> file that has been observed **passing on correct input and failing on incorrect input**, and until
> both have been seen it is an intention with YAML syntax.
>
> **What has had its failure path exercised locally**, which is the nearest thing to evidence
> available before a first push: the inventory assertion (perturbed constant, corrupted sidecar, and
> now an unmeasurable constant, which it reports as `OWED` and exits 1 on); the container-path check
> (four `COPY` sources named as missing, which is the gate working); the pre-commit SPDX hook
> (rejects a missing header *and* a header naming a superseded licence, accepts a correct one); and the
> engine-boundary check (its planted `statsmodels` manifest is caught before it reports on the real
> tree). The rest have not.
>
> Each gate leaves this caveat individually, on the day its negative control is observed red.
>
> Two of them cannot be built at all yet, because they act on a TypeScript layer this repository
> does not contain; they are marked **blocked** below.
>
> One correction, since this section previously implied otherwise: requiring every leaf job context
> is the documented way to block every merge permanently — a required check that is skipped or
> renamed remains `Expected` forever. The ruleset names a single aggregate context, `ci-gate`, to
> which new gates attach as dependencies.

| Gate | Enforces |
|---|---|
| Code generation, type check, test, build — **blocked** | The TypeScript layer compiles, passes tests, and its generated code is current. No TypeScript exists here yet. |
| Fixture drift — **partial** | Committed cross-language fixtures still match what the code produces, byte for byte. The engine side is complete; the cross-language half needs the TypeScript layer. |
| Licence and SPDX | Every source file declares its licence identifier, and declares the *right* one: 380 of 380 Python files carry `AGPL-3.0-only`, and any other value fails rather than merely being counted. |
| Lint and commit message — **partial** | Commit subjects follow the agreed vocabulary. "Static analysis with type information" is TypeScript-only and does not apply yet. |
| Artifact drift | Each generator re-run in `--check` mode must reproduce its committed output exactly, and the loop must have run as many generators as the manifest declares. |
| Lint | `ruff` over the engine, with a floor on the number of candidate files it examined. |
| **The engine boundary** | No statistical dependency in any `backend/` dependency group. **New, and it replaces a mechanism rather than adding a rule** — see below. |
| Workflow validity | Continuous-integration definitions are themselves linted; shell scripts are checked; the ruleset's required contexts are proven to resolve to real jobs. |
| Container build and scan — **not yet run** | Images build; a bill of materials is produced and scanned for known vulnerabilities. The container has never been built in its current state. |
| Static security analysis | Secret detection with a positive control that fails if detection stops working, and container-definition linting. CodeQL joins this once configured — its verdict was reversed on 2026-08-16, since the language objection that deferred it has expired. |
| Dependency vulnerabilities — **partial** | The lockfile is scanned, gated on scan result *and* on package count — a scan that silently covered nothing must fail. The JavaScript half awaits that layer. |

The **anti-vacuity** pattern above is deliberate and applies throughout: a gate that passes because it
examined zero files has not passed. Every such gate asserts a minimum quantity of work done.

> **The gate that used to fail green, and how it was found.** The pre-commit SPDX hook selected
> a selector for a file type that is gone. On a tree with no such files in it that matches nothing, and a hook that matches nothing is
> reported as *Passed* — the one check in this repository capable of going green having examined zero
> files, which is precisely what this subsection forbids. It now selects `\.py$` and asserts the
> identifier as well as its presence, because a presence-only check would have accepted a file still
> carrying the old licence header while contradicting `LICENSE`.
>
> **A related hazard, measured rather than assumed.** On a maintainer machine `grep` resolves to
> **ugrep 7.5.0**, whose `--include` under `-r` reported **315** of **379** files where GNU grep
> reported 379 — silently omitting the entire generated tier. Continuous-integration runners ship GNU
> grep, so a counting gate written with `--include` passes there while undercounting locally, which is
> the direction that lets a real gap through. Every count in `assert.sh` and in the `spdx` job is
> therefore taken with `find` and `xargs`, never with `grep --include`, and `CONTRIBUTING.md` records
> the prohibition for anyone writing the next gate.

> **A file extension was a gate, and nobody had written it down as one.** `no statistic is ever
> computed outside engine/` was enforceable for free while the engine was the only place a
> statistical library could load. `backend/` and `engine/` are now the same language, so one import in
> a tool wrapper would move a statistic with nothing to notice. The rule survives; its enforcement was
> rebuilt as `.github/scripts/check-engine-boundary.sh`, which checks dependency *declarations* rather
> than import statements — a dependency cannot be smuggled past a lockfile, and the declaration is
> what appears in a diff. Because `backend/` holds no code yet, the script plants a manifest declaring
> `statsmodels` and fails if that is not caught, so it cannot pass by examining an empty directory.

### 11.2 Added for this architecture

| Gate | Enforces |
|---|---|
| Tool linting | Every generated tool file is schema-valid. |
| Tool testing | Declared tool tests execute against a real platform instance. |
| Workflow linting | Workflows satisfy metadata best practice. |
| Tool generation drift | Regenerating tools from the engine artifact reproduces what is committed. |

### 11.3 Decided but not built

Named here so their absence is explicit: static application-security analysis, end-to-end browser
testing, release automation, multi-architecture image publication, build provenance attestation,
open-source health scoring, and action-pinning verification. Which of these get built, and in what
order, is `U54`.

Four items moved *towards* this list rather than off it on 2026-08-16. SonarQube, its agent, Endor
Labs and CodeQL were all excluded on the grounds that they did not analyse the engine's language.
That objection expired, the verdicts were reversed, and each is now a configuration change away — but
**a reversed verdict is not coverage**, and `docs/decisions/marketplace-apps.md` states so in place
rather than letting a table of intentions read as a table of gates.

### 11.4 Not run in continuous integration

The full engine suite is long enough that making it a required per-pull-request check would make
every pull request as long.

**`U55` is answered** (`.github/workflows/engine-suite.yml`): a path-selected subset on every pull
request, the **full suite required on every push to `main`**, an opt-in `full-suite` label for a
risky branch, and a nightly full run. Actions minutes are unlimited on a public repository, so the
constraint was never cost — it was latency.

**This does not fully close the gap, and the gap is worth naming precisely.** A pull request that
touches a wrapper whose tests are not matched by the path selector can still merge green. What the
post-merge run buys is the difference between *silently* broken and *loudly* broken — a red run on
`main` opens an issue labelled `broken-main`. That is a real improvement and it is not the same thing
as per-pull-request protection.

**A second trap in the same job, which fails green and has already been measured once.** The subset
step sets `working-directory: engine`, and git pathspecs resolve against the current directory. The
correct pathspec is therefore `'src/**/*.py'`. Writing the apparently more careful
`'engine/src/**/*.py'` matches **nothing** from there: the changed-file list comes back empty, the
step exits 0, and the green tick means the selector found no changes rather than that the changes
passed. `docs/decisions/repository-layout.md` records the measurement.

One further limit, recorded because a green run here would otherwise be read as more than it is: the
suite runs on a stock runner against whatever OpenBLAS build the installed wheels carry, not against
a fixed one. Thread counts are pinned, which removes the scheduling-order variation, but two
different wheel builds of the same version are still not guaranteed to agree in the last bits. So a
green run proves the tests pass; it does not prove they produce the pinned numbers. The authoritative
run is the one inside the engine image, where the lockfile fixes the wheel set and the suite is a
build gate. When that image is published and this workflow runs inside it, this caveat is retired.

---

## 12. Containers and deployment

### 12.1 The engine image

A three-stage build on `python:3.12-slim`. The first stage installs the small set of system libraries
the scientific wheels link against and fixes the linear-algebra thread count; the second restores the
locked environment with `uv sync --locked`, copies the sources, and **runs the full test suite as a
build gate** — a failing suite fails the image; the third produces a minimal runtime layer running as
an unprivileged user.

The build context is the repository **root**, not `engine/`, because the image copies `LICENSE` and
because the workspace `pyproject.toml` and the single `uv.lock` are root files.

Two details are load-bearing and must survive any refactor:

- **The thread pin.** `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS` and `MKL_NUM_THREADS` are all set to
  one. This is the sibling of the reference-BLAS installation the previous image performed, and it
  exists for the same measured reason: a multithreaded backend's reduction order depends on how work
  was split across threads, so the same input can land on a different last bit with no code change
  and no seed change. Removing it does not break the build — it quietly stops the numbers being
  reproducible, which is worse.
- **The in-image suite run**, which prevents an image existing that has not proven itself.

**There is no healthcheck, and its absence is the design rather than an omission.** The previous image
carried one against an HTTP router's liveness endpoint. §2 states that the engine is not a service:
this container computes one node and exits, so a liveness probe would report a fault precisely when
the design is working.

### 12.2 Services

| Service | Role |
|---|---|
| Galaxy | Web processes, job handlers and background workers. Image: **`quay.io/galaxyproject/galaxy-min`**, pinned by digest at the release chosen in `U8` — never by the `:latest` tag, which has not moved since 2021. |
| PostgreSQL | Galaxy's own database. |
| Message broker | Background task coordination and event fan-out. |
| Engine image | Not a running service. Started per job, exits when the method finishes. |
| Web canvas | Static assets, served behind the proxy. |
| Reverse proxy | Terminates connections and routes. Must disable buffering on the event-stream route, or live updates will not arrive. |

Compose is the primary deployment path. Upstream also provides configuration-management roles and a
Kubernetes chart; whether we support those is `U61`.

---

## 13. Licensing

**The entire repository is licensed AGPL-3.0-only** — every directory, every language, without
exception. There is no dual licence, no per-directory rule, and no commercial-use carve-out.

**Copyleft here is a choice, and the distinction is the whole content of this section.** The engine's
dependencies are the Python scientific stack — NumPy, SciPy, pandas, statsmodels, Arrow, pydantic —
and that stack is uniformly permissive: BSD-3-Clause, Apache-2.0 and MIT. None of it imposes a licence
on the work that imports it. Any licence at all would have been lawful, including a proprietary one.
So the licence has to be argued rather than reported.

**The argument is section 13 of the AGPL.** The deployed form of this project is a hosted compute
engine: the browser draws, and every statistic is computed on a server the user does not control.
Under GPL-2 and GPL-3 alike, running modified software over a network is not distribution, so a third
party may take this engine, improve it, operate it as a service and owe nothing back. For a
node-based analysis canvas that is not a hypothetical gap — it is the ordinary way such a product
reaches its users. AGPL-3.0 §13 attaches the obligation to *operation*: a user interacting with a
modified version remotely must be offered the corresponding source of that version.

**Version 3 only, not `-or-later`.** The reason the previous licence carried `-or-later` has gone: it
existed to reconcile mutually incompatible dependency licences, of which there are none left. What
would remain is a standing grant over terms that do not yet exist. Pinning to version 3 keeps the
licence a decision rather than a subscription. The cost is accepted deliberately — contributions
arrive under the DCO rather than a CLA (`U3`), so contributors keep their copyright and a future
Affero revision would need each of them to agree. A licence change should be hard enough to notice.

**One consequence governs every future dependency review.** AGPL-3.0 is one-way compatible with
GPL-3.0-or-later and is **not** compatible with GPL-2.0-only. A package published under GPL-2.0-only
can no longer be admitted to this tree, whatever its merits. No current dependency is affected; the
constraint is on what may be added, and `.github/ISSUE_TEMPLATE/method_request.yml` asks for a
proposed package's licence for exactly this reason.

Galaxy is MIT-licensed and is an upstream dependency, not vendored code; a permissive dependency
combines with a copyleft work without difficulty.

The written offer of corresponding source in `NOTICE` names a **GitHub channel** rather than an email
address: an issue titled "AGPL source request", with private vulnerability reporting as the fallback.
A published address is permanently harvested, and git authorship already uses GitHub's routed
no-reply address for the same reason. The obligation is unaffected — it requires a contact that
works, not an inbox.

`LICENSE` carries the argument above in full before the verbatim licence text, so that a reader who
opens only that file gets the reasoning and not just the terms.

---

## 14. Open decisions

Everything not yet decided, named. Each entry states what must be decided and what it affects.
Entries are referenced by identifier from the rest of this document.

### Identity and governance

| ID | Decision | Description and blast radius |
|---|---|---|
| U1 | ~~Product name~~ **DECIDED** | The product name is **EconFlow Analytics** — the repository name is the product name. Applied to the interface, documentation and citation metadata. |
| U2 | ~~Copyright holder~~ **DECIDED** | The copyright holder is **Panagiotis Tsikos**. Applied to `LICENSE`, `NOTICE` and `CITATION.cff`. |
| U3 | ~~Contribution instrument~~ **DECIDED** | **Developer-certificate sign-off only** (`git commit -s`), enforced by a continuous-integration check. No contributor agreement: under a uniform copyleft licence with no relicensing intent it would add friction for exactly the academic contributors §1 names as an audience. |
| U4 | Version scheme | Semantic or calendar versioning, and what constitutes a breaking change when the unit of change is a method catalogue. Affects release tooling and tool versioning. |
| U5 | Release automation | Whether releases and changelog entries are generated or hand-written. |
| U6 | ~~Publication timing~~ **DECIDED** | **Public from the first commit**, per §11's opening claim. The consequence is accepted deliberately: history is permanent from the first push, so licence correction, attribution and residue removal all happen *before* that commit rather than after. |
| U7 | Citation metadata | Authorship, and whether releases are archived to obtain a persistent identifier. Directly affects the academic audience. |

### Galaxy platform

| ID | Decision | Description and blast radius |
|---|---|---|
| U8 | Version pin and upgrade cadence — **cadence corrected, pin still open** | Upstream publishes a **long-term-support release in the first quarter of each year and two to three minor releases through it — roughly three per year, not every six to eight weeks** as this document previously stated. The 2026 LTS is the **26.0** line (current point release 26.0.1), supported until the next LTS; current stable overall is 26.1.1. Public servers update within 90 business days. **What remains open is which line we pin**, and it is not a free choice: §5.5 calls the server-sent event stream *core to us*, and that route is present from **26.1** but absent from the 26.0 LTS. So the decision is either 26.1.x with the event stream and the cost of tracking a non-LTS line, or 26.0.x LTS with polling-only live state and §5.5 amended to demote the stream. Upgrades are our work, not automatic; a rolling pin would break the canvas without warning. |
| U9 | ~~Official image identity~~ **DECIDED** | The image is **`quay.io/galaxyproject/galaxy-min`**, on Quay. Established by ownership rather than by a marketing claim: it is what the galaxyproject-owned Helm chart pins (`appVersion 26.0.0` at chart v6.8.2) and what the galaxyproject-owned build repository produces. ⚠️ **Never `:latest` — that tag was last modified 2021-10-08.** Not a sign of neglect: the project moved to explicit versioned tags and simply stopped publishing to `latest`, while `26.1.1` shipped on 2026-08-04. It is a trap precisely because the *rest* of the registry is current, so an unqualified pull looks reasonable and silently yields a five-year-old image. The current tags are `26.1.1` and `26.0.1` (immutable), `26.1-auto` / `26.0-auto` (rolling) and `dev`. Pin by **digest**, not by tag. Docker Hub's `galaxyproject` namespace is stale since 2023; there is no public image under `ghcr.io/galaxyproject`; `bgruening/galaxy` is a community image, one minor behind, and is not official. |
| U10 | ~~Dynamic tools versus static XML~~ **DECIDED — rejected** | Verified against the upstream source, not inferred. `/api/dynamic_tools` is gated behind `enable_beta_tool_formats`, which defaults to `false` on every instance. After a restart a dynamic tool is addressable **only by `tool_uuid`, never by `tool_id`** — the toolbox has no database fallback on the id path. Registration never calls the panel-insertion path, so such tools **do not appear in the tool panel**: unusable at 913. The permitted YAML subset **rejects `data_column` and `drill_down`**, which our column- and series-selecting methods need. And the framework ships a schema "lift" layer with `X-Galaxy-Deprecated-Fields` response headers — a system that provides forgiveness for its own stored payloads is one whose schema drifts between releases. **The 913 static Tool XML files stay.** To be clear about what this verdict is: the feature is **in beta and under active development**, not broken — the rejection is that it is not the right instrument for 913 tools *today*, and each objection above is a current-state measurement rather than a permanent property. The stronger evidence of that is upstream's own answer to our exact problem: the cached-toolbox / tool-source-storage work now on `dev`, whose motivating note reads *"with thousands of tools that scales poorly: slow boot, large per-process RSS, and expensive worker reloads."* It is absent from every current release. Track it and re-open this decision when it ships; do not depend on it yet. |
| U11 | Tool identifier and version scheme | How a method maps to a stable tool identifier, and what causes a version increment. Governs cache validity and stored-workflow stability — a careless increment invalidates every saved graph. |
| U12 | Tool panel organisation | Whether the 30 categories map directly to sections, and whether an ontology-based view is offered. |
| U13 | Tool distribution | Whether tools are published to a shared repository or shipped only with the application. |
| U14 | ~~Interface stability policy~~ **DECIDED — there is none, and here is the mitigation** | Confirmed rather than assumed: the API is **not versioned** (no `/api/v1`), and there is **no published deprecation window**. Upstream's own API guidelines open by disclaiming themselves — *"clients SHOULD NOT expect the API will conform to these guidelines"*. The OpenAPI 3.1.0 schema is served at **`/openapi.json`**, not `/api/schema`: 465 paths, of which **24 are flagged `deprecated`** and **102 are tagged `undocumented`** with no request or response models at all — roughly a fifth of the surface. What does exist is an **officially published, release-versioned TypeScript client**, `@galaxyproject/galaxy-api-client` on npm, released in lockstep with Galaxy. **We consume that client at the version matching our pinned server and never hand-roll one**, and continuous integration diffs `/openapi.json` between our pinned version and the next release, failing on the removal of any path we consume. That contract test is the mitigation; there is no upstream promise to rely on instead. **This is not a complaint about the project** — a two-decade-old codebase taking 100+ commits a month is exactly where informal API governance is normal, and the same velocity is why we benefit from building on it. It means our protection has to be a test we own rather than a guarantee we are given. |
| U15 | Resource allocation values | Concrete processor and memory allocations per memory class. The classes exist; the numbers do not. |
| U16 | Object store configuration | Local disk or an object-storage backend, and the retention policy. |
| U17 | Broker choice | Which message broker backs background work. |
| U18 | Quota policy | Quotas are inert until created. Whether any are applied, and at what values. |
| U19 | Cleanup schedule | Deleted data persists until purged. Retention and scheduling are unset. |
| U20 | Report and page usage | Whether platform-native reporting and narrative documents are exposed through our canvas or reimplemented. |

### Engine-to-platform contract

| ID | Decision | Description and blast radius |
|---|---|---|
| U21 | Tool entrypoint design | One generic runner script parameterised by method, or a generated script per method. Affects the generator and every tool file. |
| U22 | Parameter passing | A generated configuration file carrying one JSON document, versus command-line arguments. Determines how faithfully complex argument types survive the boundary. |
| U23 | Time-series datatype | Extension name, detection logic, and which metadata elements are exposed. Central: it is how frequency and start period survive between nodes. |
| U24 | Gate output contract | The exact structure a blocked gate emits, and how it is distinguished from a genuine failure. The most user-visible contract in the system. |
| U25 | Node-layer disposition — **partly decided** | The HTTP router and the inbound authentication layer are **removed** (§6.3): Galaxy supersedes them, and the reimplementation carried the removal rather than deferring it. What remains open is which of the surviving `node/` modules are kept or adapted, and what replaces the pointer contract. The discovery entrypoint, a viable interim answer to `U21`, depends on `node/store_pointers.py` — so that module's fate and `U21` are coupled. |
| U26 | Discovery gateway disposition | Whether the six-function gateway survives as the agent subsystem's reasoning surface, is ported to TypeScript, or is retired. |
| U27 | Chart specification delivery | Whether the chart specification is a separate output, embedded in the result, or computed client-side from result data. |
| U28 | Output dataset layout | One dataset per node, or a structured collection. Determines how naturally multi-output methods chain. |
| U29 | Contract hash role | Whether the existing contract hash drives tool versioning, cache identity, both, or neither. |
| U30 | Generation source of truth | Whether the committed artifact remains the input to tool generation, or tools are generated directly from the specification sources. |

### Web canvas

| ID | Decision | Description and blast radius |
|---|---|---|
| U31 | Component library and design system | Nothing chosen. Affects every screen and the accessibility baseline. |
| U32 | State management | Client state and server-state caching strategy. |
| U33 | Routing | Library and whether analyses are deep-linkable. |
| U34 | Authentication flow | How the canvas authenticates: key, session, or external identity provider. Interacts with `U49`. |
| U35 | Chart coverage | Which chart types the 913 methods actually require, and the fallback when a result has no chart representation. |
| U36 | Localisation | Whether the interface is English-only. |
| U37 | Accessibility target | Which conformance level is claimed and tested. Claiming without testing would be a false claim. |
| U38 | Offline behaviour | Whether the canvas remains usable without a reachable backend. |
| U39 | Graph persistence | Whether canvas graphs are stored as platform workflows or in our own store. Determines whether a saved graph survives a platform upgrade. |
| U40 | Gate presentation | How a blocked node communicates the rule and the remedy. The correctness thesis is only credible if this is genuinely educational. |

### Integration

| ID | Decision | Description and blast radius |
|---|---|---|
| U41 | Backend-for-frontend | Whether an intermediary service exists at all, or the canvas calls the platform directly. Affects deployment shape and where secrets can live. |
| U42 | Translation ownership | Where graph-to-workflow translation lives and how its output is versioned across upgrades. |
| U43 | Stream resilience | Reconnection, backoff, and reconciliation of state missed while disconnected. |
| U44 | Error taxonomy | The complete mapping from platform job and invocation states to canvas node states. |

### Agent subsystem

| ID | Decision | Description and blast radius |
|---|---|---|
| U45 | Known-good providers | Which model providers are documented as tested. |
| U46 | Execution location | Whether agents run in the browser, in an intermediary, or as a separate service. Determines where a key can safely live. |
| U47 | Vector store placement | Whether embeddings share the platform database or use a separate one. |
| U48 | Corpus ingestion | Sources, ingestion mode, and the structural constraint that prevents redistributing copyrighted text. |
| U49 | Agent authorisation | How an agent acts on behalf of a user without exceeding that user's permissions. |

### Data

| ID | Decision | Description and blast radius |
|---|---|---|
| U50 | Upload path | Native platform upload versus our own conversion producing a columnar file plus a metadata sidecar. Determines whether frequency and start period are captured at ingestion. |
| U51 | Accepted formats | Previously settled as comma- and tab-separated, JSON, and columnar. Requires reconfirmation against native capabilities. |
| U52 | External data node | The one deliberate network exception. The official client library for the intended source is **unmaintained since 2020-10-25 and licensed AGPL-3** — both disqualifying. The alternative is a small node calling the documented interface directly with a minimal field set that **fails loudly** rather than silently on an upstream change. No integration can be immune to upstream change; the honest goal is a small surface and safe failure. |
| U53 | Conversion library retention | Whether the existing conversion package survives, given the platform's own ingestion. |

### Continuous integration

| ID | Decision | Description and blast radius |
|---|---|---|
| U54 | Unbuilt gates | Which of the decided-but-not-built gates in §11.3 are implemented, and in what order. |
| U55 | ~~Engine suite placement~~ **ANSWERED — see §11.4** | A path-selected subset on every pull request, the full suite required on every push to `main`, an opt-in `full-suite` label, a nightly full run, and a blocking run on any release tag. §11.4 also states plainly what this does **not** close: a pull request touching a wrapper whose tests are not matched by the path selector can still merge green. This row is retained struck through rather than deleted, because the limitation is part of the answer. |
| U56 | Tool testing infrastructure | Tool tests need a live platform instance; how continuous integration provides one. |
| U57 | End-to-end strategy | What a full-stack test covers and how the environment is provisioned. |
| U58 | Coverage enforcement | Coverage floors were agreed but never gated. Whether they become gates. |
| U59 | Runner sizing | Whether hosted runners suffice for image builds and the engine suite. |
| U60 | Registry | Where images are published and how they are pinned by digest. |

### Deployment

| ID | Decision | Description and blast radius |
|---|---|---|
| U61 | Supported methods | Compose only, or also configuration-management and Kubernetes paths. Each supported path is a maintenance commitment. |
| U62 | Proxy configuration | The proxy definition we ship, including the buffering requirement on the event stream. |
| U63 | Backup and restore | What is backed up, how often, and the documented restore procedure. |
| U64 | Observability | Structured logging versus full tracing. Carried forward unresolved from the previous architecture. |
| U65 | Minimum hardware | The previous floor was explicitly lifted. A new, measured minimum is required before installation instructions can be honest. |
| U66 | Single-user configuration | Multi-user is built first. A simplified single-user version is deferred until the project is otherwise complete. |

---

## 15. Glossary

One term per concept, used consistently throughout this document.

| Term | Definition |
|---|---|
| **Wrapper** | One Python module exposing one package's methods, with gates. There are 251. |
| **Method** | One callable analysis function within a wrapper. There are 913. |
| **Generated tier** | The 64 modules under `src/econflow_engine/generated/`, emitted from `node-specs.v1.json` by `scripts/gen_schemas.py`. Committed, never hand-edited, and re-emitted in `--check` mode by the `artifact-drift` gate. |
| **Frozen artifact** | A committed JSON contract that is an *input* to this engine rather than an output of it — the 913 node specifications, the 252 cards, the 4855 parity verdicts and the 114 recommendation fixtures. They are the oracle the engine is checked against, and are never regenerated from it. |
| **Node** | A method as it appears on the canvas. One method, one node. |
| **Tool** | A method as the platform sees it: one XML definition, one executable step. |
| **Job** | One execution of one tool. |
| **Invocation** | One execution of one workflow, comprising many jobs. |
| **History** | A platform-side container of datasets belonging to one line of work. |
| **Dataset** | One typed data object with state and metadata. |
| **Collection** | A structured group of datasets over which a tool can be mapped. |
| **Gate** | An explicit refusal to compute because documented preconditions are unmet. Not an error. |
| **Blocked** | The canvas state of a node stopped by a gate, showing the rule and its requirement. |
| **Card** | One entry in the method-selection catalogue: what a method is, when to use it, and its source. There are 252. |
| **Contract hash** | A hash over a node's declared interface, used to detect drift between the engine and generated artifacts. |
| **Memory class** | A node's resource tag — `light`, `heavy` or `mcmc` — used to route its job to an appropriately sized destination. |
| **Anti-vacuity** | The requirement that a gate assert a minimum quantity of work done, so that passing because it examined nothing is impossible. Every constant such a gate asserts lives in `.github/inventory.json`. |
| **Engine boundary** | The rule that no statistic is computed outside `engine/`, and the continuous-integration check that enforces it now that both it and `backend/` are Python. |
