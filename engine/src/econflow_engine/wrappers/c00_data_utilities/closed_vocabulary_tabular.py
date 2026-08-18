# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``closed_vocabulary_tabular`` -- METHOD-SELECTION card #101.

#101 CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice)

Category 00-data-utilities; module ``closed_vocabulary_tabular``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
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
    "dpl_arrange",
    "dpl_distinct",
    "dpl_filter",
    "dpl_group_by",
    "dpl_join",
    "dpl_mutate",
    "dpl_relocate",
    "dpl_rename",
    "dpl_select",
    "dpl_slice",
    "dpl_summarise",
    "NODE_META",
    "wire_model",
]


def dpl_filter(
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
    """Node ``dpl_filter`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_filter: not implemented. The method card is in ./README.md."
    )


def dpl_select(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    action: Literal["keep", "drop"] | None = None,
) -> dict[str, Any]:
    """Node ``dpl_select`` -- METHOD-SELECTION card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Column names to keep/drop.
        action: [enum, optional] keep=keep only these, drop=remove them (default keep).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dpl_select: not implemented. The method card is in ./README.md."
    )


def dpl_mutate(
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
    """Node ``dpl_mutate`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_mutate: not implemented. The method card is in ./README.md."
    )


def dpl_arrange(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    desc: bool | None = None,
) -> dict[str, Any]:
    """Node ``dpl_arrange`` -- METHOD-SELECTION card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Sort columns (in priority order).
        desc: [boolean, optional] Descending order (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dpl_arrange: not implemented. The method card is in ./README.md."
    )


def dpl_summarise(
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
    """Node ``dpl_summarise`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_summarise: not implemented. The method card is in ./README.md."
    )


def dpl_group_by(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
) -> dict[str, Any]:
    """Node ``dpl_group_by`` -- METHOD-SELECTION card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, required] Grouping key columns (terminal info node: keys/sizes/n).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dpl_group_by: not implemented. The method card is in ./README.md."
    )


def dpl_join(
    *,
    x: pd.DataFrame,
    y: pd.DataFrame,
    type: Literal["left", "inner", "full", "anti"] | None = None,
    by: Sequence[str],
) -> dict[str, Any]:
    """Node ``dpl_join`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_join: not implemented. The method card is in ./README.md."
    )


def dpl_distinct(
    *,
    df: pd.DataFrame,
    columns: Sequence[str] | None = None,
    keep_all: bool | None = None,
) -> dict[str, Any]:
    """Node ``dpl_distinct`` -- METHOD-SELECTION card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        columns: [series_codes, optional] Uniqueness columns (empty = full rows).
        keep_all: [boolean, optional] Keep all columns (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dpl_distinct: not implemented. The method card is in ./README.md."
    )


def dpl_rename(
    *,
    df: pd.DataFrame,
    old_names: Sequence[str],
    new_names: Sequence[str],
) -> dict[str, Any]:
    """Node ``dpl_rename`` -- METHOD-SELECTION card #101.

    CLOSED-vocabulary tabular manipulation
    (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice).

    Category 00-data-utilities; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a DataFrame.
        old_names: [series_codes, required] Existing column names.
        new_names: [series_codes, required] New names (same length, non-empty, no duplicates).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dpl_rename: not implemented. The method card is in ./README.md."
    )


def dpl_relocate(
    *,
    df: pd.DataFrame,
    columns: Sequence[str],
    before: Sequence[str] | None = None,
    after: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``dpl_relocate`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_relocate: not implemented. The method card is in ./README.md."
    )


def dpl_slice(
    *,
    df: pd.DataFrame,
    type: Literal["head", "tail", "index", "min", "max"] | None = None,
    n: int | None = None,
    order_by: str | None = None,
    start: int | None = None,
    end: int | None = None,
) -> dict[str, Any]:
    """Node ``dpl_slice`` -- METHOD-SELECTION card #101.

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
    """
    raise NotImplementedError(
        "dpl_slice: not implemented. The method card is in ./README.md."
    )
