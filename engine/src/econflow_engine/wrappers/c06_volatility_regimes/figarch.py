# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``figarch`` -- method card #437.

#437 FIGARCH and HYGARCH long-memory volatility

Category 06-volatility-regimes; module ``figarch``.

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
    "vr_figarch",
    "NODE_META",
    "wire_model",
]


def vr_figarch(
    *,
    y: pd.Series,
    model: Literal["figarch", "hygarch", "fiegarch"] | None = None,
    p: int | None = None,
    q: int | None = None,
    truncation: int | None = None,
    distribution: Literal["normal", "t", "skewt", "ged"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_figarch`` -- method card #437.

    FIGARCH and HYGARCH long-memory volatility.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Return series.
        model: [enum, optional] Model family. Default ``'figarch'``.
        p: [integer, optional] Autoregressive order. Default ``1``.
        q: [integer, optional] Moving-average order. Default ``1``.
        truncation: [integer, optional] Lag truncation of the fractional polynomial. Default
            ``1000``.
        distribution: [enum, optional] Innovation distribution. Default ``'t'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_figarch: not implemented."
    )
