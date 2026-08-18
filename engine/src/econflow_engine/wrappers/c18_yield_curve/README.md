<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 18-yield-curve

4 METHOD-SELECTION cards, 4 modules, 6 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #87 — Nelson-Siegel / Svensson / Diebold-Li yield-curve factors

**Module:** `nelson_siegel_svensson.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fit_nelson_siegel` | `rates`, `maturities` | `matrix_handle`, `matrix_handle` | — | `light` | — |
| `fit_svensson` | `rates`, `maturities` | `matrix_handle`, `matrix_handle`, `enum` | — | `light` | — |

### Use when

compressing the cross-section of yields by maturity into level/slope/curvature factors (NS/Diebold-Li) or a 4-factor Svensson for a second hump; typically as an input to the recession probit #83

### Do not use when

you want a no-arbitrage/affine term premium (ACM/ABG), or only the simple 10y-2y slope spread, or time-series stationarity/cointegration of one tenor (01/05)

### Alternatives

| instead use | when |
| --- | --- |
| fit_nelson_siegel (NS / Diebold-Li 3-factor) | the default macro-factor extraction; few pillars (>=4), stability, interpretability |
| fit_svensson (4-factor) | curves with a second hump, a rich tenor grid (>=6 pillars), a better long-end fit |
| a plain slope spread (10y-2y), outside the category | you only want a recession slope indicator, not a full factor fit |
| affine no-arbitrage term premium (ACM/ABG) | you want a decomposition into expectations vs term premium — outside YieldCurve |
| recession probit #83 | the natural consumer of the extracted factors — run it after the fit |

### Output fields

- model: Nelson.Siegel or Svensson
- factors: xts of the factors per date (NS: beta_0,beta_1,beta_2,lambda; Svensson: beta_0.beta_3,tau1,tau2)
- factors_df: chart-ready data_frame with a date column + factors
- fitted_rates: xts of fitted yields per maturity
- residuals: xts of observed - fitted per pillar
- which_rate: Spot (default) or Forward (Svensson only)
- interpretation: mapping beta_0=level, beta_1=slope, beta_2=curvature,..
- n_obs / n_maturities: number of dates / pillars

### Pitfalls

- Svensson which_rate: the default MUST be Spot; with Forward the fitted/residuals silently become the wrong quantity (the instantaneous forward instead of the spot) — adversarial-review HIGH
- lambda/tau are decay rates (the hump position), NOT yields — do not feed them into a probit as a spread
- the sign of the slope depends on the direction of the definition — read the interpretation field, do not assume
- this is a descriptive fit, NOT no-arbitrage — it does not separate expectations from the term premium
- an inconsistent maturity unit (months/years) distorts lambda and the fit

### References

- Diebold-Li 2006, Forecasting the Term Structure of Government Bond Yields, J. Econometrics 130
- Nelson-Siegel 1987, J. Business 60
- Svensson 1994, IMF WP 94/114
- YieldCurve reference manual (Guirreri): Nelson.Siegel/NSrates/Svensson/Srates
- wrapper footer IMPLEMENTATION NOTE + adversarial-review HIGH (which_rate default=Spot)

## #210 — Parametric yield-curve factor models (Nelson-Siegel / Svensson / cubic spline, Diebold-Li dynamics on a panel) + curve transforms (spot/forward/discount/PCA)

