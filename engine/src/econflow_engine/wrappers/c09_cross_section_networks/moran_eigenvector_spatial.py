# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``moran_eigenvector_spatial`` -- METHOD-SELECTION card #180.

#180 Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process)

Category 09-cross-section-networks; module ``moran_eigenvector_spatial``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sp_esf",
    "sp_meigen",
    "sp_resf",
    "NODE_META",
    "wire_model",
]


def sp_meigen(
    *,
    W: np.ndarray,
    model: Literal["exp", "gau", "sph"] | None = None,
    threshold: float | None = None,
    enum: int | None = None,
) -> dict[str, Any]:
    """Node ``sp_meigen`` -- METHOD-SELECTION card #180.

    Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        W: [matrix_handle, required] Spatial connectivity/weights matrix N x N (cmat· ideally
            row-standardized· symmetrized internally).
        model: [enum, optional] Spatial dependence kernel: exponential/gaussian/spherical (default
            exp).
        threshold: [number, optional] Eigenvalue threshold in [0,1]· 0 -> all the positive ones,
            0.25 std (Griffith) (default 0). Default ``0``.
        enum: [integer, optional] Max number of Moran eigenvectors to extract (None -> auto).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_meigen: not implemented. The method card is in ./README.md."
    )


def sp_esf(
    *,
    object: Any,
    y: Sequence[float],
    x: np.ndarray | None = None,
    fn: Literal["r2", "aic", "bic", "all"] | None = None,
    vif: float | None = None,
) -> dict[str, Any]:
    """Node ``sp_esf`` -- METHOD-SELECTION card #180.

    Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Moran-eigenvector object (sp_meigen $handle/$object).
        y: [num_array, required] Dependent variable (numeric vector N x 1, no NA).
        x: [matrix_handle, optional] Matrix of explanatory variables N x K (None -> intercept-only).
        fn: [enum, optional] Objective function for stepwise eigenvector selection (default r2·
            'all' = no selection).
        vif: [number, optional] Max acceptable VIF for the eigenvector selection (None -> no
            constraint).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_esf: not implemented. The method card is in ./README.md."
    )


def sp_resf(
    *,
    object: Any,
    y: Sequence[float],
    x: np.ndarray | None = None,
    method: Literal["reml", "ml"] | None = None,
) -> dict[str, Any]:
    """Node ``sp_resf`` -- METHOD-SELECTION card #180.

    Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Moran-eigenvector object (sp_meigen $handle/$object).
        y: [num_array, required] Dependent variable (numeric vector N x 1, no NA).
        x: [matrix_handle, optional] Matrix of explanatory variables N x K (None -> intercept-only).
        method: [enum, optional] Variance-components estimation method: REML or ML (default reml).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_resf: not implemented. The method card is in ./README.md."
    )
