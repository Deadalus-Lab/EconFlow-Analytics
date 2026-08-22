# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 38-portfolio-allocation -- 17 nodes. No descriptions."""

from functools import cache

from pydantic import BaseModel

from econflow_engine.kinds import (
    NodeArgMeta,
    NodeExecutabilityMeta,
    NodeMeta,
    build_authoring_model,
    build_wire_model,
)

NODE_META: dict[str, NodeMeta] = {
    'pf_mean_variance': NodeMeta(
        fn='pf_mean_variance',
        category='38-portfolio-allocation',
        card_id=324,
        contract_hash='c2-c184c2f604c3e6c0b47afc5a8805488cd93d5a150319902cc94797fc75b9541e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='objective', kind='enum', required=False, enum=('max_sharpe', 'min_volatility', 'max_return', 'target_return', 'target_risk', 'max_utility', )),
        NodeArgMeta(name='target', kind='number', required=False),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        NodeArgMeta(name='risk_free', kind='number', required=False),
        NodeArgMeta(name='covariance', kind='enum', required=False, enum=('sample', 'ledoit_wolf', 'oas', 'exponential', 'denoised', )),
        ),
        defaults={'objective': 'max_sharpe', 'bounds': [0.0, 1.0], 'risk_free': 0.0, 'covariance': 'ledoit_wolf'},
    ),
    'pf_efficient_frontier': NodeMeta(
        fn='pf_efficient_frontier',
        category='38-portfolio-allocation',
        card_id=324,
        contract_hash='c2-c3e3fe758a6863e1af3b99bf15b980d76fd48aa1685c045a756aa7c6772db810',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='n_points', kind='integer', required=False),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        NodeArgMeta(name='covariance', kind='enum', required=False, enum=('sample', 'ledoit_wolf', 'oas', 'exponential', 'denoised', )),
        ),
        defaults={'n_points': 50, 'bounds': [0.0, 1.0], 'covariance': 'ledoit_wolf'},
    ),
    'pf_covariance': NodeMeta(
        fn='pf_covariance',
        category='38-portfolio-allocation',
        card_id=325,
        contract_hash='c2-585b46f6923156f3099639e56a79c3bcd6690f70e82d2ffd98e4cbde59ae119e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('sample', 'ledoit_wolf', 'oas', 'shrunk', 'exponential', 'denoised', 'detoned', 'graphical_lasso', )),
        NodeArgMeta(name='halflife', kind='integer', required=False),
        NodeArgMeta(name='shrinkage', kind='number', required=False),
        ),
        defaults={'method': 'ledoit_wolf'},
    ),
    'pf_expected_returns': NodeMeta(
        fn='pf_expected_returns',
        category='38-portfolio-allocation',
        card_id=325,
        contract_hash='c2-e1fba40b7abfb869f7f6db951664018538d1b394a38eabb747b5fb34ad5f61eb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('sample', 'exponential', 'james_stein', 'bayes_stein', 'capm', 'equal', )),
        NodeArgMeta(name='halflife', kind='integer', required=False),
        NodeArgMeta(name='market', kind='series_handle', required=False),
        ),
        defaults={'method': 'james_stein'},
    ),
    'pf_black_litterman': NodeMeta(
        fn='pf_black_litterman',
        category='38-portfolio-allocation',
        card_id=326,
        contract_hash='c2-2c9654fa602d4c06f28d0f28262b5ae87f654275a32ca6ee6523b4641f9c82a9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='market_weights', kind='series_handle', required=True),
        NodeArgMeta(name='views', kind='matrix_handle', required=True),
        NodeArgMeta(name='view_returns', kind='num_array', required=True),
        NodeArgMeta(name='view_confidence', kind='num_array', required=False),
        NodeArgMeta(name='tau', kind='number', required=False),
        NodeArgMeta(name='risk_aversion', kind='number', required=False),
        ),
        defaults={'tau': 0.05, 'risk_aversion': 2.5},
    ),
    'pf_implied_returns': NodeMeta(
        fn='pf_implied_returns',
        category='38-portfolio-allocation',
        card_id=326,
        contract_hash='c2-153f9c64b57cc32e0ac13e282c73888e47da5fc7d53aea108d51483220a4460c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='covariance', kind='matrix_handle', required=True),
        NodeArgMeta(name='market_weights', kind='series_handle', required=True),
        NodeArgMeta(name='risk_aversion', kind='number', required=False),
        ),
        defaults={'risk_aversion': 2.5},
    ),
    'pf_risk_parity': NodeMeta(
        fn='pf_risk_parity',
        category='38-portfolio-allocation',
        card_id=327,
        contract_hash='c2-0ca694df8b0ceff2a34eb4adfa4e0bab2a6275b442cf2bd57e66dd46124ab917',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='budget', kind='num_array', required=False),
        NodeArgMeta(name='risk_measure', kind='enum', required=False, enum=('variance', 'mad', 'cvar', 'cdar', 'evar', )),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        ),
        defaults={'risk_measure': 'variance', 'bounds': [0.0, 1.0]},
    ),
    'pf_risk_contributions': NodeMeta(
        fn='pf_risk_contributions',
        category='38-portfolio-allocation',
        card_id=327,
        contract_hash='c2-88e8f8d3a72e611e86dd9b847b7e2e7cd3d9aaaf0f9701a9ee6456792c20c587',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='weights', kind='series_handle', required=True),
        NodeArgMeta(name='covariance', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'pf_hrp': NodeMeta(
        fn='pf_hrp',
        category='38-portfolio-allocation',
        card_id=328,
        contract_hash='c2-675306ff4c8620329e7a3745ba602b5d8924a9c9b35f92fa71d3fb6aaf23f1cf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='linkage', kind='enum', required=False, enum=('single', 'complete', 'average', 'ward', )),
        NodeArgMeta(name='distance', kind='enum', required=False, enum=('correlation', 'absolute_correlation', 'distance_correlation', )),
        NodeArgMeta(name='risk_measure', kind='enum', required=False, enum=('variance', 'mad', 'cvar', 'cdar', )),
        ),
        defaults={'linkage': 'ward', 'distance': 'correlation', 'risk_measure': 'variance'},
    ),
    'pf_herc': NodeMeta(
        fn='pf_herc',
        category='38-portfolio-allocation',
        card_id=328,
        contract_hash='c2-862243c28b56d7a30f00926ef1a3980b5eace8ff8e19e9cbfccfa78cfe083ce0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='linkage', kind='enum', required=False, enum=('single', 'complete', 'average', 'ward', )),
        NodeArgMeta(name='n_clusters', kind='integer', required=False),
        NodeArgMeta(name='risk_measure', kind='enum', required=False, enum=('variance', 'mad', 'cvar', 'cdar', )),
        ),
        defaults={'linkage': 'ward', 'risk_measure': 'variance'},
    ),
    'pf_downside_optimise': NodeMeta(
        fn='pf_downside_optimise',
        category='38-portfolio-allocation',
        card_id=329,
        contract_hash='c2-e648cb92b69e52c31d1186ff4f61034772e52cf24a70d59e1725a1d1db694c58',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='risk_measure', kind='enum', required=False, enum=('cvar', 'cdar', 'semivariance', 'evar', 'worst_realisation', 'max_drawdown', )),
        NodeArgMeta(name='confidence', kind='number', required=False),
        NodeArgMeta(name='target_return', kind='number', required=False),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        ),
        defaults={'risk_measure': 'cvar', 'confidence': 0.95, 'bounds': [0.0, 1.0]},
    ),
    'pf_kelly': NodeMeta(
        fn='pf_kelly',
        category='38-portfolio-allocation',
        card_id=329,
        contract_hash='c2-ea9d148138d95cd3818893c53e88063d676fddb6d63c53ca40ddd3bd909e2d85',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='fraction', kind='number', required=False),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        ),
        defaults={'fraction': 0.5, 'bounds': [0.0, 1.0]},
    ),
    'pf_robust_optimise': NodeMeta(
        fn='pf_robust_optimise',
        category='38-portfolio-allocation',
        card_id=330,
        contract_hash='c2-d2a6b4508363f01cbce153f14e4d4180996e2f6e3432eab67a8c1b1cba736781',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='uncertainty', kind='enum', required=False, enum=('box', 'ellipsoidal', 'budget', )),
        NodeArgMeta(name='size', kind='number', required=False),
        NodeArgMeta(name='objective', kind='enum', required=False, enum=('max_worst_case_return', 'min_worst_case_risk', )),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        ),
        defaults={'uncertainty': 'ellipsoidal', 'size': 1.0, 'objective': 'max_worst_case_return', 'bounds': [0.0, 1.0]},
    ),
    'pf_walk_forward': NodeMeta(
        fn='pf_walk_forward',
        category='38-portfolio-allocation',
        card_id=331,
        contract_hash='c2-d84be31f5e06b2fb573338b7a0b27c9d1d1640c3e8b5ba172c7ce293a20e13bd',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='rule', kind='formula', required=True),
        NodeArgMeta(name='train_window', kind='integer', required=False),
        NodeArgMeta(name='rebalance_every', kind='integer', required=False),
        NodeArgMeta(name='cost_bps', kind='number', required=False),
        NodeArgMeta(name='expanding', kind='boolean', required=False),
        ),
        defaults={'train_window': 252, 'rebalance_every': 21, 'cost_bps': 10.0, 'expanding': False},
    ),
    'pf_backtest_summary': NodeMeta(
        fn='pf_backtest_summary',
        category='38-portfolio-allocation',
        card_id=331,
        contract_hash='c2-6e751ef8316958da6ad79e481b65831011867553932116230cadd90e3b1297d2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='backtest', kind='raw_handle', required=True),
        NodeArgMeta(name='frequency', kind='enum', required=False, enum=('daily', 'weekly', 'monthly', )),
        ),
        defaults={'frequency': 'daily'},
    ),
    'pf_risk_attribution': NodeMeta(
        fn='pf_risk_attribution',
        category='38-portfolio-allocation',
        card_id=332,
        contract_hash='c2-ac1d5055f9a6b675ac9132e49de32095ad40e8bf6c7202dc04a6df1b251234ed',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='weights', kind='series_handle', required=True),
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='risk_measure', kind='enum', required=False, enum=('volatility', 'cvar', 'var', 'mad', )),
        NodeArgMeta(name='confidence', kind='number', required=False),
        ),
        defaults={'risk_measure': 'volatility', 'confidence': 0.95},
    ),
    'pf_factor_attribution': NodeMeta(
        fn='pf_factor_attribution',
        category='38-portfolio-allocation',
        card_id=332,
        contract_hash='c2-cb6d03cbe23626a050ab66d8ff8a4b764afbbe35c3d0403f19ef29797a1221f3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='weights', kind='series_handle', required=True),
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='factors', kind='multiseries_handle', required=True),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'pf_mean_variance': {'objective': 'max_sharpe', 'bounds': [0.0, 1.0], 'risk_free': 0.0, 'covariance': 'ledoit_wolf'},
    'pf_efficient_frontier': {'n_points': 50, 'bounds': [0.0, 1.0], 'covariance': 'ledoit_wolf'},
    'pf_covariance': {'method': 'ledoit_wolf'},
    'pf_expected_returns': {'method': 'james_stein'},
    'pf_black_litterman': {'tau': 0.05, 'risk_aversion': 2.5},
    'pf_implied_returns': {'risk_aversion': 2.5},
    'pf_risk_parity': {'risk_measure': 'variance', 'bounds': [0.0, 1.0]},
    'pf_risk_contributions': {},
    'pf_hrp': {'linkage': 'ward', 'distance': 'correlation', 'risk_measure': 'variance'},
    'pf_herc': {'linkage': 'ward', 'risk_measure': 'variance'},
    'pf_downside_optimise': {'risk_measure': 'cvar', 'confidence': 0.95, 'bounds': [0.0, 1.0]},
    'pf_kelly': {'fraction': 0.5, 'bounds': [0.0, 1.0]},
    'pf_robust_optimise': {'uncertainty': 'ellipsoidal', 'size': 1.0, 'objective': 'max_worst_case_return', 'bounds': [0.0, 1.0]},
    'pf_walk_forward': {'train_window': 252, 'rebalance_every': 21, 'cost_bps': 10.0, 'expanding': False},
    'pf_backtest_summary': {'frequency': 'daily'},
    'pf_risk_attribution': {'risk_measure': 'volatility', 'confidence': 0.95},
    'pf_factor_attribution': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
