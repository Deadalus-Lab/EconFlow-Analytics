# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 18-yield-curve -- 6 nodes. No descriptions."""

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
        contract_hash='c-04efe0ae69952ba5daa1e045e4ad09d6c94e725a0104cde1d6968929ec238b6a',
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
        contract_hash='c-33136cecac87f5a4cfac3f962ce5d4fb0f034a9f32b2a346931446d3c5129ebd',
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
        contract_hash='c-9bfcda3517f8d436eb23b6bf23adaebdd2c3db7652e31cc5243ec94653c961a4',
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
        contract_hash='c-f33d06d3c4170bde7be37d5a560596207556e6ab8c3d9b711475ce4f7a8de35d',
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
        contract_hash='c-54134b52866a69f27d11c262e56d273e72704e4c5000b84a2d170b50a667765d',
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
    'ycevo_estimate': NodeMeta(
        fn='ycevo_estimate',
        category='18-yield-curve',
        card_id=212,
        contract_hash='c-25597341c1e79b979fa484956ae500264ca805c546c7a884fb61a1d654d48552',
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
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'atsm_estimate': {'n_factors': 1, 'stationary_Q': False, 'horizon': 25, 'compute_term_premia': True},
    'fit_nelson_siegel': {},
    'fit_svensson': {},
    'yc_fit': {'tau_init': 1, 'tau1_init': 1, 'tau2_init': 5},
    'yc_transform': {'n_components': 3, 'scale': False},
    'ycevo_estimate': {'span_x': 60, 'smooth': False},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
