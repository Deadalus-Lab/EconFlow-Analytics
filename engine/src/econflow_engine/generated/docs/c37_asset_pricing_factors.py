# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 37-asset-pricing-factors: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'ap_factor_regression': {
        'fn': 'ap_factor_regression',
        'description': 'ap_factor_regression -- category 37-asset-pricing-factors, method card #316.',
        'args': {'returns': 'Excess returns, one column per test asset.', 'factors': 'Factor returns.', 'cov_type': 'Covariance estimator.', 'bandwidth': 'HAC lag truncation; omitted = automatic.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'returns': '<multiseries_handle>', 'factors': '<multiseries_handle>', 'cov_type': 'hac', 'conf_level': 0.95},
    },
    'ap_alpha_table': {
        'fn': 'ap_alpha_table',
        'description': 'ap_alpha_table -- category 37-asset-pricing-factors, method card #316.',
        'args': {'fit': 'Handle to a fitted factor regression.', 'annualise': 'Report alpha in annual units.'},
        'input_example': {'fit': '<raw_handle>', 'annualise': True},
    },
    'ap_grs_test': {
        'fn': 'ap_grs_test',
        'description': 'ap_grs_test -- category 37-asset-pricing-factors, method card #317.',
        'args': {'returns': 'Excess returns of the test assets.', 'factors': 'Factor returns.', 'alpha': 'Significance level.'},
        'input_example': {'returns': '<multiseries_handle>', 'factors': '<multiseries_handle>', 'alpha': 0.05},
    },
    'ap_fama_macbeth': {
        'fn': 'ap_fama_macbeth',
        'description': 'ap_fama_macbeth -- category 37-asset-pricing-factors, method card #318.',
        'args': {'returns': 'Excess returns of the test assets.', 'factors': 'Factor returns.', 'shanken': 'Apply the errors-in-variables correction.', 'intercept': 'Include a cross-sectional intercept.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'returns': '<multiseries_handle>', 'factors': '<multiseries_handle>', 'shanken': True, 'intercept': True, 'conf_level': 0.95},
    },
    'ap_sdf_gmm': {
        'fn': 'ap_sdf_gmm',
        'description': 'ap_sdf_gmm -- category 37-asset-pricing-factors, method card #319.',
        'args': {'returns': 'Excess returns of the test assets.', 'factors': 'Factor series, traded or not.', 'traded': 'Whether the factors are traded excess returns.', 'weighting': 'GMM weighting.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'returns': '<multiseries_handle>', 'factors': '<multiseries_handle>', 'traded': False, 'weighting': 'hansen_jagannathan', 'conf_level': 0.95},
    },
    'ap_pricing_errors': {
        'fn': 'ap_pricing_errors',
        'description': 'ap_pricing_errors -- category 37-asset-pricing-factors, method card #319.',
        'args': {'fit': 'Handle to a fitted factor-pricing model.'},
        'input_example': {'fit': '<raw_handle>'},
    },
    'ap_portfolio_sort': {
        'fn': 'ap_portfolio_sort',
        'description': 'ap_portfolio_sort -- category 37-asset-pricing-factors, method card #320.',
        'args': {'returns': 'Panel of asset returns.', 'characteristic': 'Panel of the sorting characteristic, lagged.', 'n_portfolios': 'Number of sort bins.', 'weighting': 'Within-portfolio weighting.', 'market_cap': 'Panel of market values for value weighting.'},
        'input_example': {'returns': '<df_handle>', 'characteristic': '<df_handle>', 'n_portfolios': 5, 'weighting': 'equal'},
    },
    'ap_double_sort': {
        'fn': 'ap_double_sort',
        'description': 'ap_double_sort -- category 37-asset-pricing-factors, method card #320.',
        'args': {'returns': 'Panel of asset returns.', 'characteristic_1': 'First sorting characteristic.', 'characteristic_2': 'Second sorting characteristic.', 'n_1': 'Bins on the first characteristic.', 'n_2': 'Bins on the second characteristic.', 'conditional': 'Sort on the second within the first.'},
        'input_example': {'returns': '<df_handle>', 'characteristic_1': '<df_handle>', 'characteristic_2': '<df_handle>', 'n_1': 5, 'n_2': 5, 'conditional': False},
    },
    'ap_pca_factors': {
        'fn': 'ap_pca_factors',
        'description': 'ap_pca_factors -- category 37-asset-pricing-factors, method card #321.',
        'args': {'returns': 'Panel of asset returns.', 'n_factors': 'Factors to extract; omitted = selected by criterion.', 'method': 'Extraction method.', 'criterion': 'Selection criterion when n_factors is omitted.', 'standardise': 'Standardise returns before extraction.'},
        'input_example': {'returns': '<df_handle>', 'method': 'pca', 'criterion': 'bai_ng_icp2', 'standardise': True},
    },
    'ap_n_factors_test': {
        'fn': 'ap_n_factors_test',
        'description': 'ap_n_factors_test -- category 37-asset-pricing-factors, method card #321.',
        'args': {'returns': 'Panel of asset returns.', 'k_max': 'Largest number of factors considered.'},
        'input_example': {'returns': '<df_handle>', 'k_max': 10},
    },
    'ap_event_study': {
        'fn': 'ap_event_study',
        'description': 'ap_event_study -- category 37-asset-pricing-factors, method card #322.',
        'args': {'returns': 'Panel of asset returns.', 'events': 'Event table: asset identifier and event date.', 'market': 'Market return for the normal-return model.', 'model': 'Normal-return model.', 'estimation_window': 'Estimation window offsets.', 'event_window': 'Event window offsets.'},
        'input_example': {'returns': '<df_handle>', 'events': '<df_handle>', 'model': 'market', 'estimation_window': [-250, -30], 'event_window': [-5, 5]},
    },
    'ap_car_test': {
        'fn': 'ap_car_test',
        'description': 'ap_car_test -- category 37-asset-pricing-factors, method card #322.',
        'args': {'fit': 'Handle to a fitted event study.', 'aggregation': 'Aggregation over the window.', 'test': 'Test statistic.', 'alpha': 'Significance level.'},
        'input_example': {'fit': '<raw_handle>', 'aggregation': 'car', 'test': 'patell', 'alpha': 0.05},
    },
    'ap_performance_summary': {
        'fn': 'ap_performance_summary',
        'description': 'ap_performance_summary -- category 37-asset-pricing-factors, method card #323.',
        'args': {'returns': 'Portfolio return series.', 'benchmark': 'Benchmark return series.', 'risk_free': 'Risk-free rate series.', 'frequency': 'Return frequency for annualisation.', 'autocorrelation_adjust': 'Apply the Lo autocorrelation correction.'},
        'input_example': {'returns': '<series_handle>', 'frequency': 'monthly', 'autocorrelation_adjust': True},
    },
    'ap_drawdown': {
        'fn': 'ap_drawdown',
        'description': 'ap_drawdown -- category 37-asset-pricing-factors, method card #323.',
        'args': {'returns': 'Portfolio return series.', 'top_n': 'Number of largest drawdowns to report.'},
        'input_example': {'returns': '<series_handle>', 'top_n': 5},
    },
    'ap_turnover': {
        'fn': 'ap_turnover',
        'description': 'ap_turnover -- category 37-asset-pricing-factors, method card #323.',
        'args': {'weights': 'Panel of portfolio weights over time.', 'cost_bps': 'Round-trip cost in basis points.'},
        'input_example': {'weights': '<df_handle>', 'cost_bps': 10.0},
    },
}
