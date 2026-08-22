# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``date_parsing_rounding`` -- method card #111.

#111 Date parsing/rounding/components + safe month arithmetic (flexible parsing,
    floor/ceiling/round, calendar components, month rollback)

Category 00-data-utilities; module ``date_parsing_rounding``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

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
    "date_component",
    "date_month_arith",
    "date_parse",
    "date_parse_datetime",
    "date_round",
    "NODE_META",
    "wire_model",
]


def date_parse(
    *,
    x: Sequence[str],
    order: Literal["ymd", "ym"] | None = None,
) -> dict[str, Any]:
    """Node ``date_parse`` -- method card #111.

    Date parsing/rounding/components + safe month arithmetic (flexible parsing, floor/ceiling/round,
    calendar components, month rollback).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``dates``, so a later node can consume it as a handle.

    Args:
        x: [series_codes, required] Character/numeric vector of date strings to parse (e.g.
            '2015-01-31', '2015/03/04', 20150102).
        order: [enum, optional] Component order: ymd=full date, ym=year-month (day=1). Default ymd.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_parse: not implemented."
    )


def date_parse_datetime(
    *,
    x: Sequence[str],
    orders: Sequence[str],
    tz: str | None = None,
) -> dict[str, Any]:
    """Node ``date_parse_datetime`` -- method card #111.

    Date parsing/rounding/components + safe month arithmetic (flexible parsing, floor/ceiling/round,
    calendar components, month rollback).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``dates``, so a later node can consume it as a handle.

    Args:
        x: [series_codes, required] Character/numeric vector of datetime strings to parse.
        orders: [series_codes, required] Character vector of formats (e.g. ['ymd HMS','ymd']); ALL
            are tried (not a single-choice match).
        tz: [string, optional] Time zone of the timestamp output (default UTC). Default ``'UTC'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_parse_datetime: not implemented."
    )


def date_round(
    *,
    x: Any,
    unit: Literal["month", "quarter", "year", "week", "day"] | None = None,
    boundary: Literal["floor", "ceiling", "round"] | None = None,
) -> dict[str, Any]:
    """Node ``date_round`` -- method card #111.

    Date parsing/rounding/components + safe month arithmetic (flexible parsing, floor/ceiling/round,
    calendar components, month rollback).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``dates``, so a later node can consume it as a handle.

    Args:
        x: [raw_handle, required] Handle to a parsed Date/timestamp vector (from
            date_parse/date_parse_datetime).
        unit: [enum, optional] Calendar rounding boundary — closed enum (default month).
        boundary: [enum, optional] floor=downwards, ceiling=upwards, round=nearest. Default floor.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_round: not implemented."
    )


def date_component(
    *,
    x: Any,
    component: Literal["quarter", "semester", "year", "month", "wday"] | None = None,
) -> dict[str, Any]:
    """Node ``date_component`` -- method card #111.

    Date parsing/rounding/components + safe month arithmetic (flexible parsing, floor/ceiling/round,
    calendar components, month rollback).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a parsed Date/timestamp vector.
        component: [enum, optional] Calendar field to extract as numeric (default quarter; wday:
            week_start=7 -> Sunday=1).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_component: not implemented."
    )


def date_month_arith(
    *,
    x: Any,
    months: int,
    op: Literal["add", "subtract"] | None = None,
) -> dict[str, Any]:
    """Node ``date_month_arith`` -- method card #111.

    Date parsing/rounding/components + safe month arithmetic (flexible parsing, floor/ceiling/round,
    calendar components, month rollback).

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``dates``, so a later node can consume it as a handle.

    Args:
        x: [raw_handle, required] Handle to a parsed Date/timestamp vector.
        months: [integer, required] Finite integer number of months (safe %m+%/%m-% rollback at
            month end).
        op: [enum, optional] add=%m+%, subtract=%m-%. Default add.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "date_month_arith: not implemented."
    )
