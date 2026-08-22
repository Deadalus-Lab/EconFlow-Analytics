# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``price_impact`` -- method card #335.

#335 Kyle's lambda, Hasbrouck's lambda and price impact

Category 39-market-microstructure; module ``price_impact``.

Reference implementation: frds.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c39_market_microstructure import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ms_hasbrouck_lambda",
    "ms_kyle_lambda",
    "NODE_META",
    "wire_model",
]


def ms_kyle_lambda(
    *,
    returns: pd.Series,
    signed_volume: pd.Series,
    window: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ms_kyle_lambda`` -- method card #335.

    Kyle's lambda, Hasbrouck's lambda and price impact.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        returns: [series_handle, required] Returns at the sampling frequency.
        signed_volume: [series_handle, required] Signed order flow.
        window: [integer, optional] Rolling window; omitted = full sample.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_kyle_lambda: not implemented."
    )


def ms_hasbrouck_lambda(
    *,
    returns: pd.Series,
    signed_trades: pd.Series,
    lags: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_hasbrouck_lambda`` -- method card #335.

    Kyle's lambda, Hasbrouck's lambda and price impact.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        returns: [series_handle, required] Quote-midpoint returns.
        signed_trades: [series_handle, required] Signed trade indicator or volume.
        lags: [integer, optional] VAR lag order. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_hasbrouck_lambda: not implemented."
    )
