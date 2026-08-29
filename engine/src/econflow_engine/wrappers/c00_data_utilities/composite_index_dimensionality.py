# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``composite_index_dimensionality`` -- method card #117.

#117 Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck)

Category 00-data-utilities; module ``composite_index_dimensionality``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pca_biplot_coords",
    "pca_composite",
    "pca_n_components",
    "pca_predict",
    "pca_stationarity_precheck",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pca_composite(
    *,
    x: np.ndarray,
    center: bool | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``pca_composite`` -- method card #117.

    Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric matrix of indicators (rows=observations,
            cols=indicators). Plain numeric matrix — NOT DataFrame/ts. Requires >=2 columns, >=3
            rows, no NA/Inf.
        center: [boolean, optional] Center each column on its mean before PCA (prcomp center).
            Default True. Default ``True``.
        scale: [boolean, optional] Scale each column to unit variance (prcomp scale.). Recommended
            for heterogeneous indicators; hard gate on a constant/zero-variance column. Default
            True. Default ``True``.

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
        "pca_composite: not implemented."
    )


def pca_biplot_coords(
    *,
    x: np.ndarray,
    center: bool | None = None,
    scale: bool | None = None,
    choices: Sequence[int] | None = None,
    biplot_scale: float | None = None,
    pc_biplot: bool | None = None,
) -> dict[str, Any]:
    """Node ``pca_biplot_coords`` -- method card #117.

    Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric matrix of indicators (rows=observations,
            cols=indicators); >=2 columns, >=3 rows, no NA/Inf.
        center: [boolean, optional] Center each column before PCA (prcomp center). Default True.
            Default ``True``.
        scale: [boolean, optional] Scale to unit variance (prcomp scale.). Default True; hard gate
            on a constant column. Default ``True``.
        choices: [int_array, optional] TWO DISTINCT component indices in [1, n_comp] (default [1, 2]
            = PC1/PC2). Equal/out of range => stop; ~zero singular value (rank-deficient) => stop.
        biplot_scale: [number, optional] The `scale` of the biplot scaling, in [0, 1] (default 1).
            lam = (sdev*sqrt(n))^biplot_scale; obs = scores/lam, vars = loadings*lam. 1 = form
            biplot (observation distances), 0 = covariance biplot (variable angles/lengths). ⚠️ This
            is NOT the prcomp scale; outside [0,1] => stop (stats only warns). Default ``1``.
        pc_biplot: [boolean, optional] Gabriel (1971) principal-component biplot (lam/sqrt(n)):
            variable inner products ~ covariances, observation distances ~ Mahalanobis. Default
            False. Default ``False``.

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
        "pca_biplot_coords: not implemented."
    )


def pca_predict(
    *,
    x: np.ndarray,
    newdata: np.ndarray,
    center: bool | None = None,
    scale: bool | None = None,
) -> dict[str, Any]:
    """Node ``pca_predict`` -- method card #117.

    Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to the TRAINING matrix (fit). It MUST have column labels
            — without them predict.prcomp matches columns BY POSITION and projects SILENTLY WRONG
            (hard gate).
        newdata: [matrix_handle, required] Handle to the NEW observations to project; IDENTICAL
            column labels AND SAME ORDER as x, >=1 row, no NA/Inf.
        center: [boolean, optional] Centering at fit time (prcomp center); the APPLIED center is
            returned as center_used. Default True. Default ``True``.
        scale: [boolean, optional] Scaling at fit time (prcomp scale.); the APPLIED scale is
            returned as scale_used. Default True. Default ``True``.

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
        "pca_predict: not implemented."
    )


def pca_n_components(
    *,
    x: np.ndarray,
    center: bool | None = None,
    scale: bool | None = None,
    cum_var_threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pca_n_components`` -- method card #117.

    Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric matrix of indicators; >=2 columns, >=3
            rows, no NA/Inf.
        center: [boolean, optional] Center each column (prcomp center). Default True. Default
            ``True``.
        scale: [boolean, optional] True (default) => eigenvalues of the CORRELATION matrix,
            Kaiser-Guttman threshold = 1 (Kaiser 1960). False => COVARIANCE, threshold =
            mean(eigenvalues) (Jolliffe 2002 §6.1.2); kaiser_basis/kaiser_threshold are returned
            explicitly. Default ``True``.
        cum_var_threshold: [number, optional] Cumulative-variance threshold in [0.5, 1] (Jolliffe
            2002 §6.1.1; typically 0.70-0.90; default 0.90). The SMALLEST k with cum_var >=
            threshold is returned. Default ``0.9``.

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
        "pca_n_components: not implemented."
    )


def pca_stationarity_precheck(
    *,
    x: np.ndarray,
    null_hypothesis: Literal["Level", "Trend"] | None = None,
    lshort: bool | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pca_stationarity_precheck`` -- method card #117.

    Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance
    decomposition + biplot coordinates + newdata projection + rules for the number of components +
    KPSS precheck).

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to the SAME matrix that will be passed to pca_composite;
            >=2 columns, >=3 rows, no NA/Inf.
        null_hypothesis: [enum, optional] KPSS null hypothesis: Level (default, level-stationary) or
            Trend (trend-stationary).
        lshort: [boolean, optional] True (default) => truncation lag floor(4*(n/100)^0.25); False =>
            floor(12*(n/100)^0.25) (the kpss.test documentation). Default ``True``.
        alpha: [number, optional] Significance level in [0.01, 0.10] (default 0.05). the test
            returns a p-value ONLY inside that interval (interpolation in the KPSS 1992 Table 1);
            outside => undecidable => stop. Per column, p_at_bound (lower/interpolated/upper) is
            returned. Default ``0.05``.

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
        "pca_stationarity_precheck: not implemented."
    )
