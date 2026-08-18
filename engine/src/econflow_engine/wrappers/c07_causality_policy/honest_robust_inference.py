# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``honest_robust_inference`` -- METHOD-SELECTION card #168.

#168 Honest/robust inference under relaxed parallel trends (Rambachan-Roth sensitivity analysis)

Category 07-causality-policy; module ``honest_robust_inference``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "honest_original_cs",
    "honest_relmag",
    "honest_smoothness",
    "NODE_META",
    "wire_model",
]


def honest_smoothness(
    *,
    betahat: Sequence[float],
    sigma: np.ndarray,
    numPrePeriods: int,
    numPostPeriods: int,
    Mvec: Sequence[float] | None = None,
    l_vec: Sequence[float] | None = None,
    method: Literal["FLCI", "Conditional", "C-F", "C-LF"] | None = None,
    monotonicityDirection: Literal["increasing", "decreasing"] | None = None,
    biasDirection: Literal["positive", "negative"] | None = None,
    alpha: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``honest_smoothness`` -- METHOD-SELECTION card #168.

    Honest/robust inference under relaxed parallel trends (Rambachan-Roth sensitivity analysis).

    Category 07-causality-policy; memory class ``light``.

    Args:
        betahat: [num_array, required] Event-study coefficients (pre+post, in time order) — num
            vector.
        sigma: [matrix_handle, required] Handle to the vcov of betahat (square matrix, dim =
            length(betahat)).
        numPrePeriods: [integer, required] Number of pre-treatment periods (>=1).
        numPostPeriods: [integer, required] Number of post-treatment periods (>=1); numPre+numPost =
            length(betahat).
        Mvec: [num_array, optional] Non-negative values of the smoothness bound M (max |second
            difference| of the trend). None -> auto grid.
        l_vec: [num_array, optional] Weights of the linear combination of post-period effects
            (length numPostPeriods; default = 1st post period).
        method: [enum, optional] CI method (default: FLCI for DeltaSD). C-LF/Conditional =
            simulation-based.
        monotonicityDirection: [enum, optional] Optional monotonicity restriction on the trend.
        biasDirection: [enum, optional] Optional sign restriction on the bias.
        alpha: [number, optional] Significance level in (0,1) (default 0.05 -> 95% CI). Default
            ``0.05``.
        seed: [integer, optional] Seed for the simulation-based CIs (C-LF/Conditional);
            reproducibility. Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "honest_smoothness: not implemented. The method card is in ./README.md."
    )


def honest_relmag(
    *,
    betahat: Sequence[float],
    sigma: np.ndarray,
    numPrePeriods: int,
    numPostPeriods: int,
    Mbarvec: Sequence[float] | None = None,
    l_vec: Sequence[float] | None = None,
    method: Literal["Conditional", "C-LF"] | None = None,
    monotonicityDirection: Literal["increasing", "decreasing"] | None = None,
    biasDirection: Literal["positive", "negative"] | None = None,
    alpha: float | None = None,
    gridPoints: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``honest_relmag`` -- METHOD-SELECTION card #168.

    Honest/robust inference under relaxed parallel trends (Rambachan-Roth sensitivity analysis).

    Category 07-causality-policy; memory class ``light``.

    Args:
        betahat: [num_array, required] Event-study coefficients (pre+post, in time order) — num
            vector.
        sigma: [matrix_handle, required] Handle to the vcov of betahat (square matrix, dim =
            length(betahat)).
        numPrePeriods: [integer, required] Number of pre-treatment periods (>=1; basis for the
            relative magnitude).
        numPostPeriods: [integer, required] Number of post-treatment periods (>=1); numPre+numPost =
            length(betahat).
        Mbarvec: [num_array, optional] Non-negative Mbar values (multiple of the max pre-trend
            violation). None -> auto grid.
        l_vec: [num_array, optional] Weights of the linear combination of post-period effects
            (length numPostPeriods; default = 1st post period).
        method: [enum, optional] CI method (default C-LF); simulation-based. Default ``'C-LF'``.
        monotonicityDirection: [enum, optional] Optional monotonicity restriction on the trend.
        biasDirection: [enum, optional] Optional sign restriction on the bias.
        alpha: [number, optional] Significance level in (0,1) (default 0.05 -> 95% CI). Default
            ``0.05``.
        gridPoints: [integer, optional] Number of points in the search grid (>=2); fewer =
            faster/coarser. Default ``1000``.
        seed: [integer, optional] Seed for the simulation-based CIs; reproducibility. Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "honest_relmag: not implemented. The method card is in ./README.md."
    )


def honest_original_cs(
    *,
    betahat: Sequence[float],
    sigma: np.ndarray,
    numPrePeriods: int,
    numPostPeriods: int,
    l_vec: Sequence[float] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``honest_original_cs`` -- METHOD-SELECTION card #168.

    Honest/robust inference under relaxed parallel trends (Rambachan-Roth sensitivity analysis).

    Category 07-causality-policy; memory class ``light``.

    Args:
        betahat: [num_array, required] Event-study coefficients (pre+post, in time order) — num
            vector.
        sigma: [matrix_handle, required] Handle to the vcov of betahat (square matrix, dim =
            length(betahat)).
        numPrePeriods: [integer, required] Number of pre-treatment periods (>=1).
        numPostPeriods: [integer, required] Number of post-treatment periods (>=1); numPre+numPost =
            length(betahat).
        l_vec: [num_array, optional] Weights of the linear combination of post-period effects
            (length numPostPeriods; default = 1st post period).
        alpha: [number, optional] Significance level in (0,1) (default 0.05 -> 95% CI). Default
            ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "honest_original_cs: not implemented. The method card is in ./README.md."
    )
