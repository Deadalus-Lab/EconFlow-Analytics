<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 07-causality-policy

22 METHOD-SELECTION cards, 22 modules, 59 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #33 — Fixed-effects OLS/IV + event study

**Module:** `fixed_effects_ols.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fx_feols` | `fml`, `data` | `formula`, `df_handle`, `string`, `string` | — | `light` | `object` |
| `fx_coeftable` | `object` | `raw_handle`, `string`, `string` | — | `light` | — |
| `fx_confint` | `object` | `raw_handle`, `number`, `string`, `string` | `level=0.95` | `light` | — |
| `fx_vcov` | `object` | `raw_handle`, `string`, `string` | — | `light` | — |
| `fx_fitstat` | `object`, `type` | `raw_handle`, `string`, `string`, `string` | — | `light` | — |

### Use when

panel/high-dimensional FE OLS, IV/2SLS, event study (sunab) with clustered SE

### Do not use when

staggered heterogeneity-robust ATT -> did/didimputation; naive TWFE on staggered designs = biased

### Alternatives

| instead use | when |
| --- | --- |
| #34 ivreg | classic single-endogenous 2SLS with ready-made diagnostics |
| #36 did / #37 didimputation | staggered ATT(g,t), heterogeneity-robust |
| #35 sandwich | HAC/Newey-West SE under serial correlation |

### Output fields

- coeftable: Estimate/Std.Error/t/p (data_frame)
- coefficients: named numeric coefficients
- is_iv: TRUE => the SE are 2SLS
- fixef_names: which FE were absorbed

### Pitfalls

- the default vcov is clustered on the 1st FE; changing the cluster changes all SE/CI
- event study: the reference-period coefficient is 0 by construction, not a 'zero effect'
- under staggered timing use sunab, not a bare i (negative-weighting bias)

### References

- Berge 2018 CREST WP
- Sun & Abraham 2021 J.Econometrics
- Goodman-Bacon 2021
- vignette fixest_walkthrough

## #34 — IV / 2SLS (classic)

**Module:** `iv_2sls.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_ivreg` | `formula`, `data` | `formula`, `df_handle`, `number` | `conf_level=0.95` | `light` | — |

### Use when

single-equation 2SLS with exogenous instruments + weak-IV/Wu-Hausman/Sargan diagnostics

### Do not use when

high-dimensional FE+IV -> fixest; high-dimensional controls -> DoubleML

### Alternatives

| instead use | when |
| --- | --- |
| #33 fixest IV | absorbed high-dimensional FE |
| #45 DoubleML PLR score=IV-type | high-dimensional controls/ML nuisance |
| #35 sandwich | robust/HAC SE on top of .object |

### Output fields

- coef_table: Estimate/SE/t/p
- diagnostics: test/df1/df2/statistic/p_value (Weak-IV/Wu-Hausman/Sargan)
- confint: CI at conf_level

### Pitfalls

- weak instruments (small F) => 2SLS biased towards OLS, SE unreliable
- a non-significant Wu-Hausman => endogeneity is not proven (OLS may suffice)
- just-identified: the Sargan row has df1=0 & NA statistic/p = 'not applicable', not an error

### References

- Kleiber & Zeileis 2008 (AER book)
- Wooldridge 2010
- Stock & Yogo 2005 (weak-IV)
- Sargan 1958
- Angrist & Pischke 2009

## #35 — HAC / robust standard errors

**Module:** `hac_robust_standard.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_vcov_hc` | `object` | `raw_handle`, `enum`, `boolean` | `sandwich=True` | `light` | — |
| `wrap_vcov_hac` | `object` | `raw_handle`, `enum`, `integer`, `boolean`, `boolean`, `boolean` | `sandwich=True` | `light` | — |
| `wrap_vcov_cl` | `object`, `cluster` | `raw_handle`, `raw_handle`, `enum`, `boolean` | `fix=False` | `light` | — |
| `wrap_vcov_panel` | `object`, `cluster`, `order_by` | `raw_handle`, `raw_handle`, `raw_handle`, `enum`, `enum`, `boolean`, `boolean` | `pairwise=False`, `fix=False` | `light` | — |
| `wrap_sandwich_blocks` | `object` | `raw_handle`, `boolean` | `adjust=False` | `light` | — |

### Use when

post-estimation correction of the SE of an already-fitted model (HC/Newey-West/clustered/Driscoll-Kraay/PCSE)

### Do not use when

when the estimating package already gives correct clustered SE (e.g. feols cluster=)

### Prerequisites

- c15_model_evaluation/breusch_godfrey_breusch.run_bg_test

### Alternatives

| instead use | when |
| --- | --- |
| #33 fixest built-in clustered SE | when they are available |
| vcovBS bootstrap (not exposed) | a very small number of clusters |

### Output fields

- vcov: covariance matrix (dimnames)
- se: sqrt of the diagonal
- coeftable: term/estimate/std_error/statistic/p_value (Normal z-test, not t)

### Pitfalls

- the p-values are asymptotic z, not small-sample t -> take care with small n
- NeweyWest defaults to prewhite=TRUE (VAR(1) prewhitening)
- the gates block silent failures: lag=-1 -> a NaN matrix; a cluster of length 1 -> non-conformable

### References

- White 1980
- Newey & West 1987/1994
- Andrews 1991
- Long & Ervin 2000 (HC3)
- Driscoll & Kraay 1998; Beck & Katz 1995; Cameron-Gelbach-Miller 2011
- Zeileis 2004/2006 JSS (sandwich)

## #36 — Staggered DiD (Callaway-Sant'Anna)

**Module:** `staggered_did.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_att_gt` | `yname`, `tname`, `gname`, `data` | `string`, `string`, `string`, `string`, `formula`, `df_handle`, `boolean`, `enum`, `enum`, `enum`, `boolean`, `integer`, `boolean`, `number` | `panel=True`, `bstrap=True`, `biters=1000`, `cband=True`, `alp=0.05` | `heavy` | `object` |
| `wrap_aggte` | `MP` | `raw_handle`, `enum`, `number`, `number`, `boolean` | `na_rm=False` | `light` | — |

### Use when

a panel with staggered adoption, heterogeneous ATT(g,t), doubly-robust + bootstrap bands

### Do not use when

analytic SE/speed -> didimputation; a simple 2x2 DiD -> a fixest interaction

### Alternatives

| instead use | when |
| --- | --- |
| #37 didimputation | imputation-based identification, analytic SE, speed |
| #33 fixest sunab | interaction-weighted event study |

### Output fields

- att/se per (group,t): the ATT(g,t)
- W/Wpval: pre-test of parallel trends
- overall.att/att.egt/se.egt: event study by relative time
- crit.val.egt: simultaneous critical value (not 1.96)

### Pitfalls

- the wrapper default aggregation = 'dynamic' (event study), not the package default 'group'
- the CI use crit.val.egt (a uniform band, wider than the pointwise one)
- bstrap=TRUE => stochastic, requires set.seed; a pre-period att~0 supports (does not prove) parallel trends

