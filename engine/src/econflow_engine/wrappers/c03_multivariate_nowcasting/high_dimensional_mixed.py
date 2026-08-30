# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``high_dimensional_mixed`` -- method card #145.

#145 High-dimensional mixed-frequency regression via MIDAS-ML sparse-group LASSO
    (Legendre/Gegenbauer weighted high-frequency blocks -> a low-frequency target, sg-LASSO lambda +
    mixing gamma, CV-tuned)

Category 03-multivariate-nowcasting; module ``high_dimensional_mixed``.

Reference implementation: 10.1080/07350015.2021.1899933.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mml_cv",
    "mml_fit",
    "mml_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mml_fit(
    *,
    y: Sequence[float],
    X: np.ndarray,
    group: Sequence[int],
    degree: int | None = None,
    weight: Literal["legendre", "gegenbauer", "none"] | None = None,
    gb_alpha: float | None = None,
    gamma: float | None = None,
    lambda_: Sequence[float] | None = None,
    nlambda: int | None = None,
    intercept: bool | None = None,
    standardize: bool | None = None,
) -> dict[str, Any]:
    """Node ``mml_fit`` -- method card #145.

    High-dimensional mixed-frequency regression via MIDAS-ML sparse-group LASSO (Legendre/Gegenbauer
    weighted high-frequency blocks -> a low-frequency target, sg-LASSO lambda + mixing gamma,
    CV-tuned).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Low-frequency target (T x 1 numeric vector, aligned with X).
        X: [matrix_handle, required] High-frequency predictor block (T x p)· columns grouped per
            predictor (jmax lags each).
        group: [int_array, required] Predictor label per column of X (length==the column count of
            X)· defines the MIDAS blocks.
        degree: [integer, optional] Degree of the polynomial basis (degree+1 basis functions per
            predictor· default 3). Default ``3``.
        weight: [enum, optional] MIDAS weighting basis (default legendre· none = no lag
            compression).
        gb_alpha: [number, optional] Gegenbauer alpha parameter (only for weight=gegenbauer· alpha=0
            -> Legendre). Default ``1``.
        gamma: [number, optional] sg-LASSO mixing in [0,1] (0 = group LASSO, 1 = LASSO· default
            0.5). Default ``0.5``.
        lambda_ (wire name ``lambda``): [num_array, optional] Optional sequence of positive lambda
            values (otherwise an automatic lambda path).
        nlambda: [integer, optional] Length of the automatic lambda path (default 100). Default
            ``100``.
        intercept: [boolean, optional] Fit an intercept (default True). Default ``True``.
        standardize: [boolean, optional] Standardise the regressors (default False· the MIDAS basis
            is already orthonormal). Default ``False``.

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
        "mml_fit: not implemented."
    )


def mml_cv(
    *,
    y: Sequence[float],
    X: np.ndarray,
    group: Sequence[int],
    degree: int | None = None,
    weight: Literal["legendre", "gegenbauer", "none"] | None = None,
    gb_alpha: float | None = None,
    gamma: float | None = None,
    lambda_: Sequence[float] | None = None,
    nfolds: int | None = None,
    intercept: bool | None = None,
    standardize: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mml_cv`` -- method card #145.

    High-dimensional mixed-frequency regression via MIDAS-ML sparse-group LASSO (Legendre/Gegenbauer
    weighted high-frequency blocks -> a low-frequency target, sg-LASSO lambda + mixing gamma,
    CV-tuned).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Low-frequency target (T x 1, aligned with X).
        X: [matrix_handle, required] High-frequency predictor block (T x p· columns per predictor).
        group: [int_array, required] Predictor label per column of X (length==the column count of
            X).
        degree: [integer, optional] Degree of the polynomial basis (default 3). Default ``3``.
        weight: [enum, optional] MIDAS weighting basis (default legendre).
        gb_alpha: [number, optional] Gegenbauer alpha (only for weight=gegenbauer). Default ``1``.
        gamma: [number, optional] sg-LASSO mixing in [0,1] (default 0.5). Default ``0.5``.
        lambda_ (wire name ``lambda``): [num_array, optional] Optional sequence of positive lambda
            values (otherwise an automatic path).
        nfolds: [integer, optional] Number of CV folds (3..nrow, default 10). Default ``10``.
        intercept: [boolean, optional] Fit an intercept (default True). Default ``True``.
        standardize: [boolean, optional] Standardise the regressors (default False). Default
            ``False``.
        seed: [integer, optional] Seed for a reproducible fold partition (CV resampling ->
            determinism/cache).

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
        "mml_cv: not implemented."
    )


def mml_predict(
    *,
    model: Any,
    newx: np.ndarray,
    s: Literal["lam.min", "lam.1se"] | None = None,
) -> dict[str, Any]:
    """Node ``mml_predict`` -- method card #145.

    High-dimensional mixed-frequency regression via MIDAS-ML sparse-group LASSO (Legendre/Gegenbauer
    weighted high-frequency blocks -> a low-frequency target, sg-LASSO lambda + mixing gamma,
    CV-tuned).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an 'mml_model' (from mml_fit or mml_cv).
        newx: [matrix_handle, required] New high-frequency block· ncol == length(group) of the fit
            (same lag structure).
        s: [enum, optional] lambda selection for a CV model (lam.min default)· for a path model
            leave it empty (uses the default lambda).

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
        "mml_predict: not implemented."
    )
