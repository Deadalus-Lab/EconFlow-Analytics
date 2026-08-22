# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``temporal_hierarchy`` -- method card #534.

#534 Temporal-hierarchy combination: MAPA and THieF

Category 17-forecast-combination; module ``temporal_hierarchy``.

Reference implementation: hierarchicalforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fc_temporal_hierarchy",
    "NODE_META",
    "wire_model",
]


def fc_temporal_hierarchy(
    *,
    y: pd.Series,
    h: int,
    levels: Sequence[int] | None = None,
    base_model: Literal["auto_arima", "auto_ets", "theta", "naive"] | None = None,
    reconciliation: Literal["ols", "wls_struct", "wls_var", "mint_shrink"] | None = None,
) -> dict[str, Any]:
    """Node ``fc_temporal_hierarchy`` -- method card #534.

    Temporal-hierarchy combination: MAPA and THieF.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        y: [series_handle, required] Series at the highest frequency.
        h: [integer, required] Forecast horizon at the base frequency.
        levels: [int_array, optional] Aggregation levels; omitted = divisors of the season.
        base_model: [enum, optional] Model fitted at each level. Default ``'auto_ets'``.
        reconciliation: [enum, optional] Reconciliation method. Default ``'wls_struct'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fc_temporal_hierarchy: not implemented."
    )
