# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 2 for category 27-frequency-domain -- 14 nodes. No descriptions."""

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
    'spec_cumulative_periodogram': NodeMeta(
        fn='spec_cumulative_periodogram',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c2-0fff38a9fab00810f45f4a89fdfbfcfaeaa0fd3b298e06199f51477487c6b2e3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='taper', kind='number', required=False),
        ),
        defaults={'taper': 0.1},
    ),
    'spec_periodogram': NodeMeta(
        fn='spec_periodogram',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c2-bce61db0dc1dc3b122911d3e59f118a57e2427017878d53c1b1e1dfa61573afa',
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
    'spec_spectrum': NodeMeta(
        fn='spec_spectrum',
        category='27-frequency-domain',
        card_id=236,
        contract_hash='c2-a40b554719bdc1c6dca4bb5dec775552406ca3e7e05826bf9019712ae3b505b3',
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
        contract_hash='c2-cccd12b0c8700f77cb0790275bd3f1a99587460e8796e6dcf83b99ae82c78756',
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
    'wv_transform': NodeMeta(
        fn='wv_transform',
        category='27-frequency-domain',
        card_id=235,
        contract_hash='c2-dd07ea0fcf802b5cf0d08a5805b79028fa74987dc376cf2e2e8b1a9f571a73d1',
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
    'fd_cross_spectrum': NodeMeta(
        fn='fd_cross_spectrum',
        category='27-frequency-domain',
        card_id=586,
        contract_hash='c2-503a87a939b3046fea56ce47252279ab264e7ac2981b7794399b7661f812fa0b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='y', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('welch', 'multitaper', 'bartlett', 'periodogram', )),
        NodeArgMeta(name='nperseg', kind='integer', required=False),
        NodeArgMeta(name='detrend', kind='enum', required=False, enum=('none', 'constant', 'linear', )),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'welch', 'detrend': 'linear', 'conf_level': 0.95},
    ),
    'fd_wavelet_mra': NodeMeta(
        fn='fd_wavelet_mra',
        category='27-frequency-domain',
        card_id=587,
        contract_hash='c2-ef57c46534846f67cccd729c528a56c73edfca04b6c0295f69b16996f063e84d',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='wavelet', kind='enum', required=False, enum=('haar', 'd4', 'la8', 'la16', 'c6', 'sym8', )),
        NodeArgMeta(name='transform', kind='enum', required=False, enum=('dwt', 'modwt', 'swt', )),
        NodeArgMeta(name='levels', kind='integer', required=False),
        NodeArgMeta(name='boundary', kind='enum', required=False, enum=('periodic', 'reflection', 'zero', )),
        ),
        defaults={'wavelet': 'la8', 'transform': 'modwt', 'boundary': 'reflection'},
    ),
    'fd_wavelet_variance': NodeMeta(
        fn='fd_wavelet_variance',
        category='27-frequency-domain',
        card_id=587,
        contract_hash='c2-3a9be8a5460b35c5095b415f3c1db5783cf0d0c93b7d3516c24d7285151c667b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='y', kind='series_handle', required=False),
        NodeArgMeta(name='wavelet', kind='enum', required=False, enum=('haar', 'd4', 'la8', 'la16', 'c6', 'sym8', )),
        NodeArgMeta(name='levels', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'wavelet': 'la8', 'conf_level': 0.95},
    ),
    'fd_spectral_estimate': NodeMeta(
        fn='fd_spectral_estimate',
        category='27-frequency-domain',
        card_id=588,
        contract_hash='c2-70b86b5a495a961cc3010cff8f03c73e2229e8324aec1dc1ddc89bcee2274d5b',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('multitaper', 'welch', 'bartlett', 'periodogram', 'ar', )),
        NodeArgMeta(name='n_tapers', kind='integer', required=False),
        NodeArgMeta(name='time_bandwidth', kind='number', required=False),
        NodeArgMeta(name='nperseg', kind='integer', required=False),
        NodeArgMeta(name='ar_order', kind='integer', required=False),
        NodeArgMeta(name='conf_level', kind='number', required=False),
        ),
        defaults={'method': 'multitaper', 'n_tapers': 5, 'time_bandwidth': 4.0, 'conf_level': 0.95},
    ),
    'fd_frequency_granger': NodeMeta(
        fn='fd_frequency_granger',
        category='27-frequency-domain',
        card_id=589,
        contract_hash='c2-1a5ffc4a25fe612f884cdbb67e70be1e8247a4b94e0de43e81cae169fd4349ce',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='y', kind='multiseries_handle', required=True),
        NodeArgMeta(name='cause', kind='string', required=True),
        NodeArgMeta(name='effect', kind='string', required=True),
        NodeArgMeta(name='lags', kind='integer', required=False),
        NodeArgMeta(name='bands', kind='num_array', required=False),
        NodeArgMeta(name='alpha', kind='number', required=False),
        ),
        defaults={'lags': 4, 'alpha': 0.05},
    ),
    'fd_emd': NodeMeta(
        fn='fd_emd',
        category='27-frequency-domain',
        card_id=590,
        contract_hash='c2-6f666474996a783264a48ec76e2a52412c54db36f6a2a3b1abd666ba2504f4c2',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('emd', 'eemd', 'ceemdan', )),
        NodeArgMeta(name='max_imfs', kind='integer', required=False),
        NodeArgMeta(name='n_ensemble', kind='integer', required=False),
        NodeArgMeta(name='noise_strength', kind='number', required=False),
        NodeArgMeta(name='hilbert', kind='boolean', required=False),
        NodeArgMeta(name='seed', kind='integer', required=True),
        ),
        defaults={'method': 'ceemdan', 'max_imfs': 10, 'n_ensemble': 100, 'noise_strength': 0.2, 'hilbert': True},
    ),
    'fd_synchrosqueeze': NodeMeta(
        fn='fd_synchrosqueeze',
        category='27-frequency-domain',
        card_id=591,
        contract_hash='c2-7621b69bb16aafe344b8da72ce89dab982baf9762ed0dab02a16363d31bd60b3',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='transform', kind='enum', required=False, enum=('cwt', 'stft', )),
        NodeArgMeta(name='squeeze', kind='boolean', required=False),
        NodeArgMeta(name='wavelet', kind='enum', required=False, enum=('morlet', 'bump', 'gmw', )),
        NodeArgMeta(name='extract_ridges', kind='integer', required=False),
        ),
        defaults={'transform': 'cwt', 'squeeze': True, 'wavelet': 'morlet', 'extract_ridges': 0},
    ),
    'fd_lomb_scargle': NodeMeta(
        fn='fd_lomb_scargle',
        category='27-frequency-domain',
        card_id=592,
        contract_hash='c2-d3c1ff511be993c28deef576e24a38cc620320af714e55eede7d359fd8dee5c8',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='irregular_series_handle', required=True),
        NodeArgMeta(name='frequencies', kind='num_array', required=False),
        NodeArgMeta(name='normalisation', kind='enum', required=False, enum=('standard', 'model', 'log', 'psd', )),
        NodeArgMeta(name='false_alarm', kind='boolean', required=False),
        ),
        defaults={'normalisation': 'standard', 'false_alarm': True},
    ),
    'fd_band_variance': NodeMeta(
        fn='fd_band_variance',
        category='27-frequency-domain',
        card_id=592,
        contract_hash='c2-c31a5fb7c7149e5aaa9845134a0b848f2cec171b9fb1b7913a4a1f7ad04ceef6',
        register_field=None,
        executability=NodeExecutabilityMeta(status='executable', reason_code=None, reason=None, blocked_arg=None),
        memory_class='light',
        args=(
        NodeArgMeta(name='x', kind='series_handle', required=True),
        NodeArgMeta(name='bands', kind='num_array', required=True),
        NodeArgMeta(name='method', kind='enum', required=False, enum=('welch', 'multitaper', 'periodogram', )),
        ),
        defaults={'method': 'welch'},
    ),
}

