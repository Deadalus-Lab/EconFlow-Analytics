<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 02-univariate-forecasting

10 METHOD-SELECTION cards, 10 modules, 30 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #7 — forecast (ARIMA/ETS/Theta/TBATS)

**Module:** `forecast.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_auto_arima` | `y` | `series_handle`, `integer`, `enum`, `boolean`, `boolean`, `exog_handle` | — | `light` | — |
| `run_ets` | `y` | `series_handle`, `string`, `boolean`, `integer`, `enum` | — | `light` | — |
| `run_theta` | `y` | `series_handle`, `integer` | — | `light` | — |
| `run_tbats` | `y` | `series_handle`, `boolean`, `boolean`, `boolean`, `boolean`, `integer` | — | `light` | — |

### Use when

univariate forecasting of one ts with automatic ARIMA/ETS, a robust Theta baseline, or TBATS for multiple/non-integer seasonalities

### Do not use when

multivariate structure (VAR/VECM), calendar holidays (prophet), intermittent/non-gaussian (smooth/ADAM)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test

### Alternatives

| instead use | when |
| --- | --- |
| #8 fable (ARIMA/ETS) | you want a tidy tsibble workflow or a <distribution> output / several models at once |
| #10 smooth ADAM | you need ETS+ARIMA+regression unified or a non-gaussian error |
| #9 prophet | holidays/calendar effects dominate |

### Output fields

- mean: point forecasts (ts -> {values,start,frequency})
- lower/upper: prediction interval bounds per level (matrix)
- level: confidence levels (80,95)
- fitted/residuals: in-sample one-step values for diagnostics
- accuracy: training-set measures (RMSE,MAE,MAPE,MASE,ACF1)
- model: fitted object (compact stub in to_mcp)

### Pitfalls

- accuracy(fc) is in-sample (training-set), NOT out-of-sample generalisation — for OOS use 15-model-evaluation (tsCV/DM) or a holdout
- MAPE is unstable/infinite when y≈0 (growth rates) — prefer MASE (<1 = better than naive)
- ETS/ARIMA prediction intervals assume gaussian innovations — they understate under heavy tails
- run_auto_arima gate: exog_handle not a data frame + NROW(exog_handle)==length(y); run_tbats gate: NCOL(y)==1
- y must be a ts with the correct frequency, otherwise a non-seasonal fit results

### References

- Hyndman & Athanasopoulos FPP3 (ARIMA/ETS)
- Hyndman & Khandakar 2008 JSS (forecast package / auto.arima)
- Assimakopoulos & Nikolopoulos 2000 (Theta); Hyndman & Billah 2003 (Theta=SES+drift)
- De Livera, Hyndman & Snyder 2011 JASA (TBATS)
- Hyndman, Koehler, Ord & Snyder 2008 (ETS state-space)
- forecast reference manual

## #8 — fable (tidy ARIMA/ETS)

**Module:** `fable.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_fable_arima` | `data`, `formula` | `df_handle`, `formula`, `enum`, `boolean`, `integer` | — | `light` | — |
| `run_fable_ets` | `data`, `formula` | `df_handle`, `formula`, `enum`, `enum`, `integer` | — | `light` | — |

### Use when

ARIMA/ETS in tidyverts (tsibble+formula) with <distribution> forecasts, manual pdq/PDQ, or components for ETS states

### Do not use when

a plain ts without the tsibble overhead (forecast); Theta/TBATS/multiple-seasonality (forecast); non-gaussian/intermittent (smooth)

### Prerequisites

- c00_data_utilities/replacement_missing_values.imputets_kalman (for ETS, if anyNA)
- c01_preparation_prechecks/unit_root_normality.run_adf_test

### Alternatives

| instead use | when |
| --- | --- |
| #7 forecast | non-tidy quick use or Theta/TBATS |
| #10 smooth ADAM | ETS+ARIMA+exog_handle together or a different error distribution |

### Output fields

