# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``realtime_evaluation`` -- method card #566.

#566 Real-time forecast evaluation conventions

Category 23-real-time-revisions; module ``realtime_evaluation``.

Reference implementation: utilsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c23_real_time_revisions import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rt_realtime_evaluation",
    "NODE_META",
    "wire_model",
]


def rt_realtime_evaluation(
    *,
    forecasts: pd.DataFrame,
    vintages: pd.DataFrame,
    conventions: Sequence[str] | None = None,
    fixed_lag: int | None = None,
    metrics: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``rt_realtime_evaluation`` -- method card #566.

    Real-time forecast evaluation conventions.

    Category 23-real-time-revisions; memory class ``light``.

    Args:
        forecasts: [df_handle, required] Forecasts by origin and horizon.
        vintages: [df_handle, required] Vintage data.
        conventions: [series_codes, optional] Conventions to evaluate; omitted = all three.
        fixed_lag: [integer, optional] Periods after first release for the fixed-lag convention.
            Default ``12``.
        metrics: [series_codes, optional] Metrics to compute.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rt_realtime_evaluation: not implemented."
    )
