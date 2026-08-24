# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dsge_perturbation`` -- method card #503.

#503 Perturbation DSGE solution and Bayesian estimation from a model file

Category 13-heterogeneous-agent-ge; module ``dsge_perturbation``.

Reference implementation: gEconpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ge_dsge_estimate",
    "ge_dsge_solve",
    "ge_identification_check",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_dsge_solve(
    *,
    model: Any,
    calibration: pd.DataFrame,
    order: int | None = None,
    check_determinacy: bool | None = None,
) -> dict[str, Any]:
    """Node ``ge_dsge_solve`` -- method card #503.

    Perturbation DSGE solution and Bayesian estimation from a model file.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``solution``, so a later node can consume it as a handle.

    Args:
        model: [raw, required] Model specification.
        calibration: [df_handle, required] Parameter values.
        order: [integer, optional] Perturbation order. Default ``1``.
        check_determinacy: [boolean, optional] Verify the Blanchard-Kahn conditions. Default
            ``True``.

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
        "ge_dsge_solve: not implemented."
    )


def ge_dsge_estimate(
    *,
    solution: Any,
    data: pd.DataFrame,
    priors: pd.DataFrame,
    draws: int | None = None,
    warmup: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``ge_dsge_estimate`` -- method card #503.

    Perturbation DSGE solution and Bayesian estimation from a model file.

    Category 13-heterogeneous-agent-ge; memory class ``mcmc``.

    Registers its result under ``posterior``, so a later node can consume it as a handle.

    Args:
        solution: [raw_handle, required] Handle to a solved model.
        data: [df_handle, required] Observed series.
        priors: [df_handle, required] Prior specification.
        draws: [integer, optional] Posterior draws. Default ``10000``.
        warmup: [integer, optional] Warm-up draws. Default ``5000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "ge_dsge_estimate: not implemented."
    )


def ge_identification_check(
    *,
    solution: Any,
    method: Literal["rank", "sensitivity", "prior_posterior"] | None = None,
) -> dict[str, Any]:
    """Node ``ge_identification_check`` -- method card #503.

    Perturbation DSGE solution and Bayesian estimation from a model file.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        solution: [raw_handle, required] Handle to a solved model.
        method: [enum, optional] Identification diagnostic. Default ``'rank'``.

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
        "ge_identification_check: not implemented."
    )
