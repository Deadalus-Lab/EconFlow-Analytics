# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``forecast_rationality`` -- method card #517.

#517 Forecast rationality: Mincer-Zarnowitz and encompassing

Category 15-model-evaluation; module ``forecast_rationality``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import pandas as pd

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_forecast_rationality",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_forecast_rationality(
    *,
    actual: pd.Series,
    forecast: pd.Series,
    rival: pd.Series | None = None,
    information: pd.DataFrame | None = None,
    horizon: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_forecast_rationality`` -- method card #517.

    Forecast rationality: Mincer-Zarnowitz and encompassing.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        actual: [series_handle, required] Realised values.
        forecast: [series_handle, required] Forecast to test.
        rival: [series_handle, optional] Rival forecast for the encompassing test.
        information: [multiseries_handle, optional] Information set for orthogonality tests.
        horizon: [integer, optional] Forecast horizon, for the HAC lag. Default ``1``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "me_forecast_rationality: not implemented."
    )
