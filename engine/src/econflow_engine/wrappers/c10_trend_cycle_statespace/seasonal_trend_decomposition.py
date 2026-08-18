# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``seasonal_trend_decomposition`` -- METHOD-SELECTION card #187.

#187 Seasonal-Trend decomposition using Regression (AutoSTR) — trend + multiple/complex seasonality
    + remainder with CIs per component

Category 10-trend-cycle-statespace; module ``seasonal_trend_decomposition``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "str_decompose",
    "str_seasadj",
    "NODE_META",
    "wire_model",
]


def str_decompose(
    *,
    y: pd.Series,
    frequency: int | None = None,
    robust: bool | None = None,
    gapCV: int | None = None,
    confidence: float | None = None,
    lambdas: Sequence[float] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``str_decompose`` -- METHOD-SELECTION card #187.

    Seasonal-Trend decomposition using Regression (AutoSTR) — trend + multiple/complex seasonality +
    remainder with CIs per component.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts (or msts for multiple/complex
            seasonality)· the series to decompose.
        frequency: [integer, optional] Seasonal frequency (>=2) when y is a numeric vector· ignored
            for ts/msts.
        robust: [boolean, optional] Robust STR (M-estimation) — True when outliers/level shifts are
            present. Default ``False``.
        gapCV: [integer, optional] Gap length for the CV selection of lambdas· larger ->
            faster/coarser (None = package default).
        confidence: [number, optional] Confidence level ∈ (0,1) for per-component CIs· None =
            without CIs (faster). Default ``0.95``.
        lambdas: [num_array, optional] Fixed smoothing parameters (they bypass the CV)· None = auto
            via gapCV.
        seed: [integer, optional] Determinism seed for the stochastic CV selection of lambdas.
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "str_decompose: not implemented. The method card is in ./README.md."
    )


def str_seasadj(
    *,
    object: Any,
    include: Any | None = None,
) -> dict[str, Any]:
    """Node ``str_seasadj`` -- METHOD-SELECTION card #187.

    Seasonal-Trend decomposition using Regression (AutoSTR) — trend + multiple/complex seasonality +
    remainder with CIs per component.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an STR object (str_decompose$object).
        include: [raw, optional] Names of the components that are summed (character vector)· None =
            ["Trend","Random"] = seasonally-adjusted.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "str_seasadj: not implemented. The method card is in ./README.md."
    )
