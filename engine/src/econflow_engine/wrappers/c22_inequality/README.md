<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 22-inequality

6 METHOD-SELECTION cards, 6 modules, 25 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #91 — inequality indices + Lorenz curve (Gini/Theil/Atkinson/RS/Kolm/CV/entropy)

**Module:** `inequality_indices_lorenz.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `compute_inequality` | `x` | `matrix_handle`, `enum`, `number` | — | `light` | — |
| `lorenz_curve` | `x` | `matrix_handle` | — | `light` | — |

### Use when

a cross-section of non-negative values (incomes/wealth/shares) → a scalar inequality index or the Lorenz curve as numeric data; descriptive/distributional at one point in time

### Do not use when

a return tail (VaR/ES→#65); a conditional-on-X tail/GaR (→#64); poverty/concentration indices (pov/conc are not exposed); a within/between Theil decomposition by group; time-series dynamics

### Alternatives

| instead use | when |
| --- | --- |
| type=Gini | a headline single number, the most comparable; sensitive mainly to the centre of the distribution |
| type=Theil / type=entropy | you want an additive within/between decomposition (the GE family); entropy@1==Theil@0==Theil's T/GE(1) (upper tail), entropy@0==Theil@1==mean log deviation/GE(0) (lower tail) |
| type=Atkinson | you want an explicit inequality-aversion parameter epsilon (normative/welfare) |
| type=Kolm | you want absolute inequality (invariant to adding a constant), not relative |
| type=RS | Ricci-Schutz/Pietra: the share of the total that would have to be redistributed (Robin Hood) |
| lorenz_curve + Lorenz dominance | a non-parametric comparison: if curve A lies everywhere above B ⇒ unambiguously less inequality (stronger than a scalar) |
| cat.12 quantreg/PerformanceAnalytics | a conditional-on-X tail (GaR) or return risk metrics — a different question |

### Output fields

- compute_inequality.index: the scalar index; Gini/Atkinson/RS∈[0,1] (0=equality), Theil/entropy≥0 (NOT a percentage), Kolm in units of x (absolute), var=CV/square.var=CV²
- compute_inequality.type: which index was computed (match.arg, default Gini)
- compute_inequality.parameter: NA_real_ ⇒ the package default (Atkinson 0.5, Kolm 1, entropy 0.5, Theil 0), NOT 'no parameter'
- compute_inequality.n: sample size
- lorenz_curve.p: cumulative population share 0.1 (chart-ready array)
- lorenz_curve$L: ordinary Lorenz 0.1 (the bottom p*100% holds L(p)*100% of the total); relative inequality
- lorenz_curve$L_general: generalized Lorenz = L×mean (units of x); it embeds the level → a welfare comparison
- lorenz_curve.gini: the Gini of the same series, for consistency; lorenz_curve.n: the size

### Pitfalls

- Theil/entropy are NOT bounded at 1 — do not read them as a percentage; only Gini/Atkinson/RS∈[0,1]
- Kolm is absolute (units of x), not a 0-1 relative index — do not compare it with the Gini
- in ineq the parameter is inverted between the two types: entropy@1==Theil@0 (==the Theil default; Theil's T/GE(1), upper tail), entropy@0==Theil@1 (mean log deviation/GE(0), lower tail): the same number, a different name/tail
- parameter=NA in the output ⇒ the package default, NOT 'no parameter'
- non-negativity is enforced ONLY for Gini/Atkinson/Theil/entropy+Lorenz; RS/Kolm/var/square.var accept negatives; ineq itself does not error on negatives
- all zeros: it passes the >=0 gate but Lc divides by 0 → NaN→JSON null; the wrapper blocks it with a sum(x)>0 gate
- ordinary L (shape) vs generalized L_general (shape+level): the same L does not mean the same welfare if the mean differs (Shorrocks)

### References

- Cowell 2000 Measurement of Inequality (Handbook of Income Distribution)
- Atkinson 1970 JET 2:244 (Atkinson index & inequality aversion)
- Theil 1967 Economics and Information Theory (Theil/entropy indices)
- Arnold 1987 Majorization and the Lorenz Order, Springer (Lorenz dominance)
- Shorrocks 1983 Economica 50:3 (generalized Lorenz)
- Kolm 1976 JET 12:416 (absolute inequality)

## #224 — tax progressivity & redistribution + subgroup decomposition of inequality (extended/S-Gini · concentration · Atkinson · GEI · Lorenz)

**Module:** `tax_progressivity_redistribution.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ic2_sgini` | `x` | `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |
| `ic2_sconc` | `x`, `y` | `matrix_handle`, `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |
| `ic2_atkinson` | `x` | `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |
| `ic2_gei` | `x` | `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |
| `ic2_lorenz` | `x` | `matrix_handle`, `matrix_handle` | — | `light` | — |
| `ic2_decomp_sgini` | `x`, `z` | `matrix_handle`, `series_codes`, `matrix_handle`, `number`, `enum`, `boolean` | — | `light` | — |
| `ic2_decomp_gei` | `x`, `z` | `matrix_handle`, `series_codes`, `matrix_handle`, `number`, `boolean` | — | `light` | — |
| `ic2_decomp_atkinson` | `x`, `z` | `matrix_handle`, `series_codes`, `matrix_handle`, `number`, `enum`, `boolean` | — | `light` | — |

### Use when

a cross-section of non-negative values (income/wealth/tax/expenditure) when you want (a) a single-parameter/extended Gini with an explicit tail weight (param), an Atkinson index (aversion epsilon), a GEI (Theil/MLD), (b) a concentration index ranked by ANOTHER variable → the building blocks of Kakwani progressivity/Reynolds-Smolensky redistribution, (c) the Lorenz curve as numeric data, or (d) a SUBGROUP decomposition into within/between/(overlap\|stratif\|cross\|residual) by a factor

### Do not use when

a plain scalar index with no tail parameter/decomposition → #91 ineq (Gini/RS/Kolm/var); a return tail VaR/ES → #65; a conditional-on-X GaR → #64; poverty indices (FGT) — not exposed; time-series dynamics

### Alternatives

| instead use | when |
| --- | --- |
| #91 ineq (compute_inequality) | a headline scalar Gini/Theil/Atkinson/Kolm WITHOUT a group decomposition and WITHOUT an extended-Gini param — a simpler surface |
| ic2_sgini param>1 | an extended Gini with an explicit weight on the poor (param=2 is the classic Gini; a larger param → more sensitivity to the lower tail) |
| ic2_gei alpha=1 (Theil-T) / alpha=0 (MLD) | you want a FULLY ADDITIVE within+between decomposition (the GE family) |
| ic2_decomp_atkinson decomp=BDA vs DP | BDA is multiplicative (1-(1-w)(1-b)) with a cross term; DP is additive (within+between+residual) — choose according to your reference framework |
| ic2_sconc + ic2_sgini (the difference) | Kakwani progressivity = C_tax - G_preTax; Reynolds-Smolensky = G_preTax - C_postTax — the redistributive analysis of taxes/benefits |
| ic2_lorenz + Lorenz dominance | a non-parametric comparison of distributions (curve A everywhere above B ⇒ unambiguously less inequality) |

### Output fields

- ic2_sgini/sconc/atkinson/gei.index: the scalar index; .index_name (SGini/SConc/Atk/GEI); .parameter + .parameter_name (param/epsilon/alpha); .n; .weighted
- ic2_lorenz.p: the cumulative population share 0.1 (n+1 points, chart-ready); $L: the ordinary Lorenz curve 0.1; $L_general: the generalized one = L*mean (in units of x); .gini; .mean
- ic2_decomp_*.within/.between: the within-/between-group inequality; .third_component + .third_name (overlap\|stratif\|cross\|residual); .between_elmo (the Elbers 'maximum' between; NA if ELMO=FALSE, OUTSIDE the identity)
- ic2_decomp_*.reconciled_total + .reconcile_error: the recomposition check (\|total-sum(components)\|<=1e-6); .decomp_method; .groups (a data_frame per group: group/index/share/weight[/contribution]); .n_groups

### Pitfalls

- the EXTENDED GINI param: param=2 == the classic Gini; param>1 weights the poor; param->1 => 0; 0<param<1 => a NEGATIVE index (a mathematically valid S-Gini, NOT conventional inequality — for a headline figure use param>=1)
- the ATKINSON DECOMPOSITION: BDA is MULTIPLICATIVE (total=1-(1-within)(1-between)) — do NOT add within+between+cross (it does not equal the total; the 'cross' term = within+between-total); DP is ADDITIVE (within+between+residual)
- the GEI is FULLY ADDITIVE (total=within+between); the SGini BM decomposition is within+between+overlap, YL is within+between+stratif; betweenELMO is NOT part of any identity
- KAKWANI/REDISTRIBUTION = the DIFFERENCE between a concentration index and a Gini, NOT a single output: Kakwani progressivity = C_tax - G_preTax (positive=progressive); Reynolds-Smolensky = G_preTax - C_postTax; the wrapper supplies the building blocks, the difference is taken downstream
- STRICT POSITIVITY: Atkinson with epsilon==1 & GEI with alpha ∈ {0,1} require x>0 (a zero → IC2 silently returns NULL); epsilon!=1 / alpha outside {0,1} accept zeros
- SILENTLY WRONG (gated by the wrapper): a negative x → IC2 NULL; NA in x/w → silent removal; a wrong length(w) → silent recycling; a non-factor z → NULL; an extreme alpha → overflow to Inf
- GEI alpha: alpha=1 is Theil-T/GE(1) (the upper tail); alpha=0 is the mean log deviation/GE(0) (the lower tail); alpha=2 is half the CV²

### References

- Kakwani N.C. (1977) Measurement of Tax Progressivity, Economic Journal 87(345):71-80 (concentration/progressivity)
- Atkinson A.B. (1970) On the Measurement of Inequality, JET 2:244-263
- Blackorby C., Donaldson D., Auersperg M. (1981) Canadian J. Economics 14:665-685 (the BDA Atkinson decomposition)
- Das T., Parikh A. (1982) Empirical Economics 7:23-48 (the DP Atkinson decomposition)
- Bhattacharya N., Mahalanobis B. (1967) JASA 62:143-161 (the BM Gini decomposition); Yitzhaki S., Lerman R. (1991) Review of Income and Wealth 37:313 (YL stratification)
- Shorrocks A.F. (1980) The Class of Additively Decomposable Inequality Measures, Econometrica 48:613-625 (GE within/between); Elbers et al. (2005) World Bank WP 3687 (the ELMO maximum between)
- Reynolds M., Smolensky E. (1977) Public Expenditure, Taxes and the Distribution of Income (the redistribution effect)

## #225 — drivers of inequality change: RIF (recentered influence function) regressions + regression-based (Fields/Yun) inequality decomposition

**Module:** `drivers_inequality_change.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `rif_influence` | `x` | `matrix_handle`, `matrix_handle`, `enum`, `number`, `enum` | `quantile=0.5` | `light` | — |
| `rif_regression` | `formula`, `data` | `formula`, `df_handle`, `string`, `enum`, `num_array`, `enum` | — | `light` | — |
| `rif_regression_se` | `formula`, `data` | `formula`, `df_handle`, `string`, `enum`, `number`, `enum`, `integer`, `number`, `integer` | `quantile=0.5`, `Nboot=100`, `confidence=0.95`, `seed=42` | `light` | — |
| `gini_decomposition` | `x`, `z` | `matrix_handle`, `raw_handle`, `matrix_handle` | — | `light` | — |
| `mld_decomposition` | `x`, `z` | `matrix_handle`, `raw_handle`, `matrix_handle` | — | `light` | — |
| `dineq_regression_decomp` | `formula`, `data` | `formula`, `df_handle`, `string` | — | `light` | — |
| `dineq_change_decomp` | `formula1`, `data1`, `formula2`, `data2` | `formula`, `df_handle`, `string`, `formula`, `df_handle`, `string` | — | `light` | — |

