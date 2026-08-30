# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``regularisation_decomposition_space`` -- method card #129.

#129 Regularisation/decomposition & analysis of space-time series (turning points + Kendall info; a
    full descriptive table including normality; diff/LOESS trend-seasonal decomposition)

Category 01-preparation-prechecks; module ``regularisation_decomposition_space``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ps_decompose",
    "ps_descriptives",
    "ps_turning_points",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ps_turning_points(
    *,
    x: pd.Series,
    calc_proba: bool | None = None,
) -> dict[str, Any]:
    """Node ``ps_turning_points`` -- method card #129.

    Regularisation/decomposition & analysis of space-time series (turning points + Kendall info; a
    full descriptive table including normality; diff/LOESS trend-seasonal decomposition).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series/ts (no NA, >=3 obs & >=3
            unique values).
        calc_proba: [boolean, optional] Compute the Kendall probability/information per turning
            point (default True). Default ``True``.

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
        "ps_turning_points: not implemented."
    )


def ps_descriptives(
    *,
    x: pd.Series,
    basic: bool | None = None,
    desc: bool | None = None,
    norm: bool | None = None,
    p: float | None = None,
) -> dict[str, Any]:
    """Node ``ps_descriptives`` -- method card #129.

    Regularisation/decomposition & analysis of space-time series (turning points + Kendall info; a
    full descriptive table including normality; diff/LOESS trend-seasonal decomposition).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series/ts (or a numeric multi-series df).
        basic: [boolean, optional] Basic statistics: nbr.val/null/na/min/max/range/sum (default
            True). Default ``True``.
        desc: [boolean, optional] Descriptive statistics:
            median/mean/SE.mean/CI.mean/var/std.dev/coef.var (default True). Default ``True``.
        norm: [boolean, optional] Normality: skewness/kurtosis/Shapiro-Wilk (default False). Default
            ``False``.
        p: [number, optional] Confidence level of CI.mean, in (0,1) (default 0.95). Default
            ``0.95``.

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
        "ps_descriptives: not implemented."
    )


def ps_decompose(
    *,
    x: pd.Series,
    method: Literal["loess", "diff"] | None = None,
    type: Literal["additive", "multiplicative"] | None = None,
    lag: int | None = None,
    order: int | None = None,
    ends: Literal["fill", "NAs", "drop"] | None = None,
    s_window: Any | None = None,
    s_degree: int | None = None,
    t_window: int | None = None,
    t_degree: int | None = None,
    robust: bool | None = None,
    trend: bool | None = None,
) -> dict[str, Any]:
    """Node ``ps_decompose`` -- method card #129.

    Regularisation/decomposition & analysis of space-time series (turning points + Kendall info; a
    full descriptive table including normality; diff/LOESS trend-seasonal decomposition).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a regular univariate ts (no NA· loess: frequency>1 &
            >=2 full periods).
        method: [enum, optional] loess=STL trend-seasonal· diff=differencing filter that removes the
            trend (default loess).
        type: [enum, optional] Model· loess supports additive ONLY (default additive).
        lag: [integer, optional] [diff] differencing lag, positive integer (default 1). Default
            ``1``.
        order: [integer, optional] [diff] differencing order, positive integer (default 1). Default
            ``1``.
        ends: [enum, optional] [diff] handling of the non-computable initial values (default fill).
        s_window: [raw, optional] [loess] "periodic" or an odd number (default "periodic").
        s_degree: [integer, optional] [loess] seasonal polynomial degree, 0 or 1 (default 0).
            Default ``0``.
        t_window: [integer, optional] [loess] trend window width (odd· default data-driven).
        t_degree: [integer, optional] [loess] trend polynomial degree 0/1/2 (default 2). Default
            ``2``.
        robust: [boolean, optional] [loess] robust regression (default False). Default ``False``.
        trend: [boolean, optional] [loess] compute a separate trend component (default False).
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
        "ps_decompose: not implemented."
    )
