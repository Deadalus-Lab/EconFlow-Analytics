# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``structural_simultaneous_equation`` -- METHOD-SELECTION card #201.

#201 Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers

Category 13-dsge-general-equilibrium; module ``structural_simultaneous_equation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c13_dsge_general_equilibrium import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bimets_estimate",
    "bimets_multipliers",
    "bimets_simulate",
    "NODE_META",
    "wire_model",
]


def bimets_estimate(
    *,
    model: str,
    data: pd.DataFrame,
    tsrange: Any | None = None,
    estTech: Literal["OLS", "IV"] | None = None,
    iv: Any | None = None,
    eqList: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``bimets_estimate`` -- METHOD-SELECTION card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        model: [string, required] MDL model-string (MODEL... END· behaviorals with EQ>/COEFF>,
            identities with EQ>).
        data: [multiseries_handle, required] Handle to an mts (one column per variable)· covers ALL
            the vendog ∪ vexog of the model.
        tsrange: [raw, optional] Optional estimation period
            [startYear,startPeriod,endYear,endPeriod] (default = the TSRANGE of the MDL).
        estTech: [enum, optional] Estimation technique· OLS (default) or IV (Instrumental
            Variables).
        iv: [raw, optional] Character vector of instrumental-variables expressions (when
            estTech='IV' & they are not defined in the MDL).
        eqList: [series_codes, optional] Names of behavioral equations to estimate (default = all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bimets_estimate: not implemented. The method card is in ./README.md."
    )


def bimets_simulate(
    *,
    object: Any,
    tsrange: Any,
    simType: Literal["DYNAMIC", "FORECAST", "STATIC"] | None = None,
    simAlgo: Literal["GAUSS-SEIDEL", "NEWTON", "FULLNEWTON"] | None = None,
    stochastic: bool | None = None,
    stoch_replica: int | None = None,
    seed: int | None = None,
    simConvergence: float | None = None,
    simIterLimit: int | None = None,
) -> dict[str, Any]:
    """Node ``bimets_simulate`` -- METHOD-SELECTION card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an estimated BIMETS_MODEL (from bimets_estimate).
        tsrange: [raw, required] Simulation period [startYear,startPeriod,endYear,endPeriod] (within
            the data).
        simType: [enum, optional] Simulation type· DYNAMIC (default), FORECAST, STATIC.
        simAlgo: [enum, optional] Solution algorithm of the system (default GAUSS-SEIDEL).
        stochastic: [boolean, optional] False=deterministic SIMULATE· True=STOCHSIMULATE (auto
            NORM(0,SER) perturbation per behavioral -> mean/sd). Default ``False``.
        stoch_replica: [integer, optional] Number of stochastic replications when stochastic=True
            (>=2). Default ``100``.
        seed: [integer, optional] Reproducibility seed for the stochastic path (StochSeed). Default
            ``2025``.
        simConvergence: [number, optional] Convergence tolerance of the simulation (positive number·
            default 1e-5). Default ``1e-05``.
        simIterLimit: [integer, optional] Maximum iterations per period (default 100). Default
            ``100``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bimets_simulate: not implemented. The method card is in ./README.md."
    )


def bimets_multipliers(
    *,
    object: Any,
    tsrange: Any,
    target: Sequence[str],
    instrument: Sequence[str],
    mm_shock: float | None = None,
    simType: Literal["DYNAMIC", "FORECAST", "STATIC"] | None = None,
    simAlgo: Literal["GAUSS-SEIDEL", "NEWTON", "FULLNEWTON"] | None = None,
) -> dict[str, Any]:
    """Node ``bimets_multipliers`` -- METHOD-SELECTION card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-dsge-general-equilibrium; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an estimated BIMETS_MODEL (from bimets_estimate).
        tsrange: [raw, required] Period [startYear,startPeriod,endYear,endPeriod]·
            single-period=>impact, multi-period=>interim/dynamic.
        target: [series_codes, required] Endogenous target variables (⊆ vendog) for the multipliers.
        instrument: [series_codes, required] Exogenous instrument variables (⊆ vexog) that are
            perturbed.
        mm_shock: [number, optional] Relative perturbation of the instruments for the numerical
            computation (default 1e-5). Default ``1e-05``.
        simType: [enum, optional] Simulation type behind the multiplier matrix (default DYNAMIC).
        simAlgo: [enum, optional] Solution algorithm (default GAUSS-SEIDEL).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bimets_multipliers: not implemented. The method card is in ./README.md."
    )
