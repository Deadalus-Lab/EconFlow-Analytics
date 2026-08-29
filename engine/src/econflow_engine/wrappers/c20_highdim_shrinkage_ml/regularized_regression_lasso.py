# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``regularized_regression_lasso`` -- method card #216.

#216 Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path)

Category 20-highdim-shrinkage-ml; module ``regularized_regression_lasso``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "enet_coefficients",
    "enet_cv",
    "enet_fit",
    "enet_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def enet_fit(
    *,
    x: np.ndarray,
    y: np.ndarray,
    family: Literal["gaussian", "binomial", "poisson", "multinomial"] | None = None,
    alpha: float | None = None,
    nlambda: int | None = None,
    standardize: bool | None = None,
    intercept: bool | None = None,
) -> dict[str, Any]:
    """Node ``enet_fit`` -- method card #216.

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
        "enet_fit: not implemented."
    )


def enet_cv(
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
    """Node ``enet_cv`` -- method card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``cv``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n×p, p>=2, without
            NA/Inf).
        y: [matrix_handle, required] Handle to the response y (length == the row count of x); gates
            per family as in enet_fit.
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
        "enet_cv: not implemented."
    )


def enet_coefficients(
    *,
    object: Any,
    lambda_: float | None = None,
    which: Literal["lambda_min", "lambda_1se"] | None = None,
) -> dict[str, Any]:
    """Node ``enet_coefficients`` -- method card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a elastic_net or the cross-validated elastic net
            fit (from enet_fit.model / enet_cv.cv register).
        lambda_ (wire name ``lambda``): [number, optional] Explicit lambda (non-negative). REQUIRED
            for a elastic_net path fit; for the cross-validated fit it overrides 'which'.
        which: [enum, optional] For the cross-validated fit: lambda_min (min CV error) or lambda_1se
            (parsimonious).

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
        "enet_coefficients: not implemented."
    )


def enet_predict(
    *,
    object: Any,
    newx: np.ndarray,
    lambda_: float | None = None,
    which: Literal["lambda_min", "lambda_1se"] | None = None,
    type: Literal["link", "response", "class"] | None = None,
) -> dict[str, Any]:
    """Node ``enet_predict`` -- method card #216.

    Regularized regression: Lasso / Ridge / Elastic-Net (+ a k-fold CV path).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a elastic_net or the cross-validated elastic net
            fit (from enet_fit/enet_cv register).
        newx: [matrix_handle, required] Handle to a new design matrix (same p columns as the
            training x, without NA/Inf).
        lambda_ (wire name ``lambda``): [number, optional] Explicit lambda; REQUIRED for a
            elastic_net path fit; cv overrides 'which'.
        which: [enum, optional] For the cross-validated fit: lambda_min or lambda_1se.
        type: [enum, optional] link (linear predictor); response (probabilities/mean value); class
            (label — only binomial/multinomial).

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
        "enet_predict: not implemented."
    )
