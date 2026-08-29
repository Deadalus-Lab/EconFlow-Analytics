# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``analytic_ols_closed`` -- method card #121.

#121 Analytic OLS on a CLOSED formula: a deterministic time trend (linear/quadratic) + the detrended
    series, or response ~ named numeric predictor columns

Category 00-data-utilities; module ``analytic_ols_closed``.

Reference implementation: statsmodels.

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
    "ols_regress",
    "ols_trend",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ols_trend(
    *,
    y: pd.Series,
    trend: Literal["linear", "quadratic"] | None = None,
) -> dict[str, Any]:
    """Node ``ols_trend`` -- method card #121.

    Analytic OLS on a CLOSED formula: a deterministic time trend (linear/quadratic) + the detrended
    series, or response ~ named numeric predictor columns.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a numeric series (ts/series/vector; stripped to plain
            numeric). Must be finite, no NA/NaN/Inf — otherwise OLS would SILENTLY drop observations
            (hard gate).
        trend: [enum, optional] Closed deterministic trend: linear=1+t, quadratic=1+t+t^2 (default
            linear). The formula is built internally with reformulate — NEVER a free string.

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
        "ols_trend: not implemented."
    )


def ols_regress(
    *,
    data: pd.DataFrame,
    response: str,
    predictors: Sequence[str],
) -> dict[str, Any]:
    """Node ``ols_regress`` -- method card #121.

    Analytic OLS on a CLOSED formula: a deterministic time trend (linear/quadratic) + the detrended
    series, or response ~ named numeric predictor columns.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a DataFrame holding the response + the predictor
            columns.
        response: [string, required] ONE column name — the numeric dependent variable (finite, no
            NA).
        predictors: [series_codes, required] Vector of numeric predictor column names (no
            duplicates, ∉ response). The formula reformulate(`preds`, response=`resp`) is built
            internally — NEVER a free string.

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
        "ols_regress: not implemented."
    )
