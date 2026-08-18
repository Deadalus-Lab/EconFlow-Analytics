# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 24-panel-var -- 4 nodes. No descriptions."""

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
    'pv_bootstrap': NodeMeta(
        fn='pv_bootstrap',
        category='24-panel-var',
        card_id=230,
        contract_hash='c-417027cba4a28806368f281a6f172346f1938165c013fb5ba68184c6050375ca',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('pmb', 'mg', 'mb', )),
        NodeArgMeta(name='n_ahead', kind='integer', required=False),
        NodeArgMeta(name='n_boot', kind='integer', required=False),
        NodeArgMeta(name='b_length', kind='integer', required=False),
        NodeArgMeta(name='b_dim', kind='int_array', required=False),
        NodeArgMeta(name='individual', kind='string', required=False),
        NodeArgMeta(name='level', kind='number', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'n_ahead': 20, 'n_boot': 100, 'b_length': 1, 'b_dim': [1, 1], 'level': 0.9, 'seed': 1},
    ),
    'pv_cointegration': NodeMeta(
        fn='pv_cointegration',
        category='24-panel-var',
        card_id=230,
        contract_hash='c-ef49a8daf71c3859718d82bbed83cf5e505b12e8dc41b242f5698d9ad8b1bc35',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=True),
        NodeArgMeta(name='lags', kind='integer', required=True),
        NodeArgMeta(name='test', kind='enum', required=False, enum=('JO', 'SL', 'BR', 'CAIN', )),
        NodeArgMeta(name='id_col', kind='string', required=False),
        NodeArgMeta(name='det_case', kind='enum', required=False, enum=('Case1', 'Case2', 'Case3', 'Case4', )),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        ),
        defaults={'id_col': 'id'},
    ),
    'pv_estimate': NodeMeta(
        fn='pv_estimate',
        category='24-panel-var',
        card_id=230,
        contract_hash='c-d5223decee505079628d8216be08b063779154c0bd00ae14f28004e9d0f535b7',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=True),
        NodeArgMeta(name='lags', kind='integer', required=True),
        NodeArgMeta(name='id_col', kind='string', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('VAR', 'VEC', )),
        NodeArgMeta(name='type', kind='string', required=False),
        NodeArgMeta(name='dim_r', kind='integer', required=False),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='n_iterations', kind='integer', required=False),
        ),
        defaults={'id_col': 'id'},
    ),
    'pv_identify': NodeMeta(
        fn='pv_identify',
        category='24-panel-var',
        card_id=230,
        contract_hash='c-f7009c005d32c6735580bccbfbfec96fc8c034cba0f201c095542b7180c018bb',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('chol', 'cvm', 'dc', 'iv', 'grt', )),
        NodeArgMeta(name='n_ahead', kind='integer', required=False),
        NodeArgMeta(name='fevd_ahead', kind='integer', required=False),
        NodeArgMeta(name='order_k', kind='raw', required=False),
        NodeArgMeta(name='combine', kind='string', required=False),
        NodeArgMeta(name='iv', kind='df_handle', required=False),
        NodeArgMeta(name='S2', kind='enum', required=False, enum=('MR', 'JL', 'NQ', )),
        NodeArgMeta(name='cov_u', kind='enum', required=False, enum=('OMEGA', 'SIGMA', )),
        NodeArgMeta(name='LR', kind='raw', required=False),
        NodeArgMeta(name='SR', kind='raw', required=False),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'n_ahead': 20, 'fevd_ahead': 10, 'seed': 1},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'pv_bootstrap': {'n_ahead': 20, 'n_boot': 100, 'b_length': 1, 'b_dim': [1, 1], 'level': 0.9, 'seed': 1},
    'pv_cointegration': {'id_col': 'id'},
    'pv_estimate': {'id_col': 'id'},
    'pv_identify': {'n_ahead': 20, 'fevd_ahead': 10, 'seed': 1},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
