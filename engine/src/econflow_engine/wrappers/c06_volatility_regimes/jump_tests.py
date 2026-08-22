# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``jump_tests`` -- method card #440.

#440 High-frequency jump tests: bipower variation and Lee-Mykland

Category 06-volatility-regimes; module ``jump_tests``.

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
    "vr_jump_test",
    "NODE_META",
    "wire_model",
]


def vr_jump_test(
    *,
    prices: pd.Series,
    test: Literal["bns", "lee_mykland", "threshold"] | None = None,
    interval: int | None = None,
    deseasonalise: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``vr_jump_test`` -- method card #440.

    High-frequency jump tests: bipower variation and Lee-Mykland.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        prices: [irregular_series_handle, required] Intraday price series.
        test: [enum, optional] Test family. Default ``'bns'``.
        interval: [integer, optional] Sampling interval in seconds. Default ``300``.
        deseasonalise: [boolean, optional] Remove intraday periodicity first. Default ``True``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_jump_test: not implemented."
    )
