<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 17-forecast-combination

4 METHOD-SELECTION cards, 4 modules, 4 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #85 — Ensemble forecast combination (equal / in-sample / CV weights)

**Module:** `ensemble_forecast_combination.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_hybrid` | `y` | `series_handle`, `string`, `enum`, `enum`, `integer`, `enum`, `integer`, `integer`, `integer` | `models='aefnst'`, `windowSize=84`, `seed=42` | `light` | — |

### Use when

a robust combination of 2-7 univariate models (a/e/f/n/s/t/z) on ONE series; a baseline macro forecast where stability matters

### Do not use when

multivariate/structural analysis (VAR/VECM), causal Granger, a need for statistically exact PI, or a single dominant model; length(y)<4

### Alternatives

| instead use | when |
| --- | --- |
| A single model (auto.arima/ets/fable, sections 03/16) | one model clearly dominates or you want interpretable parameters/diagnostics |
| VAR/VECM (sections 04/05) | there are cross-series dependencies/cointegration that the univariate combination ignores |
| Bayesian model averaging (section 14) | you want a posterior-weighted combination with full uncertainty quantification |

### Output fields

- included_models: which components ACTUALLY took part after the automatic removals
- dropped_models: requested but NOT included (length removal or a drop by hybridModel) — always check it
- weights_method / weights: the method + per-model weights (summing to ~1)
- point_forecast: ts -> {values,start,frequency}, the central forecast
- lower / upper: matrix h x length(level) -> nested rows+dim+dimnames, the PI bounds
- pi_combination: 'extreme' (the more extreme bounds) or 'mean'
- pi_disclaimer: an explicit statement that the PI are over-conservative

### Pitfalls

- the PI are OVER-CONSERVATIVE: lower/upper are heuristic, with no guaranteed nominal coverage — not strict statistical bounds
- silent degradation: hybridModel removes components on its own (stlm/nnetar if length<2*frequency, ets if the seasonal period>24) — read dropped_models/included_models
- nnetar (n) is stochastic (random initial weights): the wrapper enforces a local seed (default 42L); changing the seed changes the forecasts
- insample.errors is not recommended : it overfits the weights; equal is more robust, cv.errors is better but slow and data-hungry
- the weights reflect low error, NOT the structural correctness of the component (a purely predictive criterion)

### References

