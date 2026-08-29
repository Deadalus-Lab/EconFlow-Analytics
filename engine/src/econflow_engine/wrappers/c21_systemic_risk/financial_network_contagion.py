# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``financial_network_contagion`` -- method card #222.

#222 Financial-network contagion: DebtRank + Furfine cascades + interbank exposure-matrix
    reconstruction (Maximum Entropy / Minimum Density)

Category 21-systemic-risk; module ``financial_network_contagion``.

Reference implementation: 10.1038/srep00541.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nrm_contagion",
    "nrm_reconstruct_matrix",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def nrm_reconstruct_matrix(
    *,
    rowsums: np.ndarray,
    colsums: np.ndarray,
    method: Literal["me", "md"] | None = None,
    seed: int | None = None,
    max_it: int | None = None,
    abs_tol: float | None = None,
    md_c: float | None = None,
    md_lambda: float | None = None,
    md_k: int | None = None,
    md_theta: float | None = None,
    md_remove_prob: float | None = None,
) -> dict[str, Any]:
    """Node ``nrm_reconstruct_matrix`` -- method card #222.

    Financial-network contagion: DebtRank + Furfine cascades + interbank exposure-matrix
    reconstruction (Maximum Entropy / Minimum Density).

    Category 21-systemic-risk; memory class ``light``.

    Registers its result under ``exposure_matrix``, so a later node can consume it as a handle.

    Args:
        rowsums: [matrix_handle, required] Handle to a numeric vector of ASSETS per node (row sums;
            length >= 2, non-negative); sum(rowsums) MUST == sum(colsums).
        colsums: [matrix_handle, required] Handle to a numeric vector of LIABILITIES per node
            (column sums; same length as rowsums, non-negative, equal total sum).
        method: [enum, optional] Reconstruction method: 'me' Maximum Entropy (Upper & Worm 2004;
            dense, deterministic); 'md' Minimum Density (Anand et al. 2015; sparse, STOCHASTIC ->
            seed). Default 'me'.
        seed: [integer, optional] Positive integer seed for reproducibility of 'md' (default 1).
        max_it: [integer, optional] Maximum iterations (default 100000).
        abs_tol: [number, optional] Convergence tolerance (default 0.001).
        md_c: [number, optional] md: cost of an additional link (Anand et al.; default 1).
        md_lambda: [number, optional] md: low-density fraction for the first md_k rounds, in [0,1]
            (default 1).
        md_k: [integer, optional] md: low-density allocation rounds (default 100).
        md_theta: [number, optional] md: scaling parameter prior (default 1).
        md_remove_prob: [number, optional] md: probability of randomly removing a link, in [0,1)
            (default 0.01).

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
        "nrm_reconstruct_matrix: not implemented."
    )


def nrm_contagion(
    *,
    exposures: np.ndarray,
    buffer: np.ndarray,
    weights: np.ndarray | None = None,
    shock: Any | None = None,
    method: Literal["debtrank", "threshold"] | None = None,
    exposure_type: Literal["assets", "liabilities"] | None = None,
    max_it: int | None = None,
    single_hit: bool | None = None,
) -> dict[str, Any]:
    """Node ``nrm_contagion`` -- method card #222.

    Financial-network contagion: DebtRank + Furfine cascades + interbank exposure-matrix
    reconstruction (Maximum Entropy / Minimum Density).

    Category 21-systemic-risk; memory class ``light``.

    Args:
        exposures: [matrix_handle, required] Handle to a SQUARE (n x n) non-negative matrix of
            bilateral exposures (assets network: A->B => A has an asset in B); e.g. the
            exposure_matrix from nrm_reconstruct_matrix.
        buffer: [matrix_handle, required] Handle to a numeric non-negative vector of capital buffer
            per node (length n).
        weights: [matrix_handle, optional] Handle to a non-negative vector of weights per node (e.g.
            total assets; length n, positive sum >0). Default: equal weights rep(1,n) — unweighted.
        shock: [raw, optional] "all" (default; one default scenario per node) or a JSON array of n
            percentage shocks in [0,1] (a single scenario).
        method: [enum, optional] 'debtrank' (Bardoscia et al. 2015 continuous stress propagation) or
            'threshold' (traditional Furfine default cascades). Default 'debtrank'.
        exposure_type: [enum, optional] Matrix interpretation: 'assets' (A->B: A has an asset in B;
            default) or 'liabilities' (A->B: A owes B).
        max_it: [integer, optional] Maximum propagation iterations (default 1000).
        single_hit: [boolean, optional] Only for method='debtrank': True => old single-hit DebtRank
            (Battiston et al. 2012). Default False.

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
        "nrm_contagion: not implemented."
    )
