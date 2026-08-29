# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``macro_arithmetic`` -- method card #82.

#82 Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions)

Category 00-data-utilities; module ``macro_arithmetic``.

Reference implementation: pandas.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "macro_contributions",
    "macro_deflate",
    "macro_growth",
    "macro_per_capita",
    "macro_rebase",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def macro_growth(
    *,
    x: pd.Series,
    periods: int | None = None,
    annualize: bool | None = None,
    frequency: int | None = None,
    log: bool | None = None,
) -> dict[str, Any]:
    """Node ``macro_growth`` -- method card #82.

    Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a finite series (>=2 values).
        periods: [integer, optional] Lag periods for the growth rate (default 1). Default ``1``.
        annualize: [boolean, optional] Annualization (compound for simple, linear for log; default
            False). Default ``False``.
        frequency: [integer, optional] Periods per year; REQUIRED when annualize=True.
        log: [boolean, optional] log-diff instead of simple growth (requires x>0; default False).
            Default ``False``.

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
        "macro_growth: not implemented."
    )


def macro_deflate(
    *,
    nominal: pd.Series,
    deflator: pd.Series,
    base: float | None = None,
) -> dict[str, Any]:
    """Node ``macro_deflate`` -- method card #82.

    Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions).

    Category 00-data-utilities; memory class ``light``.

    Args:
        nominal: [series_handle, required] Handle to a nominal series.
        deflator: [series_handle, required] Handle to a deflator (>0, same length as nominal).
        base: [number, optional] Deflator base (default 100). Default ``100``.

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
        "macro_deflate: not implemented."
    )


def macro_rebase(
    *,
    x: pd.Series,
    base_period: int,
    base_value: float | None = None,
) -> dict[str, Any]:
    """Node ``macro_rebase`` -- method card #82.

    Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to the series to convert into an index.
        base_period: [integer, required] Position (1..n) of the base period (anchor != 0).
        base_value: [number, optional] Index value at the base (default 100). Default ``100``.

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
        "macro_rebase: not implemented."
    )


def macro_per_capita(
    *,
    x: pd.Series,
    population: pd.Series,
    scale: float | None = None,
) -> dict[str, Any]:
    """Node ``macro_per_capita`` -- method card #82.

    Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a magnitude (e.g. GDP).
        population: [series_handle, required] Handle to population (>0, same length as x).
        scale: [number, optional] Scale multiplier (default 1). Default ``1``.

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
        "macro_per_capita: not implemented."
    )


def macro_contributions(
    *,
    components: np.ndarray,
    weights: pd.Series,
    aggregate_growth: pd.Series | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``macro_contributions`` -- method card #82.

    Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions).

    Category 00-data-utilities; memory class ``light``.

    Args:
        components: [matrix_handle, required] Handle to a matrix of GROWTH RATES (rows=periods,
            columns=components).
        weights: [series_handle, required] Handle to a vector of weights (length = number of
            components).
        aggregate_growth: [series_handle, optional] Handle to the aggregate growth rate for a HARD
            additivity post-check (optional).
        tol: [number, optional] Tolerance of the additivity check (default 1e-6). Default ``1e-06``.

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
        "macro_contributions: not implemented."
    )
