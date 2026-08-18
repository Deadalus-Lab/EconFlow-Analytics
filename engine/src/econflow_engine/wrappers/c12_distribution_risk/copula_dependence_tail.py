# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``copula_dependence_tail`` -- METHOD-SELECTION card #197.

#197 Copula dependence + tail dependence + goodness of fit (joint stress)

Category 12-distribution-risk; module ``copula_dependence_tail``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cop_fit",
    "cop_gof",
    "cop_tail_index",
    "NODE_META",
    "wire_model",
]


def cop_fit(
    *,
    data: np.ndarray,
    family: Literal["normal", "t", "clayton", "gumbel", "frank"] | None = None,
    dim: int | None = None,
    method: Literal["mpl", "ml", "itau", "irho", "itau.mpl"] | None = None,
) -> dict[str, Any]:
    """Node ``cop_fit`` -- METHOD-SELECTION card #197.

    Copula dependence + tail dependence + goodness of fit (joint stress).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [matrix_handle, required] Handle to a matrix of pseudo-observations in [0,1]^d (one
            column per dimension· apply the pseudo-observation transform to the raw data first).
        family: [enum, optional] Copula family (default normal)· clayton=lower-tail,
            gumbel=upper-tail, t=symmetric tail, normal/frank=without tail dependence.
        dim: [integer, optional] Copula dimension = the column count of data (default 2· tail
            dependence is defined only for dim==2). Default ``2``.
        method: [enum, optional] Parameter estimator (default mpl = maximum pseudo-likelihood·
            itau/irho = inversion Kendall/Spearman without optim).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cop_fit: not implemented. The method card is in ./README.md."
    )


def cop_tail_index(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``cop_tail_index`` -- METHOD-SELECTION card #197.

    Copula dependence + tail dependence + goodness of fit (joint stress).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitCopula (from cop_fit· ONLY bivariate)· returns
            lower/upper coefficients of tail dependence (the tail-dependence routine).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cop_tail_index: not implemented. The method card is in ./README.md."
    )


def cop_gof(
    *,
    object: Any,
    data: np.ndarray,
    N: int | None = None,
    method: Literal["Sn", "SnB", "SnC"] | None = None,
    estim_method: Literal["mpl", "ml", "itau", "irho", "itau.mpl"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``cop_gof`` -- METHOD-SELECTION card #197.

    Copula dependence + tail dependence + goodness of fit (joint stress).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitCopula (from cop_fit)· gives the candidate
            family/structure for H0.
        data: [matrix_handle, required] Handle to a matrix of pseudo-observations in [0,1]^d (same
            data as the fit).
        N: [integer, optional] Parametric bootstrap replications (default 200· STOCHASTIC p-value·
            keep small). Default ``200``.
        method: [enum, optional] GoF statistic (default Sn = Cramer-von Mises,
            Genest-Remillard-Beaudoin 2009).
        estim_method: [enum, optional] Estimator re-applied to each bootstrap replicate (default
            mpl).
        seed: [integer, optional] Reproducibility seed of the parametric bootstrap (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cop_gof: not implemented. The method card is in ./README.md."
    )
