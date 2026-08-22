# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``direct_multistep`` -- method card #413.

#413 Direct multi-step reduction forecasting

Category 02-univariate-forecasting; module ``direct_multistep``.

Reference implementation: sktime.

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
    "uf_direct_multistep",
    "NODE_META",
    "wire_model",
]


def uf_direct_multistep(
    *,
    y: pd.Series,
    h: int,
    strategy: Literal["direct", "recursive", "dirrec", "multioutput"] | None = None,
    window_length: int | None = None,
    model: Literal["linear", "ridge", "random_forest", "gradient_boosting"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``uf_direct_multistep`` -- method card #413.

    Direct multi-step reduction forecasting.

    Category 02-univariate-forecasting; memory class ``light``.

    Args:
        y: [series_handle, required] Series to forecast.
        h: [integer, required] Forecast horizon.
        strategy: [enum, optional] Reduction strategy. Default ``'direct'``.
        window_length: [integer, optional] Lag window used as features. Default ``12``.
        model: [enum, optional] Base regressor. Default ``'gradient_boosting'``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "uf_direct_multistep: not implemented."
    )
