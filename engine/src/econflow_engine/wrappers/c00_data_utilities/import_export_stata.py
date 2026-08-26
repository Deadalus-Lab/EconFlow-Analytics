# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``import_export_stata`` -- method card #100.

#100 Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation

Category 00-data-utilities; module ``import_export_stata``.

Reference implementation: pyreadstat.

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
    "sfile_labels_to_categorical",
    "sfile_read_sas",
    "sfile_read_spss",
    "sfile_read_stata",
    "sfile_write_stata",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sfile_read_stata(
    *,
    path: str,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``sfile_read_stata`` -- method card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read path: a string of length 1, NOT a directory, existing; write path: the parent dir
          exists + a POST-gate that it was written
        - the data to write must be a frame with at least one column; version a single integer in
          8-15; and the label either unset or at most 80 bytes
        - sfile_labels_to_categorical: a non-df input MUST be labelled (otherwise forcats silently
          turns every vector into a factor)

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sfile_read_stata: not implemented."
    )


def sfile_read_spss(
    *,
    path: str,
    user_na: bool | None = None,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``sfile_read_spss`` -- method card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read path: a string of length 1, NOT a directory, existing; write path: the parent dir
          exists + a POST-gate that it was written
        - the data to write must be a frame with at least one column; version a single integer in
          8-15; and the label either unset or at most 80 bytes
        - sfile_labels_to_categorical: a non-df input MUST be labelled (otherwise forcats silently
          turns every vector into a factor)

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sfile_read_spss: not implemented."
    )


def sfile_read_sas(
    *,
    path: str,
    catalog_file: str | None = None,
    encoding: str | None = None,
    col_select: Sequence[str] | None = None,
    skip: int | None = None,
    n_max: int | None = None,
    name_repair: Literal["unique", "minimal", "check_unique", "universal"] | None = None,
) -> dict[str, Any]:
    """Node ``sfile_read_sas`` -- method card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read path: a string of length 1, NOT a directory, existing; write path: the parent dir
          exists + a POST-gate that it was written
        - the data to write must be a frame with at least one column; version a single integer in
          8-15; and the label either unset or at most 80 bytes
        - sfile_labels_to_categorical: a non-df input MUST be labelled (otherwise forcats silently
          turns every vector into a factor)

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sfile_read_sas: not implemented."
    )


def sfile_write_stata(
    *,
    data: pd.DataFrame,
    version: int | None = None,
    label: str | None = None,
) -> dict[str, Any]:
    """Node ``sfile_write_stata`` -- method card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (>=1 column) to write .dta (terminal
            writer).
        version: [integer, optional] Stata dta format version in 8-15 (default 14). Default ``14``.
        label: [string, optional] Dataset label <= 80 bytes; empty = none.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read path: a string of length 1, NOT a directory, existing; write path: the parent dir
          exists + a POST-gate that it was written
        - the data to write must be a frame with at least one column; version a single integer in
          8-15; and the label either unset or at most 80 bytes
        - sfile_labels_to_categorical: a non-df input MUST be labelled (otherwise forcats silently
          turns every vector into a factor)

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sfile_write_stata: not implemented."
    )


def sfile_labels_to_categorical(
    *,
    x: Any,
    levels: Literal["default", "labels", "values", "both"] | None = None,
    ordered: bool | None = None,
    only_labelled: bool | None = None,
) -> dict[str, Any]:
    """Node ``sfile_labels_to_categorical`` -- method card #100.

    Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata +
    labelled-to-categorical materialisation.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read path: a string of length 1, NOT a directory, existing; write path: the parent dir
          exists + a POST-gate that it was written
        - the data to write must be a frame with at least one column; version a single integer in
          8-15; and the label either unset or at most 80 bytes
        - sfile_labels_to_categorical: a non-df input MUST be labelled (otherwise forcats silently
          turns every vector into a factor)

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "sfile_labels_to_categorical: not implemented."
    )
