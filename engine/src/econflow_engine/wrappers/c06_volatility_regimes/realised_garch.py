# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``realised_garch`` -- method card #439.

#439 Realised GARCH and HEAVY models

Category 06-volatility-regimes; module ``realised_garch``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_realised_garch",
    "NODE_META",
    "wire_model",
]


def vr_realised_garch(
    *,
    y: pd.Series,
    realised: pd.Series,
    model: Literal["realised_garch", "heavy"] | None = None,
    leverage: bool | None = None,
    distribution: Literal["normal", "t", "skewt"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_realised_garch`` -- method card #439.

    Realised GARCH and HEAVY models.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Daily return series.
        realised: [series_handle, required] Daily realised variance measure.
        model: [enum, optional] Model family. Default ``'realised_garch'``.
        leverage: [boolean, optional] Include a leverage function. Default ``True``.
        distribution: [enum, optional] Innovation distribution. Default ``'t'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_realised_garch: not implemented."
    )
