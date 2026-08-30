# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``time_series_decomposition`` -- method card #126.

#126 Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy)

Category 01-preparation-prechecks; module ``time_series_decomposition``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tsf_classical_decomposition",
    "tsf_features",
    "tsf_stl",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tsf_stl(
    *,
    series: pd.Series,
    s_window: Any | None = None,
    t_window: int | None = None,
) -> dict[str, Any]:
    """Node ``tsf_stl`` -- method card #126.

    Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy).

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``decomp``, so a later node can consume it as a handle.

    Args:
        series: [series_handle, required] Handle to a univariate regular ts, frequency > 1, no NA.
        s_window: [raw, optional] Season loess window: 'periodic' (default, fixed pattern) or an ODD
            integer >= 7.
        t_window: [integer, optional] Trend loess window: None (package default) or an ODD integer
            >= 3.

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
        "tsf_stl: not implemented."
    )


def tsf_classical_decomposition(
    *,
    series: pd.Series,
    type: Literal["additive", "multiplicative"] | None = None,
) -> dict[str, Any]:
    """Node ``tsf_classical_decomposition`` -- method card #126.

    Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy).

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``decomp``, so a later node can consume it as a handle.

    Args:
        series: [series_handle, required] Handle to a univariate regular ts, frequency > 1, no NA.
        type: [enum, optional] Decomposition type (default additive· multiplicative => strictly
            positive values).

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
        "tsf_classical_decomposition: not implemented."
    )


def tsf_features(
    *,
    series: pd.Series,
) -> dict[str, Any]:
    """Node ``tsf_features`` -- method card #126.

    Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        series: [series_handle, required] Handle to a univariate regular ts (frequency >= 1), no NA,
            n >= max(10, 2*freq).

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
        "tsf_features: not implemented."
    )
