# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``transition_matrices`` -- method card #348.

#348 Rating and state transition matrices, generators and long-run behaviour

Category 41-credit-risk-default; module ``transition_matrices``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_generator",
    "cr_stationary_distribution",
    "cr_transition_matrix",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cr_transition_matrix(
    *,
    data: pd.DataFrame,
    id: str,
    state: str,
    date: str,
    estimator: Literal["cohort", "duration"] | None = None,
    horizon: float | None = None,
) -> dict[str, Any]:
    """Node ``cr_transition_matrix`` -- method card #348.

    Rating and state transition matrices, generators and long-run behaviour.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        data: [df_handle, required] Panel of state observations.
        id: [string, required] Column identifying the obligor.
        state: [string, required] Column holding the state.
        date: [string, required] Column holding the observation date.
        estimator: [enum, optional] Estimator. Default ``'duration'``.
        horizon: [number, optional] Horizon in years. Default ``1.0``.

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
        "cr_transition_matrix: not implemented."
    )


def cr_generator(
    *,
    transition_matrix: np.ndarray,
    method: Literal["log", "qo", "wa", "dae"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_generator`` -- method card #348.

    Rating and state transition matrices, generators and long-run behaviour.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        transition_matrix: [matrix_handle, required] Discrete transition matrix.
        method: [enum, optional] Embedding method. Default ``'qo'``.

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
        "cr_generator: not implemented."
    )


def cr_stationary_distribution(
    *,
    transition_matrix: np.ndarray,
) -> dict[str, Any]:
    """Node ``cr_stationary_distribution`` -- method card #348.

    Rating and state transition matrices, generators and long-run behaviour.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        transition_matrix: [matrix_handle, required] Transition matrix.

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
        "cr_stationary_distribution: not implemented."
    )
