# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fast_transformation`` -- method card #103.

#103 Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform)

Category 00-data-utilities; module ``fast_transformation``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fast_aggregate",
    "fast_cumsum",
    "fast_diff",
    "fast_growth",
    "fast_lag",
    "fast_scale",
    "fast_summary",
    "fast_transform",
    "fast_within",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fast_growth(
    *,
    x: pd.Series,
    n: int | None = None,
    diff: int | None = None,
    logdiff: bool | None = None,
    scale: float | None = None,
    power: float | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``fast_growth`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] Lag order (default 1). Default ``1``.
        diff: [integer, optional] Iteration order >=1 (default 1). Default ``1``.
        logdiff: [boolean, optional] Log-difference growth (default False = exact %). Default
            ``False``.
        scale: [number, optional] Scale (default 100 = percentages). Default ``100``.
        power: [number, optional] Annualization exponent (default 1). Default ``1``.
        g: [series_codes, optional] Panel grouping labels (length = observations).
        t: [num_array, optional] Time vector (without g: NO duplicates).
        fill: [number, optional] Padding value (default NA).

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
        "fast_growth: not implemented."
    )


def fast_diff(
    *,
    x: pd.Series,
    n: int | None = None,
    diff: int | None = None,
    log: bool | None = None,
    rho: float | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``fast_diff`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] Lag order (default 1). Default ``1``.
        diff: [integer, optional] Iteration order >=1 (default 1). Default ``1``.
        log: [boolean, optional] Log-difference (default False). Default ``False``.
        rho: [number, optional] Quasi-differencing coef (rho=1 = plain difference). Default ``1``.
        g: [series_codes, optional] Panel grouping labels.
        t: [num_array, optional] Time vector.
        fill: [number, optional] Padding value (default NA).

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
        "fast_diff: not implemented."
    )


def fast_lag(
    *,
    x: pd.Series,
    n: int | None = None,
    g: Sequence[str] | None = None,
    t: Sequence[float] | None = None,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``fast_lag`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        n: [integer, optional] n>0 lag, n<0 lead (default 1). Default ``1``.
        g: [series_codes, optional] Panel grouping labels.
        t: [num_array, optional] Time vector.
        fill: [number, optional] Padding value (default NA).

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
        "fast_lag: not implemented."
    )


def fast_cumsum(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    na_rm: bool | None = None,
    fill: bool | None = None,
) -> dict[str, Any]:
    """Node ``fast_cumsum`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (grouped cumsum).
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        fill: [boolean, optional] Fill NA with the previous sum (default False). Default ``False``.

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
        "fast_cumsum: not implemented."
    )


def fast_scale(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    na_rm: bool | None = None,
    mean: float | None = None,
    sd: float | None = None,
) -> dict[str, Any]:
    """Node ``fast_scale`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (within-group z-scores).
        w: [num_array, optional] Weights (length = observations).
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        mean: [number, optional] Target mean (default 0). Default ``0``.
        sd: [number, optional] Target sd (default 1; a constant series -> NaN, honestly). Default
            ``1``.

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
        "fast_scale: not implemented."
    )


def fast_within(
    *,
    x: pd.Series,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    na_rm: bool | None = None,
    mean: float | None = None,
    theta: float | None = None,
) -> dict[str, Any]:
    """Node ``fast_within`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        g: [series_codes, optional] Panel grouping labels (within/demean).
        w: [num_array, optional] Weights.
        na_rm: [boolean, optional] Ignore NA (default True). Default ``True``.
        mean: [number, optional] Value added back after centering (default 0). Default ``0``.
        theta: [number, optional] theta=1 plain within, 0<theta<1 quasi-demean (RE-style). Default
            ``1``.

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
        "fast_within: not implemented."
    )


def fast_aggregate(
    *,
    X: pd.DataFrame,
    by: Sequence[str],
    FUN: (
        Literal[
            "mean",
            "sum",
            "median",
            "min",
            "max",
            "sd",
            "first",
            "last",
            "prod",
            "nobs",
        ]
        | None
    ) = None,
    cols: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``fast_aggregate`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        X: [df_handle, required] Handle to a (panel) DataFrame to aggregate.
        by: [series_codes, required] Grouping columns (names).
        FUN: [enum, optional] Fast statistical function per numeric column (default mean).
        cols: [series_codes, optional] Subset of columns to aggregate.
        w: [num_array, optional] Weights; ONLY the weighted fast-stat funcs
            (mean/sum/median/sd/prod) use them — first/last/min/max/nobs ignore them (warning).

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
        "fast_aggregate: not implemented."
    )


def fast_summary(
    *,
    x: pd.DataFrame,
    g: Sequence[str] | None = None,
    w: Sequence[float] | None = None,
    higher: bool | None = None,
) -> dict[str, Any]:
    """Node ``fast_summary`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a DataFrame (per-column summary).
        g: [series_codes, optional] Grouping labels (routed as 'by' for a DataFrame — otherwise
            SILENTLY IGNORED).
        w: [num_array, optional] Weights.
        higher: [boolean, optional] Add Skew & Kurt (default False). Default ``False``.

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
        "fast_summary: not implemented."
    )


def fast_transform(
    *,
    x: pd.Series,
    STATS: Sequence[float],
    FUN: (
        Literal[
            "-",
            "replace_na",
            "replace_fill",
            "replace",
            "-+",
            "/",
            "%",
            "+",
            "*",
            "%%",
            "-%%",
        ]
        | None
    ) = None,
    g: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``fast_transform`` -- method card #103.

    Fast (grouped/panel) data transformation
    (growth/diff/lag/cumsum/scale/within/aggregate/summary/generic transform).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series.
        STATS: [num_array, required] Statistics (atomic if g=None; one per group if grouped).
        FUN: [enum, optional] Sweep-out operation (default '-' center); '-+' requires groups.
        g: [series_codes, optional] Panel grouping labels.

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
        "fast_transform: not implemented."
    )
