# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gmm_weighting`` -- method card #293.

#293 Optimal weighting matrices: HAC, cluster and kernel choices

Category 34-gmm-mestimation-partial-id; module ``gmm_weighting``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_weighting_matrix",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_weighting_matrix(
    *,
    moments: np.ndarray,
    kind: Literal["homoskedastic", "robust", "hac", "cluster"] | None = None,
    kernel: Literal["bartlett", "parzen", "quadratic_spectral", "truncated"] | None = None,
    bandwidth: int | None = None,
    cluster: pd.Series | None = None,
) -> dict[str, Any]:
    """Node ``gme_weighting_matrix`` -- method card #293.

    Optimal weighting matrices: HAC, cluster and kernel choices.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        moments: [matrix_handle, required] Evaluated moment conditions, one row per observation.
        kind: [enum, optional] Covariance family. Default ``'hac'``.
        kernel: [enum, optional] HAC kernel. Default ``'bartlett'``.
        bandwidth: [integer, optional] Lag truncation; omitted = automatic.
        cluster: [series_handle, optional] Cluster identifier when kind is cluster.

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
        "gme_weighting_matrix: not implemented."
    )
