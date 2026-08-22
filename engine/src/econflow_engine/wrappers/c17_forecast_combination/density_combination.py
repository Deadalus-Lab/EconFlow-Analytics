# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_combination`` -- method card #531.

#531 Density combination: linear and logarithmic opinion pools

Category 17-forecast-combination; module ``density_combination``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fc_density_combination",
    "fc_score_driven_weights",
    "NODE_META",
    "wire_model",
]


def fc_density_combination(
    *,
    densities: np.ndarray,
    weights: Sequence[float] | None = None,
    pool: Literal["linear", "logarithmic", "beta_transformed"] | None = None,
    grid: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``fc_density_combination`` -- method card #531.

    Density combination: linear and logarithmic opinion pools.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        densities: [matrix_handle, required] Predictive densities or samples, one per component.
        weights: [num_array, optional] Component weights; omitted = equal.
        pool: [enum, optional] Pooling rule. Default ``'linear'``.
        grid: [num_array, optional] Evaluation grid.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fc_density_combination: not implemented."
    )


def fc_score_driven_weights(
    *,
    actual: pd.Series,
    densities: np.ndarray,
    forgetting: float | None = None,
) -> dict[str, Any]:
    """Node ``fc_score_driven_weights`` -- method card #531.

    Density combination: linear and logarithmic opinion pools.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        densities: [matrix_handle, required] Component predictive densities over time.
        forgetting: [number, optional] Forgetting factor on past scores. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fc_score_driven_weights: not implemented."
    )
