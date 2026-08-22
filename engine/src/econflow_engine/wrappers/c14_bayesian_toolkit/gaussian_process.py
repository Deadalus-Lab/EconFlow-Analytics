# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gaussian_process`` -- method card #512.

#512 Gaussian-process regression and Bayesian nonparametric trends

Category 14-bayesian-toolkit; module ``gaussian_process``.

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
    "bt_gaussian_process",
    "NODE_META",
    "wire_model",
]


def bt_gaussian_process(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    kernel: Literal["rbf", "matern32", "matern52", "periodic", "linear", "white"] | None = None,
    approximation: Literal["none", "sparse", "hsgp"] | None = None,
    n_inducing: int | None = None,
    draws: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bt_gaussian_process`` -- method card #512.

    Gaussian-process regression and Bayesian nonparametric trends.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Outcome.
        x: [multiseries_handle, required] Inputs.
        kernel: [enum, optional] Covariance kernel. Default ``'matern52'``.
        approximation: [enum, optional] Approximation for large samples. Default ``'none'``.
        n_inducing: [integer, optional] Inducing points for a sparse fit. Default ``100``.
        draws: [integer, optional] Posterior draws. Default ``1000``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_gaussian_process: not implemented."
    )
