# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 43-microsimulation-taxbenefit -- 10 nodes. No descriptions."""

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
    'tb_compute': NodeMeta(
        fn='tb_compute',
        category='43-microsimulation-taxbenefit',
        card_id=361,
        contract_hash='c2-b150e5a6de3cc7d4c20ca76597f37a1872893867e78afcb8cc8e7ee824b37c0f',
        register_field='simulation',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='population', kind='df_handle', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='country', kind='enum', required=False, enum=('generic', 'uk', 'fr', 'us', 'eu', )),
        ),
        defaults={'country': 'generic'},
    ),
    'tb_reform': NodeMeta(
        fn='tb_reform',
        category='43-microsimulation-taxbenefit',
        card_id=361,
        contract_hash='c2-b682e5715faf95508841a3ff77fe80c10db1f3ff69bf72974fe941be84a8b4cf',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='simulation', kind='raw_handle', required=True),
        NodeArgMeta(name='reform', kind='df_handle', required=True),
        NodeArgMeta(name='variables', kind='series_codes', required=True),
        ),
        defaults={},
    ),
    'tb_parameters': NodeMeta(
        fn='tb_parameters',
        category='43-microsimulation-taxbenefit',
        card_id=361,
        contract_hash='c2-6707dadda2682f5562c71f9e10372284cf351a00c4fcd2777e5dc505a6d96b88',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='path', kind='string', required=False),
        ),
        defaults={},
    ),
    'tb_disposable_income': NodeMeta(
        fn='tb_disposable_income',
        category='43-microsimulation-taxbenefit',
        card_id=362,
        contract_hash='c2-f1b70403f0bc2ecc095f5b721ac661e572906961e776be8d81ab15971d0b68c9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='population', kind='df_handle', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='include_housing', kind='boolean', required=False),
        ),
        defaults={'include_housing': False},
    ),
    'tb_budget_constraint': NodeMeta(
        fn='tb_budget_constraint',
        category='43-microsimulation-taxbenefit',
        card_id=362,
        contract_hash='c2-3d1b7a845af7d926873314c442d1f9b0779b3f7281cb4191677f3a60ff51f5c2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='household', kind='df_handle', required=True),
        NodeArgMeta(name='earnings_grid', kind='num_array', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        ),
        defaults={},
    ),
    'tb_metr': NodeMeta(
        fn='tb_metr',
        category='43-microsimulation-taxbenefit',
        card_id=363,
        contract_hash='c2-68559a1bb09596e7378697c9ff9fbc7441ffe7a8afb1ecf4796675592b6c5ecb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='population', kind='df_handle', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='increment', kind='number', required=False),
        ),
        defaults={'increment': 100.0},
    ),
    'tb_participation_tax_rate': NodeMeta(
        fn='tb_participation_tax_rate',
        category='43-microsimulation-taxbenefit',
        card_id=363,
        contract_hash='c2-077dcae5ef89be4f861becc22baa803f1986f39771680fd0ee90d9f6fdd177d2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='population', kind='df_handle', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='transition', kind='enum', required=False, enum=('zero_to_full', 'zero_to_part', 'part_to_full', )),
        ),
        defaults={'transition': 'zero_to_full'},
    ),
    'tb_distributional_impact': NodeMeta(
        fn='tb_distributional_impact',
        category='43-microsimulation-taxbenefit',
        card_id=364,
        contract_hash='c2-ee3711fd1e91dafa24873c75141b71e73dcbbfb220a80ee61677f06b67c4ab3a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='baseline', kind='raw_handle', required=True),
        NodeArgMeta(name='reform', kind='raw_handle', required=True),
        NodeArgMeta(name='weights', kind='series_handle', required=False),
        NodeArgMeta(name='equivalence_scale', kind='enum', required=False, enum=('none', 'oecd', 'oecd_modified', 'square_root', )),
        NodeArgMeta(name='n_groups', kind='integer', required=False),
        ),
        defaults={'equivalence_scale': 'oecd_modified', 'n_groups': 10},
    ),
    'tb_labour_supply': NodeMeta(
        fn='tb_labour_supply',
        category='43-microsimulation-taxbenefit',
        card_id=365,
        contract_hash='c2-b413cf64be741a16c3dfc0fa8fbab583140f6bbba5330bc7952e9fc9f39613e8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='baseline', kind='raw_handle', required=True),
        NodeArgMeta(name='reform', kind='raw_handle', required=True),
        NodeArgMeta(name='intensive_elasticity', kind='number', required=False),
        NodeArgMeta(name='extensive_elasticity', kind='number', required=False),
        NodeArgMeta(name='by_group', kind='series_codes', required=False),
        ),
        defaults={'intensive_elasticity': 0.2, 'extensive_elasticity': 0.3},
    ),
    'tb_reweight': NodeMeta(
        fn='tb_reweight',
        category='43-microsimulation-taxbenefit',
        card_id=366,
        contract_hash='c2-1a92fa9c83004a691f5222124b109dd0310db459c3cf7353decbf90ecf7b9f4e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='weights', kind='string', required=True),
        NodeArgMeta(name='targets', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('post_stratification', 'raking', 'linear', 'logit', )),
        NodeArgMeta(name='bounds', kind='num_array', required=False),
        NodeArgMeta(name='max_iter', kind='integer', required=False),
        ),
        defaults={'method': 'raking', 'bounds': [0.2, 5.0], 'max_iter': 100},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'tb_compute': {'country': 'generic'},
    'tb_reform': {},
    'tb_parameters': {},
    'tb_disposable_income': {'include_housing': False},
    'tb_budget_constraint': {},
    'tb_metr': {'increment': 100.0},
    'tb_participation_tax_rate': {'transition': 'zero_to_full'},
    'tb_distributional_impact': {'equivalence_scale': 'oecd_modified', 'n_groups': 10},
    'tb_labour_supply': {'intensive_elasticity': 0.2, 'extensive_elasticity': 0.3},
    'tb_reweight': {'method': 'raking', 'bounds': [0.2, 5.0], 'max_iter': 100},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
