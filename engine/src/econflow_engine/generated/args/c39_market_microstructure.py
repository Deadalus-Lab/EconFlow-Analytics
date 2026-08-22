# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 39-market-microstructure -- 14 nodes. No descriptions."""

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
    'ms_ohlc_spread': NodeMeta(
        fn='ms_ohlc_spread',
        category='39-market-microstructure',
        card_id=333,
        contract_hash='c2-c1210addd02e1fcbe2d0df334ff0ba90390bda28fd0a8e0798081035576657fc',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='open', kind='series_handle', required=True),
        NodeArgMeta(name='high', kind='series_handle', required=True),
        NodeArgMeta(name='low', kind='series_handle', required=True),
        NodeArgMeta(name='close', kind='series_handle', required=True),
        NodeArgMeta(name='estimator', kind='enum', required=False, enum=('roll', 'corwin_schultz', 'abdi_ranaldo', 'edge', )),
        NodeArgMeta(name='negative', kind='enum', required=False, enum=('keep', 'zero', 'drop', )),
        NodeArgMeta(name='window', kind='integer', required=False),
        ),
        defaults={'estimator': 'edge', 'negative': 'zero'},
    ),
    'ms_amihud': NodeMeta(
        fn='ms_amihud',
        category='39-market-microstructure',
        card_id=334,
        contract_hash='c2-c80aa4204b7c1575e5e751013488aa1b25489c7707c456790ec6b9394abac222',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='volume', kind='series_handle', required=True),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='min_observations', kind='integer', required=False),
        ),
        defaults={'window': 21, 'min_observations': 15},
    ),
    'ms_liquidity_panel': NodeMeta(
        fn='ms_liquidity_panel',
        category='39-market-microstructure',
        card_id=334,
        contract_hash='c2-eb0ac46e4114ad8d652fbb9e58c53140aa45c9224352cf11a703526f0b3e2097',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='volume', kind='series_handle', required=True),
        NodeArgMeta(name='shares_outstanding', kind='series_handle', required=False),
        NodeArgMeta(name='window', kind='integer', required=False),
        ),
        defaults={'window': 21},
    ),
    'ms_kyle_lambda': NodeMeta(
        fn='ms_kyle_lambda',
        category='39-market-microstructure',
        card_id=335,
        contract_hash='c2-16d4f90aece0a636eb6915f8666df329115564aab68dfb3bef084fb15063518a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='signed_volume', kind='series_handle', required=True),
        NodeArgMeta(name='window', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'conf_level': 0.95},
    ),
    'ms_hasbrouck_lambda': NodeMeta(
        fn='ms_hasbrouck_lambda',
        category='39-market-microstructure',
        card_id=335,
        contract_hash='c2-0157011d62cc8732aabf1a1869a6a82fa472456e242977689c6b40d8294de7d2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='series_handle', required=True),
        NodeArgMeta(name='signed_trades', kind='series_handle', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        ),
        defaults={'lags': 5},
    ),
    'ms_classify_trades': NodeMeta(
        fn='ms_classify_trades',
        category='39-market-microstructure',
        card_id=336,
        contract_hash='c2-8e70e9dc502e7c688e8d68a7e544b3c60d6c7d28a36391852d002cf51af2cd3a',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='price', kind='series_handle', required=True),
        NodeArgMeta(name='bid', kind='series_handle', required=False),
        NodeArgMeta(name='ask', kind='series_handle', required=False),
        NodeArgMeta(name='rule', kind='enum', required=False, enum=('tick', 'quote', 'lee_ready', 'emo', 'clnv', )),
        NodeArgMeta(name='quote_lag', kind='number', required=False),
        ),
        defaults={'rule': 'lee_ready', 'quote_lag': 0.0},
    ),
    'ms_order_flow_imbalance': NodeMeta(
        fn='ms_order_flow_imbalance',
        category='39-market-microstructure',
        card_id=336,
        contract_hash='c2-34305357e89ff8f5b3e12b03a08b32d89eee552f02e8adda1c5277cb478a1ba0',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='signed_volume', kind='series_handle', required=True),
        NodeArgMeta(name='frequency', kind='enum', required=False, enum=('1min', '5min', '15min', '30min', '1h', 'daily', )),
        ),
        defaults={'frequency': '5min'},
    ),
    'ms_realised_variance': NodeMeta(
        fn='ms_realised_variance',
        category='39-market-microstructure',
        card_id=337,
        contract_hash='c2-b057e39cbd2add5328a8a411cd67602e42e14169df4b4cfa50187faf43f1c2b1',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='prices', kind='irregular_series_handle', required=True),
        NodeArgMeta(name='estimator', kind='enum', required=False, enum=('naive', 'sparse', 'two_scale', 'multi_scale', 'kernel', 'pre_averaged', )),
        NodeArgMeta(name='sampling', kind='enum', required=False, enum=('calendar', 'tick', 'business', )),
        NodeArgMeta(name='interval', kind='integer', required=False),
        ),
        defaults={'estimator': 'kernel', 'sampling': 'calendar', 'interval': 300},
    ),
    'ms_noise_variance': NodeMeta(
        fn='ms_noise_variance',
        category='39-market-microstructure',
        card_id=337,
        contract_hash='c2-4d35cc57cad4b742a4e799b63d55e488282cdddd4755d1ed277c7e5dcd64e2d2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='prices', kind='irregular_series_handle', required=True),
        ),
        defaults={},
    ),
    'ms_signature_plot': NodeMeta(
        fn='ms_signature_plot',
        category='39-market-microstructure',
        card_id=338,
        contract_hash='c2-bf0c7f3906e4e80136e389a83aa54dcdff38ab4ec88f6dabf90bba28bea4e1ac',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='prices', kind='irregular_series_handle', required=True),
        NodeArgMeta(name='intervals', kind='int_array', required=False),
        ),
        defaults={'intervals': [5, 10, 30, 60, 300, 600, 1800]},
    ),
    'ms_intraday_periodicity': NodeMeta(
        fn='ms_intraday_periodicity',
        category='39-market-microstructure',
        card_id=338,
        contract_hash='c2-ddb6a3e38e2f3a9c8c5fd4d4bec17f428892500bed2d6354829181512c910f81',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='returns', kind='irregular_series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('mean_absolute', 'wsd', 'shortest_half', 'trimmed_mean', )),
        NodeArgMeta(name='bins_per_day', kind='integer', required=False),
        ),
        defaults={'method': 'wsd', 'bins_per_day': 78},
    ),
    'ms_spread_decomposition': NodeMeta(
        fn='ms_spread_decomposition',
        category='39-market-microstructure',
        card_id=339,
        contract_hash='c2-785ed3d712dbedbda3afa047ca3fba1ff922023803930a5371de59d0795c10ff',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='price', kind='series_handle', required=True),
        NodeArgMeta(name='midpoint', kind='series_handle', required=True),
        NodeArgMeta(name='direction', kind='series_handle', required=True),
        NodeArgMeta(name='horizon', kind='integer', required=False),
        ),
        defaults={'horizon': 5},
    ),
    'ms_information_share': NodeMeta(
        fn='ms_information_share',
        category='39-market-microstructure',
        card_id=339,
        contract_hash='c2-afc16e6bc18fead659a820545efcbf0293bc5232beaac947e55e953e98701d30',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='prices', kind='multiseries_handle', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        ),
        defaults={'lags': 5},
    ),
    'ms_component_share': NodeMeta(
        fn='ms_component_share',
        category='39-market-microstructure',
        card_id=339,
        contract_hash='c2-eab4c7a0abead09b9d305d0934fe25f6bcf1c0d2d947e3cc6ee962c975236468',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='prices', kind='multiseries_handle', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        ),
        defaults={'lags': 5},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'ms_ohlc_spread': {'estimator': 'edge', 'negative': 'zero'},
    'ms_amihud': {'window': 21, 'min_observations': 15},
    'ms_liquidity_panel': {'window': 21},
    'ms_kyle_lambda': {'conf_level': 0.95},
    'ms_hasbrouck_lambda': {'lags': 5},
    'ms_classify_trades': {'rule': 'lee_ready', 'quote_lag': 0.0},
    'ms_order_flow_imbalance': {'frequency': '5min'},
    'ms_realised_variance': {'estimator': 'kernel', 'sampling': 'calendar', 'interval': 300},
    'ms_noise_variance': {},
    'ms_signature_plot': {'intervals': [5, 10, 30, 60, 300, 600, 1800]},
    'ms_intraday_periodicity': {'method': 'wsd', 'bins_per_day': 78},
    'ms_spread_decomposition': {'horizon': 5},
    'ms_information_share': {'lags': 5},
    'ms_component_share': {'lags': 5},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
