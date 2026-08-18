# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``time_series_decomposition`` -- METHOD-SELECTION card #126.

#126 Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy)

Category 01-preparation-prechecks; module ``time_series_decomposition``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fst_classical",
    "fst_features",
    "fst_stl",
    "NODE_META",
    "wire_model",
]


def fst_stl(
    *,
    series: pd.Series,
    s_window: Any | None = None,
    t_window: int | None = None,
) -> dict[str, Any]:
    """Node ``fst_stl`` -- METHOD-SELECTION card #126.

    Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy).

    Category 01-preparation-prechecks; memory class ``light``.

    Registers its result under ``decomp``, so a later node can consume it as a handle.

    Args:
        series: [series_handle, required] Handle to a univariate regular ts, frequency > 1, no NA.
        s_window: [raw, optional] Season loess window: 'periodic' (default, fixed pattern) or an ODD
            integer >= 7.
        t_window: [integer, optional] Trend loess window: None (default feasts) or an ODD integer >=
            3.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fst_stl: not implemented. The method card is in ./README.md."
    )


def fst_classical(
    *,
    series: pd.Series,
    type: Literal["additive", "multiplicative"] | None = None,
) -> dict[str, Any]:
    """Node ``fst_classical`` -- METHOD-SELECTION card #126.

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
    """
    raise NotImplementedError(
        "fst_classical: not implemented. The method card is in ./README.md."
    )


def fst_features(
    *,
    series: pd.Series,
) -> dict[str, Any]:
    """Node ``fst_features`` -- METHOD-SELECTION card #126.

    Time-series decomposition (STL / classical) + feature extraction (STL strength / ACF / spectral
    entropy).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        series: [series_handle, required] Handle to a univariate regular ts (frequency >= 1), no NA,
            n >= max(10, 2*freq).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fst_features: not implemented. The method card is in ./README.md."
    )
