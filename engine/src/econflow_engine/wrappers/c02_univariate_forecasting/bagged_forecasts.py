# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bagged_forecasts`` -- method card #412.

#412 Bagged and bootstrap-aggregated forecasts with STL and block bootstrap

Category 02-univariate-forecasting; module ``bagged_forecasts``.

Reference implementation: statsforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_bagged_forecast",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_bagged_forecast(
    *,
    y: pd.Series,
    h: int,
    n_replicates: int | None = None,
    bootstrap: Literal["stl_block", "moving_block", "stationary"] | None = None,
    base_model: Literal["auto_arima", "auto_ets", "theta", "naive"] | None = None,
    aggregate: Literal["mean", "median"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``uf_bagged_forecast`` -- method card #412.

    Bagged and bootstrap-aggregated forecasts with STL and block bootstrap.

    Category 02-univariate-forecasting; memory class ``heavy``.

    Args:
        y: [series_handle, required] Series to forecast.
        h: [integer, required] Forecast horizon.
        n_replicates: [integer, optional] Bootstrap replicates. Default ``100``.
        bootstrap: [enum, optional] Bootstrap scheme. Default ``'stl_block'``.
        base_model: [enum, optional] Model fitted to each replicate. Default ``'auto_ets'``.
        aggregate: [enum, optional] Aggregation across replicates. Default ``'mean'``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "uf_bagged_forecast: not implemented."
    )
