# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``beveridge_nelson`` -- method card #476.

#476 Beveridge-Nelson decomposition and the BN filter

Category 10-trend-cycle-statespace; module ``beveridge_nelson``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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
    "tc_beveridge_nelson",
    "NODE_META",
    "wire_model",
]


def tc_beveridge_nelson(
    *,
    y: pd.Series,
    order: Sequence[int] | None = None,
    filter: bool | None = None,
    delta: float | None = None,
) -> dict[str, Any]:
    """Node ``tc_beveridge_nelson`` -- method card #476.

    Beveridge-Nelson decomposition and the BN filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series, usually in logs.
        order: [int_array, optional] ARIMA order; omitted = selected.
        filter: [boolean, optional] Use the BN filter with a persistence prior. Default ``False``.
        delta: [number, optional] Persistence prior for the BN filter. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tc_beveridge_nelson: not implemented."
    )
