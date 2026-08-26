# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``global_tree_forecasting`` -- method card #411.

#411 Global pooled tree forecasting with lag features

Category 02-univariate-forecasting; module ``global_tree_forecasting``.

Reference implementation: mlforecast.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_global_forecast",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_global_forecast(
    *,
    data: pd.DataFrame,
    id: str,
    time: str,
    value: str,
    h: int,
    lags: Sequence[int] | None = None,
    model: Literal["lightgbm", "random_forest", "gradient_boosting", "linear"] | None = None,
    difference: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``uf_global_forecast`` -- method card #411.

    Global pooled tree forecasting with lag features.

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Long-format panel: series id, time and value.
        id: [string, required] Column identifying the series.
        time: [string, required] Column holding the time index.
        value: [string, required] Column holding the value.
        h: [integer, required] Forecast horizon.
        lags: [int_array, optional] Lag features to construct. Default ``[1, 2, 3, 12]``.
        model: [enum, optional] Learner. Default ``'lightgbm'``.
        difference: [integer, optional] Differencing applied before fitting. Default ``0``.
        seed: [integer, optional] Seed for the random number generator.

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
        "uf_global_forecast: not implemented."
    )
