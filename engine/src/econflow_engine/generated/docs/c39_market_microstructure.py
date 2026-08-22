# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 39-market-microstructure: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'ms_ohlc_spread': {
        'fn': 'ms_ohlc_spread',
        'description': 'ms_ohlc_spread -- category 39-market-microstructure, method card #333.',
        'args': {'open': 'Open price.', 'high': 'High price.', 'low': 'Low price.', 'close': 'Close price.', 'estimator': 'Estimator family.', 'negative': 'Handling of negative estimates.', 'window': 'Rolling window in periods; omitted = full sample.'},
        'input_example': {'open': '<series_handle>', 'high': '<series_handle>', 'low': '<series_handle>', 'close': '<series_handle>', 'estimator': 'edge', 'negative': 'zero'},
    },
    'ms_amihud': {
        'fn': 'ms_amihud',
        'description': 'ms_amihud -- category 39-market-microstructure, method card #334.',
        'args': {'returns': 'Daily returns.', 'volume': 'Daily dollar volume.', 'window': 'Aggregation window in days.', 'min_observations': 'Minimum non-zero-volume days required.'},
        'input_example': {'returns': '<series_handle>', 'volume': '<series_handle>', 'window': 21, 'min_observations': 15},
    },
    'ms_liquidity_panel': {
        'fn': 'ms_liquidity_panel',
        'description': 'ms_liquidity_panel -- category 39-market-microstructure, method card #334.',
        'args': {'returns': 'Daily returns.', 'volume': 'Daily share volume.', 'shares_outstanding': 'Shares outstanding for turnover.', 'window': 'Aggregation window in days.'},
        'input_example': {'returns': '<series_handle>', 'volume': '<series_handle>', 'window': 21},
    },
    'ms_kyle_lambda': {
        'fn': 'ms_kyle_lambda',
        'description': 'ms_kyle_lambda -- category 39-market-microstructure, method card #335.',
        'args': {'returns': 'Returns at the sampling frequency.', 'signed_volume': 'Signed order flow.', 'window': 'Rolling window; omitted = full sample.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'returns': '<series_handle>', 'signed_volume': '<series_handle>', 'conf_level': 0.95},
    },
    'ms_hasbrouck_lambda': {
        'fn': 'ms_hasbrouck_lambda',
        'description': 'ms_hasbrouck_lambda -- category 39-market-microstructure, method card #335.',
        'args': {'returns': 'Quote-midpoint returns.', 'signed_trades': 'Signed trade indicator or volume.', 'lags': 'VAR lag order.'},
        'input_example': {'returns': '<series_handle>', 'signed_trades': '<series_handle>', 'lags': 5},
    },
    'ms_classify_trades': {
        'fn': 'ms_classify_trades',
        'description': 'ms_classify_trades -- category 39-market-microstructure, method card #336.',
        'args': {'price': 'Trade price.', 'bid': 'Prevailing bid.', 'ask': 'Prevailing ask.', 'rule': 'Classification rule.', 'quote_lag': 'Quote alignment offset in seconds.'},
        'input_example': {'price': '<series_handle>', 'rule': 'lee_ready', 'quote_lag': 0.0},
    },
    'ms_order_flow_imbalance': {
        'fn': 'ms_order_flow_imbalance',
        'description': 'ms_order_flow_imbalance -- category 39-market-microstructure, method card #336.',
        'args': {'signed_volume': 'Signed trade volume.', 'frequency': 'Aggregation frequency.'},
        'input_example': {'signed_volume': '<series_handle>', 'frequency': '5min'},
    },
    'ms_realised_variance': {
        'fn': 'ms_realised_variance',
        'description': 'ms_realised_variance -- category 39-market-microstructure, method card #337.',
        'args': {'prices': 'Intraday price series with timestamps.', 'estimator': 'Estimator construction.', 'sampling': 'Sampling scheme.', 'interval': 'Sampling interval in seconds.'},
        'input_example': {'prices': '<irregular_series_handle>', 'estimator': 'kernel', 'sampling': 'calendar', 'interval': 300},
    },
    'ms_noise_variance': {
        'fn': 'ms_noise_variance',
        'description': 'ms_noise_variance -- category 39-market-microstructure, method card #337.',
        'args': {'prices': 'Intraday price series.'},
        'input_example': {'prices': '<irregular_series_handle>'},
    },
    'ms_signature_plot': {
        'fn': 'ms_signature_plot',
        'description': 'ms_signature_plot -- category 39-market-microstructure, method card #338.',
        'args': {'prices': 'Intraday price series.', 'intervals': 'Sampling intervals in seconds to scan.'},
        'input_example': {'prices': '<irregular_series_handle>', 'intervals': [5, 10, 30, 60, 300, 600, 1800]},
    },
    'ms_intraday_periodicity': {
        'fn': 'ms_intraday_periodicity',
        'description': 'ms_intraday_periodicity -- category 39-market-microstructure, method card #338.',
        'args': {'returns': 'Intraday returns.', 'method': 'Periodicity estimator.', 'bins_per_day': 'Intraday bins per trading day.'},
        'input_example': {'returns': '<irregular_series_handle>', 'method': 'wsd', 'bins_per_day': 78},
    },
    'ms_spread_decomposition': {
        'fn': 'ms_spread_decomposition',
        'description': 'ms_spread_decomposition -- category 39-market-microstructure, method card #339.',
        'args': {'price': 'Trade price.', 'midpoint': 'Prevailing quote midpoint.', 'direction': 'Signed trade direction.', 'horizon': 'Periods ahead for the post-trade midpoint.'},
        'input_example': {'price': '<series_handle>', 'midpoint': '<series_handle>', 'direction': '<series_handle>', 'horizon': 5},
    },
    'ms_information_share': {
        'fn': 'ms_information_share',
        'description': 'ms_information_share -- category 39-market-microstructure, method card #339.',
        'args': {'prices': 'Price series, one column per venue.', 'lags': 'VECM lag order.'},
        'input_example': {'prices': '<multiseries_handle>', 'lags': 5},
    },
    'ms_component_share': {
        'fn': 'ms_component_share',
        'description': 'ms_component_share -- category 39-market-microstructure, method card #339.',
        'args': {'prices': 'Price series, one column per venue.', 'lags': 'VECM lag order.'},
        'input_example': {'prices': '<multiseries_handle>', 'lags': 5},
    },
}
