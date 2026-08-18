# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``regularized_regression_lasso`` -- METHOD-SELECTION card #216.

#216 Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path)

Category 20-highdim-shrinkage-ml; module ``regularized_regression_lasso``.

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
    "cv_glmnet",
    "fit_glmnet",
    "glmnet_coefficients",
    "glmnet_predict",
    "NODE_META",
    "wire_model",
]


def fit_glmnet(
    *,
    x: np.ndarray,
    y: np.ndarray,
    family: Literal["gaussian", "binomial", "poisson", "multinomial"] | None = None,
    alpha: float | None = None,
    nlambda: int | None = None,
    standardize: bool | None = None,
    intercept: bool | None = None,
) -> dict[str, Any]:
    """Node ``fit_glmnet`` -- METHOD-SELECTION card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n×p, p>=2 columns, without
            NA/Inf). The predictors — NEVER in the schema, they pass as a handle.
        y: [matrix_handle, required] Handle to the response y (length == the row count of x).
            gaussian: numeric; poisson: non-negative counts; binomial: 2 classes; multinomial: >=3.
        family: [enum, optional] Distribution/loss (default gaussian; binomial/poisson/multinomial).
        alpha: [number, optional] Elastic-net mixing ∈ [0,1]: 1=Lasso (sparse), 0=Ridge,
            intermediate=Elastic-Net. Default ``1``.
        nlambda: [integer, optional] Number of points on the lambda path (default 100). Default
            ``100``.
        standardize: [boolean, optional] Standardization of predictors before the fit (default
            True). Default ``True``.
        intercept: [boolean, optional] Inclusion of intercept (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fit_glmnet: not implemented. The method card is in ./README.md."
    )


def cv_glmnet(
    *,
    x: np.ndarray,
    y: np.ndarray,
    family: Literal["gaussian", "binomial", "poisson", "multinomial"] | None = None,
    alpha: float | None = None,
    nfolds: int | None = None,
    type_measure: Literal["default", "mse", "deviance", "mae", "class", "auc"] | None = None,
    seed: int | None = None,
    standardize: bool | None = None,
    intercept: bool | None = None,
) -> dict[str, Any]:
    """Node ``cv_glmnet`` -- METHOD-SELECTION card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``cv``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n×p, p>=2, without
            NA/Inf).
        y: [matrix_handle, required] Handle to the response y (length == the row count of x); gates
            per family as in fit_glmnet.
        family: [enum, optional] Distribution/loss (default gaussian).
        alpha: [number, optional] Elastic-net mixing ∈ [0,1] (1=Lasso, 0=Ridge). Default ``1``.
        nfolds: [integer, optional] Number of CV folds (>=3, <= n; default 10). Default ``10``.
        type_measure: [enum, optional] CV metric (default = family default); auc only binomial;
            class only binomial/multinomial.
        seed: [integer, optional] Seed for DETERMINISTIC foldid (same seed => identical CV). Default
            ``42``.
        standardize: [boolean, optional] Standardization of predictors (default True). Default
            ``True``.
        intercept: [boolean, optional] Inclusion of intercept (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cv_glmnet: not implemented. The method card is in ./README.md."
    )


def glmnet_coefficients(
    *,
    object: Any,
    lambda_: float | None = None,
    which: Literal["lambda.min", "lambda.1se"] | None = None,
) -> dict[str, Any]:
    """Node ``glmnet_coefficients`` -- METHOD-SELECTION card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a glmnet or cv.glmnet fit (from fit_glmnet$model /
            cv_glmnet$cv register).
        lambda_ (wire name ``lambda``): [number, optional] Explicit lambda (non-negative). REQUIRED
            for a glmnet path fit; for cv.glmnet it overrides 'which'.
        which: [enum, optional] For cv.glmnet: lambda.min (min CV error) or lambda.1se
            (parsimonious).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "glmnet_coefficients: not implemented. The method card is in ./README.md."
    )


def glmnet_predict(
    *,
    object: Any,
    newx: np.ndarray,
    lambda_: float | None = None,
    which: Literal["lambda.min", "lambda.1se"] | None = None,
    type: Literal["link", "response", "class"] | None = None,
) -> dict[str, Any]:
    """Node ``glmnet_predict`` -- METHOD-SELECTION card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a glmnet or cv.glmnet fit (from
            fit_glmnet/cv_glmnet register).
        newx: [matrix_handle, required] Handle to a new design matrix (same p columns as the
            training x, without NA/Inf).
        lambda_ (wire name ``lambda``): [number, optional] Explicit lambda; REQUIRED for a glmnet
            path fit; cv overrides 'which'.
        which: [enum, optional] For cv.glmnet: lambda.min or lambda.1se.
        type: [enum, optional] link (linear predictor); response (probabilities/mean value); class
            (label — only binomial/multinomial).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "glmnet_predict: not implemented. The method card is in ./README.md."
    )
