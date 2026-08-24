# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``agent_based_macro`` -- method card #506.

#506 Agent-based macro and stock-flow-consistent ABM simulation

Category 13-heterogeneous-agent-ge; module ``agent_based_macro``.

Reference implementation: mesa.

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
    "ge_abm_calibrate",
    "ge_abm_simulate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_abm_simulate(
    *,
    model: Any,
    parameters: pd.DataFrame,
    n_agents: int | None = None,
    n_periods: int | None = None,
    n_seeds: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``ge_abm_simulate`` -- method card #506.

    Agent-based macro and stock-flow-consistent ABM simulation.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        model: [raw, required] Model specification.
        parameters: [df_handle, required] Parameter values.
        n_agents: [integer, optional] Number of agents. Default ``1000``.
        n_periods: [integer, optional] Simulation periods. Default ``500``.
        n_seeds: [integer, optional] Ensemble size. Default ``30``.
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
        "ge_abm_simulate: not implemented."
    )


def ge_abm_calibrate(
    *,
    model: Any,
    targets: pd.DataFrame,
    bounds: pd.DataFrame,
    n_seeds: int | None = None,
    method: Literal["grid", "latin_hypercube", "surrogate", "differential_evolution"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``ge_abm_calibrate`` -- method card #506.

    Agent-based macro and stock-flow-consistent ABM simulation.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        model: [raw, required] Model specification.
        targets: [df_handle, required] Target moments.
        bounds: [df_handle, required] Parameter bounds.
        n_seeds: [integer, optional] Ensemble size per evaluation. Default ``10``.
        method: [enum, optional] Search method. Default ``'surrogate'``.
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
        "ge_abm_calibrate: not implemented."
    )
