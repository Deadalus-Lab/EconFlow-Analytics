# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 02-univariate-forecasting: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'rml_fit': {
        'fn': 'rml_fit',
        'description': 'rml_fit -- category 02-univariate-forecasting, method card #134.',
        'args': {'y': 'Handle to a univariate ts (the series to forecast).', 'seed': 'REQUIRED seed (seeded before resampling; cache key; uncacheable without it).', 'max_lag': 'Maximum lag of the autoregressive features (positive integer; default 5; length(y)>max_lag+1).', 'learner_method': 'CLOSED whitelist of lightweight learners (default lm); maps internally to the learner method and tuning grid; NEVER a free string.', 'pre_process': 'Optional preprocessing steps (center/scale/range/BoxCox etc.; gated to an allowed set; None=none).', 'cv': 'Model selection with time-slice CV (default True; cv=False is rejected — requires a forbidden tuning grid).', 'cv_horizon': 'Number of consecutive values in the test set of each resample (positive integer; default 4).', 'seasonal': 'Fourier terms for seasonality (default True).', 'exog': 'In-sample exogenous regressors (matrix, nrow==length(y); NOT a data frame).', 'new_exog': 'Future exogenous regressors for the forecast (nrow==h, same columns as exog_handle; required if exog_handle is given).', 'h': 'Forecast horizon (positive integer; None -> frequency(y)).'},
        'input_example': {'y': '<series_handle>', 'seed': 1},
    },
    'rml_conformal': {
        'fn': 'rml_conformal',
        'description': 'rml_conformal -- category 02-univariate-forecasting, method card #134.',
        'args': {'model': 'Handle to an ARml model (rml_fit.model) — conformal PI from its in-sample residuals.', 'h': 'Forecast horizon (positive integer; None -> frequency(model.y)).', 'confidence': 'Confidence level of the conformal interval ∈ (0,1) (default 0.95).', 'new_exog': 'Future regressors if the model was trained with exog_handle (NOT a data frame).', 'y_min': 'Lower clip of the intervals (default -Inf).', 'y_max': 'Upper clip of the intervals (> y_min; default Inf).'},
        'input_example': {'model': '<raw_handle>'},
    },
    'rml_variable_importance': {
        'fn': 'rml_variable_importance',
        'description': 'rml_variable_importance -- category 02-univariate-forecasting, method card #134.',
        'args': {'model': 'Handle to an ARml or forecast object (rml_fit) — variable importance of the lags/regressors.'},
        'input_example': {'model': '<raw_handle>'},
    },
    'dlag_ardl': {
        'fn': 'dlag_ardl',
        'description': 'dlag_ardl -- category 02-univariate-forecasting, method card #137.',
        'args': {'x': 'Handle to predictor series X (vector mode).', 'y': 'Handle to dependent series Y (vector mode).', 'data': 'Handle to a DataFrame (closed formula mode; requires y_col+x_cols).', 'y_col': 'Response column name (formula mode).', 'x_cols': 'Predictor column names >=1 (formula mode).', 'p': 'Lag length of predictor X (positive integer >=1, < nobs).', 'q': 'AR order of dependent Y (positive integer >=1, < nobs).', 'remove': 'list(p=, q=) of lags to remove (optional).'},
        'input_example': {'p': 1, 'q': 1},
    },
    'dlag_finite': {
        'fn': 'dlag_finite',
        'description': 'dlag_finite -- category 02-univariate-forecasting, method card #137.',
        'args': {'x': 'Handle to predictor series X (vector mode; numeric >=3, without NA/Inf).', 'y': 'Handle to dependent series Y (vector mode; same length as x).', 'data': 'Handle to a DataFrame (closed formula mode; requires y_col+x_cols).', 'y_col': 'Response column name (formula mode).', 'x_cols': 'Predictor column names >=1 (formula mode; closed, without a free formula string).', 'q': 'Finite lag length (positive integer >=1, < nobs).', 'remove': 'list of lags to remove per predictor (optional).'},
        'input_example': {'q': 1},
    },
    'dlag_koyck': {
        'fn': 'dlag_koyck',
        'description': 'dlag_koyck -- category 02-univariate-forecasting, method card #137.',
        'args': {'x': 'Handle to predictor series X (numeric >=3).', 'y': 'Handle to dependent series Y (same length as x).', 'intercept': 'Inclusion of intercept in the Koyck-transformed model (default True).'},
        'input_example': {'x': '<series_handle>', 'y': '<series_handle>'},
    },
    'dlag_almon': {
        'fn': 'dlag_almon',
        'description': 'dlag_almon -- category 02-univariate-forecasting, method card #137.',
        'args': {'x': 'Handle to predictor series X (numeric >=3).', 'y': 'Handle to dependent series Y (same length as x).', 'q': 'Finite lag length (positive integer >=1, < nobs).', 'k': 'Almon polynomial order (positive integer >=1, k <= q).', 'show_beta': 'Return of original beta lag weights + t-tests (default True).'},
        'input_example': {'x': '<series_handle>', 'y': '<series_handle>', 'q': 1, 'k': 1},
    },
    'arfima_difference': {
        'fn': 'arfima_difference',
        'description': 'arfima_difference -- category 02-univariate-forecasting, method card #136.',
        'args': {'x': 'Handle to a univariate ts/numeric.', 'd': 'Fractional differencing order (a single finite number).'},
        'input_example': {'x': '<series_handle>', 'd': 0.5},
    },
    'arfima_fit': {
        'fn': 'arfima_fit',
        'description': 'arfima_fit -- category 02-univariate-forecasting, method card #136.',
        'args': {'x': 'Handle to a univariate ts/numeric (the series for the ARFIMA fit).', 'nar': 'Number of AR parameters p (non-negative integer; default 0).', 'nma': 'Number of MA parameters q (non-negative integer; default 0).', 'M': 'Terms in the likelihood approximation (Haslett-Raftery; default 100).'},
        'input_example': {'x': '<series_handle>'},
    },
    'arfima_gph': {
        'fn': 'arfima_gph',
        'description': 'arfima_gph -- category 02-univariate-forecasting, method card #136.',
        'args': {'x': 'Handle to a univariate ts/numeric.', 'bandw_exp': 'Bandwidth exponent bw=trunc(n^bandw.exp); strictly in (0,1); default 0.5.'},
        'input_example': {'x': '<series_handle>'},
    },
    'arfima_sperio': {
        'fn': 'arfima_sperio',
        'description': 'arfima_sperio -- category 02-univariate-forecasting, method card #136.',
        'args': {'x': 'Handle to a univariate ts/numeric.', 'bandw_exp': 'Bandwidth exponent; strictly in (0,1); default 0.5.', 'beta': 'Bandwidth exponent of the Parzen lag window; strictly in (0,1); default 0.9.'},
        'input_example': {'x': '<series_handle>'},
    },
    'meb_ensemble': {
        'fn': 'meb_ensemble',
        'description': 'meb_ensemble -- category 02-univariate-forecasting, method card #138.',
        'args': {'x': 'Handle to a univariate series (numeric/ts; fully finite, length>=2).', 'seed': 'Seed (REQUIRED; stochastic — seeded before the draw; reproducibility/caching).', 'reps': 'Number of bootstrap replicates (default 999; gate reps>=10).', 'trim': 'Trimming proportion of the tails (default 0.10; gate 0<=trim<0.5).', 'reachbnd': 'Reached-bounds draws at the 0/1 edges (default True).', 'expand_sd': "Widening of the ensemble's SD (default True).", 'force_clt': 'Forcing of CLT on the ensemble mean (default True).', 'scl_adjustment': 'Scale adjustment so that var(ensemble)=var(x) (default False).', 'sym': 'Symmetric ME density adjustment (default False).'},
        'input_example': {'x': '<series_handle>', 'seed': 1},
    },
    'nn_elm': {
        'fn': 'nn_elm',
        'description': 'nn_elm -- category 02-univariate-forecasting, method card #133.',
        'args': {'y': 'Handle to a univariate ts/msts.', 'seed': 'REQUIRED seed (seeded before the random hidden weights; cache key).', 'h': 'Forecast horizon (positive integer; None -> frequency(y)).', 'hd': 'Number of hidden nodes (small default 3).', 'type': 'Estimation of output-layer weights (default lasso).', 'reps': 'Ensemble size (default 2).', 'comb': 'Ensemble combination operator (default median).', 'sel_lag': 'Automatic lag selection (default True).', 'direct': 'Direct input-output connections for linear effects (default False).', 'det_type': 'Type of deterministic seasonal dummies (default auto).', 'exog': 'Exogenous regressors (matrix, length >= n+h; NOT a data frame).'},
        'input_example': {'y': '<series_handle>', 'seed': 1},
    },
    'nn_mlp': {
        'fn': 'nn_mlp',
        'description': 'nn_mlp -- category 02-univariate-forecasting, method card #133.',
        'args': {'y': 'Handle to a univariate ts/msts (the series to forecast).', 'seed': 'REQUIRED seed (seeded before the random weights; cache key; uncacheable without it).', 'h': 'Forecast horizon (positive integer; None -> frequency(y)).', 'hd': 'Number of hidden nodes (small default 3; keeps the node cheap).', 'reps': 'Ensemble size (number of networks; default 2; docs 20).', 'comb': 'Ensemble combination operator (default median).', 'sel_lag': 'Automatic lag selection (default True).', 'det_type': 'Type of deterministic seasonal dummies (default auto).', 'exog': 'Exogenous regressors (matrix, length >= n+h; NOT a data frame).'},
        'input_example': {'y': '<series_handle>', 'seed': 1},
    },
    'run_adam': {
        'fn': 'run_adam',
        'description': 'run_adam -- category 02-univariate-forecasting, method card #10.',
        'args': {'data': 'Handle to a series (1st column = response; data-agnostic passthrough).', 'model': "ETS spec E/T/S (default 'ZXZ'; Z=auto, X=pure additive selection).", 'h': 'Fit-time horizon (for holdout; default 0).', 'holdout': 'Keep the last h points as holdout (requires h>0; default False).', 'loss': 'Loss function (default likelihood).', 'ic': 'Information criterion (default AICc).', 'forecast_h': 'Horizon of the forecast step (None -> fit h if >0, otherwise 10).'},
        'input_example': {'data': '<series_handle>'},
    },
    'run_auto_adam': {
        'fn': 'run_auto_adam',
        'description': 'run_auto_adam -- category 02-univariate-forecasting, method card #10.',
        'args': {'data': 'Handle to a series (auto.adam tries multiple distributions).', 'model': "ETS spec E/T/S (default 'ZXZ').", 'h': 'Fit-time horizon (default 0).', 'holdout': 'Holdout of the last h (requires h>0; default False).', 'ic': 'Information criterion (default AICc).', 'forecast_h': 'Horizon of the forecast step.'},
        'input_example': {'data': '<series_handle>'},
    },
    'run_auto_arima': {
        'fn': 'run_auto_arima',
        'description': 'run_auto_arima -- category 02-univariate-forecasting, method card #7.',
        'args': {'y': 'Handle to a univariate ts (the series to forecast).', 'h': 'Forecast horizon (number of steps; None -> documented default).', 'ic': 'Information criterion for the selection (default aicc).', 'stepwise': 'Stepwise search (default True; False = exhaustive, slow).', 'seasonal': 'Allow seasonal ARIMA terms (default True).', 'exog': 'Handle to exogenous regressors (matrix, same rows as y; NOT a data frame).'},
        'input_example': {'y': '<series_handle>'},
    },
    'run_auto_ces': {
        'fn': 'run_auto_ces',
        'description': 'run_auto_ces -- category 02-univariate-forecasting, method card #10.',
        'args': {'y': 'Handle to a series (auto.ces tries the seasonality types).', 'ic': 'Information criterion (default AICc).', 'loss': 'Loss function (default likelihood).', 'h': 'Fit-time horizon (default 0).', 'holdout': 'Holdout of the last h (requires h>0; default False).', 'forecast_h': 'Horizon of the forecast step.'},
        'input_example': {'y': '<series_handle>'},
    },
    'run_ces': {
        'fn': 'run_ces',
        'description': 'run_ces -- category 02-univariate-forecasting, method card #10.',
        'args': {'y': 'Handle to a series (univariate response).', 'seasonality': 'Type of complex seasonality (default none).', 'loss': 'Loss function (default likelihood).', 'h': 'Fit-time horizon (default 0).', 'holdout': 'Holdout of the last h (requires h>0; default False).', 'forecast_h': 'Horizon of the forecast step.'},
        'input_example': {'y': '<series_handle>'},
    },
    'run_ets': {
        'fn': 'run_ets',
        'description': 'run_ets -- category 02-univariate-forecasting, method card #7.',
        'args': {'y': 'Handle to a univariate ts.', 'model': "ETS spec, 3 letters E/T/S (default 'ZZZ' = automatic selection).", 'damped': 'Damped trend (None -> auto; True/False forces it).', 'h': 'Forecast horizon.', 'ic': 'Information criterion (default aicc).'},
        'input_example': {'y': '<series_handle>'},
    },
    'run_grouped_arima': {
        'fn': 'run_grouped_arima',
        'description': 'run_grouped_arima -- category 02-univariate-forecasting, method card #8.',
        'args': {'data': 'Handle to a series (index + value variable).', 'formula': "Model spec, e.g. 'value ~ 1' (automatic order selection). NOTE: the special order functions pdq/PDQ are NOT allowed by the security allowlist.", 'ic': 'Information criterion (default aicc).', 'stepwise': 'Stepwise search (default True).', 'h': 'Forecast horizon.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x'},
    },
    'run_grouped_ets': {
        'fn': 'run_grouped_ets',
        'description': 'run_grouped_ets -- category 02-univariate-forecasting, method card #8.',
        'args': {'data': 'Handle to a series (WITHOUT missing values — ETS does not support them).', 'formula': 'ETS model spec; NOTE: the order functions error/trend/season are NOT allowed by the security allowlist.', 'opt_crit': 'Optimization criterion (default lik).', 'ic': 'Information criterion (default aicc).', 'h': 'Forecast horizon.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x'},
    },
    'run_prophet': {
        'fn': 'run_prophet',
        'description': 'run_prophet -- category 02-univariate-forecasting, method card #9.',
        'args': {'df': 'Handle to a DataFrame; either ds/y or long-format (date_col/value_col).', 'growth': "Trend growth (default linear; 'logistic' requires a cap column).", 'seasonality_mode': 'Seasonality mode (default additive).', 'date_col': "Date column name for mapping to ds (default 'period').", 'value_col': "Value column name for mapping to y (default 'value').", 'periods': 'Forecast horizon (future steps; default 0).', 'freq': "Frequency of future dates (e.g. 'month'; None -> auto-infer)."},
        'input_example': {'df': '<df_handle>'},
    },
    'run_prophet_cv': {
        'fn': 'run_prophet_cv',
        'description': 'run_prophet_cv -- category 02-univariate-forecasting, method card #9.',
        'args': {'model': 'Handle to a fitted prophet model (from run_prophet).', 'horizon': "Horizon of each fold (in 'units').", 'units': "Time unit (e.g. 'days', 'weeks').", 'period': 'Cutoff spacing (units; None -> 0.5*horizon).', 'initial': 'Initial training window (units; None -> 3*horizon).', 'rolling_window': 'Aggregation window of the performance metrics (default 0.1).'},
        'input_example': {'model': '<raw_handle>', 'horizon': 1, 'units': '...'},
    },
    'run_tbats': {
        'fn': 'run_tbats',
        'description': 'run_tbats -- category 02-univariate-forecasting, method card #7.',
        'args': {'y': 'Handle to a univariate ts (univariate only; multiple seasonal periods possible).', 'use_box_cox': 'Box-Cox transformation (None -> auto).', 'use_trend': 'Inclusion of trend (None -> auto).', 'use_damped_trend': 'Damped trend (None -> auto).', 'use_arma_errors': 'ARMA errors on the residuals (default True).', 'h': 'Forecast horizon.'},
        'input_example': {'y': '<series_handle>'},
    },
    'run_theta': {
        'fn': 'run_theta',
        'description': 'run_theta -- category 02-univariate-forecasting, method card #7.',
        'args': {'y': 'Handle to a univariate ts.', 'h': 'Forecast horizon.'},
        'input_example': {'y': '<series_handle>'},
    },
    'tsi_croston': {
        'fn': 'tsi_croston',
        'description': 'tsi_croston -- category 02-univariate-forecasting, method card #135.',
        'args': {'data': 'Handle to a univariate intermittent-demand series (non-negative, with zeros).', 'h': 'Forecast horizon (positive integer; default 10).', 'type': 'Croston variant (default croston; sba/sbj = bias-corrected).', 'init': 'Initial demand/interval values (default mean).', 'cost': 'Optimization cost function (default mar).', 'nop': 'Number of parameters: 1 (shared) or 2 (default, separate demand/interval).', 'w': 'Smoothing parameters (None -> optimise; 1 or 2 values).', 'init_opt': 'Optimization of initial values (default True).', 'na_rm': 'Removal of NA before the fit (default False).'},
        'input_example': {'data': '<series_handle>'},
    },
    'tsi_decomp': {
        'fn': 'tsi_decomp',
        'description': 'tsi_decomp -- category 02-univariate-forecasting, method card #135.',
        'args': {'data': 'Handle to a univariate intermittent-demand series.', 'init': 'Initial interval value (default naive — CAUTION: reverse order from crost/tsb).'},
        'input_example': {'data': '<series_handle>'},
    },
    'tsi_imapa': {
        'fn': 'tsi_imapa',
        'description': 'tsi_imapa -- category 02-univariate-forecasting, method card #135.',
        'args': {'data': 'Handle to a univariate intermittent-demand series.', 'h': 'Forecast horizon (positive integer; default 10).', 'comb': 'Combination operator over the aggregation levels (default mean).', 'minimumAL': 'Lowest aggregation level (default 1).', 'maximumAL': 'Highest aggregation level (None -> maximum interval).', 'w': 'Smoothing parameters (None -> optimise).', 'init_opt': 'Optimization of Croston/SBA initial values (default True).', 'na_rm': 'Removal of NA (default False).'},
        'input_example': {'data': '<series_handle>'},
    },
    'tsi_tsb': {
        'fn': 'tsi_tsb',
        'description': 'tsi_tsb -- category 02-univariate-forecasting, method card #135.',
        'args': {'data': 'Handle to a univariate intermittent-demand series.', 'h': 'Forecast horizon (positive integer; default 10).', 'init': 'Initial values (default mean).', 'cost': 'Cost function (default mar).', 'w': 'Smoothing (demand, demand-probability)· None -> optimise.', 'init_opt': 'Optimization of initial values (default True).', 'na_rm': 'Removal of NA (default False).'},
        'input_example': {'data': '<series_handle>'},
    },
    'uf_benchmark_forecast': {
        'fn': 'uf_benchmark_forecast',
        'description': 'uf_benchmark_forecast -- category 02-univariate-forecasting, method card #407.',
        'args': {'y': 'Series to forecast.', 'h': 'Forecast horizon.', 'method': 'Benchmark method.', 'season_length': 'Seasonal period.', 'window': 'Window for the window average.', 'levels': 'Prediction interval levels.'},
        'input_example': {'y': '<series_handle>', 'h': 1, 'method': 'seasonal_naive', 'season_length': 1, 'window': 12, 'levels': [0.8, 0.95]},
    },
    'uf_dynamic_regression': {
        'fn': 'uf_dynamic_regression',
        'description': 'uf_dynamic_regression -- category 02-univariate-forecasting, method card #408.',
        'args': {'y': 'Dependent series.', 'exog': 'Exogenous regressors.', 'order': 'ARIMA order.', 'seasonal_order': 'Seasonal ARIMA order.', 'season_length': 'Seasonal period.'},
        'input_example': {'y': '<series_handle>', 'exog': '<exog_handle>', 'order': [1, 0, 0], 'season_length': 1},
    },
    'uf_dynamic_regression_forecast': {
        'fn': 'uf_dynamic_regression_forecast',
        'description': 'uf_dynamic_regression_forecast -- category 02-univariate-forecasting, method card #408.',
        'args': {'fit': 'Handle to a fitted model.', 'exog_future': 'Future regressor values.', 'h': 'Forecast horizon.', 'levels': 'Prediction interval levels.'},
        'input_example': {'fit': '<raw_handle>', 'exog_future': '<exog_handle>', 'h': 1, 'levels': [0.8, 0.95]},
    },
    'uf_intervention': {
        'fn': 'uf_intervention',
        'description': 'uf_intervention -- category 02-univariate-forecasting, method card #409.',
        'args': {'y': 'Series.', 'intervention_date': 'Date the intervention begins.', 'shape': 'Intervention shape.', 'decay': 'Decay parameter for a gradual response.', 'order': 'ARIMA order.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'intervention_date': '...', 'shape': 'step', 'decay': 0.5, 'order': [1, 0, 0], 'conf_level': 0.95},
    },
    'uf_fan_chart': {
        'fn': 'uf_fan_chart',
        'description': 'uf_fan_chart -- category 02-univariate-forecasting, method card #410.',
        'args': {'fit': 'Handle to a fitted forecasting model.', 'h': 'Forecast horizon.', 'n_simulations': 'Simulated paths.', 'innovations': 'Innovation source.', 'quantiles': 'Fan quantiles.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'fit': '<raw_handle>', 'h': 1, 'n_simulations': 1000, 'innovations': 'bootstrap', 'quantiles': [0.05, 0.25, 0.5, 0.75, 0.95], 'seed': 1},
    },
    'uf_global_forecast': {
        'fn': 'uf_global_forecast',
        'description': 'uf_global_forecast -- category 02-univariate-forecasting, method card #411.',
        'args': {'data': 'Long-format panel: series id, time and value.', 'id': 'Column identifying the series.', 'time': 'Column holding the time index.', 'value': 'Column holding the value.', 'h': 'Forecast horizon.', 'lags': 'Lag features to construct.', 'model': 'Learner.', 'difference': 'Differencing applied before fitting.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'data': '<df_handle>', 'id': '...', 'time': '...', 'value': '...', 'h': 1, 'lags': [1, 2, 3, 12], 'model': 'lightgbm', 'difference': 0},
    },
    'uf_bagged_forecast': {
        'fn': 'uf_bagged_forecast',
        'description': 'uf_bagged_forecast -- category 02-univariate-forecasting, method card #412.',
        'args': {'y': 'Series to forecast.', 'h': 'Forecast horizon.', 'n_replicates': 'Bootstrap replicates.', 'bootstrap': 'Bootstrap scheme.', 'base_model': 'Model fitted to each replicate.', 'aggregate': 'Aggregation across replicates.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'y': '<series_handle>', 'h': 1, 'n_replicates': 100, 'bootstrap': 'stl_block', 'base_model': 'auto_ets', 'aggregate': 'mean', 'seed': 1},
    },
    'uf_direct_multistep': {
        'fn': 'uf_direct_multistep',
        'description': 'uf_direct_multistep -- category 02-univariate-forecasting, method card #413.',
        'args': {'y': 'Series to forecast.', 'h': 'Forecast horizon.', 'strategy': 'Reduction strategy.', 'window_length': 'Lag window used as features.', 'model': 'Base regressor.', 'seed': 'Seed for the random number generator.'},
        'input_example': {'y': '<series_handle>', 'h': 1, 'strategy': 'direct', 'window_length': 12, 'model': 'gradient_boosting'},
    },
    'uf_conformal_intervals': {
        'fn': 'uf_conformal_intervals',
        'description': 'uf_conformal_intervals -- category 02-univariate-forecasting, method card #414.',
        'args': {'fit': 'Handle to a fitted forecasting model.', 'y_calibration': 'Held-out calibration series.', 'h': 'Forecast horizon.', 'method': 'Conformal variant.', 'levels': 'Coverage levels.'},
        'input_example': {'fit': '<raw_handle>', 'y_calibration': '<series_handle>', 'h': 1, 'method': 'enbpi', 'levels': [0.8, 0.95]},
    },
    'uf_auto_select': {
        'fn': 'uf_auto_select',
        'description': 'uf_auto_select -- category 02-univariate-forecasting, method card #415.',
        'args': {'y': 'Series to forecast.', 'h': 'Forecast horizon.', 'candidates': 'Candidate families; omitted = the standard set.', 'n_folds': 'Cross-validation folds.', 'metric': 'Selection metric.', 'season_length': 'Seasonal period.'},
        'input_example': {'y': '<series_handle>', 'h': 1, 'n_folds': 5, 'metric': 'mase', 'season_length': 1},
    },
}
