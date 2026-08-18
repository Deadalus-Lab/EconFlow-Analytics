<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 08-panel-data

5 METHOD-SELECTION cards, 4 modules, 20 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #46 — Static panel estimators (FE/RE/pooling/between/FD) + Hausman/LM/F

**Module:** `static_panel_estimators.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pd_fit` | `formula`, `data` | `formula`, `df_handle`, `enum`, `enum` | — | `light` | `object` |
| `pd_hausman_test` | `x`, `data` | `formula`, `df_handle`, `enum`, `enum` | — | `light` | — |
| `pd_poolability_test` | `x`, `data` | `formula`, `df_handle`, `enum`, `enum` | — | `light` | — |
| `pd_effects_ftest` | `x`, `data` | `formula`, `df_handle`, `enum` | — | `light` | — |
| `pd_fixed_effects` | `object` | `raw_handle`, `enum` | — | `light` | — |
| `pd_random_effects` | `object` | `raw_handle` | — | `light` | — |

### Use when

a panel (i,t); estimating one equation with a test for unit/time effects (within/random/pooling/between/fd)

### Do not use when

a lagged dependent variable on the RHS (Nickell bias -> #47 GMM); small-N/large-T; panel unit-root/cointegration (01/other categories)

### Prerequisites

- pd_hausman_test (FE vs RE: reject H0 -> FE)
- pd_poolability_test (LM Breusch-Pagan: are there effects?)
- pd_effects_ftest (F within vs pooling)
- c01_preparation_prechecks/panel_unit_root.run_purtest (macro/large-T only: panel unit root first)

### Alternatives

| instead use | when |
| --- | --- |
| #47 pd_gmm_fit | a dynamic panel / endogenous regressors |
| brms panel (category 14) | hierarchical shrinkage / non-gaussian / a full posterior |
| model=between | the cross-sectional long-run relation only |

### Output fields

- coefficients: named vector of regressor effects (within = within-unit)
- coef_table: Estimate/SE/t/p — the SE correspond to the vcov that was supplied
- vcov: ALWAYS non-robust; rvcov: the actual robust one (NULL if it was not requested)
- ercomp: RE variance components + theta (theta->0 ~pooling, ->1 ~FE); NULL elsewhere
- hausman_test/lm_test/f_test: htest {statistic,p_value,parameter,method}

### Pitfalls

- robust inference: read the SE from rvcov/coef_table, NOT from vcov (always non-robust)
- FE vs RE is a Hausman test, not an assumption; reject -> FE
- the within R² is measured in the transformed space — not comparable with the pooling R²
- pd_fixed_effects only for within, pd_random_effects only for random (explicit gates)
- panelmodel-interface tests: a pgmm object is deliberately blocked (otherwise LAPACK singular)

### References

- Croissant & Millo, plm JSS 2008 vignette ( plm)
- help('plm','plm'), phtest, plmtest, pFtest, fixef.plm, ranef.plm
- Hausman 1978 (Econometrica 46:1251)
- Baltagi 2013 Econometric Analysis of Panel Data 5th ed. §4.3
- Wooldridge 2010 §10.7 (regression-based Hausman)

## #47 — Dynamic panel GMM (Arellano-Bond difference / Blundell-Bond system)

**Module:** `static_panel_estimators.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pd_gmm_fit` | `formula`, `data` | `formula`, `df_handle`, `enum`, `enum`, `enum` | — | `light` | `object` |
| `pd_gmm_autocorr_test` | `object` | `raw_handle`, `integer` | `order=1` | `light` | — |
| `pd_gmm_sargan_test` | `object` | `raw_handle`, `enum` | — | `light` | — |

### Use when

a dynamic panel (lagged dependent / endogenous regressors), large-N small-T; diff-GMM (transformation=d) or system-GMM (ld)

### Do not use when

static, without a lagged dependent variable -> #46; small-N/large-T; instrument proliferation (Sargan p~1)

### Prerequisites

- pd_gmm_autocorr_test (post: AR(2)/m2 MUST NOT be rejected)
- pd_gmm_sargan_test (post: overidentification, H0 valid instruments)

### Alternatives

| instead use | when |
| --- | --- |
| #46 FE | T is large (Nickell bias negligible) or there is no lagged dependent variable |
| transformation=ld (system GMM) | a persistent/near-unit-root dependent variable (weak instruments in the differences) |
| Bayesian panel VAR (bvartools/14) | joint dynamics of many equations |

### Output fields

- coefficients: named; the lag(y) coefficient = persistence (must be <1)
- coef_table: Estimate/SE/z/p — robust=TRUE twosteps -> Windmeijer-corrected SE
- sargan_test: htest of overidentification, H0 = instruments valid (you want a large p)
- autocorr_test1/autocorr_test2: htest m1/m2 Arellano-Bond serial correlation
- residuals: a list per individual (not a flat vector); fitted: numeric

### Pitfalls

- Sargan: a large p is good (valid); p~1.00 = instrument proliferation (use collapse=TRUE)
- m1/AR(1) is expected to be significant (normal, due to differencing) — NOT a problem
- m2/AR(2) must NOT be rejected; rejection -> the moment conditions are invalid
- twosteps SE without Windmeijer (robust=FALSE) are severely downward-biased
- the df_residual of the documentation does not exist in the object (plm 2.6.7) — it is not exposed

### References

- help('plm','pgmm') ( plm)
- Arellano & Bond 1991 (Review of Economic Studies 58:277)
- Blundell & Bond 1998 (J. Econometrics 87:115)
- Windmeijer 2005 (J. Econometrics 126:25)
- Roodman 2009 (Stata Journal 9:86, instrument proliferation/collapse)

## #173 — Fixed-Effects Individual-Slopes (FEIS) + a slope-heterogeneity Hausman test (artificial & bootstrapped)

**Module:** `fixed_effects_individual.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `feis_fit` | `formula`, `data`, `id` | `formula`, `df_handle`, `string`, `boolean`, `boolean`, `boolean` | `robust=False`, `intercept=False`, `dropgroups=False` | `light` | `object` |
| `feis_test` | `object` | `raw_handle`, `enum`, `boolean`, `raw` | `robust=False` | `light` | — |
| `feis_bstest` | `object` | `raw_handle`, `enum`, `integer`, `integer`, `raw` | `rep=500`, `seed=2025` | `light` | — |
| `feis_slopes` | `object` | `raw_handle` | — | `light` | — |

### Use when

a panel (i,t) where the effect of a trend/slope variable (e.g. time/experience) differs by unit; you want consistency even when the unit-specific slope is correlated with the regressors (detrending instead of demeaning)

### Do not use when

no theoretical slope heterogeneity (conventional FE #46 suffices); fewer than q+1 observations per unit (q=the number of slope parameters); a dynamic panel / lagged dependent variable (Nickell -> #47 GMM); time-invariant regressors of interest (detrending removes them)

### Prerequisites

- feis_test (a regression-based Hausman test: rejecting art1 -> FEIS over FE)
- feis_bstest (the bootstrapped Hausman test; more reliable at small N)
- c08_panel_data/static_panel_estimators.pd_hausman_test (the classic FE vs RE test before considering slope heterogeneity)

### Alternatives

| instead use | when |
| --- | --- |
| #46 pd_fit (model=within) | no slope heterogeneity; feis_test art1 does not reject |
| #47 pd_gmm_fit | a dynamic panel / endogenous regressors |
| brms random slopes (category 14) | hierarchical shrinkage of the slopes / a full posterior / non-gaussian |

### Output fields

- coefficients: a named vector of regressor effects in the detrended space
- coef_table: Estimate/Std. Error/t-value/Pr(>\|t\|); the SE are robust if robust=TRUE (vcov_arg records it)
- slopevars: the slope variables (the RHS of '\|'); r2/adj.r2 in the detrended space; n_groups after dropping units with <q+1 observations
- feis_test/feis_bstest: art_feis_vs_fe/art_fe_vs_re/art_feis_vs_re = {chi2, df, p_value}; those not requested are NULL
- feis_slopes.slopes: an N x J matrix of alpha_i (rownames=ids); it includes the (Intercept)

### Pitfalls

- the coefficients/r2 are in the DETRENDED space — not directly comparable with within/pooling FE
- art1 (FEIS vs FE) rejection -> the slope heterogeneity matters; do NOT fall back to conventional FE
- feis silently drops units with <q+1 observations (a warning); check n_groups against the original N
- time-invariant regressors vanish under the detrending — they are not estimated here
- feis_bstest is STOCHASTIC (a pairs-cluster bootstrap); the same seed -> the same p (seed=2025 by default); a low number of reps gives a noisy p
- feis_test/feis_bstest return NULL for the components outside the selected type (art1/bs1 -> only art_feis_vs_fe)

### References

- Ruettenauer & Ludwig 2020, Sociological Methods & Research (FEIS), doi:10.1177/0049124120926211
- Bruederl & Ludwig 2015, Sage Handbook of Regression Analysis §Fixed-Effects Panel Regression
- Wooldridge 2010 Econometric Analysis of Cross Section and Panel Data 2nd ed. §10.7 (regression-based Hausman), §11 (heterogeneous slopes)
- Mundlak 1978 (Econometrica 46:69) — the CRE specification behind feistest
- help('feis','feisr'), feistest, bsfeistest, slopes (feisr 1.3.1 )

## #174 — Beck-Katz Panel-Corrected Standard Errors (PCSE) for pooled TSCS/OLS

**Module:** `beck_katz_panel.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pcse_fit` | `formula`, `data`, `groupN`, `groupT` | `formula`, `df_handle`, `string`, `string`, `boolean` | `pairwise=False` | `light` | `object` |
| `pcse_vcov` | `object`, `groupN`, `groupT` | `raw_handle`, `num_array`, `num_array`, `boolean` | `pairwise=False` | `light` | `object` |
| `pcse_summary` | `object` | `raw_handle` | — | `light` | — |

### Use when

pooled OLS on time-series cross-section data (N units × T periods, with T not << N); you want SE robust to panel heteroskedasticity + contemporaneous (cross-unit) correlation, keeping the OLS coefficients

### Do not use when

a lagged dependent variable / endogeneity (Nickell bias -> #47 GMM); within/random effects (#46); an N >> T micro panel (prefer clustered/Driscoll-Kraay); serial correlation as the main problem (Prais-Winsten/Newey-West)

### Prerequisites

- pcse_fit (it produces the pcse object; all it needs is formula+data+index)
- c01_preparation_prechecks/panel_unit_root.run_purtest (a panel unit-root test for a large-T macro panel before pooled OLS)

### Alternatives

| instead use | when |
| --- | --- |
| #46 pd_fit (within/random) | unit-specific effects correlated/uncorrelated with the regressors — FE/RE instead of pooling |
| plm vcovSCC (Driscoll-Kraay) | N >> T or strong cross-sectional dependence with a large N |
| plm vcovBK | Beck-Katz PCSE inside a plm panelmodel rather than a pooled lm |

### Output fields

- coefficients: a named vector of OLS coefficients (they do NOT change under the PCSE correction)
- coef_table: Estimate/PCSE/t value/Pr(>\|t\|) — the SE are panel-corrected
- pcse: a named vector of the panel-corrected SE; vcov: the full PCSE covariance matrix
- df/nobs/nmiss: degrees of freedom, valid observations, missing panel cells
- pairwise: TRUE=pairwise / FALSE=casewise; balanced: (nmiss==0)

### Pitfalls

- PCSE corrects ONLY the SE — the coefficients remain pooled OLS (non-robust point estimates)
- casewise (pairwise=FALSE) uses only the balanced rectangle; on a heavily unbalanced panel set pairwise=TRUE
- pairwise=NA runs silently wrong in pcse — the wrapper blocks it explicitly
- Beck-Katz assumes T is not << N; with N >> T the PCSE are unreliable -> Driscoll-Kraay/clustered
- vcov = the PCSE covariance (NOT the classical OLS vcov); read the inference from coef_table/pcse
- NA in the model/index columns drop rows inside lm -> a length mismatch; the wrapper requires complete cases

### References

- Beck & Katz 1995, 'What to Do (and Not to Do) with Time-Series Cross-Section Data', APSR 89(3):634-647
- Beck 2001, Annual Review of Political Science 4:271-293 (TSCS practice)

## #175 — Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling)

**Module:** `hierarchical_multilevel_linear.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `lme_lmer` | `formula`, `data` | `formula`, `df_handle`, `boolean` | `REML=True` | `light` | `object` |
| `lme_glmer` | `formula`, `data` | `formula`, `df_handle`, `enum`, `integer` | `nAGQ=1` | `light` | `object` |
| `lme_ranef` | `object` | `raw_handle`, `boolean` | `condVar=True` | `light` | — |
| `lme_varcorr` | `object` | `raw_handle` | — | `light` | — |

### Use when

hierarchical/nested data (e.g. regions within countries, years within units); you want partial pooling — random intercepts/slopes per group with shrinkage — instead of full pooling or entirely separate models per group

### Do not use when

the group effects are correlated with the regressors (endogeneity -> FE/within #46); a lagged dependent variable on the RHS (Nickell bias -> #47 GMM); a single hierarchical level with no repeated sampling; you want a full Bayesian posterior/priors (-> brms, category 14)

### Prerequisites

- lme_lmer (a linear response; register the model handle for ranef/varcorr)
- lme_glmer (a non-gaussian response: binomial/poisson/Gamma/inverse.gaussian)
- c08_panel_data/static_panel_estimators.pd_fit (comparison: FE/within when the effects are endogenous)

### Alternatives

| instead use | when |
| --- | --- |
| #46 pd_fit (within/FE) | the individual effects are correlated with the regressors -> partial pooling causes bias, use FE |
| #46 pd_fit (random) | one level, linear, a panel (i,t); GLS variance components suffice without the full mixed-model machinery |
| brms (category 14) | you want priors / a full posterior / a more complex likelihood, or hierarchical shrinkage with uncertainty quantification |

### Output fields

- fixef: a named vector of population-level (fixed) coefficients
- coef_table: Estimate/Std.Error/t (lmer) or +z/Pr(>\|z\|) (glmer) — NOTE: lmer gives NO p-value by design
- varcorr: tidy records {grp,var1,var2,vcov,sdcor} — the variance/covariance/correlation of the random effects
- sigma: the residual scale (== attr(VarCorr,'sc')); ngrps: the number of groups per grouping factor; nobs
- ranef: records {grpvar,term,grp,condval,condsd} — the BLUPs (shrunk group deviations) + the conditional SD
- log_lik/AIC/BIC: model fit (AIC/BIC are comparable only ML-vs-ML; REML likelihoods are NOT comparable across different fixed effects)
- singular (the logical isSingular)/converged (logical)/conv_messages (char): they record degeneracy & convergence IN THE SAME output — under a stateless node contract stderr is lost, so check these instead of relying on warnings

### Pitfalls

- REML=TRUE likelihoods are NOT comparable across models with different fixed effects — for an LRT/AIC on the fixed effects set REML=FALSE (ML)
- lme4 returns NO p-values for lmer (no default df) — coef_table has only the t value; significance is judged with a CI/LRT, not from a non-existent p
- ranef are conditional modes (BLUPs), NOT parameters — they are shrunk towards 0; do NOT read them as separate fixed effects per group
- a 'boundary (singular) fit' (the group sd → 0) means the random effect is not supported by the data (too few groups / zero between-group variance); the wrapper records it explicitly as singular=TRUE (do not ignore it — the variance components are degenerate)
- partial pooling presupposes random effects UNCORRELATED with the regressors (as in RE/Hausman) — otherwise prefer within/FE (#46)
- family (glmer) = a closed set through match.arg; gaussian is NOT allowed (use lme_lmer)

### References

- Bates, Mächler, Bolker & Walker, 'Fitting Linear Mixed-Effects Models Using lme4', JSS 2015 67(1)
- help('lmer','lme4'), help('glmer','lme4'), ranef.merMod, fixef.merMod, VarCorr.merMod
- Gelman & Hill 2007, Data Analysis Using Regression and Multilevel/Hierarchical Models
- Pinheiro & Bates 2000, Mixed-Effects Models in S and S-PLUS (BLUP/partial pooling)
