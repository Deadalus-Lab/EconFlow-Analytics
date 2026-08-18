# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 13-dsge-general-equilibrium -- 12 nodes. No descriptions."""

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
    'bimets_estimate': NodeMeta(
        fn='bimets_estimate',
        category='13-dsge-general-equilibrium',
        card_id=201,
        contract_hash='c-578529502f62682b39645e17e422e1fb3f95d87c5758693ab56bcce3c4ab9ad7',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='model', kind='string', required=True),
        NodeArgMeta(name='data', kind='multiseries_handle', required=True),
        NodeArgMeta(name='tsrange', kind='raw', required=False),
        NodeArgMeta(name='estTech', kind='enum', required=False, enum=('OLS', 'IV', )),
        NodeArgMeta(name='iv', kind='raw', required=False),
        NodeArgMeta(name='eqList', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'bimets_multipliers': NodeMeta(
        fn='bimets_multipliers',
        category='13-dsge-general-equilibrium',
        card_id=201,
        contract_hash='c-1d8e45c5374671d23529442800155b2d761b307fd9217a7c4cb02d54b4f75497',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='tsrange', kind='raw', required=True),
        NodeArgMeta(name='target', kind='series_codes', required=True),
        NodeArgMeta(name='instrument', kind='series_codes', required=True),
        NodeArgMeta(name='mm_shock', kind='number', required=False),
        NodeArgMeta(name='simType', kind='enum', required=False, enum=('DYNAMIC', 'FORECAST', 'STATIC', )),
        NodeArgMeta(name='simAlgo', kind='enum', required=False, enum=('GAUSS-SEIDEL', 'NEWTON', 'FULLNEWTON', )),
        ),
        defaults={'mm_shock': 1e-05},
    ),
    'bimets_simulate': NodeMeta(
        fn='bimets_simulate',
        category='13-dsge-general-equilibrium',
        card_id=201,
        contract_hash='c-4fbbd6252b8db3c27cba482899eaaf319b332f92c76d4801a265b5d6739ef138',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='tsrange', kind='raw', required=True),
        NodeArgMeta(name='simType', kind='enum', required=False, enum=('DYNAMIC', 'FORECAST', 'STATIC', )),
        NodeArgMeta(name='simAlgo', kind='enum', required=False, enum=('GAUSS-SEIDEL', 'NEWTON', 'FULLNEWTON', )),
        NodeArgMeta(name='stochastic', kind='boolean', required=False),
        NodeArgMeta(name='stoch_replica', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        NodeArgMeta(name='simConvergence', kind='number', required=False),
        NodeArgMeta(name='simIterLimit', kind='integer', required=False),
        ),
        defaults={'stochastic': False, 'stoch_replica': 100, 'seed': 2025, 'simConvergence': 1e-05, 'simIterLimit': 100},
    ),
    'cge_solve': NodeMeta(
        fn='cge_solve',
        category='13-dsge-general-equilibrium',
        card_id=202,
        contract_hash='c-52e81e3e066358cd0dcf688cea0be221bfe384039d226f539e3d293f4793d726',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='dstype', kind='enum', required=False, enum=('constant', 'CD', 'CES', )),
        NodeArgMeta(name='A', kind='matrix_handle', required=False),
        NodeArgMeta(name='Beta', kind='matrix_handle', required=False),
        NodeArgMeta(name='alpha', kind='num_array', required=False),
        NodeArgMeta(name='sigma', kind='num_array', required=False),
        NodeArgMeta(name='Theta', kind='matrix_handle', required=False),
        NodeArgMeta(name='B', kind='matrix_handle', required=False),
        NodeArgMeta(name='S0Exg', kind='matrix_handle', required=False),
        NodeArgMeta(name='p0', kind='num_array', required=False),
        NodeArgMeta(name='z0', kind='num_array', required=False),
        NodeArgMeta(name='GRExg', kind='number', required=False),
        NodeArgMeta(name='tolCond', kind='number', required=False),
        NodeArgMeta(name='maxIteration', kind='integer', required=False),
        NodeArgMeta(name='numberOfPeriods', kind='integer', required=False),
        NodeArgMeta(name='priceAdjustmentMethod', kind='enum', required=False, enum=('variable', 'fixed', )),
        NodeArgMeta(name='priceAdjustmentVelocity', kind='number', required=False),
        NodeArgMeta(name='ts', kind='boolean', required=False),
        ),
        defaults={'tolCond': 1e-05, 'maxIteration': 200, 'numberOfPeriods': 300, 'priceAdjustmentVelocity': 0.15, 'ts': False},
    ),
    'dsge_estimate': NodeMeta(
        fn='dsge_estimate',
        category='13-dsge-general-equilibrium',
        card_id=200,
        contract_hash='c-8e1604584b1a5717b9366e3d4e902169249bbe4be8ab93bfd604fc6499432cdc',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='obs_eqs', kind='series_codes', required=True),
        NodeArgMeta(name='state_eqs', kind='series_codes', required=True),
        NodeArgMeta(name='unobs_eqs', kind='series_codes', required=False),
        NodeArgMeta(name='fixed', kind='raw', required=False),
        NodeArgMeta(name='start', kind='raw', required=False),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('BFGS', 'Nelder-Mead', 'CG', 'L-BFGS-B', )),
        NodeArgMeta(name='demean', kind='boolean', required=False),
        NodeArgMeta(name='maxit', kind='integer', required=False),
        ),
        defaults={'demean': True, 'maxit': 500},
    ),
    'dsge_forecast': NodeMeta(
        fn='dsge_forecast',
        category='13-dsge-general-equilibrium',
        card_id=200,
        contract_hash='c-70f05f28d51d06a3d691f30054c277c1a67b49268fea213775be5c5e9c3350d9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        ),
        defaults={'horizon': 12},
    ),
    'dsge_irf': NodeMeta(
        fn='dsge_irf',
        category='13-dsge-general-equilibrium',
        card_id=200,
        contract_hash='c-78abd0e038397395b869ce355c77e634b943e9e5b3d366a628bfaea20997e26d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='periods', kind='integer', required=False),
        NodeArgMeta(name='impulse', kind='series_codes', required=False),
        NodeArgMeta(name='response', kind='series_codes', required=False),
        NodeArgMeta(name='se', kind='boolean', required=False),
        NodeArgMeta(name='level', kind='number', required=False),
        ),
        defaults={'periods': 20, 'se': True, 'level': 0.95},
    ),
    'dsge_shock_decomposition': NodeMeta(
        fn='dsge_shock_decomposition',
        category='13-dsge-general-equilibrium',
        card_id=200,
        contract_hash='c-00ac71dfb204434a4602444d8c1773b0b3cb3b81e4068f19440bd6077611377d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'dsge_solve': NodeMeta(
        fn='dsge_solve',
        category='13-dsge-general-equilibrium',
        card_id=200,
        contract_hash='c-e42b2bb32b44de571c73944b9c1c58a49619f92d4636b7e4f2c435d21d5cac72',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='obs_eqs', kind='series_codes', required=True),
        NodeArgMeta(name='state_eqs', kind='series_codes', required=True),
        NodeArgMeta(name='unobs_eqs', kind='series_codes', required=False),
        NodeArgMeta(name='fixed', kind='raw', required=False),
        NodeArgMeta(name='params', kind='raw', required=True),
        NodeArgMeta(name='shock_sd', kind='raw', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        ),
        defaults={'tol': 1e-06},
    ),
    'sfcr_balance_check': NodeMeta(
        fn='sfcr_balance_check',
        category='13-dsge-general-equilibrium',
        card_id=203,
        contract_hash='c-3b79b018dee5bb995be57d8a26dd3b9bb13d9f0bdf0d0d9477b712f3223e750c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='baseline', kind='raw_handle', required=True),
        NodeArgMeta(name='matrix_type', kind='enum', required=False, enum=('tfm', 'bs', )),
        NodeArgMeta(name='columns', kind='series_codes', required=True),
        NodeArgMeta(name='codes', kind='series_codes', required=True),
        NodeArgMeta(name='rows', kind='raw', required=True),
        NodeArgMeta(name='tol', kind='number', required=False),
        NodeArgMeta(name='rtol', kind='boolean', required=False),
        ),
        defaults={'tol': 1, 'rtol': False},
    ),
    'sfcr_scenario_run': NodeMeta(
        fn='sfcr_scenario_run',
        category='13-dsge-general-equilibrium',
        card_id=203,
        contract_hash='c-12049eeedfe065f9ab3e03113473215d260886a13d65771895306b63b0d684f0',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='baseline', kind='raw_handle', required=True),
        NodeArgMeta(name='shock_variables', kind='series_codes', required=True),
        NodeArgMeta(name='shock_start', kind='integer', required=True),
        NodeArgMeta(name='shock_end', kind='integer', required=True),
        NodeArgMeta(name='periods', kind='integer', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('Broyden', 'Gauss', 'Newton', )),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        ),
        defaults={'max_iter': 350, 'tol': 1e-10},
    ),
    'sfcr_simulate': NodeMeta(
        fn='sfcr_simulate',
        category='13-dsge-general-equilibrium',
        card_id=203,
        contract_hash='c-0e8580f870dec4640334c384147da88d9f95b47a7a3e7dc7296c03d811651bda',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='equations', kind='series_codes', required=True),
        NodeArgMeta(name='external', kind='series_codes', required=True),
        NodeArgMeta(name='periods', kind='integer', required=True),
        NodeArgMeta(name='initial', kind='series_codes', required=False),
        NodeArgMeta(name='hidden', kind='raw', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('Broyden', 'Gauss', 'Newton', )),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        NodeArgMeta(name='tol', kind='number', required=False),
        NodeArgMeta(name='rhtol', kind='boolean', required=False),
        NodeArgMeta(name='hidden_tol', kind='number', required=False),
        ),
        defaults={'max_iter': 350, 'tol': 1e-08, 'rhtol': False, 'hidden_tol': 0.1},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'bimets_estimate': {},
    'bimets_multipliers': {'mm_shock': 1e-05},
    'bimets_simulate': {'stochastic': False, 'stoch_replica': 100, 'seed': 2025, 'simConvergence': 1e-05, 'simIterLimit': 100},
    'cge_solve': {'tolCond': 1e-05, 'maxIteration': 200, 'numberOfPeriods': 300, 'priceAdjustmentVelocity': 0.15, 'ts': False},
    'dsge_estimate': {'demean': True, 'maxit': 500},
    'dsge_forecast': {'horizon': 12},
    'dsge_irf': {'periods': 20, 'se': True, 'level': 0.95},
    'dsge_shock_decomposition': {},
    'dsge_solve': {'tol': 1e-06},
    'sfcr_balance_check': {'tol': 1, 'rtol': False},
    'sfcr_scenario_run': {'max_iter': 350, 'tol': 1e-10},
    'sfcr_simulate': {'max_iter': 350, 'tol': 1e-08, 'rhtol': False, 'hidden_tol': 0.1},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
