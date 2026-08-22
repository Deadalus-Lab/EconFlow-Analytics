# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 41-credit-risk-default: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'cr_distance_to_default': {
        'fn': 'cr_distance_to_default',
        'description': 'cr_distance_to_default -- category 41-credit-risk-default, method card #347.',
        'args': {'equity_value': 'Market value of equity.', 'equity_volatility': 'Equity volatility.', 'debt': 'Face value of debt at the horizon.', 'rate': 'Risk-free rate.', 'horizon': 'Horizon in years.', 'barrier': 'Default barrier definition.'},
        'input_example': {'equity_value': '<series_handle>', 'equity_volatility': '<series_handle>', 'debt': '<series_handle>', 'rate': '<series_handle>', 'horizon': 1.0, 'barrier': 'short_plus_half_long'},
    },
    'cr_merton_pd': {
        'fn': 'cr_merton_pd',
        'description': 'cr_merton_pd -- category 41-credit-risk-default, method card #347.',
        'args': {'distance_to_default': 'Distance to default.', 'mapping': 'Mapping to a probability.', 'empirical_map': 'Empirical default frequency table when mapping is empirical.'},
        'input_example': {'distance_to_default': '<series_handle>', 'mapping': 'normal'},
    },
    'cr_transition_matrix': {
        'fn': 'cr_transition_matrix',
        'description': 'cr_transition_matrix -- category 41-credit-risk-default, method card #348.',
        'args': {'data': 'Panel of state observations.', 'id': 'Column identifying the obligor.', 'state': 'Column holding the state.', 'date': 'Column holding the observation date.', 'estimator': 'Estimator.', 'horizon': 'Horizon in years.'},
        'input_example': {'data': '<df_handle>', 'id': '...', 'state': '...', 'date': '...', 'estimator': 'duration', 'horizon': 1.0},
    },
    'cr_generator': {
        'fn': 'cr_generator',
        'description': 'cr_generator -- category 41-credit-risk-default, method card #348.',
        'args': {'transition_matrix': 'Discrete transition matrix.', 'method': 'Embedding method.'},
        'input_example': {'transition_matrix': '<matrix_handle>', 'method': 'qo'},
    },
    'cr_stationary_distribution': {
        'fn': 'cr_stationary_distribution',
        'description': 'cr_stationary_distribution -- category 41-credit-risk-default, method card #348.',
        'args': {'transition_matrix': 'Transition matrix.'},
        'input_example': {'transition_matrix': '<matrix_handle>'},
    },
    'cr_optimal_binning': {
        'fn': 'cr_optimal_binning',
        'description': 'cr_optimal_binning -- category 41-credit-risk-default, method card #349.',
        'args': {'x': 'Characteristic to bin.', 'y': 'Binary default indicator.', 'monotonic_trend': 'Required trend of the default rate.', 'max_bins': 'Maximum number of bins.', 'min_bin_size': 'Minimum share of observations per bin.'},
        'input_example': {'x': '<series_handle>', 'y': '<series_handle>', 'monotonic_trend': 'auto', 'max_bins': 10, 'min_bin_size': 0.05},
    },
    'cr_woe_transform': {
        'fn': 'cr_woe_transform',
        'description': 'cr_woe_transform -- category 41-credit-risk-default, method card #349.',
        'args': {'x': 'Characteristic to transform.', 'y': 'Binary default indicator.', 'bins': 'Bin edges; omitted = fitted here.', 'smoothing': 'Laplace smoothing for empty cells.'},
        'input_example': {'x': '<series_handle>', 'y': '<series_handle>', 'smoothing': 0.5},
    },
    'cr_scorecard': {
        'fn': 'cr_scorecard',
        'description': 'cr_scorecard -- category 41-credit-risk-default, method card #349.',
        'args': {'data': 'Training table.', 'y': 'Binary default indicator column.', 'covariates': 'Characteristic columns.', 'base_points': 'Score at the base odds.', 'pdo': 'Points to double the odds.'},
        'input_example': {'data': '<df_handle>', 'y': '...', 'base_points': 600.0, 'pdo': 20.0},
    },
    'cr_discrimination': {
        'fn': 'cr_discrimination',
        'description': 'cr_discrimination -- category 41-credit-risk-default, method card #350.',
        'args': {'y': 'Binary default indicator.', 'score': 'Model score or predicted probability.'},
        'input_example': {'y': '<series_handle>', 'score': '<series_handle>'},
    },
    'cr_calibration': {
        'fn': 'cr_calibration',
        'description': 'cr_calibration -- category 41-credit-risk-default, method card #350.',
        'args': {'y': 'Binary default indicator.', 'pd': 'Predicted default probability.', 'n_bins': 'Calibration buckets.', 'strategy': 'Bucketing strategy.'},
        'input_example': {'y': '<series_handle>', 'pd': '<series_handle>', 'n_bins': 10, 'strategy': 'quantile'},
    },
    'cr_grade_test': {
        'fn': 'cr_grade_test',
        'description': 'cr_grade_test -- category 41-credit-risk-default, method card #350.',
        'args': {'y': 'Binary default indicator.', 'grade': 'Assigned rating grade.', 'grade_pd': 'PD assigned to each grade.', 'alpha': 'Significance level.'},
        'input_example': {'y': '<series_handle>', 'grade': '<series_handle>', 'grade_pd': '<series_handle>', 'alpha': 0.05},
    },
    'cr_lgd_model': {
        'fn': 'cr_lgd_model',
        'description': 'cr_lgd_model -- category 41-credit-risk-default, method card #351.',
        'args': {'data': 'Table of resolved defaults.', 'lgd': 'Column holding realised loss given default.', 'covariates': 'Covariate columns.', 'model': 'Model family.', 'downturn': 'Indicator column marking downturn periods.'},
        'input_example': {'data': '<df_handle>', 'lgd': '...', 'model': 'fractional'},
    },
    'cr_ead_model': {
        'fn': 'cr_ead_model',
        'description': 'cr_ead_model -- category 41-credit-risk-default, method card #351.',
        'args': {'data': 'Table of resolved defaults.', 'ccf': 'Column holding the realised credit conversion factor.', 'covariates': 'Covariate columns.', 'model': 'Model family.'},
        'input_example': {'data': '<df_handle>', 'ccf': '...', 'model': 'fractional'},
    },
    'cr_lifetime_pd': {
        'fn': 'cr_lifetime_pd',
        'description': 'cr_lifetime_pd -- category 41-credit-risk-default, method card #352.',
        'args': {'data': 'Person-period or duration table.', 'time': 'Column holding the duration or period index.', 'event': 'Column holding the default indicator.', 'covariates': 'Covariate columns.', 'horizon': 'Lifetime horizon in periods.', 'model': 'Hazard model family.'},
        'input_example': {'data': '<df_handle>', 'time': '...', 'event': '...', 'horizon': 10, 'model': 'cox'},
    },
    'cr_pd_scenario': {
        'fn': 'cr_pd_scenario',
        'description': 'cr_pd_scenario -- category 41-credit-risk-default, method card #352.',
        'args': {'fit': 'Handle to a fitted lifetime PD model.', 'scenarios': 'Macroeconomic scenario paths.', 'weights': 'Scenario probability weights.'},
        'input_example': {'fit': '<raw_handle>', 'scenarios': '<df_handle>'},
    },
    'cr_vasicek_loss': {
        'fn': 'cr_vasicek_loss',
        'description': 'cr_vasicek_loss -- category 41-credit-risk-default, method card #353.',
        'args': {'pd': 'Default probability per exposure.', 'lgd': 'Loss given default per exposure.', 'exposure': 'Exposure at default.', 'asset_correlation': 'Asset correlation.', 'confidence': 'Tail level for VaR and ES.'},
        'input_example': {'pd': '<series_handle>', 'lgd': '<series_handle>', 'exposure': '<series_handle>', 'asset_correlation': 1.0, 'confidence': 0.999},
    },
    'cr_credit_monte_carlo': {
        'fn': 'cr_credit_monte_carlo',
        'description': 'cr_credit_monte_carlo -- category 41-credit-risk-default, method card #353.',
        'args': {'pd': 'Default probability per exposure.', 'lgd': 'Loss given default per exposure.', 'exposure': 'Exposure at default.', 'factor_loadings': 'Systematic factor loadings per exposure.', 'n_simulations': 'Monte Carlo draws.', 'confidence': 'Tail level for VaR and ES.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'pd': '<series_handle>', 'lgd': '<series_handle>', 'exposure': '<series_handle>', 'factor_loadings': '<matrix_handle>', 'n_simulations': 100000, 'confidence': 0.999, 'seed': 1},
    },
    'cr_concentration': {
        'fn': 'cr_concentration',
        'description': 'cr_concentration -- category 41-credit-risk-default, method card #353.',
        'args': {'exposure': 'Exposure at default.', 'pd': 'Default probability per exposure.', 'sector': 'Sector label per exposure.'},
        'input_example': {'exposure': '<series_handle>'},
    },
}
