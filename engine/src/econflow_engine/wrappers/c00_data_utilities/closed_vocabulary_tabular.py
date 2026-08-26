# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``closed_vocabulary_tabular`` -- method card #101.

#101 CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice)

Category 00-data-utilities; module ``closed_vocabulary_tabular``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tab_aggregate",
    "tab_assign",
    "tab_drop_duplicates",
    "tab_filter",
    "tab_group_by",
    "tab_join",
    "tab_rename",
    "tab_reorder_columns",
    "tab_select",
    "tab_slice_rows",
    "tab_sort",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tab_filter(
    *,
    df: pd.DataFrame,
    column: str,
    op: (
        Literal[
            "eq",
            "neq",
            "lt",
            "lte",
            "gt",
            "gte",
            "in",
            "not_in",
            "between",
            "is_na",
            "not_na",
        ]
        | None
    ) = None,
    value: Any | None = None,
) -> dict[str, Any]:
    """Node ``tab_filter`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to the DataFrame to filter.
        column: [string, required] ONE column (name) the predicate is applied to.
        op: [enum, optional] Closed comparator (default eq).
        value: [raw, optional] Comparison value: scalar (eq..gte), array (in/not_in), [low,high]
            (between); empty for is_na/not_na. A numeric column vs a non-numeric value is blocked
            (silent 0-rows guard).

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
        "tab_filter: not implemented."
    )


def tab_select(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    action: Literal["keep", "drop"] | None = None,
) -> dict[str, Any]:
    """Node ``tab_select`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Column names to keep/drop.
        action: [enum, optional] keep=keep only these, drop=remove them (default keep).

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
        "tab_select: not implemented."
    )


def tab_assign(
    *,
    df: pd.DataFrame,
    new_column: str,
    op: (
        Literal[
            "log",
            "log10",
            "sqrt",
            "abs",
            "exp",
            "cumsum",
            "lag",
            "lead",
            "add",
            "sub",
            "mul",
            "div",
        ]
        | None
    ) = None,
    columns: Sequence[str],
    constant: float | None = None,
) -> dict[str, Any]:
    """Node ``tab_assign`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        new_column: [string, required] Name of the new column.
        op: [enum, optional] Closed unary/binary transformation (default log).
        columns: [series_codes, required] 1 column (unary/lag/lead) or 2 columns (binary) or 1
            column + constant.
        constant: [number, optional] Constant for a binary op with 1 column.

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
        "tab_assign: not implemented."
    )


def tab_sort(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    desc: bool | None = None,
) -> dict[str, Any]:
    """Node ``tab_sort`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Sort columns (in priority order).
        desc: [boolean, optional] Descending order (default False). Default ``False``.

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
        "tab_sort: not implemented."
    )


def tab_aggregate(
    *,
    df: pd.DataFrame,
    stat: (
        Literal[
            "mean",
            "median",
            "sd",
            "var",
            "min",
            "max",
            "sum",
            "IQR",
            "n",
            "n_distinct",
            "first",
            "last",
        ]
        | None
    ) = None,
    column: str | None = None,
    by: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tab_aggregate`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        stat: [enum, optional] Closed aggregator (default mean).
        column: [string, optional] Column to aggregate (not needed for stat='n').
        by: [series_codes, optional] Grouping columns (per-group summarise via.by).

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
        "tab_aggregate: not implemented."
    )


def tab_group_by(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
) -> dict[str, Any]:
    """Node ``tab_group_by`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Grouping key columns (terminal info node: keys/sizes/n).

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
        "tab_group_by: not implemented."
    )


def tab_join(
    *,
    x: pd.DataFrame,
    y: pd.DataFrame,
    type: Literal["left", "inner", "full", "anti"] | None = None,
    by: Sequence[str],
) -> dict[str, Any]:
    """Node ``tab_join`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to the left DataFrame.
        y: [df_handle, required] Handle to the right DataFrame.
        type: [enum, optional] Join type (default left).
        by: [series_codes, required] Shared key columns (they must exist in BOTH).

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
        "tab_join: not implemented."
    )


def tab_drop_duplicates(
    *,
    df: pd.DataFrame,
    columns: Sequence[str] | None = None,
    keep_all: bool | None = None,
) -> dict[str, Any]:
    """Node ``tab_drop_duplicates`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, optional] Uniqueness columns (empty = full rows).
        keep_all: [boolean, optional] Keep all columns (default True). Default ``True``.

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
        "tab_drop_duplicates: not implemented."
    )


def tab_rename(
    *,
    df: pd.DataFrame,
    old_names: Sequence[str],
    new_names: Sequence[str],
) -> dict[str, Any]:
    """Node ``tab_rename`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        old_names: [series_codes, required] Existing column names.
        new_names: [series_codes, required] New names (same length, non-empty, no duplicates).

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
        "tab_rename: not implemented."
    )


def tab_reorder_columns(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    before: Sequence[str] | None = None,
    after: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tab_reorder_columns`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Columns to move.
        before: [series_codes, optional] Place BEFORE this column (not together with after).
        after: [series_codes, optional] Place AFTER this column (not together with before).

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
        "tab_reorder_columns: not implemented."
    )


def tab_slice_rows(
    *,
    df: pd.DataFrame,
    type: Literal["head", "tail", "index", "min", "max"] | None = None,
    n: int | None = None,
    order_by: str | None = None,
    start: int | None = None,
    end: int | None = None,
) -> dict[str, Any]:
    """Node ``tab_slice_rows`` -- method card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        type: [enum, optional] Positional selection — DETERMINISTIC (no sampling; default head).
        n: [integer, optional] Number of rows (head/tail/min/max). Default ``1``.
        order_by: [string, optional] Ordering column (required for min/max).
        start: [integer, optional] Start position (type=index).
        end: [integer, optional] End position >= start (type=index).

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
        "tab_slice_rows: not implemented."
    )
