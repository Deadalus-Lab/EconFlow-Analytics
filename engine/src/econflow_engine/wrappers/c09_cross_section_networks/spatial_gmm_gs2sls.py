# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_gmm_gs2sls`` -- method card #178.

#178 Spatial GMM / GS2SLS (SARAR/lag/error) with heteroskedasticity-robust SEs

Category 09-cross-section-networks; module ``spatial_gmm_gs2sls``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

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
    "sp_gmm_reg",
    "NODE_META",
    "wire_model",
]


def sp_gmm_reg(
    *,
    formula: str,
    data: pd.DataFrame,
    W: np.ndarray,
    model: Literal["sarar", "lag", "error", "ols"] | None = None,
    het: bool | None = None,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
    initial_value: float | None = None,
    q: int | None = None,
) -> dict[str, Any]:
    """Node ``sp_gmm_reg`` -- method card #178.

    Spatial GMM / GS2SLS (SARAR/lag/error) with heteroskedasticity-robust SEs.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Regression model, e.g. 'y ~ x1 + x2'.
        data: [df_handle, required] DataFrame with the variables (same order/count as the W).
        W: [matrix_handle, required] Square spatial weights matrix n x n (ideally row-standardized·
            dim == the row count of data).
        model: [enum, optional] sarar=lag+error, lag=Wy only, error=Wu only, ols=non-spatial
            baseline (default sarar). Default ``'sarar'``.
        het: [boolean, optional] True -> heteroskedasticity-robust GMM SEs (Kelejian-Prucha/Arraiz)·
            False -> homoskedastic (default True — the reason this node exists). Default ``True``.
        style: [enum, optional] weights coding scheme for converting W -> spatial weights (default W
            = row-standardized). Default ``'W'``.
        initial_value: [number, optional] Starting value of the spatial rho in the GMM optimisation,
            ∈ (-1,1) (default 0.2). Default ``0.2``.
        q: [integer, optional] Order of the spatial instruments W X,..., W^q X (default 2· a very
            large q -> singular). Default ``2``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sp_gmm_reg: not implemented."
    )