- forecast: a fable with a <distribution> column -> quantile grid (probs+mean+sd); median≈point
- glance: 1-row sigma2/log_lik/AIC/AICc/BIC + ar_roots/ma_roots (complex -> {re,im})
- tidy: coefficients (term,estimate,std_error,statistic,p_value)
- components: ETS-only dable with states (level,slope,season)
- fitted/residuals: in-sample (type innovation vs regression)

### Pitfalls

- <distribution> is NOT a number — take median or mean, not the raw cell
- ar_roots/ma_roots are complex; stationarity/invertibility ⇒ modulus>1 (sqrt(re^2+im^2))
- glance does NOT compute accuracy — for OOS you need new_data + accuracy (15-model-evaluation)
- NA: ETS is a hard error (anyNA gate), ARIMA reverts with a warning — do not confuse them

### References

- Hyndman & Athanasopoulos FPP3 (tidy edition, fable)
- fable reference + vignette (ARIMA, ETS)
- fabletools docs (model, glance, <distribution>)

## #9 — prophet

**Module:** `prophet.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_prophet` | `df` | `df_handle`, `enum`, `enum`, `string`, `string`, `integer`, `string` | — | `heavy` | `model` |
| `run_prophet_cv` | `model`, `horizon`, `units` | `raw_handle`, `integer`, `string`, `integer`, `integer`, `number` | — | `heavy` | — |

### Use when

decomposable additive trend+seasonality(Fourier)+holidays+regressors with automatic changepoints; calendar effects, gaps/irregular index, an interpretable decomposition

### Do not use when

clean monthly/quarterly macro series without a calendar (ARIMA/ETS are more accurate); autoregressive dynamics; a very short series

### Alternatives

| instead use | when |
| --- | --- |
| #7/#8 ARIMA/ETS | clean low-frequency macro series without calendar structure |
| #10 smooth ADAM | explanatory regressors with state-space rigour |
| 18-intervention/structural | the objective is causal impact, not a forecast |

### Output fields

- forecast: df records; ds,yhat(point),yhat_lower/upper(interval),trend,*_terms(components)
- future: the future df (ds + regressors)
- regressor_coefficients: center/coef per regressor (only with regressors)
- cv: per cutoff yhat,y(actual),cutoff,ds,horizon (run_prophet_cv)
- metrics: horizon + mse/rmse/mae/mape/mdape/smape/coverage

### Pitfalls

- the default interval.width=0.8 ⇒ 80% intervals, NOT 95%
- without mcmc.samples>0 the intervals capture trend uncertainty only (MAP) — they understate
- run_prophet_cv is expensive (many re-fits)
- horizon/units in cross_validation are time units (180 days ≠ 180 monthly periods)
- coverage in metrics must be ≈ interval.width for calibrated intervals
- gates: seasonality.mode∈{additive,multiplicative}; logistic->cap; regressors->an explicit future with the columns; macro spacing>=28d auto-disables weekly/daily

### References

- Taylor & Letham 2018 Forecasting at scale (The American Statistician)
- prophet reference manual + Facebook Prophet docs

## #10 — smooth (ADAM / ES variants)

**Module:** `smooth.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_adam` | `data` | `series_handle`, `string`, `integer`, `boolean`, `enum`, `enum`, `integer` | — | `heavy` | — |
| `run_auto_adam` | `data` | `series_handle`, `string`, `integer`, `boolean`, `enum`, `integer` | — | `heavy` | — |
| `run_ces` | `y` | `series_handle`, `enum`, `enum`, `integer`, `boolean`, `integer` | — | `heavy` | — |
| `run_auto_ces` | `y` | `series_handle`, `enum`, `enum`, `integer`, `boolean`, `integer` | — | `heavy` | — |

### Use when

ADAM unifies ETS+ARIMA+regression in state space with a non-gaussian error (dlaplace/ds/dgamma/..) or intermittent demand (occurrence); CES when trend/season are hard to separate

### Do not use when

