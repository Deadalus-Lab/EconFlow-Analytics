# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multidimensional_scaling_classical`` -- method card #245.

#245 Multidimensional Scaling: CLASSICAL/metric (principal coordinates analysis + the Cailliez
    constant) · NON-METRIC after Kruskal · the NON-LINEAR Sammon mapping

Category 29-unsupervised-clustering; module ``multidimensional_scaling_classical``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mds_classical",
    "mds_nonmetric",
    "mds_sammon",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mds_classical(
    *,
    d: Any,
    k: int | None = None,
    add: bool | None = None,
) -> dict[str, Any]:
    """Node ``mds_classical`` -- method card #245.

    Multidimensional Scaling: CLASSICAL/metric (principal coordinates analysis + the Cailliez
    constant) · NON-METRIC after Kruskal · the NON-LINEAR Sammon mapping.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they
            are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.
        k: [integer, optional] Number of dimensions of the map (default 2 = the documented default).
            MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise
            the solution has fewer columns -> the node blocks).
        add: [boolean, optional] True = compute the Cailliez additive constant (1983) so that the
            dissimilarities become EUCLIDEAN (default False). Useful ONLY when there are negative
            eigenvalues (n_eig_negative > 0 / gof_abs < gof_pos).

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
        "mds_classical: not implemented."
    )


def mds_nonmetric(
    *,
    d: Any,
    k: int | None = None,
    maxit: int | None = None,
    tol: float | None = None,
    p: float | None = None,
) -> dict[str, Any]:
    """Node ``mds_nonmetric`` -- method card #245.

    Multidimensional Scaling: CLASSICAL/metric (principal coordinates analysis + the Cailliez
    constant) · NON-METRIC after Kruskal · the NON-LINEAR Sammon mapping.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they
            are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.
        k: [integer, optional] Number of dimensions of the map (default 2 = the documented default).
            MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise
            the solution has fewer columns -> the node blocks).
        maxit: [integer, optional] Maximum iterations (default 50· typically converges in ~10).
            Positive integer — 0 is SILENTLY accepted by MASS and returns a NON-optimized
            configuration.
        tol: [number, optional] Convergence tolerance (default 0.001). MUST be > 0 — non-positive is
            silently accepted and it stops prematurely with much worse stress.
        p: [number, optional] Minkowski power in the configuration space (default 2 = Euclidean).
            MUST be >= 1 (the Minkowski is a metric only for p >= 1· p = 0 does NOT terminate).

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
        "mds_nonmetric: not implemented."
    )


def mds_sammon(
    *,
    d: Any,
    k: int | None = None,
    niter: int | None = None,
    magic: float | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``mds_sammon`` -- method card #245.

    Multidimensional Scaling: CLASSICAL/metric (principal coordinates analysis + the Cailliez
    constant) · NON-METRIC after Kruskal · the NON-LINEAR Sammon mapping.

    Category 29-unsupervised-clustering; memory class ``mcmc``.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame (they are silently accepted even when they
            are NOT symmetric) — NO NA/Inf, NO negative dissimilarities, NOT all zero, n >= 2.
        k: [integer, optional] Number of dimensions of the map (default 2 = the documented default).
            MUST be in {1, 2,.. n-1}· in addition the POSITIVE eigenvalues must be >= k (otherwise
            the solution has fewer columns -> the node blocks).
        niter: [integer, optional] Maximum iterations (default 100· typically converges in ~50).
            Positive integer — 0 is SILENTLY accepted (no optimization).
        magic: [number, optional] Initial step of the diagonal-Newton (default 0.2). MUST be > 0 —
            magic <= 0 is SILENTLY accepted and does NOT optimize at all.
        tol: [number, optional] Termination tolerance in stress units (default 0.0001· > 0).

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
        "mds_sammon: not implemented."
    )