### References

- Callaway & Sant'Anna 2021 J.Econometrics
- Sant'Anna & Zhao 2020 (doubly-robust DiD)
- Goodman-Bacon 2021
- vignette did (multi-period-did)

## #37 — DiD imputation (Borusyak-Jaravel-Spiess)

**Module:** `did_imputation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_did_imputation` | `data`, `yname`, `gname`, `tname`, `idname` | `df_handle`, `string`, `string`, `string`, `string`, `formula`, `string` | — | `light` | — |

### Use when

staggered imputation-based DiD (Y(0) counterfactual), analytic SE, no seed

### Do not use when

a full ATG(g,t) + multiple aggregations + bands -> did

### Alternatives

| instead use | when |
| --- | --- |
| #36 did | group/calendar aggregation or bootstrap bands |
| #33 fixest sunab | event study |

### Output fields

- table/records: term/estimate/std_error/conf.low/conf.high
- n_terms: number of terms
- cluster_var: default = idname

### Pitfalls

- first_stage MUST be a one-sided formula (a two-sided one -> a silently wrong LHS, ~40% error)
- no treated unit => a silently empty table (the gate catches it)
- the CI are analytic (normal), not bootstrap

### References

- Borusyak, Jaravel & Spiess 2024 REStud (2021 WP)
- didimputation

## #38 — RDD robust (Calonico-Cattaneo-Titiunik)

**Module:** `rdd_robust.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_rdrobust` | `y`, `x` | `raw_handle`, `raw_handle`, `number`, `raw_handle`, `integer`, `enum`, `enum`, `enum`, `number` | `c=0`, `level=95` | `light` | — |
| `wrap_rdbwselect` | `y`, `x` | `raw_handle`, `raw_handle`, `number`, `integer`, `enum`, `enum`, `enum` | `c=0` | `light` | — |

### Use when

sharp/fuzzy/covariate-adjusted RD, MSE-optimal bw + robust bias-corrected CI (the CCT gold standard)

### Do not use when

a transparent/didactic RD or an IK cross-check -> rddtools; no clear cutoff -> RDD does not apply

### Alternatives

| instead use | when |
| --- | --- |
| #39 rddtools rdd_bw_ik | IK bandwidth vs CCT robustness comparison |

### Output fields

- coef/se/z/pv/ci: 3 rows Conventional/Bias-Corrected/Robust
- bws: h,b bandwidths
- tau_T/ci_T: fuzzy first-stage/LATE; coef_covs: only with covs

### Pitfalls

- report the ROBUST row for inference, not the Conventional p-value
- the estimate is LOCAL at the cutoff (LATE), not a global ATE
- manipulation of the running variable -> McCrary/rddensity (not exposed)

### References

- Calonico, Cattaneo & Titiunik 2014 Econometrica
- Calonico-Cattaneo-Farrell-Titiunik 2017 (rdrobust)
- Cattaneo-Idrobo-Titiunik 2020; Lee & Lemieux 2010

## #39 — RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only)

**Module:** `rdd.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_rdd_data` | `y`, `x`, `cutpoint` | `raw_handle`, `raw_handle`, `number`, `raw_handle` | — | `light` | `object` |
| `wrap_rdd_reg_lm` | `rdd_object` | `raw_handle`, `integer`, `enum`, `number` | `order=1` | `light` | — |
| `wrap_rdd_reg_np` | `rdd_object` | `raw_handle`, `number`, `enum`, `enum` | — | `light` | — |
| `wrap_rdd_bw_ik` | `rdd_object` | `raw_handle`, `enum` | — | `light` | — |

### Use when

a transparent step-by-step RD workflow, IK (2012) bandwidth, robustness cross-check of rdrobust

### Do not use when

production robust inference -> rdrobust; fuzzy RD ONLY through rdd_reg_lm

### Alternatives

| instead use | when |
| --- | --- |
| #38 rdrobust | the modern CCT robust standard; the two together = an IK vs CCT comparison |

### Output fields

- coefficients: the D (treatment dummy) = ATE/LATE
- coefficients_table: term/Estimate/Std.Error
- bandwidth; type (Sharp/Fuzzy); object = lm (sharp) or ivreg (fuzzy)

### Pitfalls

- fuzzy RD ONLY in rdd_reg_lm (rdd_reg_np is hard-blocked: a wrong D coefficient, not a LATE)
- the D coefficient is the quantity of interest (not the intercept/slope)
- a parametric RD with order>1 is sensitive to overfitting far from the cutoff

### References

- Imbens & Kalyanaraman 2012 REStud
- Imbens & Lemieux 2008; Gelman & Imbens 2019 JBES
- rddtools

## #40 — Synthetic Control (classic, Abadie)

**Module:** `synthetic_control.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_dataprep` | `foo` | `df_handle`, `series_codes`, `string`, `string`, `string`, `string`, `number`, `raw_handle`, `raw_handle`, `raw_handle`, `raw_handle` | `predictors_op='mean'` | `light` | `object` |
| `wrap_synth` | `dataprep_object` | `raw_handle`, `enum`, `boolean` | `genoud=False` | `heavy` | `object` |
| `wrap_synth_tab` | `synth_object`, `dataprep_object` | `raw_handle`, `raw_handle`, `integer` | `round_digit=3` | `light` | — |

### Use when

one treated unit + a donor pool; a synthetic counterfactual matching pre-treatment predictors

### Do not use when

prediction intervals -> scpi; a tidy API -> tidysynth; multiple/staggered -> gsynth; no donor pool -> CausalImpact

### Alternatives

| instead use | when |
| --- | --- |
| #41 scpi | uncertainty quantification / prediction intervals |
| #43 gsynth | >=2 treated / staggered / interactive FE |

### Output fields

- solution_w: donor weights (sparse, summing to 1)
- solution_v: predictor weights; loss_w/loss_v: MSPE
- Y1plot/Y0plot: for the frontend gap = Y1 - Y0*W

### Pitfalls

- a poor pre-fit (large loss_w) => the gap is not a valid effect
- no statistical significance directly -> placebo/permutation tests
- genoud=TRUE is stochastic (set.seed); genoud=FALSE is deterministic

### References

- Abadie & Gardeazabal 2003 AER
- Abadie, Diamond & Hainmueller 2010 JASA / 2015 AJPS
- Synth

## #41 — Synthetic Control + prediction intervals

**Module:** `synthetic_control_prediction.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_scdata` | `df`, `id_var`, `time_var`, `outcome_var`, `period_pre`, `period_post`, `unit_tr`, `unit_co` | `df_handle`, `string`, `string`, `string`, `raw_handle`, `raw_handle`, `raw_handle`, `raw_handle`, `series_codes`, `boolean`, `boolean` | `constant=False`, `cointegrated_data=False` | `light` | `object` |
| `wrap_scest` | `data` | `raw_handle`, `enum`, `string` | `solver='CLARABEL'` | `light` | `object` |
| `wrap_scpi` | `data` | `raw_handle`, `enum`, `enum`, `enum`, `integer`, `string` | `sims=200`, `solver='CLARABEL'` | `heavy` | — |

