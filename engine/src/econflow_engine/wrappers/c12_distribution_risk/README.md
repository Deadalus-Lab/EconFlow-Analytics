<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 12-distribution-risk

12 METHOD-SELECTION cards, 12 modules, 36 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #64 — Quantile regression (+ Growth-at-Risk, ABG)

**Module:** `quantile_regression.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `qr_regression` | `formula`, `data` | `formula`, `df_handle`, `number`, `enum`, `enum`, `integer`, `integer` | `boot_replications=200`, `seed=42` | `light` | `object` |
| `qr_conditional_quantiles` | `object` | `raw_handle`, `df_handle` | — | `light` | — |
| `qr_slope_equality` | `object` | `raw_handle` | — | `light` | — |
| `qr_growth_at_risk` | `formula`, `data` | `formula`, `df_handle`, `df_handle`, `number`, `number`, `integer`, `enum`, `enum`, `integer`, `integer` | `risk_tau=0.05`, `h=0`, `boot_replications=200`, `seed=42` | `light` | `object` |

### Use when

modelling the whole conditional distribution of an outcome given covariates (several tau); a lower-tail tau = Growth-at-Risk (ABG)

### Do not use when

only the mean effect -> OLS; a descriptive tail without covariates -> #65; nlrq/crq/rqss are out of scope; a very small n (rank-deficient)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (time-series GaR only: stationarity, +KPSS confirmatory with the opposite polarity)
- qr_slope_equality (anova.rq: do the slopes differ across quantiles? -> justifies GaR, requires >=2 tau)

### Alternatives

| instead use | when |
| --- | --- |
| #95 sn skew-t (NEXT STEP) | you want the FULL growth density + expected shortfall from the GaR quantiles (ABG step 2) — the natural next step |
| OLS/lm | the mean effect suffices, homoskedasticity |
| #65 PerformanceAnalytics VaR/ES | a tail metric without covariates (descriptive) |
| brms quantile/distributional (cat. 14) | a full posterior / non-crossing / a skew-t likelihood |
| GARCH conditional VaR (volatility) | a tail driven by volatility clustering |

### Output fields

- coefficients: tidy tau/term/estimate/std_error/t_value/p_value (one block per tau)
- quantiles: tidy row_id/tau/predicted; crossing/any_crossing = quantile-crossing flag+count
- qr_slope_equality: statistic/ndf/ddf/p_value (pseudo-F, anova.rq)
- gar: row_id/gar/upside (gar=fitted risk_tau, upside=fitted 1-risk_tau); curve = the full curve
- n=complete rows (post-NA); n_total/n_dropped; h; risk_tau/upside_tau; object=rq/rqs (stub)

### Pitfalls

- quantile crossing: fitted quantiles are non-monotone in tau — flagged and counted, not hidden; any_crossing=TRUE -> suspect predictions
- GaR h-lead: for h>0 the prediction y_{t+h}~x_t uses orig_last (x_T), NOT a stale x_{T-h}; gar = the GaR h steps ahead, not today
- a tau outside (0,1) is blocked (rq accepted it for the WHOLE process)
- risk_tau must be ONE of the fitted tau (otherwise stop)
- se='boot' is the only stochastic option -> set.seed(seed) before summary; br/fn/pfn are deterministic

### References

- help('rq'), help('anova.rq'), help('predict.rq') ( quantreg)
- Koenker & Bassett 1978 (Econometrica 46:33, regression quantiles)
- Koenker & Bassett 1982 (Econometrica 50:43, slope-equality Wald test)
- Koenker 2005 Quantile Regression, Cambridge U. Press
- Adrian, Boyarchenko & Giannone 2019 (AER 109:1263, Vulnerable Growth / GaR)

## #65 — Value-at-Risk / Expected Shortfall / downside-risk / component-VaR

**Module:** `value_risk_expected.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pa_var` | `returns` | `matrix_handle`, `number`, `enum`, `enum`, `boolean` | `p=0.95`, `invert=False` | `light` | — |
| `pa_expected_shortfall` | `returns` | `matrix_handle`, `number`, `enum`, `enum`, `boolean` | `p=0.95`, `invert=False` | `light` | — |
| `pa_downside_risk` | `returns` | `matrix_handle`, `number`, `number` | `MAR=0`, `p=0.95` | `light` | — |
| `pa_component_var` | `returns`, `weights` | `matrix_handle`, `number`, `number`, `enum` | `p=0.95` | `light` | — |
| `pa_returns_from_long` | `data` | `df_handle`, `string`, `string` | `period_col='period'`, `value_col='value'` | `light` | — |

### Use when

downside-risk metrics for a return series: VaR/ES/CVaR, drawdown/semi-deviation/Sortino, skew/kurtosis, portfolio component-VaR (Euler)

### Do not use when

a conditional-on-covariates tail -> #64 GaR; a volatility-clustering tail -> GARCH; EVT/GPD/kernel/MC were excluded; the historical component (non-additive)

### Alternatives

| instead use | when |
| --- | --- |
| method=historical | no distributional assumption, large n (an ex-post empirical tail) |
| method=gaussian | a small sample / RiskMetrics parametric, returns ~normal |
| method=modified (Cornish-Fisher) | skew/excess kurtosis — check cf_valid |
| #64 GaR / quantile regression | a conditional-on-covariates tail |
| GARCH conditional VaR (volatility) | volatility clustering drives the tail |

### Output fields

- var/es: tidy series/var (plus es/es_ge_var); p/method/clean/invert/cf_valid/na_count/sign_convention
- sign_convention: invert=FALSE (our default) -> a POSITIVE loss magnitude; invert=TRUE -> a signed quantile
- downside summary: matrix metric x series (StdDev/SemiDev/DownsideDev/maxDD/VaR/ES/skew/kurt/Sortino)
- pa_component_var: portfolio_var scalar + contributions (series/contribution/pct_contribution)
- es_ge_var: \|ES\|>=\|VaR\| per series (a check on magnitude, independent of invert)

### Pitfalls

- sign convention: invert=FALSE => a positive loss magnitude (VaR=0.029 = a 2.9% loss); NEVER assume the sign, read .sign_convention
- modified/Cornish-Fisher: non-finite or \|ES\|<\|VaR\| -> cf_valid=FALSE (not silent); a gaussian/historical violation -> hard stop
- component: gaussian/modified only (the historical component is NOT additive -> silently wrong); POST-GATE Euler additivity; a negative contribution = a diversifier
- gaussian/modified VaR is UNCONDITIONAL (constant mu, sigma); not conditional/volatility-driven
- SE=FALSE is pinned -> no RNG (deterministic); skew/kurt = the tail shape (excess kurtosis>0 -> gaussian VaR understates)

### References

- help('VaR'), help('ES'), help('DownsideDeviation') ( PerformanceAnalytics)
- Zangari 1996 (RiskMetrics Monitor, Cornish-Fisher / modified VaR)
- Favre & Galeano 2002 (J. Alternative Investment 5, Mean-Modified VaR)
- Boudt, Peterson & Croux 2008 (J. of Risk 11:79, downside risk decomposition)
- Gourieroux, Laurent & Scaillet 2000 (J. Empirical Finance 7:225, Euler decomposition of VaR)
- Rockafellar & Uryasev 2000 (J. of Risk 2:21, CVaR/Expected Shortfall)

## #95 — Skew-t fit to fitted quantiles (ABG Growth-at-Risk «step 2») + density/ES

**Module:** `skew_fit_fitted.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `st_fit_quantiles` | `probs`, `quantiles` | `number`, `number`, `number`, `number`, `enum`, `integer` | `maxit=2000` | `light` | `dp` |
| `st_density` | `fit` | `raw_handle`, `integer` | `n=512` | `light` | — |
| `st_shortfall` | `fit` | `raw_handle`, `number`, `enum` | `prob=0.05` | `light` | — |

