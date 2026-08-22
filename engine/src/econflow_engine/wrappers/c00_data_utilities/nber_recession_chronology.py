# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nber_recession_chronology`` -- method card #119.

#119 US NBER recession chronology — recession-shading intervals + a per-date 0/1 recession dummy

Category 00-data-utilities; module ``nber_recession_chronology``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nber_recession_flag",
    "nber_recessions",
    "NODE_META",
    "wire_model",
]


def nber_recessions(
    *,
    from_: str | None = None,
    to: str | None = None,
    as_date: bool | None = None,
) -> dict[str, Any]:
    """Node ``nber_recessions`` -- method card #119.

    US NBER recession chronology — recession-shading intervals + a per-date 0/1 recession dummy.

    Category 00-data-utilities; memory class ``light``.

    Args:
        from_ (wire name ``from``): [string, optional] Lower window bound (ISO 'YYYY-MM-DD' or
            integer yyyymmdd); a recession is kept if end>=from. Empty = no lower bound.
        to: [string, optional] Upper window bound (ISO 'YYYY-MM-DD' or yyyymmdd); a recession is
            kept if start<=to. Requires from<=to.
        as_date: [boolean, optional] True => Date columns; False (default) => integer yyyymmdd.
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nber_recessions: not implemented."
    )


def nber_recession_flag(
    *,
    dates: Sequence[str],
    as_date: bool | None = None,
) -> dict[str, Any]:
    """Node ``nber_recession_flag`` -- method card #119.

    US NBER recession chronology — recession-shading intervals + a per-date 0/1 recession dummy.

    Category 00-data-utilities; memory class ``light``.

    Args:
        dates: [series_codes, required] Vector of dates (ISO 'YYYY-MM-DD' strings or yyyymmdd) —
            e.g. the time index of a series; a per-date 0/1 recession dummy is returned.
        as_date: [boolean, optional] True => Date column date; False (default) => integer yyyymmdd.
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nber_recession_flag: not implemented."
    )
