# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``wavelet_time_frequency`` -- METHOD-SELECTION card #235.

#235 Wavelet time-frequency analysis (the Morlet CWT: power spectrum, cross-wavelet, wavelet
    coherence, phase difference — numeric grids)

Category 27-frequency-domain; module ``wavelet_time_frequency``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wv_coherency",
    "wv_wavelet",
    "NODE_META",
    "wire_model",
]


def wv_wavelet(
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
    """Node ``wv_wavelet`` -- METHOD-SELECTION card #235.

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
    """
    raise NotImplementedError(
        "wv_wavelet: not implemented. The method card is in ./README.md."
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
    """Node ``wv_coherency`` -- METHOD-SELECTION card #235.

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
        method: [enum, optional] Null model surrogate (default white.noise· see wv_wavelet).
        n_sim: [integer, optional] Number of surrogate simulations (>= 1 if make_pval=True· default
            10). Default ``10``.
        seed: [integer, optional] Seed before the surrogate simulation (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wv_coherency: not implemented. The method card is in ./README.md."
    )
