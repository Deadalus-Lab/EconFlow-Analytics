# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayesian_regression`` -- method card #69.

#69 Bayesian regression models

Category 14-bayesian-toolkit; module ``bayesian_regression``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

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
    "breg_fit",
    "breg_make_formula",
    "breg_set_prior",
    "NODE_META",
    "wire_model",
]


def breg_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    family: (
        Literal[
            "gaussian",
            "student",
            "bernoulli",
            "poisson",
            "negbinomial",
            "Gamma",
            "lognormal",
        ]
        | None
    ) = None,
    prior: Any | None = None,
    seed: int,
    chains: int | None = None,
    iter: int | None = None,
    rhat_threshold: float | None = None,
    neff_ratio_threshold: float | None = None,
    allow_nonconvergence: bool | None = None,
) -> dict[str, Any]:
    """Node ``breg_fit`` -- method card #69.

    Bayesian regression models.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        formula: [formula, required] Regression formula AS A STRING (ACE-sanitized), e.g. 'y ~ x1 +
            x2'.
        data: [df_handle, required] Handle to a DataFrame with columns matching the formula (WITHOUT
            NA in the model columns).
        family: [enum, optional] Family AS A STRING (default gaussian· Gamma uses the LOG link, not
            INVERSE).
        prior: [raw_handle, optional] Handle to a 'brmsprior' (from breg_set_prior)· optional.
        seed: [integer, required] REQUIRED seed (Stan RNG· default RANDOM).
        chains: [integer, optional] Number of chains (default 2). Default ``2``.
        iter: [integer, optional] Iterations per chain (default 1000, warmup=iter/2). Default
            ``1000``.
        rhat_threshold: [number, optional] Threshold of the rank-normalized R-hat (default 1.01).
            Default ``1.01``.
        neff_ratio_threshold: [number, optional] Minimum neff_ratio (default 0.1). Default ``0.1``.
        allow_nonconvergence: [boolean, optional] True -> converged=False instead of stop on
            non-convergence. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "breg_fit: not implemented."
    )


def breg_set_prior(
    *,
    prior: str,
    class_: str | None = None,
) -> dict[str, Any]:
    """Node ``breg_set_prior`` -- method card #69.

    Bayesian regression models.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        prior: [string, required] Stan prior distribution AS A STRING (e.g. 'normal(0, 5)')· it is
            parsed by Stan and never evaluated as code here.
        class_ (wire name ``class``): [string, optional] Prior class (e.g. 'b' coefficients,
            'Intercept', 'sigma'· default 'b'). Default ``'b'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "breg_set_prior: not implemented."
    )


def breg_make_formula(
    *,
    formula: str,
) -> dict[str, Any]:
    """Node ``breg_make_formula`` -- method card #69.

    Bayesian regression models.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        formula: [formula, required] Regression formula AS A STRING (e.g. 'y ~ x1 + x2') ->
            brmsformula (ACE-sanitized).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "breg_make_formula: not implemented."
    )
