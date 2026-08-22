# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``max_share_identification`` -- method card #429.

#429 Maximum-share and spectral identification

Category 04-structural-shocks; module ``max_share_identification``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_max_share",
    "NODE_META",
    "wire_model",
]


def ss_max_share(
    *,
    y: pd.DataFrame,
    target: str,
    lags: int | None = None,
    horizon_range: Sequence[int] | None = None,
    frequency_band: Sequence[float] | None = None,
    horizons: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_max_share`` -- method card #429.

    Maximum-share and spectral identification.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        target: [string, required] Variable whose variance is maximised.
        lags: [integer, optional] VAR lag order. Default ``4``.
        horizon_range: [int_array, optional] Horizons the share is maximised over. Default ``[0,
            40]``.
        frequency_band: [num_array, optional] Frequency band for spectral identification.
        horizons: [integer, optional] Impulse-response horizon. Default ``40``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ss_max_share: not implemented."
    )
