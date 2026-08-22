# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 38-portfolio-allocation: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'pf_mean_variance': {
        'fn': 'pf_mean_variance',
        'description': 'pf_mean_variance -- category 38-portfolio-allocation, method card #324.',
        'args': {'returns': 'Asset return panel.', 'objective': 'Optimisation objective.', 'target': 'Target return or risk when the objective names one.', 'bounds': 'Lower and upper weight bounds.', 'risk_free': 'Risk-free rate.', 'covariance': 'Covariance estimator.'},
        'input_example': {'returns': '<df_handle>', 'objective': 'max_sharpe', 'bounds': [0.0, 1.0], 'risk_free': 0.0, 'covariance': 'ledoit_wolf'},
    },
    'pf_efficient_frontier': {
        'fn': 'pf_efficient_frontier',
        'description': 'pf_efficient_frontier -- category 38-portfolio-allocation, method card #324.',
        'args': {'returns': 'Asset return panel.', 'n_points': 'Points along the frontier.', 'bounds': 'Lower and upper weight bounds.', 'covariance': 'Covariance estimator.'},
        'input_example': {'returns': '<df_handle>', 'n_points': 50, 'bounds': [0.0, 1.0], 'covariance': 'ledoit_wolf'},
    },
    'pf_covariance': {
        'fn': 'pf_covariance',
        'description': 'pf_covariance -- category 38-portfolio-allocation, method card #325.',
        'args': {'returns': 'Asset return panel.', 'method': 'Estimator.', 'halflife': 'Half-life for the exponential estimator.', 'shrinkage': 'Manual shrinkage intensity; omitted = analytic.'},
        'input_example': {'returns': '<df_handle>', 'method': 'ledoit_wolf'},
    },
    'pf_expected_returns': {
        'fn': 'pf_expected_returns',
        'description': 'pf_expected_returns -- category 38-portfolio-allocation, method card #325.',
        'args': {'returns': 'Asset return panel.', 'method': 'Estimator.', 'halflife': 'Half-life for the exponential estimator.', 'market': 'Market return for the CAPM estimator.'},
        'input_example': {'returns': '<df_handle>', 'method': 'james_stein'},
    },
    'pf_black_litterman': {
        'fn': 'pf_black_litterman',
        'description': 'pf_black_litterman -- category 38-portfolio-allocation, method card #326.',
        'args': {'returns': 'Asset return panel.', 'market_weights': 'Market-capitalisation weights for the prior.', 'views': 'View picking matrix P.', 'view_returns': 'View return vector Q.', 'view_confidence': 'Confidence per view; omitted = proportional to prior variance.', 'tau': 'Scaling of the prior covariance.', 'risk_aversion': 'Risk-aversion coefficient.'},
        'input_example': {'returns': '<df_handle>', 'market_weights': '<series_handle>', 'views': '<matrix_handle>', 'view_returns': [1.0, 2.0], 'tau': 0.05, 'risk_aversion': 2.5},
    },
    'pf_implied_returns': {
        'fn': 'pf_implied_returns',
        'description': 'pf_implied_returns -- category 38-portfolio-allocation, method card #326.',
        'args': {'covariance': 'Asset covariance matrix.', 'market_weights': 'Market-capitalisation weights.', 'risk_aversion': 'Risk-aversion coefficient.'},
        'input_example': {'covariance': '<matrix_handle>', 'market_weights': '<series_handle>', 'risk_aversion': 2.5},
    },
    'pf_risk_parity': {
        'fn': 'pf_risk_parity',
        'description': 'pf_risk_parity -- category 38-portfolio-allocation, method card #327.',
        'args': {'returns': 'Asset return panel.', 'budget': 'Target risk shares; omitted = equal.', 'risk_measure': 'Risk measure the contributions are defined on.', 'bounds': 'Lower and upper weight bounds.'},
        'input_example': {'returns': '<df_handle>', 'risk_measure': 'variance', 'bounds': [0.0, 1.0]},
    },
    'pf_risk_contributions': {
        'fn': 'pf_risk_contributions',
        'description': 'pf_risk_contributions -- category 38-portfolio-allocation, method card #327.',
        'args': {'weights': 'Portfolio weights.', 'covariance': 'Asset covariance matrix.'},
        'input_example': {'weights': '<series_handle>', 'covariance': '<matrix_handle>'},
    },
    'pf_hrp': {
        'fn': 'pf_hrp',
        'description': 'pf_hrp -- category 38-portfolio-allocation, method card #328.',
        'args': {'returns': 'Asset return panel.', 'linkage': 'Hierarchical linkage.', 'distance': 'Distance metric on correlations.', 'risk_measure': 'Risk measure used at each split.'},
        'input_example': {'returns': '<df_handle>', 'linkage': 'ward', 'distance': 'correlation', 'risk_measure': 'variance'},
    },
    'pf_herc': {
        'fn': 'pf_herc',
        'description': 'pf_herc -- category 38-portfolio-allocation, method card #328.',
        'args': {'returns': 'Asset return panel.', 'linkage': 'Hierarchical linkage.', 'n_clusters': 'Clusters to cut the tree at; omitted = gap statistic.', 'risk_measure': 'Risk measure used at each split.'},
        'input_example': {'returns': '<df_handle>', 'linkage': 'ward', 'risk_measure': 'variance'},
    },
    'pf_downside_optimise': {
        'fn': 'pf_downside_optimise',
        'description': 'pf_downside_optimise -- category 38-portfolio-allocation, method card #329.',
        'args': {'returns': 'Asset return panel.', 'risk_measure': 'Risk measure to minimise.', 'confidence': 'Tail level for CVaR and CDaR.', 'target_return': 'Return floor.', 'bounds': 'Lower and upper weight bounds.'},
        'input_example': {'returns': '<df_handle>', 'risk_measure': 'cvar', 'confidence': 0.95, 'bounds': [0.0, 1.0]},
    },
    'pf_kelly': {
        'fn': 'pf_kelly',
        'description': 'pf_kelly -- category 38-portfolio-allocation, method card #329.',
        'args': {'returns': 'Asset return panel.', 'fraction': 'Fraction of full Kelly to apply.', 'bounds': 'Lower and upper weight bounds.'},
        'input_example': {'returns': '<df_handle>', 'fraction': 0.5, 'bounds': [0.0, 1.0]},
    },
    'pf_robust_optimise': {
        'fn': 'pf_robust_optimise',
        'description': 'pf_robust_optimise -- category 38-portfolio-allocation, method card #330.',
        'args': {'returns': 'Asset return panel.', 'uncertainty': 'Uncertainty-set geometry.', 'size': 'Uncertainty radius.', 'objective': 'Objective.', 'bounds': 'Lower and upper weight bounds.'},
        'input_example': {'returns': '<df_handle>', 'uncertainty': 'ellipsoidal', 'size': 1.0, 'objective': 'max_worst_case_return', 'bounds': [0.0, 1.0]},
    },
    'pf_walk_forward': {
        'fn': 'pf_walk_forward',
        'description': 'pf_walk_forward -- category 38-portfolio-allocation, method card #331.',
        'args': {'returns': 'Asset return panel.', 'rule': 'Allocation rule to apply at each rebalance.', 'train_window': 'Estimation window in periods.', 'rebalance_every': 'Periods between rebalances.', 'cost_bps': 'Round-trip cost in basis points.', 'expanding': 'Use an expanding rather than rolling window.'},
        'input_example': {'returns': '<df_handle>', 'rule': 'y ~ x', 'train_window': 252, 'rebalance_every': 21, 'cost_bps': 10.0, 'expanding': False},
    },
    'pf_backtest_summary': {
        'fn': 'pf_backtest_summary',
        'description': 'pf_backtest_summary -- category 38-portfolio-allocation, method card #331.',
        'args': {'backtest': 'Handle to a completed backtest.', 'frequency': 'Return frequency for annualisation.'},
        'input_example': {'backtest': '<raw_handle>', 'frequency': 'daily'},
    },
    'pf_risk_attribution': {
        'fn': 'pf_risk_attribution',
        'description': 'pf_risk_attribution -- category 38-portfolio-allocation, method card #332.',
        'args': {'weights': 'Portfolio weights.', 'returns': 'Asset return panel.', 'risk_measure': 'Risk measure to decompose.', 'confidence': 'Tail level where the measure needs one.'},
        'input_example': {'weights': '<series_handle>', 'returns': '<df_handle>', 'risk_measure': 'volatility', 'confidence': 0.95},
    },
    'pf_factor_attribution': {
        'fn': 'pf_factor_attribution',
        'description': 'pf_factor_attribution -- category 38-portfolio-allocation, method card #332.',
        'args': {'weights': 'Portfolio weights.', 'returns': 'Asset return panel.', 'factors': 'Factor return series.'},
        'input_example': {'weights': '<series_handle>', 'returns': '<df_handle>', 'factors': '<multiseries_handle>'},
    },
}
