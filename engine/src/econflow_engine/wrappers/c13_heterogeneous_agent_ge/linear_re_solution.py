# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``linear_re_solution`` -- method card #504.

#504 Linear rational-expectations solution and simulation

Category 13-heterogeneous-agent-ge; module ``linear_re_solution``.

Reference implementation: linearsolve.

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
    "ge_linear_re_solve",
    "ge_simulate_re",
    "NODE_META",
    "wire_model",
]


def ge_linear_re_solve(
    *,
    A: np.ndarray,
    B: np.ndarray,
    C: np.ndarray | None = None,
    n_forward: int,
    method: Literal["klein", "gensys", "blanchard_kahn"] | None = None,
) -> dict[str, Any]:
    """Node ``ge_linear_re_solve`` -- method card #504.

    Linear rational-expectations solution and simulation.

    Category 13-heterogeneous-agent-ge; memory class ``heavy``.

    Registers its result under ``solution``, so a later node can consume it as a handle.

    Args:
        A: [matrix_handle, required] Coefficient matrix on future variables.
        B: [matrix_handle, required] Coefficient matrix on current variables.
        C: [matrix_handle, optional] Coefficient matrix on shocks.
        n_forward: [integer, required] Number of forward-looking variables.
        method: [enum, optional] Solution method. Default ``'klein'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ge_linear_re_solve: not implemented."
    )


def ge_simulate_re(
    *,
    solution: Any,
    n_periods: int | None = None,
    shock_cov: np.ndarray | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``ge_simulate_re`` -- method card #504.

    Linear rational-expectations solution and simulation.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        solution: [raw_handle, required] Handle to a solved system.
        n_periods: [integer, optional] Simulation length. Default ``1000``.
        shock_cov: [matrix_handle, optional] Shock covariance matrix.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ge_simulate_re: not implemented."
    )
