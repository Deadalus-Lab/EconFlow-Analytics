<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 16-limited-dependent

3 METHOD-SELECTION cards, 3 modules, 4 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #83 — Binomial GLM (probit/logit) — recession probability (Estrella-Mishkin)

**Module:** `binomial_glm_recession.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_feglm_binom` | `formula`, `data` | `formula`, `df_handle`, `enum`, `string` | — | `light` | — |

### Use when

a binary outcome (a recession dummy 0/1); estimating P(y=1\|x) from predictors (the yield-curve spread) with probit/logit; optionally high-dimensional fixed effects + clustered SE + weights

### Do not use when

a continuous outcome (-> feols/forecasting); >2 categories (-> ordered/MSwM); an endogenous dynamic recession state (dynamic probit, outside the surface); counts (-> Poisson)

### Alternatives

| instead use | when |
| --- | --- |
| logit link | you want an odds-ratio interpretation (probit is the Estrella-Mishkin default) |
| base glm(family=binomial) | without high-dimensional FE / clustered SE it is equivalent |
| MSwM (cat. 06) | the recession state is latent/unobserved -> extract regime probabilities (gaussian/lm only) |
| dynamic probit (Kauppi-Saikkonen) | an autoregressive latent recession probability (outside the wrapper) |

### Output fields

- coefficients: named beta on the LINK scale (the index), NOT marginal effects/probabilities
- coeftable: term/estimate/std_error/z_value/p_value (z-test; SE clustered if a cluster was supplied)
- fitted_probabilities: P(y=1\|x) via predict(type=response) — the score that feeds #84
- obs_kept: 1-based indices of the retained rows (fixef/separation -> length < nrow; alignment)
- pseudo_r2: McFadden pseudo-R2 (ratio of log-likelihoods, fitstat pr2) — NOT an OLS R2
- loglik/aic/bic/deviance/nobs: fit stats; link/family/fixef_names: metadata

### Pitfalls

