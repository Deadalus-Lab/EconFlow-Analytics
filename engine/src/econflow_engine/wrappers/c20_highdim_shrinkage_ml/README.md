<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 20-highdim-shrinkage-ml

5 METHOD-SELECTION cards, 5 modules, 12 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #216 — Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path)

**Module:** `regularized_regression_lasso.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fit_glmnet` | `x`, `y` | `matrix_handle`, `matrix_handle`, `enum`, `number`, `integer`, `boolean`, `boolean` | `alpha=1`, `nlambda=100`, `standardize=True`, `intercept=True` | `light` | `model` |
| `cv_glmnet` | `x`, `y` | `matrix_handle`, `matrix_handle`, `enum`, `number`, `integer`, `enum`, `integer`, `boolean`, `boolean` | `alpha=1`, `nfolds=10`, `seed=42`, `standardize=True`, `intercept=True` | `light` | `cv` |
| `glmnet_coefficients` | `object` | `raw_handle`, `number`, `enum` | — | `light` | — |
| `glmnet_predict` | `object`, `newx` | `raw_handle`, `matrix_handle`, `number`, `enum`, `enum` | — | `light` | — |

### Use when

many predictors p (or p >> n); you want shrinkage + variable selection with a penalized regression; alpha=1 Lasso (sparse), alpha=0 Ridge, 0<alpha<1 Elastic-Net; cv.glmnet selects lambda (lambda.min = the minimum CV error, lambda.1se = the parsimonious choice). families: gaussian/binomial/poisson/multinomial

### Do not use when

