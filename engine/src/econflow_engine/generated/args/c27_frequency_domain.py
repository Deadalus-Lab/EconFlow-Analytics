# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 27-frequency-domain -- 5 nodes. No descriptions."""

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
    'sp_cumulative_periodogram': NodeMeta(
        fn='sp_cumulative_periodogram',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c-947a6c581ff35fe648bea1d4d77db4543107e0528cb5105ca59e9f1a41f9b09d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='taper', kind='number', required=False),
        ),
        defaults={'taper': 0.1},
    ),
    'sp_periodogram': NodeMeta(
        fn='sp_periodogram',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c-0f452470e5d6028a656511e2f1fd1ab435c92af7be31d18446f8e3378e550c58',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='spans', kind='int_array', required=False),
        NodeArgMeta(name='taper', kind='number', required=False),
        NodeArgMeta(name='pad', kind='number', required=False),
        NodeArgMeta(name='fast', kind='boolean', required=False),
        NodeArgMeta(name='demean', kind='boolean', required=False),
        NodeArgMeta(name='detrend', kind='boolean', required=False),
        ),
        defaults={'taper': 0.1, 'pad': 0, 'fast': True, 'demean': False, 'detrend': True},
    ),
    'sp_spectrum': NodeMeta(
        fn='sp_spectrum',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c-562fe2a3927281f0bf2361eed95c74901509be933a5fa88b7979a15b58958653',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('pgram', 'ar', )),
        NodeArgMeta(name='spans', kind='int_array', required=False),
        NodeArgMeta(name='taper', kind='number', required=False),
        NodeArgMeta(name='order', kind='integer', required=False),
        NodeArgMeta(name='n_freq', kind='integer', required=False),
        ),
        defaults={'taper': 0.1, 'n_freq': 500},
    ),
    'wv_coherency': NodeMeta(
        fn='wv_coherency',
        category='27-frequency-domain',
        card_id=235,
        contract_hash='c-62a8e46a40171d7b80167f4e553f95a7215448afb8d246a3777b5ac8ca257c13',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='x', kind='string', required=False),
        NodeArgMeta(name='y', kind='string', required=False),
        NodeArgMeta(name='dt', kind='number', required=False),
        NodeArgMeta(name='dj', kind='number', required=False),
        NodeArgMeta(name='lower_period', kind='number', required=False),
        NodeArgMeta(name='upper_period', kind='number', required=False),
        NodeArgMeta(name='loess_span', kind='number', required=False),
        NodeArgMeta(name='window_size_t', kind='number', required=False),
        NodeArgMeta(name='window_size_s', kind='number', required=False),
        NodeArgMeta(name='make_pval', kind='boolean', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('white.noise', 'shuffle', 'Fourier.rand', 'AR', 'ARIMA', )),
        NodeArgMeta(name='n_sim', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'window_size_t': 5, 'window_size_s': 0.25, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    ),
    'wv_wavelet': NodeMeta(
        fn='wv_wavelet',
        category='27-frequency-domain',
        card_id=235,
        contract_hash='c-48453db897ecc50c67568906d5a73dacd0060cc4ef181cc3532be31e6f893ba6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='heavy',
        args=(
        NodeArgMeta(name='df', kind='df_handle', required=True),
        NodeArgMeta(name='series', kind='string', required=False),
        NodeArgMeta(name='dt', kind='number', required=False),
        NodeArgMeta(name='dj', kind='number', required=False),
        NodeArgMeta(name='lower_period', kind='number', required=False),
        NodeArgMeta(name='upper_period', kind='number', required=False),
        NodeArgMeta(name='loess_span', kind='number', required=False),
        NodeArgMeta(name='make_pval', kind='boolean', required=False),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('white.noise', 'shuffle', 'Fourier.rand', 'AR', 'ARIMA', )),
        NodeArgMeta(name='n_sim', kind='integer', required=False),
        NodeArgMeta(name='seed', kind='integer', required=False),
        ),
        defaults={'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'sp_cumulative_periodogram': {'taper': 0.1},
    'sp_periodogram': {'taper': 0.1, 'pad': 0, 'fast': True, 'demean': False, 'detrend': True},
    'sp_spectrum': {'taper': 0.1, 'n_freq': 500},
    'wv_coherency': {'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'window_size_t': 5, 'window_size_s': 0.25, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    'wv_wavelet': {'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'make_pval': True, 'n_sim': 10, 'seed': 1},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
