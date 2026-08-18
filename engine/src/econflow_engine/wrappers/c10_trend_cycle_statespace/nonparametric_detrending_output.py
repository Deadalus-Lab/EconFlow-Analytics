# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonparametric_detrending_output`` -- METHOD-SELECTION card #189.

#189 Nonparametric detrending & output gap (loess / smoothing spline / Friedman super-smoother)

Category 10-trend-cycle-statespace; module ``nonparametric_detrending_output``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_detrend",
    "np_output_gap",
    "NODE_META",
    "wire_model",
]


def np_detrend(
    *,
    y: Sequence[float],
    x: Sequence[float] | None = None,
    method: Literal["loess", "smooth.spline", "supsmu"] | None = None,
    span: float | None = None,
    degree: int | None = None,
    spar: float | None = None,
    cv: bool | None = None,
) -> dict[str, Any]:
    """Node ``np_detrend`` -- METHOD-SELECTION card #189.

    Nonparametric detrending & output gap (loess / smoothing spline / Friedman super-smoother).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [num_array, required] The series (numeric vector, e.g. 100*log(GDP))· without NA, n>=4·
            cycle = y - trend.
        x: [num_array, optional] Optional numeric index of the same length (None -> 1..n).
        method: [enum, optional] Non-parametric smoother (default loess):
            loess/smooth.spline/supsmu.
        span: [number, optional] Smoothing fraction ∈ [0,1] for loess/supsmu (loess: >0)· default
            0.75. Default ``0.75``.
        degree: [integer, optional] loess local polynomial 0/1/2 (default 2). Default ``2``.
        spar: [number, optional] smooth.spline smoothing parameter ∈ (0,1.5]· None -> automatic GCV.
        cv: [boolean, optional] smooth.spline: True -> LOOCV instead of GCV (ignored if spar is
            given). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_detrend: not implemented. The method card is in ./README.md."
    )


def np_output_gap(
    *,
    y: Sequence[float],
    x: Sequence[float] | None = None,
    method: Literal["loess", "smooth.spline", "supsmu"] | None = None,
    mode: Literal["pct", "log", "level"] | None = None,
    span: float | None = None,
    degree: int | None = None,
    spar: float | None = None,
    cv: bool | None = None,
) -> dict[str, Any]:
    """Node ``np_output_gap`` -- METHOD-SELECTION card #189.

    Nonparametric detrending & output gap (loess / smoothing spline / Friedman super-smoother).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [num_array, required] The series (numeric vector)· without NA, n>=4· gap = deviation from
            the non-parametric trend.
        x: [num_array, optional] Optional numeric index of the same length (None -> 1..n).
        method: [enum, optional] Non-parametric trend smoother (default loess).
        mode: [enum, optional] pct=100*(y-trend)/trend (default)· log=100*(log y - log trend),
            y&trend>0· level=y-trend.
        span: [number, optional] Smoothing fraction ∈ [0,1] for loess/supsmu (loess: >0)· default
            0.75. Default ``0.75``.
        degree: [integer, optional] loess local polynomial 0/1/2 (default 2). Default ``2``.
        spar: [number, optional] smooth.spline smoothing parameter ∈ (0,1.5]· None -> automatic GCV.
        cv: [boolean, optional] smooth.spline: True -> LOOCV instead of GCV (ignored if spar is
            given). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_output_gap: not implemented. The method card is in ./README.md."
    )
