# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``var_backtesting`` -- method card #491.

#491 VaR and ES backtesting: Kupiec, Christoffersen, dynamic quantile and traffic light

Category 12-distribution-risk; module ``var_backtesting``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_var_backtest",
    "NODE_META",
    "wire_model",
]


def dr_var_backtest(
    *,
    returns: pd.Series,
    var_forecast: pd.Series,
    es_forecast: pd.Series | None = None,
    confidence: float | None = None,
    tests: Sequence[str] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``dr_var_backtest`` -- method card #491.

    VaR and ES backtesting: Kupiec, Christoffersen, dynamic quantile and traffic light.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        returns: [series_handle, required] Realised returns.
        var_forecast: [series_handle, required] Forecast value at risk.
        es_forecast: [series_handle, optional] Forecast expected shortfall.
        confidence: [number, optional] Tail level of the forecasts. Default ``0.99``.
        tests: [series_codes, optional] Tests to run; omitted = the standard set.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dr_var_backtest: not implemented."
    )
