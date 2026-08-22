# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 27-frequency-domain: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'spec_cumulative_periodogram': {
        'fn': 'spec_cumulative_periodogram',
        'description': 'spec_cumulative_periodogram -- category 27-frequency-domain, method card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (ts or single-series df); >= 4 observations, without NA.', 'taper': 'Split-cosine-bell taper in [0, 0.5] (default 0.1, as in the cumulative-periodogram routine).'},
        'input_example': {'x': '<series_handle>', 'taper': 0.1},
    },
    'spec_periodogram': {
        'fn': 'spec_periodogram',
        'description': 'spec_periodogram -- category 27-frequency-domain, method card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (a stored ts or single-series DataFrame); >= 4 observations, without NA.', 'spans': 'Widths of modified Daniell smoothers — vector of ODD positive integers (e.g. [3,5]); None = raw (unsmoothed) periodogram. CAUTION: even spans are blocked (silent-wrong smoother).', 'taper': 'Percentage of split-cosine-bell taper at each end, in [0, 0.5] (default 0.1).', 'pad': 'Zero-padding as a percentage of the length (>= 0; default 0).', 'fast': 'Padding to a highly-composite length for a fast FFT (default True).', 'demean': 'Removal of the mean before the FFT (default False).', 'detrend': 'Removal of a linear trend before the FFT (default True).'},
        'input_example': {'x': '<series_handle>', 'taper': 0.1, 'pad': 0, 'fast': True, 'demean': False, 'detrend': True},
    },
    'spec_spectrum': {
        'fn': 'spec_spectrum',
        'description': 'spec_spectrum -- category 27-frequency-domain, method card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (ts or single-series df); >= 4 observations, without NA.', 'method': 'Spectrum estimator (default pgram): pgram=(smoothed) periodogram; ar=autoregressive (Yule-Walker) smooth spectral density.', 'spans': "method='pgram': modified Daniell smoothers (odd positive integers); otherwise None.", 'taper': "method='pgram': split-cosine-bell taper in [0, 0.5] (default 0.1).", 'order': "method='ar': AR order (non-negative integer); None = auto selection via AIC.", 'n_freq': "method='ar': number of frequency points of the estimate (positive integer; default 500)."},
        'input_example': {'x': '<series_handle>', 'taper': 0.1, 'n_freq': 500},
    },
    'wv_coherency': {
        'fn': 'wv_coherency',
        'description': 'wv_coherency -- category 27-frequency-domain, method card #235.',
        'args': {'df': 'Handle to a DataFrame with >= 2 numeric, ALIGNED series (complete, same length, equally spaced samples).', 'x': 'Column name of the 1st series (default: 1st numeric column).', 'y': 'Column name of the 2nd series, x != y (default: 2nd numeric column).', 'dt': 'Sampling time step (default 1).', 'dj': 'Scale voice spacing (default 1/20).', 'lower_period': 'Lower period (>= 2*dt)· default 2*dt.', 'upper_period': 'Upper period (<= n*dt)· default floor(n/3)*dt.', 'loess_span': 'Loess span for detrending in [0,1] (default 0.75).', 'window_size_t': 'Smoothing window size in time for coherence (default 5).', 'window_size_s': 'Smoothing window size in scale for coherence (default 1/4).', 'make_pval': 'Surrogate p-values for cross-power & coherence (default True).', 'method': 'Null model surrogate (default white.noise· see wv_transform).', 'n_sim': 'Number of surrogate simulations (>= 1 if make_pval=True· default 10).', 'seed': 'Seed before the surrogate simulation (default 1).'},
        'input_example': {'df': '<df_handle>', 'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'window_size_t': 5, 'window_size_s': 0.25, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    },
    'wv_transform': {
        'fn': 'wv_transform',
        'description': 'wv_transform -- category 27-frequency-domain, method card #235.',
        'args': {'df': 'Handle to a DataFrame with >= 1 numeric series column (complete, without NA/Inf, >= 8 values, equally spaced samples).', 'series': 'Column name of the series to analyse (default: 1st numeric column).', 'dt': 'Sampling time step (default 1· period is expressed in units of dt).', 'dj': 'Voice spacing (scale resolution)· smaller = denser scales (default 1/20).', 'lower_period': 'Lower period (>= 2*dt, Nyquist)· default 2*dt (if omitted).', 'upper_period': 'Upper period (<= n*dt, otherwise inside the COI = silent-wrong)· default floor(n/3)*dt.', 'loess_span': 'Loess span for detrending before the CWT in [0,1] (0 = no detrending· default 0.75).', 'make_pval': 'Computation of significance p-values via surrogate simulation (default True).', 'method': 'Null model surrogate (default white.noise): white.noise· shuffle· Fourier.rand· AR· ARIMA.', 'n_sim': 'Number of surrogate simulations (>= 1 if make_pval=True· default 10).', 'seed': 'Seed before the surrogate simulation (determinism of p-values· default 1).'},
        'input_example': {'df': '<df_handle>', 'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    },
    'fd_cross_spectrum': {
        'fn': 'fd_cross_spectrum',
        'description': 'fd_cross_spectrum -- category 27-frequency-domain, method card #586.',
        'args': {'x': 'First series.', 'y': 'Second series.', 'method': 'Spectral estimator.', 'nperseg': 'Segment length.', 'detrend': 'Detrending applied per segment.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'x': '<series_handle>', 'y': '<series_handle>', 'method': 'welch', 'detrend': 'linear', 'conf_level': 0.95},
    },
    'fd_wavelet_mra': {
        'fn': 'fd_wavelet_mra',
        'description': 'fd_wavelet_mra -- category 27-frequency-domain, method card #587.',
        'args': {'x': 'Series.', 'wavelet': 'Wavelet filter.', 'transform': 'Transform.', 'levels': 'Decomposition levels; omitted = maximum admissible.', 'boundary': 'Boundary handling.'},
        'input_example': {'x': '<series_handle>', 'wavelet': 'la8', 'transform': 'modwt', 'boundary': 'reflection'},
    },
    'fd_wavelet_variance': {
        'fn': 'fd_wavelet_variance',
        'description': 'fd_wavelet_variance -- category 27-frequency-domain, method card #587.',
        'args': {'x': 'First series.', 'y': 'Second series for cross-correlation.', 'wavelet': 'Wavelet filter.', 'levels': 'Scales computed.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'x': '<series_handle>', 'wavelet': 'la8', 'conf_level': 0.95},
    },
    'fd_spectral_estimate': {
        'fn': 'fd_spectral_estimate',
        'description': 'fd_spectral_estimate -- category 27-frequency-domain, method card #588.',
        'args': {'x': 'Series.', 'method': 'Estimator.', 'n_tapers': 'Tapers for the multitaper estimator.', 'time_bandwidth': 'Time-bandwidth product.', 'nperseg': 'Segment length for Welch.', 'ar_order': 'Order for the parametric estimator.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'x': '<series_handle>', 'method': 'multitaper', 'n_tapers': 5, 'time_bandwidth': 4.0, 'conf_level': 0.95},
    },
    'fd_frequency_granger': {
        'fn': 'fd_frequency_granger',
        'description': 'fd_frequency_granger -- category 27-frequency-domain, method card #589.',
        'args': {'y': 'Two or more series.', 'cause': 'Candidate causal variable.', 'effect': 'Affected variable.', 'lags': 'VAR lag order.', 'bands': 'Frequency bands to aggregate over.', 'alpha': 'Significance level.'},
        'input_example': {'y': '<multiseries_handle>', 'cause': '...', 'effect': '...', 'lags': 4, 'alpha': 0.05},
    },
    'fd_emd': {
        'fn': 'fd_emd',
        'description': 'fd_emd -- category 27-frequency-domain, method card #590.',
        'args': {'x': 'Series.', 'method': 'Variant.', 'max_imfs': 'Maximum modes extracted.', 'n_ensemble': 'Ensemble size for the noise-assisted variants.', 'noise_strength': 'Added noise standard deviation.', 'hilbert': 'Compute the Hilbert spectrum.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'x': '<series_handle>', 'method': 'ceemdan', 'max_imfs': 10, 'n_ensemble': 100, 'noise_strength': 0.2, 'hilbert': True, 'seed': 1},
    },
    'fd_synchrosqueeze': {
        'fn': 'fd_synchrosqueeze',
        'description': 'fd_synchrosqueeze -- category 27-frequency-domain, method card #591.',
        'args': {'x': 'Series.', 'transform': 'Transform.', 'squeeze': 'Apply synchrosqueezing.', 'wavelet': 'Analysing wavelet.', 'extract_ridges': 'Ridges to extract; 0 = none.'},
        'input_example': {'x': '<series_handle>', 'transform': 'cwt', 'squeeze': True, 'wavelet': 'morlet', 'extract_ridges': 0},
    },
    'fd_lomb_scargle': {
        'fn': 'fd_lomb_scargle',
        'description': 'fd_lomb_scargle -- category 27-frequency-domain, method card #592.',
        'args': {'x': 'Irregularly sampled series with timestamps.', 'frequencies': 'Frequency grid; omitted = automatic.', 'normalisation': 'Power normalisation.', 'false_alarm': 'Compute false-alarm probabilities.'},
        'input_example': {'x': '<irregular_series_handle>', 'normalisation': 'standard', 'false_alarm': True},
    },
    'fd_band_variance': {
        'fn': 'fd_band_variance',
        'description': 'fd_band_variance -- category 27-frequency-domain, method card #592.',
        'args': {'x': 'Series.', 'bands': 'Band edges in cycles per period.', 'method': 'Spectral estimator.'},
        'input_example': {'x': '<series_handle>', 'bands': [1.0, 2.0], 'method': 'welch'},
    },
}
