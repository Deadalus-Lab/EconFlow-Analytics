# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 24-panel-var -- 9 nodes. No descriptions."""

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
        contract_hash='c2-6b8cd172278141c17169b43a55f5c77d306f78efd6f8b327cd7054bdd2e6a0b4',
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
        contract_hash='c2-5bb1cf045c007a6de4ecc8331ea96699640a05067cbc41710a79c095facd76b2',
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
        contract_hash='c2-54a0c57e9be06be21ed28594c07e24383d0d73c2063a1052a5a2f278107e6b38',
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
        contract_hash='c2-c4a409468a0cbddf3e736457ec933d354c7e2fa49864025beb3e8889bb7388a7',
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
    'pv_gmm_panel_var': NodeMeta(
        fn='pv_gmm_panel_var',
        category='24-panel-var',
        card_id=569,
        contract_hash='c2-e150ce062d84929cfaba031805871e3ed04e62953e805a5cc3d39ba2312a672c',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=True),
        NodeArgMeta(name='unit', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='estimator', kind='enum', required=False, enum=('difference', 'system', )),
        NodeArgMeta(name='max_instrument_lags', kind='integer', required=False),
        NodeArgMeta(name='collapse', kind='boolean', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'lags': 1, 'estimator': 'system', 'max_instrument_lags': 3, 'collapse': True, 'conf_level': 0.95},
    ),
    'pv_panel_granger': NodeMeta(
        fn='pv_panel_granger',
        category='24-panel-var',
        card_id=570,
        contract_hash='c2-351e0a24cc0f61b186845ef384256e1509034d57bad1f33886d732bb008f98cb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='y', kind='string', required=True),
        NodeArgMeta(name='x', kind='string', required=True),
        NodeArgMeta(name='unit', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'lags': 1, 'nboot': 0, 'alpha': 0.05},
    ),
    'pv_panel_lp': NodeMeta(
        fn='pv_panel_lp',
        category='24-panel-var',
        card_id=571,
        contract_hash='c2-a71da8791cc2452914f97e4c7c8c27c7c292f927083d3a7b42bed0f2e579f91e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='y', kind='string', required=True),
        NodeArgMeta(name='shock', kind='string', required=True),
        NodeArgMeta(name='unit', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='controls', kind='series_codes', required=False),
        NodeArgMeta(name='horizons', kind='integer', required=False),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='cov_type', kind='enum', required=False, enum=('driscoll_kraay', 'cluster', 'robust', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'horizons': 20, 'lags': 4, 'cov_type': 'driscoll_kraay', 'conf_level': 0.95},
    ),
    'pv_cd_diagnostics': NodeMeta(
        fn='pv_cd_diagnostics',
        category='24-panel-var',
        card_id=572,
        contract_hash='c2-eb099423fa8ef3fce8d2e435ba9814e4e310d693e1fa51001136057095e84f49',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='residuals', kind='df_handle', required=True),
        NodeArgMeta(name='unit', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'n_factors': 3, 'alpha': 0.05},
    ),
    'pv_gvar_weights': NodeMeta(
        fn='pv_gvar_weights',
        category='24-panel-var',
        card_id=573,
        contract_hash='c2-5d144c04219c522de71b50d866a03ccfd93fef70b7d26ad31f42bdbbc5d04528',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='weights', kind='matrix_handle', required=True),
        NodeArgMeta(name='country', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=False),
        NodeArgMeta(name='time_varying', kind='boolean', required=False),
        NodeArgMeta(name='normalise', kind='boolean', required=False),
        ),
        defaults={'time_varying': False, 'normalise': True},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'pv_bootstrap': {'n_ahead': 20, 'n_boot': 100, 'b_length': 1, 'b_dim': [1, 1], 'level': 0.9, 'seed': 1},
    'pv_cointegration': {'id_col': 'id'},
    'pv_estimate': {'id_col': 'id'},
    'pv_identify': {'n_ahead': 20, 'fevd_ahead': 10, 'seed': 1},
    'pv_gmm_panel_var': {'lags': 1, 'estimator': 'system', 'max_instrument_lags': 3, 'collapse': True, 'conf_level': 0.95},
    'pv_panel_granger': {'lags': 1, 'nboot': 0, 'alpha': 0.05},
    'pv_panel_lp': {'horizons': 20, 'lags': 4, 'cov_type': 'driscoll_kraay', 'conf_level': 0.95},
    'pv_cd_diagnostics': {'n_factors': 3, 'alpha': 0.05},
    'pv_gvar_weights': {'time_varying': False, 'normalise': True},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
