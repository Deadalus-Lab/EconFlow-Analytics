# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mean_variance`` -- method card #324.

#324 Mean-variance optimisation and the efficient frontier under constraints

Category 38-portfolio-allocation; module ``mean_variance``.

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
    "pf_efficient_frontier",
    "pf_mean_variance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pf_mean_variance(
    *,
    returns: pd.DataFrame,
    objective: (
        Literal[
            "max_sharpe",
            "min_volatility",
            "max_return",
            "target_return",
            "target_risk",
            "max_utility",
        ]
        | None
    ) = None,
    target: float | None = None,
    bounds: Sequence[float] | None = None,
    risk_free: float | None = None,
    covariance: Literal["sample", "ledoit_wolf", "oas", "exponential", "denoised"] | None = None,
) -> dict[str, Any]:
    """Node ``pf_mean_variance`` -- method card #324.

    Mean-variance optimisation and the efficient frontier under constraints.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        objective: [enum, optional] Optimisation objective. Default ``'max_sharpe'``.
        target: [number, optional] Target return or risk when the objective names one.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.
        risk_free: [number, optional] Risk-free rate. Default ``0.0``.
        covariance: [enum, optional] Covariance estimator. Default ``'ledoit_wolf'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "pf_mean_variance: not implemented."
    )


def pf_efficient_frontier(
    *,
    returns: pd.DataFrame,
    n_points: int | None = None,
    bounds: Sequence[float] | None = None,
    covariance: Literal["sample", "ledoit_wolf", "oas", "exponential", "denoised"] | None = None,
) -> dict[str, Any]:
    """Node ``pf_efficient_frontier`` -- method card #324.

    Mean-variance optimisation and the efficient frontier under constraints.

    Category 38-portfolio-allocation; memory class ``light``.

    Args:
        returns: [df_handle, required] Asset return panel.
        n_points: [integer, optional] Points along the frontier. Default ``50``.
        bounds: [num_array, optional] Lower and upper weight bounds. Default ``[0.0, 1.0]``.
        covariance: [enum, optional] Covariance estimator. Default ``'ledoit_wolf'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "pf_efficient_frontier: not implemented."
    )
