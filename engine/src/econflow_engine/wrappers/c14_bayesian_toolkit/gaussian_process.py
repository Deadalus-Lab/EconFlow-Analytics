# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gaussian_process`` -- method card #512.

#512 Gaussian-process regression and Bayesian nonparametric trends

Category 14-bayesian-toolkit; module ``gaussian_process``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_gaussian_process",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "bt_gaussian_process: not implemented."
    )
