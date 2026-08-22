# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``business_day_calendar`` -- method card #112.

#112 Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays)

Category 00-data-utilities; module ``business_day_calendar``.

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
    "bday_adjust",
    "bday_count",
    "bday_create_calendar",
    "bday_offset",
    "bday_sequence",
    "NODE_META",
    "wire_model",
]


def bday_create_calendar(
    *,
    holidays: Sequence[str] | None = None,
    weekdays: Sequence[str] | None = None,
    financial: bool | None = None,
    adjust_from: Literal["none", "previous", "next"] | None = None,
    adjust_to: Literal["none", "previous", "next"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``bday_create_calendar`` -- method card #112.

    Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays).

    Category 00-data-utilities; memory class ``light``.

    Args:
        holidays: [series_codes, optional] Vector of ISO dates (YYYY-MM-DD) of holidays; empty =
            actual calendar.
        weekdays: [series_codes, optional] Non-business days (LOWERCASE): e.g.
            ['saturday','sunday']; None=actual.
        financial: [boolean, optional] Financial calendar (default True): the final business day is
            not counted in bizdays. Default ``True``.
        adjust_from: [enum, optional] Adjustment of from (NETWORKDAYS-style: previous). Default
            ``'none'``.
        adjust_to: [enum, optional] Adjustment of to (NETWORKDAYS-style: next). Default ``'none'``.
        start_date: [string, optional] Optional ISO range start; empty = min(holidays) or
            1970-01-01.
        end_date: [string, optional] Optional ISO range end; empty = max(holidays) or 2071-01-01.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bday_create_calendar: not implemented."
    )


def bday_count(
    *,
    from_: Sequence[str],
    to: Sequence[str],
    holidays: Sequence[str] | None = None,
    weekdays: Sequence[str] | None = None,
    financial: bool | None = None,
    adjust_from: Literal["none", "previous", "next"] | None = None,
    adjust_to: Literal["none", "previous", "next"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``bday_count`` -- method card #112.

    Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays).

    Category 00-data-utilities; memory class ``light``.

    Args:
        from_ (wire name ``from``): [series_codes, required] Start ISO dates (recycle rule with to).
        to: [series_codes, required] End ISO dates (from <= to is required).
        holidays: [series_codes, optional] Vector of ISO holidays (closed calendar specification).
        weekdays: [series_codes, optional] Non-business days (LOWERCASE), e.g.
            ['saturday','sunday'].
        financial: [boolean, optional] Financial calendar (default True). Default ``True``.
        adjust_from: [enum, optional] Adjustment of from. Default ``'none'``.
        adjust_to: [enum, optional] Adjustment of to. Default ``'none'``.
        start_date: [string, optional] Optional ISO range start.
        end_date: [string, optional] Optional ISO range end.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bday_count: not implemented."
    )


def bday_offset(
    *,
    dates: Sequence[str],
    n: Sequence[int],
    holidays: Sequence[str] | None = None,
    weekdays: Sequence[str] | None = None,
    financial: bool | None = None,
    adjust_from: Literal["none", "previous", "next"] | None = None,
    adjust_to: Literal["none", "previous", "next"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``bday_offset`` -- method card #112.

    Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays).

    Category 00-data-utilities; memory class ``light``.

    Args:
        dates: [series_codes, required] ISO dates to shift (recycle rule with n).
        n: [int_array, required] Number of business days to shift (integers; ± = forward/backward).
        holidays: [series_codes, optional] Vector of ISO holidays.
        weekdays: [series_codes, optional] Non-business days (LOWERCASE).
        financial: [boolean, optional] Financial calendar. Default ``True``.
        adjust_from: [enum, optional] Adjustment of from. Default ``'none'``.
        adjust_to: [enum, optional] Adjustment of to. Default ``'none'``.
        start_date: [string, optional] Optional ISO range start.
        end_date: [string, optional] Optional ISO range end.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bday_offset: not implemented."
    )


def bday_adjust(
    *,
    dates: Sequence[str],
    direction: Literal["next", "previous"] | None = None,
    holidays: Sequence[str] | None = None,
    weekdays: Sequence[str] | None = None,
    financial: bool | None = None,
    adjust_from: Literal["none", "previous", "next"] | None = None,
    adjust_to: Literal["none", "previous", "next"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``bday_adjust`` -- method card #112.

    Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays).

    Category 00-data-utilities; memory class ``light``.

    Args:
        dates: [series_codes, required] ISO dates to roll onto a business day.
        direction: [enum, optional] Roll direction: next (adjust.next) or previous
            (adjust.previous). Default ``'next'``.
        holidays: [series_codes, optional] Vector of ISO holidays.
        weekdays: [series_codes, optional] Non-business days (LOWERCASE).
        financial: [boolean, optional] Financial calendar. Default ``True``.
        adjust_from: [enum, optional] Adjustment of from (calendar). Default ``'none'``.
        adjust_to: [enum, optional] Adjustment of to (calendar). Default ``'none'``.
        start_date: [string, optional] Optional ISO range start.
        end_date: [string, optional] Optional ISO range end.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bday_adjust: not implemented."
    )


def bday_sequence(
    *,
    from_: str,
    to: str,
    holidays: Sequence[str] | None = None,
    weekdays: Sequence[str] | None = None,
    financial: bool | None = None,
    adjust_from: Literal["none", "previous", "next"] | None = None,
    adjust_to: Literal["none", "previous", "next"] | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
) -> dict[str, Any]:
    """Node ``bday_sequence`` -- method card #112.

    Business-day calendar + working-day arithmetic (calendar creation / business-day count / offset
    / adjust / sequence) from a closed specification (holidays + weekdays).

    Category 00-data-utilities; memory class ``light``.

    Args:
        from_ (wire name ``from``): [string, required] Start ISO date (single; from <= to is
            required).
        to: [string, required] End ISO date (single).
        holidays: [series_codes, optional] Vector of ISO holidays.
        weekdays: [series_codes, optional] Non-business days (LOWERCASE).
        financial: [boolean, optional] Financial calendar. Default ``True``.
        adjust_from: [enum, optional] Adjustment of from. Default ``'none'``.
        adjust_to: [enum, optional] Adjustment of to. Default ``'none'``.
        start_date: [string, optional] Optional ISO range start.
        end_date: [string, optional] Optional ISO range end.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bday_sequence: not implemented."
    )
