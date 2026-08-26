# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``reading_delimited_fixed`` -- method card #96.

#96 Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics

Category 00-data-utilities; module ``reading_delimited_fixed``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "read_csv_data",
    "read_delimited",
    "read_fwf_data",
    "read_parse_problems",
    "read_tsv_data",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def read_csv_data(
    *,
    path: str,
    col_types: str | None = None,
    na: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``read_csv_data`` -- method card #96.

    Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a CSV file (comma-separated).
        col_types: [string, optional] Compact column-spec string (e.g. 'Dd', 'dci'); empty =
            auto-guess.
        na: [series_codes, optional] Strings treated as NA (default ['', 'NA']).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - path: a non-empty string, NOT a directory, existing, size>0 bytes
        - POST-gate ncol>0 (a whitespace-only file yields a silent 0x0 frame)
        - col_types unset, a compact string, or a full column spec; the missing-value markers a
          non-empty list of strings with no blank entry; and read_delimited takes a delimiter of
          EXACTLY one character

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "read_csv_data: not implemented."
    )


def read_tsv_data(
    *,
    path: str,
    col_types: str | None = None,
    na: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``read_tsv_data`` -- method card #96.

    Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a TSV file (tab-separated).
        col_types: [string, optional] Compact column-spec string; empty = auto-guess.
        na: [series_codes, optional] Strings treated as NA (default ['', 'NA']).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - path: a non-empty string, NOT a directory, existing, size>0 bytes
        - POST-gate ncol>0 (a whitespace-only file yields a silent 0x0 frame)
        - col_types unset, a compact string, or a full column spec; the missing-value markers a
          non-empty list of strings with no blank entry; and read_delimited takes a delimiter of
          EXACTLY one character

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "read_tsv_data: not implemented."
    )


def read_delimited(
    *,
    path: str,
    delim: str,
    col_types: str | None = None,
    na: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``read_delimited`` -- method card #96.

    Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a delimited file.
        delim: [string, required] ONE delimiter character (e.g. ';', '|', '\\t').
        col_types: [string, optional] Compact column-spec string; empty = auto-guess.
        na: [series_codes, optional] Strings treated as NA (default ['', 'NA']).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - path: a non-empty string, NOT a directory, existing, size>0 bytes
        - POST-gate ncol>0 (a whitespace-only file yields a silent 0x0 frame)
        - col_types unset, a compact string, or a full column spec; the missing-value markers a
          non-empty list of strings with no blank entry; and read_delimited takes a delimiter of
          EXACTLY one character

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "read_delimited: not implemented."
    )


def read_fwf_data(
    *,
    path: str,
    col_types: str | None = None,
    na: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``read_fwf_data`` -- method card #96.

    Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        path: [path, required] Object-store path to a fixed-width file (column bounds auto-guessed).
        col_types: [string, optional] Compact column-spec string; empty = auto-guess.
        na: [series_codes, optional] Strings treated as NA (default ['', 'NA']).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - path: a non-empty string, NOT a directory, existing, size>0 bytes
        - POST-gate ncol>0 (a whitespace-only file yields a silent 0x0 frame)
        - col_types unset, a compact string, or a full column spec; the missing-value markers a
          non-empty list of strings with no blank entry; and read_delimited takes a delimiter of
          EXACTLY one character

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "read_fwf_data: not implemented."
    )


def read_parse_problems(
    *,
    path: str,
    format: Literal["csv", "tsv", "delim"] | None = None,
    delim: str | None = None,
    col_types: str | None = None,
) -> dict[str, Any]:
    """Node ``read_parse_problems`` -- method card #96.

    Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics.

    Category 00-data-utilities; memory class ``light``.

    Args:
        path: [path, required] Object-store path for a re-read + parse-problem diagnosis (no data
            payload).
        format: [enum, optional] Read format (default csv).
        delim: [string, optional] Delimiter (mandatory ONLY for format='delim').
        col_types: [string, optional] Compact column-spec string; empty = auto-guess.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - path: a non-empty string, NOT a directory, existing, size>0 bytes
        - POST-gate ncol>0 (a whitespace-only file yields a silent 0x0 frame)
        - col_types unset, a compact string, or a full column spec; the missing-value markers a
          non-empty list of strings with no blank entry; and read_delimited takes a delimiter of
          EXACTLY one character

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "read_parse_problems: not implemented."
    )
