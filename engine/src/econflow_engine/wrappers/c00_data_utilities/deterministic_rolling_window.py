# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``deterministic_rolling_window`` -- method card #105.

#105 Deterministic rolling-window aggregations (positional / index / calendar-period /
    arbitrary-pair windows)

Category 00-data-utilities; module ``deterministic_rolling_window``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "win_hop_index",
    "win_slide",
    "win_slide_index",
    "win_slide_period",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def win_slide(
    *,
    x: pd.Series,
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    before: float | None = None,
    after: float | None = None,
    step: int | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``win_slide`` -- method card #105.

    Deterministic rolling-window aggregations (positional / index / calendar-period / arbitrary-pair
    windows).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        reducer: [enum, optional] Closed reducer (default mean).
        before: [number, optional] Observations before (integer or Inf; negative=look-forward;
            default 0). Default ``0``.
        after: [number, optional] Observations after (integer or Inf; default 0; before+after>=0).
            Default ``0``.
        step: [integer, optional] Slide step >=1 (default 1). Default ``1``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA in the reducer (default False). Default ``False``.

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
        "win_slide: not implemented."
    )


def win_slide_index(
    *,
    x: pd.Series,
    i: Sequence[float],
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    before: float | None = None,
    after: float | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``win_slide_index`` -- method card #105.

    Deterministic rolling-window aggregations (positional / index / calendar-period / arbitrary-pair
    windows).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, no NA, increasing); the bounds are
            i-before, i+after.
        reducer: [enum, optional] Closed reducer (default mean).
        before: [number, optional] Backward width in index units (default 0). Default ``0``.
        after: [number, optional] Forward width in index units (default 0). Default ``0``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

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
        "win_slide_index: not implemented."
    )


def win_slide_period(
    *,
    x: pd.Series,
    i: Sequence[float],
    period: (
        Literal[
            "month",
            "quarter",
            "year",
            "week",
            "day",
            "hour",
            "minute",
            "second",
        ]
        | None
    ) = None,
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    every: int | None = None,
    before: float | None = None,
    after: float | None = None,
    complete: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``win_slide_period`` -- method card #105.

    Deterministic rolling-window aggregations (positional / index / calendar-period / arbitrary-pair
    windows).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, increasing); split into period blocks.
        period: [enum, optional] Calendar block period (default month).
        reducer: [enum, optional] Closed reducer (default mean).
        every: [integer, optional] Number of periods per block >=1 (default 1). Default ``1``.
        before: [number, optional] BLOCKS backward (default 0). Default ``0``.
        after: [number, optional] BLOCKS forward (default 0). Default ``0``.
        complete: [boolean, optional] Complete windows only (default False). Default ``False``.
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

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
        "win_slide_period: not implemented."
    )


def win_hop_index(
    *,
    x: pd.Series,
    i: Sequence[float],
    starts: Sequence[float],
    stops: Sequence[float],
    reducer: Literal["mean", "sum", "sd", "min", "max", "median"] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``win_hop_index`` -- method card #105.

    Deterministic rolling-window aggregations (positional / index / calendar-period / arbitrary-pair
    windows).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a numeric series.
        i: [num_array, required] Index (same length as x, increasing, no NA).
        starts: [num_array, required] Window starts (same length as stops; start<=stop).
        stops: [num_array, required] Window ends; output length = length(starts).
        reducer: [enum, optional] Closed reducer (default mean).
        na_rm: [boolean, optional] Ignore NA (default False). Default ``False``.

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
        "win_hop_index: not implemented."
    )
