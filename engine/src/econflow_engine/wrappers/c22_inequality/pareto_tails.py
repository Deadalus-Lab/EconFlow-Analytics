# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``pareto_tails`` -- method card #559.

#559 Top incomes and Pareto tails

Category 22-inequality; module ``pareto_tails``.

Reference implementation: powerlaw.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_pareto_tail",
    "NODE_META",
    "wire_model",
]


def iq_pareto_tail(
    *,
    income: pd.Series,
    weights: pd.Series | None = None,
    threshold: float | None = None,
    method: Literal["hill", "mle", "gpd_interpolation", "regression"] | None = None,
    top_shares: Sequence[float] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``iq_pareto_tail`` -- method card #559.

    Top incomes and Pareto tails.

    Category 22-inequality; memory class ``light``.

    Args:
        income: [series_handle, required] Income or wealth.
        weights: [series_handle, optional] Survey weights.
        threshold: [number, optional] Tail threshold; omitted = selected.
        method: [enum, optional] Estimator. Default ``'hill'``.
        top_shares: [num_array, optional] Top shares to report. Default ``[0.1, 0.01, 0.001]``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iq_pareto_tail: not implemented."
    )
