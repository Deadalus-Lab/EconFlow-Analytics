# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hierarchical_clustering_distance`` -- METHOD-SELECTION card #242.

#242 Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) +
    agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and
    tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships

Category 29-unsupervised-clustering; module ``hierarchical_clustering_distance``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hc_agnes",
    "hc_cutree",
    "hc_diana",
    "hc_hclust",
    "NODE_META",
    "wire_model",
]


def hc_hclust(
    *,
    d: Any,
    method: (
        Literal[
            "complete",
            "ward.D2",
            "ward.D",
            "single",
            "average",
            "mcquitty",
            "median",
            "centroid",
        ]
        | None
    ) = None,
    k: int | None = None,
    h: float | None = None,
) -> dict[str, Any]:
    """Node ``hc_hclust`` -- METHOD-SELECTION card #242.

    Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) +
    agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and
    tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships.

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``tree``, so a later node can consume it as a handle.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n
            >= 2.
        method: [enum, optional] Agglomeration method (default 'complete' = the documented default
            of the hierarchical-clustering routine). CAUTION: 'ward.D2' implements the Ward (1963)
            criterion (Murtagh & Legendre 2014)· 'ward.D' does NOT implement it — they are not
            equivalent. 'median'/'centroid' can produce inversions.
        k: [integer, optional] Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k'
            or 'h' (or neither = dendrogram data only).
        h: [number, optional] Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY
            one of 'k' or 'h'.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hc_hclust: not implemented. The method card is in ./README.md."
    )


def hc_cutree(
    *,
    tree: Any,
    k: int | None = None,
    h: float | None = None,
) -> dict[str, Any]:
    """Node ``hc_cutree`` -- METHOD-SELECTION card #242.

    Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) +
    agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and
    tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        tree: [raw_handle, required] Handle to an hclust or agnes/diana ('twins') tree — from the
            register of hc_hclust/hc_agnes/hc_diana.
        k: [integer, optional] Number of groups (1..n). EXACTLY one of 'k'/'h' (required).
        h: [number, optional] Cut height (>= 0· only on a monotone tree). EXACTLY one of 'k'/'h'
            (required).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hc_cutree: not implemented. The method card is in ./README.md."
    )


def hc_agnes(
    *,
    d: Any,
    method: (
        Literal[
            "average",
            "single",
            "complete",
            "ward",
            "weighted",
            "flexible",
            "gaverage",
        ]
        | None
    ) = None,
    par_method: Sequence[float] | None = None,
    k: int | None = None,
    h: float | None = None,
) -> dict[str, Any]:
    """Node ``hc_agnes`` -- METHOD-SELECTION card #242.

    Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) +
    agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and
    tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships.

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``tree``, so a later node can consume it as a handle.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n
            >= 2.
        method: [enum, optional] Agglomeration method (default 'average' = the documented default of
            the agglomerative-clustering routine). method='ward' is equivalent to
            hclust(method='ward.D2').
        par_method: [num_array, optional] Lance-Williams coefficients of length 1, 3 or 4 — ONLY for
            method='flexible' (REQUIRED, without default) or 'gaverage' (default -0.1). In other
            methods it is blocked (it would be ignored silently).
        k: [integer, optional] Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k'
            or 'h' (or neither = dendrogram data only).
        h: [number, optional] Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY
            one of 'k' or 'h'.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hc_agnes: not implemented. The method card is in ./README.md."
    )


def hc_diana(
    *,
    d: Any,
    k: int | None = None,
    h: float | None = None,
) -> dict[str, Any]:
    """Node ``hc_diana`` -- METHOD-SELECTION card #242.

    Hierarchical clustering on a distance matrix: agglomerative hclust (the 8 documented methods) +
    agnes (with an agglomerative coefficient), divisive diana (with a divisive coefficient), and
    tree cutting with cutree (k OR h) -> dendrogram chart-data (merge/height/order) + memberships.

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``tree``, so a later node can consume it as a handle.

    Args:
        d: [raw_handle, required] Handle to a 'dist' object (distance matrix· typically from the
            distance-matrix node). NO matrix/DataFrame — NO NA/Inf, NO negative dissimilarities, n
            >= 2.
        k: [integer, optional] Number of groups for cutting the tree (1..n). Give EXACTLY one of 'k'
            or 'h' (or neither = dendrogram data only).
        h: [number, optional] Cut height of the tree (>= 0· only on a monotone tree). Give EXACTLY
            one of 'k' or 'h'.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hc_diana: not implemented. The method card is in ./README.md."
    )
