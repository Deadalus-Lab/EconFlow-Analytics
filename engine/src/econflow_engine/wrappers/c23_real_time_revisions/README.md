<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 23-real-time-revisions

1 METHOD-SELECTION card, 1 module, 5 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #229 — Real-time data-revision analysis (vintages: a triangle, revision statistics, news-vs-noise/efficiency tests, a state-space nowcast)

**Module:** `real_time_revision.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `build_revision_triangle` | `df` | `df_handle` | — | `light` | — |
| `compute_revisions` | `df` | `df_handle`, `enum`, `integer`, `string`, `string` | `interval=1` | `light` | — |
| `analyze_revisions` | `df` | `df_handle`, `integer`, `string`, `integer` | `n_releases=3`, `degree=5` | `light` | — |
| `first_efficient_release` | `df` | `df_handle`, `integer`, `string`, `number`, `boolean`, `boolean` | `n_releases=5`, `significance=0.05`, `robust=True`, `test_all=False` | `light` | — |
| `nowcast_revisions` | `df`, `e` | `df_handle`, `integer`, `integer`, `enum`, `integer`, `integer` | `n_releases=6`, `h=0`, `seed=1` | `light` | — |

### Use when

successive releases/vintages of the SAME macro series (real-time data) -> a revision triangle, revision summary statistics, news-vs-noise/bias/efficiency tests, or a state-space efficient final-estimate nowcast

### Do not use when

a single release (no vintage dimension); business-cycle dating (#88); plain forecast evaluation without vintages (#74-77); data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| build_revision_triangle | you want a simple overview/heatmap of the revision table (wide: reference periods x publication dates) |
| compute_revisions (mode=interval/nth_release/ref_date) | you want the VALUES of the revisions relative to one reference; nth_release='latest' => the total revision (to the final release) |
| analyze_revisions (get_revision_analysis, degree 1.5) | you want statistics + tests: bias/MAR/noise-to-signal/correlation/Theil and news-vs-noise (Mankiw-Shapiro) |
| first_efficient_release (Mincer-Zarnowitz, Aruoba 2008) | you want to find the first release that is unbiased & efficient (b0=0 & b1=1, HAC) |
| nowcast_revisions (method=jvn/kk) | you want a state-space 'efficient' estimate of the final value (Jacobs-van Norden news/noise or Kishor-Koenig) |

### Output fields

- triangle: a matrix (reference periods x vintages) + n_obs_per_period (the number of non-NA values per period)
- revisions: a data_frame {pub_date,time,revision} + a summary (mean/sd/MAR/min/max, n_revisions non-NA, n_missing)
- compute_revisions.sign_convention: a mode-dependent string that travels WITH the numbers — 'revision = final - release' (nth_release='latest') vs 'revision = reference - vintage (older - newer)' (interval/a small nth_release/ref_date); the OPPOSITE polarity from analyze_revisions.sign_convention ('final - initial')
- revision_summary: a data_frame with one row per release (Bias(mean), MAR, noise/signal, Correlation, Theil's U, the news/noise test coefficient + p)
- first_efficient_release: e (0-indexed; NA if none) + a tests data_frame {release,F_stat,p_value,efficient}
- nowcast: states/params data.frames + loglik/aic/bic/convergence/converged + the raw fit (to_mcp -> a stub)

### Pitfalls

- TWO different sign conventions: compute_revisions revision = REFERENCE - VINTAGE (nth_release='latest' => final - initial; interval/a small nth_release => NEGATIVE values for an upward-trending series); analyze_revisions revision = final - initial
- news/noise polarity: the News test = a regression of the revision on the INITIAL value; the Noise test = a regression on the FINAL value (the coefficient point estimates coincide with a plain lm; HAC changes ONLY the SE/p-value)
- the get_revision_analysis columns depend on the degree (1=magnitude/bias, 2=correlation, 3=news/noise, 4=Theil/sign, 5=all 38)
- first_efficient_release: e is 0-indexed (0=the first release is already efficient); NA+a warning if there is none -> a valid result, not an error
- nowcast: e MUST be >0 AND e<n_releases; the MLE is deterministic (identical when seeded); a small sample -> boundary/degenerate parameters
- the node handles ONE series: several 'id' values are blocked (a gate); NA revisions do NOT inflate n (n_revisions counts only the non-NA ones)
- diagnose WAS OMITTED (a console-printing helper); the same statistics are exposed machine-readably by analyze_revisions

### References

- reviser v0.1.1 ref manual (the vintages_wide/get_revisions/get_revision_analysis/get_first_efficient_release/jvn_nowcast/kk_nowcast help pages)
- Mankiw-Shapiro 1986 'News or Noise? An Analysis of GNP Revisions' Survey of Current Business (news vs noise)
- Aruoba 2008 'Data Revisions Are Not Well Behaved' Journal of Money, Credit and Banking 40(2-3) 319-340 (the efficient release / Mincer-Zarnowitz test)
- Jacobs & van Norden 2011 'Modeling data revisions: Measurement error and dynamics of true values' Journal of Econometrics 161(1) 101-109 (the jvn nowcast)
- Kishor & Koenig 2012 'VAR Estimation and Forecasting When Data Are Subject to Revision' Journal of Business & Economic Statistics 30(2) 181-190 (the kk nowcast)
- wrapper footer IMPLEMENTATION NOTE (c23_real_time_revisions/real_time_revision)
