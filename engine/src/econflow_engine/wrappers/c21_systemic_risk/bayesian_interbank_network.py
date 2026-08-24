# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_interbank_network`` -- method card #223.

#223 Bayesian interbank-network reconstruction (the Gandy-Veraart Gibbs sampler, an Erdős-Rényi
    hierarchical model)

Category 21-systemic-risk; module ``bayesian_interbank_network``.

Reference implementation: 10.1287/mnsc.2016.2546.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "build_er_model",
    "sample_interbank_network",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def build_er_model(
    *,
    l: np.ndarray,
    a: np.ndarray,
    targetdensity: float | None = None,
    seed: int | None = None,
    nsamples_calib: int | None = None,
    thin_calib: int | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``build_er_model`` -- method card #223.

    Bayesian interbank-network reconstruction (the Gandy-Veraart Gibbs sampler, an Erdős-Rényi
    hierarchical model).

    Category 21-systemic-risk; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        l: [matrix_handle, required] Handle to a numeric vector of row sums (total LIABILITIES of
            each bank), length >= 2, non-negative, without NA/Inf; sum(l)==sum(a) is required.
        a: [matrix_handle, required] Handle to a numeric vector of column sums (total ASSETS of each
            bank), same length as l, non-negative.
        targetdensity: [number, optional] Target network density ∈ (0,1] (default 0.5).
        seed: [integer, optional] Reproducibility seed of the calibration (positive integer; default
            1).
        nsamples_calib: [integer, optional] Number of matrices in the calibration (positive integer;
            default 100).
        thin_calib: [integer, optional] Thinning during the calibration (positive integer; default
            100).
        tol: [number, optional] Relative tolerance of the sum(l)==sum(a) balance check (default
            1e-6).

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
        "build_er_model: not implemented."
    )


def sample_interbank_network(
    *,
    l: np.ndarray,
    a: np.ndarray,
    model: Any,
    nsamples: int | None = None,
    thin: int | None = None,
    seed: int | None = None,
    matrpertheta: int | None = None,
    burnin: int | None = None,
    probs: Sequence[float] | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``sample_interbank_network`` -- method card #223.

    Bayesian interbank-network reconstruction (the Gandy-Veraart Gibbs sampler, an Erdős-Rényi
    hierarchical model).

    Category 21-systemic-risk; memory class ``mcmc``.

    Registers its result under ``samples``, so a later node can consume it as a handle.

    Args:
        l: [matrix_handle, required] Handle to row sums (liabilities); same as build_er_model.
        a: [matrix_handle, required] Handle to col sums (assets); same length as l, sum(l)==sum(a).
        model: [raw_handle, required] Handle to a systemicrisk model (build_er_model.model).
        nsamples: [integer, optional] Number of posterior samples of matrix L (positive integer;
            default 100).
        thin: [integer, optional] Thinning: theta updates per sample (positive integer; default
            100).
        seed: [integer, optional] Reproducibility seed of the MCMC (positive integer; default 1).
            REQUIRED determinism.
        matrpertheta: [integer, optional] Matrix updates per theta update (positive integer; default
            length(l)^2).
        burnin: [integer, optional] Number of burn-in iterations (positive integer; default auto).
        probs: [num_array, optional] 2 increasing quantiles ∈ (0,1) for lower/upper matrices per
            cell (default [0.05, 0.95]).
        tol: [number, optional] Relative tolerance of the sum(l)==sum(a) balance check (default
            1e-6).

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
        "sample_interbank_network: not implemented."
    )