### Use when

a single treated unit with valid prediction intervals (in-sample + out-of-sample uncertainty)

### Do not use when

a point estimate only -> Synth; >=2 treated/staggered -> gsynth; placebo-only -> tidysynth

### Alternatives

| instead use | when |
| --- | --- |
| #40 Synth | the point estimate suffices |
| #43 gsynth | multi-unit / interactive FE |

### Output fields

- w: donor weights; fitted_pre/fitted_post
- ci_in_sample, ci_gaussian/ci_ls/ci_qreg (by e.method)
- bounds/sigma: variance components

### Pitfalls

- e.method='gaussian' => ci_ls/ci_qreg are NULL (not an error)
- prediction intervals are wider than naive CI (out-of-sample risk)
- sims= => stochastic (set.seed); the CLARABEL solver is deterministic for the weights

### References

- Cattaneo, Feng & Titiunik 2021 JASA
- Cattaneo-Feng-Palomba-Titiunik 2025 JSS scpi
- scpi

## #42 — Synthetic Control (tidy pipe)

**Module:** `synthetic_control_2.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_synthetic_control` | `data`, `outcome`, `unit`, `time`, `i_unit`, `i_time` | `df_handle`, `string`, `string`, `string`, `string`, `number`, `boolean` | `generate_placebos=False` | `heavy` | `object` |
| `wrap_generate_predictor` | `data`, `time_window`, `predictors` | `raw_handle`, `raw_handle`, `raw_handle` | — | `light` | `object` |
| `wrap_generate_weights` | `data`, `optimization_window` | `raw_handle`, `raw_handle`, `enum`, `boolean`, `enum`, `boolean` | `genoud=False`, `include_fit=False` | `heavy` | `object` |
| `wrap_generate_control` | `data` | `raw_handle` | — | `light` | `object` |
| `wrap_grab_synthetic_control` | `data` | `raw_handle`, `boolean` | `placebo=False` | `light` | — |
| `wrap_grab_unit_weights` | `data` | `raw_handle`, `boolean` | `placebo=False` | `light` | — |
| `wrap_grab_predictor_weights` | `data` | `raw_handle`, `boolean` | `placebo=False` | `light` | — |
| `wrap_grab_significance` | `data` | `raw_handle`, `raw_handle` | — | `light` | — |
| `wrap_grab_loss` | `data` | `raw_handle` | — | `light` | — |

### Use when

Abadie SC with a tidy/pipe grammar + built-in placebo-based inference (rank, Fisher p, MSPE ratio)

### Do not use when

prediction intervals -> scpi; multi-unit/interactive FE -> gsynth; minimal dependencies -> Synth

### Alternatives

| instead use | when |
| --- | --- |
| #40 Synth / #41 scpi | depending on the inference needs |

### Output fields

- grab_synthetic_control: real vs synthetic series (chart)
- grab_unit_weights (W); grab_predictor_weights (V)
- grab_significance: rank/fishers_exact_pvalue/mspe_ratio; grab_loss: pre/post MSPE

### Pitfalls

- generate_placebos=TRUE is MANDATORY for the placebo grab/significance (otherwise the treated unit is silently used as a placebo)
- without a sufficient donor pool (~20) the rank/Fisher significance is trivial (rank=1,p=1)
- 'significance' here is placebo-based permutation, not a classical p-value

### References

- Dunford tidysynth (the Abadie-Diamond-Hainmueller method)
- Abadie, Diamond & Hainmueller 2010 JASA / 2015 AJPS
- tidysynth

## #43 — Generalized Synthetic Control (interactive FE)

**Module:** `generalized_synthetic_control.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_gsynth` | `data`, `index` | `formula`, `df_handle`, `string`, `string`, `series_codes`, `series_codes`, `enum`, `enum`, `enum`, `integer`, `boolean`, `boolean`, `integer` | `r=0`, `CV=True`, `se=False`, `nboots=200` | `heavy` | — |

### Use when

multiple treated units / staggered adoption with latent common factors (interactive FE / matrix completion)

### Do not use when

one treated unit + donor matching -> Synth/scpi/tidysynth; covariate series without a panel -> CausalImpact

### Alternatives

| instead use | when |
| --- | --- |
| #40/#41 Synth/scpi | a single treated unit |
| #36/#37 did/didimputation | parallel trends without latent factors is plausible |

### Output fields

- att: by relative-to-treatment time (not calendar); att.avg: scalar ATT
- est.att/est.avg: ATT/S.E./CI/p (ONLY when se=TRUE, otherwise NULL)
- Y.ct: counterfactual matrix; r.cv: selected factors; vartype: inference path

### Pitfalls

- the wrapper default is force='two-way' (the package default is 'unit')
- est.att/est.avg are NULL without se=TRUE -> do not look for CI there
- se=TRUE requires an explicit seed; the na.rm documentation is FALSE (NA are silently accepted); r=-1 crashes, r=1.5 is silent; an alpha outside (0,1) -> an inverted CI

### References

- Xu 2017 Political Analysis
- Bai 2009 Econometrica (interactive FE)
- Liu-Wang-Xu 2022 fect; gsynth

## #44 — Causal forests / GRF

**Module:** `causal_forests_grf.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_causal_forest` | `X`, `Y`, `W` | `matrix_handle`, `raw_handle`, `raw_handle`, `integer`, `integer`, `boolean`, `integer` | `num_trees=2000`, `min_node_size=5`, `honesty=True` | `light` | `object` |
| `wrap_predict_causal_forest` | `forest` | `raw_handle`, `matrix_handle`, `boolean` | `estimate_variance=True` | `light` | — |
| `wrap_average_treatment_effect` | `forest` | `raw_handle`, `enum`, `enum` | — | `light` | — |
| `wrap_variable_importance` | `forest` | `raw_handle`, `integer`, `integer` | `decay_exponent=2`, `max_depth=4` | `light` | — |

### Use when

heterogeneous treatment effects CATE(x) with valid pointwise CI + doubly-robust ATE (AIPW/TMLE)

### Do not use when

a scalar ATE only with many controls -> DoubleML; a panel/time design -> #36-43; an instrument -> instrumental_forest

### Alternatives

| instead use | when |
| --- | --- |
| #45 DoubleML | mainly the ATE + a choice of learner & cross-fitting |

### Output fields

- predictions: OOB CATE on the training set
- se/ci.lower/ci.upper: 95% Normal (predict); estimate/std.err: AIPW ATE
- importance + variables: split-based

### Pitfalls

- the CATE are out-of-bag on the training set (not an in-sample fit)
- estimate.variance=TRUE is MANDATORY for CI (otherwise NULL); the seed is mandatory
- variable_importance is a split heuristic, not a formal test; ATT/overlap change the estimand

### References

