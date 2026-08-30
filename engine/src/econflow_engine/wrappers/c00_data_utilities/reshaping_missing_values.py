# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``reshaping_missing_values`` -- method card #102.

#102 Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest)

Category 00-data-utilities; module ``reshaping_missing_values``.

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
    "shape_complete_grid",
    "shape_dropna",
    "shape_explode",
    "shape_fillna",
    "shape_forward_fill",
    "shape_join_columns",
    "shape_melt",
    "shape_nest",
    "shape_pivot",
    "shape_split_column",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def shape_melt(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    names_to: Sequence[str] | None = None,
    values_to: str | None = None,
    names_prefix: str | None = None,
    names_sep: str | None = None,
    names_pattern: str | None = None,
    values_drop_na: bool | None = None,
) -> dict[str, Any]:
    """Node ``shape_melt`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a wide DataFrame.
        cols: [series_codes, required] Columns to fold into long form.
        names_to: [series_codes, optional] Key column name(s) (default 'name'; >1 requires
            names_sep/pattern).
        values_to: [string, optional] Value column name (default 'value').
        names_prefix: [string, optional] Prefix to strip from the names.
        names_sep: [string, optional] Separator for splitting the name into >1 names_to.
        names_pattern: [string, optional] Regex for extracting >1 names_to.
        values_drop_na: [boolean, optional] Drop rows with an NA value (default False). Default
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
        "shape_melt: not implemented."
    )


def shape_pivot(
    *,
    data: pd.DataFrame,
    names_from: Sequence[str],
    values_from: Sequence[str],
    id_cols: Sequence[str] | None = None,
    values_fill: Any | None = None,
    values_fn: (
        Literal[
            "none",
            "mean",
            "sum",
            "min",
            "max",
            "median",
            "length",
            "first",
            "last",
        ]
        | None
    ) = None,
    names_prefix: str | None = None,
    names_sep: str | None = None,
    names_sort: bool | None = None,
) -> dict[str, Any]:
    """Node ``shape_pivot`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a long DataFrame.
        names_from: [series_codes, required] Column(s) supplying the names of the new columns.
        values_from: [series_codes, required] Column(s) supplying the cell values.
        id_cols: [series_codes, optional] Row-identity columns; empty = inferred from the rest.
        values_fill: [raw, optional] Atomic scalar used to fill empty cells.
        values_fn: [enum, optional] Aggregator for a non-unique key (default none — REQUIRED if the
            key is non-unique).
        names_prefix: [string, optional] Prefix of the new columns (default ''). Default ``''``.
        names_sep: [string, optional] Separator for composite names (default '_'). Default ``'_'``.
        names_sort: [boolean, optional] Sort the new names (default False). Default ``False``.

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
        "shape_pivot: not implemented."
    )


def shape_split_column(
    *,
    data: pd.DataFrame,
    col: str,
    mode: Literal["delim", "position", "regex"] | None = None,
    delim: str | None = None,
    names: Sequence[str] | None = None,
    widths: Any | None = None,
    patterns: Any | None = None,
    too_few: str | None = None,
    too_many: str | None = None,
    names_sep: str | None = None,
    cols_remove: bool | None = None,
) -> dict[str, Any]:
    """Node ``shape_split_column`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        col: [string, required] One string column to split.
        mode: [enum, optional] delim=fixed separator, position=fixed widths, regex=patterns (default
            delim).
        delim: [string, optional] Separator (mode=delim).
        names: [series_codes, optional] Names of the new columns (mode=delim; or supply names_sep).
        widths: [raw, optional] NAMED numeric vector name->width (mode=position; unnamed=skip).
        patterns: [raw, optional] NAMED character vector name->regex (mode=regex).
        too_few: [string, optional] error/align_start/align_end/debug (default error). Default
            ``'error'``.
        too_many: [string, optional] error/drop/merge/debug (delim/position; NOT for regex). Default
            ``'error'``.
        names_sep: [string, optional] Auto-naming separator.
        cols_remove: [boolean, optional] Remove the original column (default True). Default
            ``True``.

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
        "shape_split_column: not implemented."
    )


def shape_join_columns(
    *,
    data: pd.DataFrame,
    col: str,
    cols: Sequence[str],
    sep: str | None = None,
    remove: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``shape_join_columns`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        col: [string, required] Name of the new united column.
        cols: [series_codes, required] Columns to paste.
        sep: [string, optional] Separator (default '_'). Default ``'_'``.
        remove: [boolean, optional] Remove the source columns (default True). Default ``True``.
        na_rm: [boolean, optional] Ignore NA in the paste (default False). Default ``False``.

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
        "shape_join_columns: not implemented."
    )


def shape_dropna(
    *,
    data: pd.DataFrame,
    cols: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``shape_dropna`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        cols: [series_codes, optional] Columns checked for NA (empty = all).

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
        "shape_dropna: not implemented."
    )


def shape_fillna(
    *,
    data: pd.DataFrame,
    replace: Any,
) -> dict[str, Any]:
    """Node ``shape_fillna`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        replace: [raw, required] NAMED list column->replacement value (one value per column).

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
        "shape_fillna: not implemented."
    )


def shape_forward_fill(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    direction: Literal["down", "up", "downup", "updown"] | None = None,
    by: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``shape_forward_fill`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        cols: [series_codes, required] Columns to LOCF/NOCB.
        direction: [enum, optional] down=LOCF, up=NOCB (default down).
        by: [series_codes, optional] Grouping columns (.by).

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
        "shape_forward_fill: not implemented."
    )


def shape_complete_grid(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    fill: Any | None = None,
) -> dict[str, Any]:
    """Node ``shape_complete_grid`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        cols: [series_codes, required] Columns whose combinations are all materialized.
        fill: [raw, optional] NAMED list column->value for the new rows.

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
        "shape_complete_grid: not implemented."
    )


def shape_nest(
    *,
    data: pd.DataFrame,
    by: Sequence[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Node ``shape_nest`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        by: [series_codes, required] Grouping columns.
        key: [string, optional] Name of the list-column (default 'data'). Default ``'data'``.

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
        "shape_nest: not implemented."
    )


def shape_explode(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    keep_empty: bool | None = None,
    names_sep: str | None = None,
) -> dict[str, Any]:
    """Node ``shape_explode`` -- method card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame with a list-column.
        cols: [series_codes, required] List-columns to flatten (they MUST be list-columns).
        keep_empty: [boolean, optional] Keep empty list-cells as an NA row (default False). Default
            ``False``.
        names_sep: [string, optional] Prefix for inner names.

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
        "shape_explode: not implemented."
    )
