# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``conformal_intervals`` -- method card #414.

#414 Conformal prediction intervals for forecasts

Category 02-univariate-forecasting; module ``conformal_intervals``.

Reference implementation: mapie.

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
    "uf_conformal_intervals",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uf_conformal_intervals(
    *,
    fit: Any,
    y_calibration: pd.Series,
    h: int,
    method: Literal["split", "cv_plus", "jackknife_plus", "enbpi", "adaptive"] | None = None,
    levels: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``uf_conformal_intervals`` -- method card #414.

    Conformal prediction intervals for forecasts.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted forecasting model.
        y_calibration: [series_handle, required] Held-out calibration series.
        h: [integer, required] Forecast horizon.
        method: [enum, optional] Conformal variant. Default ``'enbpi'``.
        levels: [num_array, optional] Coverage levels. Default ``[0.8, 0.95]``.

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
        "uf_conformal_intervals: not implemented."
    )
