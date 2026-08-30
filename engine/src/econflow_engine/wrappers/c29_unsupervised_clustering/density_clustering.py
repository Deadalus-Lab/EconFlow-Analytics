# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_clustering`` -- method card #598.

#598 Density-based clustering: DBSCAN, HDBSCAN and OPTICS

Category 29-unsupervised-clustering; module ``density_clustering``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uc_density_clustering",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_density_clustering(
    *,
    x: pd.DataFrame,
    method: Literal["dbscan", "hdbscan", "optics"] | None = None,
    min_cluster_size: int | None = None,
    min_samples: int | None = None,
    eps: float | None = None,
    metric: Literal["euclidean", "manhattan", "cosine", "correlation"] | None = None,
) -> dict[str, Any]:
    """Node ``uc_density_clustering`` -- method card #598.

    Density-based clustering: DBSCAN, HDBSCAN and OPTICS.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [df_handle, required] Data to cluster.
        method: [enum, optional] Algorithm. Default ``'hdbscan'``.
        min_cluster_size: [integer, optional] Minimum cluster size. Default ``5``.
        min_samples: [integer, optional] Core-point threshold.
        eps: [number, optional] Neighbourhood radius for DBSCAN.
        metric: [enum, optional] Distance metric. Default ``'euclidean'``.

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
        "uc_density_clustering: not implemented."
    )
