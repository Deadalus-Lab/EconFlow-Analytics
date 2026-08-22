# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``size_power`` -- method card #310.

#310 Size and power studies with rejection frequencies

Category 36-monte-carlo-design; module ``size_power``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_power_study",
    "mc_size_study",
    "NODE_META",
    "wire_model",
]


def mc_size_study(
    *,
    dgp: str,
    test: str,
    n_replications: int | None = None,
    sample_sizes: Sequence[int] | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``mc_size_study`` -- method card #310.

    Size and power studies with rejection frequencies.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        dgp: [formula, required] Data-generating process under the null.
        test: [formula, required] Test to apply.
        n_replications: [integer, optional] Monte Carlo replications. Default ``1000``.
        sample_sizes: [int_array, optional] Sample sizes to scan. Default ``[50, 100, 250, 500]``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_size_study: not implemented."
    )


def mc_power_study(
    *,
    dgp: str,
    test: str,
    effect_grid: Sequence[float],
    n_replications: int | None = None,
    size_correct: bool | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``mc_power_study`` -- method card #310.

    Size and power studies with rejection frequencies.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        dgp: [formula, required] Data-generating process under the alternative.
        test: [formula, required] Test to apply.
        effect_grid: [num_array, required] Alternative values to scan.
        n_replications: [integer, optional] Monte Carlo replications. Default ``1000``.
        size_correct: [boolean, optional] Report power at the empirical critical value. Default
            ``True``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_power_study: not implemented."
    )
