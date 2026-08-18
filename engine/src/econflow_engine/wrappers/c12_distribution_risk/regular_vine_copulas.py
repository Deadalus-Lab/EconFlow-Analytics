# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``regular_vine_copulas`` -- METHOD-SELECTION card #198.

#198 Regular-vine copulas — a pair-copula construction of the joint dependence (structure selection
    + loglik + simulate)

Category 12-distribution-risk; module ``regular_vine_copulas``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vine_loglik",
    "vine_select",
    "vine_sim",
    "NODE_META",
    "wire_model",
]


def vine_select(
    *,
    data: np.ndarray,
    familyset: Sequence[int] | None = None,
    type: Literal["RVine", "CVine"] | None = None,
    selectioncrit: Literal["AIC", "BIC", "logLik"] | None = None,
    indeptest: bool | None = None,
    level: float | None = None,
    trunclevel: int | None = None,
    rotations: bool | None = None,
    method: Literal["mle", "itau"] | None = None,
) -> dict[str, Any]:
    """Node ``vine_select`` -- METHOD-SELECTION card #198.

    Regular-vine copulas — a pair-copula construction of the joint dependence (structure selection +
    loglik + simulate).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [matrix_handle, required] Handle to a matrix of pseudo-observations (>=2 columns, ALL
            in [0,1], without NA· do the PIT/rank-transform first).
        familyset: [int_array, optional] Permitted copula families (BiCop codes· default curated:
            0/1/2/3/4/5/6 + rotations). Leave it unset for all.
        type: [enum, optional] Vine type: RVine (regular, default) or CVine (canonical).
        selectioncrit: [enum, optional] Pair-copula selection criterion (default AIC).
        indeptest: [boolean, optional] Preliminary independence test per pair (default False).
            Default ``False``.
        level: [number, optional] Significance level of the indeptest in (0,1) (default 0.05).
            Default ``0.05``.
        trunclevel: [integer, optional] Truncation: keep only the first k trees (NA = no
            truncation).
        rotations: [boolean, optional] Include rotated versions (90/180/270) of the families
            (default True). Default ``True``.
        method: [enum, optional] Parameter estimation: mle (default) or itau (inversion of Kendall's
            tau).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vine_select: not implemented. The method card is in ./README.md."
    )


def vine_loglik(
    *,
    object: Any,
    data: np.ndarray,
    separate: bool | None = None,
) -> dict[str, Any]:
    """Node ``vine_loglik`` -- METHOD-SELECTION card #198.

    Regular-vine copulas — a pair-copula construction of the joint dependence (structure selection +
    loglik + simulate).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an RVineMatrix (from vine_select).
        data: [matrix_handle, required] Handle to a matrix of pseudo-observations of the SAME
            dimension as the vine (in [0,1], without NA).
        separate: [boolean, optional] False (default) -> total loglik· True -> per-observation
            vector. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vine_loglik: not implemented. The method card is in ./README.md."
    )


def vine_sim(
    *,
    object: Any,
    N: int,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``vine_sim`` -- METHOD-SELECTION card #198.

    Regular-vine copulas — a pair-copula construction of the joint dependence (structure selection +
    loglik + simulate).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an RVineMatrix (from vine_select).
        N: [integer, required] Number of pseudo-observations to simulate (positive integer).
        seed: [integer, optional] Reproducibility seed (STOCHASTIC· default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vine_sim: not implemented. The method card is in ./README.md."
    )
