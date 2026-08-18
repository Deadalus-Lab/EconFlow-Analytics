<!-- SPDX-License-Identifier: AGPL-3.0-only -->

## What and why

<!-- What changed, and the problem it solves. Not a restatement of the diff. -->

## Verification

Tick only what you actually ran. An unticked box is information; a wrongly
ticked one is a false claim, and this project's whole thesis is that claims are
backed by evidence.

- [ ] `./run_verifications.sh` exits 0
- [ ] The `--check` generators reproduce their output (or: no generator input changed)
- [ ] New behaviour has a test that **fails without the change**

## The non-negotiables

- [ ] No gate softened from a refusal into a warning, and none deleted
- [ ] No test weakened to make it pass — no added `skip`, no loosened assertion
- [ ] Nothing under `engine/artifacts/` hand-edited
- [ ] Nothing under `engine/src/econflow_engine/generated/` hand-edited — it is
      re-emitted by `scripts/gen_schemas.py`, and a hand edit turns
      `artifact-drift` red on the next run
- [ ] No network call added to a wrapper (the engine makes none: 0 of 251)
- [ ] No `eval`, `exec` or `pickle` on anything a user supplied
- [ ] No chart rendered in the engine — it emits chart data, the browser draws
- [ ] Pinned lockfile and linear-algebra thread settings untouched
- [ ] No statistical dependency added to `backend/` — the `engine-boundary` gate
      enforces this, and it is the replacement for the file extension that used
      to enforce it for free

## For a new or changed wrapper

- [ ] Arguments and defaults taken only from the package documentation
- [ ] Every documented requirement is an explicit gate that refuses to compute
- [ ] Returns a structured result — no printing, no plotting
- [ ] Examples live in the docstring, not at module scope
- [ ] Implementation-note footer: functions used, what was omitted, gates added
- [ ] Stochastic methods take a mandatory seed
- [ ] The package's licence is compatible with AGPL-3.0-only — in particular
      it is **not** GPL-2.0-only

## Sign-off

- [ ] Every commit is signed off (`git commit -s`) — the `dco` check enforces this