a plain gaussian monthly series (ets/auto.arima suffices); holidays (prophet); tidy <distribution> (fable)

### Alternatives

| instead use | when |
| --- | --- |
| #7 forecast ets/auto.arima | the classic gaussian path, lighter |
| #8 fable | tidy workflow |
| #9 prophet | calendar effects |

### Output fields

- mean: point forecasts (conditional mean, ts)
- lower/upper: bounds of interval=prediction at level=0.95 (side both)
- level/interval: the level + a binary flag for whether an interval was produced
- accuracy: accuracy.smooth — automatic holdout (MASE/RMSSE) if holdout=TRUE, otherwise in-sample
- model: adam/ces object (states,persistence,phi,complex params) compact stub
- fitted/residuals: in-sample

### Pitfalls

- fit-time level=0.99 is the outlier-detection level, NOT forecast confidence (that is interval.level 0.95)
- h/holdout are fit-time; the forecast horizon is the separate forecast.h (explicit->fit h if >0->10)
- accuracy is holdout (OOS) only if holdout=TRUE, otherwise in-sample
- auto.adam distribution & auto.ces seasonality are vectors to be tried (not match.arg)
- gate: holdout=TRUE requires h>0 (in all 4)

### References

- Svetunkov 2023 Forecasting and Analytics with the ADAM (openforecast.org monograph)
- Svetunkov & Kourentzes (CES / complex exponential smoothing)
- smooth reference manual + vignettes (adam, ces, forecast.adam, accuracy.smooth)

## #133 — nnfor (neural-network univariate forecasting: MLP ensemble + ELM)

**Module:** `nnfor.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nnf_mlp` | `y`, `seed` | `series_handle`, `integer`, `integer`, `integer`, `integer`, `enum`, `boolean`, `enum`, `exog_handle` | — | `light` | `model` |
| `nnf_elm` | `y`, `seed` | `series_handle`, `integer`, `integer`, `integer`, `enum`, `integer`, `enum`, `boolean`, `boolean`, `enum`, `exog_handle` | — | `light` | `model` |

### Use when

non-linear univariate forecasting; nnf_mlp=an MLP ensemble (backprop), nnf_elm=an Extreme Learning Machine (random hidden weights, output lasso/ridge/step/lm); automatic lag selection + differencing + seasonal dummies; an ensemble of reps networks

### Do not use when

a small sample/interpretability/a linear DGP -> #7 forecast or #10 smooth; multivariate -> 03-multivariate-nowcasting; without a seed it is uncacheable (forbidden)

### Alternatives

| instead use | when |
| --- | --- |
| 02-univariate-forecasting/forecast-run_auto_arima | the linear/interpretable path with analytic PI (lightweight) |
| 02-univariate-forecasting/smooth-run_adam | state-space ETS+ARIMA (non-gaussian/intermittent) |
| nnf_elm | speed (closed-form output weights, no backprop) rather than full MLP training |

### Output fields

- mean: point forecasts (the ensemble combination via comb, ts)
- all.mean: h x reps, ALL the ensemble members
- lower/upper: EMPIRICAL PI (per-horizon quantiles of the members; NOT analytic; it needs reps>1)
- accuracy: in-sample ME/RMSE/MAE/MAPE (computed here — forecast.net does not provide them)
- model: the mlp/elm object -> producer register field=model bucket=rds; a compact stub in to_mcp
- hd/lags/difforder/reps/seed/n: the selections + the pinned seed (cache key)

### Pitfalls

- the seed is MANDATORY & part of the cache key — the same seed gives identical output, a different one a different forecast (live-verified)
- the PI are empirical ensemble quantiles, NOT frequentist/Bayesian intervals
- exog_handle must cover in-sample + horizon (length >= n+h)
- the defaults reps=2/hd=3 are curated to be cheap (the docs use reps=20); raise them deliberately
- gate: y must be ts/msts (a plain vector is rejected); hd/reps positive integers; level in (0,100); exog_handle not a data_frame

