# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_markov`` -- method card #472.

#472 Spatial-temporal Markov chains and regional mobility

Category 09-cross-section-networks; module ``spatial_markov``.

Reference implementation: giddy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_spatial_markov",
    "NODE_META",
    "wire_model",
]


def cs_spatial_markov(
    *,
    data: pd.DataFrame,
    weights: np.ndarray,
    n_states: int | None = None,
    discretisation: Literal["quantile", "equal_interval", "fixed"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cs_spatial_markov`` -- method card #472.

    Spatial-temporal Markov chains and regional mobility.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        data: [df_handle, required] Panel of regional values.
        weights: [matrix_handle, required] Spatial weights matrix.
        n_states: [integer, optional] Number of discretised states. Default ``5``.
        discretisation: [enum, optional] How states are formed. Default ``'quantile'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cs_spatial_markov: not implemented."
    )