- vignette forecastHybrid (
- Bates & Granger 1969 The Combination of Forecasts
- Timmermann 2006 Forecast Combinations (Handbook of Economic Forecasting)
- Hyndman & Athanasopoulos, Forecasting: Principles and Practice

## #207 — Online probabilistic forecast combination via CRPS-Learning (BOA/BEWA/ML-Poly/EWA aggregation of quantile expert forecasts)

**Module:** `online_probabilistic_forecast.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `profoc_online` | `y`, `experts`, `tau` | `matrix_handle`, `raw_handle`, `num_array`, `enum`, `enum`, `number`, `boolean`, `integer`, `number`, `number`, `number`, `number`, `number`, `boolean`, `integer` | `loss_parameter=1`, `loss_gradient=True`, `lead_time=0`, `forget_regret=0`, `fixed_share=0`, `gamma=1`, `soft_threshold=None`, `hard_threshold=None`, `allow_quantile_crossing=False`, `seed=2025` | `light` | — |

### Use when

you have >=2 experts producing PROBABILISTIC (quantile) forecasts at the SAME tau levels and you want to combine them ADAPTIVELY online (the weights are learned sequentially from the past loss), optimally under CRPS; experts = a 3D array [T x quantiles(P) x experts(K)], y = a Tx1 realized series; appropriate when the relative performance of the experts changes over time (regime shifts) and you want per-quantile weights + the out-of-sample loss against each expert

### Do not use when

point-only forecasts (not quantiles) -> #85 run_hybrid (forecastHybrid); hierarchical/temporal RECONCILIATION rather than combination -> foreco_reconcile / fable_reconcile; a single expert (K<2; there is nothing to combine); you want batch/offline optimal fixed weights (not online adaptivity; outside the curated surface); you simply want to EVALUATE a density forecast, not combine -> #74 sr_crps_sample (scoringRules)

### Prerequisites

- c02_univariate_forecasting/fable.run_fable_arima (it produces the quantile forecasts of one expert; repeat per model -> stack into a [T x P x K] array)
- c02_univariate_forecasting/fable.run_fable_ets (a second expert for the array; >=2 are needed)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the realized y values)

### Alternatives

| instead use | when |
| --- | --- |
| #85 run_hybrid (forecastHybrid) | point-forecast combination (not probabilistic/quantile) over a single ts |
| FoReco/foreco_reconcile | hierarchical/temporal RECONCILIATION (coherence within a hierarchy) rather than learning weights from a loss |
| 17-forecast-combination/fable_reconcile | reconciliation inside the fable ecosystem (mint/wls/ols) |
| 15-model-evaluation/sr_crps_sample | you want ONLY the evaluation of a density/quantile forecast (CRPS/LogS/PIT), not a combination |

### Output fields

- predictions: a T x P matrix (the combined probabilistic forecast per time × quantile level; chart-data; sorted if allow_quantile_crossing=FALSE)
- final_weights: a P x K matrix (the adaptive weights at the last instant T+1; the weights with which the experts will be combined in the NEXT forecast; they sum to ~1 per quantile for method boa/bewa/ewa)
- mean_weights: a P x K matrix (the average weight over time per expert × quantile — which expert dominated overall)
- forecaster_loss_total / forecaster_loss_mean / forecaster_loss_per_quantile: the cumulative & mean CRPS-learning loss of the COMBINATION (per quantile, of length P)
- expert_loss_total: a length-K cumulative loss for EACH single expert (the baseline); best_expert = the best single one
- beats_best_expert: TRUE if forecaster_loss_total <= min(expert_loss_total) — the combination beats the best single expert out of sample (the reason online learning exists)

### Pitfalls

- dims: experts MUST be [T x P x K] with dim1==length(y), dim2==length(tau); the wrong axis order (e.g. [T x K x P]) passes silently and gives a WRONG result -> a hard gate checks dim2==length(tau); double-check that the 2nd dimension is quantiles (in the same order as tau)
- tau must be STRICTLY increasing & must match exactly the quantile levels at which the expert forecasts were computed; a mismatch -> an invalid loss (the gate blocks values outside (0,1)/unsorted values but NOT a semantic mismatch of levels — that is the caller's responsibility)
- method: 'bewa' (default) = the BOA regret + an EWA weight update; 'boa' = the full BOA (second order); 'ewa' = plain exponential weighting; 'ml_poly'; different adaptivity — 'ewa'/'ml_poly' may not give simplex weights with thresholds
- beats_best_expert=FALSE is NOT a failure: with a small T or one dominant expert the online learning needs time to converge; look at mean_weights (is it learning the right expert?) before rejecting it
- allow_quantile_crossing=FALSE (default) sorts the predictions per t (monotone quantiles); TRUE allows crossing (an invalid CDF) — leave it FALSE for interpretable quantiles
- smoothing (a B-spline/P-spline across quantiles) is NOT exposed (the defaults mean no smoothing); for smooth per-quantile weights you need a custom fit outside the node
- predict/update (incremental on new data) are NOT exposed: a stateless node -> every call is a complete re-fit over the supplied window

### References

- Berrisch, J. & Ziel, F. (2023) CRPS Learning, Journal of Econometrics 237(2):105221 <doi:10.1016/j.jeconom.2021.11.008>
- Gaillard, P. & Goude, Y. (2015) Forecasting electricity consumption by aggregating experts (BOA/ML-Poly online aggregation)
- Wintenberger, O. (2017) Optimal learning with Bernstein Online Aggregation, Machine Learning 106:119

## #208 — Coherent forecast reconciliation (cross-sectional / temporal / cross-temporal) via an optimal least-squares projection (MinT: ols/str/wls/shr/sam)

**Module:** `coherent_forecast_reconciliation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `foreco_reconcile` | `type`, `base` | `enum`, `matrix_handle`, `matrix_handle`, `int_array`, `string`, `enum`, `enum`, `matrix_handle`, `enum` | `comb='ols'` | `light` | — |

### Use when

you have INCOHERENT base forecasts of a linearly constrained (hierarchical/grouped) multiple series — e.g. GDP = the sum of sectors, national = the sum of regions, or annual = the sum of quarters — and you want to make them COHERENT (the aggregates equal the sum of the components exactly) while ALSO improving accuracy through MinT (Wickramasuriya 2019). type: 'cs' a cross-sectional hierarchy, 'te' temporal (one series, several frequencies), 'ct' cross-temporal (both at once)

### Do not use when

a single series with no hierarchical/temporal constraint structure (there is nothing to reconcile); you want to COMBINE alternative forecasts of the SAME series (an ensemble/model averaging -> #85 run_hybrid or a fabletools combination); you do not have base forecasts for ALL the levels of the hierarchy; you want probabilistic/bootstrap reconciled paths (csboot/ctboot — outside the curated surface)

### Prerequisites

- c02_univariate_forecasting/fable.run_fable_arima (it produces the base forecasts PER series/level; stack them into a base matrix/vector)
- c02_univariate_forecasting/forecast.run_ets (an alternative producer of base forecasts + residuals for the MinT comb)
- foreco_reconcile (an ols baseline first; then MinT shr/wls with res for accuracy)

### Alternatives

| instead use | when |
| --- | --- |
| foreco_reconcile comb='shr' | MinT shrinkage (Wickramasuriya 2019) — the normal default for accuracy when you have in-sample residuals; ols/str ignore the error covariance |
| foreco_reconcile type='ct' | you want simultaneous cross-sectional AND temporal coherence (e.g. quarterly regional series summing to an annual national total) |
| #85 run_hybrid (forecastHybrid) | you want a COMBINATION of several models for ONE series (an ensemble), not the reconciliation of a hierarchy |
| nn='sntz'/'osqp' | the reconciled forecasts must be non-negative (e.g. counts, positive magnitudes) |

### Output fields

- reconciled: the coherent forecasts — cs, an (h x n) matrix; te, a vector of length h*(k*+m) with labels; ct, an (n x h*(k*+m)) matrix (chart-data)
- type/comb/approach/nn: the reconciliation that was performed
- cs: n/n_upper/n_bottom/h + coherence_err (max\|upper - agg_mat·bottom\| ~0 => coherent, a post-check)
- te/ct: agg_order/m/kt/h + tew; ct: n/n_upper/n_bottom
- object: the foreco object (fitted)

### Pitfalls

- the ORDER OF THE base COLUMNS/ROWS: cs columns = [upper.., bottom..] (the n_a upper series FIRST, then the n_b bottom ones) consistent with agg_mat; the wrong order => a silently wrong reconciliation (the wrapper checks ONLY the dimension n, not the semantic mapping)
- comb DIFFERS by type: 'wlsv' is valid only for te/ct (NOT cs); 'oasd' only for cs; the wrapper blocks an invalid comb for a given type
- MinT (shr/wls/sam/acov..) REQUIRES res (the in-sample residuals); without res -> a gate stop; ols/str/csstr/testr do NOT need res
- temporal base ordering: LOW->HIGH frequency (the most aggregated first, e.g. annual, then semi-annual, then quarterly); the wrong order => a wrong result
- a scalar agg_order m => ALL the divisors of m are used (k*+m = the sum of the divisors; m=4 -> 7, m=12 -> 28); length(base) must be a multiple of that
- reconciliation is NOT an ensemble: it combines forecasts of DIFFERENT series/frequencies within one hierarchy so that they add up; it does NOT average models of the same series

### References

- Wickramasuriya, S.L., Athanasopoulos, G. & Hyndman, R.J. (2019), Optimal forecast reconciliation through trace minimization (MinT), JASA 114(526):804-819. doi:10.1080/01621459.2018.1448825
- Hyndman, R.J., Ahmed, R.A., Athanasopoulos, G. & Shang, H.L. (2011), Optimal combination forecasts for hierarchical time series, CSDA 55(9):2579-2589. doi:10.1016/j.csda.2011.03.006
- Athanasopoulos, G., Hyndman, R.J., Kourentzes, N. & Petropoulos, F. (2017), Forecasting with temporal hierarchies, EJOR 262(1):60-74. doi:10.1016/j.ejor.2017.02.046
- Di Fonzo, T. & Girolimetto, D. (2023), Cross-temporal forecast reconciliation: Optimal combination method and heuristic alternatives, Int. J. Forecasting 39(1):39-57. doi:10.1016/j.ijforecast.2021.08.004
- Panagiotelis, A., Athanasopoulos, G., Gamakumara, P. & Hyndman, R.J. (2021), Forecast reconciliation: A geometric view, Int. J. Forecasting 37(1):343-359. doi:10.1016/j.ijforecast.2020.06.004

## #209 — Tidy hierarchical/grouped forecast reconciliation (aggregate_key + MinT/bottom_up) in the fable framework

**Module:** `tidy_hierarchical_grouped.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fable_reconcile` | `data`, `index`, `keys`, `value` | `df_handle`, `string`, `series_codes`, `string`, `enum`, `enum`, `enum`, `integer` | `h=8` | `light` | — |

### Use when

you have a long panel (an index + >=1 key/grouping columns + a numeric value) that aggregates naturally into a hierarchy (e.g. region/sector -> national, or CPI sub-indices -> the headline) and you want COHERENT forecasts — the leaves must sum EXACTLY to the aggregates; one base model (ARIMA/ETS/SNAIVE) is fitted per node and reconciled with MinT (min_trace) or bottom_up

### Do not use when

a single univariate series with no hierarchy (-> #85 forecastHybrid or a standalone fable/ARIMA); you want an online/adaptive combination of experts (-> profoc); purely cross-temporal (temporal aggregation) reconciliation of numeric matrices without a tsibble (-> FoReco csrec/terec/ctrec); a value with NA/an irregular (gapped) index; structural/causal analysis (VAR/VECM)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the long-format panel CSV)
- fable_reconcile (run it with method='bottom_up' as a coherence baseline before comparing with MinT)
- c02_univariate_forecasting/fable.run_fable_arima (checking the base model on a single node before the hierarchy)

### Alternatives

| instead use | when |
| --- | --- |
| 17-forecast-combination/csrec | you want cross-sectional/temporal/cross-temporal reconciliation of READY base forecasts (numeric matrices), not a tidy tsibble->mable round trip |
| 17-forecast-combination/run_hybrid | ONE series without a hierarchy — you want an ensemble of several models rather than a coherent hierarchy |
| 02-univariate-forecasting/fable-run_fable_arima | a single node / no need for coherence — a plain ARIMA/ETS fit + forecast |
| 14-bayesian toolkit (BMA) | you want a posterior-weighted combination with full uncertainty quantification rather than a MinT projection |

### Output fields

- reconciled: data_frame records (the key columns + index + point + lower_L/upper_L per level) — the COHERENT forecast (chart-data); aggregated nodes are labelled '<aggregated>'
- base: the corresponding records of the UNRECONCILED base forecasts (to compare the effect of the reconciliation)
- hierarchy: a data_frame of the hierarchy nodes (each row = a key combination; '<aggregated>' = an aggregated level); n_series (leaves+aggregates); n_leaf
- method / reconciliation: the selected method (min_trace(<method>) or bottom_up); structure (nested/grouped); base_model
- object: the reconciled mable (fabletools) — stubbed by to_mcp (there is no downstream consumer in the category)

### Pitfalls

- coherence != accuracy: reconciliation GUARANTEES that the leaves sum to the aggregates, NOT that every node becomes more accurate — MinT (min_trace) typically improves matters, but bottom_up can worsen the top level if the leaves are noisy
- choosing the MinT method: 'wls_struct' (default) = structural scaling, always robust; 'mint_shrink' (Wickramasuriya 2019) = shrinkage towards a diagonal, theoretically optimal but it NEEDS enough residuals — with short/few series it can be unstable; 'ols' ignores scale
- '<aggregated>' in the key fields = an aggregated level (is_aggregated), NOT a category literally named '<aggregated>' — do not read it as a leaf
- nested (grp1/grp2) vs grouped (grp1*grp2): nested => a genuine hierarchy (a region within a state); grouped => crossed without natural nesting (e.g. purpose x state) — the wrong choice changes which nodes exist
- the PI come from the reconciled predictive distribution (hilo) — valid intervals per node, but the joint coherence concerns the points (the means), it does not guarantee joint coverage of the intervals
- the value must aggregate meaningfully (a flow/stock): the coherence constraint is the sum of the leaves = the aggregate; ratios/percentages/index levels do NOT add up -> do not use them as the value

### References

- the fabletools reference manual — aggregate_key, reconcile, min_trace, bottom_up, hilo help pages (Mitchell O'Hara-Wild, Rob Hyndman)
- Wickramasuriya, Athanasopoulos & Hyndman (2019) Optimal forecast reconciliation for hierarchical and grouped time series through trace minimization, JASA 114(526):804
- Hyndman & Athanasopoulos, Forecasting: Principles and Practice (3rd ed.), ch. 11 Forecasting hierarchical and grouped series (https://otexts.com/fpp3/hierarchical.html)
- Hyndman, Ahmed, Athanasopoulos & Shang (2011) Optimal combination forecasts for hierarchical time series, CSDA 55:2579
