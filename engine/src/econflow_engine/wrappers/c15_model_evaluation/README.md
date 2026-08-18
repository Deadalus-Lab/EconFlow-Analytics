<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 15-model-evaluation

5 METHOD-SELECTION cards, 5 modules, 15 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #74 — Diebold-Mariano test + tsCV rolling backtest

**Module:** `diebold_mariano_tscv.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `eval_dm_test` | `e1`, `e2` | `series_handle`, `series_handle`, `enum`, `integer`, `number`, `enum` | `h=1`, `power=2` | `light` | — |
| `eval_tsCV` | `y`, `forecastfunction` | `series_handle`, `forecastfn_enum`, `integer`, `integer`, `integer` | `h=1`, `initial=0` | `light` | — |

### Use when

comparing the forecast accuracy of TWO methods (DM) or an honest out-of-sample backtest of one model per horizon (tsCV)

### Do not use when

>2 models together (→ MCS); assumption diagnostics for one model (→ lmtest/FinTS); an in-sample/nested comparison

### Alternatives

| instead use | when |
| --- | --- |
| #75 MCS | when you compare >2 models (it avoids the multiple-testing bias of the pairwise DM) |
| 02/accuracy | loss-based ranking without a statistical significance test |

### Output fields

- statistic: the DM stat (~t); the sign/direction depends on the order of e1,e2
- p_value: < a rejects equal accuracy
- parameter: (horizon, power)
- errors: ts(h=1)/mts(h>1) of errors with leading NAs
- accuracy: data_frame per-horizon rmse/mae/me/n_eff over the finite values

### Pitfalls

- alternative=less => method 2 is less accurate than 1 (e1 is better); greater => the reverse; the sign depends on the order of e1,e2
- me != 0 => a bias in the forecast
- n_eff falls at large h => a less reliable RMSE
- DM is not for in-sample/nested comparison (Diebold 2015)

### References

- Diebold & Mariano 1995 (JBES)
- Harvey, Leybourne & Newbold 1997 (IJF small-sample DM)
- Diebold 2015 (careful use of DM)
- Hyndman & Athanasopoulos FPP3 (tsCV)
- forecast reference manual (dm_test, tsCV)

## #75 — Model Confidence Set (Hansen-Lunde-Nason)

**Module:** `confidence_set.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_mcs_procedure` | `Loss` | `matrix_handle`, `number`, `integer`, `enum`, `integer`, `integer`, `integer` | `alpha=0.15`, `B=1000`, `min_k=3` | `heavy` | — |
| `compute_loss_level` | `realized`, `evaluated` | `series_handle`, `matrix_handle`, `enum` | — | `light` | — |
| `compute_loss_vol` | `realized`, `evaluated` | `series_handle`, `matrix_handle`, `enum` | — | `light` | — |

### Use when

many (>=2) models together -> the subset statistically indistinguishable from the best at (1-alpha), via a block bootstrap of the loss matrix

### Do not use when

exactly 2 models (→ dm_test, simpler, no bootstrap); it does not say which one is 'the best'

### Alternatives

| instead use | when |
| --- | --- |
| #74 dm_test | for exactly 2 models, a pairwise test |
| SPA test (Hansen 2005) | many models against ONE benchmark (not covered here) |

### Output fields

- show: data_frame of the surviving models only (model, Avg.Loss, ranks, MCS p-Value)
- included: the names of the models in the final confidence set
- statistic: Tmax or TR; ssm: raw S4 (a stub in to_mcp)

### Pitfalls

- show contains ONLY the surviving models, not the eliminated ones
- the MCS p-Value is NOT the p-value of an individual model; a model is in the set if its MCS p-Value > alpha
- a different seed/B => a slightly different set (bootstrap variability) - supply a seed
- Tmax vs TR can give different sets
- LossLevel/LossVol are non-conformable for a multi-column evaluated argument => the wrapper calls them per column + cbind

### References

- Hansen, Lunde & Nason 2011 (Econometrica 79(2):453-497)
- Bernardi & Catania 2014 (MCS package for the reference)
- Patton 2011 (robust volatility loss, QLIKE)
- MCS reference manual (MCSprocedure, LossLevel, LossVol)

## #76 — Breusch-Godfrey / Breusch-Pagan / Ramsey RESET

**Module:** `breusch_godfrey_breusch.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_bg_test` | `formula` | `formula`, `integer`, `enum`, `df_handle` | `order=1` | `light` | — |
| `run_bp_test` | `formula` | `formula`, `boolean`, `df_handle` | `studentize=True` | `light` | — |
| `run_reset_test` | `formula` | `formula`, `integer`, `enum`, `df_handle` | — | `light` | — |

### Use when

residual diagnostics for a regression (lm/glm): serial correlation (BG), heteroskedasticity (BP), wrong functional form (RESET)

### Do not use when

ARCH in a time series (→ FinTS); unit root/stationarity (→ 01); models other than lm/glm (→ vars serial-corr)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test

### Alternatives

| instead use | when |
| --- | --- |
| White test | more general heteroskedasticity (approximated by BP + varformula) |
| Ljung-Box | autocorrelation in a plain residual series without a regression design matrix |
| #77 ARCH-LM | when the heteroskedasticity is time-dependent (volatility clustering) |

### Output fields

- statistic: BG LM=n*R2 (Chisq)/F; BP Chisq; RESET F
- p_value: < a rejects H0 => a problem EXISTS
- parameter: df; method/data_name; htest: raw

### Pitfalls

- polarity: rejection = BAD (the model fails the diagnostic); H0='all is well'
- BG with a very small order misses high-order autocorrelation
- BP with studentize=FALSE is sensitive to non-normality - prefer TRUE
- a RESET rejection => misspecification BUT not of what kind
- a serial-correlation rejection => the OLS standard errors are invalid (use HAC/Newey-West), not necessarily biased coefficients

### References

- Breusch & Godfrey 1978
- Breusch & Pagan 1979; Koenker 1981 (studentized BP)
- Ramsey 1969 (RESET)
- Enders 2015 (BG > DW with a lagged y)
- lmtest reference manual (bgtest, bptest, resettest)

## #77 — ARCH-LM test (Engle)

**Module:** `arch.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_arch_test` | `x` | `series_handle`, `integer`, `boolean` | `lags=12`, `demean=False` | `light` | — |

### Use when

testing for ARCH effects (conditional heteroskedasticity / volatility clustering) in a univariate series/residuals; a pre-check before GARCH

### Do not use when

cross-sectional heteroskedasticity (→ bptest); autocorrelation in the level (→ bgtest/Ljung-Box); multivariate volatility

### Alternatives

| instead use | when |
| --- | --- |
| McLeod-Li (Ljung-Box on the squared residuals) | equivalent evidence of ARCH; ARCH-LM is preferred as a formal LM test with clear df |
| 06 GARCH-family | after a positive ARCH-LM -> fit a volatility model |

### Output fields

- statistic: Chi-squared LM=n*R2 of the auxiliary regression
- parameter: df = lags
- p_value: < a rejects H0 => ARCH effects EXIST (you want GARCH)
- lags/demean echoes; htest: raw

### Pitfalls

- polarity: rejection = an ARCH effect is present (H0='no ARCH'); a small p => conditional heteroskedasticity
- run it on residuals, not the raw series - ARCH in the raw series may be due to an unmodelled mean
- large lags => lower power
- namespace trap: ARIMA masks ARIMA in the model NSE - qualify the consumer, run the WHOLE run_verifications.sh

### References

- Engle 1982 (Econometrica, ARCH LM)
- McLeod & Li 1983 (squared-residual Ljung-Box)
- Tsay, Analysis of Financial Time Series (ARCH-LM pre-GARCH)
- FinTS reference manual (ArchTest)

## #94 — Density-forecast evaluation — CRPS / LogS / PIT (sample + parametric + tail-weighted)

**Module:** `density_forecast_evaluation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sr_crps_sample` | `y`, `dat` | `raw_handle`, `matrix_handle`, `enum`, `number` | — | `light` | — |
| `sr_logs_sample` | `y`, `dat` | `raw_handle`, `matrix_handle`, `number` | — | `light` | — |
| `sr_crps_parametric` | `y` | `raw_handle`, `enum`, `number`, `number`, `number`, `number`, `number` | `mean=0`, `sd=1`, `location=0`, `scale=1` | `light` | — |
| `sr_logs_parametric` | `y` | `raw_handle`, `enum`, `number`, `number`, `number`, `number`, `number` | `mean=0`, `sd=1`, `location=0`, `scale=1` | `light` | — |
| `sr_crps_tailweighted` | `y`, `dat` | `raw_handle`, `matrix_handle`, `enum`, `number`, `number`, `enum` | — | `light` | — |
| `sr_pit_sample` | `y`, `dat` | `raw_handle`, `matrix_handle` | — | `light` | — |

### Use when

evaluating a predictive DISTRIBUTION (posterior/ensemble draws or parametric) as a whole distribution; proper scoring (CRPS/LogS) + PIT calibration + tail-weighted CRPS for GaR downside risk

### Do not use when

a point-forecast comparison -> #74 DM; selecting among many point models -> #75 MCS; binary AUC -> #84 pROC; in-sample fit -> #76/#77; multivariate ES/VS are outside the surface

### Prerequisites

- c03_multivariate_nowcasting/bayesian_var.bvar_predict (or bvartools/bvarsv/mfbvar/bssm: they produce posterior predictive draws -> dat)
- c12_distribution_risk/quantile_regression.qr_growth_at_risk (GaR quantiles; the density comes via #95 -> parametric scoring)

### Alternatives

| instead use | when |
| --- | --- |
| sr_crps_sample(method=edf) | a robust default for draws; the same units as y |
| sr_logs_sample | a likelihood-based/local score; BUT sensitive to the KDE bandwidth in the tails |
| sr_*_parametric | the predictive distribution is explicitly normal/t/mixnorm (an analytic BVAR predictive) |
| sr_crps_tailweighted (twcrps/owcrps) | an asymmetric cost in the tail (GaR left-tail focus) |
| #74 Diebold-Mariano | point forecasts only (comparing 2 models) |
| #95 sn skew-t | GaR quantiles -> a full density; then parametric scoring here |

### Output fields

- scores: per-observation score vector (chart-data, score per time period)
- mean_score: the mean score (the comparative number; LOWER=BETTER)
- score: 'CRPS'/'LogS'/'twCRPS'; method (edf/kde) or family (normal/t/mixnorm)
- weighted/side/a/b/kind: tail-weighted metadata (twcrps threshold / owcrps outcome)
- sr_pit_sample.pit: PIT values in [0,1]; a histogram ~ Uniform => good calibration
- n / n_draws: number of observations / draws

### Pitfalls

- ORIENTATION: CRPS & LogS are NEGATIVELY oriented — LOWER = BETTER (not accuracy)
- LogS = -Inf if y falls outside the support of the draws; KDE smooths that but is sensitive to the bandwidth in the tails -> for heavy tails prefer CRPS(edf)
- the CRPS of a single observation is in the same units as y -> it is NOT comparable across series of different scale
- PIT: a ∪ shape => underdispersed (too tight a distribution); a ∩ shape => overdispersed; uniform => calibrated
- a low tail-weighted score may simply reflect few observations in the tail — read the per-obs scores
- bw: crps/logs_sample requires a bw vector[1:n]; the wrapper recycles a scalar -> length(y)

### References

- Jordan, Krüger & Lerch 2019 JSS 90(12) 'Evaluating Probabilistic Forecasts with scoringRules'
- Gneiting & Raftery 2007 JASA 102:359-378 (proper scoring rules, CRPS/LogS)
- Gneiting & Ranjan 2011 JBES 29(3):411-422 (threshold/outcome-weighted CRPS)
- Krüger, Lerch, Thorarinsdottir & Gneiting 2021 Int. J. Forecast. (predictive-distribution scoring)
- Diebold, Gunther & Tay 1998 Int. Econ. Rev. 39(4):863-883 (PIT calibration evaluation — the basis of sr_pit_sample, custom implementation)
- Berkowitz 2001 JBES 19(4):465-474 (PIT-based density-forecast test)
- scoringRules reference manual (
