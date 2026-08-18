# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``skew_fit_fitted`` -- METHOD-SELECTION card #95.

#95 Skew-t fit to fitted quantiles (ABG Growth-at-Risk «step 2») + density/ES

Category 12-distribution-risk; module ``skew_fit_fitted``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "st_density",
    "st_fit_quantiles",
    "st_shortfall",
    "NODE_META",
    "wire_model",
]


def st_fit_quantiles(
    *,
    probs: float,
    quantiles: float,
    fix_nu: float | None = None,
    weights: float | None = None,
    method: Literal["Nelder-Mead", "BFGS"] | None = None,
    maxit: int | None = None,
) -> dict[str, Any]:
    """Node ``st_fit_quantiles`` -- METHOD-SELECTION card #95.

    Skew-t fit to fitted quantiles (ABG Growth-at-Risk «step 2») + density/ES.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``dp``, so a later node can consume it as a handle.

    Args:
        probs: [number, required] Vector of probabilities in (0,1), strictly increasing (>=4
            points).
        quantiles: [number, required] Vector of fitted quantiles (strictly increasing· same length
            as probs).
        fix_nu: [number, optional] Optionally fix the degrees of freedom nu (>2).
        weights: [number, optional] Optional positive weights of length length(probs) for the SSE.
        method: [enum, optional] optim method (default Nelder-Mead).
        maxit: [integer, optional] Maximum optim iterations (default 2000). Default ``2000``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "st_fit_quantiles: not implemented. The method card is in ./README.md."
    )


def st_density(
    *,
    fit: Any,
    n: int | None = None,
) -> dict[str, Any]:
    """Node ``st_density`` -- METHOD-SELECTION card #95.

    Skew-t fit to fitted quantiles (ABG Growth-at-Risk «step 2») + density/ES.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a skew-t fit/dp (from st_fit_quantiles).
        n: [integer, optional] Number of pdf/cdf grid points (default 512). Default ``512``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "st_density: not implemented. The method card is in ./README.md."
    )


def st_shortfall(
    *,
    fit: Any,
    prob: float | None = None,
    side: Literal["left", "right"] | None = None,
) -> dict[str, Any]:
    """Node ``st_shortfall`` -- METHOD-SELECTION card #95.

    Skew-t fit to fitted quantiles (ABG Growth-at-Risk «step 2») + density/ES.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a skew-t fit/dp (from st_fit_quantiles).
        prob: [number, optional] Tail probability for VaR/ES (default 0.05). Default ``0.05``.
        side: [enum, optional] left = downside ES (default)· right = upside.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "st_shortfall: not implemented. The method card is in ./README.md."
    )
