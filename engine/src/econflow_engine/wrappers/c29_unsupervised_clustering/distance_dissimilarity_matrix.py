# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``distance_dissimilarity_matrix`` -- METHOD-SELECTION card #240.

#240 DISTANCE / dissimilarity matrix between objects: dist (the 6 documented metrics),
    correlation-based dissimilarity (1-r | 1-|r| | sqrt(2(1-r)) Mantegna), dist (14 further
    shape/compositional/Mahalanobis metrics)

Category 29-unsupervised-clustering; module ``distance_dissimilarity_matrix``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dm_cor_dist",
    "dm_dist",
    "dm_proxy_dist",
    "NODE_META",
    "wire_model",
]


def dm_dist(
    *,
    x: np.ndarray,
    method: (
        Literal[
            "euclidean",
            "maximum",
            "manhattan",
            "canberra",
            "binary",
            "minkowski",
        ]
        | None
    ) = None,
    p: float | None = None,
    orientation: Literal["rows_are_objects", "columns_are_objects"],
) -> dict[str, Any]:
    """Node ``dm_dist`` -- METHOD-SELECTION card #240.

    DISTANCE / dissimilarity matrix between objects: dist (the 6 documented metrics),
    correlation-based dissimilarity (1-r | 1-|r| | sqrt(2(1-r)) Mantegna), dist (14 further
    shape/compositional/Mahalanobis metrics).

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``dist_object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the
            distance routine does NOT error — it silently returns values with pairwise deletion)· >=
            2 objects· unique row names. sliding-window subsequence is explicitly rejected input
            (Keogh gate).
        method: [enum, optional] Metric of the distance routine (default 'euclidean'): euclidean
            (L2)· maximum (sup-norm)· manhattan (L1)· canberra (sum |x-y|/(|x|+|y|)) — HARD GATE: NO
            negative value (the dist documentation: "intended for non-negative values (e.g.,
            counts)»)· binary (asymmetric Jaccard over on/off) — HARD GATE: EVERY element ∈ {0,1}·
            on CONTINUOUS data everything is 'on' and the matrix comes out SILENTLY FULL OF ZEROS
            (discretize first with bn_quantile_bins)· minkowski (Lp, with 'p'). CAUTION: the metrics
            are NOT scale-invariant — standardize first if the units differ.
        p: [number, optional] Minkowski power (positive· default 2). Used ONLY when
            method='minkowski'· p<=0 -> hard gate («distance: invalid p»). Default ``2``.
        orientation: [enum, required] REQUIRED, never guessed: which dimension holds the objects to
            be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in
            the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical
            macro panel).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dm_dist: not implemented. The method card is in ./README.md."
    )


def dm_cor_dist(
    *,
    x: np.ndarray,
    cor_method: Literal["pearson", "spearman", "kendall"] | None = None,
    transform: Literal["one_minus", "one_minus_abs", "mantegna"] | None = None,
    orientation: Literal["rows_are_objects", "columns_are_objects"],
) -> dict[str, Any]:
    """Node ``dm_cor_dist`` -- METHOD-SELECTION card #240.

    DISTANCE / dissimilarity matrix between objects: dist (the 6 documented metrics),
    correlation-based dissimilarity (1-r | 1-|r| | sqrt(2(1-r)) Mantegna), dist (14 further
    shape/compositional/Mahalanobis metrics).

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``dist_object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the
            distance routine does NOT error — it silently returns values with pairwise deletion)· >=
            2 objects· unique row names. sliding-window subsequence is explicitly rejected input
            (Keogh gate).
        cor_method: [enum, optional] Correlation coefficient (default 'pearson'): pearson (linear)·
            spearman (monotone, on ranks)· kendall (concordance, robust to outliers/small samples).
        transform: [enum, optional] Transformation r -> distance (default 'one_minus'): one_minus
            d=1-r (the DIRECTION matters· range [0,2])· one_minus_abs d=1-|r| (opposite phase =
            'similar'· range [0,1])· mantegna d=sqrt(2(1-r)) = a True metric (Mantegna 1999) —
            prefer it for ward.D2/MDS.
        orientation: [enum, required] REQUIRED, never guessed: which dimension holds the objects to
            be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in
            the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical
            macro panel).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dm_cor_dist: not implemented. The method card is in ./README.md."
    )


def dm_proxy_dist(
    *,
    x: np.ndarray,
    method: (
        Literal[
            "cosine",
            "angular",
            "Chord",
            "Geodesic",
            "Mahalanobis",
            "Bray",
            "Soergel",
            "Whittaker",
            "Hellinger",
            "Kullback",
            "divergence",
            "Wave",
            "Podani",
            "eJaccard",
        ]
        | None
    ) = None,
    orientation: Literal["rows_are_objects", "columns_are_objects"],
) -> dict[str, Any]:
    """Node ``dm_proxy_dist`` -- METHOD-SELECTION card #240.

    DISTANCE / dissimilarity matrix between objects: dist (the 6 documented metrics),
    correlation-based dissimilarity (1-r | 1-|r| | sqrt(2(1-r)) Mantegna), dist (14 further
    shape/compositional/Mahalanobis metrics).

    Category 29-unsupervised-clustering; memory class ``light``.

    Registers its result under ``dist_object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC matrix/DataFrame. NO NA/NaN/Inf (the
            distance routine does NOT error — it silently returns values with pairwise deletion)· >=
            2 objects· unique row names. sliding-window subsequence is explicitly rejected input
            (Keogh gate).
        method: [enum, optional] Metric of the extended distance routine (default 'cosine').
            SHAPE/norm-based (NO zero row norm): cosine, angular, Chord, Geodesic. SCALE-aware:
            Mahalanobis (requires n > p AND a non-singular cov). COMPOSITIONAL/shares (require
            NON-negative & non-zero row sum): Bray, Soergel, Whittaker, Hellinger, Kullback,
            divergence, Wave, Podani, eJaccard. Euclidean/Manhattan/supremum/Minkowski/Canberra live
            in dm_dist· correlation in dm_cor_dist.
        orientation: [enum, required] REQUIRED, never guessed: which dimension holds the objects to
            be clustered. 'rows_are_objects' = objects (countries/units) in the ROWS, features in
            the columns· 'columns_are_objects' = series in the COLUMNS, time in the rows (typical
            macro panel).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dm_proxy_dist: not implemented. The method card is in ./README.md."
    )