#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent
#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.
DEFAULTS: dict[str, dict[str, object]] = {
    'spec_cumulative_periodogram': {'taper': 0.1},
    'spec_periodogram': {'taper': 0.1, 'pad': 0, 'fast': True, 'demean': False, 'detrend': True},
    'spec_spectrum': {'taper': 0.1, 'n_freq': 500},
    'wv_coherency': {'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'window_size_t': 5, 'window_size_s': 0.25, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    'wv_transform': {'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    'fd_cross_spectrum': {'method': 'welch', 'detrend': 'linear', 'conf_level': 0.95},
    'fd_wavelet_mra': {'wavelet': 'la8', 'transform': 'modwt', 'boundary': 'reflection'},
    'fd_wavelet_variance': {'wavelet': 'la8', 'conf_level': 0.95},
    'fd_spectral_estimate': {'method': 'multitaper', 'n_tapers': 5, 'time_bandwidth': 4.0, 'conf_level': 0.95},
    'fd_frequency_granger': {'lags': 4, 'alpha': 0.05},
    'fd_emd': {'method': 'ceemdan', 'max_imfs': 10, 'n_ensemble': 100, 'noise_strength': 0.2, 'hilbert': True},
    'fd_synchrosqueeze': {'transform': 'cwt', 'squeeze': True, 'wavelet': 'morlet', 'extract_ridges': 0},
    'fd_lomb_scargle': {'normalisation': 'standard', 'false_alarm': True},
    'fd_band_variance': {'method': 'welch'},
}


@cache
def wire_model(fn: str) -> type[BaseModel]:
    """The model the ENGINE validates. Built on first use and cached."""
    return build_wire_model(NODE_META[fn])


@cache
def authoring_model(fn: str) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits. Built on first use and cached."""
    return build_authoring_model(NODE_META[fn])
