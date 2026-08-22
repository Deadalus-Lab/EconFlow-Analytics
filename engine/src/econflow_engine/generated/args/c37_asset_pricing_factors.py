# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 37-asset-pricing-factors -- 15 nodes. No descriptions."""

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
    'ap_factor_regression': NodeMeta(
        fn='ap_factor_regression',
        category='37-asset-pricing-factors',
        card_id=316,
        contract_hash='c2-763d174d27f49a0d4e3aadd0fbcd42213d605ca9053c30732e5b1d737bdd417d',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='multiseries_handle', required=True),
        NodeArgMeta(name='factors', kind='multiseries_handle', required=True),
        NodeArgMeta(name='cov_type', kind='enum', required=False, enum=('nonrobust', 'robust', 'hac', )),
        NodeArgMeta(name='bandwidth', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'cov_type': 'hac', 'conf_level': 0.95},
    ),
    'ap_alpha_table': NodeMeta(
        fn='ap_alpha_table',
        category='37-asset-pricing-factors',
        card_id=316,
        contract_hash='c2-1a26a64a59f13e1637554abd981942fa0088fa0e590beb60b364810599bd2997',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='annualise', kind='boolean', required=False),
        ),
        defaults={'annualise': True},
    ),
    'ap_grs_test': NodeMeta(
        fn='ap_grs_test',
        category='37-asset-pricing-factors',
        card_id=317,
        contract_hash='c2-a878168b28dbf776bb2bff52ed0c69bc3dfd89d6fc6b9dc2eec8beb4da0085f9',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='multiseries_handle', required=True),
        NodeArgMeta(name='factors', kind='multiseries_handle', required=True),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'alpha': 0.05},
    ),
    'ap_fama_macbeth': NodeMeta(
        fn='ap_fama_macbeth',
        category='37-asset-pricing-factors',
        card_id=318,
        contract_hash='c2-fcd90fe0a70bcfcb0a4f290414f99e772cd0366a1c91c891de7e63ca4f3280af',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='multiseries_handle', required=True),
        NodeArgMeta(name='factors', kind='multiseries_handle', required=True),
        NodeArgMeta(name='shanken', kind='boolean', required=False),
        NodeArgMeta(name='intercept', kind='boolean', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'shanken': True, 'intercept': True, 'conf_level': 0.95},
    ),
    'ap_sdf_gmm': NodeMeta(
        fn='ap_sdf_gmm',
        category='37-asset-pricing-factors',
        card_id=319,
        contract_hash='c2-8246ad116b8a1738ebb373f57c26ee11d41f8559a0c69e234e544956fb0310b2',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='multiseries_handle', required=True),
        NodeArgMeta(name='factors', kind='multiseries_handle', required=True),
        NodeArgMeta(name='traded', kind='boolean', required=False),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('identity', 'optimal', 'hansen_jagannathan', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'traded': False, 'weighting': 'hansen_jagannathan', 'conf_level': 0.95},
    ),
    'ap_pricing_errors': NodeMeta(
        fn='ap_pricing_errors',
        category='37-asset-pricing-factors',
        card_id=319,
        contract_hash='c2-5d5b0a067e205562ae2bdfb400ba601d6aacaa76febb37bbb57d1aff4a36d083',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        ),
        defaults={},
    ),
    'ap_portfolio_sort': NodeMeta(
        fn='ap_portfolio_sort',
        category='37-asset-pricing-factors',
        card_id=320,
        contract_hash='c2-96c0cf3d31c148f335708dece6a06b280a52518136e711a14790e7357200c345',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='characteristic', kind='df_handle', required=True),
        NodeArgMeta(name='n_portfolios', kind='integer', required=False),
        NodeArgMeta(name='weighting', kind='enum', required=False, enum=('equal', 'value', )),
        NodeArgMeta(name='market_cap', kind='df_handle', required=False),
        ),
        defaults={'n_portfolios': 5, 'weighting': 'equal'},
    ),
    'ap_double_sort': NodeMeta(
        fn='ap_double_sort',
        category='37-asset-pricing-factors',
        card_id=320,
        contract_hash='c2-a917cf75a98410ccde960d3af50464c95af70ff82517c4f89f3c3604e8c45e1b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='characteristic_1', kind='df_handle', required=True),
        NodeArgMeta(name='characteristic_2', kind='df_handle', required=True),
        NodeArgMeta(name='n_1', kind='integer', required=False),
        NodeArgMeta(name='n_2', kind='integer', required=False),
        NodeArgMeta(name='conditional', kind='boolean', required=False),
        ),
        defaults={'n_1': 5, 'n_2': 5, 'conditional': False},
    ),
    'ap_pca_factors': NodeMeta(
        fn='ap_pca_factors',
        category='37-asset-pricing-factors',
        card_id=321,
        contract_hash='c2-14e73b01499b1775d0fc49469b9b39a8b1cb2ce500e161e20089bc0d9b759387',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='n_factors', kind='integer', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('pca', 'asymptotic_pca', 'rp_pca', )),
        NodeArgMeta(name='criterion', kind='enum', required=False, enum=('bai_ng_icp1', 'bai_ng_icp2', 'bai_ng_icp3', 'scree', 'explained_variance', )),
        NodeArgMeta(name='standardise', kind='boolean', required=False),
        ),
        defaults={'method': 'pca', 'criterion': 'bai_ng_icp2', 'standardise': True},
    ),
    'ap_n_factors_test': NodeMeta(
        fn='ap_n_factors_test',
        category='37-asset-pricing-factors',
        card_id=321,
        contract_hash='c2-4ddc1efdc2c0e7045f6f0d59fb8b4b45e7b4ccabc1e741afb68100cbb00587cb',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='k_max', kind='integer', required=False),
        ),
        defaults={'k_max': 10},
    ),
    'ap_event_study': NodeMeta(
        fn='ap_event_study',
        category='37-asset-pricing-factors',
        card_id=322,
        contract_hash='c2-3cbe346a7041cbfaaec0650d7f6d8b9b9db000cde39cfa23c85fff5563bef68d',
        register_field='fit',
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='df_handle', required=True),
        NodeArgMeta(name='events', kind='df_handle', required=True),
        NodeArgMeta(name='market', kind='series_handle', required=False),
        NodeArgMeta(name='model', kind='enum', required=False, enum=('market', 'market_adjusted', 'mean_adjusted', 'fama_french', )),
        NodeArgMeta(name='estimation_window', kind='int_array', required=False),
        NodeArgMeta(name='event_window', kind='int_array', required=False),
        ),
        defaults={'model': 'market', 'estimation_window': [-250, -30], 'event_window': [-5, 5]},
    ),
    'ap_car_test': NodeMeta(
        fn='ap_car_test',
        category='37-asset-pricing-factors',
        card_id=322,
        contract_hash='c2-a6c6f4e93a5edd189f6cff502ed72ff815a78270a86816dc76c5b85962cd6803',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='fit', kind='raw_handle', required=True),
        NodeArgMeta(name='aggregation', kind='enum', required=False, enum=('car', 'bhar', )),
        NodeArgMeta(name='test', kind='enum', required=False, enum=('patell', 'boehmer', 'rank', 'sign', 'crude', )),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'aggregation': 'car', 'test': 'patell', 'alpha': 0.05},
    ),
    'ap_performance_summary': NodeMeta(
        fn='ap_performance_summary',
        category='37-asset-pricing-factors',
        card_id=323,
        contract_hash='c2-9e70faa27f27e0ad87997ebdbfee1fff3fe122584c01939e676fd2e735ced7d4',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='benchmark', kind='series_handle', required=False),
        NodeArgMeta(name='risk_free', kind='series_handle', required=False),
        NodeArgMeta(name='frequency', kind='enum', required=False, enum=('daily', 'weekly', 'monthly', 'quarterly', 'annual', )),
        NodeArgMeta(name='autocorrelation_adjust', kind='boolean', required=False),
        ),
        defaults={'frequency': 'monthly', 'autocorrelation_adjust': True},
    ),
    'ap_drawdown': NodeMeta(
        fn='ap_drawdown',
        category='37-asset-pricing-factors',
        card_id=323,
        contract_hash='c2-4577405066cee8893288632afc26ed8997b7cf5be2b3a2512bd72cf496fe6455',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='top_n', kind='integer', required=False),
        ),
        defaults={'top_n': 5},
    ),
    'ap_turnover': NodeMeta(
        fn='ap_turnover',
        category='37-asset-pricing-factors',
        card_id=323,
        contract_hash='c2-832b71de80f51cdc977e8d9a4d388d5f1f8d448386ce7999e5d40a0db3ddcb71',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='weights', kind='df_handle', required=True),
        NodeArgMeta(name='cost_bps', kind='number', required=False),
        ),
        defaults={'cost_bps': 10.0},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'ap_factor_regression': {'cov_type': 'hac', 'conf_level': 0.95},
    'ap_alpha_table': {'annualise': True},
    'ap_grs_test': {'alpha': 0.05},
    'ap_fama_macbeth': {'shanken': True, 'intercept': True, 'conf_level': 0.95},
    'ap_sdf_gmm': {'traded': False, 'weighting': 'hansen_jagannathan', 'conf_level': 0.95},
    'ap_pricing_errors': {},
    'ap_portfolio_sort': {'n_portfolios': 5, 'weighting': 'equal'},
    'ap_double_sort': {'n_1': 5, 'n_2': 5, 'conditional': False},
    'ap_pca_factors': {'method': 'pca', 'criterion': 'bai_ng_icp2', 'standardise': True},
    'ap_n_factors_test': {'k_max': 10},
    'ap_event_study': {'model': 'market', 'estimation_window': [-250, -30], 'event_window': [-5, 5]},
    'ap_car_test': {'aggregation': 'car', 'test': 'patell', 'alpha': 0.05},
    'ap_performance_summary': {'frequency': 'monthly', 'autocorrelation_adjust': True},
    'ap_drawdown': {'top_n': 5},
    'ap_turnover': {'cost_bps': 10.0},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
