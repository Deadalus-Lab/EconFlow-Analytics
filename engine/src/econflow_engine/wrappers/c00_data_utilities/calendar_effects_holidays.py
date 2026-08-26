# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``calendar_effects_holidays`` -- method card #254.

#254 CALENDAR EFFECTS: holidays for G7+CH & financial centres (NYSE/LONDON/ZURICH/TSX) -> NAMED 0/1
    columns aligned to a given vector of dates + weekday/business-day flags

Category 00-data-utilities; module ``calendar_effects_holidays``.

Reference implementation: holidays.

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
    "hd_dummies",
    "hd_holidays",
    "hd_list",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hd_list(
    *,
    pattern: str | None = None,
) -> dict[str, Any]:
    """Node ``hd_list`` -- method card #254.

    CALENDAR EFFECTS: holidays for G7+CH & financial centres (NYSE/LONDON/ZURICH/TSX) -> NAMED 0/1
    columns aligned to a given vector of dates + weekday/business-day flags.

    Category 00-data-utilities; memory class ``light``.

    Args:
        pattern: [string, optional] Regular expression on the NAMES of the holidays ('.*' = all,
            default). listHolidays matches ANYWHERE inside the name, not only as a prefix — that is
            why 'GB' gives 4 (3 with the GB prefix + specialHolidayGB). Country codes: US, CA, GB,
            DE, FR, IT, JP, CH. An invalid regex -> a clean error. Default ``'.*'``.

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
        "hd_list: not implemented."
    )


def hd_holidays(
    *,
    year: Sequence[int],
    holidays: Sequence[str] | None = None,
    calendar: Literal["none", "NYSE", "LONDON", "ZURICH", "TSX"] | None = None,
    nyse_type: Literal["all", "standard", "special"] | None = None,
) -> dict[str, Any]:
    """Node ``hd_holidays`` -- method card #254.

    CALENDAR EFFECTS: holidays for G7+CH & financial centres (NYSE/LONDON/ZURICH/TSX) -> NAMED 0/1
    columns aligned to a given vector of dates + weekday/business-day flags.

    Category 00-data-utilities; memory class ``light``.

    Args:
        year: [int_array, required] YEARS (YYYY) — MANDATORY and INTEGER, within [1583, 2200].
            timeDate's default is the CURRENT year FROM THE CLOCK => NOT reproducible, which is why
            it is required explicitly. Lower bound 1583 = the 1st full year of the Gregorian
            calendar (the Easter algorithm is Gregorian). Outside [1000, 9999] timeDate returns NA
            SILENTLY.
        holidays: [series_codes, optional] NAMES of holidays from timeDate's catalogue (120 in
            total; run hd_list FIRST to find them: US 18 · CA 6 · GB 4 · DE 5 · FR 6 · IT 6 · JP 33
            · CH 5). EVERY name is validated BEFORE the call — an unknown name is blocked with an
            explicit message instead of the cryptic "object 'X' of mode 'function' was not found" of
            timeDate. NO duplicates (they would give identical, perfectly collinear columns).
            Examples: USNewYearsDay, USThanksgivingDay, GoodFriday, ChristmasDay, DEGermanUnity,
            JPMountainDay.
        calendar: [enum, optional] Calendar of a FINANCIAL CENTRE (closing days) as an ADDITIONAL
            source, beyond the named 'holidays': NYSE / LONDON / ZURICH / TSX (default 'none'). It
            gives ONE dummy column named after the centre. Useful for daily financial data (a closed
            market = a structural gap, not a missing value). Default ``'none'``.
        nyse_type: [enum, optional] ONLY for calendar = 'NYSE': 'all' = ALL the closures (default);
            'standard' = only the institutional holidays; 'special' = only the EXTRAORDINARY
            closures (e.g. 2001-09-11 to 09-14). With another calendar it is blocked instead of
            being ignored silently. Default ``'all'``.

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
        "hd_holidays: not implemented."
    )


