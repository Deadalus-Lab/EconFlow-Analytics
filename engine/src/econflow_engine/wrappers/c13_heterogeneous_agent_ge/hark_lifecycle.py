# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hark_lifecycle`` -- method card #500.

#500 Heterogeneous-agent consumption-saving and life-cycle models

Category 13-heterogeneous-agent-ge; module ``hark_lifecycle``.

Reference implementation: econ-ark.

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
    "ge_lifecycle_simulate",
    "ge_lifecycle_solve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_lifecycle_solve(
    *,
    calibration: pd.DataFrame,
    model: (
        Literal[
            "perfect_foresight",
            "buffer_stock",
            "life_cycle",
            "portfolio_choice",
        ]
        | None
    ) = None,
    n_grid: int | None = None,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``ge_lifecycle_solve`` -- method card #500.

    Heterogeneous-agent consumption-saving and life-cycle models.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``solution``, so a later node can consume it as a handle.

    Args:
        calibration: [df_handle, required] Model parameters.
        model: [enum, optional] Model variant. Default ``'buffer_stock'``.
        n_grid: [integer, optional] Grid points for the wealth state. Default ``100``.
        horizon: [integer, optional] Life-cycle horizon; 0 = infinite. Default ``0``.

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
        "ge_lifecycle_solve: not implemented."
    )


def ge_lifecycle_simulate(
    *,
    solution: Any,
    n_agents: int | None = None,
    n_periods: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``ge_lifecycle_simulate`` -- method card #500.

    Heterogeneous-agent consumption-saving and life-cycle models.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        solution: [raw_handle, required] Handle to a solved model.
        n_agents: [integer, optional] Simulated agents. Default ``10000``.
        n_periods: [integer, optional] Simulation periods. Default ``1000``.
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
        "ge_lifecycle_simulate: not implemented."
    )
