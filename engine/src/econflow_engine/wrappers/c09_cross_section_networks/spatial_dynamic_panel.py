# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_dynamic_panel`` -- method card #179.

#179 Spatial dynamic panel data model (Lee-Yu QML, fixed effects) + direct/indirect/total effects

Category 09-cross-section-networks; module ``spatial_dynamic_panel``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sp_dynpanel",
    "sp_dynpanel_impacts",
    "NODE_META",
    "wire_model",
]


def sp_dynpanel(
    *,
    formula: str,
    data: pd.DataFrame,
    W: np.ndarray,
    index: Sequence[str],
    model: Literal["sar", "sdm"] | None = None,
    effect: Literal["individual", "time", "twoways", "none"] | None = None,
    dynamic: bool | None = None,
    tl: bool | None = None,
    stl: bool | None = None,
    tlag_ind: int | None = None,
    LYtrans: bool | None = None,
    rowstand: bool | None = None,
) -> dict[str, Any]:
    """Node ``sp_dynpanel`` -- method card #179.

    Spatial dynamic panel data model (Lee-Yu QML, fixed effects) + direct/indirect/total effects.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Static-part panel formula (WITHOUT time-lag terms), e.g. 'y ~
            x1 + x2'.
        data: [df_handle, required] Balanced panel DataFrame (long-format) with variables + index
            columns.
        W: [matrix_handle, required] Spatial weights matrix n×n (n = number of spatial units·
            ideally row-standardized).
        index: [series_codes, required] Two column names [<spatial>, <time>] — spatial first, time
            second.
        model: [enum, optional] sar (spatial lag) or sdm (spatial Durbin, +W*X)· default sar. 'sem'
            is NOT supported.
        effect: [enum, optional] Type of fixed effects· default individual.
        dynamic: [boolean, optional] True -> adds the time-lag of the dependent variable (y_{t-1})·
            default False.
        tl: [boolean, optional] Only when dynamic=True: includes y_{t-1} (default True).
        stl: [boolean, optional] Only when dynamic=True: includes W*y_{t-1} (space-time lag, default
            True).
        tlag_ind: [integer, optional] Optional index of the data column that supplies the time-lag·
            None -> created automatically.
        LYtrans: [boolean, optional] Lee-Yu bias-correction transformation (default True). Default
            ``True``.
        rowstand: [boolean, optional] Row-standardize the W via row normalisation before estimation
            (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_dynpanel: not implemented."
    )


def sp_dynpanel_impacts(
    *,
    object: Any,
    NSIM: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sp_dynpanel_impacts`` -- method card #179.

    Spatial dynamic panel data model (Lee-Yu QML, fixed effects) + direct/indirect/total effects.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] SDPDm fitted object (sp_dynpanel $object handle).
        NSIM: [integer, optional] Number of simulations for the SE of the effects (default 200).
            Default ``200``.
        seed: [integer, optional] Reproducibility seed for the simulation (default 2025). Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_dynpanel_impacts: not implemented."
    )
