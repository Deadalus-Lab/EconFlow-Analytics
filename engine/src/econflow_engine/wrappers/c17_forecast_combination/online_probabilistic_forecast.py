# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``online_probabilistic_forecast`` -- method card #207.

#207 Online probabilistic forecast combination via CRPS-Learning (BOA/BEWA/ML-Poly/EWA aggregation
    of quantile expert forecasts)

Category 17-forecast-combination; module ``online_probabilistic_forecast``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "crps_learning",
    "NODE_META",
    "wire_model",
]


def crps_learning(
    *,
    y: np.ndarray,
    experts: Any,
    tau: Sequence[float],
    method: Literal["bewa", "boa", "ml_poly", "ewa"] | None = None,
    loss_function: Literal["quantile", "expectile", "percentage"] | None = None,
    loss_parameter: float | None = None,
    loss_gradient: bool | None = None,
    lead_time: int | None = None,
    forget_regret: float | None = None,
    fixed_share: float | None = None,
    gamma: float | None = None,
    soft_threshold: float | None = None,
    hard_threshold: float | None = None,
    allow_quantile_crossing: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``crps_learning`` -- method card #207.

    Online probabilistic forecast combination via CRPS-Learning (BOA/BEWA/ML-Poly/EWA aggregation of
    quantile expert forecasts).

    Category 17-forecast-combination; memory class ``light``.

    Args:
        y: [matrix_handle, required] Handle to a Tx1 matrix of realized values (probabilistic
            setting); without NA.
        experts: [raw_handle, required] Handle to a numeric 3D array [T x quantiles(P) x
            experts(K)]: experts[t,,k] = quantile forecasts of expert k at the tau levels;
            dim1==length(y), dim2==length(tau), K>=2, without NA.
        tau: [num_array, required] Probability levels in (0,1); STRICTLY increasing/unique; length P
            == dim(experts)[2].
        method: [enum, optional] Online-learning algorithm (default bewa· boa=full BOA, ewa=exp.
            weighting, ml_poly=ML-Poly).
        loss_function: [enum, optional] Loss (default quantile = pinball/CRPS scoring).
        loss_parameter: [number, optional] Scaling of the loss power (> 0; default 1). Default
            ``1``.
        loss_gradient: [boolean, optional] Linearized (gradient) version of the loss (default True).
            Default ``True``.
        lead_time: [integer, optional] Offset of expert forecasts (0 = t+1 at t); integer 0<=·<T.
            Default ``0``.
        forget_regret: [number, optional] Share of past regret to forget per iteration; in [0,1]
            (default 0). Default ``0``.
        fixed_share: [number, optional] Fixed share added to the weights; in [0,1] (1 => uniform;
            default 0). Default ``0``.
        gamma: [number, optional] Scaling of the learning rate (> 0; default 1). Default ``1``.
        soft_threshold: [number, optional] Soft-threshold on the weights (default -Inf = none).
            Default ``None``.
        hard_threshold: [number, optional] Hard-threshold on the weights (default -Inf = none).
            Default ``None``.
        allow_quantile_crossing: [boolean, optional] False => the forecasts are sorted ascending per
            t (default False). Default ``False``.
        seed: [integer, optional] Seed (integer >=0) — determinism of any grid sampling. Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "crps_learning: not implemented."
    )