### References

- Kourentzes nnfor reference (mlp, elm, forecast.mlp, forecast.elm)
- Ord, Fildes & Kourentzes 2017 Principles of Business Forecasting 2e Ch.10
- Kourentzes, Barrow & Crone 2014 neural network ensemble operators (Expert Systems with Applications 41(9))
- Huang, Zhou & Ding 2006 Extreme Learning Machine (Neurocomputing 70(1))

## #134 — caretForecast (recursive autoregressive ML forecasting via caret + conformal prediction intervals + variable importance)

**Module:** `caretforecast.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `caf_arml` | `y`, `seed` | `series_handle`, `integer`, `integer`, `enum`, `raw`, `boolean`, `integer`, `boolean`, `exog_handle`, `exog_handle`, `integer` | — | `light` | `model` |
| `caf_conformal` | `model` | `raw_handle`, `integer`, `number`, `exog_handle`, `number`, `number` | — | `light` | — |
| `caf_varimp` | `model` | `raw_handle` | — | `light` | — |

### Use when

univariate forecasting with an ML learner on lagged+fourier features (recursive AR); caf_arml=ARml+forecast (point+PI), caf_conformal=distribution-free conformal PI, caf_varimp=variable importance; a CLOSED whitelist of light learners (lm/glmnet/ridge/lasso)

### Do not use when

a full NN -> #133 nnfor; a linear/interpretable model with analytic PI -> #7 forecast; state-space ETS+ARIMA -> #10 smooth; multivariate -> 03; free choice of a caret learner is NOT allowed (security/cost); without a seed it is uncacheable

### Alternatives

| instead use | when |
| --- | --- |
| 02-univariate-forecasting/nnf_mlp | a full/ELM NN for non-linearities rather than regularized ML |
| 02-univariate-forecasting/forecast-run_auto_arima | the linear/interpretable path with analytic PI (lightweight) |
| caf_conformal | you need explicitly distribution-free (residual-based) PI rather than the parametric ones of caf_arml |

### Output fields

- mean: point forecasts (ts, recursive AR)
- lower/upper: the h x length(level) PI of forecast.ARml (conformal-calibrated)
- accuracy: in-sample ME/RMSE/MAE/MAPE (computed here from residuals/fitted)
- model: the ARml object -> producer register field=model bucket=rds; a compact stub in to_mcp
- caret_method/max_lag/seed/n: the public learner token + the pinned values (cache key)
- caf_conformal: the lower/upper conformal bounds + confidence + n_calibration; caf_varimp: an importance df (variable/overall)

### Pitfalls

- the seed is MANDATORY & part of the cache key — the same seed gives identical output (live-verified); caret resampling is stochastic
- the public caret_method token is mapped INTERNALLY (ridge/lasso -> glmnet with a fixed alpha); it is NOT a free caret string
- an exog_handle at fit time requires a future newxreg (nrow==h) for the forecast
- conformal PI are distribution-free (residual-based), NOT gaussian; caf_conformal is a separate tool
- gate: y a univariate ts & length>max_lag+1; cv=FALSE is rejected; caret_method is a closed whitelist; level in (0,100); confidence in (0,1)

### References

- Akay caretForecast reference (ARml, forecast.ARml, conformalRegressor, predict.conformalRegressor, get_var_imp)
- Kuhn 2008 Building Predictive Models in the reference Using the caret Package (JSS 28(5))
- Bostrom 2022 crepes: a Python Package for Generating Conformal Regressors (PMLR 179)
- Hyndman & Athanasopoulos Forecasting: Principles and Practice 3e (fourier/recursive forecasting)

## #135 — Intermittent / sparse-demand forecasting (Croston + SBA/SBJ variants, TSB, iMAPA auto-selection, Croston decomposition)

**Module:** `intermittent_sparse_demand.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tsi_croston` | `data` | `series_handle`, `integer`, `enum`, `enum`, `enum`, `integer`, `raw`, `boolean`, `boolean` | — | `light` | — |
| `tsi_tsb` | `data` | `series_handle`, `integer`, `enum`, `enum`, `raw`, `boolean`, `boolean` | — | `light` | — |
| `tsi_imapa` | `data` | `series_handle`, `integer`, `enum`, `integer`, `integer`, `raw`, `boolean`, `boolean` | — | `light` | — |
| `tsi_decomp` | `data` | `series_handle`, `enum` | — | `light` | — |

### Use when

demand series with many zeros (spare parts / rare events); a constant out-of-sample demand rate; automatic model selection (imapa) or a demand/interval decomposition

### Do not use when

dense series with no zeros -> forecast #7; charts (frontend; outplot=FALSE); continuous macro series

### Alternatives

| instead use | when |
| --- | --- |
| tsi_croston (type=sba) | bias-corrected Croston (SBA/SBJ) — less positive bias |
| tsi_tsb | declining demand / obsolescence (it models the demand probability, not the interval) |
| tsi_imapa | automatic robust model selection (a combination across aggregation levels) |
| 02-univariate-forecasting/forecast-run_ets | the series is NOT intermittent (it is dense) |

### Output fields

- forecast: the out-of-sample demand RATE (frc.out, of length h; a constant per-period rate, NOT discrete events)
- fitted: the in-sample demand rate (frc.in, leading NA); weights/initial: smoothing & init parameters; model: the selected model
- imapa.summary: a matrix per AL (AL/n/p/cv2/model 1=Cro; 2=SBA; 3=SES/use); model_fit: parameters per AL
- croston.components: c.in/c.out (demand & interval) + coeff (sba/sbj scaling); decomp: demand + interval (equal length)

### Pitfalls

- forecast = a demand RATE per period (e.g. 0.19 units/period), NOT a forecast of an individual order — sum it for total demand
- crost does NOT validate type -> silently wrong; negative values are silently accepted -> a non-negativity gate; h<=0 -> a silently empty frc.out
- intermittency gate: >=1 zero (otherwise it is dense -> #7) AND >=2 non-zero values; imapa ALs with use=0 (<4 obs) are ignored; deterministic (no seed)

### References

- tsintermittent 1.10 reference (crost/tsb/imapa/crost.decomp — formals & outputs live-probed)
- Kourentzes 2014, On intermittent demand model optimisation and selection, IJPE 156:180-190 (doi:10.1016/j.ijpe.2014.06.007)
- Petropoulos & Kourentzes 2015, Forecast Combinations for Intermittent Demand, JORS (doi:10.1057/jors.2014.62)

## #136 — Long memory / fractional integration ARFIMA(p,d,q) (ML fit + GPH/Sperio semiparametric d + fractional differencing)

**Module:** `long_memory_fractional.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `fdf_fit` | `x` | `series_handle`, `integer`, `integer`, `integer` | — | `light` | `model` |
| `fdf_gph` | `x` | `series_handle`, `number` | — | `light` | — |
| `fdf_sperio` | `x` | `series_handle`, `number`, `number` | — | `light` | — |
| `fdf_diffseries` | `x`, `d` | `series_handle`, `number` | — | `light` | — |

