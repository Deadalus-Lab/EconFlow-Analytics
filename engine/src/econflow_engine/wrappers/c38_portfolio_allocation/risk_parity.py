# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``risk_parity`` -- method card #327.

#327 Risk parity, equal risk contribution and risk budgeting

Category 38-portfolio-allocation; module ``risk_parity``.

Reference implementation: riskfolio-lib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c38_portfolio_allocation import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pf_risk_contributions",
    "pf_risk_parity",
    "NODE_META",
    "wire_model",
]


def pf_risk_parity(
    *,
    returns: pd.DataFrame,
    budget: Sequence[float] | None = None,
    risk_measure: Literal["variance", "mad", "cvar", "cdar", "evar"] | None = None,
    bounds: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``pf_risk_parity`` -- method card #327.

    Risk parity, equal risk contribution and risk budgeting.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        budget: [num_array, optional] Target risk shares; omitted = equal.
        risk_measure: [enum, optional] Risk measure the contributions are defined on. Default
            ``'variance'``.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pf_risk_parity: not implemented."
    )


def pf_risk_contributions(
    *,
    weights: pd.Series,
    covariance: np.ndarray,
) -> dict[str, Any]:
    """Node ``pf_risk_contributions`` -- method card #327.

    Risk parity, equal risk contribution and risk budgeting.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        weights: [series_handle, required] Portfolio weights.
        covariance: [matrix_handle, required] Asset covariance matrix.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pf_risk_contributions: not implemented."
    )
