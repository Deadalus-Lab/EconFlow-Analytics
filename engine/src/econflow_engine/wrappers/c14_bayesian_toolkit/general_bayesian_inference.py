# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``general_bayesian_inference`` -- METHOD-SELECTION card #68.

#68 General Bayesian inference via Stan (NUTS-only + convergence gate)

Category 14-bayesian-toolkit; module ``general_bayesian_inference``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_compile",
    "rs_fit",
    "rs_sample",
    "rs_syntax_check",
    "NODE_META",
    "wire_model",
]


def rs_syntax_check(
    *,
    model_code: str,
    model_name: str | None = None,
) -> dict[str, Any]:
    """Node ``rs_syntax_check`` -- METHOD-SELECTION card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        model_code: [string, required] Stan model AS A STRING (sandboxed DSL, never evaluated as
            code here)· cheap stanc syntax pre-gate.
        model_name: [string, optional] Model name (default anon_model). Default ``'anon_model'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_syntax_check: not implemented. The method card is in ./README.md."
    )


def rs_compile(
    *,
    model_code: str,
    model_name: str | None = None,
) -> dict[str, Any]:
    """Node ``rs_compile`` -- METHOD-SELECTION card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model_code: [string, required] Stan model AS A STRING· stan_model compile (~40s) -> compiled
            stanmodel handle.
        model_name: [string, optional] Model name (default anon_model). Default ``'anon_model'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_compile: not implemented. The method card is in ./README.md."
    )


def rs_sample(
    *,
    model: Any,
    data: Any,
    seed: int,
    chains: int | None = None,
    iter: int | None = None,
    algorithm: Literal["NUTS"] | None = None,
    rhat_max: float | None = None,
    ess_min: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``rs_sample`` -- METHOD-SELECTION card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        model: [raw_handle, required] Handle to a compiled stanmodel (from rs_compile).
        data: [raw_handle, required] Handle to a GENUINE named data list matching the Stan data
            block (numeric, finite).
        seed: [integer, required] REQUIRED seed (the Stan RNG is not affected by set.seed· default
            RANDOM).
        chains: [integer, optional] Number of chains (>=2 required: the split-R-hat of one chain
            does not detect non-convergence). Default ``2``.
        iter: [integer, optional] Iterations per chain (default 1000, warmup=iter/2). Default
            ``1000``.
        algorithm: [enum, optional] Sampler (only NUTS).
        rhat_max: [number, optional] Threshold of the rank-normalized split-R-hat (hard gate,
            default 1.01). Default ``1.01``.
        ess_min: [number, optional] Minimum Bulk/Tail ESS (hard gate, default 400). Default ``400``.
        allow_nonconvergence: [boolean, optional] True -> returns draws with converged=False instead
            of stopping on non-convergence. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_sample: not implemented. The method card is in ./README.md."
    )


def rs_fit(
    *,
    model_code: str,
    data: Any,
    model_name: str | None = None,
    seed: int,
    chains: int | None = None,
    iter: int | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``rs_fit`` -- METHOD-SELECTION card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        model_code: [string, required] Stan model AS A STRING· one-shot compile + sample.
        data: [raw_handle, required] Handle to a named data list (Stan data block).
        model_name: [string, optional] Model name (default anon_model). Default ``'anon_model'``.
        seed: [integer, required] REQUIRED seed (reproducibility of the Stan RNG).
        chains: [integer, optional] Number of chains (>=2). Default ``2``.
        iter: [integer, optional] Iterations per chain. Default ``1000``.
        allow_nonconvergence: [boolean, optional] True -> converged=False instead of stop. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_fit: not implemented. The method card is in ./README.md."
    )