- coef = the effect on the latent index, NOT the marginal effect on the probability (which shrinks at the extremes); only the sign & significance are directly readable
- do NOT assume length(fitted_probabilities)==nrow; fixef/separation drops rows -> align through obs_kept
- pseudo-R2 != R2; a McFadden value of 0.3 is excellent (not '30% of the variance')
- perfect/quasi-separation -> coefficients of ±∞ with enormous SE, or a drop (check obs_kept & the SE)
- an in-sample AUC (via #84 on the same sample) is optimistic; an out-of-sample/real-time vintage is needed

### References

- fixest (help feglm, fitstat pr2=McFadden, predict.fixest; live-verified)
- Berge 2018 CREA DP (fixest reference)
- Estrella & Mishkin 1998 Rev. Econ. Stat. 80(1):45-61 (probit recession probability)
- Estrella & Hardouvelis 1991 J. Finance 46(2):555-576 (yield curve -> activity)
- Kauppi & Saikkonen 2008 Rev. Econ. Stat. 90(4):777-791 (dynamic probit, alt)
- McFadden 1974 (pseudo-R2)

## #84 — ROC / AUC — binary forecast evaluation

**Module:** `roc_auc_binary.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_roc` | `response`, `predictor` | `raw_handle`, `raw_handle`, `enum`, `boolean`, `number` | `ci=True`, `conf_level=0.95` | `light` | — |

### Use when

a numeric score/prediction (the fitted_probabilities of #83) + a binary target; threshold-independent discrimination: AUC + DeLong CI + the full ROC curve + the Youden best threshold

### Do not use when

>2 classes (multiclass); a point/interval forecast of a continuous variable (-> RMSE/DM, cat. 15); comparing two curves (roc_test, out of scope); calibration (-> Brier/reliability)

### Prerequisites

- c16_limited_dependent/binomial_glm_recession.run_feglm_binom (produces the fitted_probabilities score)

### Alternatives

| instead use | when |
| --- | --- |
| single-threshold accuracy/precision/recall | a specific false-alarm/miss cost; you operate at one cutoff (-> best_threshold) |
| bootstrap CI (ci.se/ci.sp) | partial AUC or smoothed curves (outside the wrapper; the default is analytic DeLong) |
| a cost-weighted threshold from roc_curve | an asymmetric cost, missed recession >> false alarm (Youden weights them equally) |
| roc_test (DeLong paired) | comparing two models/curves (outside the wrapper) |

### Output fields

- auc: Area Under Curve in [0,1]; 0.5=random, 1=perfect (the C-statistic)
- auc_ci: {low,high,conf_level,method=delong}; low>0.5 -> significantly better than random
- roc_curve: data_frame threshold/sensitivity/specificity (chart-ready; the ±Inf sentinels are removed)
- best_threshold: named list at the Youden point (threshold/sensitivity/specificity; several rows on ties)
- n_cases/n_controls: positives/negatives after the NA drop; controls_level/cases_level: WHICH label is which
- direction: '<' (controls<cases, the normal case for a probability score) or '>'; percent: FALSE

### Pitfalls

- CRITICAL label inversion: swapped control/case labels -> AUC=1-AUC; always read controls_level/cases_level; AUC<0.5 is often inverted labels/direction
- direction=auto silently picks the orientation with AUC>=0.5, hiding an inversion; for a strict evaluation set direction='<'
- an in-sample AUC (a predictor from the same sample) is optimistic; an out-of-sample/real-time evaluation is needed
- Youden != operationally optimal (it weights false alarm/miss equally; macro recession-calling is asymmetric)
- AUC measures discrimination, NOT calibration; the same AUC can correspond to very different probability calibration

### References

- pROC (help roc, ci.auc DeLong-default, coords(x=best)=Youden; live-verified)
- Robin et al. 2011 BMC Bioinformatics 12:77 (pROC)
- DeLong, DeLong & Clarke-Pearson 1988 Biometrics 44:837-845 (AUC variance / CI)
- Youden 1950 Cancer 3(1):32-35 (index J, best operating point)

## #206 — High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects

**Module:** `high_dimensional_way.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `alpaca_feglm` | `formula`, `data` | `formula`, `df_handle`, `enum`, `boolean`, `integer`, `enum` | `bias_correct=False`, `L=0` | `light` | `object` |
| `alpaca_apes` | `object` | `raw_handle`, `integer`, `enum`, `boolean` | `weak_exo=False` | `light` | — |

### Use when

panel/pseudo-panel micro data with MULTIPLE high-dimensional fixed effects (e.g. unit + time; or a network: exporter + importer) and a binary/count response — the probability of a recession/default/transition per unit; you want a consistent nonlinear FE estimate with a CORRECTION for the incidental-parameter bias (short-T panels) + interpretable average partial effects with SE

### Do not use when

no fixed effects (a plain glm/probit); a single FE + few levels (a classic conditional logit or #83 feglm suffices); you only want fitted probabilities/AUC without a bias correction (#83 run_feglm_binom); a continuous response (linear FE -> #33 fixest feols / #46 plm); APEs for poisson (getAPEs does not support it); functional forms (interactions/polynomials) in the APEs (not supported)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the panel data_frame; clean NA in the model variables)
- alpaca_feglm (the PRODUCER; the fit + an optional biasCorr -> the object handle consumed by alpaca_apes)
- c16_limited_dependent/binomial_glm_recession.run_feglm_binom (a fast binomial FE GLM + fitted probabilities/pseudo-R2 when you do NOT need the bias correction)

### Alternatives

| instead use | when |
| --- | --- |
| 16-limited-dependent/fixest-run_feglm_binom (fixest) | you want a plain binomial FE GLM with fitted probabilities/clustered SE/pseudo-R2 and you do NOT care about the incidental-parameter bias correction (a long T or large groups) |
| alpaca_apes | you have a fitted (+ bias-corrected) binary model and you want interpretable average partial effects (marginal effects) + delta-method SE rather than log-odds coefficients |
| #33 fx_feols / #46 pd_fit (plm) | a continuous response — linear fixed effects rather than a nonlinear GLM |

### Output fields

- alpaca_feglm.coefficients: the uncorrected structural beta (log-odds / log-rate); .coefficients_bias_corrected: the bias-corrected beta (NULL if bias_correct=FALSE)
- alpaca_feglm.coef_table: a matrix Estimate/Std. error/z value/Pr(>\|z\|) of the primary estimate (bias-corrected if it was requested)
- alpaca_feglm.deviance / .null_deviance / .converged / .iterations: fit diagnostics (converged=FALSE is blocked by a hard gate)
- alpaca_feglm.nobs (full/na/pc/effective) · .fe_names · .fe_levels (the number of levels per FE) · .n_fe · .bias_term/.bandwidth/.panel_structure (when bias corrected)
- alpaca_apes.ape: the average partial effects per covariate (in probability units); .ape_se: the delta-method SE; .ape_table: Estimate/SE/z/p; .vcov: the covariance matrix
- alpaca_apes.bias_corrected / .panel_structure / .sampling_fe / .weak_exo / .bandwidth / .n_pop: the estimation settings

### Pitfalls

- incidental-parameter bias: in nonlinear FE models with a short T the MLE coefficients are biased; bias_correct=TRUE (biasCorr) gives the correct (bias-corrected) beta — compare coefficients vs coefficients_bias_corrected (the difference is often ~20-30%)
- biasCorr/getAPEs are for binomial models ONLY: a poisson feglm is estimated, but bias_correct=TRUE and alpaca_apes are rejected by a hard gate (getAPEs supports binary choice only)
- coefficients != marginal effects: the feglm beta are log-odds (logit) / z-scores (probit) — do NOT interpret them as changes in probability; use alpaca_apes for interpretable average partial effects
- bandwidth L: 0 only if ALL the regressors are strictly exogenous; with a lagged outcome (a dynamic panel / state dependence) set L=1.4 (Fernández-Val/Weidner); the order of the FE in the formula matters when L>0
- panel.structure network vs classic: for bilateral flows (trade: exporter+importer+time) use network; the wrong structure gives a wrong bias correction & APE covariance (the wrapper reads the structure from the biasCorr object inside alpaca_apes for consistency)
- perfect classification: feglm silently drops rows/FE groups that are perfectly predicted (nobs.pc); check nobs so that you do not read a reduced sample as an error
- non-convergence: converged=FALSE (hard-gated) usually means linear dependence between a regressor and the FE; revise the specification

### References

- Stammann, A. (2018) Fast and Feasible Estimation of Generalized Linear Models with High-Dimensional k-Way Fixed Effects, ArXiv e-prints
- Fernández-Val, I. & Weidner, M. (2016) Individual and time effects in nonlinear panel models with large N, T, J. Econometrics 192(1):291-312
- Fernández-Val, I. & Weidner, M. (2018) Fixed effects estimation of large-T panel data models, Annual Review of Economics 10:109-138
- Neyman, J. & Scott, E.L. (1948) Consistent estimates based on partially consistent observations, Econometrica 16(1):1-32 (the incidental parameter problem)
- Cruz-Gonzalez, M., Fernández-Val, I. & Weidner, M. (2017) Bias corrections for probit and logit models with two-way fixed effects, Stata Journal 17(3):517-545 (average partial effects)
- Czarnowske, D. & Stammann, A. (2020) Fixed Effects Binary Choice Models: Estimation and Inference with Long Panels, ArXiv e-prints
