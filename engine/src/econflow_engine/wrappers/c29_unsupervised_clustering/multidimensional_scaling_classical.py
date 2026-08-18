# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multidimensional_scaling_classical`` -- METHOD-SELECTION card #245.

#245 Multidimensional Scaling: CLASSICAL/metric (cmdscale = principal coordinates analysis, + the
    Cailliez constant) · NON-METRIC after Kruskal (isoMDS) · the NON-LINEAR Sammon mapping

Category 29-unsupervised-clustering; module ``multidimensional_scaling_classical``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mds_cmdscale",
    "mds_isomds",
    "mds_sammon",
    "NODE_META",
    "wire_model",
]


def mds_cmdscale(
    *,
    d: Any,
    k: int | None = None,
    add: bool | None = None,
) -> dict[str, Any]:
    """Node ``mds_cmdscale`` -- METHOD-SELECTION card #245.

    Multidimensional Scaling: CLASSICAL/metric (cmdscale = principal coordinates analysis, + the
    Cailliez constant) · NON-METRIC after Kruskal (isoMDS) · the NON-LINEAR Sammon mapping.

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
    """
    raise NotImplementedError(
        "mds_cmdscale: not implemented. The method card is in ./README.md."
    )


def mds_isomds(
    *,
    d: Any,
    k: int | None = None,
    maxit: int | None = None,
    tol: float | None = None,
    p: float | None = None,
) -> dict[str, Any]:
    """Node ``mds_isomds`` -- METHOD-SELECTION card #245.

    Multidimensional Scaling: CLASSICAL/metric (cmdscale = principal coordinates analysis, + the
    Cailliez constant) · NON-METRIC after Kruskal (isoMDS) · the NON-LINEAR Sammon mapping.

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
    """
    raise NotImplementedError(
        "mds_isomds: not implemented. The method card is in ./README.md."
    )


def mds_sammon(
    *,
    d: Any,
    k: int | None = None,
    niter: int | None = None,
    magic: float | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``mds_sammon`` -- METHOD-SELECTION card #245.

    Multidimensional Scaling: CLASSICAL/metric (cmdscale = principal coordinates analysis, + the
    Cailliez constant) · NON-METRIC after Kruskal (isoMDS) · the NON-LINEAR Sammon mapping.

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
    """
    raise NotImplementedError(
        "mds_sammon: not implemented. The method card is in ./README.md."
    )
