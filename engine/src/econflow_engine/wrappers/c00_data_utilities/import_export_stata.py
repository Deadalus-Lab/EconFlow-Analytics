# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``import_export_stata`` -- METHOD-SELECTION card #100.

#100 Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation

Category 00-data-utilities; module ``import_export_stata``.

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
    "hvn_as_factor",
    "hvn_read_sas",
    "hvn_read_spss",
    "hvn_read_stata",
    "hvn_write_stata",
    "NODE_META",
    "wire_model",
]


def hvn_read_stata(
    *,
    path: str,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``hvn_read_stata`` -- METHOD-SELECTION card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a Stata.dta file.
        encoding: [string, optional] Character encoding (e.g. 'latin1'); empty = auto.
        col_select: [series_codes, optional] Column names to read; empty = all.
        skip: [integer, optional] Rows to skip (default 0). Default ``0``.
        n_max: [integer, optional] Maximum number of rows; empty = Inf (all).
        name_repair: [enum, optional] Name-repair policy (default unique).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hvn_read_stata: not implemented. The method card is in ./README.md."
    )


def hvn_read_spss(
    *,
    path: str,
    user_na: bool | None = None,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``hvn_read_spss`` -- METHOD-SELECTION card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to an SPSS.sav/.zsav file.
        user_na: [boolean, optional] Keep user-defined missing values as labels (default False).
            Default ``False``.
        encoding: [string, optional] Character encoding; empty = auto.
        col_select: [series_codes, optional] Column names to read; empty = all.
        skip: [integer, optional] Rows to skip (default 0). Default ``0``.
        n_max: [integer, optional] Maximum number of rows; empty = Inf.
        name_repair: [enum, optional] Name policy (default unique).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hvn_read_spss: not implemented. The method card is in ./README.md."
    )


def hvn_read_sas(
    *,
    path: str,
    catalog_file: str | None = None,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``hvn_read_sas`` -- METHOD-SELECTION card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a SAS.sas7bdat file.
        catalog_file: [path, optional] Object-store path to a.sas7bcat catalog (value formats);
            empty = none.
        encoding: [string, optional] Character encoding; empty = auto.
        col_select: [series_codes, optional] Column names to read; empty = all.
        skip: [integer, optional] Rows to skip (default 0). Default ``0``.
        n_max: [integer, optional] Maximum number of rows; empty = Inf.
        name_repair: [enum, optional] Name policy (default unique).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hvn_read_sas: not implemented. The method card is in ./README.md."
    )


def hvn_write_stata(
    *,
    data: pd.DataFrame,
    version: int | None = None,
    label: str | None = None,
) -> dict[str, Any]:
    """Node ``hvn_write_stata`` -- METHOD-SELECTION card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (>=1 column) to write as.dta (terminal
            writer).
        version: [integer, optional] Stata dta format version in 8-15 (default 14). Default ``14``.
        label: [string, optional] Dataset label <= 80 bytes; empty = none.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hvn_write_stata: not implemented. The method card is in ./README.md."
    )


def hvn_as_factor(
    *,
    x: Any,
    levels: Literal["default", "labels", "values", "both"] | None = None,
    ordered: bool | None = None,
    only_labelled: bool | None = None,
) -> dict[str, Any]:
    """Node ``hvn_as_factor`` -- METHOD-SELECTION card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor
    materialisation.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        x: [raw_handle, required] Handle to a labelled vector OR a DataFrame with labelled columns.
        levels: [enum, optional] Source of the factor levels (default = labels where present).
        ordered: [boolean, optional] Ordered factor (default False). Default ``False``.
        only_labelled: [boolean, optional] Labelled columns only (DataFrame path; default True).
            Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hvn_as_factor: not implemented. The method card is in ./README.md."
    )
