# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spectral_periodogram_quick`` -- method card #236.

#236 Spectral / periodogram quick look (a smoothed periodogram, the high-level spectrum pgram|AR, a
    numeric cumulative periodogram + KS white-noise bands)

Category 27-frequency-domain; module ``spectral_periodogram_quick``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "spec_cumulative_periodogram",
    "spec_periodogram",
    "spec_spectrum",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def spec_periodogram(
    *,
    x: pd.Series,
    spans: Sequence[int] | None = None,
    taper: float | None = None,
    pad: float | None = None,
    fast: bool | None = None,
    demean: bool | None = None,
    detrend: bool | None = None,
) -> dict[str, Any]:
    """Node ``spec_periodogram`` -- method card #236.

    Spectral / periodogram quick look (a smoothed periodogram, the high-level spectrum pgram|AR, a
    numeric cumulative periodogram + KS white-noise bands).

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to A SINGLE univariate series (a stored ts or
            single-series DataFrame); >= 4 observations, without NA.
        spans: [int_array, optional] Widths of modified Daniell smoothers — vector of ODD positive
            integers (e.g. [3,5]); None = raw (unsmoothed) periodogram. CAUTION: even spans are
            blocked (silent-wrong smoother).
        taper: [number, optional] Percentage of split-cosine-bell taper at each end, in [0, 0.5]
            (default 0.1). Default ``0.1``.
        pad: [number, optional] Zero-padding as a percentage of the length (>= 0; default 0).
            Default ``0``.
        fast: [boolean, optional] Padding to a highly-composite length for a fast FFT (default
            True). Default ``True``.
        demean: [boolean, optional] Removal of the mean before the FFT (default False). Default
            ``False``.
        detrend: [boolean, optional] Removal of a linear trend before the FFT (default True).
            Default ``True``.

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
        "spec_periodogram: not implemented."
    )


def spec_spectrum(
    *,
    x: pd.Series,
    method: Literal["pgram", "ar"] | None = None,
    spans: Sequence[int] | None = None,
    taper: float | None = None,
    order: int | None = None,
    n_freq: int | None = None,
) -> dict[str, Any]:
    """Node ``spec_spectrum`` -- method card #236.

    Spectral / periodogram quick look (a smoothed periodogram, the high-level spectrum pgram|AR, a
    numeric cumulative periodogram + KS white-noise bands).

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to A SINGLE univariate series (ts or single-series df);
            >= 4 observations, without NA.
        method: [enum, optional] Spectrum estimator (default pgram): pgram=(smoothed) periodogram;
            ar=autoregressive (Yule-Walker) smooth spectral density.
        spans: [int_array, optional] method='pgram': modified Daniell smoothers (odd positive
            integers); otherwise None.
        taper: [number, optional] method='pgram': split-cosine-bell taper in [0, 0.5] (default 0.1).
            Default ``0.1``.
        order: [integer, optional] method='ar': AR order (non-negative integer); None = auto
            selection via AIC.
        n_freq: [integer, optional] method='ar': number of frequency points of the estimate
            (positive integer; default 500). Default ``500``.

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
        "spec_spectrum: not implemented."
    )


def spec_cumulative_periodogram(
    *,
    x: pd.Series,
    taper: float | None = None,
) -> dict[str, Any]:
    """Node ``spec_cumulative_periodogram`` -- method card #236.

    Spectral / periodogram quick look (a smoothed periodogram, the high-level spectrum pgram|AR, a
    numeric cumulative periodogram + KS white-noise bands).

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to A SINGLE univariate series (ts or single-series df);
            >= 4 observations, without NA.
        taper: [number, optional] Split-cosine-bell taper in [0, 0.5] (default 0.1, as in the
            cumulative-periodogram routine). Default ``0.1``.

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
        "spec_cumulative_periodogram: not implemented."
    )
