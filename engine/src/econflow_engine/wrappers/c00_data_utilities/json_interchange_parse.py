# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``json_interchange_parse`` -- method card #99.

#99 JSON interchange: parse / serialise / validate / NDJSON stream in-out

Category 00-data-utilities; module ``json_interchange_parse``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "json_parse",
    "json_stream_parse",
    "json_stream_write",
    "json_validate",
    "json_write",
    "NODE_META",
    "wire_model",
]


def json_parse(
    *,
    txt: str,
    flatten: bool | None = None,
    simplify_vector: bool | None = None,
    simplify_dataframe: bool | None = None,
    simplify_matrix: bool | None = None,
) -> dict[str, Any]:
    """Node ``json_parse`` -- method card #99.

    JSON interchange: parse / serialise / validate / NDJSON stream in-out.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``parsed``, so a later node can consume it as a handle.

    Args:
        txt: [string, required] LITERAL JSON string (validate-first; a URL/path is NOT fetched — no
            SSRF).
        flatten: [boolean, optional] Flatten nested tables (default False). Default ``False``.
        simplify_vector: [boolean, optional] JSON arrays -> atomic vectors (default True). Default
            ``True``.
        simplify_dataframe: [boolean, optional] Array-of-objects -> DataFrame (default True).
            Default ``True``.
        simplify_matrix: [boolean, optional] Array-of-arrays -> matrix (default True). Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "json_parse: not implemented."
    )


def json_write(
    *,
    x: Any,
    auto_unbox: bool | None = None,
    pretty: bool | None = None,
    dataframe: Literal["rows", "columns", "values"] | None = None,
    na: Literal["null", "string"] | None = None,
    null: Literal["list", "null"] | None = None,
    digits: int | None = None,
) -> dict[str, Any]:
    """Node ``json_write`` -- method card #99.

    JSON interchange: parse / serialise / validate / NDJSON stream in-out.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a stored object to serialize to JSON text.
        auto_unbox: [boolean, optional] Length-1 vectors -> JSON scalars (default True). Default
            ``True``.
        pretty: [boolean, optional] Pretty-print with indentation (default False). Default
            ``False``.
        dataframe: [enum, optional] DataFrame orientation (default rows).
        na: [enum, optional] NA encoding (default null).
        null: [enum, optional] None encoding (default list).
        digits: [integer, optional] Decimal digits; empty = NA (full precision, NOT the toJSON
            default of 4 -> data corruption).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "json_write: not implemented."
    )


def json_validate(
    *,
    txt: str,
) -> dict[str, Any]:
    """Node ``json_validate`` -- method card #99.

    JSON interchange: parse / serialise / validate / NDJSON stream in-out.

    Category 00-data-utilities; memory class ``light``.

    Args:
        txt: [string, required] JSON string to validate; returns valid/error/offset.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "json_validate: not implemented."
    )


def json_stream_parse(
    *,
    txt: str,
    flatten: bool | None = None,
) -> dict[str, Any]:
    """Node ``json_stream_parse`` -- method card #99.

    JSON interchange: parse / serialise / validate / NDJSON stream in-out.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        txt: [string, required] NDJSON content (lines separated by \\n); every line is
            validate-first.
        flatten: [boolean, optional] Flatten nested fields (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "json_stream_parse: not implemented."
    )


def json_stream_write(
    *,
    x: pd.DataFrame,
    pagesize: int | None = None,
) -> dict[str, Any]:
    """Node ``json_stream_write`` -- method card #99.

    JSON interchange: parse / serialise / validate / NDJSON stream in-out.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a DataFrame (>=1 row) -> NDJSON lines.
        pagesize: [integer, optional] Rows per write batch (default 500). Default ``500``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "json_stream_write: not implemented."
    )
