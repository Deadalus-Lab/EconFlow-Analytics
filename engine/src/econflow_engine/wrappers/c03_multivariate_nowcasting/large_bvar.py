# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``large_bvar`` -- method card #421.

#421 Large Bayesian VAR with dummy-observation priors, sum-of-coefficients and co-persistence

Category 03-multivariate-nowcasting; module ``large_bvar``.

Reference implementation: pymc.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_large_bvar",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mn_large_bvar(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    prior: Literal["minnesota", "normal_wishart", "independent_normal_wishart"] | None = None,
    lambda_: float | None = None,
    sum_of_coefficients: bool | None = None,
    co_persistence: bool | None = None,
    draws: int | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``mn_large_bvar`` -- method card #421.

    Large Bayesian VAR with dummy-observation priors, sum-of-coefficients and co-persistence.

    Category 03-multivariate-nowcasting; memory class ``mcmc``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] Lag order. Default ``13``.
        prior: [enum, optional] Prior family. Default ``'minnesota'``.
        lambda_: [number, optional] Overall shrinkage; omitted = chosen by marginal likelihood.
        sum_of_coefficients: [boolean, optional] Add the sum-of-coefficients dummy observations.
            Default ``True``.
        co_persistence: [boolean, optional] Add the co-persistence dummy observation. Default
            ``True``.
        draws: [integer, optional] Posterior draws. Default ``2000``.
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
        "mn_large_bvar: not implemented."
    )
