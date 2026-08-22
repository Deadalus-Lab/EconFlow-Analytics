# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hierarchical_grouped_reconciliation`` -- method card #209.

#209 Tidy hierarchical/grouped forecast reconciliation (aggregate_key + MinT/bottom_up) in the
    long-format forecasting framework

Category 17-forecast-combination; module ``hierarchical_grouped_reconciliation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

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
    "reconcile_grouped",
    "NODE_META",
    "wire_model",
]


def reconcile_grouped(
    *,
    data: pd.DataFrame,
    index: str,
    keys: Sequence[str],
    value: str,
    structure: Literal["nested", "grouped"] | None = None,
    base_model: Literal["arima", "ets", "snaive"] | None = None,
    method: (
        Literal[
            "wls_struct",
            "ols",
            "wls_var",
            "mint_shrink",
            "mint_cov",
            "bottom_up",
        ]
        | None
    ) = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``reconcile_grouped`` -- method card #209.

    Tidy hierarchical/grouped forecast reconciliation (aggregate_key + MinT/bottom_up) in the
    long-format forecasting framework.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long-format DataFrame (index column + >=1 key
            columns + numeric value column).
        index: [string, required] Time column name (valid series index:
            Date/yearmonth/yearquarter/numeric).
        keys: [series_codes, required] Key/grouping column names (>=1; they define the hierarchy's
            nodes); grouped requires >=2.
        value: [string, required] Measured numeric column name (without NA; summed into the
            aggregates).
        structure: [enum, optional] Structure: nested (grp1/grp2 hierarchy) or grouped (grp1*grp2
            crossed; default nested).
        base_model: [enum, optional] Base model per node (ARIMA/ETS/SNAIVE; default arima).
        method: [enum, optional] Reconciliation: min_trace(method) MinT variants or bottom_up
            (default wls_struct — robust structural MinT).
        h: [integer, optional] Forecast horizon (positive integer; default 8). Default ``8``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "reconcile_grouped: not implemented."
    )
