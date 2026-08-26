# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonlinear_embedding`` -- method card #604.

#604 Nonlinear embeddings: UMAP, t-SNE, Isomap and kernel PCA

Category 29-unsupervised-clustering; module ``nonlinear_embedding``.

Reference implementation: umap-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uc_nonlinear_embedding",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_nonlinear_embedding(
    *,
    x: pd.DataFrame,
    method: Literal["umap", "tsne", "isomap", "kernel_pca", "spectral", "mds"] | None = None,
    n_components: int | None = None,
    n_neighbors: int | None = None,
    min_dist: float | None = None,
    perplexity: float | None = None,
    metric: Literal["euclidean", "manhattan", "cosine", "correlation"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uc_nonlinear_embedding`` -- method card #604.

    Nonlinear embeddings: UMAP, t-SNE, Isomap and kernel PCA.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [df_handle, required] High-dimensional data.
        method: [enum, optional] Method. Default ``'umap'``.
        n_components: [integer, optional] Embedding dimension. Default ``2``.
        n_neighbors: [integer, optional] Neighbourhood size. Default ``15``.
        min_dist: [number, optional] Minimum distance for UMAP. Default ``0.1``.
        perplexity: [number, optional] Perplexity for t-SNE. Default ``30.0``.
        metric: [enum, optional] Distance metric. Default ``'euclidean'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "uc_nonlinear_embedding: not implemented."
    )