- Wager & Athey 2018 JASA
- Athey, Tibshirani & Wager 2019 Annals of Statistics
- grf

## #45 — Double/Debiased ML

**Module:** `double_debiased.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `wrap_doubleml_data` | `data`, `y_col`, `d_cols`, `x_cols` | `df_handle`, `string`, `series_codes`, `series_codes`, `series_codes`, `boolean` | `use_other_treat_as_covariate=True` | `light` | `object` |
| `wrap_doubleml_plr` | `data`, `seed` | `raw_handle`, `enum`, `integer`, `integer`, `enum`, `enum`, `integer` | `n_folds=5`, `n_rep=1` | `heavy` | — |
| `wrap_doubleml_irm` | `data`, `seed` | `raw_handle`, `enum`, `integer`, `integer`, `enum`, `enum`, `enum`, `integer` | `n_folds=5`, `n_rep=1` | `heavy` | — |

### Use when

a causal parameter (ATE/coefficient) with high-dimensional confounders, ML nuisance + cross-fitting (Neyman-orthogonal)

### Do not use when

heterogeneity/CATE -> grf; low-dimensional + a known instrument -> AER; panel/time -> #36-43

### Alternatives

| instead use | when |
| --- | --- |
| #44 grf | CATE/heterogeneity is the objective |
| #34 AER ivreg | low-dimensional IV |

### Output fields

- coef: the debiased/orthogonal causal parameter
- se/t_stat/pval/ci_lower/ci_upper
- learner/n_folds/score/seed

### Pitfalls

- coef = the debiased orthogonal estimate (not a naive ML plug-in); PLR partialling-out vs IV-type changes the moment
- the IRM score ATE vs ATTE changes the estimand; the same seed => an identical coef/se
- learner is a closed whitelist {ranger,glmnet} (security); little overlap -> trimming affects the estimand

### References

- Chernozhukov et al. 2018 Econometrics Journal
- Bach-Chernozhukov-Kurz-Spindler 2022 JMLR DoubleML
- Robinson 1988; DoubleML

## #90 — Counterfactual intervention analysis (BSTS)

**Module:** `counterfactual_intervention.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_causal_impact` | `data`, `pre_period`, `post_period`, `seed` | `matrix_handle`, `raw_handle`, `raw_handle`, `number`, `integer` | `alpha=0.05` | `light` | — |

### Use when

the causal effect of one intervention on a time series without a donor pool; it requires unaffected covariate series

### Do not use when

a donor pool of units exists -> Synth/scpi/gsynth; a staggered panel -> did/didimputation; affected covariates -> biased

### Alternatives

| instead use | when |
| --- | --- |
| #40-43 Synthetic Control | a counterfactual from control units instead of control series |

### Output fields

- summary: Average & Cumulative x Actual/Pred/AbsEffect/RelEffect/p
- effect: scalars (abs/relative/p_value/alpha)
- series: a 15-column zoo (predictions+effect+bands, chart)

### Pitfalls

- p_value = a Bayesian tail-area posterior probability (not frequentist)
- the bands are credible intervals; if the covariates were affected, the 'effect' is an artifact
- MCMC => reproduction only with a fixed seed; no stationarity is required (bsts)

### References

- Brodersen, Gallusser, Koehler, Remy & Scott 2015 Annals of Applied Statistics
- Scott & Varian 2014 (bsts)
- CausalImpact

## #165 — Instrumental variables / 2SLS (the modern standalone ivreg, a three-part formula) + weak-instruments / Wu-Hausman / Sargan diagnostics

**Module:** `instrumental_variables_2sls.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `iv_fit` | `formula`, `data` | `formula`, `df_handle`, `enum`, `number` | `method='OLS'`, `conf_level=0.95` | `light` | `object` |

### Use when

endogenous regressor(s) — the regressor is correlated with the error (simultaneity/omitted variables/measurement error); you have valid external instruments; you want a consistent causal estimate with 2SLS + full identification/endogeneity/over-identification diagnostics

### Do not use when

all regressors are exogenous (use OLS/lm); fewer instruments than endogenous regressors (under-identified); weak instruments (weak-IV bias -> Anderson-Rubin/weak-IV-robust inference); panel FE-IV -> #33 fixest; ML-driven high-dimensional controls -> #45 DoubleML

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the data_frame; alternatively read_csv_data)
- iv_fit (the diagnostics come back inside it: the weak_instruments F, wu_hausman, sargan)

### Alternatives

| instead use | when |
| --- | --- |
| #34 wrap_ivreg (AER) | the classic 2-part IV interface 'y ~ x \| z'; the already existing ivreg |
| #33 fx_feols (fixest) | high-dimensional fixed effects + IV in the same fit (panel) |
| #45 wrap_doubleml_plr/irm (DoubleML) | many/non-linear controls, ML nuisance, debiased inference |
| method='M'/'MM' | outliers/heavy tails -> robust IV (it requires robustbase) |

### Output fields

- coefficients / coef_table: the 2SLS estimates + Estimate/Std. Error/t/p (the structural equation)
- conf_int: coefficient CIs at conf_level; sigma/df_residual/nobs/r_squared/adj_r_squared
- n_endogenous / n_instruments: the identification counts (over-identified <=> excluded instruments > endogenous regressors)
- weak_instruments: a list {df1,df2,statistic,p_value} PER endogenous regressor (the first-stage F); weak_instruments_flag = any F<10 (Staiger-Stock)
- wu_hausman: {df1,df2,statistic,p_value}, the endogeneity test (rejection -> the regressor really is endogenous, IV is justified)
- sargan: {df1,df2,statistic,p_value}, the over-identification test; df1=0 & NA when just-identified; the overidentified flag
- diagnostics: the full table (chart-data); fitted/residuals: chart-data

### Pitfalls

