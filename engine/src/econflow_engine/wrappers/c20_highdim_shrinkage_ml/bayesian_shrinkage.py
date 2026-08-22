# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_shrinkage`` -- method card #551.

#551 Bayesian shrinkage regression: horseshoe and spike-and-slab

Category 20-highdim-shrinkage-ml; module ``bayesian_shrinkage``.

Reference implementation: bambi.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hd_bayesian_shrinkage",
    "NODE_META",
    "wire_model",
]


def hd_bayesian_shrinkage(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    prior: (
        Literal[
            "horseshoe",
            "regularised_horseshoe",
            "spike_slab",
            "laplace",
            "ridge",
        ]
        | None
    ) = None,
    expected_nonzero: float | None = None,
    draws: int | None = None,
    warmup: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``hd_bayesian_shrinkage`` -- method card #551.

    Bayesian shrinkage regression: horseshoe and spike-and-slab.

    Category 20-highdim-shrinkage-ml; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [df_handle, required] Covariate table.
        prior: [enum, optional] Shrinkage prior. Default ``'horseshoe'``.
        expected_nonzero: [number, optional] Prior guess at the number of non-zero coefficients.
        draws: [integer, optional] Posterior draws. Default ``2000``.
        warmup: [integer, optional] Warm-up draws. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "hd_bayesian_shrinkage: not implemented."
    )
