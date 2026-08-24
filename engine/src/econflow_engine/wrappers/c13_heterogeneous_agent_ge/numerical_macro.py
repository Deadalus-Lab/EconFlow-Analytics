# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``numerical_macro`` -- method card #501.

#501 Numerical macro building blocks

Category 13-heterogeneous-agent-ge; module ``numerical_macro``.

Reference implementation: quantecon.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ge_discrete_dp",
    "ge_discretise_ar1",
    "ge_linear_quadratic",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_discretise_ar1(
    *,
    rho: float,
    sigma: float,
    n_states: int | None = None,
    method: Literal["tauchen", "rouwenhorst", "tauchen_hussey"] | None = None,
    n_std: float | None = None,
) -> dict[str, Any]:
    """Node ``ge_discretise_ar1`` -- method card #501.

    Numerical macro building blocks.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        rho: [number, required] Autoregressive coefficient.
        sigma: [number, required] Innovation standard deviation.
        n_states: [integer, optional] Number of states. Default ``7``.
        method: [enum, optional] Discretisation method. Default ``'rouwenhorst'``.
        n_std: [number, optional] Grid width in standard deviations for Tauchen. Default ``3.0``.

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
        "ge_discretise_ar1: not implemented."
    )


def ge_linear_quadratic(
    *,
    transition: np.ndarray,
    control: np.ndarray,
    control_cost: np.ndarray,
    state_cost: np.ndarray,
    beta: float | None = None,
) -> dict[str, Any]:
    """Node ``ge_linear_quadratic`` -- method card #501.

    Numerical macro building blocks.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        transition: [matrix_handle, required] State transition matrix.
        control: [matrix_handle, required] Control matrix.
        control_cost: [matrix_handle, required] Control cost matrix.
        state_cost: [matrix_handle, required] State cost matrix.
        beta: [number, optional] Discount factor. Default ``0.95``.

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
        "ge_linear_quadratic: not implemented."
    )


def ge_discrete_dp(
    *,
    rewards: np.ndarray,
    transitions: np.ndarray,
    beta: float | None = None,
    method: (
        Literal[
            "value_iteration",
            "policy_iteration",
            "modified_policy_iteration",
        ]
        | None
    ) = None,
) -> dict[str, Any]:
    """Node ``ge_discrete_dp`` -- method card #501.

    Numerical macro building blocks.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        rewards: [matrix_handle, required] Reward matrix over states and actions.
        transitions: [matrix_handle, required] Transition probabilities.
        beta: [number, optional] Discount factor. Default ``0.95``.
        method: [enum, optional] Solution method. Default ``'policy_iteration'``.

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
        "ge_discrete_dp: not implemented."
    )
