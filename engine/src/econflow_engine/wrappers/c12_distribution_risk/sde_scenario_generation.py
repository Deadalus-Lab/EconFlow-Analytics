# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sde_scenario_generation`` -- METHOD-SELECTION card #199.

#199 SDE scenario generation (short-rate/asset diffusion paths) + a martingale no-arbitrage check

Category 12-distribution-risk; module ``sde_scenario_generation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "esg_martingale_test",
    "esg_simdiff",
    "NODE_META",
    "wire_model",
]


def esg_simdiff(
    *,
    model: Literal["vasicek", "cir", "ou", "gbm"] | None = None,
    params: Any,
    T: float | None = None,
    n_steps: int | None = None,
    n_paths: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``esg_simdiff`` -- METHOD-SELECTION card #199.

    SDE scenario generation (short-rate/asset diffusion paths) + a martingale no-arbitrage check.

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        model: [enum, optional] SDE model (CLOSED set· default vasicek): vasicek/ou short-rate
            mean-reverting, cir positive short-rate, gbm asset. drift/diffusion HARD-CODED (NEVER an
            eval string).
        params: [raw, required] Named list of parameters per model: vasicek/ou {theta,mu,sigma,x0}·
            cir {kappa,theta,sigma,x0}· gbm {mu,sigma,x0}. sigma>0, speed>0, gbm x0>0, cir x0>=0
            (gates).
        T: [number, optional] Horizon (time) of the simulation, >0 (default 1). Default ``1``.
        n_steps: [integer, optional] Number of grid steps, >=2· the paths matrix has n_steps+1 rows
            (default 100). Default ``100``.
        n_paths: [integer, optional] Number of simulated paths, >=2 (columns of the matrix· default
            200). Default ``200``.
        seed: [integer, optional] Reproducibility seed (the simulation is stochastic· default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "esg_simdiff: not implemented. The method card is in ./README.md."
    )


def esg_martingale_test(
    *,
    object: Any,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``esg_martingale_test`` -- METHOD-SELECTION card #199.

    SDE scenario generation (short-rate/asset diffusion paths) + a martingale no-arbitrage check.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to esg_simdiff$object (list
            model/params/T/time/paths). Gate: model ∈ {vasicek,cir} (only these have a closed-form
            bond price).
        conf_level: [number, optional] Confidence level of the MC interval for the within_ci check,
            in (0,1) (default 0.95). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "esg_martingale_test: not implemented. The method card is in ./README.md."
    )