a low dimension + you want inference/p-values (OLS/GLM); group-structured selection (grpreg); nonlinear/tree ML (ranger/mboost); Bayesian model averaging (BMS); quantile/tail work (quantreg #64); you need unbiased coefficients (the shrinkage introduces bias — a feature, not a bug)

### Alternatives

| instead use | when |
| --- | --- |
| alpha=1 (Lasso) | you want a SPARSE model — variable selection; unstable with strongly correlated predictors (it picks one arbitrarily) |
| alpha=0 (Ridge) | correlated predictors; you want to shrink everything (nothing is EXACTLY zero); better under multicollinearity |
| 0<alpha<1 (Elastic-Net) | grouped selection under correlation — a compromise between Lasso and Ridge (Zou-Hastie) |
| grpreg (group lasso/SCAD/MCP) | the predictors have a KNOWN group structure (dummies, splines) — selecting whole groups |
| ranger / mboost | you want non-linearity/interactions (RF / boosting) rather than a linear penalized model |
| lambda.min vs lambda.1se | lambda.min = the best prediction; lambda.1se = parsimonious/interpretable (the one-standard-error rule) |

### Output fields

- fit_glmnet.path: a data_frame step/lambda/df/dev_ratio (the regularization path)
- fit_glmnet.dev_ratio: the share of deviance explained per lambda (increasing as lambda falls, ∈[0,1))
- cv_glmnet.cv_curve: a data_frame lambda/cvm/cvsd/cvup/cvlo/nzero (the CV curve)
- cv_glmnet.lambda_min / .lambda_1se: the selected lambdas (1se >= min)
- cv_glmnet.selected_min / .selected_1se: the NON-ZERO coefficients (class/term/coefficient)
- cv_glmnet.nzero_min / .nzero_1se · .dev_ratio_min / .dev_ratio_1se: the size & fit at the two lambdas
- glmnet_coefficients.selected: the nonzero coefficients at a given lambda; .n_nonzero
- glmnet_predict.predictions: a data_frame row_id + prediction (or per-class probabilities / predicted_class)
- model / cv: the raw fits (to_mcp -> a stub; registry chaining)

### Pitfalls

- shrinkage => BIASED coefficients (they shrink towards 0); do NOT read them as unbiased OLS effects — glmnet coefficients yield no valid p-value/CI
- lambda.min vs lambda.1se: lambda.1se is ALWAYS >= lambda.min => fewer variables; the '1se' rule is more parsimonious (the one-standard-error rule), not 'a better prediction'
- cv.glmnet is STOCHASTIC (the fold split) — without a fixed seed/foldid you get a DIFFERENT lambda every time; the wrapper seeds it (default seed=42)
- the Lasso with correlated predictors picks ONE arbitrarily => the 'selection' is not stable; use Ridge/Elastic-Net for groups
- standardize=TRUE (default) standardizes INTERNALLY but returns the coefficients on the original scale — compare magnitudes ONLY on a standardized scale
- df = the number of non-zero coefficients (EXCLUDING the intercept); nzero from cv is the same; the intercept is not penalized
- binomial: 2 classes (otherwise multinomial); multinomial: >=3; predict type=response = probabilities (the rows sum to 1 in the multinomial case), type=class = a label
- the variable-selection count = nrow(selected_min)/nrow(selected_1se)/n_nonzero EXCLUDES the (Intercept) and equals nzero_min/nzero_1se — do NOT add 1 for the intercept; coef_min/coef_1se/coefficients do keep the intercept
- multinomial predict: n_new==nrow(predictions) ALWAYS; for ONE new period the k values are the class probabilities of that ONE observation (the columns), NOT k separate observations (rows)

### References

- Friedman, Hastie, Tibshirani 2010 JSS 33(1) 'Regularization Paths for GLMs via Coordinate Descent' (glmnet)
- Tibshirani 1996 JRSS-B 58(1) 267-288 (the Lasso); Hoerl-Kennard 1970 Technometrics (Ridge); Zou-Hastie 2005 JRSS-B 67(2) 301-320 (the Elastic-Net)
- glmnet v5.0 ref manual — the glmnet/cv.glmnet/coef.glmnet/predict.glmnet help pages, the glmnet vignette (live-verified)
- wrapper footer IMPLEMENTATION NOTE (c20_highdim_shrinkage_ml/regularized_regression_lasso)

## #217 — Random forests (ranger): OOB error, variable importance, quantile regression forests

**Module:** `random_forests_oob.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `rf_fit` | `x`, `y` | `matrix_handle`, `matrix_handle`, `integer`, `integer`, `integer`, `enum`, `boolean`, `boolean`, `boolean`, `integer` | `num_trees=500`, `quantreg=False`, `probability=False`, `classification=False`, `seed=42` | `light` | `model` |
| `rf_predict` | `object`, `newdata` | `raw_handle`, `matrix_handle`, `enum`, `num_array`, `enum`, `integer` | `seed=42` | `light` | — |

### Use when

a non-parametric, non-linear predictive baseline on a macro/financial cross-section or a pooled panel (a design matrix X + a response y); you want an OOB error estimate without a separate validation set, variable importance (non-linear importance/interactions), or the WHOLE conditional distribution through quantile regression forests (prediction intervals / tails); a regression, classification or probability forest

### Do not use when

you want interpretable coefficients / sparse variable selection -> glmnet/grpreg; linear relations with few variables (an RF is excessive and loses efficiency); a temporal structure/autocorrelation that must be modelled explicitly (an RF ignores the order — you need lagged features); a conditional-on-X tail of a linear outcome with interpretable SE -> quantreg GaR (#64); extrapolation outside the training support (an RF does not extrapolate)

### Alternatives

| instead use | when |
| --- | --- |
| glmnet (Lasso/Ridge/Elastic-Net) | you want sparse, interpretable linear coefficients + a regularization path/CV rather than black-box importance; a linear structure |
| mboost (component-wise boosting) | you want custom losses (quantile/Huber) + automatic variable selection with additive interpretability |
| grf/DoubleML (cat. 07 causal ML) | you want CAUSAL effects (CATE/heterogeneous treatment) with valid inference, not pure prediction |
| quantreg (#64 Growth-at-Risk) | a linear conditional-quantile relation with interpretable coefficients + analytic SE rather than a forest-based distribution |

### Output fields

- oob_prediction_error: the out-of-bag error — MSE (regression), the misclassification rate in [0,1] (classification), the Brier score (probability); NOT in-sample
- variable_importance / importance_table: the named importance per variable (sorted in decreasing order); empty when importance='none'
- r_squared: the OOB R^2 (regression); NA for classification/probability
- treetype: 'Regression' / 'Classification' / 'Probability estimation' (it states which forest was trained)
- num_trees/mtry/min_node_size: the ACTUAL values that were used (the ranger defaults for mtry/min_node_size if NULL)
- is_quantreg/is_classification/is_probability/classes: the flags + the class levels; seed: reproducibility
- model: the raw ranger forest (register -> a raw_handle for rf_predict; to_mcp -> a stub)
- rf_predict predictions: a numeric vector (regression), character labels (classification), a probability matrix (probability), a q<value> matrix (quantiles); se/se_table (type='se')

### Pitfalls

- DETERMINISM: ranger is NON-reproducible with num.threads>1 EVEN with a fixed seed (per-thread RNG streams); the wrapper PINS num.threads=1 (it is not exposed) — do not bypass it
- type='se' (jackknife-after-bootstrap, Wager-Hastie-Efron) uses the reference RNG -> it was NON-deterministic; the wrapper calls set.seed(seed) BEFORE predict; in addition the infjack SE can be NA at a few points (a small num.trees) — that is real, not an error
- importance='impurity' is biased towards high-cardinality/continuous variables (Strobl 2007); for a reliable comparison use 'permutation' or 'impurity_corrected' (Nembrini 2018); the importance is NOT a causal effect and carries no sign/direction
- type='quantiles' requires a forest trained with quantreg=TRUE (Meinshausen); the wrapper fences it (object.random.node.values); the quantiles are not theoretically guaranteed monotone but typically are (quantile crossing is rare in forests)
- the OOB error is NOT a test error under temporal/spatial dependence (the OOB samples leak information from neighbours); for time series use out-of-time validation, not OOB
- an RF does NOT extrapolate: predictions at X outside the training support are pinned to the extremes of the training values (do not use it for out-of-sample scenarios)
- classification/probability convert a numeric y into a factor; the classes are the codes as strings; quantreg is incompatible with classification/probability (a hard stop)
- rf_predict NAME-MATCH gate: newdata must have colnames matching (as a set) the training variables; an unnamed/wrongly named newdata → blocked-by-gate (NOT a silent positional match); the column order does NOT matter (matching is by NAME)
- rf_predict accepts a newdata of ONE row (n_pred=1, a single out-of-sample/GaR point); the >=2-row rule applies ONLY at training; the quantiles must be DISTINCT (otherwise blocked-by-gate)
- type='se' (infjack/jack) is SEED-INDEPENDENT (deterministic given the inbag counts); the 'seed' argument acts ONLY on the rf_fit bootstrap; num.threads is pinned to 1 for determinism

### References

- Wright M.N., Ziegler A. (2017) 'ranger: A Fast Implementation of Random Forests for High Dimensional Data in C++ and the reference' J. Statistical Software 77(1) 1-17
- Breiman L. (2001) 'Random Forests' Machine Learning 45(1) 5-32
- Meinshausen N. (2006) 'Quantile Regression Forests' JMLR 7 983-999 [quantreg=TRUE]
- Wager S., Hastie T., Efron B. (2014) 'Confidence Intervals for Random Forests: The Jackknife and the Infinitesimal Jackknife' JMLR 15 1625-1651 [type='se' infjack/jack]
- Nembrini S., Koenig I., Wright M.N. (2018) 'The revival of the Gini importance?' Bioinformatics 34(21) 3711-3718 [impurity_corrected]
- Strobl C. et al. (2007) 'Bias in random forest variable importance measures' BMC Bioinformatics 8:25 [permutation vs impurity bias]
- ranger v0.18.0 ref manual (the ranger, predict.ranger help pages, live-verified)
- wrapper footer IMPLEMENTATION NOTE (c20_highdim_shrinkage_ml/random_forests_oob)

## #218 — Component-wise gradient boosting (glmboost) — high-dimensional shrinkage + automatic variable selection with custom losses

**Module:** `component_wise_gradient.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `glmboost_fit` | `x`, `y` | `matrix_handle`, `matrix_handle`, `enum`, `number`, `integer`, `number`, `boolean` | `mstop=100` | `light` | `model` |
| `glmboost_cv_mstop` | `x`, `y` | `matrix_handle`, `matrix_handle`, `enum`, `number`, `integer`, `number`, `boolean`, `enum`, `integer`, `integer` | `mstop_max=200`, `cv_B=25`, `seed=42` | `light` | `model` |

### Use when

high-dimensional (p~n or p>n) macro/financial predictors X; you want shrinkage AND sparse variable selection SIMULTANEOUSLY (unselected variables get a coefficient of EXACTLY 0) with a selectable loss (L2 Gaussian; pinball QuantReg; L1 Laplace; robust Huber; logistic Binomial; count Poisson); mstop (the regularization) is chosen data-driven with a cross-validated risk (glmboost_cv_mstop)

### Do not use when

you want non-linear/smooth effects (gamboost/bbs — NOT exposed; see the footer); purely non-linear prediction + importance -> ranger; heterogeneous CATE -> grf; debiased inference on ONE target coefficient -> DoubleML; a linear Growth-at-Risk over several tau -> quantreg (#64); a sparse VAR/lag-multivariate model -> BigVAR/midasml

### Alternatives

| instead use | when |
| --- | --- |
| ranger (a random forest) | you want non-linear interactions + permutation importance rather than a linear sparse model; no strict sparsity |
| grf (a causal/regression forest) | you want heterogeneous treatment effects (CATE), not predictor selection in a regression |
| DoubleML (double/debiased ML) | you want an unbiased SE on ONE specific coefficient with ML nuisance controls, not a selection path |
| quantreg (a linear QR / GaR, #64) | you want full multi-tau conditional-quantile inference (se/p-values) without boosting selection |
| glmnet / BigVAR (penalized) | you want an L1/elastic-net path with lambda (a convex penalty) rather than functional-gradient descent with mstop |
| gamboost (smooth base learners) | you want non-linear P-spline effects — outside the surface (the bbs symbol lookup requires attaching, which breaks the masking rule) |

### Output fields

- coefficients: a data_frame term/coefficient/selected — COMPLETE (all p predictors; 0 for the unselected ones); on the centered scale when center=TRUE
- offset: the intercept level (with the centered scale the mean moves here; NOT 0)
- selection_freq: term/n_selected/frequency — how often each predictor was updated along the boosting path (the sum of n_selected == mstop)
- n_selected_vars / selected_vars: the number & names of the non-zero predictors (the sparsity)
- path_risk / final_risk (glmboost_fit): the empirical in-bag risk per step (chart-ready; monotonically decreasing)
- optimal_mstop / optimal_mean_risk (glmboost_cv_mstop): the data-driven mstop = the argmin of the cross-validated risk
- cv_curve (glmboost_cv_mstop): a data_frame mstop/mean_risk/se_risk — the CV curve (chart-ready)
- family/tau/nu/mstop/center/n/p/cv_type/cv_B/seed: the rules that produced the result (an audit trail)
- model: the raw glmboost fit — a register handle for downstream chaining; to_mcp -> a stub

### Pitfalls

- Binomial coefficients are HALF the size of the glm(family=binomial) coefficients (mboost emits a NOTE about this); do NOT compare them directly with a logistic regression — multiply by 2 for the glm scale
- mstop IS the regularization knob: too large -> overfitting, too small -> underfitting; for an honest choice use glmboost_cv_mstop (cross-validated), NOT an arbitrary fixed mstop
- selection_freq counts the UPDATE FREQUENCY (its sum == mstop), NOT the effect size; a predictor with a large \|coefficient\| may have been selected few times and vice versa
- center=TRUE emits the benign warning 'model does not contain intercept' — the offset IS the intercept (off2int=TRUE is ignored); read the offset field, not 0
- cvrisk is STOCHASTIC in generating the folds -> set.seed(seed) INSIDE (default 42) + papply=lapply (single-threaded); mclapply/fork would break reproducibility; the glmboost fit itself is deterministic
- Binomial requires a binary y (a 2-level factor; the wrapper converts a numeric 2-value y); Poisson requires non-negative INTEGERS (counts) — hard gates
- the QuantReg tau is the quantile in (0,1) of the pinball loss (default 0.5=the median); it is NOT a significance level
- QuantReg calibration: the constant conditional-quantile LEVEL = .offset + .intercept; .offset is ALWAYS the median of y (it does NOT depend on tau) — the tau dependence lives in .intercept (a movable base learner via the formula interface); take the calibrated fitted quantile from the .model handle (it needs a large enough mstop for P(y<=fitted)→tau)
- Binomial: .coefficients are HALF the glm(binomial) ones (mboost: f=0.5*logit) — multiply by 2 for the logistic scale before interpretation/odds ratios; the positive class = .positive_class (the 2nd factor level); see .coef_scale

### References

- Bühlmann P., Hothorn T. (2007) 'Boosting Algorithms: Regularization, Prediction and Model Fitting' Statistical Science 22(4) 477-505 [component-wise functional gradient descent]
- Hofner B., Mayr A., Robinzonov N., Schmid M. (2014) 'Model-based Boosting in the reference: A Hands-on Tutorial Using the reference Package mboost' Computational Statistics 29 3-35
- Hothorn T. et al. (2010) 'Model-based Boosting 2.0' JMLR 11 2109-2113 [the mboost architecture, cvrisk, Family objects]
- mboost v2.9-12 ref manual — glmboost, boost_control, cvrisk, cv, Gaussian/QuantReg/Binomial/Poisson/Laplace/Huber, mstop/selected/risk (live-verified)
- wrapper footer IMPLEMENTATION NOTE (c20_highdim_shrinkage_ml/component_wise_gradient)

## #219 — Bayesian Model Averaging (BMA, g-priors: enumeration + MCMC)

**Module:** `bayesian_averaging.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bma_average` | `X_data` | `matrix_handle`, `enum`, `string`, `enum`, `integer`, `integer`, `integer`, `number`, `integer` | `nmodel=100`, `burn=1000`, `iter=3000`, `seed=42` | `mcmc` | `bma` |
| `bma_coefficients` | `object` | `raw_handle`, `boolean`, `boolean` | `exact=False`, `order_by_pip=True` | `light` | — |

### Use when

model uncertainty in a LINEAR regression with many candidate regressors (a small to moderate K); you want Posterior Inclusion Probabilities (which regressors matter), model-averaged coefficients & sign certainty without choosing ONE model (growth/determinants regressions, Sala-i-Martin BACE style)

### Do not use when

a very large K (>~30-40) with a sparsity objective → penalized shrinkage (glmnet lasso/elastic-net, grpreg); pure prediction without inference → the ML nodes (ranger/mboost); a time series with lags/SV → Bayesian VAR shrinkage (bvar/bayesianVARs, cat 03/14); non-linear interactions → RF/BART

### Alternatives

| instead use | when |
| --- | --- |
| mcmc=enumerate | K<=20 → an EXACT enumeration of all 2^K models (deterministic, exact PMP); prefer it whenever feasible |
| mcmc=bd / rev.jump (MCMC) | K>20 → model sampling; CHECK corr_pmp>=~0.9 (convergence) & the seed for reproducibility |
| g=UIP vs BRIC/RIC/HQ or a custom number | UIP (g=N) is a balanced default; BRIC/RIC (g=max(N,K^2)/K^2) are more conservative (a larger penalty); run a sensitivity check — the PIP depend on g (the Bartlett/Lindley paradox) |
| mprior=random (the Ley-Steel beta-binomial prior) | robustness with respect to the prior model size rather than a fixed inclusion probability of 0.5 (uniform) |
| penalized shrinkage (glmnet/grpreg, cat 20) or spike-and-slab/SSVS (the Bayesian VAR nodes) | a very large K + sparsity (a point estimate); or a time-series/VAR context |

### Output fields

- pip: the named PIP per regressor ∈[0,1] — the posterior probability that the regressor belongs in the model
- coefficients: a data_frame term/idx/pip/post_mean/post_sd/cond_pos_sign/post_sign_prob (model-averaged, UNCONDITIONAL)
- post_sign_prob: the sign certainty = P(the coefficient has the sign of post_mean) — the robustness of the sign
- top_models: the PMP (exact vs mcmc) + the inclusion binary matrix + pmp_exact_share (the probability normalized within the retained set)
- best_model: the highest-PMP model (included_terms, n_regressors, pmp_exact_share)
- corr_pmp / corr_pmp_ok: the MCMC convergence diagnostic (the analytical-vs-frequency PMP correlation); NA under enumerate
- n_models_visited / modelspace(2^K) / pct_topmodels: the number of draws, the size of the space, the % of posterior mass in the top models
- mean_n_regressors (=the sum of the PIP, the posterior E[#regressors]), shrinkage_av, K, N
- bma: the raw S3 bma fit (to_mcp → a stub; a register handle for chaining into bma_coefficients)

### Pitfalls

- a PIP is not a p-value: under a uniform prior the prior-neutral point is 0.5; PIP>0.5 = 'supported'; the scale depends on mprior
- post_mean/post_sd are UNCONDITIONAL (averaged over ALL models, including those that exclude the regressor) → a low PIP ⇒ a post_mean shrunk towards 0; it is NOT the conditional effect (use condi.coef for that)
- pmp_exact/pmp_mcmc (pmp.bma) are RAW marginal-likelihood weights — they do NOT sum to 1 over the retained set; the probability interpretation is pmp_exact_share
- g-prior SENSITIVITY: a large g → less shrinkage but a stronger 'null penalty' (g→∞ ⇒ PIP→0, the Bartlett-Lindley paradox); UIP/BRIC/RIC give different PIP → a sensitivity check is mandatory
- enumerate = exact PMP, deterministic (no seed); MCMC = CHECK corr_pmp>=~0.9 BEFORE trusting the PIP (a low value ⇒ a non-converged sampler, raise iter/burn; the corr_pmp_ok flag)
- NA/Inf in X.data → a HARD STOP: bms silently drops NA rows (only a warning) → a silently wrong sample
- the 1st column of X.data is the dependent variable y (NOT a regressor); the wrong column order ⇒ the wrong model
- mcmc='bd'/'rev.jump' is a stochastic MCMC sampler and is NOT bit-reproducible even with a fixed seed — do not rely on run-to-run identity or on input-hash cache reuse==recompute; for an EXACTLY deterministic result use mcmc='enumerate' when K<=20 (see output.deterministic/.reproducibility)
- pmp_exact & pmp_mcmc are NORMALIZED posterior model probabilities in [0,1] that sum to 1; under enumerate they coincide (analytical), under MCMC they differ (analytical vs sampling frequency); their correlation = corr_pmp (the convergence diagnostic)

### References

- Zeugner & Feldkircher 2015 'Bayesian Model Averaging Employing Fixed and Flexible Priors: The BMS Package for the reference' JSS 68(4)
- Fernández, Ley & Steel 2001 'Benchmark priors for Bayesian model averaging' J. Econometrics 100(2) 381-427 (the g-priors UIP/BRIC/RIC/HQ)
- Sala-i-Martin, Doppelhofer & Miller 2004 'Determinants of Long-Term Growth: A BACE Approach' AER 94(4) 813-835
- Ley & Steel 2009 'On the effect of prior assumptions in BMA' J. Applied Econometrics 24(4) 651-674 (the random model prior)
- BMS v0.3.5 ref manual — the bms/coef.bma/pmp.bma/topmodels.bma help pages ( wrapper footer IMPLEMENTATION NOTE (c20_highdim_shrinkage_ml/bayesian_averaging)

## #220 — Grouped / bi-level penalized regression (group lasso, group MCP/SCAD, gel/cMCP)

**Module:** `grouped_level_penalized.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `group_penalized_regression` | `X`, `y` | `matrix_handle`, `matrix_handle`, `int_array`, `enum`, `enum`, `integer`, `number`, `number` | `nlambda=100`, `alpha=1` | `light` | — |
| `cv_group_penalized_regression` | `X`, `y` | `matrix_handle`, `matrix_handle`, `int_array`, `enum`, `enum`, `integer`, `integer`, `integer`, `number`, `number` | `nfolds=10`, `seed=20240720`, `nlambda=100`, `alpha=1` | `light` | — |

### Use when

a high-dimensional regression where the regressors come in KNOWN GROUPS (lags of the same variable, the dummies of one categorical variable, indicators per sector) and you want sparse selection at the GROUP level; grLasso/grMCP/grSCAD select whole groups, gel/cMCP select bi-level (groups AND variables within a group); cv.grpreg gives the data-driven lambda.min

### Do not use when

no natural grouping of the columns → a plain lasso/elastic-net (glmnet, cat. 20); you want oracle-fair post-selection inference → a separate inference node; a survival outcome (grpsurv is scoped out); you want a conditional tail/GaR → quantreg (#64); a low dimension p<<n without sparsity → OLS/GLM

### Alternatives

| instead use | when |
| --- | --- |
| penalty=grLasso (the Yuan-Lin group lasso) | you want convex, stable all-or-nothing selection of a whole group; the default, less biased for large coefficients than MCP but with more shrinkage |
| penalty=grMCP / grSCAD | you want nearly unbiased large coefficients (a nonconvex group penalty); grSCAD defaults to gamma=4, grMCP to gamma=3 |
| penalty=gel / cMCP (bi-level) | you want sparsity BOTH BETWEEN groups AND WITHIN a group (not all-or-nothing) — only some variables inside a selected group are kept |
| glmnet lasso/elastic-net (cat. 20) | the columns have NO natural grouping; you want individual-variable sparsity |
| quantreg GaR (#64) | you want a conditional tail (Growth-at-Risk) rather than a mean regression with group sparsity |

### Output fields

- cv_curve: a data_frame lambda/cve/cvse/cvlo/cvup (the CV curve; cvlo/cvup = cve -/+ cvse)
- lambda_min / min_index / cve_min: the CV-optimal lambda, its position, the minimum cross-validation error
- coefficients: a data_frame term/coefficient at lambda.min (the intercept + p columns, in the order of X)
- selected_groups: the SELECTED (non-zero) groups at lambda.min — from predict(type='groups'), not a manual threshold
- selected_members: a data_frame variable/group of the members of the selected groups; n_nonzero_groups / n_nonzero_vars
- path (grpreg): a data_frame step/lambda/df/deviance (a DECREASING lambda); group_structure variable/group; group_multiplier
- object: the raw grpreg/cv.grpreg fit (a list-based S3 → a to_mcp stub)

### Pitfalls

- grpreg is DETERMINISTIC (coordinate descent, no RNG); ONLY cv.grpreg is stochastic (the random fold assignment) → the seed defaults to 20240720; the same seed → an identical lambda.min/cve, a different seed → a different one (live-verified with identical)
- group=all-or-nothing: grLasso/grMCP/grSCAD zero out a WHOLE group together; gel/cMCP allow partial selection within a group — do not confuse them
- the selected groups come from predict(type='groups')/predict(type='vars') (authoritative); do NOT threshold the coefficients by hand (there are small nonzeros along the MCP/SCAD path)
- a group value of 0 = an UNPENALIZED/always-in group (unpenalized covariates); it does not count towards n_groups — it is not a wrong label
- gel/cMCP return an UNNAMED group.multiplier (grLasso/grMCP/grSCAD name it) — the wrapper adds fallback labels from the non-zero groups
- family='binomial' requires a BINARY {0,1} y (grpreg: a 'non-binary data' error); family='poisson' rejects negative y — hard gates
- lambda is DECREASING (the first value = the most penalized/largest lambda, the last = the smallest); nfolds must satisfy 3<=nfolds<=n

### References

- Yuan & Lin 2006 'Model selection and estimation in regression with grouped variables' JRSS-B 68(1) 49-67 [the group lasso]
- Breheny & Huang 2015 'Group descent algorithms for nonconvex penalized linear and logistic regression models with grouped predictors' Statistics and Computing 25 173-187 [the grpreg algorithm, grMCP/grSCAD]
- Breheny & Huang 2009 'Penalized methods for bi-level variable selection' Statistics and its Interface 2 369-380 [cMCP/gel bi-level]
- Huang, Breheny & Ma 2012 'A selective review of group selection in high-dimensional models' Statistical Science 27(4) 481-499
- grpreg v3.6.0 ref manual — grpreg, cv.grpreg, the predict/coef methods (args/values live-verified)
- wrapper footer IMPLEMENTATION NOTE (c20_highdim_shrinkage_ml/grouped_level_penalized)
