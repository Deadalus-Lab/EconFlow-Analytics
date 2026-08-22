# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 19-business-cycle-dating -- 14 nodes. No descriptions."""

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
    'average_over_phases': NodeMeta(
        fn='average_over_phases',
        category='19-business-cycle-dating',
        card_id=88,
        contract_hash='c2-e5900f77c9ef4be0f6b0e3e4726e12e639ff941bded152bceceb846c64985062',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='series', kind='series_handle', required=True),
        NodeArgMeta(name='dates', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'changepoint_segments': NodeMeta(
        fn='changepoint_segments',
        category='19-business-cycle-dating',
        card_id=213,
        contract_hash='c2-8e24461d5b53ae2598a2cd8710d578683ba3cc10b84642b368268a9ab29f2d3c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'date_business_cycles': NodeMeta(
        fn='date_business_cycles',
        category='19-business-cycle-dating',
        card_id=88,
        contract_hash='c2-3418d3cdedb29f1f341522106ec42b498b0cd9b259c331a3ce73a4cfa20eb998',
        register_field='bcdating',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='mincycle', kind='integer', required=False),
        NodeArgMeta(name='minphase', kind='integer', required=False),
        NodeArgMeta(name='name', kind='string', required=False),
        ),
        defaults={'mincycle': 5, 'minphase': 2},
    ),
    'detect_change_points': NodeMeta(
        fn='detect_change_points',
        category='19-business-cycle-dating',
        card_id=214,
        contract_hash='c2-7a0bafbae9a243893410348d5285a7e9f15ca925ad7fae25313d6027412fc16e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='mcmc',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='p0', kind='number', required=False),
        NodeArgMeta(name='w0', kind='number', required=False),
        NodeArgMeta(name='burnin', kind='integer', required=False),
        NodeArgMeta(name='mcmc', kind='integer', required=False),
        NodeArgMeta(name='threshold', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'p0': 0.2, 'w0': 0.2, 'burnin': 50, 'mcmc': 500, 'threshold': 0.5, 'seed': 20240719},
    ),
    'detect_changepoints': NodeMeta(
        fn='detect_changepoints',
        category='19-business-cycle-dating',
        card_id=213,
        contract_hash='c2-1de04d394ef39a7e017eeab841a7147910f98fe17a3990879364a9a853989550',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='statistic', kind='enum', required=False, enum=('mean', 'variance', 'meanvar', )),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('MBIC', 'SIC', 'BIC', 'AIC', 'Hannan-Quinn', 'Asymptotic', 'Manual', 'None', )),
        NodeArgMeta(name='pen_value', kind='number', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('PELT', 'AMOC', 'SegNeigh', 'BinSeg', )),
        NodeArgMeta(name='Q', kind='integer', required=False),
        NodeArgMeta(name='test_stat', kind='string', required=False),
        NodeArgMeta(name='minseglen', kind='integer', required=False),
        NodeArgMeta(name='know_mean', kind='boolean', required=False),
        NodeArgMeta(name='mu', kind='number', required=False),
        NodeArgMeta(name='shape', kind='number', required=False),
        ),
        defaults={'pen_value': 0, 'Q': 5, 'know_mean': False, 'shape': 1},
    ),
    'detect_changepoints_agglo': NodeMeta(
        fn='detect_changepoints_agglo',
        category='19-business-cycle-dating',
        card_id=215,
        contract_hash='c2-2602e8711f40213873a3e67a04346248e151b7569c99ac58cf01106c57084f73',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='X', kind='matrix_handle', required=True),
        NodeArgMeta(name='member', kind='int_array', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        NodeArgMeta(name='penalty', kind='enum', required=False, enum=('none', 'num_cp', )),
        ),
        defaults={'alpha': 1},
    ),
    'detect_changepoints_divisive': NodeMeta(
        fn='detect_changepoints_divisive',
        category='19-business-cycle-dating',
        card_id=215,
        contract_hash='c2-3392bb0fa0c6f80ae98bafb0338924139eb474504edf806d1532132e1b1cf69e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='X', kind='matrix_handle', required=True),
        NodeArgMeta(name='sig_lvl', kind='number', required=False),
        NodeArgMeta(name='n_permutations', kind='integer', required=False),
        NodeArgMeta(name='min_size', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        NodeArgMeta(name='k', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'sig_lvl': 0.05, 'n_permutations': 199, 'min_size': 30, 'alpha': 1, 'seed': 20240101},
    ),
    'bc_ms_recession': NodeMeta(
        fn='bc_ms_recession',
        category='19-business-cycle-dating',
        card_id=540,
        contract_hash='c2-09dee59bed1ac719a0d4d9fdd7d963c63bc91773695795620d88d812cec10caf',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='k_regimes', kind='integer', required=False),
        NodeArgMeta(name='order', kind='integer', required=False),
        NodeArgMeta(name='switching_variance', kind='boolean', required=False),
        NodeArgMeta(name='threshold', kind='number', required=False),
        NodeArgMeta(name='n_starts', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'k_regimes': 2, 'order': 4, 'switching_variance': True, 'threshold': 0.5, 'n_starts': 10},
    ),
    'bc_ms_factor': NodeMeta(
        fn='bc_ms_factor',
        category='19-business-cycle-dating',
        card_id=540,
        contract_hash='c2-0a1bb9d0dc6d21e219456d05d377db10489531bb923f8bad0101638b47bf27a3',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='k_regimes', kind='integer', required=False),
        NodeArgMeta(name='factor_order', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'k_regimes': 2, 'factor_order': 2},
    ),
    'bc_bry_boschan': NodeMeta(
        fn='bc_bry_boschan',
        category='19-business-cycle-dating',
        card_id=541,
        contract_hash='c2-efb947ea0fe76bff2c062d1098671ef4ad5310a4959c6de8bc1fb4203127151e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='min_phase', kind='integer', required=False),
        NodeArgMeta(name='min_cycle', kind='integer', required=False),
        NodeArgMeta(name='smoothing', kind='enum', required=False, enum=('none', 'mcd', 'spencer', 'henderson', )),
        NodeArgMeta(name='end_censor', kind='integer', required=False),
        ),
        defaults={'min_phase': 5, 'min_cycle': 15, 'smoothing': 'spencer', 'end_censor': 6},
    ),
    'bc_cycle_statistics': NodeMeta(
        fn='bc_cycle_statistics',
        category='19-business-cycle-dating',
        card_id=541,
        contract_hash='c2-59a4d54d30898809e158685380f98d1b35cbcf964a80b44c878b28925b646d0c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='peaks', kind='int_array', required=True),
        NodeArgMeta(name='troughs', kind='int_array', required=True),
        ),
        defaults={},
    ),
    'bc_online_change_detection': NodeMeta(
        fn='bc_online_change_detection',
        category='19-business-cycle-dating',
        card_id=542,
        contract_hash='c2-9a48d6ed7bc8a94bfdb6909b480c5575560690ff0261db1d3eeea86ee9469604',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('cusum', 'page_hinkley', 'bocpd', 'ewma', )),
        NodeArgMeta(name='threshold', kind='number', required=False),
        NodeArgMeta(name='hazard', kind='number', required=False),
        NodeArgMeta(name='burn_in', kind='integer', required=False),
        ),
        defaults={'method': 'bocpd', 'hazard': 0.01, 'burn_in': 50},
    ),
    'bc_multivariate_changepoints': NodeMeta(
        fn='bc_multivariate_changepoints',
        category='19-business-cycle-dating',
        card_id=543,
        contract_hash='c2-cf81f4bda0d2d5b69453002b4ef54b5736d4f8f4a9ef5260bb65fc9705136bd3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('l1', 'l2', 'rbf', 'linear', 'normal', 'ar', )),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('pelt', 'binseg', 'dynp', 'window', 'bottomup', )),
        NodeArgMeta(name='penalty', kind='number', required=False),
        NodeArgMeta(name='n_changepoints', kind='integer', required=False),
        NodeArgMeta(name='min_size', kind='integer', required=False),
        ),
        defaults={'model': 'rbf', 'method': 'pelt', 'min_size': 5},
    ),
    'bc_matrix_profile': NodeMeta(
        fn='bc_matrix_profile',
        category='19-business-cycle-dating',
        card_id=544,
        contract_hash='c2-e14ba064c5c41e6e44219a585a961a36f2a096290069bfbbb84863263151c794',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='window', kind='integer', required=True),
        NodeArgMeta(name='n_motifs', kind='integer', required=False),
        NodeArgMeta(name='n_discords', kind='integer', required=False),
        NodeArgMeta(name='normalise', kind='boolean', required=False),
        ),
        defaults={'n_motifs': 3, 'n_discords': 3, 'normalise': True},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'average_over_phases': {},
    'changepoint_segments': {},
    'date_business_cycles': {'mincycle': 5, 'minphase': 2},
    'detect_change_points': {'p0': 0.2, 'w0': 0.2, 'burnin': 50, 'mcmc': 500, 'threshold': 0.5, 'seed': 20240719},
    'detect_changepoints': {'pen_value': 0, 'Q': 5, 'know_mean': False, 'shape': 1},
    'detect_changepoints_agglo': {'alpha': 1},
    'detect_changepoints_divisive': {'sig_lvl': 0.05, 'n_permutations': 199, 'min_size': 30, 'alpha': 1, 'seed': 20240101},
    'bc_ms_recession': {'k_regimes': 2, 'order': 4, 'switching_variance': True, 'threshold': 0.5, 'n_starts': 10},
    'bc_ms_factor': {'k_regimes': 2, 'factor_order': 2},
    'bc_bry_boschan': {'min_phase': 5, 'min_cycle': 15, 'smoothing': 'spencer', 'end_censor': 6},
    'bc_cycle_statistics': {},
    'bc_online_change_detection': {'method': 'bocpd', 'hazard': 0.01, 'burn_in': 50},
    'bc_multivariate_changepoints': {'model': 'rbf', 'method': 'pelt', 'min_size': 5},
    'bc_matrix_profile': {'n_motifs': 3, 'n_discords': 3, 'normalise': True},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
