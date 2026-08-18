# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_panel_spatial`` -- METHOD-SELECTION card #177.

#177 Spatial panel models (SAR/SEM/SDM · FE/RE/pooling) — ML & GM + spatial LM tests

Category 09-cross-section-networks; module ``spatial_panel_spatial``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
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
    "sp_panel_gm",
    "sp_panel_lmtest",
    "sp_panel_ml",
    "NODE_META",
    "wire_model",
]


def sp_panel_ml(
    *,
    formula: str,
    data: pd.DataFrame,
    W: np.ndarray,
    model: Literal["within", "random", "pooling"] | None = None,
    effect: Literal["individual", "time", "twoways"] | None = None,
    lag: bool | None = None,
    spatial_error: Literal["b", "kkp", "none"] | None = None,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
    index: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``sp_panel_ml`` -- METHOD-SELECTION card #177.

    Spatial panel models (SAR/SEM/SDM · FE/RE/pooling) — ML & GM + spatial LM tests.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial panel formula, e.g. 'y ~ x1 + x2' (RHS = regressors,
            not indices).
        data: [df_handle, required] Balanced panel DataFrame· the first 2 columns = index
            (individual, time) unless index is given.
        W: [matrix_handle, required] Spatial weights matrix n x n (n = #spatial units)· converted to
            listw via a spatial weights list.
        model: [enum, optional] Panel effects: within=FE, random=RE, pooling=OLS (default within).
        effect: [enum, optional] Effects dimension (default individual).
        lag: [boolean, optional] Spatially lagged dependent Wy (SAR term) (default True). Default
            ``True``.
        spatial_error: [enum, optional] Spatial error: 'b' Baltagi, 'kkp' Kapoor-Kelejian-Prucha,
            'none' (default b).
        style: [enum, optional] mat2listw coding scheme (default W = row-standardized).
        index: [series_codes, optional] 2 column names ['individual','time'] (default = first 2
            columns).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_panel_ml: not implemented. The method card is in ./README.md."
    )


def sp_panel_gm(
    *,
    formula: str,
    data: pd.DataFrame,
    W: np.ndarray,
    model: Literal["within", "random"] | None = None,
    lag: bool | None = None,
    spatial_error: bool | None = None,
    moments: Literal["initial", "weights", "fullweights"] | None = None,
    method: Literal["w2sls", "b2sls", "g2sls", "ec2sls"] | None = None,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
    index: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``sp_panel_gm`` -- METHOD-SELECTION card #177.

    Spatial panel models (SAR/SEM/SDM · FE/RE/pooling) — ML & GM + spatial LM tests.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial panel formula, e.g. 'y ~ x1 + x2'.
        data: [df_handle, required] Balanced panel DataFrame (first 2 columns = index unless index
            is given).
        W: [matrix_handle, required] Spatial weights matrix n x n· -> listw via a spatial weights
            list.
        model: [enum, optional] Panel effects: within=FE or random=RE (default within).
        lag: [boolean, optional] Spatially lagged dependent Wy (SAR term) (default True). Default
            ``True``.
        spatial_error: [boolean, optional] Spatial error term (True/False) (default True). Default
            ``True``.
        moments: [enum, optional] GM moments (Kapoor-Kelejian-Prucha) (default initial).
        method: [enum, optional] IV estimator (default w2sls).
        style: [enum, optional] mat2listw coding scheme (default W).
        index: [series_codes, optional] 2 column names ['individual','time'] (default = first 2
            columns).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_panel_gm: not implemented. The method card is in ./README.md."
    )


def sp_panel_lmtest(
    *,
    formula: str,
    data: pd.DataFrame,
    W: np.ndarray,
    test: Literal["lme", "lml", "rlme", "rlml"] | None = None,
    model: str | None = None,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
    index: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``sp_panel_lmtest`` -- METHOD-SELECTION card #177.

    Spatial panel models (SAR/SEM/SDM · FE/RE/pooling) — ML & GM + spatial LM tests.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        formula: [formula, required] Spatial panel formula, e.g. 'y ~ x1 + x2'.
        data: [df_handle, required] Panel DataFrame (first 2 columns = index unless index is given).
        W: [matrix_handle, required] Spatial weights matrix n x n· -> listw via a spatial weights
            list.
        test: [enum, optional] LM test: lme=error, lml=lag, rlme/rlml=robust respectively (default
            lme).
        model: [string, optional] Baseline estimation for the LM test (default 'pooling'). Default
            ``'pooling'``.
        style: [enum, optional] mat2listw coding scheme (default W).
        index: [series_codes, optional] 2 column names ['individual','time'] (default = first 2
            columns).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_panel_lmtest: not implemented. The method card is in ./README.md."
    )
