# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``kalman_filter_smoother`` -- METHOD-SELECTION card #58.

#58 Kalman filter/smoother + unobserved-components models

Category 10-trend-cycle-statespace; module ``kalman_filter_smoother``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "kf_forecast",
    "kf_local_level",
    "kf_local_linear_trend",
    "kf_trend_cycle",
    "NODE_META",
    "wire_model",
]


def kf_local_level(
    *,
    y: pd.Series,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``kf_local_level`` -- METHOD-SELECTION card #58.

    Kalman filter/smoother + unobserved-components models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· local level (level random walk).
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "kf_local_level: not implemented. The method card is in ./README.md."
    )


def kf_local_linear_trend(
    *,
    y: pd.Series,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``kf_local_linear_trend`` -- METHOD-SELECTION card #58.

    Kalman filter/smoother + unobserved-components models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· local linear trend (level + slope).
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "kf_local_linear_trend: not implemented. The method card is in ./README.md."
    )


def kf_trend_cycle(
    *,
    y: pd.Series,
    cycle_period: float | None = None,
    seasonal: bool | None = None,
    seasonal_period: int | None = None,
) -> dict[str, Any]:
    """Node ``kf_trend_cycle`` -- METHOD-SELECTION card #58.

    Kalman filter/smoother + unobserved-components models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts· trend + stochastic cycle (output
            gap).
        cycle_period: [number, optional] Cycle length in periods (> 2)· default 8*frequency.
        seasonal: [boolean, optional] Add a dummy seasonal term. Default ``False``.
        seasonal_period: [integer, optional] Seasonal period (>=2, <=n)· default frequency(y).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "kf_trend_cycle: not implemented. The method card is in ./README.md."
    )


def kf_forecast(
    *,
    object: Any,
    n_ahead: int | None = None,
    interval: Literal["prediction", "confidence", "none"] | None = None,
    level: float | None = None,
) -> dict[str, Any]:
    """Node ``kf_forecast`` -- METHOD-SELECTION card #58.

    Kalman filter/smoother + unobserved-components models.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted SSModel (the model from
            kf_local_level/.../kf_trend_cycle).
        n_ahead: [integer, optional] Forecast horizon (positive integer). Default ``8``.
        interval: [enum, optional] Interval type (default prediction).
        level: [number, optional] Confidence level ∈ (0,1). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "kf_forecast: not implemented. The method card is in ./README.md."
    )