**Module:** `parametric_yield_curve.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `yc_fit` | `maturities` | `num_array`, `num_array`, `matrix_handle`, `enum`, `enum`, `number`, `number`, `number`, `num_array`, `series_codes` | `tau_init=1`, `tau1_init=1`, `tau2_init=5` | `light` | `object` |
| `yc_transform` | `object` | `raw_handle`, `enum`, `num_array`, `number`, `enum`, `integer`, `boolean` | `n_components=3`, `scale=False` | `light` | — |

### Use when

you have observed yields by maturity (a single cross-sectional curve AS a vector, or a time series of curves AS a time × maturity matrix) and you want (a) to compress them into level/slope/curvature factors (+ the extra Svensson term) with an explicit decay lambda, or (b) Diebold-Li factor dynamics (a Nelson-Siegel fit per date on a panel), or (c) to produce forward rates / discount factors / spot rates on a free maturity grid, or a PCA (Litterman-Scheinkman) of a yield panel

### Do not use when

you have coupon-bond cash-flow micro data (prices+coupons, not ready spot yields) -> #212 ycevo_estimate (nonparametric); you want a no-arbitrage/affine term-premium decomposition (ACM/ABG expectations vs term premium) — this is a descriptive fit ONLY, out of scope; you only want the simple 10y-2y slope spread (a transform, cat. 00); time-series stationarity/cointegration of one tenor (cat. 01/05); fewer pillars than parameters (NS<4, Svensson<6, cubic<3 = underdetermined)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the yields — one curve or a time × maturity panel)
- yc_fit (the fit of one curve; register field='object' -> it feeds yc_transform as a handle)
- c18_yield_curve/nelson_siegel_svensson.fit_nelson_siegel (the xts-based baseline; compare the factors before changing method)

### Alternatives

| instead use | when |
| --- | --- |
| 18-yield-curve/fit_nelson_siegel | you want an xts/Date-indexed factor series ready as an input to the recession probit #83; or Diebold-Li through the established YieldCurve interface |
| 18-yield-curve/fit_svensson | you want a 4-factor Svensson on an xts panel with a Spot/Forward which_rate choice |
| 18-yield-curve/ycevo_estimate | you have a coupon-bond cash-flow panel (not ready spot yields); you want a nonparametric time-varying discount/yield surface with no parametric shape |
| yc_transform (transform='pca') | you want empirical (data-driven) level/slope/curvature factors as loadings rather than a parametric Nelson-Siegel fit |
| affine no-arbitrage term premium (ACM/ABG) | you want an expectations vs term-premium decomposition — outside yieldcurves (a descriptive fit only) |

### Output fields

- yc_fit (one curve): factors {level,slope,curvature}; params (beta0.; tau/tau1/tau2); lambda (=1/tau; NS: lambda; Svensson: lambda1,lambda2; cubic: NA); fitted (chart-data yields); residuals; rmse; object (yc_curve, the register handle)
- yc_fit (a panel, Diebold-Li): factors, a matrix [dates × {level,slope,curvature}]; params [dates × params]; lambda [dates × lambda(s)]; fitted [dates × maturities]; rmse per date; object = the panel matrix (the register handle -> pca)
- yc_transform spot: maturity/rate on a grid (yc_predict); forward: maturity/forward_rate (instantaneous, or forward-forward with a horizon); discount: maturity/discount_factor (continuous/annual/semi_annual)
- yc_transform pca: loadings [tenors × components]; scores [obs × components]; variance_explained; cumulative_variance; sdev; center; tenors

### Pitfalls

- lambda = 1/tau is a decay rate (the hump position/loading), NOT a yield — do not use it as a spread; the NS lambda default comes from tau_init=1, but tau is estimated (optim), so the final lambda differs
- cubic_spline has no parametric beta/tau -> lambda=NA; its factors (level/slope/curvature) are computed empirically from the curve (yc_level_slope_curvature), not from beta coefficients — do not compare them one-to-one with the NS betas
- a panel + nelson_siegel = Diebold-Li: an INDEPENDENT fit per row (no common lambda/state space) — for joint dynamics run a VAR on the extracted factors (cat. 03)
- the PCA default scale=FALSE (covariance) is standard in yield-curve PCA; scale=TRUE (correlation) changes the loadings — do not confuse them; the sign of the loadings/scores is arbitrary (identifiability up to sign)
- the maturities must be STRICTLY INCREASING & positive; duplicates/unsorted values are accepted silently by the package (gate); an inconsistent unit (months vs years) distorts lambda and the fit
- a forward without a horizon = the instantaneous forward; with horizon>0 = a forward-forward rate (between maturity and maturity+horizon) — a different quantity, state it explicitly
- n_components in the pca is capped at min(n_obs-1, n_maturities); exceeding it -> the package silently reduces it (the gate blocks that)

### References

- the yieldcurves reference manual + help: yc_fit (dispatching yc_nelson_siegel/yc_svensson/yc_cubic_spline), yc_level_slope_curvature, yc_predict, yc_forward, yc_discount, yc_pca (live introspection, yieldcurves 0.1.0) <
- Nelson, C. R., & Siegel, A. F. (1987). Parsimonious Modeling of Yield Curves. Journal of Business, 60(4), 473-489
- Svensson, L. E. O. (1994). Estimating and Interpreting Forward Interest Rates: Sweden 1992-1994. IMF Working Paper 94/114
- Diebold, F. X., & Li, C. (2006). Forecasting the Term Structure of Government Bond Yields. Journal of Econometrics, 130(2), 337-364
- Litterman, R., & Scheinkman, J. (1991). Common Factors Affecting Bond Returns. Journal of Fixed Income, 1(1), 54-61 (PCA level/slope/curvature)

## #211 — Arbitrage-free affine (Gaussian) term-structure model — JSZ-style single-country JPS estimation with unspanned macro risks (risk-neutral Q + physical P parameters, model-implied yields, term-premia decomposition)

**Module:** `arbitrage_free_affine.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `atsm_estimate` | — | `enum`, `string`, `integer`, `series_codes`, `series_codes`, `string`, `string`, `enum`, `boolean`, `integer`, `boolean`, `matrix_handle`, `matrix_handle`, `matrix_handle` | `n_factors=1`, `stationary_Q=False`, `horizon=25`, `compute_term_premia=True` | `light` | — |

