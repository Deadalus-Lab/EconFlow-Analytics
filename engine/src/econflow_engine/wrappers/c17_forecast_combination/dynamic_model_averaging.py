# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_model_averaging`` -- method card #532.

#532 Dynamic model averaging and dynamic model selection

Category 17-forecast-combination; module ``dynamic_model_averaging``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fc_dynamic_model_averaging",
    "NODE_META",
    "wire_model",
]


def fc_dynamic_model_averaging(
    *,
    actual: pd.Series,
    forecasts: pd.DataFrame,
    forgetting_weights: float | None = None,
    forgetting_variance: float | None = None,
    mode: Literal["averaging", "selection"] | None = None,
) -> dict[str, Any]:
    """Node ``fc_dynamic_model_averaging`` -- method card #532.

    Dynamic model averaging and dynamic model selection.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecasts: [df_handle, required] Forecasts, one column per model.
        forgetting_weights: [number, optional] Forgetting factor on model probabilities. Default
            ``0.99``.
        forgetting_variance: [number, optional] Forgetting factor on the variance. Default ``0.95``.
        mode: [enum, optional] Averaging or selection. Default ``'averaging'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fc_dynamic_model_averaging: not implemented."
    )
