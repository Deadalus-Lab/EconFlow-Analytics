# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quasi_random`` -- method card #315.

#315 Quasi-random and low-discrepancy sequences

Category 36-monte-carlo-design; module ``quasi_random``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_discrepancy",
    "mc_qmc_sample",
    "NODE_META",
    "wire_model",
]


def mc_qmc_sample(
    *,
    n_dimensions: int,
    n_samples: int,
    sequence: Literal["sobol", "halton", "latin_hypercube", "poisson_disk"] | None = None,
    scramble: bool | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_qmc_sample`` -- method card #315.

    Quasi-random and low-discrepancy sequences.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        n_dimensions: [integer, required] Dimension of the sample.
        n_samples: [integer, required] Number of points.
        sequence: [enum, optional] Sequence family. Default ``'sobol'``.
        scramble: [boolean, optional] Randomise the sequence to permit an error estimate. Default
            ``True``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_qmc_sample: not implemented."
    )


def mc_discrepancy(
    *,
    sample: np.ndarray,
    method: Literal["cd", "wd", "md", "l2_star"] | None = None,
) -> dict[str, Any]:
    """Node ``mc_discrepancy`` -- method card #315.

    Quasi-random and low-discrepancy sequences.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        sample: [matrix_handle, required] Point set to assess.
        method: [enum, optional] Discrepancy measure. Default ``'cd'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_discrepancy: not implemented."
    )
