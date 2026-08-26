# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``elastic_distances`` -- method card #603.

#603 Elastic distance measures at scale

Category 29-unsupervised-clustering; module ``elastic_distances``.

Reference implementation: aeon.

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
    "uc_elastic_distance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_elastic_distance(
    *,
    series: pd.DataFrame,
    measure: Literal["dtw", "ddtw", "wdtw", "lcss", "erp", "msm", "twe", "euclidean"] | None = None,
    warping_window: float | None = None,
    normalise: bool | None = None,
    use_pruning: bool | None = None,
) -> dict[str, Any]:
    """Node ``uc_elastic_distance`` -- method card #603.

    Elastic distance measures at scale.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        series: [df_handle, required] Series panel, one row per series.
        measure: [enum, optional] Distance measure. Default ``'dtw'``.
        warping_window: [number, optional] Warping band as a fraction of length. Default ``0.1``.
        normalise: [boolean, optional] Normalise series before comparison. Default ``True``.
        use_pruning: [boolean, optional] Use lower bounds to prune computations. Default ``True``.

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
        "uc_elastic_distance: not implemented."
    )
