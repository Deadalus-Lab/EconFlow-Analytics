<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Roadmap

What is built, what is not, and the order the rest arrives in.

[`ARCHITECTURE.md`](../ARCHITECTURE.md) describes what the system **is** and names every decision not
yet taken. This document says what has to **happen**. Where the two disagree, `ARCHITECTURE.md` wins.

One rule governs both: **nothing is described as working until it has been observed working.** A
written CI workflow is not a gate; a gate is a check that has been seen passing on correct input and
failing on incorrect input. Items below are marked accordingly, and the distinction is never blurred
to make progress look better than it is.

---

## Status

| Layer | Language | State |
|---|---|---|
| Compute engine | Python | **Complete.** 251 wrapper modules, 913 methods, 30 categories |
| Platform integration | Python | Specified, not built |
| Integration layer | TypeScript | Specified, not built |
| Web canvas | TypeScript | Specified, not built |
| Agent subsystem | TypeScript | Specified, not built |

The engine's figures are reproduced by the commands in [`README.md`](../README.md), run from
`engine/`, and re-measured on every pull request by `.github/inventory.json`. Re-run them rather than
trusting any written number, including those.

---

## Phases

### Foundation

| # | Phase | What it delivers |
|---|---|---|
| 0 | Pre-publication | Licence, attribution and contact correctness; the three language toolchains declared and pinned; first commit |
| 1 | Gate architecture | One aggregate required check, so a skipped or renamed job cannot block every merge forever |
| 2 | Decision sprint | The Galaxy version pin, the image identity, and the engine↔platform seam settled in writing before code depends on them |
| 3 | Measurement baseline | Every published figure re-measured with the command that produced it |
| 4 | Repository layout | One top-level directory per **layer**, the public root surface asserted in both directions, and the engine boundary enforced by a check rather than by a file extension ✅ **done** |

### Engine contracts

| # | Phase | What it delivers |
|---|---|---|
| 5 | Interface freeze | Every change that moves the contract hash, batched into one |
| 6 | Engine contracts | The gate output contract, the tool entrypoint, parameter passing, the time-series datatype, output layout |
| 7 | ~~Retire the HTTP layer~~ | **Subsumed.** This phase existed to remove the router Galaxy supersedes, sequenced carefully because doing so would move the constants the gates assert. The reimplementation carried the removal: the 913 routes, the inbound authentication layer, the container healthcheck and the router entrypoint are simply absent, and §4.1's constants were measured without them. There is no delta left to apply — see `ARCHITECTURE.md` §6.3 |
| 8 | The engine image | The only environment that can prove the pinned numerics, because it is the only one where the lockfile fixes the wheel set rather than the runner choosing it |

### Platform

| # | Phase | What it delivers |
|---|---|---|
| 9 | Galaxy foundation | A pinned instance that boots with our configuration and none of our tools |
| 10 | Galaxy catalogue | 913 generated tools, the panel, and job routing by memory class |

### Integration and canvas

| # | Phase | What it delivers |
|---|---|---|
| 11 | Typed contract | Zod schemas generated from the engine artifact, proven against 4855 parity cases |
| 12 | Integration runtime | Graph translation, invocation lifecycle, the state taxonomy, live updates |
| 13 | Canvas foundation | Generated forms, typed connection handles, the 913-node palette |
| 14 | Canvas product | What a result actually looks like — including the blocked node, which is where the correctness claim becomes visible to a user |
| 15 | System proof | End to end, on Compose, under a memory limit |

### Operation and reach

| # | Phase | What it delivers |
|---|---|---|
| 16 | Operations | Backup and restore with a drill that proves it; observability; a measured hardware floor |
| 17 | Product lifecycle | Adding, changing and deprecating a method; wrong-number triage |
| 18 | Agent subsystem | The optional layer that helps assemble a graph and never computes |
| 19 | Quality and reach | Accessibility, localisation, dependency and licence update pipelines |
| 20 | Beyond CI | The gates continuous integration structurally cannot provide — scheduled human review |
| 21 | Editions | Single-user and single-tenant configurations |

---

## What the engine already guarantees

These are properties of the code as it stands, not plans:

- **Gates, not warnings.** Every documented requirement of every method is an explicit refusal to
  compute. An invalid result cannot escape; it becomes a blocked node with a stated reason.
- **Generated contracts.** Node schemas are generated from the committed node-specification
  artifact, so the contract cannot drift from the implementation. The generated form is committed
  and reviewed in a diff, and a gate re-emits it and compares byte for byte.
- **Pinned computation.** Interpreter version, package versions and package *hashes* in one
  lockfile, and every linear-algebra thread pool pinned to one.
- **No network.** No wrapper makes a network call — 0 of 251.
- **A guarded boundary.** No statistical dependency may appear in `backend/`. This is now a
  continuous-integration check with its own positive control, because both layers being Python
  removed the mechanism that does not enforce it for free.

## What is deliberately not decided

`ARCHITECTURE.md` §14 carries the open decisions with their blast radius. They are listed there
rather than omitted, because an unanswered question is a register entry, not a gap.

## Contributing

See [`CONTRIBUTING.md`](../CONTRIBUTING.md). The engine suite must exit 0 before you start, so that a
red suite after your change is unambiguous about its cause. Sync from the repository root with
`uv sync --locked`, never from inside `engine/`: the two Python layers are one workspace with one
lockfile, and syncing a member on its own produces a second environment nothing governs.
