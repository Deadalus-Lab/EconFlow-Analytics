# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_regression_time`` -- method card #184.

#184 Bayesian regression with time-varying (random-walk) coefficients — HMC (Stan)

Category 10-trend-cycle-statespace; module ``bayesian_regression_time``.

Reference implementation: pymc-extras.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tvreg_coef",
    "tvreg_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tvreg_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    family: Literal["gaussian", "poisson", "binomial"] | None = None,
    rw_order: Literal["rw1", "rw2"] | None = None,
    beta_prior: Sequence[float] | None = None,
    sigma_prior: Sequence[float] | None = None,
    nu_prior: Sequence[float] | None = None,
    sigma_y_prior: Sequence[float] | None = None,
    u: Sequence[float] | None = None,
    chains: int | None = None,
    iter: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tvreg_fit`` -- method card #184.

    Bayesian regression with time-varying (random-walk) coefficients — HMC (Stan).

    Category 10-trend-cycle-statespace; memory class ``mcmc``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Regression formula AS A STRING (ACE-sanitized), e.g. 'y ~ x1 +
            x2'· the regressors become time-varying (wrapped automatically in rw1/rw2).
        data: [df_handle, required] Handle to a TIME-SORTED DataFrame (row = time)· contains
            response + regressors, WITHOUT NA, >=5 rows.
        family: [enum, optional] gaussian -> walker· poisson/binomial -> walker_glm (counts).
            Default ``'gaussian'``.
        rw_order: [enum, optional] Random-walk order of the coefficients: rw1 (level) or rw2 (local
            linear, with slope). Default ``'rw1'``.
        beta_prior: [num_array, optional] [mean, sd]: Gaussian prior of the INITIAL time-varying
            coefficients. Default ``[0, 10]``.
        sigma_prior: [num_array, optional] [shape, rate]: Gamma prior of the walk sd (>0). Default
            ``[2, 0.01]``.
        nu_prior: [num_array, optional] [mean, sd]: prior of the initial slope· ONLY for
            rw_order='rw2'. Default ``[0, 10]``.
        sigma_y_prior: [num_array, optional] [shape, rate]: Gamma prior of the observational sd
            (>0)· ONLY family='gaussian'. Default ``[2, 0.01]``.
        u: [num_array, optional] poisson -> exposures (E(y)=u*exp(x*beta))· binomial -> number of
            trials· length 1 or n· ONLY glm (default 1).
        chains: [integer, optional] Number of HMC chains (SMALL· default 1). Default ``1``.
        iter: [integer, optional] Iterations per chain (SMALL· default 400, warmup=iter/2). Default
            ``400``.
        seed: [integer, optional] Reproducibility seed (seeded + Stan sampler seed). Default
            ``2025``.

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
        "tvreg_fit: not implemented."
    )


def tvreg_coef(
    *,
    object: Any,
    exponentiate: bool | None = None,
) -> dict[str, Any]:
    """Node ``tvreg_coef`` -- method card #184.

    Bayesian regression with time-varying (random-walk) coefficients — HMC (Stan).

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted 'tvreg_fit' object (from
            tvreg_fit.object).
        exponentiate: [boolean, optional] exp on the coefficients (link-scale -> multiplicative·
            useful for poisson/binomial). Default ``False``.

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
        "tvreg_coef: not implemented."
    )
