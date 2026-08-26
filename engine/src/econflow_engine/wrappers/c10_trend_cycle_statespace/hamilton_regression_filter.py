# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hamilton_regression_filter`` -- method card #57.

#57 Hamilton regression filter

Category 10-trend-cycle-statespace; module ``hamilton_regression_filter``.

Reference implementation: quantecon.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ham_filter",
    "ham_frame_from_long",
    "ham_regression",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ham_frame_from_long(
    *,
    df: pd.DataFrame,
    series_name: str,
    transform: Literal["none", "log100"] | None = None,
    frequency: int | None = None,
) -> dict[str, Any]:
    """Node ``ham_frame_from_long`` -- method card #57.

    Hamilton regression filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Registers its result under ``x``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a long DataFrame (one series, period/value).
        series_name: [string, required] Series name -> colname of the series (determines the output
            names).
        transform: [enum, optional] log100 = 100*log (Hamilton canonical for levels).
        frequency: [integer, optional] Frequency assertion (1/4/12)· None -> inferred.

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
        "ham_frame_from_long: not implemented."
    )


def ham_filter(
    *,
    x: Any,
    h: int | None = None,
    p: int | None = None,
) -> dict[str, Any]:
    """Node ``ham_filter`` -- method card #57.

    Hamilton regression filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an series from ham_frame_from_long (kept as series).
        h: [integer, optional] Regression horizon (default 2*periods_per_year).
        p: [integer, optional] Number of lags (>=2· default periods_per_year).

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
        "ham_filter: not implemented."
    )


def ham_regression(
    *,
    x: Any,
    h: int | None = None,
    p: int | None = None,
) -> dict[str, Any]:
    """Node ``ham_regression`` -- method card #57.

    Hamilton regression filter.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an series from ham_frame_from_long (underlying Hamilton
            regression).
        h: [integer, optional] Regression horizon (default 2*periods_per_year).
        p: [integer, optional] Number of lags (>=2· default periods_per_year).

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
        "ham_regression: not implemented."
    )
