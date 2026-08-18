<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `engine/scripts/`

Three generators live here. They read the frozen artifacts and emit code and documents that are
committed, and CI runs each in `--check` mode and fails on any difference.

**Nothing here produces an artifact.** The exporters that made them ran under a reference
implementation that is no longer in this tree, and they were removed with it. That direction is
one-way now: the artifacts are input, the code is output, and no script in this directory can
regenerate the contract it reads. `../artifacts/PROVENANCE.md` is the record of where they came
from and of the one edit ever made to one of them.

## The generators

Every one supports `--check`, which compares byte for byte and never writes. That is the contract CI
depends on; a generator that writes during a check is a generator that makes its own gate pass.

| Script | Reads | Emits |
|---|---|---|
| `gen_schemas.py` | `artifacts/node-specs.v1.json` | `src/econflow_engine/generated/**` in three tiers |
| `gen_wrappers.py` | `artifacts/node-specs.v1.json`, `artifacts/method-cards.v1.json` | the wrapper stub modules and the per-category guides |
| `gen_third_party.py` | `../uv.lock` | `THIRD-PARTY-LICENSES.md` and `sbom.cdx.json` |

```sh
uv run python scripts/gen_schemas.py --check
uv run python scripts/gen_wrappers.py --check
uv run python scripts/gen_third_party.py --check
```

`gen_wrappers.py --check` does more than compare files: it asserts that every emitted stub signature
still matches the node spec. A hand-edited wrapper whose parameter no longer matches the wire contract
is exactly the failure the `DO NOT EDIT` banner cannot prevent on its own.

### Three things that have already gone wrong here

**A comment change in a generator shifts every file it emits.** That property is intrinsic;
it moved from the spec sources to these scripts. It is the reason **no auto-formatter may run over
this tree** — see `.pre-commit-config.yaml`. A formatter pass over a generator is a diff in dozens of
emitted files that nobody asked for and nobody can review.

**`--check` must ignore `__pycache__`.** Importing the generated package leaves bytecode behind, so
the first clean-slate run reported `__pycache__/manifest.cpython-312.pyc` as drift and `--check`
failed on any machine that had ever run the tests. The exclusion is load-bearing.

**Both `--check` modes were proven non-tautological by mutation, once.** Changing a `card_id` in the
emitted manifest produced *content differs*; changing a parameter's annotation in a stub produced
*signature drift*, naming the node. A check that has only been observed passing has not been observed
working — repeat the mutation whenever the emitter changes.

## Where the artifacts came from

Nothing in this directory produced them. They were emitted by a set of exporters under the reference
implementation, which is no longer in the tree — the exporters went with it, and no copy of that
toolchain is restorable from this repository alone.

That has one consequence worth stating plainly, because it inverts the usual assumption: **a drift
failure here can never be resolved by regenerating the input.** If `gen_schemas.py --check` fails,
the code moved. The artifact did not, and cannot.

`../artifacts/PROVENANCE.md` records which exporter produced which artifact, where the reference tree
survives, and the one edit ever made to a sealed file.

### The oracle that was never captured

One thing the artifacts do **not** contain is what the reference engine *returned*. The parity corpus
proves the two engines agree about which calls are **valid**; it says nothing about the numbers.

Capturing that would have required the reference toolchain restored and its library rebuilt, and it
was never done. The port does not wait on it: the authored tier is graded against published results,
which is a stronger instrument anyway, because the reference body was itself written from the paper —
a shared misreading would reproduce green against it and red against the paper.

## The environment rule

Everything here runs through the workspace:

```sh
uv sync --locked        # from the repository root
uv run python scripts/<script>.py
```

**`--locked` is not optional and the repair is never to re-lock.** `uv sync --locked` refuses to
re-resolve and fails when the lockfile does not already satisfy the manifests. When it fails, the fix
is to re-sync, or to change a manifest and re-lock *deliberately* as a reviewed diff. Running
`uv lock` to clear the error redefines the pinned dependency set to whatever this host happened to
want — which is the silent-drift failure the lockfile exists to prevent, wearing a clean exit code.

An earlier design hit precisely that failure once: the interpreter resolved five packages from a system
library the lockfile did not describe, so every recorded figure demonstrated that the tests *passed*
rather than that they produced the *pinned numbers*.
