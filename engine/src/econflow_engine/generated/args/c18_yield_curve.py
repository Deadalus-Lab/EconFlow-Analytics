# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 18-yield-curve -- 11 nodes. No descriptions."""

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
    'atsm_estimate': NodeMeta(
        fn='atsm_estimate',
        category='18-yield-curve',
        card_id=211,
        contract_hash='c2-7cedf61dcca6c1b4d54cb892223351e4cc51246152848b4e474ee3b9973aa78d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='model_type', kind='enum', required=False, enum=('JPS original', 'JPS global', )),
        NodeArgMeta(name='economy', kind='string', required=False),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='global_var', kind='series_codes', required=False),
        NodeArgMeta(name='dom_var', kind='series_codes', required=False),
        NodeArgMeta(name='init_date', kind='string', required=False),
        NodeArgMeta(name='final_date', kind='string', required=False),
        NodeArgMeta(name='data_freq', kind='enum', required=False, enum=('Monthly', 'Quarterly', 'Weekly', 'Annually', 'Daily All Days', 'Daily Business Days', )),
        NodeArgMeta(name='stationary_Q', kind='boolean', required=False),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        NodeArgMeta(name='compute_term_premia', kind='boolean', required=False),
        NodeArgMeta(name='yields', kind='matrix_handle', required=False),
        NodeArgMeta(name='global_macro', kind='matrix_handle', required=False),
        NodeArgMeta(name='dom_macro', kind='matrix_handle', required=False),
        ),
        defaults={'n_factors': 1, 'stationary_Q': False, 'horizon': 25, 'compute_term_premia': True},
    ),
    'fit_nelson_siegel': NodeMeta(
        fn='fit_nelson_siegel',
        category='18-yield-curve',
        card_id=87,
        contract_hash='c2-c19727bbf29a40daf4436aaa098079036fdc22e19bfb6796bfa7441e4f21193f',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='rates', kind='matrix_handle', required=True),
        NodeArgMeta(name='maturities', kind='matrix_handle', required=True),
        ),
        defaults={},
    ),
    'fit_svensson': NodeMeta(
        fn='fit_svensson',
        category='18-yield-curve',
        card_id=87,
        contract_hash='c2-a8efed67bc04d5e6a744680dd71fe7da68cb572730c5e65249eac95e1af9421e',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='rates', kind='matrix_handle', required=True),
        NodeArgMeta(name='maturities', kind='matrix_handle', required=True),
        NodeArgMeta(name='which_rate', kind='enum', required=False, enum=('Spot', 'Forward', )),
        ),
        defaults={},
    ),
    'yc_fit': NodeMeta(
        fn='yc_fit',
        category='18-yield-curve',
        card_id=210,
        contract_hash='c2-04bd164db514a3ffcdce6deb6be6e81460d4149a8964c27997095de5e30c1ce8',
        register_field='object',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='rates', kind='num_array', required=False),
        NodeArgMeta(name='panel', kind='matrix_handle', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('nelson_siegel', 'svensson', 'cubic_spline', )),
        NodeArgMeta(name='type', kind='enum', required=False, enum=('zero', 'par', 'forward', )),
        NodeArgMeta(name='tau_init', kind='number', required=False),
        NodeArgMeta(name='tau1_init', kind='number', required=False),
        NodeArgMeta(name='tau2_init', kind='number', required=False),
        NodeArgMeta(name='weights', kind='num_array', required=False),
        NodeArgMeta(name='dates', kind='series_codes', required=False),
        ),
        defaults={'tau_init': 1, 'tau1_init': 1, 'tau2_init': 5},
    ),
    'yc_transform': NodeMeta(
        fn='yc_transform',
        category='18-yield-curve',
        card_id=210,
        contract_hash='c2-0c4cc360d1b12e261dfd96ba0b1fe3757e5676f6444d67bc3651f245d1145d57',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='object', kind='raw_handle', required=True),
        NodeArgMeta(name='transform', kind='enum', required=False, enum=('spot', 'forward', 'discount', 'pca', )),
        NodeArgMeta(name='grid', kind='num_array', required=False),
        NodeArgMeta(name='horizon', kind='number', required=False),
        NodeArgMeta(name='compounding', kind='enum', required=False, enum=('continuous', 'annual', 'semi_annual', )),
        NodeArgMeta(name='n_components', kind='integer', required=False),
        NodeArgMeta(name='scale', kind='boolean', required=False),
        ),
        defaults={'n_components': 3, 'scale': False},
    ),
    'ycnp_estimate': NodeMeta(
        fn='ycnp_estimate',
        category='18-yield-curve',
        card_id=212,
        contract_hash='c2-7d2db3557af69dcba30cdb7cc8965fdc5d124168e8b35adf0a53f33c71cada54',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='data', kind='df_handle', required=True),
        NodeArgMeta(name='x', kind='series_codes', required=True),
        NodeArgMeta(name='tau', kind='num_array', required=False),
        NodeArgMeta(name='span_x', kind='number', required=False),
        NodeArgMeta(name='hx', kind='num_array', required=False),
        NodeArgMeta(name='ht', kind='num_array', required=False),
        NodeArgMeta(name='smooth', kind='boolean', required=False),
        ),
        defaults={'span_x': 60, 'smooth': False},
    ),
    'yc_acm_decomposition': NodeMeta(
        fn='yc_acm_decomposition',
        category='18-yield-curve',
        card_id=535,
        contract_hash='c2-851455661559949166015d4a205d2af64704d638a2a085fe025248ee0fe7902f',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='yields', kind='df_handle', required=True),
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='real', kind='boolean', required=False),
        ),
        defaults={'n_factors': 5, 'real': False},
    ),
    'yc_bootstrap_curve': NodeMeta(
        fn='yc_bootstrap_curve',
        category='18-yield-curve',
        card_id=536,
        contract_hash='c2-59613bb031f1de92b13041e6c68cb3d09bbc3c465518191f41e7bfce7b45c15b',
        register_field='curve',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='instruments', kind='df_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('bootstrap', 'cubic_spline', 'monotone_convex', 'nelson_siegel', 'svensson', )),
        NodeArgMeta(name='interpolation', kind='enum', required=False, enum=('zero_rate', 'log_discount', 'forward', )),
        NodeArgMeta(name='day_count', kind='enum', required=False, enum=('act360', 'act365', 'thirty360', 'actact', )),
        ),
        defaults={'method': 'bootstrap', 'interpolation': 'log_discount', 'day_count': 'act365'},
    ),
    'yc_dynamic_nelson_siegel': NodeMeta(
        fn='yc_dynamic_nelson_siegel',
        category='18-yield-curve',
        card_id=537,
        contract_hash='c2-02b0f4d1f6993de11591968e3d9b9fc8027acc287770b4b13d112a2dabe568d7',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='yields', kind='df_handle', required=True),
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='macro', kind='exog_handle', required=False),
        NodeArgMeta(name='decay', kind='number', required=False),
        NodeArgMeta(name='factors', kind='enum', required=False, enum=('three', 'four_svensson', )),
        NodeArgMeta(name='h', kind='integer', required=False),
        ),
        defaults={'decay': 0.0609, 'factors': 'three', 'h': 0},
    ),
    'yc_shadow_short_rate': NodeMeta(
        fn='yc_shadow_short_rate',
        category='18-yield-curve',
        card_id=538,
        contract_hash='c2-03f265bbfcac921ae5e9dcd7235a3b6d18cc848f464f8c643130a8e23f054eed',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='yields', kind='df_handle', required=True),
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='lower_bound', kind='number', required=False),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('wu_xia', 'krippner', )),
        ),
        defaults={'lower_bound': 0.0, 'n_factors': 3, 'model': 'wu_xia'},
    ),
    'yc_bond_return_predictability': NodeMeta(
        fn='yc_bond_return_predictability',
        category='18-yield-curve',
        card_id=539,
        contract_hash='c2-78ae0f1cb7acfa6063e65bbdcd0c4d5fd7f3dd25e3709e1d0417bd73d61a6d8a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='yields', kind='df_handle', required=True),
        NodeArgMeta(name='maturities', kind='num_array', required=True),
        NodeArgMeta(name='holding_period', kind='integer', required=False),
        NodeArgMeta(name='factor', kind='boolean', required=False),
        NodeArgMeta(name='cov_type', kind='enum', required=False, enum=('hac', 'hodrick', 'robust', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'holding_period': 12, 'factor': True, 'cov_type': 'hac', 'conf_level': 0.95},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'atsm_estimate': {'n_factors': 1, 'stationary_Q': False, 'horizon': 25, 'compute_term_premia': True},
    'fit_nelson_siegel': {},
    'fit_svensson': {},
    'yc_fit': {'tau_init': 1, 'tau1_init': 1, 'tau2_init': 5},
    'yc_transform': {'n_components': 3, 'scale': False},
    'ycnp_estimate': {'span_x': 60, 'smooth': False},
    'yc_acm_decomposition': {'n_factors': 5, 'real': False},
    'yc_bootstrap_curve': {'method': 'bootstrap', 'interpolation': 'log_discount', 'day_count': 'act365'},
    'yc_dynamic_nelson_siegel': {'decay': 0.0609, 'factors': 'three', 'h': 0},
    'yc_shadow_short_rate': {'lower_bound': 0.0, 'n_factors': 3, 'model': 'wu_xia'},
    'yc_bond_return_predictability': {'holding_period': 12, 'factor': True, 'cov_type': 'hac', 'conf_level': 0.95},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
