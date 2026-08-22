# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``downside_optimisation`` -- method card #329.

#329 CVaR, CDaR, mean-semivariance and Kelly optimisation

Category 38-portfolio-allocation; module ``downside_optimisation``.

Reference implementation: riskfolio-lib.

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
    "pf_downside_optimise",
    "pf_kelly",
    "NODE_META",
    "wire_model",
]


def pf_downside_optimise(
    *,
    returns: pd.DataFrame,
    risk_measure: (
        Literal[
            "cvar",
            "cdar",
            "semivariance",
            "evar",
            "worst_realisation",
            "max_drawdown",
        ]
        | None
    ) = None,
    confidence: float | None = None,
    target_return: float | None = None,
    bounds: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``pf_downside_optimise`` -- method card #329.

    CVaR, CDaR, mean-semivariance and Kelly optimisation.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        risk_measure: [enum, optional] Risk measure to minimise. Default ``'cvar'``.
        confidence: [number, optional] Tail level for CVaR and CDaR. Default ``0.95``.
        target_return: [number, optional] Return floor.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pf_downside_optimise: not implemented."
    )


def pf_kelly(
    *,
    returns: pd.DataFrame,
    fraction: float | None = None,
    bounds: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``pf_kelly`` -- method card #329.

    CVaR, CDaR, mean-semivariance and Kelly optimisation.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        fraction: [number, optional] Fraction of full Kelly to apply. Default ``0.5``.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "pf_kelly: not implemented."
    )
