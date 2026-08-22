# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sieve_bootstrap`` -- method card #303.

#303 Sieve and autoregressive bootstrap

Category 35-resampling-inference; module ``sieve_bootstrap``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c35_resampling_inference import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rs_sieve_bootstrap",
    "NODE_META",
    "wire_model",
]


def rs_sieve_bootstrap(
    *,
    x: pd.Series,
    statistic: str,
    ar_order: int | None = None,
    criterion: Literal["aic", "bic", "hqic"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``rs_sieve_bootstrap`` -- method card #303.

    Sieve and autoregressive bootstrap.

    Category 35-resampling-inference; memory class ``heavy``.

    Args:
        x: [series_handle, required] Serially dependent series.
        statistic: [formula, required] Statistic to bootstrap.
        ar_order: [integer, optional] Autoregressive order; omitted = selected.
        criterion: [enum, optional] Order-selection criterion. Default ``'aic'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rs_sieve_bootstrap: not implemented."
    )
