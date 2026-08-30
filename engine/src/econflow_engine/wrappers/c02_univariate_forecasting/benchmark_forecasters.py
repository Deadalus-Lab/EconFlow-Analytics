# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``benchmark_forecasters`` -- method card #407.

#407 Benchmark forecasters: naive, seasonal naive, drift, mean and window average

Category 02-univariate-forecasting; module ``benchmark_forecasters``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_benchmark_forecast",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_benchmark_forecast(
    *,
    y: pd.Series,
    h: int,
    method: (
        Literal[
            "naive",
            "seasonal_naive",
            "drift",
            "mean",
            "window_average",
            "random_walk_drift",
        ]
        | None
    ) = None,
    season_length: int | None = None,
    window: int | None = None,
    levels: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``uf_benchmark_forecast`` -- method card #407.

    Benchmark forecasters: naive, seasonal naive, drift, mean and window average.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Series to forecast.
        h: [integer, required] Forecast horizon.
        method: [enum, optional] Benchmark method. Default ``'seasonal_naive'``.
        season_length: [integer, optional] Seasonal period. Default ``1``.
        window: [integer, optional] Window for the window average. Default ``12``.
        levels: [num_array, optional] Prediction interval levels. Default ``[0.8, 0.95]``.

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
        "uf_benchmark_forecast: not implemented."
    )
