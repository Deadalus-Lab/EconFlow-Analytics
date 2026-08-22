# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``robust_optimisation`` -- method card #330.

#330 Robust and worst-case optimisation with uncertainty sets

Category 38-portfolio-allocation; module ``robust_optimisation``.

Reference implementation: cvxpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c38_portfolio_allocation import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_robust_optimise",
    "NODE_META",
    "wire_model",
]


def pf_robust_optimise(
    *,
    returns: pd.DataFrame,
    uncertainty: Literal["box", "ellipsoidal", "budget"] | None = None,
    size: float | None = None,
    objective: Literal["max_worst_case_return", "min_worst_case_risk"] | None = None,
    bounds: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``pf_robust_optimise`` -- method card #330.

    Robust and worst-case optimisation with uncertainty sets.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        uncertainty: [enum, optional] Uncertainty-set geometry. Default ``'ellipsoidal'``.
        size: [number, optional] Uncertainty radius. Default ``1.0``.
        objective: [enum, optional] Objective. Default ``'max_worst_case_return'``.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pf_robust_optimise: not implemented."
    )
