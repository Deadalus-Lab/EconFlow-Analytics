# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 19-business-cycle-dating -- 7 nodes. No descriptions."""

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
        contract_hash='c-e23bdf5dd95770aa594b5aeb44a3ca4d5507b4e75f1cf00af31ec1817ad1c3ac',
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
        contract_hash='c-cfe9cb7c15722cef7ffbd498080e8f10f6e460a93974769520f919422e9c3ea1',
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
        contract_hash='c-d6c4494c0574b606e9774d956549c1de0137430f7f66dfd5a1590e1febff19ed',
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
        contract_hash='c-9c8f64b4e349eebb38bce5f475a439f99b03ddc7d752260dc10804f8ab6c0f2a',
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
        contract_hash='c-7523c8b51e09d3b63dfe2f335983fb7c77c2c5aa19f30d067665cebde1fde6ac',
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
        contract_hash='c-9431a5e5a56833753b6caaedb567e97acbdf89e08dd6146f4b1ca8a7fec0b3e5',
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
        contract_hash='c-17877f5fd9840018472c3665afffd3b467a2b5eba84759ccb4ee7611c5a97419',
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
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
