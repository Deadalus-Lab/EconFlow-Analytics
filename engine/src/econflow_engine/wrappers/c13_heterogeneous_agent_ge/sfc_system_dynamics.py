# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sfc_system_dynamics`` -- method card #505.

#505 Stock-flow-consistent and system-dynamics solvers

Category 13-heterogeneous-agent-ge; module ``sfc_system_dynamics``.

Reference implementation: pysolve3.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ge_accounting_check",
    "ge_sfc_solve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_sfc_solve(
    *,
    model: Any,
    parameters: pd.DataFrame,
    initial: pd.DataFrame | None = None,
    n_periods: int | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``ge_sfc_solve`` -- method card #505.

    Stock-flow-consistent and system-dynamics solvers.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        model: [raw, required] Model specification.
        parameters: [df_handle, required] Parameter values.
        initial: [df_handle, optional] Initial stocks.
        n_periods: [integer, optional] Simulation periods. Default ``100``.
        tol: [number, optional] Within-period convergence tolerance. Default ``1e-10``.

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
        "ge_sfc_solve: not implemented."
    )


def ge_accounting_check(
    *,
    solution: Any,
    tolerance: float | None = None,
) -> dict[str, Any]:
    """Node ``ge_accounting_check`` -- method card #505.

    Stock-flow-consistent and system-dynamics solvers.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        solution: [raw_handle, required] Handle to a solved model.
        tolerance: [number, optional] Tolerance for the accounting residual. Default ``1e-08``.

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
        "ge_accounting_check: not implemented."
    )
