# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stl_decomposition_tolerant`` -- method card #188.

#188 STL decomposition (seasonal-trend-loess) tolerant of gaps and short series

Category 10-trend-cycle-statespace; module ``stl_decomposition_tolerant``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "stl_tolerant_decompose",
    "NODE_META",
    "wire_model",
]


def stl_tolerant_decompose(
    *,
    x: pd.Series,
    n_p: int | None = None,
    s_window: str | None = None,
    t_window: int | None = None,
    s_degree: int | None = None,
    t_degree: int | None = None,
    inner: int | None = None,
    outer: int | None = None,
) -> dict[str, Any]:
    """Node ``stl_tolerant_decompose`` -- method card #188.

    STL decomposition (seasonal-trend-loess) tolerant of gaps and short series.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate ts (or num_array)· STL loess
            decomposition· tolerates NA.
        n_p: [integer, optional] Seasonality period (integer >= 2)· None -> frequency(x) if x is a
            seasonal ts.
        s_window: [string, optional] "periodic" (default, constant seasonality) or a positive odd
            integer >= 7 (seasonal loess span). Default ``'periodic'``.
        t_window: [integer, optional] Trend loess span (positive odd integer >= 3)· None -> computed
            automatically.
        s_degree: [integer, optional] Seasonal loess degree ∈ {0,1,2}. Default ``1``.
        t_degree: [integer, optional] Trend loess degree ∈ {0,1,2}. Default ``1``.
        inner: [integer, optional] Inner-loop iterations (positive integer). Default ``2``.
        outer: [integer, optional] Outer-loop (robustness) iterations (non-negative integer).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "stl_tolerant_decompose: not implemented."
    )
