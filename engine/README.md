<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# The compute engine

Every statistic and every validation gate in EconFlow Analytics lives here, and
nowhere else. The engine exposes **913 handlers** across **251 wrappers** in
**30 categories**, and it is the only component permitted to compute a number.

## Layout

| Path | What it is |
|---|---|
| `artifacts/` | **Frozen source.** The typed node contracts, the method cards, the parity corpus. Read, never regenerated — see `artifacts/PROVENANCE.md`. |
| `src/econflow_engine/kinds.py` | The heart: the 20 argument kinds, one explicit branch each. |
| `src/econflow_engine/generated/` | Machine-written from `artifacts/`, in three tiers. Never hand-edited. |
| `src/econflow_engine/wrappers/` | 251 modules, 913 handlers, one category package each. |
| `scripts/gen_*.py` | The generators. Each supports `--check`, and CI runs them that way. |
| `tests/parity/` | The 4 855-case argument-contract corpus. |
| `fixtures/` | Serialisation contract fixtures and replication datasets. |

## Getting started

```sh
uv sync --locked            # from the repository root; engine/ is a workspace member
uv run pytest               # the suite
uv run python scripts/gen_schemas.py --check
uv run python scripts/gen_wrappers.py --check
```

## The rules that are not negotiable

- **A gate is a raise, never a warning.** A method's documented requirement is
  checked and refused, not noted and continued.
- **The engine emits chart *data*, never a chart.** Rendering belongs to the
  browser.
- **No wrapper touches the network.** Enforced by an import-linter contract in
  the workspace root manifest, not by convention.
- **Generated files are never hand-edited.** `--check` fails the build if they
  drift from the artifact.
- **The five continuity constants** — 913 nodes, 30 categories, 252 cards,
  4 855 parity cases, 114 recommend fixtures — are asserted by
  `.github/inventory.json` on every pull request. They do not move.

## Where the numbers come from

`artifacts/` is a frozen input, not an output. The generators that once produced
it read spec sources that no longer exist, and `contract_hash` is a digest over
an object shape that cannot be reconstructed outside the original toolchain.

Each artifact carries a `.sha256` sidecar, and `assert-inventory` verifies all
six on every run — refusing to pass if it checked fewer than it found, so a glob
that matched nothing cannot report success. Any edit to an artifact is recorded
in `PROVENANCE.md` with its reason and its new digest; there is one such entry.
