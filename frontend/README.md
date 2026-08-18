<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `frontend/` — TypeScript

**Specified. Not built.** This directory holds this file and a `.nvmrc`, and that is deliberate.

Named `frontend/` rather than `typescript/`: it is the user-facing half of the system. It also holds
the integration libraries under `packages/` — `galaxy-client`, `graph-model` and the generated
`node-schemas` are not strictly "frontend" code, but they exist to serve the canvas and share its
toolchain, so they live in the same workspace.

One workspace holding both the integration layer and the web canvas. It is the only place in the
repository where TypeScript lives.

## What will be here

| Path | Contents |
|---|---|
| `web/` | The canvas single-page application — Vite, React, React Flow, ECharts |
| `packages/node-schemas/` | Zod schemas **generated** from `engine/artifacts/node-specs.v1.json` |
| `packages/method-selection/` | Method cards and the deterministic `recommend()` |
| `packages/graph-model/` | Canvas graph ↔ platform workflow translation |
| `packages/galaxy-client/` | Typed client over the platform API, pinned to the server version |
| `packages/corpus/` | Retrieval corpus and local embeddings |
| `packages/agents/` | The agent subsystem |

## The rules that govern this directory

**No statistic is ever computed here.** Every number comes from the engine. The single sanctioned
exception is the port of `recommend()`, which exists to be validated against the fixtures committed
in `engine/artifacts/recommend-fixtures.v1.json` — and it runs as a post-hoc judge, never as a tool a
model may call, because a tool can be left uncalled.

**Schemas are generated, never hand-written.** The input is `node-specs.v1.json`, verified against
its `.sha256` sidecar *before* it is parsed. That is the only way the contract can be prevented from
drifting from the implementation, and `frontend/packages/node-schemas` has exactly one owner —
Phase 5. Nothing else in the repository regenerates it.

**The browser draws; the engine never does.** The engine emits chart *data* and a chart
*specification*. No image, widget or rendered artefact crosses the boundary. This was a preference
under the engine and is a rule under Python, where a plotting library is one dependency away.

**Two projections, not one.** The canvas edits the *authoring* projection — handles are edges, paths
are tickets, defaults are materialised for form prefill. The engine executes the *wire* projection —
handles are resolved pointers and **no default is ever materialised**. The function between them
already exists in `engine/src/econflow_engine/kinds.py`; this layer mirrors it rather than inventing
a second one.

**`.optional()`, never `.nullable()`.** The engine's adapter reads an explicit `null` as *absent*, so
an optional argument with no value must **omit the key**. `engine/artifacts/intentional-divergences.json`
records the client's rejection of `null` as a deliberate, safe-direction divergence — and it holds
only while nothing here is nullable.

**The wire argument name never changes.** Dotted names and language keywords are renamed on the
engine's side only. A generator that tidies `p.adjust.method` into a nicer object key produces an
unknown-argument rejection.

## Why it does not exist yet

`ARCHITECTURE.md` §11.1's correction was that *specified is not implemented*. An empty workspace with
a `package.json` would be a claim that something exists. The stack decisions it depends on — component
library, state management, routing, authentication flow — are open (`U31`–`U34`), and no continuous
integration gate in this repository has ever executed, so nothing here can yet be described as
gated.

## Where the work is written down

| | |
|---|---|
| [`../ARCHITECTURE.md`](../ARCHITECTURE.md) | The integration layer and the canvas: node states, generated forms, the blocked node, charts, accessibility |
| [`docs/ROADMAP.md`](../docs/ROADMAP.md) | Where those phases sit in the whole build |
