# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``moran_eigenvector_spatial`` -- method card #180.

#180 Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process)

Category 09-cross-section-networks; module ``moran_eigenvector_spatial``.

Reference implementation: 10.1007/s10109-015-0213-7.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sp_eigenvector_filter",
    "sp_moran_eigenvectors",
    "sp_random_effects_filter",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sp_moran_eigenvectors(
    *,
    W: np.ndarray,
    model: Literal["exp", "gau", "sph"] | None = None,
    threshold: float | None = None,
    enum: int | None = None,
) -> dict[str, Any]:
    """Node ``sp_moran_eigenvectors`` -- method card #180.

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
        "sp_moran_eigenvectors: not implemented."
    )


def sp_eigenvector_filter(
    *,
    object: Any,
    y: Sequence[float],
    x: np.ndarray | None = None,
    fn: Literal["r2", "aic", "bic", "all"] | None = None,
    vif: float | None = None,
) -> dict[str, Any]:
    """Node ``sp_eigenvector_filter`` -- method card #180.

    Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Moran-eigenvector object (sp_moran_eigenvectors
            $handle/$object).
        y: [num_array, required] Dependent variable (numeric vector N x 1, no NA).
        x: [matrix_handle, optional] Matrix of explanatory variables N x K (None -> intercept-only).
        fn: [enum, optional] Objective function for stepwise eigenvector selection (default r2·
            'all' = no selection).
        vif: [number, optional] Max acceptable VIF for the eigenvector selection (None -> no
            constraint).

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
        "sp_eigenvector_filter: not implemented."
    )


def sp_random_effects_filter(
    *,
    object: Any,
    y: Sequence[float],
    x: np.ndarray | None = None,
    method: Literal["reml", "ml"] | None = None,
) -> dict[str, Any]:
    """Node ``sp_random_effects_filter`` -- method card #180.

    Moran eigenvector spatial regression — eigenvector spatial filtering (ESF) & random-effects ESF
    (RE-ESF, an approximate Gaussian process).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] Moran-eigenvector object (sp_moran_eigenvectors
            $handle/$object).
        y: [num_array, required] Dependent variable (numeric vector N x 1, no NA).
        x: [matrix_handle, optional] Matrix of explanatory variables N x K (None -> intercept-only).
        method: [enum, optional] Variance-components estimation method: REML or ML (default reml).

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
        "sp_random_effects_filter: not implemented."
    )
