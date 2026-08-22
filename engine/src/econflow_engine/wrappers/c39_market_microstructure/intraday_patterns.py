# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``intraday_patterns`` -- method card #338.

#338 Intraday volatility patterns, signature plots and optimal sampling

Category 39-market-microstructure; module ``intraday_patterns``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_intraday_periodicity",
    "ms_signature_plot",
    "NODE_META",
    "wire_model",
]


def ms_signature_plot(
    *,
    prices: pd.Series,
    intervals: Sequence[int] | None = None,
) -> dict[str, Any]:
    """Node ``ms_signature_plot`` -- method card #338.

    Intraday volatility patterns, signature plots and optimal sampling.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        prices: [irregular_series_handle, required] Intraday price series.
        intervals: [int_array, optional] Sampling intervals in seconds to scan. Default ``[5, 10,
            30, 60, 300, 600, 1800]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_signature_plot: not implemented."
    )


def ms_intraday_periodicity(
    *,
    returns: pd.Series,
    method: Literal["mean_absolute", "wsd", "shortest_half", "trimmed_mean"] | None = None,
    bins_per_day: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_intraday_periodicity`` -- method card #338.

    Intraday volatility patterns, signature plots and optimal sampling.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        returns: [irregular_series_handle, required] Intraday returns.
        method: [enum, optional] Periodicity estimator. Default ``'wsd'``.
        bins_per_day: [integer, optional] Intraday bins per trading day. Default ``78``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_intraday_periodicity: not implemented."
    )
