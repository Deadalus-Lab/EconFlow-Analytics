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
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uf_conformal_intervals",
    "NODE_META",
    "wire_model",
]


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
    """
    raise NotImplementedError(
        "uf_conformal_intervals: not implemented."
    )
