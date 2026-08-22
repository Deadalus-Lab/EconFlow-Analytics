# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``coverage_calibration`` -- method card #311.

#311 Coverage and calibration checks

Category 36-monte-carlo-design; module ``coverage_calibration``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_coverage_study",
    "mc_pit",
    "NODE_META",
    "wire_model",
]


def mc_coverage_study(
    *,
    dgp: str,
    procedure: str,
    levels: Sequence[float] | None = None,
    n_replications: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_coverage_study`` -- method card #311.

    Coverage and calibration checks.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        dgp: [formula, required] Data-generating process with a known truth.
        procedure: [formula, required] Interval procedure to assess.
        levels: [num_array, optional] Nominal levels to check. Default ``[0.8, 0.9, 0.95]``.
        n_replications: [integer, optional] Monte Carlo replications. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_coverage_study: not implemented."
    )


def mc_pit(
    *,
    observed: pd.Series,
    predictive_cdf: np.ndarray,
    test: Literal["ks", "ad", "cvm", "berkowitz"] | None = None,
) -> dict[str, Any]:
    """Node ``mc_pit`` -- method card #311.

    Coverage and calibration checks.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        observed: [series_handle, required] Realised outcomes.
        predictive_cdf: [matrix_handle, required] Predictive CDF evaluated at the outcomes.
        test: [enum, optional] Uniformity test. Default ``'ks'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_pit: not implemented."
    )
