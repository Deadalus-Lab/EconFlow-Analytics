<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `backend/` — the platform integration layer

**Specified. Not built.** This directory is empty of code on purpose, and the reason is in
[Why it does not exist yet](#why-it-does-not-exist-yet) rather than in anyone's backlog.

Named `backend/` rather than `galaxy/`: Galaxy is the platform this layer integrates with, but the
directory holds *our* backend — the tools, datatypes and configuration we own.

The platform layer owns job execution, scheduling, data management, users and provenance —
everything between the canvas and the compute engine that we would otherwise have written and
maintained ourselves. It is an upstream dependency, never vendored or patched.

## the rule that governs this directory

**No statistic is ever computed here.** This layer and `engine/` are both Python and are the two
members of one `uv` workspace, so nothing about the toolchain stops you importing `statsmodels` in a
tool wrapper. What stops you is `.github/scripts/check-engine-boundary.sh`, which fails the
`engine-boundary` job if `numpy`, `scipy`, `statsmodels`, `pandas`, `pyarrow` or any other numerical
distribution appears in **any** dependency group of this directory.

That is a deliberate replacement rather than a new restriction. While the engine was written in another language, the file
extension enforced the rule for free; both sides being Python removed the mechanism and left the rule
standing on its own. The check declares itself with a positive control, so it cannot pass by
examining an empty directory. See
[`docs/decisions/python-engine.md`](../docs/decisions/python-engine.md).

This layer moves datasets; it does not open them. If a tool ever genuinely needs to read a table
rather than pass a path along, that is a decision with a diff, not a dependency added on a Tuesday.

## the second rule: Conda is never consulted

The platform's default dependency path ends in Conda, and Conda resolves Python natively — so a job
that fell through to it would install *something plausible* and compute *something plausible* with a
wheel set `uv.lock` never described. Every gate would stay green and the numbers would be wrong.

Six mutually redundant mechanisms close that path, and none of them is decorative: one explicit
container resolver, an empty dependency-resolver list, `require_container` on every environment with
a count assertion, Conda auto-init and auto-install disabled, a negative-control tool that must
**fail** rather than fall back, and a grep of the whole boot log. The reasoning behind each is in
[`../ARCHITECTURE.md`](../ARCHITECTURE.md).

The engine image is named **once, by digest** in a single macro token. Never by tag —
`quay.io/galaxyproject/galaxy-min:latest` was last modified 2021-10-08 while 26.1.1 shipped
2026-08-04, and the trap is that the rest of the registry is current, so an unqualified pull looks
entirely reasonable.

## what will be here

| Path | Contents |
|---|---|
| `PINS.yml` | The pin triple: image digest, typed-client version, schema snapshot release |
| `config/` | `galaxy.yml`, `job_conf.yml`, `tpv/`, `datatypes_conf.xml`, `tool_conf.xml`, the resolver files |
| `contracts/` | The committed `/openapi.json` snapshot, the gate document schema, the datatypes contract — each with a `.sha256` sidecar |
| `datatypes/` | The five custom datatype classes, as an installable distribution |
| `scripts/` | The tool generator, with a `--check` drift mode |
| `tools/` | One generated Tool XML per method, plus the shared macro library |
| `tests/` | Datatype tests, negative controls and tool tests |
| `measurements/` | The resource campaign and the disk-footprint breakdown |

Nothing in `tools/` is written by hand. It is generated from
`engine/artifacts/node-specs.v1.json`, byte-deterministically, and a drift gate re-emits it and
compares byte for byte — the same discipline the engine's own generators already follow.

## why it does not exist yet

The tool files are generated, and the generator cannot be written before the seam is settled: the
tool entrypoint, parameter passing, the gate output contract and the time-series datatype are all
open decisions (`ARCHITECTURE.md` §14, `U21`–`U24`). Scaffolding files ahead of those decisions would
encode guesses as structure.

One decision gates everything else. `U8` — which Galaxy line we pin — is not a free choice, because
`ARCHITECTURE.md` §5.5 calls the server-sent event stream *core to us* and that route exists from
26.1 and is **absent from the 26.0 LTS**. It is settled by four measurements, not by reading a
changelog.

## where the work is planned

| Guide | Covers |
|---|---|
| [`../ARCHITECTURE.md`](../ARCHITECTURE.md) | The pin, the configuration, the datatypes, the generated catalogue, routing, retention, and the seam between the platform and the engine |

See [`ARCHITECTURE.md` §5](../ARCHITECTURE.md) for the complete list of platform features this layer
relies on, and which of them are core rather than optional. See
[`docs/galaxy-provides.md`](../docs/galaxy-provides.md) — once it exists — for the register of what
the platform already gives us and must never be rebuilt here.
