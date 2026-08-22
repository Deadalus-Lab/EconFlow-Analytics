# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 15-model-evaluation: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'compute_loss_level': {
        'fn': 'compute_loss_level',
        'description': 'compute_loss_level -- category 15-model-evaluation, method card #75.',
        'args': {'realized': 'Handle to the series of realized values (realized).', 'evaluated': 'Handle to a matrix of point-forecasts (one column per model, same rows).', 'which': 'Loss function: SE=squared, AE=absolute error (default SE).'},
        'input_example': {'realized': '<series_handle>', 'evaluated': '<matrix_handle>'},
    },
    'compute_loss_vol': {
        'fn': 'compute_loss_vol',
        'description': 'compute_loss_vol -- category 15-model-evaluation, method card #75.',
        'args': {'realized': 'Handle to the realized volatility/variance series (proxy).', 'evaluated': 'Handle to a matrix of volatility-forecasts (one column per model).', 'which': 'Robust volatility loss family (default SE1· QLIKE is robust to the proxy).'},
        'input_example': {'realized': '<series_handle>', 'evaluated': '<matrix_handle>'},
    },
    'eval_dm_test': {
        'fn': 'eval_dm_test',
        'description': 'eval_dm_test -- category 15-model-evaluation, method card #74.',
        'args': {'e1': 'Handle to the forecast error series of method 1 (e1).', 'e2': 'Handle to the forecast error series of method 2 (e2, same length).', 'alternative': 'Alternative hypothesis (default two.sided· less => e1 is more accurate).', 'h': 'Forecast horizon of the errors (positive integer < length, default 1).', 'power': 'Loss power (2 = squared error, 1 = absolute error· default 2).', 'varestimator': 'Long-run variance estimator (default acf).'},
        'input_example': {'e1': '<series_handle>', 'e2': '<series_handle>', 'h': 1, 'power': 2},
    },
    'eval_rolling_origin': {
        'fn': 'eval_rolling_origin',
        'description': 'eval_rolling_origin -- category 15-model-evaluation, method card #74.',
        'args': {'y': 'Handle to the time series for the rolling-origin backtest.', 'forecastfunction': 'The model/pipeline that is backtested: rolling-origin cross-validation of ONE forecasting function with signature function(y, h) that returns a forecast object (card 74). Given ONLY as a name from a closed allowlist, never as executable code. Options: naive = Naive / random walk: f(t+k)=y(T). The classic benchmark (FPP3). · seasonal-naive = Seasonal naive: f(t+k)=y(T+k-m). Benchmark for seasonal series; at frequency=1 it degenerates IDENTICALLY to naive (lag=1). · drift = Random walk with drift: naive + mean historical change (FPP3 benchmark). · mean = Mean forecast: f(t+k)=mean(y). Benchmark; bootstrap=True (5000 stochastic paths) is PINNED to False for determinism. · ses = Simple exponential smoothing = ETS(A,N,N) (without trend/seasonality). · holt = Holt linear trend = ETS(A,A,N) (linear trend, without seasonality). · ets = Automatic ETS state-space (error/trend/season selection with AICc); same method as the run_ets node (cat. 02). · auto_arima = Automatic (S)ARIMA with stepwise Hyndman-Khandakar; same method as the run_auto_arima node (cat. 02). · theta = Theta method (Assimakopoulos & Nikolopoulos 2000, M3 winner); same family as the run_theta node (cat. 02). Caution: tsCV re-fits at EVERY origin -> ets/auto_arima are significantly slower than the benchmarks.', 'h': 'Forecast horizon per origin (positive integer, default 1).', 'window': 'Rolling window length (None = expanding· positive integer).', 'initial': 'Observations omitted from the start (>= 0, default 0).'},
        'input_example': {'y': '<series_handle>', 'forecastfunction': 'naive', 'h': 1, 'initial': 0},
    },
    'run_arch_test': {
        'fn': 'run_arch_test',
        'description': 'run_arch_test -- category 15-model-evaluation, method card #77.',
        'args': {'x': 'Handle to a univariate series/residuals for testing ARCH effects.', 'lags': 'Lags of the auxiliary regression (positive integer < length, default 12).', 'demean': 'Removal of the mean of x before the test (default False).'},
        'input_example': {'x': '<series_handle>', 'lags': 12, 'demean': False},
    },
    'run_bg_test': {
        'fn': 'run_bg_test',
        'description': 'run_bg_test -- category 15-model-evaluation, method card #76.',
        'args': {'formula': "Model formula (e.g. 'y ~ x1 + x2') for Breusch-Godfrey serial-correlation.", 'order': 'Order of serial correlation to test (positive integer, default 1).', 'type': 'Statistic type (default Chisq).', 'data': 'Handle to a DataFrame with the formula variables.'},
        'input_example': {'formula': 'y ~ x', 'order': 1},
    },
    'run_bp_test': {
        'fn': 'run_bp_test',
        'description': 'run_bp_test -- category 15-model-evaluation, method card #76.',
        'args': {'formula': 'Model formula for Breusch-Pagan heteroskedasticity.', 'studentize': 'Koenker studentized version (robust to non-normality, default True).', 'data': 'Handle to a DataFrame with the formula variables.'},
        'input_example': {'formula': 'y ~ x', 'studentize': True},
    },
    'run_mcs_procedure': {
        'fn': 'run_mcs_procedure',
        'description': 'run_mcs_procedure -- category 15-model-evaluation, method card #75.',
        'args': {'Loss': 'Handle to a loss matrix (rows=observations, columns=models, >=2 columns).', 'alpha': 'Confidence level = 1 - alpha (alpha in (0,1), default 0.15).', 'B': 'Number of block-bootstrap replications (positive integer, default 1000).', 'statistic': 'Equality test statistic (default Tmax).', 'k': 'Block length of the bootstrap (None = auto· positive integer).', 'min_k': 'Minimum block length (>= 1, default 3).', 'seed': 'Seed for reproducibility of the bootstrap (integer).'},
        'input_example': {'Loss': '<matrix_handle>', 'alpha': 0.15, 'B': 1000, 'min_k': 3},
    },
    'run_reset_test': {
        'fn': 'run_reset_test',
        'description': 'run_reset_test -- category 15-model-evaluation, method card #76.',
        'args': {'formula': 'Model formula for Ramsey RESET functional-form misspecification.', 'power': 'Power of the fitted values in the auxiliary regression (integer >= 2· default 2:3).', 'type': 'Source of the non-linear terms (default fitted).', 'data': 'Handle to a DataFrame with the formula variables.'},
        'input_example': {'formula': 'y ~ x'},
    },
    'sr_crps_parametric': {
        'fn': 'sr_crps_parametric',
        'description': 'sr_crps_parametric -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (realizations).', 'family': 'Family of the predictive distribution (default normal).', 'mean': 'Mean of the predictive normal (default 0).', 'sd': 'Standard deviation of the predictive normal (>0, default 1).', 'df': "Degrees of freedom (required when family='t', >0).", 'location': 'Location of the t (default 0).', 'scale': 'Scale of the t (>0, default 1).'},
        'input_example': {'y': '<raw_handle>', 'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    },
    'sr_crps_sample': {
        'fn': 'sr_crps_sample',
        'description': 'sr_crps_sample -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (one per time· realizations).', 'dat': 'Handle to a matrix of predictive draws (one row per observation, >=2 columns).', 'method': 'CDF estimation: edf=empirical (default, robust), kde=Gaussian kernel.', 'bw': 'Bandwidth for kde (positive· None = auto).'},
        'input_example': {'y': '<raw_handle>', 'dat': '<matrix_handle>'},
    },
    'sr_crps_tailweighted': {
        'fn': 'sr_crps_tailweighted',
        'description': 'sr_crps_tailweighted -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (realizations).', 'dat': 'Handle to a matrix of predictive draws (one row per observation, >=2 columns).', 'side': 'Weight region: left=[-Inf,b], right=[a,Inf], interval=[a,b] (default left, GaR downside).', 'a': 'Lower threshold bound (finite for right/interval).', 'b': 'Upper threshold bound (finite for left/interval).', 'kind': 'threshold=twcrps (indicator weight), outcome=owcrps (default threshold).'},
        'input_example': {'y': '<raw_handle>', 'dat': '<matrix_handle>'},
    },
    'sr_logs_parametric': {
        'fn': 'sr_logs_parametric',
        'description': 'sr_logs_parametric -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (realizations).', 'family': 'Family of the predictive distribution (default normal).', 'mean': 'Mean of the predictive normal (default 0).', 'sd': 'Standard deviation of the predictive normal (>0, default 1).', 'df': "Degrees of freedom (required when family='t', >0).", 'location': 'Location of the t (default 0).', 'scale': 'Scale of the t (>0, default 1).'},
        'input_example': {'y': '<raw_handle>', 'mean': 0, 'sd': 1, 'location': 0, 'scale': 1},
    },
    'sr_logs_sample': {
        'fn': 'sr_logs_sample',
        'description': 'sr_logs_sample -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (realizations).', 'dat': 'Handle to a matrix of predictive draws (one row per observation, >=2 columns).', 'bw': 'KDE bandwidth (positive· None = auto· sensitive in the tails).'},
        'input_example': {'y': '<raw_handle>', 'dat': '<matrix_handle>'},
    },
    'sr_pit_sample': {
        'fn': 'sr_pit_sample',
        'description': 'sr_pit_sample -- category 15-model-evaluation, method card #94.',
        'args': {'y': 'Handle to a bare numeric vector of observations (realizations).', 'dat': 'Handle to a matrix of predictive draws (one row per observation, >=2 columns).'},
        'input_example': {'y': '<raw_handle>', 'dat': '<matrix_handle>'},
    },
    'me_accuracy_table': {
        'fn': 'me_accuracy_table',
        'description': 'me_accuracy_table -- category 15-model-evaluation, method card #513.',
        'args': {'actual': 'Realised values.', 'forecast': 'Forecasts, one column per method.', 'metrics': 'Metrics to compute; omitted = the standard set.', 'insample': 'In-sample series for the scaled metrics.', 'season_length': 'Seasonal period for MASE.', 'by': 'Grouping columns for the table.'},
        'input_example': {'actual': '<df_handle>', 'forecast': '<df_handle>', 'season_length': 1},
    },
    'me_scoring_rules': {
        'fn': 'me_scoring_rules',
        'description': 'me_scoring_rules -- category 15-model-evaluation, method card #514.',
        'args': {'actual': 'Realised values.', 'forecast': 'Predictive samples or quantiles.', 'rule': 'Scoring rule.', 'quantile_levels': 'Quantile levels when the forecast is quantiles.', 'weight': 'Tail weighting.'},
        'input_example': {'actual': '<series_handle>', 'forecast': '<matrix_handle>', 'rule': 'crps', 'weight': 'none'},
    },
    'me_nested_predictive_test': {
        'fn': 'me_nested_predictive_test',
        'description': 'me_nested_predictive_test -- category 15-model-evaluation, method card #515.',
        'args': {'actual': 'Realised values.', 'forecast_restricted': 'Forecast from the nested model.', 'forecast_unrestricted': 'Forecast from the larger model.', 'test': 'Test.', 'state': 'Conditioning variable for the conditional test.', 'horizon': 'Forecast horizon, for the HAC lag.', 'alpha': 'Significance level.'},
        'input_example': {'actual': '<series_handle>', 'forecast_restricted': '<series_handle>', 'forecast_unrestricted': '<series_handle>', 'test': 'clark_west', 'horizon': 1, 'alpha': 0.05},
    },
    'me_superior_predictive_ability': {
        'fn': 'me_superior_predictive_ability',
        'description': 'me_superior_predictive_ability -- category 15-model-evaluation, method card #516.',
        'args': {'losses': 'Loss series, one column per model.', 'benchmark': 'Column holding the benchmark loss.', 'test': 'Test.', 'block_size': 'Bootstrap block length; omitted = automatic.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'alpha': 'Significance level.'},
        'input_example': {'losses': '<df_handle>', 'benchmark': '...', 'test': 'spa', 'nboot': 999, 'seed': 1, 'alpha': 0.05},
    },
    'me_forecast_rationality': {
        'fn': 'me_forecast_rationality',
        'description': 'me_forecast_rationality -- category 15-model-evaluation, method card #517.',
        'args': {'actual': 'Realised values.', 'forecast': 'Forecast to test.', 'rival': 'Rival forecast for the encompassing test.', 'information': 'Information set for orthogonality tests.', 'horizon': 'Forecast horizon, for the HAC lag.', 'alpha': 'Significance level.'},
        'input_example': {'actual': '<series_handle>', 'forecast': '<series_handle>', 'horizon': 1, 'alpha': 0.05},
    },
    'me_interval_evaluation': {
        'fn': 'me_interval_evaluation',
        'description': 'me_interval_evaluation -- category 15-model-evaluation, method card #518.',
        'args': {'actual': 'Realised values.', 'lower': 'Lower bounds, one column per level.', 'upper': 'Upper bounds, one column per level.', 'levels': 'Nominal levels.', 'decompose': 'Decompose the weighted interval score.'},
        'input_example': {'actual': '<series_handle>', 'lower': '<df_handle>', 'upper': '<df_handle>', 'levels': [1.0, 2.0], 'decompose': True},
    },
    'me_density_evaluation': {
        'fn': 'me_density_evaluation',
        'description': 'me_density_evaluation -- category 15-model-evaluation, method card #519.',
        'args': {'actual': 'Realised values.', 'predictive_cdf': 'Predictive CDF evaluated at the outcomes.', 'rival_cdf': 'Rival predictive CDF for comparison.', 'test': 'Test.', 'alpha': 'Significance level.'},
        'input_example': {'actual': '<series_handle>', 'predictive_cdf': '<matrix_handle>', 'test': 'berkowitz', 'alpha': 0.05},
    },
    'me_regression_diagnostics': {
        'fn': 'me_regression_diagnostics',
        'description': 'me_regression_diagnostics -- category 15-model-evaluation, method card #520.',
        'args': {'fit': 'Handle to a fitted regression.', 'tests': 'Tests to run; omitted = the standard set.', 'influence': 'Compute influence measures.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'influence': True, 'alpha': 0.05},
    },
    'me_non_nested_test': {
        'fn': 'me_non_nested_test',
        'description': 'me_non_nested_test -- category 15-model-evaluation, method card #521.',
        'args': {'fit_a': 'Handle to the first fitted model.', 'fit_b': 'Handle to the second fitted model.', 'test': 'Test.', 'correction': 'Vuong correction.', 'alpha': 'Significance level.'},
        'input_example': {'fit_a': '<raw_handle>', 'fit_b': '<raw_handle>', 'test': 'j', 'correction': 'bic', 'alpha': 0.05},
    },
    'me_meta_analysis': {
        'fn': 'me_meta_analysis',
        'description': 'me_meta_analysis -- category 15-model-evaluation, method card #522.',
        'args': {'effects': 'Study effect estimates.', 'standard_errors': 'Study standard errors.', 'model': 'Model.', 'method': 'Heterogeneity estimator.', 'moderators': 'Moderator columns for meta-regression.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'effects': '<series_handle>', 'standard_errors': '<series_handle>', 'model': 'random', 'method': 'dersimonian_laird', 'conf_level': 0.95},
    },
    'me_publication_bias': {
        'fn': 'me_publication_bias',
        'description': 'me_publication_bias -- category 15-model-evaluation, method card #522.',
        'args': {'effects': 'Study effect estimates.', 'standard_errors': 'Study standard errors.', 'method': 'Method.', 'alpha': 'Significance level.'},
        'input_example': {'effects': '<series_handle>', 'standard_errors': '<series_handle>', 'method': 'pet_peese', 'alpha': 0.05},
    },
}
