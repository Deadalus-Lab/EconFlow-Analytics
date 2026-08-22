# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``price_discovery`` -- method card #339.

#339 Effective and realised spreads and price discovery

Category 39-market-microstructure; module ``price_discovery``.

Reference implementation: statsmodels.

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
    "ms_component_share",
    "ms_information_share",
    "ms_spread_decomposition",
    "NODE_META",
    "wire_model",
]


def ms_spread_decomposition(
    *,
    price: pd.Series,
    midpoint: pd.Series,
    direction: pd.Series,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_spread_decomposition`` -- method card #339.

    Effective and realised spreads and price discovery.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        price: [series_handle, required] Trade price.
        midpoint: [series_handle, required] Prevailing quote midpoint.
        direction: [series_handle, required] Signed trade direction.
        horizon: [integer, optional] Periods ahead for the post-trade midpoint. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_spread_decomposition: not implemented."
    )


def ms_information_share(
    *,
    prices: pd.DataFrame,
    lags: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_information_share`` -- method card #339.

    Effective and realised spreads and price discovery.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        prices: [multiseries_handle, required] Price series, one column per venue.
        lags: [integer, optional] VECM lag order. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_information_share: not implemented."
    )


def ms_component_share(
    *,
    prices: pd.DataFrame,
    lags: int | None = None,
) -> dict[str, Any]:
    """Node ``ms_component_share`` -- method card #339.

    Effective and realised spreads and price discovery.

    Category 39-market-microstructure; memory class ``light``.

    Args:
        prices: [multiseries_handle, required] Price series, one column per venue.
        lags: [integer, optional] VECM lag order. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ms_component_share: not implemented."
    )
