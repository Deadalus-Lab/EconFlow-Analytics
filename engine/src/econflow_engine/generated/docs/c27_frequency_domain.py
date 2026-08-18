# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 27-frequency-domain: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'sp_cumulative_periodogram': {
        'fn': 'sp_cumulative_periodogram',
        'description': 'sp_cumulative_periodogram -- category 27-frequency-domain, METHOD-SELECTION card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (ts or single-series df); >= 4 observations, without NA.', 'taper': 'Split-cosine-bell taper in [0, 0.5] (default 0.1, as in the cumulative-periodogram routine).'},
        'input_example': {'x': '<series_handle>', 'taper': 0.1},
    },
    'sp_periodogram': {
        'fn': 'sp_periodogram',
        'description': 'sp_periodogram -- category 27-frequency-domain, METHOD-SELECTION card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (a stored ts or single-series DataFrame); >= 4 observations, without NA.', 'spans': 'Widths of modified Daniell smoothers — vector of ODD positive integers (e.g. [3,5]); None = raw (unsmoothed) periodogram. CAUTION: even spans are blocked (silent-wrong smoother).', 'taper': 'Percentage of split-cosine-bell taper at each end, in [0, 0.5] (default 0.1).', 'pad': 'Zero-padding as a percentage of the length (>= 0; default 0).', 'fast': 'Padding to a highly-composite length for a fast FFT (default True).', 'demean': 'Removal of the mean before the FFT (default False).', 'detrend': 'Removal of a linear trend before the FFT (default True).'},
        'input_example': {'x': '<series_handle>', 'taper': 0.1, 'pad': 0, 'fast': True, 'demean': False, 'detrend': True},
    },
    'sp_spectrum': {
        'fn': 'sp_spectrum',
        'description': 'sp_spectrum -- category 27-frequency-domain, METHOD-SELECTION card #236.',
        'args': {'x': 'Handle to A SINGLE univariate series (ts or single-series df); >= 4 observations, without NA.', 'method': 'Spectrum estimator (default pgram): pgram=(smoothed) periodogram; ar=autoregressive (Yule-Walker) smooth spectral density.', 'spans': "method='pgram': modified Daniell smoothers (odd positive integers); otherwise None.", 'taper': "method='pgram': split-cosine-bell taper in [0, 0.5] (default 0.1).", 'order': "method='ar': AR order (non-negative integer); None = auto selection via AIC.", 'n_freq': "method='ar': number of frequency points of the estimate (positive integer; default 500)."},
        'input_example': {'x': '<series_handle>', 'taper': 0.1, 'n_freq': 500},
    },
    'wv_coherency': {
        'fn': 'wv_coherency',
        'description': 'wv_coherency -- category 27-frequency-domain, METHOD-SELECTION card #235.',
        'args': {'df': 'Handle to a DataFrame with >= 2 numeric, ALIGNED series (complete, same length, equally spaced samples).', 'x': 'Column name of the 1st series (default: 1st numeric column).', 'y': 'Column name of the 2nd series, x != y (default: 2nd numeric column).', 'dt': 'Sampling time step (default 1).', 'dj': 'Scale voice spacing (default 1/20).', 'lower_period': 'Lower period (>= 2*dt)· default 2*dt.', 'upper_period': 'Upper period (<= n*dt)· default floor(n/3)*dt.', 'loess_span': 'Loess span for detrending in [0,1] (default 0.75).', 'window_size_t': 'Smoothing window size in time for coherence (default 5).', 'window_size_s': 'Smoothing window size in scale for coherence (default 1/4).', 'make_pval': 'Surrogate p-values for cross-power & coherence (default True).', 'method': 'Null model surrogate (default white.noise· see wv_wavelet).', 'n_sim': 'Number of surrogate simulations (>= 1 if make_pval=True· default 10).', 'seed': 'Seed before the surrogate simulation (default 1).'},
        'input_example': {'df': '<df_handle>', 'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'window_size_t': 5, 'window_size_s': 0.25, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    },
    'wv_wavelet': {
        'fn': 'wv_wavelet',
        'description': 'wv_wavelet -- category 27-frequency-domain, METHOD-SELECTION card #235.',
        'args': {'df': 'Handle to a DataFrame with >= 1 numeric series column (complete, without NA/Inf, >= 8 values, equally spaced samples).', 'series': 'Column name of the series to analyse (default: 1st numeric column).', 'dt': 'Sampling time step (default 1· period is expressed in units of dt).', 'dj': 'Voice spacing (scale resolution)· smaller = denser scales (default 1/20).', 'lower_period': 'Lower period (>= 2*dt, Nyquist)· default 2*dt (if omitted).', 'upper_period': 'Upper period (<= n*dt, otherwise inside the COI = silent-wrong)· default floor(n/3)*dt.', 'loess_span': 'Loess span for detrending before the CWT in [0,1] (0 = no detrending· default 0.75).', 'make_pval': 'Computation of significance p-values via surrogate simulation (default True).', 'method': 'Null model surrogate (default white.noise): white.noise· shuffle· Fourier.rand· AR· ARIMA.', 'n_sim': 'Number of surrogate simulations (>= 1 if make_pval=True· default 10).', 'seed': 'Seed before the surrogate simulation (determinism of p-values· default 1).'},
        'input_example': {'df': '<df_handle>', 'dt': 1, 'dj': 0.05, 'loess_span': 0.75, 'make_pval': True, 'n_sim': 10, 'seed': 1},
    },
}
