# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``geographically_weighted`` -- method card #469.

#469 Geographically weighted regression, GWR and MGWR

Category 09-cross-section-networks; module ``geographically_weighted``.

Reference implementation: mgwr.

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
    "cs_gwr",
    "NODE_META",
    "wire_model",
]


def cs_gwr(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    coords: np.ndarray,
    model: Literal["gwr", "mgwr"] | None = None,
    kernel: Literal["bisquare", "gaussian", "exponential"] | None = None,
    bandwidth: float | None = None,
    adaptive: bool | None = None,
) -> dict[str, Any]:
    """Node ``cs_gwr`` -- method card #469.

    Geographically weighted regression, GWR and MGWR.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [df_handle, required] Covariate table.
        coords: [matrix_handle, required] Location coordinates.
        model: [enum, optional] Model variant. Default ``'gwr'``.
        kernel: [enum, optional] Spatial kernel. Default ``'bisquare'``.
        bandwidth: [number, optional] Bandwidth; omitted = selected by criterion.
        adaptive: [boolean, optional] Adaptive nearest-neighbour bandwidth. Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cs_gwr: not implemented."
    )