- three-part only: 'y ~ exog \| endog \| instruments'; a 2-part formula is blocked (go to #34 AER); an explicit gate on the number of RHS parts
- weak instruments: F<10 (weak_instruments_flag) => 2SLS bias + invalid standard CIs -> use weak-IV-robust inference; do NOT trust coef_table
- the Sargan test is meaningful ONLY when over-identified (df1>0); just-identified -> df1=0/NA (not an error, there is simply no test)
- Wu-Hausman: if it is NOT rejected, OLS is consistent+efficient — IV only loses efficiency (larger SE)
- masking: the standalone ivreg masks ivreg in the shared env -> the wrapper calls ivreg (namespaced); do NOT confuse it with #34
- method='M'/'MM' changes the estimator (robust), not only the SE; the diagnostics are interpreted on the robust fit

### References

- Fox, Kleiber & Zeileis, ivreg: Instrumental-Variables Regression by 2SLS <
- Sargan 1958 (Econometrica 26:393) over-identification test
- Wu 1973 / Hausman 1978 endogeneity test; Staiger & Stock 1997 (Econometrica 65:557) the weak-instruments F>10 rule

## #166 — Heterogeneity-robust dynamic DiD event study (de Chaisemartin & D'Haultfoeuille; non-binary/non-absorbing treatments)

**Module:** `heterogeneity_robust_dynamic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `didm_dyn` | `df`, `outcome`, `group`, `time`, `treatment` | `df_handle`, `string`, `string`, `string`, `string`, `integer`, `integer`, `series_codes`, `string`, `string`, `boolean`, `boolean`, `integer`, `boolean`, `integer`, `integer`, `integer` | `effects=1`, `placebo=0`, `normalized=False`, `trends_lin=False`, `effects_equal=False`, `ci_level=95`, `seed=2025` | `heavy` | — |

### Use when

a staggered panel where the treatment is non-binary AND/OR non-absorbing (it can switch off or change intensity) and past treatments affect the current outcome; you want dynamic event-study effects + a placebo pre-trends test + an average total effect, robust to heterogeneous effects (without the negative-weights bias of the TWFE)

### Do not use when

the treatment is binary AND absorbing (clean staggered adoption) -> #36 did / #37 didimputation (more direct); a simple 2x2 -> #33 fixest interaction; heterogeneity by covariates (CATE) rather than by event time -> #44 grf

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the long panel; it needs group/time/outcome/treatment columns and evenly spaced time)

### Alternatives

| instead use | when |
| --- | --- |
| #36 did (Callaway-Sant'Anna att_gt/aggte) | the treatment is binary & absorbing; a doubly-robust ATT(g,t) + bootstrap bands |
| #37 didimputation (Borusyak-Jaravel-Spiess) | an absorbing design; imputation-based, analytic SE, speed |
| #44 grf causal forest | heterogeneity by covariates (CATE) rather than by relative event time |
| HonestDiD sensitivity (consumer) | robustness to parallel-trends violations; it REQUIRES reordering coef_b/coef_vcov into chronological order (pre-periods=placebos first) before chaining |

### Output fields

- effects.estimate/se/lb_ci/ub_ci: the event-study path (Effect_1.L) — the dynamic treatment effects per relative period
- ate_estimate/ate_available: the average total effect per unit of treatment (NA/FALSE when trends_lin=TRUE)
- placebos.estimate/se: the placebo (pre-trends) estimators — E[placebo]=0 under parallel trends + no anticipation
- p_jointeffects (effects>=2) / p_jointplacebo (placebo>=2): joint tests; p_equality_effects (effects_equal=TRUE)
- coef_b / coef_vcov: the full coefficient vector + vcov in the order [Effects.., Placebos..] (post-first); FOR HonestDiD reorder them chronologically (placebos first)

### Pitfalls

- HonestDiD chaining TRAP: coef_b is ordered [Effects.., Placebos..] (post-first); HonestDiD expects CHRONOLOGICAL order (pre-periods first, numPrePeriods=the number of placebos); passing coef_b AS IS produces silently wrong robust CIs — reorder first
- a placebo ~0 SUPPORTS (does not prove) parallel trends/no anticipation; a high p_jointplacebo means the hypothesis is not rejected
- trends_lin=TRUE => the ATE is NOT computed (ate_available=FALSE, ate_estimate=NA) — do not read it as 0
- placebo>effects: the package SILENTLY clamps placebo to effects -> the wrapper hard-blocks it (no silent result)
- an NA in a core column: the package silently drops rows (a partial sample) -> the wrapper hard-blocks it (the full sample is required)
- ci_level>=100 is accepted silently by the package -> the wrapper blocks it (it must lie in (0,100))
- bootstrap => stochastic SE; the seed (default 2025) gives reproducibility; analytical SE (bootstrap=NULL) are deterministic

### References

- de Chaisemartin & D'Haultfoeuille 2020 AER 110(9) (fuzzy DiD / heterogeneous treatment effects)
- de Chaisemartin & D'Haultfoeuille 2024 Econometrics Journal (dynamic/event-study non-absorbing DiD)
- DIDmultiplegtDYN vignette + the did_multiplegt_dyn routine (v2.4.0)
- Rambachan & Roth 2023 ReStud (HonestDiD sensitivity — the consumer of coef_b/coef_vcov)

## #167 — Goodman-Bacon decomposition of the TWFE DiD coefficient (staggered adoption)

**Module:** `goodman_bacon_decomposition.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bacon_decompose` | `formula`, `data`, `id_var`, `time_var` | `formula`, `df_handle`, `string`, `string`, `boolean` | `quietly=True` | `light` | — |

### Use when

you ran a two-way fixed-effects DiD (unit+time FE) on a panel with STAGGERED adoption of the intervention and you want to see WHAT the single TWFE coefficient is made of — which 2x2 comparisons feed it and with what weights

### Do not use when

an unbalanced panel (it fails deliberately); simultaneous adoption by everyone (no staggered variation -> trivial); you want an ESTIMATOR unbiased under staggering (that is did/didimputation, not a diagnostic); a continuous/non-binary treatment

### Prerequisites

- c07_causality_policy/fixed_effects_ols.fx_feols (the source of the TWFE coefficient being decomposed — unit+time FE)
- c01_preparation_prechecks/panel_unit_root.run_purtest (macro/large-T only: stationarity before a panel DiD)
- c00_data_utilities/reading_delimited_fixed.read_csv_data (loading the long panel if it comes from a file)

### Alternatives

| instead use | when |
| --- | --- |
| 07-causality-policy/wrap_att_gt (Callaway-Sant'Anna) | you want an UNBIASED group-time ATT rather than a diagnostic; a never/late-treated control group exists |
| 07-causality-policy/wrap_did_imputation (Borusyak-Jaravel-Spiess) | you want an efficient imputation estimator robust to heterogeneity |
| 07-causality-policy/fx_feols (sunab) | you want cohort-interacted event-study estimates, not a diagnosis of the TWFE |

### Output fields

- two_by_twos: a data_frame per 2x2 comparison {treated, untreated (99999=never-treated), estimate, weight, type}
- type_summary: aggregate weights + the weighted mean estimate per comparison type (chart-data for the Goodman-Bacon table)
- twfe_estimate: the overall TWFE beta as a weighted-average identity (= sum(w*est); with covariates = Omega*beta_hat_w + (1-Omega)*sum(w*est))
- total_weight: the sum of the 2x2 weights (~1); n_2x2: the number of comparisons
- has_covariates/within_estimate/within_weight: the share & estimate of the within component (Omega, beta_hat_w); NA without covariates

### Pitfalls

- WATCH the 'Later vs Earlier Treated' comparison: it uses ALREADY-treated units as controls -> a forbidden comparison; a LARGE weight here means the TWFE is contaminated by negative-weighting/heterogeneity bias
- untreated=99999 denotes the never-treated group (the 'clean' 'Treated vs Untreated' type); it is not a real time value
- negative weights or negative estimates under staggering signal that the TWFE may have the wrong sign -> move to an unbiased estimator (did/didimputation)
- with time-varying covariates the within component enters (Omega>0); the identity still holds, but the decomposition approximates the TWFE through FWL
- it REQUIRES a strongly balanced panel; an unbalanced one -> a hard error (not a silent mistake)

### References

- Goodman-Bacon 2021 (J. Econometrics 225:254, 'Difference-in-Differences with Variation in Treatment Timing')
- de Chaisemartin & D'Haultfœuille 2020 (AER 110:2964, negative weights)
- the TWFE identity was verified numerically against lm(y ~ treated + factor(id) + factor(time)) (exact)

## #168 — Honest/robust inference under relaxed parallel trends (Rambachan-Roth sensitivity analysis)

**Module:** `honest_robust_inference.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `honest_smoothness` | `betahat`, `sigma`, `numPrePeriods`, `numPostPeriods` | `num_array`, `matrix_handle`, `integer`, `integer`, `num_array`, `num_array`, `enum`, `enum`, `enum`, `number`, `integer` | `alpha=0.05`, `seed=2025` | `light` | — |
| `honest_relmag` | `betahat`, `sigma`, `numPrePeriods`, `numPostPeriods` | `num_array`, `matrix_handle`, `integer`, `integer`, `num_array`, `num_array`, `enum`, `enum`, `enum`, `number`, `integer`, `integer` | `method='C-LF'`, `alpha=0.05`, `gridPoints=1000`, `seed=2025` | `light` | — |
| `honest_original_cs` | `betahat`, `sigma`, `numPrePeriods`, `numPostPeriods` | `num_array`, `matrix_handle`, `integer`, `integer`, `num_array`, `number` | `alpha=0.05` | `light` | — |

### Use when

you have an event-study/DiD estimate (betahat + vcov per period) and you want a CI that does NOT collapse if the parallel-trends assumption is violated slightly; the sensitivity of the inference to that violation

### Do not use when

you have no per-period event-study coefficients (an upstream leads/lags estimation is needed); a single post-period with no pre-periods (no basis for relative magnitudes); you do not care about robustness to parallel trends (the classic CI suffices)

### Prerequisites

- c07_causality_policy/fixed_effects_ols.fx_feols (event-study leads/lags -> betahat, sigma)
- c07_causality_policy/staggered_did.wrap_aggte (Callaway-Sant'Anna aggregation -> dynamic effects)
- c07_causality_policy/hac_robust_standard.wrap_vcov_hac (a robust vcov -> the sigma matrix)
- honest_original_cs (the baseline CI under strict parallel trends — the reference point)

### Alternatives

| instead use | when |
| --- | --- |
| honest_smoothness (DeltaSD) | when the violation is expected to be SMOOTH (bounded curvature of the trend) — you parameterise it with M |
| honest_relmag (DeltaRM) | when you do not want to choose M in absolute units — you bound the post-period violation as a multiple (Mbar) of the observed pre-period violation |
| #33 fx_feols event study without HonestDiD | when you are willing to assume strict parallel trends (no sensitivity analysis) |

### Output fields

- results: a data_frame lb/ub per value of M (smoothness) or Mbar (relmag) — chart-data for a sensitivity plot
- lb/ub: numeric vectors of the robust CI bounds per value of the bound
- method: the CI method that was used (FLCI/Conditional/C-F/C-LF)
- Delta: the restriction set (DeltaSD for smoothness, DeltaRM for relmag, Original for the baseline)
- M (smoothness) / Mbar (relmag): the value of the bound in each row; numPrePeriods/numPostPeriods/alpha

### Pitfalls

- the CI WIDENS as M/Mbar grows — that is the point (robustness), not a problem
- the breakdown value = the largest M/Mbar at which the CI does NOT contain 0; compare it with honest_original_cs (the baseline)
- Mbar=1 (relmag) => the post-period violation is allowed to be as large as the LARGEST pre-period violation — often the natural reference
- M is in ABSOLUTE units (the maximum second difference); Mbar is RELATIVE (in units of the pre-trend) — do not confuse them
- betahat/sigma MUST be in time order (pre then post, or consistent with the indices); the wrong order -> a silently wrong CI
- negative M/Mbar are accepted silently by the package — they are blocked here (gate)

### References

- Rambachan & Roth 2023, 'A More Credible Approach to Parallel Trends', Review of Economic Studies 90(5):2555-2591
- HonestDiD vignette/README (BCdata_EventStudy, LWdata_EventStudy replications)

## #169 — RD with multiple cutoffs / multiple scores (multi-cutoff & multi-score RD, robust bias-corrected)

**Module:** `rd_multiple_cutoffs.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `rdmc_fit` | `Y`, `X`, `C` | `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `enum`, `integer`, `enum`, `number`, `boolean` | `kernel='tri'`, `p=1`, `bwselect='mserd'`, `level=95`, `conventional=False` | `light` | — |
| `rdms_fit` | `Y`, `X`, `C` | `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `num_array`, `enum`, `integer`, `enum`, `number`, `boolean` | `kernel='tri'`, `p=1`, `bwselect='mserd'`, `level=95`, `conventional=False` | `light` | — |

### Use when

an RD design with MULTIPLE cutoffs (rdmc: C varies by unit) or cumulative cutoffs on one score (rdms); you want a pooled estimand + per-cutoff estimates, robust bias-corrected (Cattaneo-Titiunik-Vazquez-Bare)

### Do not use when

a single cutoff -> #38 rdrobust; a manipulation/density test (McCrary); sharp vs fuzzy without multiple cutoffs; a two-score design with X2/zvar/C2 (deliberately excluded, the rangemat is fragile)

### Prerequisites

- rdmc_fit (>=2 distinct cutoffs in the per-observation C; pooled + per cutoff)
- rdms_fit (a vector of cutoffs; xnorm for the pooled estimate)
- c07_causality_policy/rdd_robust.wrap_rdrobust (one cutoff: a plain RD instead of rdmc/rdms)
- c07_causality_policy/rdd_robust.wrap_rdbwselect (standalone bandwidth selection per cutoff)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading Y/X/C from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #38 wrap_rdrobust | a single cutoff (single-cutoff sharp/fuzzy RD) |
| #39 rddtools | parametric/non-parametric RD with an IK bandwidth, one cutoff |
| rdms_fit + xnorm | cumulative cutoffs on ONE score & you want a pooled estimand |
| conventional=TRUE | conventional (not robust bias-corrected) p-values/CI for comparison |

### Output fields

- pooled: {tau, se, pv, ci_l, ci_r, hl, hr, Nhl, Nhr} — the pooled estimand (always for rdmc; for rdms only with xnorm, otherwise available=FALSE)
- per_cutoff: a data_frame {cutoff, coef, se, ci_l, ci_r, pv, Nh_left, Nh_right, Nh_total[, weight]} = chart-data per cutoff
- weighted (rdmc): {coef, se, pv, ci_l, ci_r} — the weighted average of all cutoff-specific estimates
- cutoffs / n_cutoffs: the cutoff values (rdmc: sort(unique(C)); rdms: C as supplied)
- cfail / n_failed: the cutoffs where rdrobust failed (degeneracy); n_failed>0 -> a suspect estimate
- kernel / p / bwselect / level / conventional: the settings that were actually used

### Pitfalls

- rdmc: C is a per-observation cutoff variable (the SAME length as X); rdms: C is a vector of cutoff values — do not confuse them (a wrong length -> silent recycling, blocked by a gate)
- an NA in Y/X/fuzzy is ignored SILENTLY by rdrobust (N falls with no warning) -> a gate forbids NA
- the rdms pooled estimate is NA without xnorm; check pooled.available before reading pooled.tau
- robust bias-corrected (the default): the CI is NOT symmetric around the (conventional) coefficient — do not read it as coef±1.96·se
- cutoff-specific estimates at cutoffs with few observations (a small Nh_total) are noisy; look at Nh_total/n_failed
- a single cutoff in rdmc -> a cryptic error; use rdrobust (explicitly blocked by a >=2-cutoff gate)

### References

- Cattaneo, Titiunik & Vazquez-Bare (2020), 'Analysis of RD Designs with Multiple Cutoffs or Multiple Scores', Stata Journal 20(4):866-891
- Calonico, Cattaneo & Titiunik (2014, Econometrica 82:2295) robust bias-corrected inference (the rdrobust backbone)
- Cattaneo, Idrobo & Titiunik (2024) 'A Practical Introduction to RD Designs: Extensions' (CUP Elements) §multi-cutoff/multi-score

## #170 — Sensitivity analysis to unobserved confounding / omitted-variable bias (robustness value + OVB bounds)

**Module:** `sensitivity_unobserved_confounding.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sens_analyze` | `treatment`, `benchmark_covariates` | `string`, `series_codes`, `formula`, `df_handle`, `raw_handle`, `num_array`, `num_array`, `number`, `number`, `boolean` | `kd=1`, `q=1`, `alpha=0.05`, `reduce=True` | `light` | — |

### Use when

you have estimated a treatment effect with OLS (selection on observables) and you want to quantify how strong an UNOBSERVED confounder would have to be to change/eliminate the result (the robustness value, partial R², OVB-adjusted bounds relative to benchmark covariates)

### Do not use when

there is no credible OLS/linear design (RD/DiD/IV/synthetic control -> #38-45); you want a point-identified effect under confounding (that needs an IV/design, not sensitivity analysis); a non-linear/GLM outcome (the lm route does not apply); pre-trend sensitivity in an event study (-> HonestDiD)

### Prerequisites

- sens_analyze (the formula+data route: it fits the lm internally)
- c00_data_utilities/reading_delimited_fixed.read_csv_data (load the cross-section before the formula+data route)
- c00_data_utilities/analytic_ols_closed.ols_regress (an ALREADY fitted lm is passed as the object; the consuming route accepts only class 'lm')

### Alternatives

| instead use | when |
| --- | --- |
| #44 wrap_causal_forest (grf) | you want heterogeneous effects under unconfoundedness, not a diagnosis of its violation |
| #45 DoubleML | high-dimensional controls / debiased estimation instead of post-hoc sensitivity analysis |
| #34 ivreg / AER 2SLS | a valid instrument exists -> point identification instead of bounds |
| manual r2dz.x/r2yz.dx bounds (sensemakr) | you want hypothetical confounding scenarios without a benchmark covariate (scoped out here) |

### Output fields

- robustness_value (rv_q): how much partial R² (of a confounder with BOTH the treatment AND the outcome) is needed to reduce the effect by q·100%; close to 0 = fragile
- robustness_value_alpha (rv_qa): the same, but for statistical non-significance at alpha
- partial_r2_treatment (r2yd.x): the partial R² of the treatment with the outcome; an upper bound on what the treatment explains given the controls
- ovb_bounds: a table per (benchmark × kd/ky) with adjusted_estimate/se/lower_CI/upper_CI — the effect IF the confounder were kd/ky times stronger than the benchmark covariate
- unadjusted_estimate/se/t_statistic/dof: the original OLS estimate + the degrees of freedom

### Pitfalls

- the RV is NOT a p-value: a small RV = little confounder strength is required = a fragile result (not the other way round)
- reduce=TRUE (default) assumes the confounder REDUCES the effect; if the confounding would inflate it in the opposite direction, set reduce=FALSE
- the bounds are conditional on the assumption 'kd times stronger than the benchmark' — their credibility rests on whether the benchmark covariate really is comparable to the plausible confounder
- sensitivity ≠ identification: the tool does NOT correct the bias; it only says how much confounding would overturn it (design-based safety remains the user's responsibility)
- lm/OLS only: the package's fixest/formula/numeric routes are deliberately excluded; supply an object of class 'lm' or formula+data

### References

- Cinelli & Hazlett (2020), 'Making Sense of Sensitivity: Extending Omitted Variable Bias', JRSS-B 82(1):39-67
- Cinelli, Ferwerda & Hazlett (2020), 'sensemakr: Sensitivity Analysis Tools for OLS in the reference' (SSRN 3588978)

## #171 — IPW / double-ML treatment effects (ATE/ATET, IV-LATE/LATT, causal mediation)

**Module:** `ipw_double_treatment.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cw_treatDML` | `y`, `d`, `x` | `raw_handle`, `raw_handle`, `matrix_handle`, `number`, `number`, `number`, `enum`, `integer`, `boolean`, `integer` | `dtreat=1`, `dcontrol=0`, `trim=0.01`, `k=3`, `normalized=True`, `seed=2025` | `light` | — |
| `cw_treatweight` | `y`, `d`, `x` | `raw_handle`, `raw_handle`, `matrix_handle`, `boolean`, `number`, `boolean`, `integer`, `integer` | `ATET=False`, `trim=0.05`, `logit=False`, `boot=1999`, `seed=2025` | `heavy` | — |
| `cw_lateweight` | `y`, `d`, `z`, `x` | `raw_handle`, `raw_handle`, `raw_handle`, `matrix_handle`, `boolean`, `number`, `boolean`, `integer`, `integer` | `LATT=False`, `trim=0.05`, `logit=False`, `boot=1999`, `seed=2025` | `heavy` | — |
| `cw_medDML` | `y`, `d`, `m`, `x` | `raw_handle`, `raw_handle`, `raw_handle`, `matrix_handle`, `integer`, `number`, `boolean`, `boolean`, `enum`, `integer` | `k=3`, `trim=0.05`, `multmed=True`, `normalized=True`, `seed=2025` | `light` | — |

### Use when

selection-on-observables treatment evaluation with ready-made y/d/x vectors (NOT a formula): DML-ATE for a discrete treatment (cw_treatDML); IPW ATE/ATET for a binary treatment (cw_treatweight); IV-LATE/LATT with a binary instrument (cw_lateweight); a direct/indirect split through a mediator (cw_medDML)

### Do not use when

you have no observable confounders (unconfoundedness fails -> RD/DiD/synthetic control); panel/staggered adoption (#36-37/#43); heterogeneous CATE by covariate (grf #44); linear IV with a formula (#34 ivreg; #33 fixest); a time series/intervention (#90 CausalImpact)

### Prerequisites

- cw_treatweight (unconfoundedness + common support: check ntrimmed/overlap before the ATE)
- cw_lateweight (the first stage 'first' = the complier share: a weak instrument if it is ~0)
- c07_causality_policy/double_debiased.wrap_doubleml_irm (cross-check the ATE with an independent DML implementation)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the tabular dataset; build the y/d/x/z/m vectors)

### Alternatives

| instead use | when |
| --- | --- |
| 07-causality-policy/wrap_doubleml_irm | you want the full DoubleML framework (ranger/glmnet learners, ATTE, tuning) rather than IPW/efficient-score |
| 07-causality-policy/wrap_causal_forest | heterogeneous CATE by covariate, not only a population ATE |
| 07-causality-policy/iv_fit | linear 2SLS IV with a formula (a continuous treatment/instrument; a global LATE assuming linearity) |
| cw_treatDML instead of cw_treatweight | you want doubly-robust/ML nuisance (Neyman orthogonality) rather than plain IPW; or a multi-valued discrete treatment |

### Output fields

- effect: the main causal effect (ATE/ATET/LATE/LATT); se: the standard error; pval: the p-value
- cw_treatweight: y1/y0 (the mean potential outcomes); estimand 'ATE'/'ATET'
- cw_lateweight: first (+se_first/pval_first) = the complier share/first stage; ITT (+se_ITT/pval_ITT) = intention to treat
- cw_medDML: ate + dir_treat/dir_control (natural direct) + indir_treat/indir_control (natural indirect); se/pval of length 6 (a 3x6 results matrix)
- ntrimmed: the number of observations dropped because of extreme propensity scores (an overlap diagnostic)

### Pitfalls

- unconfoundedness is an UNTESTABLE assumption — the SE do not certify it; a high ntrimmed = weak overlap, and the estimate then rests on a few units
- the IV-LATE (cw_lateweight) is an effect ONLY on the compliers, not on the population; a small 'first' -> a weak instrument, the effect explodes/is unstable
- mediation (cw_medDML) ADDITIONALLY requires sequential ignorability of the mediator; the direct+indirect split is not fully experimentally identified
- stochasticity: treatDML/medDML (cross-fitting fold splits) & treatweight/lateweight (bootstrap) -> the same effect ONLY with the same seed (default 2025)
- MLmethod='lasso' in cw_medDML (hdm rlasso) can throw 'subscript out of bounds' at small n -> use 'parametric'/'randomforest' or a larger sample
- d must be 0/1 (treatweight/lateweight/medDML) & z 0/1 (lateweight); a non-binary d/z is blocked (otherwise a cryptic 'y values must be 0<=y<=1' from the probit)

### References

- Chernozhukov et al. 2018, 'Double/debiased machine learning', Econometrics Journal 21:C1-C68
- Huber 2012 (JEBS 37:443) & 2014 (Econometric Reviews 33:869) — IPW treatment/selection
- Farbmacher, Huber, Laffers, Langen, Spindler 2022, 'Causal mediation analysis with double machine learning', Econometrics Journal 25:277-300
- Tchetgen Tchetgen & Shpitser 2012 (Annals of Statistics 40:1816) — semiparametric mediation
- Horvitz & Thompson 1952 (JASA 47:663) — inverse probability weighting

## #172 — Generalized Method of Moments (linear IV / moment conditions) + the Hansen-Sargan J test

**Module:** `generalized_moments_hansen.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `gmm_fit` | `formula`, `instruments`, `data` | `formula`, `formula`, `df_handle`, `enum`, `enum`, `enum` | — | `light` | `object` |
| `gmm_jtest` | `object` | `raw_handle` | — | `light` | — |

### Use when

over-identified linear IV / moment-condition estimation (Euler equations, macro/finance) where you want efficient GMM + HAC-robust inference + a test of instrument validity (Hansen J)

### Do not use when

just-identified single-endogenous 2SLS (use ivreg/AER); non-linear user-supplied moment functions (NOT exposed — an eval surface); dynamic panel GMM (Arellano-Bond -> #47 pgmm)

### Prerequisites

- gmm_jtest (the Hansen-Sargan J test after estimation: rejecting H0 -> the instruments/moment conditions are NOT valid)
- c01_preparation_prechecks/unit_root_suite.wrap_ur_df (stationarity of the series before GMM on time series — a HAC vcov presupposes weak dependence)

### Alternatives

| instead use | when |
| --- | --- |
| 07-causality-policy/iv_fit | just-identified 2SLS, or you want rich IV diagnostics (the weak-instruments F, Wu-Hausman endogeneity, Sargan) |
| 07-causality-policy/wrap_ivreg | classic 2SLS with the simple formula 'y ~ x \| z' |
| 07-causality-policy/fx_feols (IV mode) | high-dimensional fixed effects + IV together |
| wmatrix='ident' | you want a 2SLS-equivalent estimate (identity weighting) rather than efficient GMM |

### Output fields

- coefficients: a named numeric vector — the coefficient estimates (e.g. the slope on the endogenous regressor)
- coef_table: a matrix Estimate/Std. Error/z value/Pr(>\|z\|) — asymptotic normal inference (the SE come from the chosen vcov)
- vcov / std_errors: the covariance matrix of the coefficients and the SE (they correspond to the vcov argument)
- J_test: {statistic, df, p_value}, the Hansen over-identification test; df = #instruments - #coefficients (df=0 => just-identified, p_value=NA)
- df / nobs / type / wmatrix / vcov_type: the over-identifying df, the observations (after the NA gate), the estimator settings

### Pitfalls

- Hansen J: a SMALL p_value (rejecting H0) => the instruments/moment conditions are NOT valid (misspecification), NOT 'a significant result'
- just-identified (df=0): the J test is NOT defined — gmm_jtest returns statistic≈0 + a note, p_value=NA; do not read it as a 'perfect fit'
- gmm drops rows with NA SILENTLY (only a warning) — the wrapper blocks it with a gate; nobs = the rows after cleaning
- vcov='HAC' (the default): autocorrelation-robust — for a pure cross-section prefer vcov='iid'/'MDS'; the SE change substantially with the vcov
- under-identification (moments < coefficients) is blocked by a clean gate before the call — add instruments
- SECURITY: only the formula/linear interface is exposed; a user-supplied moment function (gmm(g=<fn>)) is NOT supported (an eval surface)

### References

- Hansen (1982) 'Large Sample Properties of GMM Estimators', Econometrica 50:1029
- Chausse (2010) 'Computing Generalized Method of Moments with the gmm Package', JSS 34(11) — the gmm vignette
- help('gmm','gmm'), help('specTest','gmm') (gmm 1.9.1)
- Hall (2005) Generalized Method of Moments, Oxford — the Sargan-Hansen J over-identification test
