# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``conditional_forecasts`` -- method card #417.

#417 Conditional forecasts and scenario analysis

Category 03-multivariate-nowcasting; module ``conditional_forecasts``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_conditional_forecast",
    "NODE_META",
    "wire_model",
]


def mn_conditional_forecast(
    *,
    fit: Any,
    conditions: pd.DataFrame,
    h: int,
    method: Literal["hard", "soft"] | None = None,
    shocks: Sequence[str] | None = None,
    levels: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``mn_conditional_forecast`` -- method card #417.

    Conditional forecasts and scenario analysis.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted multivariate model.
        conditions: [df_handle, required] Conditioning paths, one column per constrained variable.
        h: [integer, required] Forecast horizon.
        method: [enum, optional] Conditioning scheme. Default ``'hard'``.
        shocks: [series_codes, optional] Shocks used to achieve the conditioning.
        levels: [num_array, optional] Prediction interval levels. Default ``[0.68, 0.9]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mn_conditional_forecast: not implemented."
    )
