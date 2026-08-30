# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sequence_jacobian`` -- method card #499.

#499 Sequence-space Jacobian: HANK, Krusell-Smith and RBC

Category 13-heterogeneous-agent-ge; module ``sequence_jacobian``.

Reference implementation: sequence-jacobian.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ge_ssj_irf",
    "ge_ssj_jacobians",
    "ge_ssj_steady_state",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ge_ssj_steady_state(
    *,
    model: Any,
    calibration: pd.DataFrame,
    targets: pd.DataFrame | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``ge_ssj_steady_state`` -- method card #499.

    Sequence-space Jacobian: HANK, Krusell-Smith and RBC.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``steady_state``, so a later node can consume it as a handle.

    Args:
        model: [raw, required] Model block specification.
        calibration: [df_handle, required] Parameter calibration.
        targets: [df_handle, optional] Steady-state targets to hit.
        tol: [number, optional] Convergence tolerance. Default ``1e-09``.

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
        "ge_ssj_steady_state: not implemented."
    )


def ge_ssj_jacobians(
    *,
    steady_state: Any,
    horizon: int | None = None,
    inputs: Sequence[str],
) -> dict[str, Any]:
    """Node ``ge_ssj_jacobians`` -- method card #499.

    Sequence-space Jacobian: HANK, Krusell-Smith and RBC.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``jacobians``, so a later node can consume it as a handle.

    Args:
        steady_state: [raw_handle, required] Handle to a solved steady state.
        horizon: [integer, optional] Truncation horizon. Default ``300``.
        inputs: [series_codes, required] Input variables to differentiate with respect to.

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
        "ge_ssj_jacobians: not implemented."
    )


def ge_ssj_irf(
    *,
    jacobians: Any,
    shock: str,
    persistence: float | None = None,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``ge_ssj_irf`` -- method card #499.

    Sequence-space Jacobian: HANK, Krusell-Smith and RBC.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        jacobians: [raw_handle, required] Handle to computed Jacobians.
        shock: [string, required] Shocked variable.
        persistence: [number, optional] Shock persistence. Default ``0.9``.
        horizon: [integer, optional] Response horizon. Default ``50``.

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
        "ge_ssj_irf: not implemented."
    )
