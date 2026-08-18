# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``extreme_value_theory`` -- METHOD-SELECTION card #191.

#191 Extreme Value Theory — GEV block maxima & GP/PP/Gumbel/Exponential threshold exceedances +
    return levels

Category 12-distribution-risk; module ``extreme_value_theory``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "evt_fevd",
    "evt_return_level",
    "evt_threshold_diag",
    "NODE_META",
    "wire_model",
]


def evt_fevd(
    *,
    x: Sequence[float],
    type: Literal["GEV", "GP", "PP", "Gumbel", "Exponential"] | None = None,
    method: Literal["MLE", "GMLE", "Lmoments"] | None = None,
    threshold: float | None = None,
    time_units: str | None = None,
    period_basis: str | None = None,
) -> dict[str, Any]:
    """Node ``evt_fevd`` -- METHOD-SELECTION card #191.

    Extreme Value Theory — GEV block maxima & GP/PP/Gumbel/Exponential threshold exceedances +
    return levels.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [num_array, required] Numeric series: block maxima (GEV/Gumbel) or the whole series for
            threshold-exceedances (GP/PP/Exponential).
        type: [enum, optional] EVT family: GEV=block-maxima (default)·
            GP/PP/Exponential=threshold-exceedances (they require a threshold)· Gumbel=block-maxima
            with shape=0. Default ``'GEV'``.
        method: [enum, optional] Estimator: MLE (default)· GMLE (Beta-prior/penalty on the shape)·
            Lmoments (ONLY GEV/GP). Bayesian is NOT exposed. Default ``'MLE'``.
        threshold: [number, optional] Single threshold u for GP/PP/Exponential (< max(x)· >=5
            exceedances). Ignored for GEV/Gumbel.
        time_units: [string, optional] DETERMINES npy (e.g. 'days'->365.25, 'months'->12, '12/year')
            — i.e. the BASIS of the return periods in threshold models. Default ``'days'``.
        period_basis: [string, optional] Return period unit (default 'year'). Default ``'year'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "evt_fevd: not implemented. The method card is in ./README.md."
    )


def evt_return_level(
    *,
    object: Any,
    return_periods: Sequence[float] | None = None,
    do_ci: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``evt_return_level`` -- METHOD-SELECTION card #191.

    Extreme Value Theory — GEV block maxima & GP/PP/Gumbel/Exponential threshold exceedances +
    return levels.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an fevd fit (from evt_fevd$object).
        return_periods: [num_array, optional] Vector of return periods in period_basis units· each
            value > 1 (default [10,50,100]).
        do_ci: [boolean, optional] True (default) -> normal-approx (delta) CIs· False -> only point
            estimates. Default ``True``.
        conf_level: [number, optional] Confidence level in (0,1) for the CIs (default 0.95). Default
            ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "evt_return_level: not implemented. The method card is in ./README.md."
    )


def evt_threshold_diag(
    *,
    x: Sequence[float],
    type: Literal["GP", "PP", "Exponential"] | None = None,
    nint: int | None = None,
    alpha: float | None = None,
    r: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``evt_threshold_diag`` -- METHOD-SELECTION card #191.

    Extreme Value Theory — GEV block maxima & GP/PP/Gumbel/Exponential threshold exceedances +
    return levels.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        x: [num_array, required] Numeric series for threshold-selection diagnostics (mean residual
            life + parameter stability).
        type: [enum, optional] Model for the parameter-stability grid (default GP). Default
            ``'GP'``.
        nint: [integer, optional] Number of points in the threshold grid (>=2· default 10). Default
            ``10``.
        alpha: [number, optional] Significance level for the pointwise CIs (default 0.05). Default
            ``0.05``.
        r: [num_array, optional] Threshold range [r1,r2] (r1<r2<max(x)) for the stability grid
            (default: quantiles 0.75..0.99 of x).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "evt_threshold_diag: not implemented. The method card is in ./README.md."
    )
