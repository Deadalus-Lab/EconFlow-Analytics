# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``portfolio_sorts`` -- method card #320.

#320 Portfolio sorts and characteristic-managed portfolios

Category 37-asset-pricing-factors; module ``portfolio_sorts``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_double_sort",
    "ap_portfolio_sort",
    "NODE_META",
    "wire_model",
]


def ap_portfolio_sort(
    *,
    returns: pd.DataFrame,
    characteristic: pd.DataFrame,
    n_portfolios: int | None = None,
    weighting: Literal["equal", "value"] | None = None,
    market_cap: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``ap_portfolio_sort`` -- method card #320.

    Portfolio sorts and characteristic-managed portfolios.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [df_handle, required] Panel of asset returns.
        characteristic: [df_handle, required] Panel of the sorting characteristic, lagged.
        n_portfolios: [integer, optional] Number of sort bins. Default ``5``.
        weighting: [enum, optional] Within-portfolio weighting. Default ``'equal'``.
        market_cap: [df_handle, optional] Panel of market values for value weighting.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_portfolio_sort: not implemented."
    )


def ap_double_sort(
    *,
    returns: pd.DataFrame,
    characteristic_1: pd.DataFrame,
    characteristic_2: pd.DataFrame,
    n_1: int | None = None,
    n_2: int | None = None,
    conditional: bool | None = None,
) -> dict[str, Any]:
    """Node ``ap_double_sort`` -- method card #320.

    Portfolio sorts and characteristic-managed portfolios.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [df_handle, required] Panel of asset returns.
        characteristic_1: [df_handle, required] First sorting characteristic.
        characteristic_2: [df_handle, required] Second sorting characteristic.
        n_1: [integer, optional] Bins on the first characteristic. Default ``5``.
        n_2: [integer, optional] Bins on the second characteristic. Default ``5``.
        conditional: [boolean, optional] Sort on the second within the first. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_double_sort: not implemented."
    )
