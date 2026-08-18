# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tidy_reshaping_missing`` -- METHOD-SELECTION card #102.

#102 Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest)

Category 00-data-utilities; module ``tidy_reshaping_missing``.

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
    "tidyr_complete",
    "tidyr_drop_na",
    "tidyr_fill",
    "tidyr_nest",
    "tidyr_pivot_longer",
    "tidyr_pivot_wider",
    "tidyr_replace_na",
    "tidyr_separate_wider",
    "tidyr_unite",
    "tidyr_unnest",
    "NODE_META",
    "wire_model",
]


def tidyr_pivot_longer(
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
    """Node ``tidyr_pivot_longer`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_pivot_longer: not implemented. The method card is in ./README.md."
    )


def tidyr_pivot_wider(
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
    """Node ``tidyr_pivot_wider`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_pivot_wider: not implemented. The method card is in ./README.md."
    )


def tidyr_separate_wider(
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
    """Node ``tidyr_separate_wider`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_separate_wider: not implemented. The method card is in ./README.md."
    )


def tidyr_unite(
    *,
    data: pd.DataFrame,
    col: str,
    cols: Sequence[str],
    sep: str | None = None,
    remove: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_unite`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_unite: not implemented. The method card is in ./README.md."
    )


def tidyr_drop_na(
    *,
    data: pd.DataFrame,
    cols: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_drop_na`` -- METHOD-SELECTION card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        cols: [series_codes, optional] Columns checked for NA (empty = all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tidyr_drop_na: not implemented. The method card is in ./README.md."
    )


def tidyr_replace_na(
    *,
    data: pd.DataFrame,
    replace: Any,
) -> dict[str, Any]:
    """Node ``tidyr_replace_na`` -- METHOD-SELECTION card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        replace: [raw, required] NAMED list column->replacement value (one value per column).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tidyr_replace_na: not implemented. The method card is in ./README.md."
    )


def tidyr_fill(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    direction: Literal["down", "up", "downup", "updown"] | None = None,
    by: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_fill`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_fill: not implemented. The method card is in ./README.md."
    )


def tidyr_complete(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    fill: Any | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_complete`` -- METHOD-SELECTION card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        cols: [series_codes, required] Columns whose combinations are all materialized.
        fill: [raw, optional] NAMED list column->value for the new rows.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tidyr_complete: not implemented. The method card is in ./README.md."
    )


def tidyr_nest(
    *,
    data: pd.DataFrame,
    by: Sequence[str],
    key: str | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_nest`` -- METHOD-SELECTION card #102.

    Tidy-data reshaping & missing-value handling
    (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest).

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame.
        by: [series_codes, required] Grouping columns.
        key: [string, optional] Name of the list-column (default 'data'). Default ``'data'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "tidyr_nest: not implemented. The method card is in ./README.md."
    )


def tidyr_unnest(
    *,
    data: pd.DataFrame,
    cols: Sequence[str],
    keep_empty: bool | None = None,
    names_sep: str | None = None,
) -> dict[str, Any]:
    """Node ``tidyr_unnest`` -- METHOD-SELECTION card #102.

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
    """
    raise NotImplementedError(
        "tidyr_unnest: not implemented. The method card is in ./README.md."
    )