### Use when

a slowly decaying ACF, between I(0) and I(1); estimating the memory parameter d (semiparametric GPH/Sperio or parametric ARFIMA ML) + fractional differencing to I(0)

### Do not use when

integer differencing -> ADF/KPSS+diff, cat.01; a forecast object -> forecast/fable/smooth #7-10; long-memory volatility -> GARCH, cat.06

### Prerequisites

- .fdf_check_series (univariate numeric/ts without NA/NaN/Inf)
- c00_data_utilities/descriptive_statistics.desc_acf (a slowly/linearly decaying ACF => evidence of long memory)
- c01_preparation_prechecks/unit_root_suite.wrap_ur_df (ADF non-rejection + ambiguous stationarity => possible fractional integration)
- c01_preparation_prechecks/unit_root_suite.wrap_ur_kpss (KPSS alongside ADF for an ambiguous I(0)/I(1))
- c00_data_utilities/replacement_missing_values.imputets_kalman (fill NA before the fit if needed)

### Alternatives

| instead use | when |
| --- | --- |
| fdf_gph | a fast semiparametric estimate of d (GPH log-periodogram) — the exploration default |
| fdf_sperio | a more robust semiparametric d (smoothed periodogram, Parzen window) under short-run dynamics/noise |
| fdf_fit | a full parametric ARFIMA(p,d,q) ML (d+AR/MA+SE together) when you need a model, not just d |

