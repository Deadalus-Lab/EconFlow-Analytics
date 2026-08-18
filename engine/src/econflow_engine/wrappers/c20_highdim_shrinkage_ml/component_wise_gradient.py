# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``component_wise_gradient`` -- METHOD-SELECTION card #218.

#218 Component-wise gradient boosting (glmboost) — high-dimensional shrinkage + automatic variable
    selection with custom losses

Category 20-highdim-shrinkage-ml; module ``component_wise_gradient``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "glmboost_cv_mstop",
    "glmboost_fit",
    "NODE_META",
    "wire_model",
]


def glmboost_fit(
    *,
    x: np.ndarray,
    y: np.ndarray,
    family: (
        Literal[
            "Gaussian",
            "QuantReg",
            "Binomial",
            "Poisson",
            "Laplace",
            "Huber",
        ]
        | None
    ) = None,
    tau: float | None = None,
    mstop: int | None = None,
    nu: float | None = None,
    center: bool | None = None,
) -> dict[str, Any]:
    """Node ``glmboost_fit`` -- METHOD-SELECTION card #218.

    Component-wise gradient boosting (glmboost) — high-dimensional shrinkage + automatic variable
    selection with custom losses.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n x p predictors), >= 3
            rows, >= 1 column, without NA/Inf.
        y: [matrix_handle, required] Handle to response y (length n).
            Gaussian/QuantReg/Laplace/Huber: numeric; Binomial: EXACTLY 2 values; Poisson:
            non-negative integers (counts).
        family: [enum, optional] Loss family (default Gaussian=L2). QuantReg=pinball(tau)·
            Laplace=L1· Huber=robust· Binomial=logistic· Poisson=counts. Binomial: the $coefficients
            are HALF those of glm(binomial) ($coef_scale="mboost_half_logit"; $positive_class=2nd
            level).
        tau: [number, optional] Quantile in (0,1) when family="QuantReg" (default 0.5). The
            conditional-quantile level = $offset+$intercept and needs ENOUGH mstop to calibrate to
            tau.
        mstop: [integer, optional] Number of boosting steps (regularization; default 100; positive
            integer). Default ``100``.
        nu: [number, optional] Learning rate (shrinkage) in (0,1] (default 0.1).
        center: [boolean, optional] Centering of predictors (default True; offset as intercept).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "glmboost_fit: not implemented. The method card is in ./README.md."
    )


def glmboost_cv_mstop(
    *,
    x: np.ndarray,
    y: np.ndarray,
    family: (
        Literal[
            "Gaussian",
            "QuantReg",
            "Binomial",
            "Poisson",
            "Laplace",
            "Huber",
        ]
        | None
    ) = None,
    tau: float | None = None,
    mstop_max: int | None = None,
    nu: float | None = None,
    center: bool | None = None,
    cv_type: Literal["subsampling", "kfold", "bootstrap"] | None = None,
    cv_B: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``glmboost_cv_mstop`` -- METHOD-SELECTION card #218.

    Component-wise gradient boosting (glmboost) — high-dimensional shrinkage + automatic variable
    selection with custom losses.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n x p), without NA/Inf.
        y: [matrix_handle, required] Handle to response y (length n); same requirements per family
            as in glmboost_fit.
        family: [enum, optional] Loss family (default Gaussian). Binomial: $coefficients HALF those
            of glm ($coef_scale="mboost_half_logit"). QuantReg level = $offset+$intercept.
        tau: [number, optional] Quantile in (0,1) when family="QuantReg" (default 0.5); needs enough
            mstop_max for a calibrated level.
        mstop_max: [integer, optional] Upper bound of boosting steps for the cvrisk grid (>= 2;
            default 200). Default ``200``.
        nu: [number, optional] Learning rate (shrinkage) in (0,1] (default 0.1).
        center: [boolean, optional] Centering of predictors (default True).
        cv_type: [enum, optional] Resampling scheme of cvrisk (default subsampling).
        cv_B: [integer, optional] Number of resamples/folds (>= 2; default 25). Default ``25``.
        seed: [integer, optional] Seed for generating the folds (reproducibility; default 42).
            Default ``42``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "glmboost_cv_mstop: not implemented. The method card is in ./README.md."
    )
