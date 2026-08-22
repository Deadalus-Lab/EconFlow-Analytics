# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nonlinear_perfect_foresight`` -- method card #502.

#502 Nonlinear perfect-foresight models with occasionally binding constraints

Category 13-heterogeneous-agent-ge; module ``nonlinear_perfect_foresight``.

Reference implementation: econpizza.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ge_nonlinear_path",
    "NODE_META",
    "wire_model",
]


def ge_nonlinear_path(
    *,
    model: Any,
    shock: pd.DataFrame,
    horizon: int | None = None,
    constraints: Sequence[str] | None = None,
    tol: float | None = None,
    max_iter: int | None = None,
) -> dict[str, Any]:
    """Node ``ge_nonlinear_path`` -- method card #502.

    Nonlinear perfect-foresight models with occasionally binding constraints.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        model: [raw, required] Model specification.
        shock: [df_handle, required] Shock path.
        horizon: [integer, optional] Transition horizon. Default ``100``.
        constraints: [series_codes, optional] Occasionally binding constraints.
        tol: [number, optional] Convergence tolerance. Default ``1e-08``.
        max_iter: [integer, optional] Maximum Newton iterations. Default ``100``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ge_nonlinear_path: not implemented."
    )