### Output fields

- d + d_reading: d≈0 short memory (I0), d<0 anti-persistent, 0<d<0.5 stationary long memory, d>=0.5 non-stationary
- fdf_gph/fdf_sperio: sd_asymptotic/sd_regression (two SE estimators for d -> a CI/significance of d!=0)
- fdf_fit: d/ar/ma/sigma/log_likelihood/std_errors(order d,ar,ma)/covariance/correlation + model (a producer, rds)
- fdf_diffseries: series (fractionally differenced; it preserves the ts attributes) + d + n

### Pitfalls

- the fdf_fit drange default c(0,0.5) CONSTRAINS d to [0,0.5] — for d>=0.5 (non-stationary) widen drange explicitly
- MA sign: fracdiff uses the S-plus convention with REVERSED MA signs relative to arima/Wikipedia — do not compare directly
- BANDWIDTH GATE: fdGPH/fdSperio with bandw.exp=0 return d=NA/sd=Inf SILENTLY (silently wrong) -> a hard gate 0<bandw<1
- the cov/SE of the fracdiff ML can be inaccurate (a documented Warning) — prefer the semiparametric SE for inference on d

### References

- Haslett & Raftery 1989 (Applied Statistics 38:1-50, ML approximation)
- Geweke & Porter-Hudak 1983 (J. Time Series Analysis 4(4):221-238, GPH)
- Reisen 1994 (J. Time Series Analysis 15(1):335-350, smoothed periodogram)
- Jensen & Nielsen 2014 (J. Time Series Analysis 35(5):428-436, fast fractional difference, doi:10.1111/jtsa.12074)

## #137 — Distributed-lag & ARDL regression (finite DL / Koyck geometric / autoregressive DL / Almon polynomial DL)

**Module:** `distributed_lag_ardl.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dlm_finite` | `q` | `series_handle`, `series_handle`, `df_handle`, `string`, `series_codes`, `integer`, `raw` | — | `light` | `model` |
| `dlm_koyck` | `x`, `y` | `series_handle`, `series_handle`, `boolean` | — | `light` | `model` |
| `dlm_ardl` | — | `series_handle`, `series_handle`, `df_handle`, `string`, `series_codes`, `integer`, `integer`, `raw` | `p=1`, `q=1` | `light` | `model` |
| `dlm_poly` | `x`, `y`, `q`, `k` | `series_handle`, `series_handle`, `integer`, `integer`, `boolean` | — | `light` | `model` |

### Use when

a lag-distributed effect of a predictor X on Y (short/long-run multipliers): a finite q, an infinite geometric decay (Koyck), an autoregressive DL(p,q), Almon polynomial smoothing of the lag weights

### Do not use when

pure univariate forecasting without X -> #7/#8; non-linear relations; I(1) long-run cointegration/ECM -> ARDL bounds (05); structural shocks/IRF -> 04

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (stationarity of x & y first — a level DL regression on non-cointegrated I(1) series is spurious)
- c01_preparation_prechecks/unit_root_normality.run_kpss_test (confirmatory stationarity, the opposite H0)

### Alternatives

