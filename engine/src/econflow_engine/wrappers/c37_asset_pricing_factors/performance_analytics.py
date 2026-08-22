# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``performance_analytics`` -- method card #323.

#323 Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover

Category 37-asset-pricing-factors; module ``performance_analytics``.

Reference implementation: ffn.

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
    "ap_drawdown",
    "ap_performance_summary",
    "ap_turnover",
    "NODE_META",
    "wire_model",
]


def ap_performance_summary(
    *,
    returns: pd.Series,
    benchmark: pd.Series | None = None,
    risk_free: pd.Series | None = None,
    frequency: Literal["daily", "weekly", "monthly", "quarterly", "annual"] | None = None,
    autocorrelation_adjust: bool | None = None,
) -> dict[str, Any]:
    """Node ``ap_performance_summary`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [series_handle, required] Portfolio return series.
        benchmark: [series_handle, optional] Benchmark return series.
        risk_free: [series_handle, optional] Risk-free rate series.
        frequency: [enum, optional] Return frequency for annualisation. Default ``'monthly'``.
        autocorrelation_adjust: [boolean, optional] Apply the Lo autocorrelation correction. Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_performance_summary: not implemented."
    )


def ap_drawdown(
    *,
    returns: pd.Series,
    top_n: int | None = None,
) -> dict[str, Any]:
    """Node ``ap_drawdown`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        returns: [series_handle, required] Portfolio return series.
        top_n: [integer, optional] Number of largest drawdowns to report. Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_drawdown: not implemented."
    )


def ap_turnover(
    *,
    weights: pd.DataFrame,
    cost_bps: float | None = None,
) -> dict[str, Any]:
    """Node ``ap_turnover`` -- method card #323.

    Performance analytics: Sharpe, Sortino, information ratio, drawdown and turnover.

    Category 37-asset-pricing-factors; memory class ``light``.

    Args:
        weights: [df_handle, required] Panel of portfolio weights over time.
        cost_bps: [number, optional] Round-trip cost in basis points. Default ``10.0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ap_turnover: not implemented."
    )
