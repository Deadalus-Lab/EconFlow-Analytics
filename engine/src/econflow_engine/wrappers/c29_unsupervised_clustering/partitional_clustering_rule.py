# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``partitional_clustering_rule`` -- method card #241.

#241 Partitional (flat) clustering + RULE-BASED selection of k: k-means
    (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette
    diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules

Category 29-unsupervised-clustering; module ``partitional_clustering_rule``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "km_fit",
    "km_gap",
    "km_pam",
    "km_silhouette",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def km_fit(
    *,
    x: np.ndarray,
    k: int,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    algorithm: Literal["Hartigan-Wong", "Lloyd", "Forgy", "MacQueen"] | None = None,
    nstart: int | None = None,
    iter_max: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``km_fit`` -- method card #241.

    Partitional (flat) clustering + RULE-BASED selection of k: k-means
    (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette
    diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence
            IS REJECTED matrix (Keogh gate).
        k: [integer, required] Number of clusters. MUST be 1 <= k <= number of DISTINCT rows (NOT n:
            duplicate rows break k<n).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale).
        algorithm: [enum, optional] Algorithm (default Hartigan-Wong, the best)· Lloyd/Forgy = the
            same algorithm· Lloyd/Forgy can leave an EMPTY cluster -> hard gate.
        nstart: [integer, optional] Number of random initializations (default 25). REQUIRED >= 2
            (determinism). Default ``25``.
        iter_max: [integer, optional] Maximum iterations per start (kmeans iter.max· default 50).
            Default ``50``.
        seed: [integer, optional] REQUIRED seed — kmeans has random initialization (default 1234).
            Same seed => identical result. Default ``1234``.

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
        "km_fit: not implemented."
    )


def km_pam(
    *,
    x: np.ndarray,
    k: int,
    metric: Literal["euclidean", "manhattan"] | None = None,
    stand: bool | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
) -> dict[str, Any]:
    """Node ``km_pam`` -- method card #241.

    Partitional (flat) clustering + RULE-BASED selection of k: k-means
    (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette
    diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence
            IS REJECTED matrix (Keogh gate).
        k: [integer, required] Number of clusters· 1 <= k <= n-1 AND k <= number of DISTINCT rows
            (pam does NOT error on a larger k: it returns duplicate medoids).
        metric: [enum, optional] Dissimilarity metric (default euclidean· manhattan = more robust).
        stand: [boolean, optional] pam standardization (mean-absolute-deviation per column· default
            False). FORBIDDEN together with transform='scale' (double standardization). Default
            ``False``.
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale).

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
        "km_pam: not implemented."
    )


def km_silhouette(
    *,
    x: np.ndarray,
    cluster: Sequence[int],
    metric: Literal["euclidean", "manhattan"] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
) -> dict[str, Any]:
    """Node ``km_silhouette`` -- method card #241.

    Partitional (flat) clustering + RULE-BASED selection of k: k-means
    (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette
    diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence
            IS REJECTED matrix (Keogh gate).
        cluster: [int_array, required] Integer assignment vector of length n with CONTIGUOUS ids
            1..k (e.g. the 'cluster' field of a km_fit/km_pam node). Required: 2 <= k <= n-1: with
            k=1 silhouette returns NA WITHOUT an error.
        metric: [enum, optional] Dissimilarity metric (default euclidean· manhattan = more robust).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale).

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
        "km_silhouette: not implemented."
    )


def km_gap(
    *,
    x: np.ndarray,
    k_max: int | None = None,
    fun_cluster: Literal["kmeans", "pam"] | None = None,
    B: int | None = None,
    d_power: int | None = None,
    space_h0: Literal["scaledPCA", "original"] | None = None,
    method: (
        Literal[
            "firstSEmax",
            "Tibs2001SEmax",
            "globalSEmax",
            "firstmax",
            "globalmax",
        ]
        | None
    ) = None,
    se_factor: float | None = None,
    nstart: int | None = None,
    iter_max: int | None = None,
    metric: Literal["euclidean", "manhattan"] | None = None,
    transform: Literal["none", "center", "scale", "log"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``km_gap`` -- method card #241.

    Partitional (flat) clustering + RULE-BASED selection of k: k-means
    (Hartigan-Wong/Lloyd/Forgy/MacQueen), PAM/k-medoids (Kaufman-Rousseeuw), the silhouette
    diagnostic (Rousseeuw), the gap statistic (Tibshirani-Walther-Hastie) with the 5 maxSE rules.

    Category 29-unsupervised-clustering; memory class ``heavy``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×features matrix (rows =
            observations/countries, columns = variables). NO NA/NaN/Inf. sliding-window subsequence
            IS REJECTED matrix (Keogh gate).
        k_max: [integer, optional] Maximum k to examine (default 8)· >= 2 AND <= min(n-1, DISTINCT
            rows). Default ``8``.
        fun_cluster: [enum, optional] Algorithm inside the gap loop (default kmeans· pam = robust).
        B: [integer, optional] Number of Monte-Carlo (bootstrap) reference samples (default 100·
            B=500 for final results). Default ``100``.
        d_power: [integer, optional] Power of the euclidean distances in W(k): 1 = the conventional
            implementation (default)· 2 = proposal Tibshirani et al. Default ``1``.
        space_h0: [enum, optional] Space of the H0 distribution of "no cluster" (default scaledPCA =
            uniform over a PCA-rotated hypercube).
        method: [enum, optional] maxSE rule for the optimal k (default firstSEmax = first local
            maximum within 1 SE)· Tibs2001SEmax = the original Tibshirani rule.
        se_factor: [number, optional] Multiplier of the "1-SE" rule (positive· default 1). Default
            ``1``.
        nstart: [integer, optional] nstart of the inner kmeans (>= 2· default 25). Default ``25``.
        iter_max: [integer, optional] iter.max of the inner kmeans (default 50). Default ``50``.
        metric: [enum, optional] Dissimilarity metric (default euclidean· manhattan = more robust).
        transform: [enum, optional] EXPLICIT transformation BEFORE the clustering (default 'none' —
            NO silent standardization/detrending): center (mean removal per column)· scale (z-score·
            forbidden on a zero-variance column)· log (requires > 0). The fitted params are returned
            (transform_center/transform_scale).
        seed: [integer, optional] REQUIRED seed — clusGap is bootstrap (default 1234). Default
            ``1234``.

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
        "km_gap: not implemented."
    )
