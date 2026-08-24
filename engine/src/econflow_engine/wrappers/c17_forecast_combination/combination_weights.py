# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``combination_weights`` -- method card #530.

#530 Bates-Granger inverse-MSE and Granger-Ramanathan weights

Category 17-forecast-combination; module ``combination_weights``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c17_forecast_combination import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fc_combination_weights",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fc_combination_weights(
    *,
    actual: pd.Series,
    forecasts: pd.DataFrame,
    method: (
        Literal[
            "equal",
            "inverse_mse",
            "granger_ramanathan",
            "constrained_ls",
            "trimmed_mean",
        ]
        | None
    ) = None,
    window: int | None = None,
    constrain: bool | None = None,
) -> dict[str, Any]:
    """Node ``fc_combination_weights`` -- method card #530.

    Bates-Granger inverse-MSE and Granger-Ramanathan weights.

    Category 17-forecast-combination; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecasts: [df_handle, required] Forecasts, one column per method.
        method: [enum, optional] Weighting method. Default ``'inverse_mse'``.
        window: [integer, optional] Rolling window for the weights; omitted = expanding.
        constrain: [boolean, optional] Constrain weights to be non-negative and sum to one. Default
            ``True``.

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
        "fc_combination_weights: not implemented."
    )
