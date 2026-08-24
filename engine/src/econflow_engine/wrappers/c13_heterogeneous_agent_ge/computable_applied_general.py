# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``computable_applied_general`` -- method card #202.

#202 Computable/Applied General Equilibrium — a structural dynamic model (sdm) with a
    Leontief/Cobb-Douglas/CES demand structure; equilibrium prices, activity levels, growth rate

Category 13-heterogeneous-agent-ge; module ``computable_applied_general``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cge_solve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cge_solve(
    *,
    dstype: Literal["constant", "CD", "CES"] | None = None,
    A: np.ndarray | None = None,
    Beta: np.ndarray | None = None,
    alpha: Sequence[float] | None = None,
    sigma: Sequence[float] | None = None,
    Theta: np.ndarray | None = None,
    B: np.ndarray | None = None,
    S0Exg: np.ndarray | None = None,
    p0: Sequence[float] | None = None,
    z0: Sequence[float] | None = None,
    GRExg: float | None = None,
    tolCond: float | None = None,
    maxIteration: int | None = None,
    numberOfPeriods: int | None = None,
    priceAdjustmentMethod: Literal["variable", "fixed"] | None = None,
    priceAdjustmentVelocity: float | None = None,
    ts: bool | None = None,
) -> dict[str, Any]:
    """Node ``cge_solve`` -- method card #202.

    Computable/Applied General Equilibrium — a structural dynamic model (sdm) with a
    Leontief/Cobb-Douglas/CES demand structure; equilibrium prices, activity levels, growth rate.

    Category 13-heterogeneous-agent-ge; memory class ``heavy``.

    Args:
        dstype: [enum, optional] Demand structure: constant (Leontief/Sraffa constant A) | CD
            (Cobb-Douglas) | CES (default constant).
        A: [matrix_handle, optional] Handle to a demand-coefficient n-by-m matrix (non-negative)·
            ONLY for dstype=constant.
        Beta: [matrix_handle, optional] Handle to a share n-by-m matrix (non-negative)· required for
            CD/CES· CD => each column sums to 1.
        alpha: [num_array, optional] Efficiency m-vector (CD/CES)· of length 1 (recycle) or m·
            default rep(1,m).
        sigma: [num_array, optional] CES elasticity m-vector· of length 1 or m· required for
            dstype=CES.
        Theta: [matrix_handle, optional] Handle to a positive n-by-m matrix (CES scale params)·
            optional.
        B: [matrix_handle, optional] Handle to a supply-coefficient n-by-m matrix· default diag(n)
            (requires m==n).
        S0Exg: [matrix_handle, optional] Handle to an exogenous supply n-by-m (NA=endogenous, NOT
            0)· default all NA.
        p0: [num_array, optional] Initial prices n-vector (>0)· default rep(1,n).
        z0: [num_array, optional] Initial activity levels m-vector (>0)· default rep(100,m).
        GRExg: [number, optional] Exogenous growth rate of the S0Exg· NA -> 0 if exogenous supply
            exists.
        tolCond: [number, optional] Convergence tolerance (>0). Default ``1e-05``.
        maxIteration: [integer, optional] Maximum number of iterations (>=1)· =1 => pure simulation.
            Default ``200``.
        numberOfPeriods: [integer, optional] Number of periods per iteration (>=1). Default ``300``.
        priceAdjustmentMethod: [enum, optional] Price adjustment method (default variable).
        priceAdjustmentVelocity: [number, optional] Price adjustment speed ∈ (0,1]. Default
            ``0.15``.
        ts: [boolean, optional] If True it also returns the adjustment time series
            (ts_p/ts_z/ts_S/ts_q). Default ``False``.

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
        "cge_solve: not implemented."
    )
