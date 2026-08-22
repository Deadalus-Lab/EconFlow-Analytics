# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``tvtp_markov`` -- method card #442.

#442 Time-varying transition-probability Markov switching

Category 06-volatility-regimes; module ``tvtp_markov``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_tvtp_switching",
    "NODE_META",
    "wire_model",
]


def vr_tvtp_switching(
    *,
    y: pd.Series,
    drivers: np.ndarray,
    k_regimes: int | None = None,
    switching_variance: bool | None = None,
    n_starts: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``vr_tvtp_switching`` -- method card #442.

    Time-varying transition-probability Markov switching.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Series.
        drivers: [exog_handle, required] Variables driving the transition probabilities.
        k_regimes: [integer, optional] Number of regimes. Default ``2``.
        switching_variance: [boolean, optional] Allow the variance to switch. Default ``True``.
        n_starts: [integer, optional] Random restarts. Default ``10``.
        seed: [integer, optional] Seed for the random number generator.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vr_tvtp_switching: not implemented."
    )
