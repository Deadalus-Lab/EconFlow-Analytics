# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fixed_effects_ols`` -- method card #33.

#33 Fixed-effects OLS/IV + event study

Category 07-causality-policy; module ``fixed_effects_ols``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fx_coef_table",
    "fx_conf_int",
    "fx_fit",
    "fx_fit_stats",
    "fx_vcov",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fx_fit(
    *,
    fml: str,
    data: pd.DataFrame,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_fit`` -- method card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        fml: [formula, required] Formula, e.g. 'y ~ x1 + x2 | unit + time' (FE after the |; IV: |
            endo ~ inst).
        data: [df_handle, required] Handle to a DataFrame (panel/cross-section).
        vcov: [string, optional] vcov type, e.g. 'hetero' or 'cluster' (default: iid/by FE).
        cluster: [string, optional] Clustering variable name (or formula string) for robust SE.

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
        "fx_fit: not implemented."
    )


def fx_coef_table(
    *,
    object: Any,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_coef_table`` -- method card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_fit).
        vcov: [string, optional] Recompute SE with a different vcov without re-fitting.
        cluster: [string, optional] Clustering variable for the SE.

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
        "fx_coef_table: not implemented."
    )


def fx_conf_int(
    *,
    object: Any,
    level: float | None = None,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_conf_int`` -- method card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_fit).
        level: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        vcov: [string, optional] Alternative vcov for the intervals.
        cluster: [string, optional] Clustering variable.

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
        "fx_conf_int: not implemented."
    )


def fx_vcov(
    *,
    object: Any,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_vcov`` -- method card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_fit).
        vcov: [string, optional] vcov type (e.g. 'hetero','cluster').
        cluster: [string, optional] Clustering variable.

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
        "fx_vcov: not implemented."
    )


def fx_fit_stats(
    *,
    object: Any,
    type: str,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_fit_stats`` -- method card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_fit).
        type: [string, required] Statistic/test (required): e.g. 'r2','rmse','f','wald','ivwald'.
        vcov: [string, optional] Alternative vcov for test statistics.
        cluster: [string, optional] Clustering variable.

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
        "fx_fit_stats: not implemented."
    )
