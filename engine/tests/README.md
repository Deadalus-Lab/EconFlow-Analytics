<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `engine/tests/`

Two harnesses exist, and they answer two different questions. Confusing them is how "the port is
correct" gets claimed on evidence that cannot support it.

| Harness | Question it answers | State |
|---|---|---|
| `parity/` | do this engine and the reference engine agree about **which calls are valid**? | green |
| `conformance/` | does this engine compute **the same numbers**? | skipped — the corpus does not exist |

**Parity says nothing about the numbers.** A wrapper can accept exactly the right inputs, reject
exactly the right ones, carry exactly the right reason codes — and compute something else entirely.
That sentence belongs beside every green parity run, and it is in the module docstring for the same
reason.

## `parity/` — the argument contract

`artifacts/parity-fixtures.v1.json` holds frozen accept/reject verdicts produced by the reference
engine's own argument adapter. None of it is hand-written and nothing here may edit it. The harness
replays every case and asserts three properties:

**P1 — soundness.** `python.accept ⟹ reference.accept`, with no exceptions and no allowlist. This is
the property that makes it safe to run the same validation in the editor, in the worker and over model
output. A P1 violation is a call the canvas cheerfully accepts and the engine then refuses — the most
expensive failure the product can produce, because it lands after the user has committed to a graph.

**P2 — completeness.** A rejection inside the modelled class is a rejection here, with the **same**
reason code. Agreeing that a call is invalid while disagreeing about why is worse than not checking,
because the reason is what the user is shown.

**P3 — enumerated divergence, as set equality.** Cases where this engine is deliberately stricter are
declared in `artifacts/intentional-divergences.json`. Set equality, not containment, is the point: a
**new** divergence and a **dead** entry must both turn the suite red, or the register decays into a
list of claims nobody checks.

### Three findings that look like bugs and are not

**Three formula codes and every path code collapse to `other`.** Measured over the corpus:
`formula-bad-head`, `formula-parse`, `formula-depth` and `enum-invalid` appear **zero** times, and
every `kind: "path"` rejection carries `other`. The reference exporter classifies those messages that
way, so the precise diagnosis lives in `GateError.detail_code` and `other` goes on the wire. Emitting
the precise code looks like an improvement and **breaks P2**.

**Strict validation mode is load-bearing, not a style choice.** In lax mode a string `"42"` coerces to
`42` and `1` coerces to `True`. The reference engine accepts those too, so P1 stays green and nothing
looks broken — but the declared divergence classes go dead and **P3 fails**. A P3 failure is the only
signal that strictness was lost.

**The explicit-null guard must sit outside the optional union.** With the guard inside, an explicit
JSON `null` slips through the `None` branch unvalidated, which is a P1 violation. An *absent* key and
an *explicitly null* key are different inputs and the reference engine treats them differently.

### The register is load-bearing, which makes editing it the cheapest way to hide a bug

P3 gives `intentional-divergences.json` real force, and that cuts both ways: adding a row is the
quickest route to a green suite. A row needs a reason, a rationale citing the reference line, a date
and a members list — and the members list is a **sample of a class, not its definition**.

## `conformance/` — the numbers

Skipped by default, and that is the honest state. It reads `artifacts/golden-corpus.v1.json`, which
does not exist. The harness was written ahead of the corpus deliberately, so that the first implemented
wrapper body meets a test that already disagrees with it rather than one written to agree.

**The skip condition must remain "the corpus file is absent" and nothing else.** A harness that can
skip for any other reason is a harness that can go quietly inert, and the first honest state after a
corpus lands is a large red run — that red *is* the porting backlog, measured.

**Tolerance is per case and has no default.** A closed-form test statistic should match to machine
precision; an optimiser-driven estimate should not be held to the same bar. One global tolerance is
either too tight for the estimators or too loose to catch a wrong formula. A case carrying no
tolerance is an error, never a fallback — and widening a tolerance to pass a case is the cheapest way
to turn a real numerical disagreement green.

**Some nodes cannot be compared by value at any tolerance.** Those whose method is stochastic and
unseeded are enumerated in the node-spec vocabulary and flagged per node under `cacheability`. The set
is derived from the artifact, never from a list in a test file — a hand-kept list produces either
permanent false failures or a tolerance so loose it proves nothing.

## Running it

```sh
cd engine
./run_verifications.sh          # generators, lint, types, import contracts, suite, anti-vacuity
uv run pytest -q                # the suite alone
```

`run_verifications.sh` exports the thread pins before it runs anything. **A bare `pytest` does not**,
so a developer running the suite directly is in a different numerical environment from CI without
being told. `OPENBLAS_NUM_THREADS`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS` and `NUMEXPR_NUM_THREADS` all
need to be `1`, plus `PYTHONHASHSEED=0`.

## Anti-vacuity

The script asserts the collected test count against a floor in `.github/inventory.json`. This is not
ceremony. A pytest run that collected nothing exits 5, and a careless `|| true` turns that into a
green build — a suite that examined zero tests must never read as a suite that passed.

The floor is a floor, deliberately: it rises as the per-wrapper suites land and it may never be
lowered. Every other constant in that manifest is exact equality, so adding a test file without
bumping its count is a red gate **by design**.

## The fixtures are elsewhere

`engine/fixtures/` holds the serialisation contract fixtures and the replication datasets, and it has
its own README explaining which of them are deliberate hostile cases that must never be "cleaned up".
There is no `engine/tests/fixtures/` directory: the pre-conversion originals of the replication
datasets were verified against `engine/fixtures/replications/manifest.json`.
