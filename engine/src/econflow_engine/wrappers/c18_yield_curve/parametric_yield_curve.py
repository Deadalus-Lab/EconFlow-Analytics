# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``parametric_yield_curve`` -- METHOD-SELECTION card #210.

#210 Parametric yield-curve factor models (Nelson-Siegel / Svensson / cubic spline, Diebold-Li
    dynamics on a panel) + curve transforms (spot/forward/discount/PCA)

Category 18-yield-curve; module ``parametric_yield_curve``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "yc_fit",
    "yc_transform",
    "NODE_META",
    "wire_model",
]


def yc_fit(
    *,
    maturities: Sequence[float],
    rates: Sequence[float] | None = None,
    panel: np.ndarray | None = None,
    method: Literal["nelson_siegel", "svensson", "cubic_spline"] | None = None,
    type: Literal["zero", "par", "forward"] | None = None,
    tau_init: float | None = None,
    tau1_init: float | None = None,
    tau2_init: float | None = None,
    weights: Sequence[float] | None = None,
    dates: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``yc_fit`` -- METHOD-SELECTION card #210.

    Parametric yield-curve factor models (Nelson-Siegel / Svensson / cubic spline, Diebold-Li
    dynamics on a panel) + curve transforms (spot/forward/discount/PCA).

    Category 18-yield-curve; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        maturities: [num_array, required] Maturities in years; positive & STRICTLY INCREASING (same
            count as the columns of the yields).
        rates: [num_array, optional] Yields of ONE curve (decimals, same length as maturities); give
            rates OR panel, NOT both.
        panel: [matrix_handle, optional] Handle to a yield matrix [n_obs × n_maturities] (time
            series of curves; nelson_siegel+panel = Diebold-Li factor dynamics).
        method: [enum, optional] Fit method (default nelson_siegel; min pillars: NS 4 / svensson 6 /
            cubic 3).
        type: [enum, optional] Type of yields (default zero).
        tau_init: [number, optional] Initial decay value tau (nelson_siegel; > 0; default 1).
            Default ``1``.
        tau1_init: [number, optional] Initial value of the 1st decay tau1 (svensson; > 0; default
            1). Default ``1``.
        tau2_init: [number, optional] Initial value of the 2nd decay tau2 (svensson; > 0; default
            5). Default ``5``.
        weights: [num_array, optional] Positive weights per maturity (nelson_siegel/svensson; NOT
            cubic_spline); emphasis on liquid tenors.
        dates: [series_codes, optional] Date labels per row of the panel (count = panel rows);
            labels only, not model input.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "yc_fit: not implemented. The method card is in ./README.md."
    )


def yc_transform(
    *,
    object: Any,
    transform: Literal["spot", "forward", "discount", "pca"] | None = None,
    grid: Sequence[float] | None = None,
    horizon: float | None = None,
    compounding: Literal["continuous", "annual", "semi_annual"] | None = None,
    n_components: int | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``yc_transform`` -- METHOD-SELECTION card #210.

    Parametric yield-curve factor models (Nelson-Siegel / Svensson / cubic spline, Diebold-Li
    dynamics on a panel) + curve transforms (spot/forward/discount/PCA).

    Category 18-yield-curve; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to yc_fit$object: fitted yc_curve
            (spot/forward/discount) or panel matrix (pca).
        transform: [enum, optional] Transformation (default spot); spot/forward/discount require
            yc_curve; pca requires a panel matrix.
        grid: [num_array, optional] Maturity grid (positive maturities) for spot/forward/discount;
            None -> the curve's maturities.
        horizon: [number, optional] Forward-forward horizon (> 0) for transform='forward'; None ->
            instantaneous forward.
        compounding: [enum, optional] Compounding convention for transform='discount' (default
            continuous).
        n_components: [integer, optional] Number of principal components for transform='pca' (∈ [1,
            min(n_obs-1, n_maturities)]; default 3). Default ``3``.
        scale: [boolean, optional] Scaling of variables before the PCA (default False = covariance,
            standard in yield-curve PCA). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "yc_transform: not implemented. The method card is in ./README.md."
    )
