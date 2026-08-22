# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 11-decomposition-accounting -- 14 nodes. No descriptions."""

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
    'ox_decompose': NodeMeta(
        fn='ox_decompose',
        category='11-decomposition-accounting',
        card_id=63,
        contract_hash='c2-6dba74da6cb832b7f95d16bc4b7bbfb0d27411f58eb6bd8cf6b7cbfae277db91',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='formula', kind='formula', required=True),
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='n_bootstrap', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'n_bootstrap': 100, 'seed': 42},
    ),
    'pi_bilateral': NodeMeta(
        fn='pi_bilateral',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c2-b77c0bf0f6548cebea5ca2593b9083195244c86b6c597982a6e2b1ac98b3b47b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='formula', kind='enum', required=False, enum=('jevons', 'dutot', 'carli', 'laspeyres', 'paasche', 'fisher', 'tornqvist', 'walsh', )),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        ),
        defaults={'interval': False},
    ),
    'pi_contributions': NodeMeta(
        fn='pi_contributions',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c2-9033b18f2d79b70d49944258f4b9a6848033dbca7c966944e216b365ce578429',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bennet', 'montgomery', )),
        NodeArgMeta(name='matched', kind='boolean', required=False),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        NodeArgMeta(name='prec', kind='integer', required=False),
        ),
        defaults={'matched': False, 'interval': False, 'prec': 2},
    ),
    'pi_multilateral': NodeMeta(
        fn='pi_multilateral',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c2-727c98de35400433fea609b2508084bfc375d44a85f0e16586e00d1d782e94d2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('geks', 'ccdi', 'gk', 'tpd', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='wstart', kind='string', required=False),
        ),
        defaults={'window': 13},
    ),
    'pi_splice': NodeMeta(
        fn='pi_splice',
        category='11-decomposition-accounting',
        card_id=190,
        contract_hash='c2-444431122899ddfda74275e07e4213ae627901e12836b0b6b1c031b1540dacb4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='start', kind='string', required=True),
        NodeArgMeta(name='end', kind='string', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('geks', 'ccdi', 'gk', 'tpd', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='splice', kind='enum', required=False, enum=('movement', 'window', 'half', 'mean', 'window_published', 'half_published', 'mean_published', )),
        NodeArgMeta(name='interval', kind='boolean', required=False),
        ),
        defaults={'window': 13, 'interval': False},
    ),
    'prod_fare_primont': NodeMeta(
        fn='prod_fare_primont',
        category='11-decomposition-accounting',
        card_id=62,
        contract_hash='c2-464621c15af0ed72e81d2faa4f34fc55e7db0f4a8ef11a8051689def9df507ef',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id_var', kind='string', required=True),
        NodeArgMeta(name='time_var', kind='string', required=True),
        NodeArgMeta(name='x_vars', kind='series_codes', required=True),
        NodeArgMeta(name='y_vars', kind='series_codes', required=True),
        NodeArgMeta(name='w_vars', kind='series_codes', required=False),
        NodeArgMeta(name='p_vars', kind='series_codes', required=False),
        NodeArgMeta(name='tech_change', kind='boolean', required=False),
        NodeArgMeta(name='tech_reg', kind='boolean', required=False),
        NodeArgMeta(name='rts', kind='enum', required=False, enum=('vrs', 'crs', 'nirs', 'ndrs', )),
        NodeArgMeta(name='orientation', kind='enum', required=False, enum=('out', 'in', 'in-out', )),
        NodeArgMeta(name='scaled', kind='boolean', required=False),
        NodeArgMeta(name='shadow', kind='boolean', required=False),
        ),
        defaults={'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    ),
    'prod_malmquist': NodeMeta(
        fn='prod_malmquist',
        category='11-decomposition-accounting',
        card_id=62,
        contract_hash='c2-b6e390e44b452fd09d6ab092b8c9b26d69f995483d85655e16ab8800cb3c0eb0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='id_var', kind='string', required=True),
        NodeArgMeta(name='time_var', kind='string', required=True),
        NodeArgMeta(name='x_vars', kind='series_codes', required=True),
        NodeArgMeta(name='y_vars', kind='series_codes', required=True),
        NodeArgMeta(name='rts', kind='enum', required=False, enum=('vrs', 'crs', 'nirs', 'ndrs', )),
        NodeArgMeta(name='orientation', kind='enum', required=False, enum=('out', 'in', )),
        NodeArgMeta(name='tech_reg', kind='boolean', required=False),
        NodeArgMeta(name='scaled', kind='boolean', required=False),
        ),
        defaults={'tech_reg': True, 'scaled': True},
    ),
    'da_growth_accounting': NodeMeta(
        fn='da_growth_accounting',
        category='11-decomposition-accounting',
        card_id=484,
        contract_hash='c2-d30e0690b5fec0786b6e1bf3f9511b4f644c941956712f87a5fdb4a57085dd9a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='output', kind='series_handle', required=True),
        NodeArgMeta(name='inputs', kind='multiseries_handle', required=True),
        NodeArgMeta(name='shares', kind='multiseries_handle', required=False),
        NodeArgMeta(name='index', kind='enum', required=False, enum=('tornqvist', 'divisia', 'laspeyres', 'fixed_share', )),
        ),
        defaults={'index': 'tornqvist'},
    ),
    'da_stochastic_frontier': NodeMeta(
        fn='da_stochastic_frontier',
        category='11-decomposition-accounting',
        card_id=485,
        contract_hash='c2-160f2ec657f7813020e392609b8d72d2e2734acbe9866506177e9028d9472fe8',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='x', kind='df_handle', required=True),
        NodeArgMeta(name='frontier', kind='enum', required=False, enum=('production', 'cost', )),
        NodeArgMeta(name='distribution', kind='enum', required=False, enum=('half_normal', 'truncated_normal', 'exponential', 'gamma', )),
        NodeArgMeta(name='inefficiency_covariates', kind='series_codes', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'frontier': 'production', 'distribution': 'half_normal', 'conf_level': 0.95},
    ),
    'da_dea': NodeMeta(
        fn='da_dea',
        category='11-decomposition-accounting',
        card_id=486,
        contract_hash='c2-b8a0b203cabefb595bfa4b9f6dbe21de2f6810f68e9360ab86e82e18e08c31c6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='inputs', kind='df_handle', required=True),
        NodeArgMeta(name='outputs', kind='df_handle', required=True),
        NodeArgMeta(name='returns', kind='enum', required=False, enum=('crs', 'vrs', 'nirs', 'ndrs', )),
        NodeArgMeta(name='orientation', kind='enum', required=False, enum=('input', 'output', )),
        NodeArgMeta(name='decompose', kind='boolean', required=False),
        ),
        defaults={'returns': 'vrs', 'orientation': 'input', 'decompose': True},
    ),
    'da_multilateral_index': NodeMeta(
        fn='da_multilateral_index',
        category='11-decomposition-accounting',
        card_id=487,
        contract_hash='c2-6f5e3c5fd3e628c13d576b230051ddc9beb9ebf4d137c6850db9af89f0182e52',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='product', kind='string', required=True),
        NodeArgMeta(name='period', kind='string', required=True),
        NodeArgMeta(name='price', kind='string', required=True),
        NodeArgMeta(name='quantity', kind='string', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('geks', 'tpd', 'gk', 'tornqvist', 'jevons', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='splice', kind='enum', required=False, enum=('movement', 'window', 'half', 'mean', )),
        ),
        defaults={'method': 'geks', 'window': 13, 'splice': 'movement'},
    ),
    'da_shift_share': NodeMeta(
        fn='da_shift_share',
        category='11-decomposition-accounting',
        card_id=488,
        contract_hash='c2-4a3eb8ffb1f05950b957a0d55273c21250369da604867d78fee94973cf638859',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='region', kind='string', required=True),
        NodeArgMeta(name='industry', kind='string', required=True),
        NodeArgMeta(name='value', kind='string', required=True),
        NodeArgMeta(name='time', kind='string', required=True),
        NodeArgMeta(name='dynamic', kind='boolean', required=False),
        ),
        defaults={'dynamic': False},
    ),
    'da_reweighting_decomposition': NodeMeta(
        fn='da_reweighting_decomposition',
        category='11-decomposition-accounting',
        card_id=489,
        contract_hash='c2-6dc058f126cb8898114508fed170c432f9a0a9647ea876706a7f9f1a4e8e0a91',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='outcome', kind='string', required=True),
        NodeArgMeta(name='group', kind='string', required=True),
        NodeArgMeta(name='covariates', kind='series_codes', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('dfl', 'rif', 'oaxaca_blinder', )),
        NodeArgMeta(name='quantiles', kind='num_array', required=False),
        NodeArgMeta(name='nboot', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'dfl', 'quantiles': [0.1, 0.5, 0.9], 'nboot': 999, 'conf_level': 0.95},
    ),
    'da_structural_decomposition': NodeMeta(
        fn='da_structural_decomposition',
        category='11-decomposition-accounting',
        card_id=490,
        contract_hash='c2-7f7f10f68066ab474077c924e566e998118bc05a8aabceef84ad0ccbf03b7a74',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='table_start', kind='raw_handle', required=True),
        NodeArgMeta(name='table_end', kind='raw_handle', required=True),
        NodeArgMeta(name='extension', kind='string', required=False),
        NodeArgMeta(name='form', kind='enum', required=False, enum=('average_polar', 'first_polar', 'second_polar', 'all_forms', )),
        ),
        defaults={'form': 'average_polar'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'ox_decompose': {'n_bootstrap': 100, 'seed': 42},
    'pi_bilateral': {'interval': False},
    'pi_contributions': {'matched': False, 'interval': False, 'prec': 2},
    'pi_multilateral': {'window': 13},
    'pi_splice': {'window': 13, 'interval': False},
    'prod_fare_primont': {'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    'prod_malmquist': {'tech_reg': True, 'scaled': True},
    'da_growth_accounting': {'index': 'tornqvist'},
    'da_stochastic_frontier': {'frontier': 'production', 'distribution': 'half_normal', 'conf_level': 0.95},
    'da_dea': {'returns': 'vrs', 'orientation': 'input', 'decompose': True},
    'da_multilateral_index': {'method': 'geks', 'window': 13, 'splice': 'movement'},
    'da_shift_share': {'dynamic': False},
    'da_reweighting_decomposition': {'method': 'dfl', 'quantiles': [0.1, 0.5, 0.9], 'nboot': 999, 'conf_level': 0.95},
    'da_structural_decomposition': {'form': 'average_polar'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