def hd_dummies(
    *,
    dates: Sequence[str],
    holidays: Sequence[str] | None = None,
    calendar: Literal["none", "NYSE", "LONDON", "ZURICH", "TSX"] | None = None,
    nyse_type: Literal["all", "standard", "special"] | None = None,
    holiday_dates: Any | None = None,
    dummy_type: Literal["per_holiday", "aggregate", "both"] | None = None,
    wday: Sequence[int] | None = None,
) -> dict[str, Any]:
    """Node ``hd_dummies`` -- method card #254.

    CALENDAR EFFECTS: holidays for G7+CH & financial centres (NYSE/LONDON/ZURICH/TSX) -> NAMED 0/1
    columns aligned to a given vector of dates + weekday/business-day flags.

    Category 00-data-utilities; memory class ``light``.

    Args:
        dates: [series_codes, required] THE ALIGNMENT INDEX: dates STRICTLY 'YYYY-MM-DD', UNIQUE,
            within [1583, 2200]. Each row of the dummies matrix corresponds to ONE of them, in the
            GIVEN order. An invalid/non-existent date (e.g. 2024-02-30) is blocked — timeDate would
            return NA SILENTLY.
        holidays: [series_codes, optional] NAMES of holidays from timeDate's catalogue (120 in
            total; run hd_list FIRST to find them: US 18 · CA 6 · GB 4 · DE 5 · FR 6 · IT 6 · JP 33
            · CH 5). EVERY name is validated BEFORE the call — an unknown name is blocked with an
            explicit message instead of the cryptic "object 'X' of mode 'function' was not found" of
            timeDate. NO duplicates (they would give identical, perfectly collinear columns).
            Examples: USNewYearsDay, USThanksgivingDay, GoodFriday, ChristmasDay, DEGermanUnity,
            JPMountainDay.
        calendar: [enum, optional] Calendar of a FINANCIAL CENTRE (closing days) as an ADDITIONAL
            source, beyond the named 'holidays': NYSE / LONDON / ZURICH / TSX (default 'none'). It
            gives ONE dummy column named after the centre. Useful for daily financial data (a closed
            market = a structural gap, not a missing value). Default ``'none'``.
        nyse_type: [enum, optional] ONLY for calendar = 'NYSE': 'all' = ALL the closures (default);
            'standard' = only the institutional holidays; 'special' = only the EXTRAORDINARY
            closures (e.g. 2001-09-11 to 09-14). With another calendar it is blocked instead of
            being ignored silently. Default ``'all'``.
        holiday_dates: [raw, optional] APPLY MODE (fit/apply externalization): the READY calendar of
            a previous node — a NAMED object {column_name: ['YYYY-MM-DD',...]}, exactly as the
            'holiday_dates' of hd_holidays/hd_dummies returns it. It gives IDENTICAL columns on a
            NEW sample (even if some holiday does not fall inside it), independently of the timeDate
            version. MUTUALLY EXCLUSIVE with holidays/calendar/nyse_type (FIT).
        dummy_type: [enum, optional] Shape of the matrix: 'per_holiday' = ONE 0/1 column PER holiday
            (default; it allows a different coefficient per holiday); 'aggregate' = ONE
            'holiday_any' column (1 if the day is any holiday — fewer degrees of freedom); 'both' =
            both. The aggregate vector 'is_holiday' is ALWAYS returned, regardless of the choice.
            Default ``'per_holiday'``.
        wday: [int_array, optional] Which days count as WORKING DAYS, for the isWeekday/isBizday
            flags: 0 = Sunday... 6 = Saturday (default 1:5 = Mon-Fri). Outside [0, 6] it is blocked
            — timeDate does NOT error, it returns ALL False (silent-wrong). Default ``[1, 2, 3, 4,
            5]``.

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
        "hd_dummies: not implemented."
    )
