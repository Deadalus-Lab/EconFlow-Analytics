<!-- SPDX-License-Identifier: AGPL-3.0-only -->

# `engine/fixtures/`

Product fixtures — read by the engine, by the conformance harness and by the TypeScript side. Not
test data owned by one suite. That is why they live here and not under `tests/`.

Three sets, with three different jobs.

| Directory | What it pins | Read by |
|---|---|---|
| `contract/` | the serialisation contract: a parquet file plus the sidecar that makes it reconstructible | the pointer codec, both directions |
| `series-io-ts/` | the same contract as the TypeScript side must see it | `frontend/packages/series-io` |
| `replications/` | real published-scenario input data | the paper-replication oracle |

Every fixture is a `.parquet` beside a `.json` describing what the parquet must reconstruct to. Each
directory carries a `manifest.json` listing its members; read the count from there rather than from
this file.

## `contract/` — and why several of these look broken

The sidecar is the contract. A parquet carries no time index and no class, so the pair
`{class, ts, matrix, start, end, frequency, columns}` is what turns a table back into the object it
came from. The codec **refuses** to reconstruct a parquet with no sidecar rather than silently
degrading a time series into a data frame — that refusal is why the file has to become
self-describing, and the fixtures are what prove the refusal is the only failure mode.

> **⚠ Several fixtures are deliberately hostile. Do not clean them up.**
>
> **The Greek ones are the UTF-8 evidence.** `df-label-greek` and `mts-quarterly-greek` carry column
> labels in Greek — `ΑΕΠ`, `πληθωρισμός`, `ανεργία` — and their TypeScript twin `quarterly-mts3-greek`
> carries the same. A non-ASCII column label is exactly the input a serialisation contract is most
> likely to mangle, and these are the only fixtures that would catch it.
>
> **Translating them to English would delete the only evidence the contract is UTF-8-safe, and every
> test would stay green while it happened.** That is the worst available outcome: a silent loss of
> coverage that looks like tidying. Treat these three names, and the `β` column where it appears, as
> protected content.
>
> **The non-finite ones are the JSON-boundary evidence.** `ts-monthly-nonfinite` carries `NaN`, `+Inf`,
> `-Inf`, `NA` and `-0` in one series — and `NA` must stay **distinct from** `NaN`, because they are
> different answers and no tolerance may blur them. `ts-monthly-extremes` does the same at the ends of
> the double range. JSON cannot encode any of these natively; the serialiser writes `null` for the
> non-finite cases to match the reference behaviour, and refusing to write them would be a behaviour
> change dressed up as safety.
>
> **The gap and irregular fixtures are the frequency evidence.** `ts-monthly-freq12-gaps`,
> `ts-annual-freq1-na`, `ts-quarterly-freq4-q3start` and `df-irregular-date-nofreq` cover the cases
> where frequency and start period are the things most likely to be lost.

## `series-io-ts/` — the same contract, the other reader

Eight fixtures the TypeScript side reads with its own parquet reader. They exist because a
serialisation contract with one implementation is not a contract, and a divergence between the two
readers is invisible from either side alone.

A round-trip check is the only thing that catches a **one-directional** divergence: it verifies not
merely that the engine can read the validation schema's sidecar, but that the engine would have written the
same sidecar itself. No such check exists yet on this side.

**Byte-determinism is a property these fixtures depend on.** Two separate processes must produce the
identical parquet for the same input, or the drift gates become flaky rather than strict. Any change
to what goes into the file — including embedding the sidecar as file-level metadata — has to be
re-measured against that, not assumed to preserve it.

## `replications/` — the absolute oracle

Ten parquet files carrying real DBnomics series for four published replication scenarios: a Taylor
rule, a money–income relationship, growth-at-risk, and a Johansen vector error correction model.
`manifest.json` records rows, columns, `value_sum`, `value_n_na` and sha256 per file; the value sum was
the checksum carried across from the pre-conversion originals, which does not exist in the tree.

These are the most under-used asset in the repository: **no test currently reads them.** They matter
because they support the one oracle the parity corpus cannot provide. Parity proves the two engines
agree about which calls are valid. A regression corpus proves this engine computes what the reference
engine computed. Only a published result proves either of them was *right* — which is exactly the
question for the estimators authored from papers, where the engine was authored from
the same paper and a shared misreading reproduces perfectly.

> **⚠ Ten files, six distinct payloads.** `growth-at-risk-figb` and `johansen-vecm-long` are
> byte-identical; so are `growth-at-risk-fitb` and `johansen-vecm-short`; and `growth-at-risk-ip`,
> `money-income-income` and `taylor-rule-ip` are all the same series. **The scenarios deliberately
> share input series.** A check that counts distinct payloads rather than files will disagree with the
> manifest, and it will look exactly like data corruption. Assert the sharing rather than discovering
> it.

Every field of `manifest.json` —
rows, columns, `value_sum`, `value_n_na` and sha256 — was recomputed from the ten parquet files and
found to match, 10 of 10. `manifest.json` is therefore the sole evidence the conversion was lossless,
which is why every field in it must stay recomputable from the parquet, and why the test that
recomputes them (todo `1.3.36`) is worth more than the manifest itself.
