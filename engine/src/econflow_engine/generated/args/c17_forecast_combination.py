# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 17-forecast-combination -- 4 nodes. No descriptions."""

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
    'fable_reconcile': NodeMeta(
        fn='fable_reconcile',
        category='17-forecast-combination',
        card_id=209,
        contract_hash='c-e85dd9ed4fdf88154d8d263f0920495cbfd7c992d5570a93b174a3ada844b92d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='index', kind='string', required=True),
        NodeArgMeta(name='keys', kind='series_codes', required=True),
        NodeArgMeta(name='value', kind='string', required=True),
        NodeArgMeta(name='structure', kind='enum', required=False, enum=('nested', 'grouped', )),
        NodeArgMeta(name='base_model', kind='enum', required=False, enum=('arima', 'ets', 'snaive', )),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('wls_struct', 'ols', 'wls_var', 'mint_shrink', 'mint_cov', 'bottom_up', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        ),
        defaults={'h': 8},
    ),
    'foreco_reconcile': NodeMeta(
        fn='foreco_reconcile',
        category='17-forecast-combination',
        card_id=208,
        contract_hash='c-4604f4d75213fa8af0a70a4f5c84da48010c4d5c3684c64c6ca5f21eb8549150',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='type', kind='enum', required=True, enum=('cs', 'te', 'ct', )),
        NodeArgMeta(name='base', kind='matrix_handle', required=True),
        NodeArgMeta(name='agg_mat', kind='matrix_handle', required=False),
        NodeArgMeta(name='agg_order', kind='int_array', required=False),
        NodeArgMeta(name='comb', kind='string', required=False),
        NodeArgMeta(name='tew', kind='enum', required=False, enum=('sum', 'avg', 'first', 'last', )),
        NodeArgMeta(name='approach', kind='enum', required=False, enum=('proj', 'strc', 'proj_osqp', 'strc_osqp', )),
        NodeArgMeta(name='res', kind='matrix_handle', required=False),
        NodeArgMeta(name='nn', kind='enum', required=False, enum=('none', 'osqp', 'sntz', 'bpv', 'nfca', 'nnic', )),
        ),
        defaults={'comb': 'ols'},
    ),
    'profoc_online': NodeMeta(
        fn='profoc_online',
        category='17-forecast-combination',
        card_id=207,
        contract_hash='c-9de96c0f9cb712360573316e84c21ff1b5edcfd8306a2fe8072690893aba4ed8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='matrix_handle', required=True),
        NodeArgMeta(name='experts', kind='raw_handle', required=True),
        NodeArgMeta(name='tau', kind='num_array', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bewa', 'boa', 'ml_poly', 'ewa', )),
        NodeArgMeta(name='loss_function', kind='enum', required=False, enum=('quantile', 'expectile', 'percentage', )),
        NodeArgMeta(name='loss_parameter', kind='number', required=False),
        NodeArgMeta(name='loss_gradient', kind='boolean', required=False),
        NodeArgMeta(name='lead_time', kind='integer', required=False),
        NodeArgMeta(name='forget_regret', kind='number', required=False),
        NodeArgMeta(name='fixed_share', kind='number', required=False),
        NodeArgMeta(name='gamma', kind='number', required=False),
        NodeArgMeta(name='soft_threshold', kind='number', required=False),
        NodeArgMeta(name='hard_threshold', kind='number', required=False),
        NodeArgMeta(name='allow_quantile_crossing', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'loss_parameter': 1, 'loss_gradient': True, 'lead_time': 0, 'forget_regret': 0, 'fixed_share': 0, 'gamma': 1, 'soft_threshold': None, 'hard_threshold': None, 'allow_quantile_crossing': False, 'seed': 2025},
    ),
    'run_hybrid': NodeMeta(
        fn='run_hybrid',
        category='17-forecast-combination',
        card_id=85,
        contract_hash='c-ee6596ef1cfcd992f47544dff6033e6cb8b89a6bb5f4fd6750ea7287864ca466',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='models', kind='string', required=False),
        NodeArgMeta(name='weights', kind='enum', required=False, enum=('equal', 'insample.errors', 'cv.errors', )),
        NodeArgMeta(name='errorMethod', kind='enum', required=False, enum=('RMSE', 'MAE', 'MASE', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        NodeArgMeta(name='PI_combination', kind='enum', required=False, enum=('extreme', 'mean', )),
        NodeArgMeta(name='cvHorizon', kind='integer', required=False),
        NodeArgMeta(name='windowSize', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'models': 'aefnst', 'windowSize': 84, 'seed': 42},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'fable_reconcile': {'h': 8},
    'foreco_reconcile': {'comb': 'ols'},
    'profoc_online': {'loss_parameter': 1, 'loss_gradient': True, 'lead_time': 0, 'forget_regret': 0, 'fixed_share': 0, 'gamma': 1, 'soft_threshold': None, 'hard_threshold': None, 'allow_quantile_crossing': False, 'seed': 2025},
    'run_hybrid': {'models': 'aefnst', 'windowSize': 84, 'seed': 42},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
