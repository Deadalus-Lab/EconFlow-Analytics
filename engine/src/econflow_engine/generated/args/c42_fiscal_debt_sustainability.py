# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 42-fiscal-debt-sustainability -- 15 nodes. No descriptions."""

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
    'fis_debt_decomposition': NodeMeta(
        fn='fis_debt_decomposition',
        category='42-fiscal-debt-sustainability',
        card_id=354,
        contract_hash='c2-419cd3ec072ec1c8acccf58c11f53935dcef5e5eb592cfeed21fc6bf5824aeea',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio', kind='series_handle', required=True),
        NodeArgMeta(name='primary_balance', kind='series_handle', required=True),
        NodeArgMeta(name='interest_rate', kind='series_handle', required=True),
        NodeArgMeta(name='growth_rate', kind='series_handle', required=True),
        NodeArgMeta(name='inflation', kind='series_handle', required=False),
        ),
        defaults={},
    ),
    'fis_snowball': NodeMeta(
        fn='fis_snowball',
        category='42-fiscal-debt-sustainability',
        card_id=354,
        contract_hash='c2-ad7396c2dd36dc78d7f27b564ff7fc924c4a3e152dcccf1be48adac99659dc33',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio', kind='series_handle', required=True),
        NodeArgMeta(name='interest_rate', kind='series_handle', required=True),
        NodeArgMeta(name='growth_rate', kind='series_handle', required=True),
        ),
        defaults={},
    ),
    'fis_project_debt': NodeMeta(
        fn='fis_project_debt',
        category='42-fiscal-debt-sustainability',
        card_id=355,
        contract_hash='c2-cdb357e0371276bfc22a1e9d31ec41d53b946190c91fe313a20ee0c37bb43df4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio_initial', kind='number', required=True),
        NodeArgMeta(name='primary_balance', kind='num_array', required=True),
        NodeArgMeta(name='interest_rate', kind='num_array', required=True),
        NodeArgMeta(name='growth_rate', kind='num_array', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        ),
        defaults={'horizon': 10},
    ),
    'fis_stress_scenarios': NodeMeta(
        fn='fis_stress_scenarios',
        category='42-fiscal-debt-sustainability',
        card_id=355,
        contract_hash='c2-e663fcf4d5c8dac0810ea2fcd47c8d135e8bec0118b246175dc1ea084e8acd8e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='baseline', kind='raw_handle', required=True),
        NodeArgMeta(name='shock_size', kind='number', required=False),
        NodeArgMeta(name='scenarios', kind='series_codes', required=False),
        ),
        defaults={'shock_size': 1.0},
    ),
    'fis_debt_stabilising_balance': NodeMeta(
        fn='fis_debt_stabilising_balance',
        category='42-fiscal-debt-sustainability',
        card_id=355,
        contract_hash='c2-0d1e6e0449e588d9b66d1652135f47b565ec8598b15fca4857c3445a31cf75f4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio', kind='number', required=True),
        NodeArgMeta(name='interest_rate', kind='number', required=True),
        NodeArgMeta(name='growth_rate', kind='number', required=True),
        ),
        defaults={},
    ),
    'fis_debt_fan_chart': NodeMeta(
        fn='fis_debt_fan_chart',
        category='42-fiscal-debt-sustainability',
        card_id=356,
        contract_hash='c2-b74869792533c9f76d8545091d1554052c5cdf93093a9e6d7b101df38dc4c66a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio_initial', kind='number', required=True),
        NodeArgMeta(name='history', kind='df_handle', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='n_simulations', kind='integer', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bootstrap', 'block_bootstrap', 'normal', 'var', )),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'horizon': 10, 'n_simulations': 10000, 'method': 'bootstrap', 'quantiles': [0.1, 0.25, 0.5, 0.75, 0.9]},
    ),
    'fis_threshold_probability': NodeMeta(
        fn='fis_threshold_probability',
        category='42-fiscal-debt-sustainability',
        card_id=356,
        contract_hash='c2-5ebbf07b795799f8916e37a2aee6085de39690787dcf7f9a6a80dc6119567b6c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fan', kind='raw_handle', required=True),
        NodeArgMeta(name='threshold', kind='number', required=True),
        ),
        defaults={},
    ),
    'fis_reaction_function': NodeMeta(
        fn='fis_reaction_function',
        category='42-fiscal-debt-sustainability',
        card_id=357,
        contract_hash='c2-3c3b99461d772282ca65763924580abe4d9e0a965684e8752605fe52190aeb5c',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='primary_balance', kind='series_handle', required=True),
        NodeArgMeta(name='debt_ratio', kind='series_handle', required=True),
        NodeArgMeta(name='output_gap', kind='series_handle', required=False),
        NodeArgMeta(name='controls', kind='series_codes', required=False),
        NodeArgMeta(name='cov_type', kind='enum', required=False, enum=('nonrobust', 'robust', 'hac', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'cov_type': 'hac', 'conf_level': 0.95},
    ),
    'fis_reaction_nonlinear': NodeMeta(
        fn='fis_reaction_nonlinear',
        category='42-fiscal-debt-sustainability',
        card_id=357,
        contract_hash='c2-8a7add023c62d624fd3c179c7e97af494c4fc3e93141d8f67e2270a844e1b826',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='primary_balance', kind='series_handle', required=True),
        NodeArgMeta(name='debt_ratio', kind='series_handle', required=True),
        NodeArgMeta(name='output_gap', kind='series_handle', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('threshold', 'markov_switching', 'quadratic', 'spline', )),
        NodeArgMeta(name='n_regimes', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'model': 'threshold', 'n_regimes': 2},
    ),
    'fis_multiplier_lp': NodeMeta(
        fn='fis_multiplier_lp',
        category='42-fiscal-debt-sustainability',
        card_id=358,
        contract_hash='c2-c0fd4276b977d1682470a3f582615ee593fcddb362082af609510bc41eb9c70c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='output', kind='series_handle', required=True),
        NodeArgMeta(name='fiscal', kind='series_handle', required=True),
        NodeArgMeta(name='controls', kind='series_codes', required=False),
        NodeArgMeta(name='horizons', kind='integer', required=False),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='cumulative', kind='boolean', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'horizons': 20, 'lags': 4, 'cumulative': True, 'conf_level': 0.95},
    ),
    'fis_multiplier_state_dependent': NodeMeta(
        fn='fis_multiplier_state_dependent',
        category='42-fiscal-debt-sustainability',
        card_id=358,
        contract_hash='c2-faf7485da18a72c5d041284f667e07524e6a5c8b4ae71b1f196ec8dbb8014a9a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='output', kind='series_handle', required=True),
        NodeArgMeta(name='fiscal', kind='series_handle', required=True),
        NodeArgMeta(name='state', kind='series_handle', required=True),
        NodeArgMeta(name='transition', kind='enum', required=False, enum=('smooth', 'indicator', )),
        NodeArgMeta(name='horizons', kind='integer', required=False),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'transition': 'smooth', 'horizons': 20, 'lags': 4, 'conf_level': 0.95},
    ),
    'fis_cyclically_adjusted': NodeMeta(
        fn='fis_cyclically_adjusted',
        category='42-fiscal-debt-sustainability',
        card_id=359,
        contract_hash='c2-07126d25839da9349add07557cf9131b9b7c1b60aa4c7b054519bef81644f012',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='balance', kind='series_handle', required=True),
        NodeArgMeta(name='output_gap', kind='series_handle', required=True),
        NodeArgMeta(name='elasticity', kind='number', required=False),
        NodeArgMeta(name='one_offs', kind='series_handle', required=False),
        ),
        defaults={'elasticity': 0.5},
    ),
    'fis_budget_elasticity': NodeMeta(
        fn='fis_budget_elasticity',
        category='42-fiscal-debt-sustainability',
        card_id=359,
        contract_hash='c2-f95ed10fba40d4460f2a60d1fa139d645ad9d7c1fe9ad0f995c4b96886ac31dc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='revenue', kind='series_handle', required=True),
        NodeArgMeta(name='expenditure', kind='series_handle', required=True),
        NodeArgMeta(name='output_gap', kind='series_handle', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'conf_level': 0.95},
    ),
    'fis_rule_compliance': NodeMeta(
        fn='fis_rule_compliance',
        category='42-fiscal-debt-sustainability',
        card_id=360,
        contract_hash='c2-386e390c7bb4769681ed6e351d0d12da90c2c6a79fe35ea1a9939755022f7fa3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio', kind='series_handle', required=True),
        NodeArgMeta(name='structural_balance', kind='series_handle', required=False),
        NodeArgMeta(name='expenditure_growth', kind='series_handle', required=False),
        NodeArgMeta(name='debt_limit', kind='number', required=False),
        NodeArgMeta(name='deficit_limit', kind='number', required=False),
        NodeArgMeta(name='mto', kind='number', required=False),
        ),
        defaults={'debt_limit': 0.6, 'deficit_limit': 0.03},
    ),
    'fis_adjustment_path': NodeMeta(
        fn='fis_adjustment_path',
        category='42-fiscal-debt-sustainability',
        card_id=360,
        contract_hash='c2-d4887cac65124c1653cbbfcdbd1acc25aa6b32d920b5e891826667af55a1309e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='debt_ratio_initial', kind='number', required=True),
        NodeArgMeta(name='target', kind='number', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='interest_rate', kind='number', required=True),
        NodeArgMeta(name='growth_rate', kind='number', required=True),
        NodeArgMeta(name='multiplier', kind='number', required=False),
        ),
        defaults={'horizon': 10, 'multiplier': 0.0},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'fis_debt_decomposition': {},
    'fis_snowball': {},
    'fis_project_debt': {'horizon': 10},
    'fis_stress_scenarios': {'shock_size': 1.0},
    'fis_debt_stabilising_balance': {},
    'fis_debt_fan_chart': {'horizon': 10, 'n_simulations': 10000, 'method': 'bootstrap', 'quantiles': [0.1, 0.25, 0.5, 0.75, 0.9]},
    'fis_threshold_probability': {},
    'fis_reaction_function': {'cov_type': 'hac', 'conf_level': 0.95},
    'fis_reaction_nonlinear': {'model': 'threshold', 'n_regimes': 2},
    'fis_multiplier_lp': {'horizons': 20, 'lags': 4, 'cumulative': True, 'conf_level': 0.95},
    'fis_multiplier_state_dependent': {'transition': 'smooth', 'horizons': 20, 'lags': 4, 'conf_level': 0.95},
    'fis_cyclically_adjusted': {'elasticity': 0.5},
    'fis_budget_elasticity': {'conf_level': 0.95},
    'fis_rule_compliance': {'debt_limit': 0.6, 'deficit_limit': 0.03},
    'fis_adjustment_path': {'horizon': 10, 'multiplier': 0.0},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
