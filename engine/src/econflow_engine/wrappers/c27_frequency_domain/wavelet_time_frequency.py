# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``wavelet_time_frequency`` -- method card #235.

#235 Wavelet time-frequency analysis (the Morlet CWT: power spectrum, cross-wavelet, wavelet
    coherence, phase difference — numeric grids)

Category 27-frequency-domain; module ``wavelet_time_frequency``.

Reference implementation: pycwt.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wv_coherency",
    "wv_transform",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def wv_transform(
    *,
    df: pd.DataFrame,
    series: str | None = None,
    dt: float | None = None,
    dj: float | None = None,
    lower_period: float | None = None,
    upper_period: float | None = None,
    loess_span: float | None = None,
    make_pval: bool | None = None,
    method: Literal["white.noise", "shuffle", "Fourier.rand", "AR", "ARIMA"] | None = None,
    n_sim: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``wv_transform`` -- method card #235.

    Wavelet time-frequency analysis (the Morlet CWT: power spectrum, cross-wavelet, wavelet
    coherence, phase difference — numeric grids).

    Category 27-frequency-domain; memory class ``heavy``.

    Args:
        df: [df_handle, required] Handle to a DataFrame with >= 1 numeric series column (complete,
            without NA/Inf, >= 8 values, equally spaced samples).
        series: [string, optional] Column name of the series to analyse (default: 1st numeric
            column).
        dt: [number, optional] Sampling time step (default 1· period is expressed in units of dt).
            Default ``1``.
        dj: [number, optional] Voice spacing (scale resolution)· smaller = denser scales (default
            1/20). Default ``0.05``.
        lower_period: [number, optional] Lower period (>= 2*dt, Nyquist)· default 2*dt (if omitted).
        upper_period: [number, optional] Upper period (<= n*dt, otherwise inside the COI =
            silent-wrong)· default floor(n/3)*dt.
        loess_span: [number, optional] Loess span for detrending before the CWT in [0,1] (0 = no
            detrending· default 0.75). Default ``0.75``.
        make_pval: [boolean, optional] Computation of significance p-values via surrogate simulation
            (default True). Default ``True``.
        method: [enum, optional] Null model surrogate (default white.noise): white.noise· shuffle·
            Fourier.rand· AR· ARIMA.
        n_sim: [integer, optional] Number of surrogate simulations (>= 1 if make_pval=True· default
            10). Default ``10``.
        seed: [integer, optional] Seed before the surrogate simulation (determinism of p-values·
            default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "wv_transform: not implemented."
    )


def wv_coherency(
    *,
    df: pd.DataFrame,
    x: str | None = None,
    y: str | None = None,
    dt: float | None = None,
    dj: float | None = None,
    lower_period: float | None = None,
    upper_period: float | None = None,
    loess_span: float | None = None,
    window_size_t: float | None = None,
    window_size_s: float | None = None,
    make_pval: bool | None = None,
    method: Literal["white.noise", "shuffle", "Fourier.rand", "AR", "ARIMA"] | None = None,
    n_sim: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``wv_coherency`` -- method card #235.

    Wavelet time-frequency analysis (the Morlet CWT: power spectrum, cross-wavelet, wavelet
    coherence, phase difference — numeric grids).

    Category 27-frequency-domain; memory class ``heavy``.

    Args:
        df: [df_handle, required] Handle to a DataFrame with >= 2 numeric, ALIGNED series (complete,
            same length, equally spaced samples).
        x: [string, optional] Column name of the 1st series (default: 1st numeric column).
        y: [string, optional] Column name of the 2nd series, x != y (default: 2nd numeric column).
        dt: [number, optional] Sampling time step (default 1). Default ``1``.
        dj: [number, optional] Scale voice spacing (default 1/20). Default ``0.05``.
        lower_period: [number, optional] Lower period (>= 2*dt)· default 2*dt.
        upper_period: [number, optional] Upper period (<= n*dt)· default floor(n/3)*dt.
        loess_span: [number, optional] Loess span for detrending in [0,1] (default 0.75). Default
            ``0.75``.
        window_size_t: [number, optional] Smoothing window size in time for coherence (default 5).
            Default ``5``.
        window_size_s: [number, optional] Smoothing window size in scale for coherence (default
            1/4). Default ``0.25``.
        make_pval: [boolean, optional] Surrogate p-values for cross-power & coherence (default
            True). Default ``True``.
        method: [enum, optional] Null model surrogate (default white.noise· see wv_transform).
        n_sim: [integer, optional] Number of surrogate simulations (>= 1 if make_pval=True· default
            10). Default ``10``.
        seed: [integer, optional] Seed before the surrogate simulation (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "wv_coherency: not implemented."
    )
