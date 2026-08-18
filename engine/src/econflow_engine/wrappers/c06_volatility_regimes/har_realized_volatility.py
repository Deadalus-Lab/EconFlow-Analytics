# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``har_realized_volatility`` -- METHOD-SELECTION card #157.

#157 HAR realized-volatility models (HAR/HARJ/HARQ/HARQ-J) — estimation, rolling OOS forecasting,
    simulation

Category 06-volatility-regimes; module ``har_realized_volatility``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "har_estimate",
    "har_forecast",
    "har_simulate",
    "NODE_META",
    "wire_model",
]


def har_estimate(
    *,
    RM: Sequence[float],
    periods: Sequence[int] | None = None,
    type: Literal["HAR", "HARJ", "HARQ", "HARQ-J"] | None = None,
    BPV: Sequence[float] | None = None,
    RQ: Sequence[float] | None = None,
    periodsJ: Sequence[int] | None = None,
    periodsRQ: Sequence[int] | None = None,
    insanityFilter: bool | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``har_estimate`` -- METHOD-SELECTION card #157.

    HAR realized-volatility models (HAR/HARJ/HARQ/HARQ-J) — estimation, rolling OOS forecasting,
    simulation.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        RM: [num_array, required] Realized measure of the integrated volatility (positive realized
            variance series, e.g. from hf_realized_var· without NA).
        periods: [int_array, optional] Lags of the HAR components (Corsi 2009: [1,5,22] =
            daily/weekly/monthly). Default ``[1, 5, 22]``.
        type: [enum, optional] HAR type: HAR (vanilla), HARJ (jump), HARQ (measurement-error
            corrected), HARQ-J. Default ``'HAR'``.
        BPV: [num_array, optional] Continuous/jump component (bipower variation)· REQUIRED for
            HARJ/HARQ-J (same length as RM).
        RQ: [num_array, optional] Realized quarticity· REQUIRED for HARQ/HARQ-J (same length as RM).
        periodsJ: [int_array, optional] Lags for the jump component (HARJ/HARQ-J).
        periodsRQ: [int_array, optional] Lags for the realized quarticity component (HARQ/HARQ-J).
        insanityFilter: [boolean, optional] Insanity filter on the fitted values (BPQ 2016 footnote
            17). Default ``True``.
        h: [integer, optional] Realized variance aggregation horizon (1=none, 5=weekly, 22=monthly).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "har_estimate: not implemented. The method card is in ./README.md."
    )


def har_forecast(
    *,
    RM: Sequence[float],
    periods: Sequence[int] | None = None,
    nRoll: int | None = None,
    nAhead: int | None = None,
    type: Literal["HAR", "HARJ", "HARQ", "HARQ-J"] | None = None,
    windowType: Literal["rolling", "fixed", "increasing", "expanding"] | None = None,
    BPV: Sequence[float] | None = None,
    RQ: Sequence[float] | None = None,
    periodsJ: Sequence[int] | None = None,
    periodsRQ: Sequence[int] | None = None,
    insanityFilter: bool | None = None,
    h: int | None = None,
) -> dict[str, Any]:
    """Node ``har_forecast`` -- METHOD-SELECTION card #157.

    HAR realized-volatility models (HAR/HARJ/HARQ/HARQ-J) — estimation, rolling OOS forecasting,
    simulation.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        RM: [num_array, required] Realized measure (positive realized variance series· without NA).
        periods: [int_array, optional] Lags of the HAR components (default [1,5,22]). Default ``[1,
            5, 22]``.
        nRoll: [integer, optional] Number of rolling out-of-sample forecasts (>=1). Default ``10``.
        nAhead: [integer, optional] Length of each rolling forecast (>=1)· must be 1 when h>1.
            Default ``1``.
        type: [enum, optional] HAR model type to estimate and forecast. Default ``'HAR'``.
        windowType: [enum, optional] Estimation window type: rolling/fixed or increasing/expanding.
            Default ``'rolling'``.
        BPV: [num_array, optional] Continuous/jump component· REQUIRED for HARJ/HARQ-J (same length
            as RM).
        RQ: [num_array, optional] Realized quarticity· REQUIRED for HARQ/HARQ-J (same length as RM).
        periodsJ: [int_array, optional] Lags jump component (HARJ/HARQ-J).
        periodsRQ: [int_array, optional] Lags realized quarticity (HARQ/HARQ-J).
        insanityFilter: [boolean, optional] Insanity filter on the forecasted values (BPQ 2016
            footnote 17). Default ``True``.
        h: [integer, optional] Aggregation horizon (1=none)· when h>1 then nAhead=1. Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "har_forecast: not implemented. The method card is in ./README.md."
    )


def har_simulate(
    *,
    len: int | None = None,
    periods: Sequence[int] | None = None,
    coef: Sequence[float] | None = None,
    errorTermSD: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``har_simulate`` -- METHOD-SELECTION card #157.

    HAR realized-volatility models (HAR/HARJ/HARQ/HARQ-J) — estimation, rolling OOS forecasting,
    simulation.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        len: [integer, optional] Length of the simulated process (>=1). Default ``1500``.
        periods: [int_array, optional] Lags used to build the HAR model (default [1,5,22]). Default
            ``[1, 5, 22]``.
        coef: [num_array, optional] Coefficients: length = length(periods)+1 (intercept + one per
            period). Default ``[0.01, 0.36, 0.28, 0.28]``.
        errorTermSD: [number, optional] Standard deviation of the error term (>0). Default
            ``0.001``.
        seed: [integer, optional] Reproducibility seed (stochastic process). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "har_simulate: not implemented. The method card is in ./README.md."
    )
