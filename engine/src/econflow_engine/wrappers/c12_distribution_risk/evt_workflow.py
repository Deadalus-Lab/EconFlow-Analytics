# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``evt_workflow`` -- method card #493.

#493 Extreme value workflow: threshold selection, mean residual life and return levels

Category 12-distribution-risk; module ``evt_workflow``.

Reference implementation: pyextremes.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_evt_fit",
    "dr_evt_threshold",
    "NODE_META",
    "wire_model",
]


def dr_evt_threshold(
    *,
    x: pd.Series,
    thresholds: Sequence[float] | None = None,
    min_exceedances: int | None = None,
) -> dict[str, Any]:
    """Node ``dr_evt_threshold`` -- method card #493.

    Extreme value workflow: threshold selection, mean residual life and return levels.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        x: [series_handle, required] Data, usually losses.
        thresholds: [num_array, optional] Candidate thresholds; omitted = a quantile grid.
        min_exceedances: [integer, optional] Minimum exceedances required. Default ``30``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_evt_threshold: not implemented."
    )


def dr_evt_fit(
    *,
    x: pd.Series,
    method: Literal["pot", "block_maxima"] | None = None,
    threshold: float | None = None,
    block_size: int | None = None,
    return_periods: Sequence[float] | None = None,
    interval: Literal["delta", "profile", "bootstrap"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``dr_evt_fit`` -- method card #493.

    Extreme value workflow: threshold selection, mean residual life and return levels.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Data, usually losses.
        method: [enum, optional] Approach. Default ``'pot'``.
        threshold: [number, optional] Threshold for peaks over threshold.
        block_size: [integer, optional] Block size for block maxima.
        return_periods: [num_array, optional] Return periods to report. Default ``[10.0, 50.0,
            100.0]``.
        interval: [enum, optional] Interval method. Default ``'profile'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_evt_fit: not implemented."
    )
