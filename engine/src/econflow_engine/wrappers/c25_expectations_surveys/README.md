<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 25-expectations-surveys

4 METHOD-SELECTION cards, 4 modules, 16 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #231 — Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression approach, conditional expectations

**Module:** `quantifying_qualitative_survey.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `qn_balance` | `data`, `forecast_horizon` | `df_handle`, `integer`, `integer`, `integer`, `number`, `boolean` | `suppress_warnings=False` | `light` | — |
| `qn_carlson_parkin` | `data`, `forecast_horizon` | `df_handle`, `integer`, `integer`, `integer`, `enum`, `number`, `num_array`, `num_array`, `num_array`, `boolean`, `number`, `number`, `enum`, `number`, `number`, `number`, `number`, `number`, `boolean` | `correct_zero=True`, `correct_by=0.01`, `suppress_warnings=False` | `light` | — |
| `qn_regression` | `data`, `forecast_horizon` | `df_handle`, `integer`, `integer`, `integer`, `enum`, `number`, `number`, `number`, `number`, `number`, `number`, `enum`, `boolean` | `suppress_warnings=False` | `light` | — |
| `qn_conditional_expectations` | `data`, `forecast_horizon` | `df_handle`, `integer`, `integer`, `integer`, `enum`, `integer`, `integer`, `integer`, `enum`, `boolean` | `mov_horizon_length=10`, `fix_horizon_start=1`, `fix_horizon_end=10`, `suppress_warnings=False` | `light` | — |

### Use when

you have a QUALITATIVE expectations survey (the shares/counts of respondents expecting a rise/no change/a fall in a macro variable y, typically inflation) + the ACTUAL series y, and you want a NUMERIC series of quantified expectations for downstream analysis/charts

### Do not use when

QUANTITATIVE expectations that are already numeric (SPF/consumer point forecasts) -> analyse them directly; density/fan-chart forecasts -> #12 distribution-risk; anchoring/disagreement regressions -> lm/fixest; data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| qn_balance (Batchelor 1984) | you want the simplest indicator: a scaling of the balance (up-down) with theta calibrated to the actual change in y; minimal distributional assumptions |
| qn_carlson_parkin (Carlson-Parkin 1975) | you want the probability method with indifference limens; the options limen_type (carlson.parkin/weber.fechner/constant/symm.series/asymm.series) & distrib_type (normal/logistic/t) |
| qn_regression (Pesaran 1984) | you want time-invariant ASYMMETRIC upper/lower limens estimated by OLS + a symmetry test (White or small.sample HC SE) |
| qn_conditional_expectations (Zuckarelli 2015) | you want a method with NO assumption of symmetric/parametric limens: expectations built on the empirical distribution of past realizations (a moving/fixed experience horizon) |

### Output fields

- qn_balance: y_e_mean_abs / y_e_mean_perc (chart-data: the quantified expectation in levels, the abs & the perc version) + delta_y_e_mean/sd_abs/perc + theta_abs/theta_perc (the scaling) + nob/mae/rmse
- qn_carlson_parkin: y_e_mean_abs/perc (chart-data) + limen_abs/limen_perc (the indifference limen per period) + delta_y_e_* + nob/mae/rmse + the limen_type/distrib_type echo
- qn_regression: y_e_mean_abs/perc (chart-data) + upper_limen_abs/lower_limen_abs (+perc) + symmetry_abs/symmetry_perc (the p-value of the symmetry test) + nob/mae/rmse
- qn_conditional_expectations: y_e (chart-data: the quantified expectation, full length with NA outside the window) + nob/mae/rmse + the exp_horizon_type/distrib_param echo
- all of them: the forecast_horizon/first_period/last_period echo of the period window

### Pitfalls

- abs vs perc: each of bal/cp/ra gives TWO versions — expectations of the ABSOLUTE change (y_e_mean_abs) vs of the PERCENTAGE change (y_e_mean_perc); choose according to whether the question concerns a level or a rate
- y_e is full-length and aligned to the input (NA outside [first_period, last_period]); nob counts only the quantified periods — do not confuse length(y_e) with nob
- shares must be NON-NEGATIVE: the package SILENTLY accepts negative shares and produces plausible-but-wrong output (the bal theta was inflated) -> a hard gate up/same/down>=0; they need not sum to 100 ('Don't know' is allowed)
- cp does NOT need first_period>forecast_horizon (source-verified: cp calibrates against the FUTURE change y[t+h] vs y[t]); the ONLY constraint is last_period+forecast_horizon<=n
- ce degeneracy: if the experience/period window is too short, ce SILENTLY returns nob=0 or an all-NA y.e (the fix: fix_horizon_end must reach ~first_period-1); a post-check gate blocks it; an even shorter window -> an internal error
- the DISTRIBUTION root: cp/ra with distrib_type=t need distrib_t_df>0; the default t.df=(last-first); logistic uses a location/scale, normal a mean/sd
- DETERMINISM: analytic/OLS methods, NO RNG (identical verified) -> no seed

### References

- quantification v0.2.0 ref manual (the bal/cp/ra/ce help pages, arguments + value fields str-verified live)
- Batchelor, R.A. (1984) 'Quantitative vs. qualitative measures of inflation expectations' Oxford Bulletin of Economics and Statistics 48(2) 99-120 (the balance approach)
- Carlson, J.A. & Parkin, M. (1975) 'Inflation expectations' Economica 42, 123-138 (the Carlson-Parkin probability method)
- Henzel, S. & Wollmershaeuser, T. (2005) 'Quantifying inflation expectations with the Carlson-Parkin method' Journal of Business Cycle Measurement and Analysis 2, 321-352 (the Weber-Fechner limen)
- Nardo, M. (2003) 'The quantification of qualitative survey data: a critical assessment' Journal of Economic Surveys 17(5) 645-668 (the zero-share correction)
- Pesaran, M. (1984) 'Expectations formation and macroeconomic modelling' in Contemporary macroeconomic modelling, 27-55 (the regression approach)
- MacKinnon, J.G. & White, H. (1985) 'Some heteroskedasticity-consistent covariance matrix estimators' Journal of Econometrics 29, 305-325 (the symmetry-test SE)
- Zuckarelli, J. (2015) 'A new method for quantification of qualitative expectations' Economics and Business Letters 3(5) 123-128 (conditional expectations)
- wrapper footer IMPLEMENTATION NOTE (c25_expectations_surveys/quantifying_qualitative_survey)

## #232 — Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design variances (stratification, clustering, weights, fpc)

**Module:** `design_complex_survey.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sv_svydesign` | `df` | `df_handle`, `series_codes`, `series_codes`, `series_codes`, `series_codes`, `series_codes`, `boolean` | `ids='1'`, `nest=False` | `light` | `design` |
| `sv_svymean` | `design`, `vars` | `raw_handle`, `series_codes`, `boolean`, `boolean` | `deff=True`, `na_rm=False` | `light` | — |
| `sv_svytotal` | `design`, `vars` | `raw_handle`, `series_codes`, `boolean`, `boolean` | `deff=True`, `na_rm=False` | `light` | — |
| `sv_svyquantile` | `design`, `vars` | `raw_handle`, `series_codes`, `num_array`, `boolean` | `na_rm=False` | `light` | — |
| `sv_svyby` | `design`, `vars`, `by` | `raw_handle`, `series_codes`, `series_codes`, `enum`, `boolean`, `boolean` | `deff=False`, `na_rm=False` | `light` | — |

### Use when

estimating means/totals/quantiles/domains from survey microdata (expectation/consumer/business tendency surveys, e.g. Michigan, the ECB SPF) where the sampling DESIGN (strata/clusters/weights/fpc) must enter the variance; the naive s²/n understates it (clustering) or ignores the sampling weights -> a wrong CI

### Do not use when

informal/equally weighted data with no design (a plain mean/quantile); a regression on a survey design (svyglm — a future node); calibration/post-stratification/raking or a replicate-weights bootstrap (as.svrepdesign — a different family); estimating factor proportions (svymean(~factor) — it changes the output shape); time series/aggregate data (not microdata); quantification tendency surveys (#233) or small-area estimation (#234)

### Alternatives

| instead use | when |
| --- | --- |
| sv_svydesign (the PRODUCER -> register the design) | ALWAYS FIRST: declare the complex-survey design from a df_handle + column names (ids/strata/weights/probs/fpc); ids='1' => no clusters; it returns a raw_handle that feeds the consumers |
| sv_svymean | you want the design-based weighted MEAN of numeric variables + a correct SE/CI/cv/deff |
| sv_svytotal | you want an estimate of a population TOTAL (a weighted sum) + a design SE |
| sv_svyquantile | you want weighted QUANTILES (the median etc.) with a design CI/SE; the quantiles must lie strictly in (0,1) |
| sv_svyby | you want an estimate per DOMAIN/subgroup (a mean or a total per level of a grouping variable) with a correct design SE per domain |

### Output fields

- sv_svydesign: design (register -> a raw_handle) + metadata (n_obs, n_variables, numeric_vars, n_strata, has_strata/has_fpc/has_clusters, weighted, weight_min/max/mean/total = a summary of the design weights 1/prob)
- sv_svymean/sv_svytotal: an estimates df {variable, estimate, SE, cv, ci_lower, ci_upper[, deff]} + coefficients + SE + vcov (a matrix with dimnames) + statistic('mean'/'total') + the raw fit (to_mcp -> a stub)
- sv_svyquantile: an estimates df {variable, quantile, estimate, SE, ci_lower, ci_upper} (newsvyquantile: a matrix per variable, with columns quantile/ci.2.5/ci.97.5/se) + n_quantiles
- sv_svyby: an estimates df (records per domain, with the columns produced by svyby: the grouping + estimate + se) + n_groups + group_levels + statistic

### Pitfalls

- deff (the design effect) = Var_design/Var_SRS; >1 => clustering/unequal weighting INCREASES the variance relative to an SRS of the same n; the deff column appears ONLY when deff=TRUE
- weights AND probs are mutually exclusive (probs = 1/weights); with neither => an equally weighted SRS (weight_min==weight_max); non-positive weights -> a hard gate (invalid estimates)
- nest=TRUE applies ONLY when the cluster ids are reused within strata (relabelling per stratum); otherwise the strata are wrong
- svyquantile (survey 4.5 'newsvyquantile'): a list per variable, matrix columns {quantile, ci.2.5, ci.97.5, se}, rownames=the probs; quantiles of 0/1 -> infinities -> a gate (strictly (0,1)); in small samples the CI can be NaN (the linearization df) -> to_mcp maps them to null
- vars MUST be numeric: svymean(~factor) would give PROPORTIONS per level (a different output shape) -> a hard gate here (non-numeric variables are rejected)
- fpc (the finite population correction) REDUCES the SE when the sample is a large fraction of the population; NULL = with replacement (no fpc, a conservative SE)
- PURELY ANALYTIC (Horvitz-Thompson/linearization) -> no RNG/seed; identical output across two calls (a seed would be needed only for a replicate-weights bootstrap, which is out of scope)

### References

- survey v4.5 help(svydesign/svymean/svytotal/svyquantile/svyby/SE/cv/deff) (live-verified, the engine)
- Lumley 2010 'Complex Surveys: A Guide to Analysis Using the reference' (Wiley) — design-based estimation, design effects, domain estimation
- Lumley 2004 'Analysis of complex survey samples' Journal of Statistical Software 9(1) (the survey package)
- Horvitz & Thompson 1952 JASA 47:663-685 (the design-based estimator of totals)
- wrapper footer IMPLEMENTATION NOTE (c25_expectations_surveys/design_complex_survey)

## #233 — Small-area estimation (SAE): the Fay-Herriot area-level EBLUP (+ the analytic Prasad-Rao MSE) & the Battese-Harter-Fuller unit-level EBLUP

**Module:** `small_area_estimation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sae_eblup_fh` | `data`, `formula`, `vardir` | `df_handle`, `formula`, `string`, `enum`, `integer`, `number`, `integer`, `integer` | `MAXITER=100`, `PRECISION=0.0001`, `B=0`, `seed=1` | `heavy` | — |
| `sae_mse_fh` | `data`, `formula`, `vardir` | `df_handle`, `formula`, `string`, `enum`, `integer`, `number`, `integer`, `integer` | `MAXITER=100`, `PRECISION=0.0001`, `B=0`, `seed=1` | `heavy` | — |
| `sae_eblup_bhf` | `data`, `formula`, `dom`, `meanxpop`, `popnsize` | `df_handle`, `formula`, `string`, `df_handle`, `df_handle`, `raw`, `enum` | — | `light` | — |

### Use when

estimating an indicator per small area/domain (regions, age/subgroups of a survey) when the per-area sample is too small for a reliable DIRECT estimate -> 'borrowing strength' through a model of auxiliary variables + a random effect; eblupFH when you have ONLY aggregate direct estimates + their sampling variances (area level); eblupBHF when you have UNIT-level micro data + the population means of the auxiliary variables (unit level); mseFH for an analytic MSE/CV of reliability

### Do not use when

large per-area samples (the direct estimate suffices); unknown sampling variances for FH; spatial/spatio-temporal correlation between areas (eblupSFH/eblupSTFH, separate methods); non-normal/EB under a transformation (ebBHF); a plain regression with no domain structure

### Alternatives

| instead use | when |
| --- | --- |
| sae_eblup_fh (the area-level Fay-Herriot EBLUP) | you have ONE direct estimate theta_hat_i per area + its sampling VARIANCE psi_i (vardir); you want a shrinkage estimate (a point estimate) |
| sae_mse_fh (the FH EBLUP + an analytic MSE + CV%) | you want ALSO the analytic (Prasad-Rao g1+g2+g3) MSE/RMSE estimate + the CV% for reliability per area (with an optional seeded bootstrap goodness-of-fit test, B>0) |
| sae_eblup_bhf (the unit-level Battese-Harter-Fuller EBLUP) | you have UNIT-level micro data (a nested-error regression) + the population means/sizes of the auxiliary variables per area; you want the EBLUP of the area MEANS |

### Output fields

- eblup: a numeric vector of small-area estimates (chart-data); direct: the direct estimates (the model response); n_areas/n_domains
- coefficients (FH): a data_frame {beta,std_error,tvalue,pvalue}; fixed (BHF): a named beta vector
- variance components: refvar (the between-area sigma_u^2); errorvar (the within-area sigma_e^2, BHF); icc = refvar/(refvar+errorvar) (BHF); convergence/iterations/goodness (loglike/AIC/BIC/KIC, FH)
- sae_mse_fh: mse (a numeric vector; Prasad-Rao) + cv = 100*sqrt(mse)/eblup (the CV%); bootstrap = B
- sae_eblup_bhf: domain/sampsize/random(u_i)/residuals/loglike (the heavy merMod summary is deliberately removed)

### Pitfalls

- vardir is the sampling VARIANCE (SD^2), NOT the SD -> the wrong scale gives silently wrong shrinkage; the wrapper blocks vardir<0 (a hard gate) because eblupFH accepts negative values and returns an apparently valid EBLUP
- eblupBHF: if a target area is missing from meanxpop/popnsize, the package emits ONLY a warning and silently returns an NA EBLUP -> a hard gate on full coverage
- vardir/dom are NSE column-name arguments when data= is supplied (deparse(substitute)) -> they must be a column NAME (a string), not an expression/value; the wrapper copies them into fixed.sae_vardir/.sae_dom columns
- MASKING: NEVER library(sae) — its Depends on MASS/lme4(->Matrix)/nlme mask ~40 generics in the shared source env; use requireNamespace + sae:: everywhere (zero pollution of search verified live)
- the EBLUP = a shrinkage gamma_i*direct + (1-gamma_i)*regression with gamma_i = A/(A+psi_i); areas with a large psi_i (a small sample) shrink more towards the model; read the CV% per area for reliability
- seed: only the bootstrap goodness-of-fit path (B>0) in mseFH/eblupFH is stochastic; the EBLUP/analytic MSE are deterministic (identical when seeded, verified)

### References

- sae v1.3 ref manual (the eblupFH/mseFH/eblupBHF help pages)
- Molina & Marhuenda 2015 'sae: An the reference Package for Small Area Estimation' The 7(1) 81-98
- Fay & Herriot 1979 'Estimates of Income for Small Places: An Application of James-Stein Procedures to Census Data' JASA 74(366) 269-277 (area-level FH)
- Battese, Harter & Fuller 1988 'An Error-Components Model for Prediction of County Crop Areas Using Survey and Satellite Data' JASA 83(401) 28-36 (unit-level BHF)
- Prasad & Rao 1990 'The Estimation of the Mean Squared Error of Small-Area Estimators' JASA 85(409) 163-171 (the analytic MSE)
- Rao & Molina 2015 'Small Area Estimation' 2nd ed, Wiley (the textbook)
- wrapper footer IMPLEMENTATION NOTE (c25_expectations_surveys/small_area_estimation)

## #257 — Categorical association / contingency tables: a chi-squared test of independence, Fisher's exact test, nominal vs ordinal association measures with CIs

**Module:** `categorical_association_contingency.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ca_contingency` | `x`, `y` | `raw_handle`, `raw_handle`, `string`, `string`, `num_array`, `num_array`, `series_codes`, `series_codes`, `enum`, `integer`, `integer`, `number`, `boolean` | `x_name='x'`, `y_name='y'`, `na_action='fail'`, `max_levels=20`, `gate_alpha=0.05`, `ordered=True` | `light` | — |
| `ca_chisq` | `x`, `y` | `raw_handle`, `raw_handle`, `string`, `string`, `num_array`, `num_array`, `series_codes`, `series_codes`, `enum`, `integer`, `integer`, `number`, `boolean`, `number`, `enum`, `boolean`, `boolean`, `integer`, `integer` | `x_name='x'`, `y_name='y'`, `na_action='fail'`, `max_levels=20`, `gate_alpha=0.05`, `ordered=True`, `alpha=0.05`, `rule='cochran'`, `correct=True`, `simulate_p_value=False`, `B=2000`, `seed=1234` | `heavy` | — |
| `ca_fisher` | `x`, `y` | `raw_handle`, `raw_handle`, `string`, `string`, `num_array`, `num_array`, `series_codes`, `series_codes`, `enum`, `integer`, `integer`, `number`, `boolean`, `number`, `enum`, `number`, `boolean`, `integer`, `number`, `integer` | `x_name='x'`, `y_name='y'`, `na_action='fail'`, `max_levels=20`, `gate_alpha=0.05`, `ordered=True`, `alpha=0.05`, `alternative='two.sided'`, `conf_level=0.95`, `simulate_p_value=False`, `B=2000`, `workspace=200000`, `seed=1234` | `heavy` | — |
| `ca_assocs` | `x`, `y` | `raw_handle`, `raw_handle`, `string`, `string`, `num_array`, `num_array`, `series_codes`, `series_codes`, `enum`, `integer`, `integer`, `number`, `boolean`, `enum`, `number`, `enum`, `boolean` | `x_name='x'`, `y_name='y'`, `na_action='fail'`, `max_levels=20`, `gate_alpha=0.05`, `ordered=True`, `scale='nominal'`, `conf_level=0.95`, `cramer_method='ncchisq'`, `correct=False` | `light` | — |

### Use when

TWO CATEGORICAL answers PER RESPONDENT in a cross-section survey (e.g. a price expectation up/=/down x a plan for a major purchase): the contingency table + sparsity diagnostics (ca_contingency) -> an independence test (ca_chisq if Cochran's rule passes; ca_fisher if it does not) -> the SIZE of the relation with measures + CIs (ca_assocs)

### Do not use when

TIME SERIES / time-dependent data (a hard cross-section gate — see the #257 preconditions; the HAC path: sandwich, cat 07); CONTINUOUS variables (discretise first: c00_data_utilities/discretisation_numeric_column); QUANTIFICATION of survey balance/Carlson-Parkin shares -> #237 quantification; weighted survey designs (weights/strata/clusters) -> survey (svychisq); STRATIFIED / >=3-dimensional tables (mantelhaen/loglin); a CONTINUOUS vs CATEGORICAL comparison of means -> #250 tests-parametric / #251 tests-nonparametric; charts (the frontend, §5)

### Prerequisites

- ca_contingency # FIRST the table: min_expected/cochran_ok/strict_ok decide chi-squared vs Fisher
- c00_data_utilities/discretisation_numeric_column.bn_quantile_bins # a CONTINUOUS variable -> INTEGER codes BEFORE the node (bn_apply for the 2nd wave, THE SAME breaks)

### Alternatives

| instead use | when |
| --- | --- |
| ca_fisher | cochran_ok = FALSE (an expected count < 1 or >20% of the cells < 5) ⇒ an EXACT test instead of the asymptotic chi-squared; a 2x2 table ALSO gives an odds ratio + CI |
| ca_chisq(simulate_p_value = TRUE, seed) | a sparse AND large table where the exact Fisher test fails («FEXACT error 5/6/7») ⇒ a Monte-Carlo p-value (r2dtable, seeded) |
| ca_assocs(scale = 'ordinal') | the codes ENCODE AN ORDER (Likert/up-=-down) ⇒ Gamma/Kendall tau-b/Stuart tau-c/Somers' D; on a NOMINAL scale they are uninterpretable (this is NEVER guessed) |
| #250 tp_anova / #251 tn_kruskal | ONE of the variables is CONTINUOUS (a comparison of means/medians per group) rather than two categorical ones |
| svychisq (survey) | a weighted/complex sample (weights/strata/clusters) ⇒ the Rao-Scott correction; #257 presupposes a SIMPLE random sample |

### Output fields

- ca_contingency: counts/expected (r x c) + prop_total/prop_row/prop_col + row_sums/col_sums + min_expected/n_cells_below_1/n_cells_below_5/share_below_5 + cochran_ok/strict_ok (THE ROUTING CRITERION chi-squared vs Fisher)
- ca_chisq: statistic (OF THE TEST — Yates-corrected if correct=TRUE AND the table is 2x2) / statistic_pearson (ALWAYS the UNCORRECTED Pearson X^2) / df / p_value / significant / decision + cramers_v (ALWAYS computed from statistic_pearson ⇒ IDENTICAL to ca_assocs.nominal.cramers_v) + residuals (Pearson) / stdres (~N(0,1)) / contribution / contribution_share (the share of statistic_pearson — it ALWAYS sums to 1) PER CELL (chart-data: which cell «drives» the X^2) + yates_requested/yates_applied
- ca_fisher: p_value/decision + odds_ratio/odds_ratio_lwr/odds_ratio_upr/conf_level (2x2 ONLY, conditional MLE) + is_2x2 + workspace or (simulate_p_value, B, seed)
- ca_assocs: nominal$ {cramers_v, contingency_coef, tschuprows_t, uncertainty_coef_sym/row/col, gk_tau_row/col} — each c(estimate, lwr.ci, upr.ci); phi (2x2 ONLY, otherwise NULL); gamma (scale='ordinal' ONLY); assocs = a (16 or 9) x 3 Assocs matrix + assocs_measures/ordinal_excluded
- ALL: x_codes/y_codes + x_labels/y_labels (EXTERNALIZATION OF THE CODING — §3b gate 6) + n/n_input/n_na/na_action + cross_section_gate {lb_statistic, lb_p_value, lb_lag, n, n_na, alpha, tested, decision}

### Pitfalls

- NORMATIVE GATE 4 (cross-section only): EVERY function calls the SHARED gate_cross_section_only (the shared gates module) on the ORIGINAL vectors — an explicit rejection of ts/xts/zoo/tsibble + a Ljung-Box whiteness precheck (lag = min(10, n/5)); autocorrelation INFLATES the Type I error ⇒ a spuriously significant chi-squared. That is why the input is VECTORS OF OBSERVATIONS, NOT a ready-made contingency table (Ljung-Box is not defined on an aggregated table)
- gate_alpha (default 0.05) — DECOUPLED FROM THE TEST'S alpha: alpha exists ONLY in ca_chisq/ca_fisher (the only ones with a decision); ca_contingency/ca_assocs do NOT expose it at all (it would be a silent no-op). The Ljung-Box precheck is a TEST OF SIZE gate_alpha ⇒ by construction it blocks a small share of VALID i.i.d. input; LIVE-MEASURED (the engine, rnorm, 5000 replications): n=200 -> 1.6%/5.7%/10.1%, n=60 -> 2.3%/6.7%/10.8% for 0.01/0.05/0.10
- ordered (default TRUE) — AN EXPLICIT DECLARATION OF ROW ORDER: survey answers are the permutable population par excellence, but a SORTED CSV makes Ljung-Box reject (live-verified) whereas chisq_test/fisher_test/CramerV are PERMUTATION-INVARIANT (the contingency table does not change). ordered = FALSE ⇒ an explicit omission of Ljung-Box (branch = skipped-by-declaration, decision = pass-unordered), with the structural checks and the time-series class rejection (branch: class-rejected) ALWAYS active. lb_lag together with ordered = FALSE ⇒ a hard stop
- SILENTLY WRONG: chisq_test with expected counts < 5 emits ONLY the warning «Chi-squared approximation may be incorrect» and returns a p-value ⇒ OUR OWN HARD gate (rule='cochran' by default: none < 1 AND <=20% of the cells < 5; rule='strict': none < 5) that routes to ca_fisher / simulate_p_value
- SILENTLY WRONG: a ONE-row/one-column table ⇒ chisq_test switches SILENTLY to a «Chi-squared test for given probabilities» (goodness-of-fit, df = c-1) — A DIFFERENT TEST; gated with >=2 levels + a post-check df == (r-1)(c-1)
- SILENTLY WRONG: table drops the NA SILENTLY (useNA='no') ⇒ an explicit policy na_action='fail' (the default) \| 'omit' PAIRWISE, with n_input/n_na always in the output; a ZERO MARGIN (an empty row/column) ⇒ X-squared = NaN / p = NA with ONLY a warning (and the cryptic «missing value where TRUE/FALSE needed» in CramerV) ⇒ a hard gate
- A FACTOR INPUT (the most frequent wrong type in a categorical node) ⇒ a hard stop with an EDUCATIONAL message: it names the argument, gives the CLASS + nlevels (NOT the mode — live-verified mode(factor(x)) == 'numeric' WHILE is_numeric(factor(x)) == FALSE, i.e. the mode LIES) and the EXPLICIT conversion as.integer(x) (codes 1.k in the order of the levels) + levels(x) -> x_labels. The node requires NUMERICALLY CODED VECTORS OF OBSERVATIONS (a requirement of the shared cross-section gate)
- SILENTLY WRONG: Phi on an r x c table does NOT error — it returns sqrt(X^2/n), which EXCEEDS 1 (a perfect 3x3 -> 1.414214); it is exposed ONLY for 2x2. Likewise the Yates correction is ignored SILENTLY outside 2x2 (yates_applied says what ACTUALLY happened; in ca_assocs correct=TRUE outside 2x2 = a hard stop)
- YATES vs EFFECT SIZE (CRITICAL): Cramér's V is defined (Cramér 1946 §21.9) on the UNCORRECTED Pearson X^2 — NOT on the Yates-corrected statistic that is the conventional DEFAULT for 2x2 (correct=TRUE). The node ALWAYS computes the SIZE measures from statistic_pearson (INDEPENDENTLY of correct), so that ca_chisq.cramers_v COINCIDES (< 1e-12, pinned in a regression test) with ca_assocs.nominal.cramers_v[['estimate']] (CramerV). LIVE (2x2, n=120): from Yates 0.5009034 vs from Pearson 0.5175817 — a 4.4% UNDERSTATEMENT and TWO different numbers for ONE named statistic. Likewise contribution_share is divided by statistic_pearson (otherwise it summed to 1.0678 = «shares» > 100%). On the Monte-Carlo path the reference sets YATES=0 ⇒ statistic == statistic_pearson
- SILENTLY WRONG: fisher_test on an r x c table ignores alternative SILENTLY — a live 3x3 with alternative='less' gave THE SAME p-value as two.sided ⇒ one-sided ONLY for 2x2 (and incompatible with simulate_p_value, which is always two.sided)
- ORDINAL vs NOMINAL: the ordinal measures (Gamma/Kendall tau-b/Stuart tau-c/Somers' D/Pearson/Spearman) change SIGN with the arbitrary order of the categories ⇒ scale='nominal' is the SAFE default and excludes them explicitly (ordinal_excluded). NOTE: the Goodman-Kruskal TAU is a NOMINAL PRE measure (not Kendall's/Stuart's tau) and is ALWAYS returned
- FEXACT: the exact Fisher test allocates memory — a 4x4/n=300 table fails at the default workspace=2e5 («FEXACT error 6. LDKEY=620 is too small»); SOME such tables pass with 2e6, DENSER ones fail THERE TOO («FEXACT error 7»); a 12x12 fails even with 2e8 ⇒ then ONLY simulate_p_value=TRUE (seeded). The node translates the cryptic message into an educational one with the two ways out; a level cap max_levels (default 20, permitted [2,50])
- §3b gate 6 (fit/apply externalization): the node does NOT fit/transform, but it EXTERNALIZES THE CODING — x_codes/y_codes (numeric) + x_labels/y_labels are ALWAYS returned and handed back as x_levels/y_levels in the survey's next wave ⇒ tables COMPARABLE cell by cell. If binning preceded it, bn_apply keeps THE SAME breaks
- DETERMINISM: all the default paths are algebraic (and CramerV method='fisher' is Fisher's z transformation, NOT a simulation); the TWO Monte-Carlo paths run with set.seed(seed) AND restore the caller's.Random.seed; Assocs is PINNED to verbose=3 (with 1/2 it returns 3 of the 16 measures ⇒ it would change the SHAPE of the output)
- MASKING: library(DescTools) is NOT called — requireNamespace + DescTools:: everywhere. In the SHARED source env DescTools masks Phi (a target function of THIS file AND critical for the VAR wrappers), BoxCox, Lc/Gini/Atkinson/Herfindahl/Rosenbluth, MAPE, igraph::`%c%`, BrierScore, Quarter, AUC (live-verified; the same verdict as #114)

### References

- Cochran, W.G. (1954) «Some Methods for Strengthening the Common Chi-Squared Tests», Biometrics 10(4):417-451 — the rule «no expected count < 1, <= 20% of the cells < 5»
- Cramér, H. (1946) Mathematical Methods of Statistics, §21.9 — Cramér's V
- Goodman, L.A. & Kruskal, W.H. (1954) «Measures of Association for Cross Classifications», JASA 49:732-764 — tau (a NOMINAL PRE measure) and gamma (ORDINAL)
- Agresti, A. (2013) Categorical Data Analysis, 3rd ed., ch. 2-3 — nominal vs ordinal measures; why the ordinal ones are uninterpretable on a nominal scale
- Fisher, R.A. (1935) The Design of Experiments, ch. II — the exact test
- the chisq_test routine's documentation / the fisher_test routine — «For 2 by 2 tables, the null of conditional independence is equivalent to the hypothesis that the odds ratio equals one»; the warning-only behaviour with expected counts < 5; workspace/FEXACT
- DescTools 0.99.60 reference — CramerV/ContCoef/TschuprowT/Phi/UncertCoef/GoodmanKruskalTau/GoodmanKruskalGamma/Assocs(verbose=3 -> 16x3)
- the normative gate spec §3b normative gate 4 (cross-section only); Hyndman & Athanasopoulos, FPP 3rd ed. §5.4 — the rule lag = min(10, n/5) of the Ljung-Box precheck
