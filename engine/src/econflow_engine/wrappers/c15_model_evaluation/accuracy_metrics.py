# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``accuracy_metrics`` -- method card #513.

#513 Point-accuracy metric table across horizons and series

Category 15-model-evaluation; module ``accuracy_metrics``.

Reference implementation: utilsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_accuracy_table",
    "NODE_META",
    "wire_model",
]


def me_accuracy_table(
    *,
    actual: pd.DataFrame,
    forecast: pd.DataFrame,
    metrics: Sequence[str] | None = None,
    insample: pd.DataFrame | None = None,
    season_length: int | None = None,
    by: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``me_accuracy_table`` -- method card #513.

    Point-accuracy metric table across horizons and series.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [df_handle, required] Realised values.
        forecast: [df_handle, required] Forecasts, one column per method.
        metrics: [series_codes, optional] Metrics to compute; omitted = the standard set.
        insample: [df_handle, optional] In-sample series for the scaled metrics.
        season_length: [integer, optional] Seasonal period for MASE. Default ``1``.
        by: [series_codes, optional] Grouping columns for the table.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "me_accuracy_table: not implemented."
    )
