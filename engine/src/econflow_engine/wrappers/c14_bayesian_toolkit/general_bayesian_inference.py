# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``general_bayesian_inference`` -- method card #68.

#68 General Bayesian inference via Stan (NUTS-only + convergence gate)

Category 14-bayesian-toolkit; module ``general_bayesian_inference``.

Reference implementation: cmdstanpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "stan_compile",
    "stan_fit",
    "stan_sample",
    "stan_syntax_check",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def stan_syntax_check(
    *,
    model_code: str,
    model_name: str | None = None,
) -> dict[str, Any]:
    """Node ``stan_syntax_check`` -- method card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        model_code: [string, required] Stan model AS A STRING (sandboxed DSL, never evaluated as
            code here)· cheap stanc syntax pre-gate.
        model_name: [string, optional] Model name (default anon_model). Default ``'anon_model'``.

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
        "stan_syntax_check: not implemented."
    )


def stan_compile(
    *,
    model_code: str,
    model_name: str | None = None,
) -> dict[str, Any]:
    """Node ``stan_compile`` -- method card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model_code: [string, required] Stan model AS A STRING· stan_model compile (~40s) -> compiled
            stanmodel handle.
        model_name: [string, optional] Model name (default anon_model). Default ``'anon_model'``.

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
        "stan_compile: not implemented."
    )


def stan_sample(
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
    """Node ``stan_sample`` -- method card #68.

    General Bayesian inference via Stan (NUTS-only + convergence gate).

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        model: [raw_handle, required] Handle to a compiled stanmodel (from stan_compile).
        data: [raw_handle, required] Handle to a GENUINE named data list matching the Stan data
            block (numeric, finite).
        seed: [integer, required] REQUIRED seed (the Stan RNG is not affected by seeded· default
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
        "stan_sample: not implemented."
    )


def stan_fit(
    *,
    model_code: str,
    data: Any,
    model_name: str | None = None,
    seed: int,
    chains: int | None = None,
    iter: int | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``stan_fit`` -- method card #68.

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
        "stan_fit: not implemented."
    )