### Use when

you want to explain WHAT DRIVES inequality (not merely to measure it): (a) the marginal effect of covariates on a distributional statistic (quantile/gini/variance) through a RIF regression; (b) a decomposition of the Gini/MLD into within/between/overlap by subgroup; (c) a Fields regression-based decomposition of total inequality across several characteristics; (d) a Yun decomposition of the CHANGE in inequality between two years into a price vs a quantity effect. Income micro data with survey weights + covariates

### Do not use when

a plain scalar index/Lorenz curve without covariates (→#91 ineq); tax progressivity/single-index decomposition (→#224 IC2); a parametric income distribution (→#227 GB2); a conditional-on-X outcome tail / Growth-at-Risk (→#64 quantreg); return risk metrics VaR/ES (→#65); time-series dynamics

### Alternatives

| instead use | when |
| --- | --- |
| rif_influence (the RIF vector) | you want the influence of each observation on the index itself (an input for a downstream RIF regression or a health-inequality decomposition); recentering: the weighted mean == the index |
| rif_regression (a deterministic OLS on the RIF) | the marginal effects of covariates on a quantile/gini/variance, fast, without inference; it supports a vector of quantiles (unconditional quantile regression, Firpo-Fortin-Lemieux) |
| rif_regression_se (bootstrap SE/CI/Z/P) | you need statistical inference on the RIF coefficients; ONE quantile only; SEEDED (deterministic) |
| gini_decomposition | you want the within/between + overlap (interaction) term of the Gini by one categorical variable; the Gini does NOT decompose cleanly (the overlap != 0 when the group distributions overlap) |
| mld_decomposition (GE(0)) | you want a CLEAN within+between decomposition (no overlap) by one categorical variable; the mean log deviation = the generalized entropy GE(0), additively decomposable |
| dineq_regression_decomp (Fields 2003) | SEVERAL characteristics at once: the contribution of each covariate (+ the residual) to total inequality (4 indices: gini/mld/theil/var-log); they sum to 100% |
| dineq_change_decomp (Yun 2006) | you compare two years/datasets: a decomposition of the CHANGE in the variance of log income by characteristic into a price effect (a change in the coefficients) vs a quantity effect (a change in composition) |

### Output fields

- rif_influence.rif: the numeric RIF vector (chart-ready); recentered_stat: the index (the weighted mean of the RIF == the index, verified live); method/quantile/kernel/weighted/n
- rif_regression.coefficients: a SINGLE data_frame (term, quantile, coef, se, t, p) — normalised per quantile (the package changes shape per method); adjusted_r2 df; fit=raw (a stub)
- rif_regression_se.coefficients: a data_frame (term, coef, lower, upper, se, z_value, p_value, signif); Nboot/confidence/seed echoed; deterministic given the seed
- gini_decomposition.decomposition: named numeric (gini_total, gini_within, gini_between, gini_overlap — they do NOT add up without the overlap); by_group df (gini/contribution/mean/share_pop/share_income/n); gini_group_contribution sums to gini_within
- mld_decomposition.decomposition: named numeric (mld_total, mld_within, mld_between — within+between == total, with NO overlap); by_group df; n_deleted (the x<=0 values that were dropped, the log); note
- dineq_regression_decomp.inequality_measures: named numeric (gini, mld, theil, variance_logincome); the decomposition df (variable, contribution — they sum to 1); adjusted_r2/r_squared; n_deleted/n_used; note
- dineq_change_decomp.variance_logincome: (year1, year2, change); change_absolute/change_relative df (variable, price, quantity, total); residual_absolute/residual_relative; the Yun identity: sum(price+quantity)+residual == change

### Pitfalls

- a DUAL weights convention: rif/gini_decomp/mld_decomp take weights = a numeric VECTOR; rifr/rifrSE/dineq_rb/dineq_change_rb take weights = a COLUMN NAME (a string) inside data — the wrong type = a silent error/misalignment
- rifr CHANGES ITS OUTPUT SHAPE per method (quantile: Coef/SE/t/p matrices; gini/variance: a coefficients matrix + a scalar r2) — the wrapper normalises it into ONE tidy data_frame; do not rely on the raw shape
- rifrSE accepts a scalar quantile ONLY (a vector → 'condition has length > 1'); it is a BOOTSTRAP → SEEDED (the same seed = identical results)
- the log-based methods (mld/dineq_rb/dineq_change_rb) SILENTLY DROP x<=0 → always read n_deleted/note; if you miss it you overstate n
- the Gini overlap term != 0 when the group distributions overlap → within+between do NOT sum to the total (unlike the MLD, which is purely additive); do not ignore the overlap
- silently wrong: the package applies complete.cases dropping on NA (x/z), sets weights[is.na] to 0, and recycles if length(weights/z) != length(x); weights==0 → a silent NA RIF → the wrapper enforces no NA + length==n + weights STRICTLY >0
- gini_decomp does NOT filter negative x → a silently wrong Gini; the wrapper enforces an x>=0 gate (project-side); kernel='rectangular' with a gap around the quantile → dq=0 → Inf (the finite post-gate blocks it)
- the formula functions (rif_regression/_se, dineq_regression_decomp, dineq_change_decomp): an NA in ANY covariate → blocked-by-gate (dineq/lm would silently drop the rows through na.omit while reporting '0 deleted' + an inflated n_used); complete cases are required in every variable of the formula

### References

- Firpo, Fortin & Lemieux 2009 (Econometrica 77:953, Unconditional Quantile Regressions — the RIF)
- Fields 2003 (Research in Labor Economics 22:1, regression-based inequality decomposition)
- Yun 2006 / Brewer & Wren-Lewis 2016 (Oxford Bull. Econ. Stat. 78:289, accounting for changes in income inequality — price vs quantity)
- Mookherjee & Shorrocks 1982 (Economic Journal 92:886, the MLD within/between decomposition)
- Heckley, Gerdtham & Kjellsson 2016 (J. Health Economics 48:89, a general RIF decomposition of socioeconomic inequality)

## #226 — Complex-survey-aware inequality & poverty with design-based linearized SE (Gini/QSR/Zenga + FGT/ARPR)

**Module:** `complex_survey_aware.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `svy_inequality` | `data`, `income`, `ids`, `weights` | `df_handle`, `string`, `string`, `string`, `string`, `string`, `boolean`, `string`, `string`, `boolean`, `number`, `enum`, `number`, `number` | — | `light` | — |
| `svy_poverty` | `data`, `income`, `ids`, `weights` | `df_handle`, `string`, `string`, `string`, `string`, `string`, `boolean`, `string`, `string`, `boolean`, `number`, `enum`, `number`, `enum`, `number`, `number`, `number` | — | `light` | — |

### Use when

you have survey MICRODATA (a microdata data_frame) with sampling weights/strata/clusters and you want an inequality index (gini/qsr/zenga) or a poverty index (FGT/ARPR) WITH a correct design-based (linearized) standard error + CI + degrees of freedom; the node builds svydesign + convey_prep internally

### Do not use when

a plain vector with no complex-survey design → #91 ineq (a scalar index/Lorenz curve, without SE); replicate-weight designs (svrepdesign) — not exposed; a return tail VaR/ES → #65; a conditional-on-X GaR → #64; the other convey estimators (svygei/svyatk/svyrenyi/svywatts/svypoormed) — future candidates

### Alternatives

| instead use | when |
| --- | --- |
| svy_inequality measure=gini | a headline single-number inequality index with a design-based SE; sensitive mainly to the centre |
| svy_inequality measure=qsr | the Quintile Share Ratio S80/S20 (alpha1=0.2, alpha2=0.8): the ratio of the upper to the lower quantile share; a Eurostat headline indicator |
| svy_inequality measure=zenga | the Zenga (2007) uniformity index ∈[0,1]; sensitive to the whole distribution (a point-by-point comparison of lower/upper means) |
| svy_poverty measure=fgt g=0/1/2 | Foster-Greer-Thorbecke: g=0 the headcount ratio, g=1 the poverty gap, g=2 the severity (the squared gap); an absolute (abs_thresh) or relative (relq/relm) threshold |
| svy_poverty measure=arpr | the At-Risk-Of-Poverty Rate: the share below a relative threshold (the default is 60% of the median); a Eurostat headline poverty indicator |
| subset_var/subset_level | domain estimation (e.g. by region/group) with correctly reduced degrees of freedom |
| #91 ineq | a plain vector with no survey design/weights — a descriptive index without SE |

### Output fields

- estimate: the scalar index (Gini/QSR/Zenga/FGT/ARPR); Gini/Zenga/ARPR/FGT∈[0,1], QSR>=1 (a ratio)
- se: the design-based LINEARIZED standard error (a Deville influence function; NOT a naive/iid SE)
- ci_lower/ci_upper: a t-based CI at the given level, with the design degrees of freedom (df)
- df: degf(design) — the degrees of freedom of the design (they drop in a domain subset)
- measure/income: which index/which variable; n_total/n_used/n_na: the sizes; n_used = the ACTUAL non-NA observations that enter the estimator (= n_total - n_na, or the count of non-NA within the domain); it is NOT inflated by NA incomes that the estimator drops
- svy_poverty.g/type_thresh/abs_thresh: the FGT parameters; svy_inequality.alpha1/alpha2: the QSR quantiles

### Pitfalls

- convey_prep is MANDATORY: svyfgt/svyarpr/svyqsr error without it, BUT svygini/svyzenga compute SILENTLY (with a possibly wrong SE) — the wrapper always runs it
- wrong ids/weights/strata → a wrong linearized SE (the estimate may be right while the SE is not); the design must reflect the ACTUAL sampling
- an NA income + na_rm=FALSE → coef=NA SILENTLY; the wrapper blocks it (a hard gate) — set na_rm=TRUE explicitly
- svydesign SILENTLY accepts negative/zero weights; the wrapper requires weights>0
- svyfgt with type_thresh∈{relq,relm} SILENTLY ignores abs_thresh — the wrapper requires abs_thresh=NULL unless type_thresh='abs'
- FGT monotonicity: severity(g=2) <= gap(g=1) <= headcount(g=0); they differ in their sensitivity to the depth of poverty
- ids="1" means ~1 (no clustering); df≈n-1; for a clustered design supply the actual PSU column

### References

- Foster, Greer & Thorbecke 1984 Econometrica 52:761 (the FGT poverty measures)
- Osier 2009 Survey Methodology 35:193 (the linearization of inequality/poverty estimators)
- Deville 1999 Survey Methodology 25:193 (influence-function variance estimation)
- Zenga 2007 Statistica & Applicazioni 5:3 (the Zenga uniformity index)
- Eurostat EU-SILC methodology (ARPR at 60% of the median, the S80/S20 quintile share ratio)

## #227 — GB2 (Generalized Beta of the 2nd kind, 4 parameters a,b,p,q) parametric income-distribution ML fit + analytic Gini/ARPR

**Module:** `gb2_parametric_income.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fit_gb2` | `z` | `matrix_handle`, `matrix_handle`, `number`, `boolean` | — | `light` | — |
| `gini_gb2` | `shape1`, `shape2`, `shape3` | `number`, `number`, `number` | — | `light` | — |
| `arpr_gb2` | `prop`, `shape1`, `shape2`, `shape3` | `number`, `number`, `number`, `number` | — | `light` | — |

### Use when

you have microdata of POSITIVE income (optionally with survey weights) and you want a PARAMETRIC model of the whole distribution: the GB2(a,b,p,q) is fitted by ML (full + profile log-likelihood) and yields CLOSED-FORM analytic indicators (Gini, ARPR, RMPG, QSR) that smooth out sampling noise and allow comparison/simulation; or you already have estimated (a,p,q) and want an analytic Gini/ARPR

### Do not use when

a non-parametric scalar index or a Lorenz curve straight from the sample (→#91 ineq, with no distributional assumption); a RETURN tail VaR/ES (→#65) or a conditional-on-X GaR (→#64); income with zeros/negatives (the GB2 is defined on x>0 — it is rejected); a small sample where the 4-parameter ML does not converge (heavy-tail identifiability); a within/between decomposition by group

### Alternatives

| instead use | when |
| --- | --- |
| #91 ineq (a non-parametric Gini/Theil/Atkinson + Lorenz) | you do not want a distributional assumption; a descriptive index straight from the sample at one point in time; the GB2 is preferable when you want smoothing, tail extrapolation, or analytic poverty/welfare metrics from a single model |
| fit_gb2 (the full GB2) | the most general 4-parameter form; it needs a reasonably large sample for the full ML to converge (the convergence gate blocks it otherwise) |
| gini_gb2 / arpr_gb2 (analytic, standalone) | you already have (a,p,q) [+prop] from another source/fit and you want only the scale-free index without refitting |
| allow_nonconvergence=TRUE | you explicitly want the non-converged result for diagnosis (it is returned with converged=FALSE); NEVER as a production output — a non-converged 4-parameter fit is silently wrong |
| cat. 12 quantreg/PerformanceAnalytics | a conditional-on-X tail (GaR) or return risk metrics — a different question from an income distribution |

### Output fields

- fit_gb2.a,.b,.p,.q (+ .params, a named vector): the 4 estimated GB2 parameters from the FULL ML; a=the tail shape, b=the scale, p/q=the Beta-2 shapes; at convergence all are > 0
- fit_gb2.loglik / .loglik_profile: the CONVENTIONAL TOTAL log-likelihood (the sum of the weighted GB2 log-densities = -optim.value * sum(w); negative, O(n)) — directly usable for AIC=-2*loglik+2k/BIC/LR; NOT the raw negated per-observation MEAN from optim
- fit_gb2.converged: TRUE only if the FULL ML optim convergence==0 (a FUNCTIONAL GATE); .convergence_full/.convergence_profile are the optim codes (0=OK, 1=iteration limit)
- fit_gb2.gini: the analytic Gini(a,p,q)∈[0,1] at the fitted parameters; .gini_defined=FALSE ⇒ a heavy tail (a*q<=1) where it is undefined → NA
- fit_gb2.arpr: the At-Risk-of-Poverty Rate at prop×median (default 0.6); .arpr_prop is the proportion; .arpr_defined is the finiteness flag
- fit_gb2.n: the sample size; .indicators: a data_frame (empirical estimate vs ML full vs ML profile: median,mean,ARPR,RMPG,QSR,GINI,a,b,p,q) — a chart-ready comparison of empirical vs GB2-fitted values
- gini_gb2.gini: the analytic Gini of the GB2 (scale-free, it depends only on a,p,q)
- arpr_gb2.arpr: the analytic ARPR (scale-free); .prop is the poverty line as a proportion of the median

### Pitfalls

- CONVERGENCE: a small/heavy-tailed sample → the FULL ML does not converge (convergence==1) BUT it returns parameters as if it had succeeded — the convergence gate blocks that; converged=FALSE is not a valid output
- POSITIVE SUPPORT: zero/negative/NA incomes do NOT error in mlfit.gb2 (it proceeds silently); the x>0 & no-NA gate is imposed by the project (the documentation example itself filters inc>0)
- WEIGHTS: a wrong length of w is recycled silently, zero weights exclude observations — a gate on length==n & w>0
- HEAVY-TAIL Gini: gini.gb2 with a*q<=1 returns NA (the expectation does not exist); the standalone gini_gb2 errors explicitly, inside fit_gb2 → NA + gini_defined=FALSE (the fit itself remains valid)
- prop: the ARPR is monotone in prop; a prop outside (0,1) silently gives a wrong value — a gate on (0,1); it is scale-free (b is irrelevant)
- the gini_gb2/arpr_gb2 argument order: (shape1=a, shape2=p, shape3=q); swapping p and q changes the result — do not confuse them

## #228 — affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount ratio (r.hc), the Chakravarty concave T1 index (r.cha), the FGT convex T2 index (r.fgt), the Medeiros average affluence gap (r.med), the top income share (r.is), the Medeiros affluence line (line.med) — weighted implementations

**Module:** `affluence_richness_indices.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `richness_index` | `x`, `k` | `matrix_handle`, `matrix_handle`, `number`, `enum`, `number`, `number` | — | `light` | — |
| `income_share_top` | `x`, `p` | `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |
| `affluence_line` | `x`, `k` | `matrix_handle`, `matrix_handle`, `number` | — | `light` | — |

### Use when

a cross-section of positive incomes (with or without population weights) → how much and how intensely wealth is concentrated in the UPPER tail: the headcount of the rich (a line at k×median), the intensity of affluence (the concave T1 / convex T2 index), the absolute mean affluence gap, the income share of the top (1-p), or constructing a Medeiros affluence line from a poverty line

### Do not use when

the inequality of the WHOLE distribution (Gini/Theil/Atkinson/Lorenz → #91 ineq); POVERTY indices / the lower tail (FGT poverty); a return tail VaR/ES (→ #65); a conditional-on-X Growth-at-Risk (→ #64); Wolfson polarization / Palma / the weighted Gini (gini.w/polar.aff/S90S40 are not exposed — the Gini is covered by #91); bootstrap SE (boot.sd1/boot.sd2 are stochastic, not exposed); a subgroup decomposition (.sub is not exposed)

### Alternatives

| instead use | when |
| --- | --- |
| index=hc (r.hc) | how many people are rich — the weighted share of the population above the affluence line (the headcount); it does not capture intensity/distance |
| index=cha (Chakravarty, T1 concave) | an affluence intensity that INCREASES under a rank-preserving progressive transfer among the rich (axiom T1); bounded in [0,1]; the parameter beta>0 |
| index=fgt (FGT, T2 convex) | an affluence intensity that DECREASES under a progressive transfer among the rich (axiom T2); the parameter alpha>1; it is NOT bounded by 1 |
| index=med (the Medeiros gap) | the ABSOLUTE mean affluence gap (in income units), not a ratio — the size of the excess income above the line |
| income_share_top (r.is) | the share of total income of the richest (1-p) fraction — the most widely used metric (top 1%/10% shares); the threshold is the p-quantile, NOT k×median |
| affluence_line (line.med) | you want the affluence LINE (not an index) constructed from a poverty line (Medeiros); 0<k<1 |
| #91 ineq (Gini/Theil/Atkinson/Lorenz) | the inequality of the whole distribution, not a focus on the upper tail |

### Output fields

- richness_index.index: the affluence index; hc/cha ∈ [0,1] (ratios), fgt >= 0 (NOT bounded above), med >= 0 (absolute, in income units)
- richness_index.index_type: hc\|cha\|fgt\|med (match.arg, default hc)
- richness_index.affluence_line: rho = k × (the weighted median) — the UPPER threshold that was used; .median_income is the median
- richness_index.count_rich / share_rich / k / n: the number of units with x>rho, the weighted share of the rich, the value of k, the sample size
- income_share_top.income_share: the income share of those with x>q_p ∈ [0,1]; .threshold_quantile=q_p (the p-quantile); .top_fraction=1-p (e.g. p=0.9 → the top 10%); .count_top; .n
- affluence_line.affluence_line: rho_medeiros (the affluence line); .median_multiple=rho/median (>1); .median_income; .poverty_gap (Gp); .k; .n

### Pitfalls

- THRESHOLD DIRECTION (critical): the affluence line is an UPPER threshold. richness_index requires k>1 (rho=k×median, above the median); k<=1 → a line at or below the median → 'everyone is rich' (live: k=0.5 → r.hc=0.9, k=1 → 0.4); it is blocked by a gate
- the OPPOSITE meaning of k: in affluence_line (line.med) k is a POVERTY line (BELOW the median) → 0<k<1; it is the mirror image of richness_index — do not confuse them
- fgt is NOT bounded by 1 (it is convex, gaps^alpha; live alpha=3 → 1.27, a large alpha + a heavy tail → an overflow to Inf that the post-gate blocks); only hc/cha ∈ [0,1]; med is absolute
- alpha>1 (fgt) and beta>0 (cha): the package does NOT check the domain (live alpha=0.5 was computed silently); the wrapper enforces them only for the relevant index
- positive income x>0: the package does NOT error on negative/zero values (live r.hc(-5,…) returned a number); the wrapper blocks them (r.cha divides by x)
- weights: the same length as x (no recycling), strictly positive, with no NA; weight=NULL → equal weights; the weighted median/quantile is the SAME spatstat.univar function that the package calls internally → the reported rho/q_p is identical to the internal threshold
- r.is: p is the QUANTILE threshold in (0,1) and the index measures the richest (1-p) tail (p=0.9 → the top 10%); it is not 'the top p%'; the extremes degenerate (p→0 ⇒ ~1, p→1 ⇒ 0) — they are blocked
- affluence_line (line.med, Medeiros): the affluence line MUST lie ABOVE the median (median_multiple>1, a hard post-gate); a degenerate line.med <= median → blocked-by-gate (a line <= the median would make everyone 'rich'); a zero-dispersion x (length(unique)<2) → a pre-gate; a matrix with >1 column → a gate (vectors/1 column only)

### References

- Peichl, Schaefer, Scheicher 2008 IZA Discussion Paper 3790 (measuring richness — affluence indices, axioms T1/T2)
- Chakravarty 1983 Mathematical Social Sciences 6:307-313 (the concave index, the T1 mirror)
- Foster, Greer, Thorbecke 1984 Econometrica 52:761-766 (the FGT decomposable family, the convex T2 mirror)
- Medeiros 2006 Social Indicators Research 78:1-18 (an affluence line constructed from the poverty line)
- Brzezinski 2010 Social Indicators Research 99:285-299 (income affluence in Poland; the richness headcount & top income share)
