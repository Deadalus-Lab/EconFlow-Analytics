# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``global_sensitivity`` -- method card #312.

#312 Global sensitivity analysis: Sobol, Morris, FAST and delta

Category 36-monte-carlo-design; module ``global_sensitivity``.

Reference implementation: SALib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c36_monte_carlo_design import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mc_morris",
    "mc_sample_design",
    "mc_sobol",
    "NODE_META",
    "wire_model",
]


def mc_sobol(
    *,
    problem: pd.DataFrame,
    outputs: pd.Series,
    n_samples: int | None = None,
    calc_second_order: bool | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``mc_sobol`` -- method card #312.

    Global sensitivity analysis: Sobol, Morris, FAST and delta.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        problem: [df_handle, required] Input definition: names and bounds.
        outputs: [series_handle, required] Model outputs at the generated design.
        n_samples: [integer, optional] Base sample size. Default ``1024``.
        calc_second_order: [boolean, optional] Also compute second-order indices. Default ``False``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_sobol: not implemented."
    )


def mc_morris(
    *,
    problem: pd.DataFrame,
    outputs: pd.Series,
    n_trajectories: int | None = None,
    levels: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_morris`` -- method card #312.

    Global sensitivity analysis: Sobol, Morris, FAST and delta.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        problem: [df_handle, required] Input definition: names and bounds.
        outputs: [series_handle, required] Model outputs at the generated design.
        n_trajectories: [integer, optional] Number of trajectories. Default ``100``.
        levels: [integer, optional] Grid levels per input. Default ``4``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_morris: not implemented."
    )


def mc_sample_design(
    *,
    problem: pd.DataFrame,
    method: Literal["sobol", "morris", "fast", "latin_hypercube", "finite_diff"] | None = None,
    n_samples: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mc_sample_design`` -- method card #312.

    Global sensitivity analysis: Sobol, Morris, FAST and delta.

    Category 36-monte-carlo-design; memory class ``light``.

    Args:
        problem: [df_handle, required] Input definition: names and bounds.
        method: [enum, optional] Sampling scheme required by the analysis. Default ``'sobol'``.
        n_samples: [integer, optional] Base sample size. Default ``1024``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mc_sample_design: not implemented."
    )
