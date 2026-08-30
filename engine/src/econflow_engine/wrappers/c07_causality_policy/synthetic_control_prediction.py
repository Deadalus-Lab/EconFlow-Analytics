# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_control_prediction`` -- method card #41.

#41 Synthetic Control + prediction intervals

Category 07-causality-policy; module ``synthetic_control_prediction``.

Reference implementation: scpi-pkg.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "scp_estimate",
    "scp_intervals",
    "scp_prepare_data",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def scp_prepare_data(
    *,
    df: pd.DataFrame,
    id_var: str,
    time_var: str,
    outcome_var: str,
    period_pre: Any,
    period_post: Any,
    unit_tr: Any,
    unit_co: Any,
    features: Sequence[str] | None = None,
    constant: bool | None = None,
    cointegrated_data: bool | None = None,
) -> dict[str, Any]:
    """Node ``scp_prepare_data`` -- method card #41.

    Synthetic Control + prediction intervals.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a long-format panel DataFrame.
        id_var: [string, required] Unit id column name.
        time_var: [string, required] Time column name.
        outcome_var: [string, required] Outcome column name.
        period_pre: [raw_handle, required] Handle to a vector of pre-treatment periods.
        period_post: [raw_handle, required] Handle to a vector of post-treatment periods.
        unit_tr: [raw_handle, required] Handle to the ID(s) of the treated unit.
        unit_co: [raw_handle, required] Handle to a vector of control-unit IDs (donor pool).
        features: [series_codes, optional] Feature column names (default: outcome).
        constant: [boolean, optional] Add a constant (default False). Default ``False``.
        cointegrated_data: [boolean, optional] Treat the data as cointegrated (default False).
            Default ``False``.

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
        "scp_prepare_data: not implemented."
    )


def scp_estimate(
    *,
    data: Any,
    V: Literal["separate", "pooled"] | None = None,
    solver: str | None = None,
) -> dict[str, Any]:
    """Node ``scp_estimate`` -- method card #41.

    Synthetic Control + prediction intervals.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [raw_handle, required] Handle to an scdata object (from scp_prepare_data).
        V: [enum, optional] Weighting matrix scheme (default separate).
        solver: [string, optional] Convex solver (default CLARABEL). Default ``'CLARABEL'``.

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
        "scp_estimate: not implemented."
    )


def scp_intervals(
    *,
    data: Any,
    V: Literal["separate", "pooled"] | None = None,
    u_sigma: Literal["HC1", "HC0", "HC2", "HC3", "HC4"] | None = None,
    e_method: Literal["all", "gaussian", "ls", "qreg"] | None = None,
    sims: int | None = None,
    solver: str | None = None,
) -> dict[str, Any]:
    """Node ``scp_intervals`` -- method card #41.

    Synthetic Control + prediction intervals.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        data: [raw_handle, required] Handle to an scdata (or scest) object.
        V: [enum, optional] Weighting matrix scheme (default separate).
        u_sigma: [enum, optional] In-sample (u) variance estimator (default HC1).
        e_method: [enum, optional] Out-of-sample (e) inference method (default all).
        sims: [integer, optional] Simulations for the prediction intervals (default 200). Default
            ``200``.
        solver: [string, optional] Convex solver (default CLARABEL). Default ``'CLARABEL'``.

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
        "scp_intervals: not implemented."
    )
