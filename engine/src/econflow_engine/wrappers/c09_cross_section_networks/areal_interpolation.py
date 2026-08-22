# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``areal_interpolation`` -- method card #473.

#473 Areal interpolation and spatial harmonisation

Category 09-cross-section-networks; module ``areal_interpolation``.

Reference implementation: tobler.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cs_areal_interpolate",
    "NODE_META",
    "wire_model",
]


def cs_areal_interpolate(
    *,
    source: pd.DataFrame,
    target: pd.DataFrame,
    variables: Sequence[str],
    extensive: bool | None = None,
    method: Literal["areal", "dasymetric", "pycnophylactic"] | None = None,
    auxiliary: pd.DataFrame | None = None,
) -> dict[str, Any]:
    """Node ``cs_areal_interpolate`` -- method card #473.

    Areal interpolation and spatial harmonisation.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        source: [df_handle, required] Source areal units and values.
        target: [df_handle, required] Target areal units.
        variables: [series_codes, required] Variables to interpolate.
        extensive: [boolean, optional] Treat the variables as extensive (mass preserving). Default
            ``True``.
        method: [enum, optional] Interpolation method. Default ``'areal'``.
        auxiliary: [df_handle, optional] Auxiliary surface for dasymetric interpolation.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cs_areal_interpolate: not implemented."
    )