### Use when

you have a panel of bond yields (zero-coupon yields at many maturities) + macro factors (global & domestic) and you want an arbitrage-free affine model (JSZ/JPS): the risk-neutral (Q) + physical (P) dynamics of the risk factors, the model-implied (fitted) yields, and a DECOMPOSITION of the yield into the expected average short rate (the expectations component) + the TERM PREMIUM; unspanned macro risks (Eco_Act/Inflation) are incorporated beyond the spanned yield factors

### Do not use when

you want a simple static yield-curve fit for one date (Nelson-Siegel/Svensson -> YieldCurve/yieldcurves); you do not have a multi-maturity yield panel; you want multi-country GVAR-ATSM or JLL models (they need trade-flow weight matrices / a domestic-unit spec — outside this single-country node); you want a bias-corrected/bootstrap ensemble or out-of-sample yield forecasts (stochastic/heavy, excluded); macro data not in the strict format (yield rownames 'Y<mat>M_<economy>', macro '<var> <economy>', date colnames 'dd-mm-yyyy')

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the yield/macro panels as matrices; alternatively NULL -> the built-in 'CM_2024')
- c18_yield_curve/nelson_siegel_svenssons.yc_fit (a static Nelson-Siegel fit per date — a simpler alternative if you do not need a dynamic arbitrage-free model)
- atsm_estimate (the term-premia decomposition is returned inside it: term_premia + expected_component)

### Alternatives

| instead use | when |
| --- | --- |
| 18-yield-curve/yc_fit / nss_fit | you want only a static factor fit of the curve (level/slope/curvature) per date, NOT a dynamic arbitrage-free model with term premia |
| atsm_estimate (compute_term_premia=FALSE) | you want only the Q/P parameters + the maximum log-likelihood (faster, without the fit/term premia) |
| 10-trend-cycle-statespace/kf_fit | you want a general Gaussian state-space latent-factor model without no-arbitrage affine bond-pricing restrictions |

### Output fields

- max_llk: the maximum log-likelihood of the JSZ MLE estimation
- Q_params: the risk-neutral (Q) parameters {K1XQ (the Q-feedback eigenvalues), r0 (the short-rate intercept under Q), se (the measurement-error sd), VarYields (the per-maturity error variance)}
- P_params: the physical (P) VAR(1) dynamics of the risk factors {K0Z (the drift), K1Z (the feedback), SSZ (the innovation covariance)}
- fitted_yields / observed_yields: (time × maturities) model-implied vs observed yields + fit_rmse (chart-data)
- term_premia: (time × maturities) the term-premium component per maturity (chart-data)
- expected_component: (time × maturities) the expectations-hypothesis component (the average expected future short rate)
- maturities / sample_dates / n_obs / pc_var_explained: sample metadata & the PCA variance of the spanned factors; object = the full ATSMModelOutputs

### Pitfalls

- the identity yield = expected_component + term_premia: the term premium is the RESIDUAL above the expected future short rates; a negative term premium is valid (e.g. flight to quality)
- the input format is STRICT: yield series 'Y<mat>M_<economy>' (e.g. 'Y120M_Brazil'), macro '<var> <economy>', date colnames 'dd-mm-yyyy'; wrong rownames -> the economy gate blocks it; a wrong data_freq -> a silently wrong annualization of dt
- n_factors N = the country-specific SPANNED (yield-derived PCA) factors; N must be < the number of maturities; the macro variables (Eco_Act/Inflation) enter separately as UNSPANNED domestic factors (do not confuse them with N)
- single country only: 'JPS original' (domestic-only spanned+macro) vs 'JPS global' (it adds global factors to the P dynamics); GVAR/JLL/JPS-multi were excluded (the trade-weight/domestic-unit machinery)
- stationary_Q=TRUE enforces max\|eigenvalue\| under Q < 1 (a stable long-run curve); FALSE can produce explosive Q dynamics — check K1XQ
- masking: MultiATSM attaches `VAR` (DIFFERENT from VAR) + `autoplot` -> the wrapper calls MultiATSM:: namespaced (it does NOT use library); do not confuse it with the VAR nodes
- DETERMINISTIC (BFGS from a JSZ PCA/OLS initialisation, no RNG) -> no seed; the same input => the same max_llk

### References