| instead use | when |
| --- | --- |
| 05-cointegration/ardl_bounds_f | x,y are I(1): a bounds test for long-run cointegration + an ECM instead of a level DL regression |
| dlm_koyck | an infinite geometric decay of the lag weights (a single rate phi, parsimony) rather than an explicit finite q |
| dlm_poly | many lags with multicollinearity -> Almon polynomial smoothing of the lag weights |
| dlm_ardl | you need AR dynamics in Y (autoregressive) alongside the distributed lags of X |

### Output fields

- coefficients: named numeric (intercept + lag terms); fitted/residuals: numeric
- diagnostics: r_squared/adj_r_squared/sigma/df_residual/nobs/aic/bic (aic/bic=NA for the koyck ivreg)
- method-specific: q/k (finite/poly); order=c(p,q) (ardl); geometric_coefficients alpha/beta/phi (koyck); beta+beta_tvalue/beta_pvalue (poly); formula/removed (multi-formula mode)

### Pitfalls

- koyck: interpret the geometric_coefficients (alpha/beta/phi; phi=the decay rate), NOT the raw ivreg delta coefficients; aic/bic=NA (ivreg has no log_lik) — no comparison with lm-based models
- poly: beta (the original per-lag weights) is the interpretable quantity; the coefficients are the gamma of the z-transformed polynomial, NOT per-lag effects
- q loses q initial observations (nobs = n - q); a length mismatch between x and y was accepted SILENTLY by dLagM -> hard gate
- closed formula: it is built from y_col ~ x_cols (reformulate), NEVER a free formula string; k>q -> singular (hard gate)

### References

- Hill, Griffiths & Judge, Undergraduate Econometrics (Wiley); Baltagi, Econometrics 5th ed. (Springer)

## #138 — Maximum Entropy Bootstrap for time series (dependence/non-stationarity preserved)

**Module:** `maximum_entropy_bootstrap.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `meb_ensemble` | `x`, `seed` | `series_handle`, `integer`, `integer`, `number`, `boolean`, `boolean`, `boolean`, `boolean`, `boolean` | — | `light` | `ensemble` |

### Use when

bootstrap ensemble replicates of a series for downstream inference/confidence bands WITHOUT assuming stationarity or tuning a block length (it preserves dependence/non-stationarity)

### Do not use when

parametric prediction intervals from a correctly specified model -> forecast #7; charts (frontend); panel pdata_frame ensembles (out of scope)

### Alternatives

| instead use | when |
| --- | --- |
| 02-univariate-forecasting/forecast-run_auto_arima | a well-specified parametric model exists -> model-based prediction intervals instead of resampling |
| force.clt=TRUE (default) | preserve the CLT for the ensemble mean; FALSE for non-gaussian tails or a trim xmin=0 non-negativity constraint |

### Output fields

- ensemble: an n x reps matrix of replicates (mts/matrix -> nested rows) — the DATA/producer field
- x: the original series (as input); xx: the ordered order statistics; z: the class-interval limits
- xmin/xmax: the left/right tail limits; dvtrim: the trimmed mean deviations; kappa: the scale adjustment
- n/reps/trim/seed: metadata + the applied arguments (the seed for reproducibility)

### Pitfalls

- STOCHASTIC: the seed is MANDATORY (set.seed before the draw); without a pinned seed the node is uncacheable
- reps<10 or a trim outside [0,0.5) are accepted SILENTLY by meboot -> hard gates here (silently wrong)
- force.clt=TRUE alters the ensemble so that the mean satisfies the CLT — it is NOT a raw resample
- elaps (elapsed time) is forced FALSE & omitted — it is non-deterministic and breaks caching

### References

- Vinod, H.D. (2006) Maximum Entropy Ensembles for Time Series Inference in Economics, J. Asian Economics 17(6):955-978
- Vinod, H.D. (2013) Maximum Entropy Bootstrap Algorithm Enhancements, SSRN 2285041
- Vinod & López-de-Lacalle (2009) JSS, 'Maximum Entropy Bootstrap for Time Series: The meboot the reference Package'
- meboot reference manual (meboot)
