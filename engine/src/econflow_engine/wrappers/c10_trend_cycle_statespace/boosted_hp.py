# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``boosted_hp`` -- method card #480.

#480 Boosted Hodrick-Prescott filter

Category 10-trend-cycle-statespace; module ``boosted_hp``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_boosted_hp",
    "NODE_META",
    "wire_model",
]


def tc_boosted_hp(
    *,
    y: pd.Series,
    lamb: float | None = None,
    stopping: Literal["bic", "aic", "adf", "max_iter"] | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``tc_boosted_hp`` -- method card #480.

    Boosted Hodrick-Prescott filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        lamb: [number, optional] Smoothing parameter. Default ``1600.0``.
        stopping: [enum, optional] Stopping rule. Default ``'bic'``.
        max_iter: [integer, optional] Maximum boosting rounds. Default ``100``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tc_boosted_hp: not implemented."
    )