### Use when

you have conditional quantiles (from #64 GaR) and you want the FULL growth density: quantile matching to a skew-t (Adrian-Boyarchenko-Giannone 2019) -> density/CDF + expected shortfall / downside risk

### Do not use when

you only want the quantiles (stop at #64); you have a raw sample of returns (VaR/ES directly -> #65); you want an MLE skew-t regression on raw data (selm, outside the surface); non-monotone probs (crossing) -> fix that first

### Prerequisites

- c12_distribution_risk/quantile_regression.qr_growth_at_risk (produces the conditional quantiles input -> probs/quantiles)
- st_fit_quantiles (the fit; st_density/st_shortfall take the fit object)

### Alternatives

| instead use | when |
| --- | --- |
| #64 quantreg (stop at the quantiles) | you do not need the full density/ES, only the GaR/upside points |
| #65 PerformanceAnalytics VaR/ES | you have a raw sample of returns (not conditional quantiles) -> historical/Gaussian/modified VaR |
| selm (MLE on raw data) | you want a full ML skew-t regression, not quantile matching (outside the wrapper) |
| fix_nu | a small/noisy quantile set -> lock nu (e.g. 5) for stability |

### Output fields

- dp: c(xi=location, omega=scale, alpha=slant, nu=df) — the fitted skew-t parameters
- objective/rmse: weighted SSE / rmse of fitted vs target quantiles (small = a good fit)
- fitted_quantiles vs target_quantiles: for a visual check of fit quality (chart-data)
- st_density: {x, pdf, cdf} grid (chart-ready full density/CDF)
- st_shortfall: {var, es, mean, median} — VaR=quantile, es=Expected Shortfall (ABG downside)
- convergence: 0 = converged (hard gate: !=0 -> stop)

### Pitfalls

- alpha<0 => negative skewness (a heavy left tail) = the ABG «vulnerable growth» case; alpha>0 = right skew
- a small nu (->2) => heavy tails => a much more negative ES; nu<=2 is blocked (infinite variance)
- quantile CROSSING in the #64 conditional quantiles => non-monotone => gate stop (an invalid distribution) — fix the crossing first
- quantile matching != MLE: the fit is to the quantile points, not to raw data; its quality depends on the number of quantiles & their spread
- ES = E[X\|X<=VaR] (the left tail); the right-side ES is the 'expected longrise' (upper tail)
- CONVERGENCE gate: non-convergence of optim => stop (not a silently bad fit, as with rstan #68)

### References

- Adrian, Boyarchenko & Giannone 2019 AER 109(4):1263-1289 (Vulnerable Growth: skew-t on GaR quantiles)
- Azzalini & Capitanio 2003 JRSS-B 65(2):367-389 (skew-t distribution)
- sn reference manual (qst/dst/pst, direct parametrization)

## #191 — Extreme Value Theory — GEV block maxima & GP/PP/Gumbel/Exponential threshold exceedances + return levels

**Module:** `extreme_value_theory.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `evt_fevd` | `x` | `num_array`, `enum`, `enum`, `number`, `string`, `string` | `type='GEV'`, `method='MLE'`, `time_units='days'`, `period_basis='year'` | `light` | `object` |
| `evt_return_level` | `object` | `raw_handle`, `num_array`, `boolean`, `number` | `do_ci=True`, `conf_level=0.95` | `light` | — |
| `evt_threshold_diag` | `x` | `num_array`, `enum`, `integer`, `number`, `num_array` | `type='GP'`, `nint=10`, `alpha=0.05` | `light` | — |

### Use when

modelling the TAIL (tail risk) of a series: the size/frequency of extreme events, return levels/return periods (e.g. a 1-in-100 loss), stress thresholds — through the GEV (block maxima) or GP Peaks-Over-Threshold (POT)

### Do not use when

you care about the body of the distribution (not the tail); a single fixed-quantile VaR/ES suffices (-> #65 PerformanceAnalytics); a conditional/time-varying tail (GARCH-EVT or #64 quantile-regression GaR); non-stationary EVT with covariates (out of scope here)

### Prerequisites

- evt_threshold_diag (POT: choose the threshold BEFORE the GP/PP fit — mean-residual-life linearity + parameter stability)
- c01_preparation_prechecks/unit_root_normality.run_adf_test (check stationarity/approximate iid behaviour: stationary EVT assumes approximately iid exceedances)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading a loss/return series from a file)

### Alternatives

| instead use | when |
| --- | --- |
| #65 pa_var / pa_expected_shortfall (PerformanceAnalytics) | you want a fast historical/gaussian/Cornish-Fisher VaR/ES without a tail model — NO extrapolation beyond the sample |
| #64 qr_growth_at_risk (quantreg) | a conditional tail (Growth-at-Risk) with covariates rather than an unconditional EVT tail |
| type='GP' (POT) instead of 'GEV' | you have the whole series (not only block maxima) -> POT exploits more tail data |
| type='GEV'/'Gumbel' block maxima | only periodic maxima are available (e.g. annual), or there is no clean threshold |

### Output fields

- par: a named vector of parameters — GEV/PP {location,scale,shape}; GP {scale,shape}; Gumbel {location,scale}; Exponential {scale}. shape>0 a heavy tail (Frechet); shape<0 bounded (Weibull); shape~0 light (Gumbel)
- se/cov_theta: standard errors + covariance (MLE/GMLE); NULL for Lmoments; nllh/AIC/BIC for model comparison (NULL for Lmoments)
- threshold/rate/npy/n_exceed: (GP/PP/Exp) the threshold, the exceedance rate, npy=the number of observations per period_basis (it sets the base of the return periods), the number of exceedances
- convergence/converged: the optim code (0=ok); the converged flag (an NA convergence code from Lmoments counts as ok) — ALWAYS read it (a stateless node: stderr is lost)
- evt_return_level: return_periods + estimate + ci_lower/ci_upper (delta method) — chart-data for a return-level plot
- evt_threshold_diag: mrl_* (mean residual life + CI) & stab_* (t.scale/shape + CI) per threshold — the grids for threshold selection (NO plot)

### Pitfalls

- npy trap: for GP/PP, time_units sets npy (the default 'days'->365.25). Wrong time_units => the return levels are interpreted on the WRONG base (e.g. 'annual' on monthly data). Set time_units correctly and read npy from the output
- the sign of shape = the tail regime: shape>0 (Frechet, a heavy tail, infinite moments of order>1/shape); shape<0 (Weibull, a bounded upper tail); shape≈0 (Gumbel/exponential). Large \|shape\| with few exceedances is unstable
- threshold bias-variance: too low a threshold -> bias (a non-asymptotic GP); too high -> variance (few exceedances). evt_threshold_diag shows the lowest u above which the mean excess (linear) & shape stabilise
- return period > 1: every return period must be > 1 (rlevd); the 100-year level = the 1-1/100 quantile, NOT 'the maximum in 100 years'. The normal-approximation CIs understate the uncertainty far into the tail
- Lmoments: robust but WITHOUT SE/AIC/nllh (se=NULL); GEV/GP only. For model comparison/inference use MLE/GMLE. GMLE helps when the MLE shape is unstable (a small sample)

### References

- Gilleland & Katz, extRemes 2.0: An Extreme Value Analysis Package, JSS 2016 (help('fevd','extRemes'), 'return.level', 'mrlplot', 'threshrange.plot')
- Coles 2001, An Introduction to Statistical Modeling of Extreme Values (GEV/GP, threshold selection, return levels)
- Embrechts, Kluppelberg & Mikosch 1997, Modelling Extremal Events for Insurance and Finance (POT, tail index)
- McNeil, Frey & Embrechts 2015, Quantitative Risk Management 2nd ed. §5-7 (EVT VaR/ES, mean excess)

## #192 — Expectile-based extreme tail risk (extreme/intermediate expectiles + marginal expected shortfall + the heavy-tail index)

**Module:** `expectile_extreme_tail.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `er_expectiles` | `data`, `tau` | `num_array`, `number`, `number`, `enum`, `enum`, `boolean`, `enum`, `boolean`, `integer`, `integer`, `integer`, `number` | `var=True`, `bias=False`, `alpha=0.05` | `light` | — |
| `er_mes` | `data`, `data2`, `tau`, `tau1` | `num_array`, `num_array`, `number`, `number`, `enum`, `enum`, `boolean`, `enum`, `boolean`, `integer`, `integer`, `integer`, `number` | `var=True`, `bias=False`, `alpha=0.05` | `light` | — |
| `er_tail_index` | `data`, `k` | `num_array`, `integer`, `number`, `boolean`, `enum`, `boolean`, `integer`, `integer`, `number` | `var=True`, `bias=False`, `alpha=0.05` | `light` | — |

### Use when

a heavy-tailed financial series (fat tails, gamma>0); you want coherent tail-risk measures BEYOND the sample — extreme expectiles (asymmetric minimization, coherent), the systemic marginal expected shortfall E[Y\|X extreme], or the heavy-tail index gamma with asymptotic CIs

### Do not use when

light-tailed/bounded data (gamma~0; the Hill estimator breaks down); a small n (<~100 for an extreme level); a plain in-sample historical/gaussian VaR-ES (go to PerformanceAnalytics); a quantile-based conditional GaR with covariates (go to quantreg)

### Prerequisites

- er_tail_index (the Hill gamma>0 & its CI: confirm the heavy tail BEFORE the extreme measures; gamma>=0.5 -> infinite variance)
- c01_preparation_prechecks/unit_root_normality.run_adf_test (EVT wants (approximately) stationary data, not trending levels)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading a return series from a file)

### Alternatives

| instead use | when |
| --- | --- |
| 12-distribution-risk/pa_expected_shortfall | in-sample ES/CVaR (historical/gaussian/Cornish-Fisher) without extrapolation beyond the sample |
| 12-distribution-risk/qr_growth_at_risk | a conditional downside quantile with covariates (Growth-at-Risk), not an unconditional extreme tail |
| er_mes estimator='expectile' (ExpectMES) | coherent expectile-based systemic risk rather than the quantile-based QuantMES |
| er_expectiles method='QB' | the quantile-based indirect estimator when the direct LAWS one is unstable at the extreme level |

### Output fields

- er_expectiles: expectile (the point estimate), level (intermediate/extreme), variance + ci_lower/ci_upper (the asymptotic CI; NA if var=FALSE), biasTerm
- er_mes: mes (E[series1\|series2 extreme]), estimator (quantile/expectile), variance + ci_lower/ci_upper, conf_level
- er_tail_index: hill_gamma (Hill), hill_ci_lower/upper, hill_bias, eb_gamma (expectile-based; NA if tau was not supplied)
- object: the package's full raw list (HatQMES/gammaHat/ExpctHat etc.)

### Pitfalls

- tau is the INTERMEDIATE level (tau_n->1); tau1 is the EXTREME level; tau1 > tau is required — reversing them -> a silently wrong prediction (the gate blocks it)
- MES DIRECTION: MES = E[series1 (data) \| series2 (data2) extreme]; data2 is the conditioning/systemic variable (column 2 internally), NOT data
- an expectile != a quantile: the expectile minimises an asymmetric squared loss (a coherent risk measure); it is not the tau-quantile
- gamma (the tail index) = 1/alpha (Pareto); gamma>=0.5 -> infinite variance, gamma>=1 -> an infinite mean; this is critical for the validity of the measures
- k (the intermediate sequence) is a bias-variance tradeoff: a small k -> high variance, a large k -> bias; k>=n or k=0 silently give NA/0 (the gate blocks them)
- the asym-Dep variance requires bigBlock/smallBlock (big blocks separated by small blocks); without them the variance is blocked by a clean gate instead of a cryptic error
- fully deterministic: the CIs are ASYMPTOTIC (closed form), NOT bootstrap — no dependence on a seed

### References

- Padoan, S.A. & Stupfler, G. (2022). Joint inference on extreme expectiles for multivariate heavy-tailed distributions. Bernoulli 28(2)
- Davison, A.C., Padoan, S.A. & Stupfler, G. (2023). Tail Risk Inference via Expectiles in Heavy-Tailed Time Series. JBES 41(3) 876-889
- Daouia, A., Girard, S. & Stupfler, G. (2018). Estimation of tail risk based on extreme expectiles. JRSS-B 80, 263-292
- Hill, B.M. (1975). A simple general approach to inference about the tail of a distribution. Annals of Statistics 3, 1163-1174

## #193 — Conditional & unconditional expectiles (Expectiles-at-Risk / a GaR analogue, LAWS)

**Module:** `conditional_unconditional_expectiles.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `exr_expectile_reg` | `formula`, `data` | `formula`, `df_handle`, `enum`, `enum`, `number`, `number`, `integer` | `lambda=1`, `seed=2025` | `light` | — |
| `exr_expectile` | `x` | `num_array`, `number`, `integer` | `dec=4` | `light` | — |

### Use when

you want least-asymmetrically-weighted-squares expectile curves in the tails of the conditional distribution — an Expectile-at-Risk / GaR analogue sensitive to the MAGNITUDE of the tail; or the unconditional expectile of a vector

### Do not use when

you want a plain quantile/VaR (non-crossing, robust to outliers) -> #64 quantreg; you want a full density forecast/skew-t -> #95 sn; you want a closed-form ES/CVaR -> #65 PerformanceAnalytics

### Prerequisites

- exr_expectile (the unconditional expectile: an asymmetry benchmark before the conditional fit)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the panel/series data_frame first)
- c12_distribution_risk/quantile_regression.qr_growth_at_risk (compare with the GaR quantile before choosing an expectile)

### Alternatives

| instead use | when |
| --- | --- |
| #64 qr_growth_at_risk (quantreg) | you want the quantile/VaR interpretation (P[Y<q]=tau), robustness to outliers, non-crossing |
| #95 st_fit_quantiles (sn) | you want a FULL parametric density forecast (skew-t) rather than tail points |
| estimate='restricted'/'sheets' | the expectile curves cross -> impose monotonicity/no crossing |
| smooth='schall' vs 'fixed' | you want automatic selection of lambda (schall/gcv) rather than a manual lambda |

### Output fields

- asymmetries: the expectile levels (asymmetry weights) that were estimated
- intercepts: the expectile-specific intercept per level
- coefficients: a list per covariate — a matrix [1 x #levels] of the effects per expectile
- fitted: an n x #levels matrix with the conditional expectile curves (chart-data)
- lambda: the smoothing parameters per term (after schall/gcv/.. or fixed)
- expectiles (exr_expectile): one unconditional expectile per prob (0.5 = the arithmetic mean)

### Pitfalls

- an expectile ≠ a quantile: the tau-expectile does NOT satisfy P[Y<=e]=tau; it is asymmetric L2 (sensitive to the magnitude of the tail, NOT robust to outliers the way a quantile is)
- the 0.5-expectile EQUALS the (conditional) mean, not the median
- estimate='laws' does NOT guarantee non-crossing expectile curves; use restricted/bundle/sheets if they cross
- smooth='fixed' -> lambda is used as supplied; schall/gcv/ocv select it automatically (the returned lambda then differs from the input)
- the package is attached TEMPORARILY inside the call (its Depends on Matrix/mboost mask generics) and detached afterwards — no permanent pollution of the search path
- probs endpoints 0/1 in exr_expectile give the min/max; in the conditional fit the levels must lie strictly in (0,1)

### References

- Schnabel & Eilers 2009, 'Optimal expectile smoothing', CSDA 53:4168 (expectreg.ls, LAWS)
- Newey & Powell 1987, 'Asymmetric least squares estimation and testing', Econometrica 55:819
- Sobotka & Kneib 2012, 'Geoadditive expectile regression', CSDA 56:755 (restricted/bundle/sheets)
- help('expectreg.ls','expectreg'), help('expectile','expectreg') — expectreg 0.54
- Bellini & Di Bernardino 2017, 'Risk management with expectiles', Eur. J. Finance 23:487 (Expectile-at-Risk)

## #194 — Joint (VaR, ES) regression (Fissler-Ziegel) + an ESR-based Expected Shortfall backtest

**Module:** `joint_regression_esr.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `es_joint_reg` | `formula`, `data`, `alpha` | `formula`, `df_handle`, `number`, `enum`, `enum`, `integer`, `integer` | `early_stopping=10`, `seed=2025` | `light` | `object` |
| `es_backtest` | `r`, `q`, `e`, `alpha` | `num_array`, `num_array`, `num_array`, `number`, `enum`, `integer`, `enum`, `enum`, `boolean`, `integer` | `B=0`, `misspec=True`, `seed=2025` | `heavy` | — |

### Use when

jointly modelling Value-at-Risk & Expected Shortfall as functions of covariates (semiparametric FZ scoring); or evaluating (backtesting) external ES forecasts against realised returns

### Do not use when

a single quantile (VaR only) -> quantreg #64; an unconditional VaR/ES from history/Gaussian -> PerformanceAnalytics #65; a coverage-only VaR backtest (Kupiec/Christoffersen) -> not here; you need a full predictive distribution -> density forecasting #94 / skew-t #95

### Prerequisites

- es_backtest (post: backtest the VaR/ES forecasts; H0 is correct calibration -> you want a LARGE p-value)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load returns + covariates into a data_frame before es_joint_reg)

### Alternatives

| instead use | when |
| --- | --- |
| #64 qr_regression / qr_growth_at_risk (quantreg) | you want only the conditional quantile/VaR (Growth-at-Risk), not the ES jointly |
| #65 pa_expected_shortfall (PerformanceAnalytics) | an unconditional ES/CVaR from a return series without covariates |
| g2=4 or 5 | the ES forecasts/estimates are not guaranteed negative (types 1-3 require a negative domain) |
| es_backtest version=2 (Auxiliary ESR) | you want to test the ES given the VaR (regressing on q & e) rather than a strict ES-only test |

### Output fields

- es_joint_reg coefficients: named (bq_0. the VaR equation; be_0. the ES equation); coefficients_q / coefficients_e: the two parts separately
- es_joint_reg std_errors: asymptotic sandwich SE (NA if the vcov failed); loss: the Fissler-Ziegel score at the optimum; nobs
- es_joint_reg vcov_ok/vcov_note: a convergence/degeneracy flag — FALSE => the vcov failed or gave negative variances (a small/degenerate sample)
- es_backtest pvalue_twosided_asymptotic: the main p-value; version 3 adds pvalue_onesided_asymptotic; the pvalue_*_bootstrap fields fill only when B>0
- es_backtest es_all_negative: FALSE => the ES forecasts are not all negative (a possible domain violation for G2 types 1-3 -> a suspect p-value)

### Pitfalls

- the backtest H0 = the forecasts are correct; a SMALL p-value => REJECTION (a bad risk model), not the other way round
- a singular design matrix in es_backtest: q/e are nearly constant — you need time-varying risk forecasts
- es_joint_reg std_errors=NA (vcov_ok=FALSE): the asymptotic sandwich fails on small/degenerate samples -> increase n or check collinearity, do NOT read the point estimates as significant
- es_all_negative=FALSE: the G2 scoring functions (types 1-3) require negative ES forecasts; positive values silently produce a suspect p-value
- version 3 (Strict Intercept) tests whether the ES of the forecast error r-e is zero; version 1 (Strict ESR) regresses the returns on e only; a different hypothesis, they are not interchangeable
- the bootstrap p-values (pvalue_*_bootstrap) are NA when B=0; they are stochastic -> set.seed(seed=2025) for reproducibility

### References

- Dimitriadis & Bayer 2019, 'A joint quantile and expected shortfall regression framework' (Electronic J. Statistics 13:1823)
- help('esreg','esreg'), help('vcovA','esreg'), G1_fun/G2_fun ( esreg 0.6.2)
- Bayer & Dimitriadis 2022, 'Regression-based expected shortfall backtesting' (J. Financial Econometrics 20:437, doi:10.1093/jjfinec/nbaa013)
- help('esr_backtest','esback') ( esback 0.3.1)
- Fissler & Ziegel 2016 (Annals of Statistics 44:1680, joint elicitability of VaR & ES)

## #195 — Quantile Regression Forests (nonparametric conditional quantiles / Growth-at-Risk)

**Module:** `quantile_regression_forests.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `qrf_fit` | `x`, `y` | `matrix_handle`, `num_array`, `integer`, `integer`, `integer`, `integer` | `ntree=200`, `nodesize=5`, `seed=2025` | `light` | `object` |
| `qrf_predict` | `object`, `newdata` | `raw_handle`, `matrix_handle`, `num_array` | `quantiles=[0.1, 0.5, 0.9]` | `light` | — |

### Use when

non-parametric conditional quantiles y\|x with non-linearities/interactions & many predictors; a lower-tail quantile = a nonparametric Growth-at-Risk without imposing a linear form

### Do not use when

you want interpretable coefficients/inference per covariate -> #64 quantreg; a very small n (the trees over-fit and the OOB R² is unreliable); a purely time-series volatility-driven tail -> GARCH; a descriptive tail without covariates -> #65

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the (X,y) frame of predictors+response; clean the NA first — the forest does NOT accept NA)
- qrf_predict (conditional quantiles at new x; the mandatory second link after qrf_fit)
- c12_distribution_risk/quantile_regression.qr_growth_at_risk (the parametric linear GaR as a benchmark/cross-check)

### Alternatives

| instead use | when |
| --- | --- |
| #64 quantreg qr_growth_at_risk | you want linear, interpretable coefficients + analytic/bootstrap inference per covariate rather than a black-box forest |
| #95 sn skew-t (st_fit_quantiles) | you want the FULL growth density + expected shortfall from the fitted quantiles (ABG step 2) |
| grf quantile_forest (causal/honest forests) | you want honest splitting / treatment heterogeneity together with quantiles |
| brms distributional (cat. 14) | you want a full posterior / non-crossing quantiles / an explicit skew-t likelihood |

### Output fields

- qrf_fit: object (of class quantregForest -> a handle); ntree/nodesize/mtry/n/n_predictors/predictors; y_range (min/max)
- qrf_fit: rsq_oob/mse_oob (the OOB pseudo-R² & MSE diagnostics); degenerate (TRUE if rsq_oob=NA -> an unreliable fit)
- qrf_fit: importance (IncNodePurity per predictor; variable-importance chart-data); seed
- qrf_predict: predictions (a matrix n_new x length(quantiles); one column per quantile — chart-data); quantiles; n_new; colnames

### Pitfalls

- a factor y: quantregForest ACCEPTS a factor y at fit time but FAILS at the quantiles (a silent trap) — the wrapper blocks it in qrf_fit
- the trees do NOT guarantee non-crossing; with a small n/few trees check the monotonicity of the predictions across quantiles empirically
- the seed applies only to qrf_fit (stochastic bootstrap trees); qrf_predict is DETERMINISTIC (aggregating leaf values) — it takes no seed
- degenerate=TRUE (rsq_oob=NA) means a nearly constant response/an excessive nodesize -> the quantiles are nearly useless
- quantiles outside [0,1] are blocked cleanly (the package produced cryptic 'minimal/maximal values' errors)
- newdata must contain ALL the predictor columns from training (gate); a single quantile is normalised to a 1-column matrix

### References

- Meinshausen (2006) 'Quantile Regression Forests', JMLR 7:983-999
- quantregForest 1.4.0 help: help('quantregForest'), help('predict.quantregForest')
- Breiman (2001) Random Forests (Machine Learning 45:5-32; the randomForest engine)
- Adrian, Boyarchenko & Giannone (2019) 'Vulnerable Growth' AER 109:1263-1289 (the GaR context)

## #196 — Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs)

**Module:** `parametric_distribution_fitting.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fd_fit` | `data` | `num_array`, `enum`, `enum`, `num_array`, `enum`, `raw` | — | `light` | `object` |
| `fd_gof` | `object` | `raw_handle` | — | `light` | — |
| `fd_descdist` | `data` | `num_array`, `boolean`, `enum`, `integer`, `integer` | `discrete=False`, `boot=200`, `seed=2025` | `heavy` | — |
| `fd_bootdist` | `object` | `raw_handle`, `enum`, `integer`, `integer` | `niter=200`, `seed=2025` | `mcmc` | — |

### Use when

you have a univariate sample (returns/losses/counts) and you want to fit a parametric distribution, test how well it fits (KS/CvM/AD/chisq), and quantify the parameter uncertainty with a bootstrap

### Do not use when

regression/conditional quantiles (-> #64 quantreg); explicitly tail/EVT extremes (-> extRemes/ExtremeRisks); a time series with autocorrelation (fit the residuals, not the raw levels); censored data (fitdistcens — out of scope)

### Prerequisites

- fd_descdist (before the fit: the Cullen-Frey skewness/kurtosis -> which families are plausible)
- fd_gof (after the fit: KS/CvM/AD + AIC/BIC to compare candidate distributions)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the sample from CSV/TSV if needed)

### Alternatives

| instead use | when |
| --- | --- |
| #64 quantreg (Growth-at-Risk) | you want a conditional distribution/quantiles as a function of covariates, not an unconditional fit |
| extRemes / ExtremeRisks (EVT) | only the tail matters (block maxima / POT), not the whole distribution |
| sn skew-t (#95) | you want a skewed/heavy-tailed closed form fitted to already estimated quantiles |
| method='mge' instead of 'mle' | you want to minimise a GOF distance directly (tail-focused) rather than the likelihood |

### Output fields

- fd_fit: estimate (the named parameters) + sd (SE from the vcov); aic/bic/loglik for model selection; convergence/converged (0 = OK); distname/method/discrete
- fd_gof: ks/cvm/ad (the statistics; NA for discrete distributions); kstest/cvmtest/adtest (a verbal decision or 'not computed'); aic/bic; chisq/chisqpvalue/chisqdf (the main criterion for discrete distributions)
- fd_descdist: skewness/kurtosis + boot_skewness/boot_kurtosis (the Cullen-Frey cloud as chart-data); min/max/median/mean/sd; n
- fd_bootdist: CI (a matrix Median/2.5%/97.5% per parameter); boot_estimates (the full sample, chart-data); n_converged/conv_rate (degeneracy)

### Pitfalls

- silently wrong support: nbinom on negative values and pois on non-integers produce SILENTLY false estimates -> explicit gates per distribution (positive>0; beta∈(0,1); counts = non-negative INTEGERS)
- AIC/BIC are comparable ONLY across distributions on the SAME data with the same parameter-count penalty; lower = better, not absolute
- cvmtest/adtest = 'not computed' for distributions where the p-value is undefined (e.g. norm); this does NOT mean a good fit
- for discrete distributions (pois/nbinom) ks/cvm/ad are NA — judge from chisq/chisqpvalue
- the descdist bootstrap cloud is stochastic -> set.seed(2025); descdist itself does NOT return the cloud (only a plot) — it is reproduced explicitly here
- bootstrap CIs assume the correct family; check fd_gof first — a CI under the wrong distribution is misleadingly narrow

### References

- Delignette-Muller & Dutang, 'fitdistrplus: An the reference Package for Fitting Distributions', JSS 2015 64(4) (the fitdistrplus vignette)
- help('fitdist','fitdistrplus'), gofstat, descdist, bootdist (fitdistrplus 1.2.6)
- Cullen & Frey 1999, 'Probabilistic Techniques in Exposure Assessment' (the Cullen-Frey graph)
- Cramer-von Mises / Anderson-Darling GOF (Stephens 1986)

## #197 — Copula dependence + tail dependence + goodness of fit (joint stress)

**Module:** `copula_dependence_tail.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cop_fit` | `data` | `matrix_handle`, `enum`, `integer`, `enum` | `dim=2` | `light` | `object` |
| `cop_tail_index` | `object` | `raw_handle` | — | `light` | — |
| `cop_gof` | `object`, `data` | `raw_handle`, `matrix_handle`, `integer`, `enum`, `enum`, `integer` | `N=200`, `seed=2025` | `light` | — |

### Use when

modelling the DEPENDENCE of two (or more) series separately from the marginals; especially tail co-movement (crash/stress) in returns/losses; testing whether the candidate family fits the data

### Do not use when

univariate risk (the VaR/ES of one series -> #65); raw (non-uniform) data without pobs; temporal/dynamic dependence (a GARCH copula is out of scope); dim>2 for the tail index (it is defined only in the bivariate case)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the series; then convert them to pseudo-observations with pobs)
- cop_fit (fit FIRST; it produces the fitCopula handle for tail_index/gof)
- cop_gof (post: a parametric-bootstrap GoF; a large p means the family is not rejected)

### Alternatives

| instead use | when |
| --- | --- |
| family='clayton' | downside/crisis co-movement (lower-tail dependence; losses together) |
| family='gumbel' | upside co-movement / boom clustering (upper-tail dependence) |
| family='t' | symmetric tail dependence at both ends (heavy joint tails) |
| family='normal' or 'frank' | dependence without extreme tail co-movement (Gaussian/Frank -> lambda=0) |
| #65 PerformanceAnalytics VaR/ES | univariate downside risk of one series, not joint dependence |
| VineCopula (out of scope for now) | d>2 with asymmetric pairwise dependences (a regular vine) |

### Output fields

- cop_fit.estimate/std_errors: the named copula parameters (clayton=alpha, gumbel/frank=param, normal/t=rho[.1] + df for t); the SE come from the covariance (NA if it was not computed — e.g. the df of the t)
- cop_fit.loglik/aic/bic/kendall_tau: fit diagnostics; kendall_tau = the dependence of the fitted copula (NA if dim>2)
- cop_fit.convergence/converged: 0/TRUE = optim converged; NA for itau/irho (no optim)
- cop_tail_index.lower/upper: the coefficients of tail dependence in [0,1] (0 = asymptotic independence in that tail)
- cop_gof.statistic/p_value: the Cramer-von Mises Sn + a parametric-bootstrap p (H0 = the family fits; a SMALL p -> rejection)

### Pitfalls

- GoF polarity: a LARGE p_value is GOOD (the family is not rejected); a small p means the copula does NOT fit — the classic sign-reversal mistake
- tailIndex is DEPRECATED -> the wrapper uses lambda (the same lower/upper; it avoids a future breakage)
- clayton = the LOWER tail (co-crash); gumbel = the UPPER tail (co-boom); normal & frank give lambda 0 in both tails even when the overall correlation is high (the trap: a high rho does not imply tail dependence)
- the input MUST be pseudo-observations in [0,1]^d; fitCopula does NOT check the range (a silently wrong log-likelihood) — the wrapper blocks it with a hard gate; run pobs first
- the cop_gof p_value is STOCHASTIC (a parametric bootstrap with N replicates); the seed defaults to 2025 -> reproducible; a small N -> a noisy p
- tail_index is bivariate ONLY (dim==2); for dim>2 the function blocks explicitly

### References

- help('fitCopula','copula'), help('gofCopula','copula'), help('tailIndex','copula') ( copula 1.1-x)
- Hofert, Kojadinovic, Maechler & Yan 2018, 'Elements of Copula Modeling with the reference' (Springer)
- Genest, Remillard & Beaudoin 2009 (Insurance: Math. & Econ. 44:199, the parametric-bootstrap GoF Sn)
- Joe 2014, 'Dependence Modeling with Copulas' (CRC) §2 (tail dependence coefficients)
- Nelsen 2006, 'An Introduction to Copulas' 2nd ed. (Archimedean families)

## #198 — Regular-vine copulas — a pair-copula construction of the joint dependence (structure selection + loglik + simulate)

**Module:** `regular_vine_copulas.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `vine_select` | `data` | `matrix_handle`, `int_array`, `enum`, `enum`, `boolean`, `number`, `integer`, `boolean`, `enum` | `indeptest=False`, `level=0.05`, `rotations=True` | `light` | `object` |
| `vine_loglik` | `object`, `data` | `raw_handle`, `matrix_handle`, `boolean` | `separate=False` | `light` | — |
| `vine_sim` | `object`, `N` | `raw_handle`, `integer`, `integer` | `seed=2025` | `light` | — |

### Use when

multivariate (d>=2) dependence with tail dependence/asymmetry beyond linear correlation; the input is pseudo-observations with uniform [0,1] margins (PIT/rank); you want a flexible joint model + scenario simulation

### Do not use when

linear correlation/Gaussian dependence suffices (use the covariance); raw returns without a margin transform (apply PIT/pobs first); temporal dependence/volatility (06-volatility); d=1

### Prerequisites

- vine_loglik (in-sample vs holdout loglik: is the structure over-fitted?)
- vine_sim (a posterior-predictive check: simulated vs empirical dependence)
- c00_data_utilities/reading_delimited_fixed.read_delimited (load the pseudo-observations)

### Alternatives

| instead use | when |
| --- | --- |
| a single Gaussian/Student-t copula | symmetric dependence suffices; the pair-copula flexibility is not needed |
| sn skew-t (#95) | univariate/bivariate tail risk without a full vine |
| PerformanceAnalytics component VaR (#65) | portfolio risk decomposition under linear assumptions |
| type='CVine' | there is one dominant variable driving the whole dependence (a star structure) |

### Output fields

- Matrix: the lower-triangular structure matrix of the vine (which pairs sit in each tree)
- family / family_names: the pair-copula codes & names per position (0 = independence)
- par / par2: the parameters of each pair copula (par2 only for t/two-parameter families)
- tau: the implied Kendall's tau per pair; log_lik / AIC / BIC: the fit-time goodness
- all_independence: TRUE if ALL families = 0 (a degenerate, independent vine)
- vine_loglik: loglik (a scalar or per observation), AIC, BIC, npars on NEW data
- vine_sim: sim = an NxD matrix of simulated pseudo-observations in [0,1] (chart-data)

### Pitfalls

- the input MUST be pseudo-observations in [0,1] (PIT/rank) — NOT raw returns; NA are blocked explicitly (VineCopula silently uses pairwise-complete data)
- family=0 at a position means an independence copula there; all_independence=TRUE => the vine found no dependence at all
- the par values are interpreted PER family (a Clayton theta != a Gumbel theta != a Frank one); read family_names alongside par
- the AIC/BIC from vine_loglik are computed on the SUPPLIED data (for a holdout comparison); the fit-time AIC/BIC from vine_select are on the training set
- vine_sim is STOCHASTIC -> the same seed => identical output (default 2025); the output is in copula space [0,1], an inverse margin transform is needed for return space
- CVine vs RVine: a CVine imposes a star structure per tree (less flexible); the default is RVine (the Dissmann greedy MST)

### References

- Aas, Czado, Frigessi & Bakken 2009, 'Pair-copula constructions of multiple dependence', Insurance: Math. & Econ. 44:182-198
- Dissmann, Brechmann, Czado & Kurowicka 2013, 'Selecting and estimating regular vine copulae', CSDA 59:52-69 (the RVineStructureSelect algorithm)
- VineCopula 2.6.1 help: RVineStructureSelect, RVineLogLik, RVineSim, RVineMatrix, BiCop, BiCopName
- Czado 2019, Analyzing Dependent Data with Vine Copulas (Springer Lecture Notes in Statistics)

## #199 — SDE scenario generation (short-rate/asset diffusion paths) + a martingale no-arbitrage check

**Module:** `sde_scenario_generation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `esg_simdiff` | `params` | `enum`, `raw`, `number`, `integer`, `integer`, `integer` | `T=1`, `n_steps=100`, `n_paths=200`, `seed=2025` | `light` | `object` |
| `esg_martingale_test` | `object` | `raw_handle`, `number` | `conf_level=0.95` | `light` | — |

### Use when

generating stochastic scenarios (Monte Carlo paths) for a short rate (Vasicek/CIR/OU) or an asset (GBM); stress testing/ESG cash-flow projection; checking the no-arbitrage property of the simulation

### Do not use when

you want to ESTIMATE SDE parameters from data (qmle — out of scope); jump/Levy/COGARCH dynamics; fitting a distribution to fitted quantiles (-> #95 sn skew-t); VaR/ES on historical returns (-> #65 PerformanceAnalytics)

### Prerequisites

- esg_simdiff (run it FIRST; its object output is the input to esg_martingale_test)
- esg_martingale_test (a validation gate: E[exp(-∫r)] ≈ the closed-form P(0,T); vasicek/cir only)

### Alternatives

| instead use | when |
| --- | --- |
| #65 pa_var / pa_expected_shortfall (PerformanceAnalytics) | VaR/ES on HISTORICAL returns, not a forward-looking simulation |
| #95 st_fit_quantiles (sn skew-t) | a closed-form parametric distribution on fitted quantiles rather than path simulation |
| the yuima jump/Levy/qmle extension | jumps, heavy tails, or parameter estimation from data (a future node) |

### Output fields

- paths: a NUMERIC matrix (rows=time=n_steps+1, cols=paths) — chart-data; paths[1,]=xinit
- time: the grid [0.T] of length n_steps+1; terminal_values: the values at T per path
- summary_mean / summary_quantiles: the per-time mean & q5/q25/q50/q75/q95 (fan chart)
- feller_ok: (CIR only) 2*kappa*theta >= sigma^2 — otherwise NA; a degeneracy flag, not hard
- esg_martingale_test: {theoretical_price, empirical_mean, diff, mc_se, within_ci, n_paths}

### Pitfalls

- within_ci=TRUE => the simulation is consistent with no arbitrage (the deflated bond ≈ the closed-form P(0,T)); FALSE => Euler bias / too few paths / wrong parameters
- vasicek and ou are THE SAME SDE (theta*(mu-x)dt+sigma dW); a different label, identical dynamics
- esg_martingale_test is gated to {vasicek,cir}; gbm/ou (asset models) have NO bond price -> a hard stop, not a silent mistake
- CIR under Euler can occasionally approach 0; feller_ok=FALSE warns of a possible loss of positivity
- the seed defaults to 2025; the same seed => bit-identical paths (node reproducibility)

### References

- Brouste et al. 2014, 'The YUIMA Project', JSS 57(4) <https://www.jstatsoft.org/v57/i04/>
- Vasicek 1977 (J. Financial Economics 5:177) — the closed-form P(0,T)
- Cox, Ingersoll & Ross 1985 (Econometrica 53:385) — the CIR closed-form P(0,T)
- It replaces the -archived ESGtoolkit (simdiff + esgmartingaletest)
