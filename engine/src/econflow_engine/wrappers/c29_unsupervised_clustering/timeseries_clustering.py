# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``timeseries_clustering`` -- method card #602.

#602 Time-series clustering: DTW k-means, k-Shape and kernel k-means

Category 29-unsupervised-clustering; module ``timeseries_clustering``.

Reference implementation: tslearn.

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
    "uc_timeseries_clustering",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_timeseries_clustering(
    *,
    series: pd.DataFrame,
    n_clusters: int,
    method: Literal["euclidean_kmeans", "dtw_kmeans", "kshape", "kernel_kmeans"] | None = None,
    warping_window: float | None = None,
    normalise: bool | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uc_timeseries_clustering`` -- method card #602.

    Time-series clustering: DTW k-means, k-Shape and kernel k-means.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        series: [df_handle, required] Series panel, one row per series.
        n_clusters: [integer, required] Number of clusters.
        method: [enum, optional] Algorithm. Default ``'dtw_kmeans'``.
        warping_window: [number, optional] Sakoe-Chiba band as a fraction of length. Default
            ``0.1``.
        normalise: [boolean, optional] Normalise each series before clustering. Default ``True``.
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
        "uc_timeseries_clustering: not implemented."
    )
