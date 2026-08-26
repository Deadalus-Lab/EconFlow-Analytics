# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``calendar_regressors`` -- method card #383.

#383 Trading-day, leap-year and Easter regressors

Category 00-data-utilities; module ``calendar_regressors``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_calendar_regressors",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_calendar_regressors(
    *,
    index: pd.Series,
    trading_day: bool | None = None,
    leap_year: bool | None = None,
    easter: bool | None = None,
    easter_window: int | None = None,
    country: str | None = None,
) -> dict[str, Any]:
    """Node ``du_calendar_regressors`` -- method card #383.

    Trading-day, leap-year and Easter regressors.

    Category 00-data-utilities; memory class ``light``.

    Args:
        index: [series_handle, required] Date index the regressors are built for.
        trading_day: [boolean, optional] Include weekday-count contrasts. Default ``True``.
        leap_year: [boolean, optional] Include the leap-year correction. Default ``True``.
        easter: [boolean, optional] Include an Easter proximity regressor. Default ``False``.
        easter_window: [integer, optional] Days before Easter the effect spans. Default ``8``.
        country: [string, optional] Country code for national holidays.

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
        "du_calendar_regressors: not implemented."
    )
