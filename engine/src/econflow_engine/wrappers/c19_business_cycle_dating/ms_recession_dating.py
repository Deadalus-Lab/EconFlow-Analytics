# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ms_recession_dating`` -- method card #540.

#540 Markov-switching recession dating

Category 19-business-cycle-dating; module ``ms_recession_dating``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bc_ms_factor",
    "bc_ms_recession",
    "NODE_META",
    "wire_model",
]


def bc_ms_recession(
    *,
    y: pd.Series,
    k_regimes: int | None = None,
    order: int | None = None,
    switching_variance: bool | None = None,
    threshold: float | None = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bc_ms_recession`` -- method card #540.

    Markov-switching recession dating.

    Category 19-business-cycle-dating; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Growth series.
        k_regimes: [integer, optional] Number of regimes. Default ``2``.
        order: [integer, optional] Autoregressive order. Default ``4``.
        switching_variance: [boolean, optional] Allow the variance to switch. Default ``True``.
        threshold: [number, optional] Probability threshold for dating. Default ``0.5``.
        n_starts: [integer, optional] Optimiser restarts. Default ``10``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bc_ms_recession: not implemented."
    )


def bc_ms_factor(
    *,
    y: pd.DataFrame,
    k_regimes: int | None = None,
    factor_order: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``bc_ms_factor`` -- method card #540.

    Markov-switching recession dating.

    Category 19-business-cycle-dating; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Coincident indicators.
        k_regimes: [integer, optional] Number of regimes. Default ``2``.
        factor_order: [integer, optional] Factor autoregressive order. Default ``2``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bc_ms_factor: not implemented."
    )
