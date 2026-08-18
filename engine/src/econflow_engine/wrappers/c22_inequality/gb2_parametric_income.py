# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gb2_parametric_income`` -- METHOD-SELECTION card #227.

#227 GB2 (Generalized Beta of the 2nd kind, 4 parameters a,b,p,q) parametric income-distribution ML
    fit + analytic Gini/ARPR

Category 22-inequality; module ``gb2_parametric_income``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "arpr_gb2",
    "fit_gb2",
    "gini_gb2",
    "NODE_META",
    "wire_model",
]


def fit_gb2(
    *,
    z: np.ndarray,
    w: np.ndarray | None = None,
    prop: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``fit_gb2`` -- METHOD-SELECTION card #227.

    GB2 (Generalized Beta of the 2nd kind, 4 parameters a,b,p,q) parametric income-distribution ML
    fit + analytic Gini/ARPR.

    Category 22-inequality; memory class ``light``.

    Args:
        z: [matrix_handle, required] Handle to a numeric vector of POSITIVE income (z > 0), length
            >= 10, without NA/Inf.
        w: [matrix_handle, optional] Optional handle to a weight vector (same length as z,
            positive); if missing, all weights = 1.
        prop: [number, optional] Poverty-line ratio for the ARPR in (0,1); default 0.6 (60% of the
            median).
        allow_nonconvergence: [boolean, optional] If True, non-convergence of the full ML does not
            block (converged=False); default False => hard stop on non-convergence.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fit_gb2: not implemented. The method card is in ./README.md."
    )


def gini_gb2(
    *,
    shape1: float,
    shape2: float,
    shape3: float,
) -> dict[str, Any]:
    """Node ``gini_gb2`` -- METHOD-SELECTION card #227.

    GB2 (Generalized Beta of the 2nd kind, 4 parameters a,b,p,q) parametric income-distribution ML
    fit + analytic Gini/ARPR.

    Category 22-inequality; memory class ``light``.

    Args:
        shape1: [number, required] Positive shape parameter a of the GB2.
        shape2: [number, required] Positive shape parameter p (Beta-2).
        shape3: [number, required] Positive shape parameter q (Beta-2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "gini_gb2: not implemented. The method card is in ./README.md."
    )


def arpr_gb2(
    *,
    prop: float,
    shape1: float,
    shape2: float,
    shape3: float,
) -> dict[str, Any]:
    """Node ``arpr_gb2`` -- METHOD-SELECTION card #227.

    GB2 (Generalized Beta of the 2nd kind, 4 parameters a,b,p,q) parametric income-distribution ML
    fit + analytic Gini/ARPR.

    Category 22-inequality; memory class ``light``.

    Args:
        prop: [number, required] Poverty-line ratio in (0,1) (typically 0.6).
        shape1: [number, required] Positive shape parameter a of the GB2.
        shape2: [number, required] Positive shape parameter p (Beta-2).
        shape3: [number, required] Positive shape parameter q (Beta-2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "arpr_gb2: not implemented. The method card is in ./README.md."
    )
