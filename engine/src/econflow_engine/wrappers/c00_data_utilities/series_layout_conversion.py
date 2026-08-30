# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``series_layout_conversion`` -- method card #78.

#78 Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary)

Category 00-data-utilities; module ``series_layout_conversion``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ts_aggregate",
    "ts_combine",
    "ts_convert",
    "ts_fill_regular",
    "ts_lag_series",
    "ts_limit_span",
    "ts_rebase",
    "ts_standardize",
    "ts_stats",
    "ts_transform",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ts_convert(
    *,
    x: pd.Series,
    to: Literal["series", "indexed_series", "tidy_frame", "frame"] | None = None,
) -> dict[str, Any]:
    """Node ``ts_convert`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series (series/panel/frame — resolved from the
            registry).
        to: [enum, optional] Target representation (default series): series = a values+index series·
            indexed_series = an irregularly indexed series· tidy_frame = a long long-format table·
            frame = a wide table.

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
        "ts_convert: not implemented."
    )


def ts_transform(
    *,
    x: pd.Series,
    transform: Literal["diff", "pc", "pcy", "pca"] | None = None,
) -> dict[str, Any]:
    """Node ``ts_transform`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to transform.
        transform: [enum, optional] diff=plain difference, pc=q/q %, pcy=YoY %, pca=annualized pc.

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
        "ts_transform: not implemented."
    )


def ts_rebase(
    *,
    x: pd.Series,
    base: str | None = None,
) -> dict[str, Any]:
    """Node ``ts_rebase`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to convert into an index (index=1).
        base: [string, optional] Base DATE (e.g. '2015-01-01'); NOT a number. Empty = 1st period.

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
        "ts_rebase: not implemented."
    )


def ts_standardize(
    *,
    x: pd.Series,
    center: bool | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``ts_standardize`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to center/scale (z-scores).
        center: [boolean, optional] Subtract the mean (default True). Default ``True``.
        scale: [boolean, optional] Divide by sd (default True). Default ``True``.

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
        "ts_standardize: not implemented."
    )


def ts_lag_series(
    *,
    x: pd.Series,
    by: int | None = None,
) -> dict[str, Any]:
    """Node ``ts_lag_series`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to shift.
        by: [integer, optional] Integer number of periods to shift (negative = lead; default 1).
            Default ``1``.

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
        "ts_lag_series: not implemented."
    )


def ts_aggregate(
    *,
    x: pd.Series,
    to: Literal["year", "quarter", "month", "week", "day", "hour", "min", "sec"] | None = None,
    aggregate: Literal["mean", "sum", "first", "last"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``ts_aggregate`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to aggregate (ONLY towards a lower
            frequency).
        to: [enum, optional] Target frequency (it must be lower; default year).
        aggregate: [enum, optional] Aggregation function (default mean; flow->sum,
            index/rate->mean).
        na_rm: [boolean, optional] Ignore NA in the aggregation (default False). Default ``False``.

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
        "ts_aggregate: not implemented."
    )


def ts_limit_span(
    *,
    x: pd.Series,
    start: str | None = None,
    end: str | None = None,
    extend: bool | None = None,
) -> dict[str, Any]:
    """Node ``ts_limit_span`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series whose time span is to be limited.
        start: [string, optional] Start date (e.g. '2016-01-01'); at least one of start/end.
        end: [string, optional] End date (e.g. '2018-12-01').
        extend: [boolean, optional] Extend with NA beyond the data (default False). Default
            ``False``.

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
        "ts_limit_span: not implemented."
    )


def ts_fill_regular(
    *,
    x: pd.Series,
    fill: float | None = None,
) -> dict[str, Any]:
    """Node ``ts_fill_regular`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series with implicit time gaps to materialize.
        fill: [number, optional] Value used to fill the gaps (default NA).

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
        "ts_fill_regular: not implemented."
    )


def ts_combine(
    *,
    series1: pd.Series,
    series2: pd.Series,
    method: Literal["c", "bind"] | None = None,
) -> dict[str, Any]:
    """Node ``ts_combine`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        series1: [series_handle, required] Handle to the 1st series to combine.
        series2: [series_handle, required] Handle to the 2nd series to combine.
        method: [enum, optional] c=column-bind (aligned on time), bind=row-bind (default c).

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
        "ts_combine: not implemented."
    )


def ts_stats(
    *,
    x: pd.Series,
    spark: bool | None = None,
) -> dict[str, Any]:
    """Node ``ts_stats`` -- method card #78.

    Series layout conversion + basic transformations
    (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a series, for descriptive statistics per series.
        spark: [boolean, optional] Add a sparkline string (default False). Default ``False``.

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
        "ts_stats: not implemented."
    )
