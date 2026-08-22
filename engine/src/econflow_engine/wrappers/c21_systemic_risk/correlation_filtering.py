# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``correlation_filtering`` -- method card #557.

#557 Correlation-network filtering: minimum spanning tree and planar graphs

Category 21-systemic-risk; module ``correlation_filtering``.

Reference implementation: networkx.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sr_correlation_filter",
    "NODE_META",
    "wire_model",
]


def sr_correlation_filter(
    *,
    correlation: np.ndarray,
    method: Literal["mst", "pmfg", "threshold", "knn"] | None = None,
    threshold: float | None = None,
    metric: Literal["sqrt_2_1_minus_rho", "one_minus_abs", "angular"] | None = None,
) -> dict[str, Any]:
    """Node ``sr_correlation_filter`` -- method card #557.

    Correlation-network filtering: minimum spanning tree and planar graphs.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        correlation: [matrix_handle, required] Correlation matrix.
        method: [enum, optional] Filtering method. Default ``'mst'``.
        threshold: [number, optional] Correlation threshold when thresholding. Default ``0.5``.
        metric: [enum, optional] Correlation-to-distance transform. Default
            ``'sqrt_2_1_minus_rho'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sr_correlation_filter: not implemented."
    )
