# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``event_study`` -- method card #322.

#322 Financial event studies: abnormal returns, CAR and BHAR

Category 37-asset-pricing-factors; module ``event_study``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c37_asset_pricing_factors import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ap_car_test",
    "ap_event_study",
    "NODE_META",
    "wire_model",
]


def ap_event_study(
    *,
    returns: pd.DataFrame,
    events: pd.DataFrame,
    market: pd.Series | None = None,
    model: Literal["market", "market_adjusted", "mean_adjusted", "fama_french"] | None = None,
    estimation_window: Sequence[int] | None = None,
    event_window: Sequence[int] | None = None,
) -> dict[str, Any]:
    """Node ``ap_event_study`` -- method card #322.

    Financial event studies: abnormal returns, CAR and BHAR.

    Category 37-asset-pricing-factors; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        returns: [df_handle, required] Panel of asset returns.
        events: [df_handle, required] Event table: asset identifier and event date.
        market: [series_handle, optional] Market return for the normal-return model.
        model: [enum, optional] Normal-return model. Default ``'market'``.
        estimation_window: [int_array, optional] Estimation window offsets. Default ``[-250, -30]``.
        event_window: [int_array, optional] Event window offsets. Default ``[-5, 5]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_event_study: not implemented."
    )


def ap_car_test(
    *,
    fit: Any,
    aggregation: Literal["car", "bhar"] | None = None,
    test: Literal["patell", "boehmer", "rank", "sign", "crude"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_car_test`` -- method card #322.

    Financial event studies: abnormal returns, CAR and BHAR.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted event study.
        aggregation: [enum, optional] Aggregation over the window. Default ``'car'``.
        test: [enum, optional] Test statistic. Default ``'patell'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_car_test: not implemented."
    )
