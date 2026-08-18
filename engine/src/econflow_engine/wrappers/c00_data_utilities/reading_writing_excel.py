# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``reading_writing_excel`` -- METHOD-SELECTION card #97.

#97 Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write)

Category 00-data-utilities; module ``reading_writing_excel``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "xl_excel_sheets",
    "xl_read_excel",
    "xl_read_openxlsx",
    "xl_write_xlsx",
    "NODE_META",
    "wire_model",
]


def xl_read_excel(
    *,
    path: str,
    sheet: str | None = None,
    range: str | None = None,
    col_names: bool | None = None,
    skip: int | None = None,
) -> dict[str, Any]:
    """Node ``xl_read_excel`` -- METHOD-SELECTION card #97.

    Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to an.xls or.xlsx workbook.
        sheet: [string, optional] Sheet name or position (validated against excel_sheets); empty =
            1st sheet.
        range: [string, optional] A1/R1C1 range (e.g. 'B3:D87' or 'Sheet!B2:G14'); pre-validated
            with cellranger.
        col_names: [boolean, optional] 1st row = column names (default True). Default ``True``.
        skip: [integer, optional] Rows to skip at the start (default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "xl_read_excel: not implemented. The method card is in ./README.md."
    )


def xl_excel_sheets(
    *,
    path: str,
) -> dict[str, Any]:
    """Node ``xl_excel_sheets`` -- METHOD-SELECTION card #97.

    Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write).

    Category 00-data-utilities; memory class ``light``.

    Args:
        path: [path, required] Object-store path to a workbook; returns the sheet names (discovery).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "xl_excel_sheets: not implemented. The method card is in ./README.md."
    )


def xl_read_openxlsx(
    *,
    path: str,
    sheet: str | None = None,
    startRow: int | None = None,
    colNames: bool | None = None,
    rowNames: bool | None = None,
    detectDates: bool | None = None,
) -> dict[str, Any]:
    """Node ``xl_read_openxlsx`` -- METHOD-SELECTION card #97.

    Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to an.xlsx file (.xlsx ONLY — not legacy.xls).
        sheet: [string, optional] Sheet name or position (validated); default 1.
        startRow: [integer, optional] First row to read (default 1). Default ``1``.
        colNames: [boolean, optional] 1st row = column names (default True). Default ``True``.
        rowNames: [boolean, optional] 1st column = row names (default False). Default ``False``.
        detectDates: [boolean, optional] Auto-detect dates (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "xl_read_openxlsx: not implemented. The method card is in ./README.md."
    )


def xl_write_xlsx(
    *,
    x: pd.DataFrame,
    overwrite: bool | None = None,
    as_table: bool | None = None,
) -> dict[str, Any]:
    """Node ``xl_write_xlsx`` -- METHOD-SELECTION card #97.

    Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a DataFrame to write as.xlsx (terminal writer).
        overwrite: [boolean, optional] Overwrite an existing file (default True). Default ``True``.
        as_table: [boolean, optional] Write as an Excel Table (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "xl_write_xlsx: not implemented. The method card is in ./README.md."
    )
