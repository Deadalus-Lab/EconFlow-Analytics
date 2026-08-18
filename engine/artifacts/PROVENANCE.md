<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# Provenance of the committed artifacts

**These files are input, not output.** Nothing in this repository can regenerate them, and no future
version of this engine will be able to either. Read that as a hard constraint before changing
anything here.

The specification sources is not hand-written and the artifacts derived from them. That
relationship reversed with the language. The sources were another language — a spec tier under `the specification tier`
and 251 wrapper modules — and they are no longer in the tree. What survives is what
they produced, and the current engine is generated *from* it and checked *against* it.

```
 the engine spec sources + wrappers (NOT IN THE TREE — see "the oracle" below)
 │
 ▼
 artifacts/*.json FROZEN INPUT
 │
 ┌──────────────┴──────────────┐
 ▼ ▼
 scripts/gen_schemas.py scripts/gen_wrappers.py
 generated/** (3 tiers) wrappers/** (251 modules + 30 READMEs)
```

## What each file is

| File | What it holds | Producer | Seal |
|---|---|---|---|
| `node-specs.v1.json` | the node contracts — arguments, kinds, allowlists, memory classes, `contract_hash`, and the vocabulary every allowlist reads | the corpus exporter | `.sha256` |
| `method-cards.v1.json` | one card per method — `when`, `when_not`, `alternatives` with criteria, interpretation traps, sources, and the `wrapper_file` join key | the corpus exporter | `.sha256` |
| `method-trees.v1.json` | the master decision trees behind method selection | the corpus exporter | `.sha256` |
| `parity-fixtures.v1.json` | frozen accept/reject verdicts from the own argument adapter, with the closed reason-code set | the corpus exporter | **none — see below** |
| `recommend-fixtures.v1.json` | fixtures covering every recommendation status | the corpus exporter | `.sha256` |
| `intentional-divergences.json` | the register of deliberate schema divergences, all in the safe direction | hand-maintained | **none — see below** |

Counts are deliberately absent from this table. Read them from the files, with the commands recorded
in `.github/inventory.json` under `commands`.

## Why two files carry no sidecar

Neither omission is an oversight, and the reasons are different.

**`parity-fixtures.v1.json`** — the parity suite reads it *in full* on every run, replays every case,
and asserts three properties over the result. That is strictly stronger than comparing a digest: a
digest proves the bytes did not move, while the replay proves the bytes still describe this engine's
behaviour. Adding a sidecar would add a weaker check beside a stronger one and invite the weaker one
to be treated as sufficient.

**`intentional-divergences.json`** — it is a hand-maintained input. There is nothing to re-derive it
from, so a digest could only certify that nobody edited it, which is exactly the wrong property for a
file whose whole purpose is to be edited when a deliberate divergence is added. What guards it instead
is the parity suite's P3 property, which asserts **set equality** between the observed divergences and
the declared ones — a new divergence and a dead entry both turn the suite red.

`.github/actions/assert-inventory/assert.sh` verifies the sealed files and refuses to pass if it
verified fewer than it should have. That floor exists because a glob that matched nothing would
otherwise "verify" every sidecar without having opened one.

## What is pinned to what

`method-cards.v1.json` records the digest of the node specs it was generated against, in
`source.node_specs_sha256`. It equals the content of `node-specs.v1.sha256`. The two artifacts are
therefore pinned to one another, and a card set generated against a different node-spec revision is
detectable without opening either file.

`node-specs.v1.json` records `engine.spec_source_sha256` — a digest of the reference spec sources that
produced it. Those sources are gone, so the value can never be recomputed. It survives as an identity
token: any future corpus or fixture claiming to describe this contract carries the same value, and a
mismatch means the two were produced against different contracts.

## contract_hash: carried, never computed

Each node carries a `contract_hash` over its function name, arguments, register field and export
field — and explicitly **not** over its memory class, so that a resource-allocation change cannot
invalidate a stored graph.

The digest is taken over the binary serialisation of that object. **Python cannot reproduce it and
must never try.** A recomputation would look entirely plausible, would produce a different value for
every node at once, and would invalidate every tool version and every saved analysis simultaneously.
The generated tier carries the string verbatim; that no hash function appears anywhere under
`src/econflow_engine/generated/` is checked, not trusted.

## The oracle, and where it actually lives

`parity-fixtures.v1.json` freezes what the reference engine **accepted**. Nothing here freezes what it
**returned**.

**The oracle is established independently**, from three sources: a published paper's reported
figures, a hand-verified fixture, and a property that must hold. Checking a method only against
another implementation of it would prove the two agree, including where both are wrong.

The wrapper
docstrings name `METHOD-SOURCES.json` — the register of which library or paper implements each
module — rather than a source file to copy.

What each candidate oracle can and cannot
prove, and why the paper-replication route is not a fallback but a different and in one respect
stronger instrument.

## Rules

1. **Never edit an artifact by hand.** Not to fix a typo, not to add a field, not to make a gate green.
2. **Never regenerate one to resolve a drift failure.** Drift means the code moved, not the contract.
3. **A number quoted from an artifact is stale the moment it is written down.** Read it with the
 command in `.github/inventory.json`.
4. **Changing a sealed artifact means changing its sidecar in the same commit**, and both are reviewed
 together. That is the point of the seal, not an obstacle to working around.

## The edit register

Every deliberate change to a sealed artifact, with its reason and its resulting digest. If a file's
digest does not match the last row here and its sidecar, something happened that nobody recorded.

### `method-cards.v1.json` — 2026-08-16

**What changed.** 64 citations in `sources` and `interpretation_traps` named a planning file by its
filename; each now reads `the normative gate spec §3b`. The same substitution was applied to the two catalogue files
the cards were exported from, `METHOD-SELECTION.md` (26) and `METHOD-SELECTION.yaml` (32), so the
three stay consistent.

**Why.** The cards cited a planning document by filename. That file was removed from the project, so
every one of those citations pointed at nothing, and the 30 generated category READMEs rendered the
dead reference to every reader of a method card.

**What did not change.** No card was added, removed or renumbered. No `tool_fns` list, no
`wrapper_file`, no `when`/`when_not`, no numeric value, no structure. The card count and the
card→node join are unchanged, and `assert-inventory` verifies both.

**Digest after.** `5ad7a67c9c7647cc9db08346933b654a25659eec0e7b02a26148660940b15d9c`

**Regenerated as a consequence.** The 30 category READMEs under
`src/econflow_engine/wrappers/*/README.md`, via `scripts/gen_wrappers.py`.
