# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stationary_bootstrap`` -- method card #302.

#302 Stationary bootstrap (Politis-Romano)

Category 35-resampling-inference; module ``stationary_bootstrap``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_stationary_bootstrap",
    "NODE_META",
    "wire_model",
]


def rs_stationary_bootstrap(
    *,
    data: pd.DataFrame,
    statistic: str,
    expected_block_length: float | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_stationary_bootstrap`` -- method card #302.

    Stationary bootstrap (Politis-Romano).

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        data: [multiseries_handle, required] Serially dependent data.
        statistic: [formula, required] Statistic to bootstrap.
        expected_block_length: [number, optional] Mean block length; omitted = automatic.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_stationary_bootstrap: not implemented."
    )
