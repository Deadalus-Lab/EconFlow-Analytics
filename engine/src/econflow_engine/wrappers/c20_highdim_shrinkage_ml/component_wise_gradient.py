# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``component_wise_gradient`` -- method card #218.

#218 Component-wise gradient boosting — high-dimensional shrinkage + automatic variable selection
    with custom losses

Category 20-highdim-shrinkage-ml; module ``component_wise_gradient``.

Reference implementation: 10.1214/07-STS242.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "boost_glm_cv",
    "boost_glm_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def boost_glm_fit(
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
    """Node ``boost_glm_fit`` -- method card #218.

    Component-wise gradient boosting — high-dimensional shrinkage + automatic variable selection
    with custom losses.

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
        "boost_glm_fit: not implemented."
    )


def boost_glm_cv(
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
    """Node ``boost_glm_cv`` -- method card #218.

    Component-wise gradient boosting — high-dimensional shrinkage + automatic variable selection
    with custom losses.

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a numeric design matrix X (n x p), without NA/Inf.
        y: [matrix_handle, required] Handle to response y (length n); same requirements per family
            as in boost_glm_fit.
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
        "boost_glm_cv: not implemented."
    )
