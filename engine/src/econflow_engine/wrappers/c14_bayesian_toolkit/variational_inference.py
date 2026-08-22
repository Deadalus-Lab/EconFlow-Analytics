# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``variational_inference`` -- method card #509.

#509 Variational inference, Pathfinder and Laplace approximation

Category 14-bayesian-toolkit; module ``variational_inference``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_variational",
    "NODE_META",
    "wire_model",
]


def bt_variational(
    *,
    model: Any,
    data: pd.DataFrame,
    method: Literal["advi", "fullrank_advi", "pathfinder", "laplace", "map"] | None = None,
    n_iterations: int | None = None,
    draws: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bt_variational`` -- method card #509.

    Variational inference, Pathfinder and Laplace approximation.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Registers its result under ``approximation``, so a later node can consume it as a handle.

    Args:
        model: [raw, required] Model specification.
        data: [df_handle, required] Data.
        method: [enum, optional] Approximation method. Default ``'pathfinder'``.
        n_iterations: [integer, optional] Optimiser iterations. Default ``20000``.
        draws: [integer, optional] Draws from the approximation. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_variational: not implemented."
    )
