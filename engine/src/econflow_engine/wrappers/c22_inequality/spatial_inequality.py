# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_inequality`` -- method card #561.

#561 Spatial inequality decomposition

Category 22-inequality; module ``spatial_inequality``.

Reference implementation: inequality.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iq_spatial_decomposition",
    "NODE_META",
    "wire_model",
]


def iq_spatial_decomposition(
    *,
    income: pd.Series,
    region: pd.Series,
    weights: pd.Series | None = None,
    index: Literal["theil", "mld", "gini", "spatial_gini"] | None = None,
    spatial_weights: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``iq_spatial_decomposition`` -- method card #561.

    Spatial inequality decomposition.

    Category 22-inequality; memory class ``light``.

    Args:
        income: [series_handle, required] Income.
        region: [series_handle, required] Region label.
        weights: [series_handle, optional] Population weights.
        index: [enum, optional] Inequality index. Default ``'theil'``.
        spatial_weights: [matrix_handle, optional] Spatial weights for the spatial Gini.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "iq_spatial_decomposition: not implemented."
    )
