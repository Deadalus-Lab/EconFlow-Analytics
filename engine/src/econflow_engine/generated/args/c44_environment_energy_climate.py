# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 44-environment-energy-climate -- 14 nodes. No descriptions."""

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
    'env_footprint': NodeMeta(
        fn='env_footprint',
        category='44-environment-energy-climate',
        card_id=367,
        contract_hash='c2-5929de2d852be083b9b00e84634e6298d545be7e1d4bad550fe9f26cf4b09aa6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='io_table', kind='raw_handle', required=True),
        NodeArgMeta(name='extension', kind='string', required=True),
        NodeArgMeta(name='final_demand', kind='series_codes', required=False),
        ),
        defaults={},
    ),
    'env_multipliers': NodeMeta(
        fn='env_multipliers',
        category='44-environment-energy-climate',
        card_id=367,
        contract_hash='c2-c1d6b7563b9f3fe7088d17e4b87c108f5efbe0e62b83bd1356dab1e11bf33596',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='io_table', kind='raw_handle', required=True),
        NodeArgMeta(name='extension', kind='string', required=True),
        ),
        defaults={},
    ),
    'env_embodied_trade': NodeMeta(
        fn='env_embodied_trade',
        category='44-environment-energy-climate',
        card_id=367,
        contract_hash='c2-b523b43954f29a20129cfb7a8b95fa098b04f275c5e5e1688e12a7fdf8a2f5c4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='io_table', kind='raw_handle', required=True),
        NodeArgMeta(name='extension', kind='string', required=True),
        NodeArgMeta(name='region', kind='string', required=False),
        ),
        defaults={},
    ),
    'env_decompose_index': NodeMeta(
        fn='env_decompose_index',
        category='44-environment-energy-climate',
        card_id=368,
        contract_hash='c2-28aaa0f5ee4c2bd985e3528a13b81f6197d161f59c343f7c5f2437af25dc84c7',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='total', kind='string', required=True),
        NodeArgMeta(name='factors', kind='series_codes', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('lmdi_i', 'lmdi_ii', 'laspeyres', 'paasche', 'fisher', )),
        NodeArgMeta(name='form', kind='enum', required=False, enum=('additive', 'multiplicative', )),
        ),
        defaults={'method': 'lmdi_i', 'form': 'additive'},
    ),
    'env_scenario_filter': NodeMeta(
        fn='env_scenario_filter',
        category='44-environment-energy-climate',
        card_id=369,
        contract_hash='c2-b959f63c0d8913ee9b35d8d9aed98ccab13d476d34413050642288c2a81a319c',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='model', kind='series_codes', required=False),
        NodeArgMeta(name='scenario', kind='series_codes', required=False),
        NodeArgMeta(name='variable', kind='series_codes', required=False),
        NodeArgMeta(name='region', kind='series_codes', required=False),
        NodeArgMeta(name='year', kind='int_array', required=False),
        ),
        defaults={},
    ),
    'env_scenario_harmonise': NodeMeta(
        fn='env_scenario_harmonise',
        category='44-environment-energy-climate',
        card_id=369,
        contract_hash='c2-75a7ff747497f899cd4cc69258bc5be7958eceb210320a5ba9f50846674ffd5e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='history', kind='df_handle', required=True),
        NodeArgMeta(name='base_year', kind='integer', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('ratio', 'offset', 'reduce_ratio', 'reduce_offset', )),
        NodeArgMeta(name='convergence_year', kind='integer', required=False),
        ),
        defaults={'method': 'ratio', 'convergence_year': 2050},
    ),
    'env_scenario_aggregate': NodeMeta(
        fn='env_scenario_aggregate',
        category='44-environment-energy-climate',
        card_id=369,
        contract_hash='c2-f378f16dd92fdd572b6c86b4749a75351c12157a8bc6176444a1e7b8cd725030',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='mapping', kind='df_handle', required=True),
        NodeArgMeta(name='dimension', kind='enum', required=False, enum=('region', 'variable', )),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('sum', 'mean', 'weighted', )),
        ),
        defaults={'dimension': 'region', 'method': 'sum'},
    ),
    'env_ekc': NodeMeta(
        fn='env_ekc',
        category='44-environment-energy-climate',
        card_id=370,
        contract_hash='c2-1231ccb7476ce3a838d2ab4de506f7a45c989d3cfffa54e5b9fff8134a583260',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='emissions', kind='string', required=True),
        NodeArgMeta(name='income', kind='string', required=True),
        NodeArgMeta(name='controls', kind='series_codes', required=False),
        NodeArgMeta(name='unit', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='form', kind='enum', required=False, enum=('linear', 'quadratic', 'cubic', 'semiparametric', )),
        NodeArgMeta(name='cluster', kind='string', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'form': 'quadratic', 'conf_level': 0.95},
    ),
    'env_degree_days': NodeMeta(
        fn='env_degree_days',
        category='44-environment-energy-climate',
        card_id=371,
        contract_hash='c2-e9df21c9d506862cc7ad75fa50235e0289ab6cf3c442565cb457d4e2c7c5b148',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='temperature', kind='series_handle', required=True),
        NodeArgMeta(name='base_heating', kind='number', required=False),
        NodeArgMeta(name='base_cooling', kind='number', required=False),
        NodeArgMeta(name='frequency', kind='enum', required=False, enum=('daily', 'weekly', 'monthly', 'annual', )),
        ),
        defaults={'base_heating': 15.5, 'base_cooling': 22.0, 'frequency': 'monthly'},
    ),
    'env_weather_normalise': NodeMeta(
        fn='env_weather_normalise',
        category='44-environment-energy-climate',
        card_id=371,
        contract_hash='c2-f5b0750876a96245fd6832cb022754d85a89d7aaa53fcd9845783c845d85aa1a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='demand', kind='series_handle', required=True),
        NodeArgMeta(name='hdd', kind='series_handle', required=True),
        NodeArgMeta(name='cdd', kind='series_handle', required=True),
        NodeArgMeta(name='controls', kind='series_codes', required=False),
        NodeArgMeta(name='estimate_base', kind='boolean', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'estimate_base': False, 'conf_level': 0.95},
    ),
    'env_climate_macro_map': NodeMeta(
        fn='env_climate_macro_map',
        category='44-environment-energy-climate',
        card_id=372,
        contract_hash='c2-db2d552f0e9728d8c693b6ab9fb6799499fbbb11f718ae3096167d799022b70b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='scenario', kind='df_handle', required=True),
        NodeArgMeta(name='elasticities', kind='df_handle', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='component', kind='enum', required=False, enum=('transition', 'physical', 'both', )),
        ),
        defaults={'horizon': 30, 'component': 'both'},
    ),
    'env_damage_function': NodeMeta(
        fn='env_damage_function',
        category='44-environment-energy-climate',
        card_id=372,
        contract_hash='c2-79c457f848b4817b34497765294d47ae7f915943727ec0edceccc0a2539c1476',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='temperature', kind='series_handle', required=True),
        NodeArgMeta(name='function', kind='enum', required=False, enum=('nordhaus', 'weitzman', 'howard_sterner', 'burke', 'linear', )),
        NodeArgMeta(name='parameters', kind='num_array', required=False),
        ),
        defaults={'function': 'nordhaus'},
    ),
    'env_kaya': NodeMeta(
        fn='env_kaya',
        category='44-environment-energy-climate',
        card_id=373,
        contract_hash='c2-a14f5f6225d3436cc3db5e5da0d4dd21a5d1d834d82459b5f120aa57e6345fca',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='emissions', kind='series_handle', required=True),
        NodeArgMeta(name='population', kind='series_handle', required=True),
        NodeArgMeta(name='output', kind='series_handle', required=True),
        NodeArgMeta(name='energy', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('lmdi', 'laspeyres', 'simple', )),
        ),
        defaults={'method': 'lmdi'},
    ),
    'env_energy_balance': NodeMeta(
        fn='env_energy_balance',
        category='44-environment-energy-climate',
        card_id=373,
        contract_hash='c2-2a633099a2412d5521ecf8a5d200616d02544ff9b14a224a3c63bf586096de79',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='carrier', kind='string', required=True),
        NodeArgMeta(name='stage', kind='string', required=True),
        NodeArgMeta(name='value', kind='string', required=True),
        ),
        defaults={},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'env_footprint': {},
    'env_multipliers': {},
    'env_embodied_trade': {},
    'env_decompose_index': {'method': 'lmdi_i', 'form': 'additive'},
    'env_scenario_filter': {},
    'env_scenario_harmonise': {'method': 'ratio', 'convergence_year': 2050},
    'env_scenario_aggregate': {'dimension': 'region', 'method': 'sum'},
    'env_ekc': {'form': 'quadratic', 'conf_level': 0.95},
    'env_degree_days': {'base_heating': 15.5, 'base_cooling': 22.0, 'frequency': 'monthly'},
    'env_weather_normalise': {'estimate_base': False, 'conf_level': 0.95},
    'env_climate_macro_map': {'horizon': 30, 'component': 'both'},
    'env_damage_function': {'function': 'nordhaus'},
    'env_kaya': {'method': 'lmdi'},
    'env_energy_balance': {},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
