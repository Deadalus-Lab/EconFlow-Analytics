# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``biclustering`` -- method card #605.

#605 Biclustering and co-clustering

Category 29-unsupervised-clustering; module ``biclustering``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uc_biclustering",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_biclustering(
    *,
    x: np.ndarray,
    method: Literal["cocluster", "bicluster"] | None = None,
    n_clusters: int | None = None,
    n_row_clusters: int | None = None,
    n_column_clusters: int | None = None,
    normalise: Literal["none", "log", "scale", "bistochastic"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uc_biclustering`` -- method card #605.

    Biclustering and co-clustering.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [matrix_handle, required] Data matrix.
        method: [enum, optional] Method. Default ``'cocluster'``.
        n_clusters: [integer, optional] Cluster count. Default ``3``.
        n_row_clusters: [integer, optional] Row clusters for biclustering.
        n_column_clusters: [integer, optional] Column clusters for biclustering.
        normalise: [enum, optional] Normalisation. Default ``'log'``.
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
        "uc_biclustering: not implemented."
    )
