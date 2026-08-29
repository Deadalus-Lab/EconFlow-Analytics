# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``structural_simultaneous_equation`` -- method card #201.

#201 Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers

Category 13-heterogeneous-agent-ge; module ``structural_simultaneous_equation``.

Reference implementation: modelflowib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sem_estimate",
    "sem_multipliers",
    "sem_simulate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sem_estimate(
    *,
    model: str,
    data: pd.DataFrame,
    tsrange: Any | None = None,
    estTech: Literal["OLS", "IV"] | None = None,
    iv: Any | None = None,
    eqList: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``sem_estimate`` -- method card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        model: [string, required] MDL model-string (MODEL... END· behaviorals with EQ>/COEFF>,
            identities with EQ>).
        data: [multiseries_handle, required] Handle to an panel (one column per variable)· covers
            ALL the vendog ∪ vexog of the model.
        tsrange: [raw, optional] Optional estimation period
            [startYear,startPeriod,endYear,endPeriod] (default = the TSRANGE of the MDL).
        estTech: [enum, optional] Estimation technique· OLS (default) or IV (Instrumental
            Variables).
        iv: [raw, optional] Character vector of instrumental-variables expressions (when
            estTech='IV' & they are not defined in the MDL).
        eqList: [series_codes, optional] Names of behavioral equations to estimate (default = all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sem_estimate: not implemented."
    )


def sem_simulate(
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
    """Node ``sem_simulate`` -- method card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an estimated BIMETS_MODEL (from sem_estimate).
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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sem_simulate: not implemented."
    )


def sem_multipliers(
    *,
    object: Any,
    tsrange: Any,
    target: Sequence[str],
    instrument: Sequence[str],
    mm_shock: float | None = None,
    simType: Literal["DYNAMIC", "FORECAST", "STATIC"] | None = None,
    simAlgo: Literal["GAUSS-SEIDEL", "NEWTON", "FULLNEWTON"] | None = None,
) -> dict[str, Any]:
    """Node ``sem_multipliers`` -- method card #201.

    Structural simultaneous-equation macro-econometric model (FRB/US-style): MDL definition →
    estimate → deterministic/stochastic simulation → policy multipliers.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an estimated BIMETS_MODEL (from sem_estimate).
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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sem_multipliers: not implemented."
    )