- the MultiATSM vignette 'MultiATSM' + help: Optimization, InputsForOpt, LabFac, NumOutputs, InputsForOutputs (v1.5.1.2)
- Joslin, Singleton & Zhu (2011) 'A New Perspective on Gaussian Dynamic Term Structure Models', Review of Financial Studies 24(3):926-970 (the JSZ canonical form)
- Joslin, Priebsch & Singleton (2014) 'Risk Premiums in Dynamic Term Structure Models with Unspanned Macro Risks', Journal of Finance 69(3):1197-1233 (JPS)
- Candelon & Moura (2024) 'A Multicountry Model of the Term Structures of Interest Rates with a GVAR', Journal of Financial Econometrics 22(5):1558-1587
- Le & Singleton (2018) 'A Small Package of Matlab Routines for the Estimation of Some Term Structure Models', EABCN Training School

## #212 — Nonparametric time-varying yield curve / discount function estimation from coupon-bond cash-flow data (the Koo-La Vecchia-Linton kernel estimator)

**Module:** `nonparametric_time_varying.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ycevo_estimate` | `data`, `x` | `df_handle`, `series_codes`, `num_array`, `number`, `num_array`, `num_array`, `boolean` | `span_x=60`, `smooth=False` | `light` | — |

### Use when

you have coupon-bond cross-section+time-series micro data (a cash-flow panel: qdate, id, price, tupq=the time to the cash flow in days, pdint=the cash-flow amount) and you want to ESTIMATE non-parametrically the discount function d(tau,t) and the implied yield curve y(tau,t) that EVOLVE over time — without imposing a parametric shape (Nelson-Siegel/Svensson); appropriate for sparse/irregular coupon schedules

### Do not use when

you already have a matrix of spot yields by maturity (zero-coupon rates) — then #87 fit_nelson_siegel/fit_svensson (parametric factor fitting); you want level/slope/curvature factors for macro/probit work — #87; you want an affine term-structure/no-arbitrage model; you do not have cash-flow-level data (only aggregate yields); very few bonds/dates (the kernel estimator needs density around each x)

### Prerequisites

- c00_data_utilities/reading_delimited_fixed.read_delimited (load the bond cash-flow panel; the columns qdate/id/price/tupq/pdint)
- ycevo_estimate (the estimation returns the estimates + the yield/discount surface matrices inside it)

### Alternatives

| instead use | when |
| --- | --- |
| 18-yield-curve/fit_nelson_siegel | you already have spot yields by maturity and you want a parametric 3-factor (level/slope/curvature) fit rather than nonparametric cash-flow estimation |
| 18-yield-curve/fit_svensson | a parametric 4-factor (Svensson/Diebold-Li) fit on a ready spot curve |

### Output fields

- estimates: records {date, tau, discount, yield} — the estimated discount function + yield curve per (time, maturity) (chart-data)
- yield_matrix: a numeric matrix [tau × date] — the yield surface (rows=maturities, cols=dates)
- discount_matrix: a numeric matrix [tau × date] — the discount surface
- x: the estimation time points (dates); tau: the maturities that were used; span_x; smooth
- n_obs (cash-flow rows), n_bonds (unique ids), n_dates, n_tau; object: the fitted ycevo tibble (a nested.est)

### Pitfalls

- tupq is the time to EACH cash flow in DAYS (not years); pdint is the AMOUNT of the flow (a coupon, or a coupon+face value at maturity) — one row per (bond, cash flow), not per bond
- x must lie INSIDE the range of qdate and have enough data around it (the kernel window ~ span_x): an x in a sparse region or at the edges -> non-finite/unstable estimates (the wrapper hard-gates non-finite values)
- tau=NULL -> the package chooses ITS OWN dense maturity grid (percentiles of the observed maturities), not fixed pillars; supply an explicit tau for controlled maturities
- span_x is measured in the number of regular intervals between consecutive qdate values (e.g. trading days): a small span_x -> noise/overfitting, a large one -> over-smoothing over time
- smooth=TRUE applies a loess over tau (augment.ycevo loess=TRUE); with few tau values it produces 'span too small' warnings — the default FALSE returns the raw estimator points (deterministic)
- yield = -log(discount)/tau (a transformation of the discount factor); it is a continuously compounded spot yield per maturity, NOT a par/coupon yield

### References

- Koo, B., La Vecchia, D., & Linton, O. (2021). Estimation of a nonparametric model for bond prices from cross-section and time series information. Journal of Econometrics, 220(2), 562-588
- Nelson, C. R., & Siegel, A. F. (1987). Parsimonious Modeling of Yield Curves. Journal of Business, 60(4), 473-489 (the DGP for ycevo_data)
