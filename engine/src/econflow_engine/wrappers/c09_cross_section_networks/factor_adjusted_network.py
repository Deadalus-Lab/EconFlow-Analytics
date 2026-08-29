# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``factor_adjusted_network`` -- method card #182.

#182 Factor-adjusted network estimation (high-dimensional TS): a common factor + an idiosyncratic
    VAR + Granger/partial-correlation networks

Category 09-cross-section-networks; module ``factor_adjusted_network``.

Reference implementation: 10.1080/07350015.2023.2257270.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fnets_factor",
    "fnets_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fnets_fit(
    *,
    x: np.ndarray,
    q: Any | None = None,
    var_order: int | None = None,
    var_method: Literal["lasso", "ds"] | None = None,
    fm_restricted: bool | None = None,
    center: bool | None = None,
    do_threshold: bool | None = None,
    do_lrpc: bool | None = None,
    tuning: Literal["cv", "bic"] | None = None,
    n_folds: int | None = None,
    path_length: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fnets_fit`` -- method card #182.

    Factor-adjusted network estimation (high-dimensional TS): a common factor + an idiosyncratic VAR
    + Granger/partial-correlation networks.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Numeric matrix T x N (each column = one time series, N>=2, no
            NA/Inf).
        q: [raw, optional] Number of factors: positive integer (>=1) OR selection method "ic"/"er".
            Default ``'ic'``.
        var_order: [integer, optional] Order of the idiosyncratic VAR (positive integer· a vector ->
            selection via tuning). Default ``1``.
        var_method: [enum, optional] VAR estimation method: "lasso" (l1 M-estimation) or "ds"
            (Dantzig selector). Default ``'lasso'``.
        fm_restricted: [boolean, optional] True -> restricted (static PCA) factor model· False ->
            unrestricted (dynamic PCA). Default ``False``.
        center: [boolean, optional] Remove the mean (de-mean) of x. Default ``True``.
        do_threshold: [boolean, optional] Adaptive thresholding of the parameter estimators. Default
            ``False``.
        do_lrpc: [boolean, optional] Estimation of long-run & contemporaneous partial correlation
            (pc/lrpc networks). Default ``True``.
        tuning: [enum, optional] Selection of var.order/lambda: "cv" (cross-validation) or "bic"
            (information criterion). Default ``'cv'``.
        n_folds: [integer, optional] Number of folds when tuning="cv" (positive integer). Default
            ``1``.
        path_length: [integer, optional] Number of regularisation parameter values along the path
            (integer >= 2). Default ``10``.
        seed: [integer, optional] Reproducibility seed (tuning/cv path). Default ``2025``.

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
        "fnets_fit: not implemented."
    )


def fnets_factor(
    *,
    x: np.ndarray,
    q: Any | None = None,
    fm_restricted: bool | None = None,
    center: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fnets_factor`` -- method card #182.

    Factor-adjusted network estimation (high-dimensional TS): a common factor + an idiosyncratic VAR
    + Granger/partial-correlation networks.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Numeric matrix T x N (each column = one time series, N>=2, no
            NA/Inf).
        q: [raw, optional] Number of factors: positive integer (>=1) OR selection method "ic"/"er".
            Default ``'ic'``.
        fm_restricted: [boolean, optional] True -> restricted (static PCA, 2D loadings)· False ->
            unrestricted (dynamic, 3D IRF loadings). Default ``False``.
        center: [boolean, optional] Remove the mean (de-mean) of x. Default ``True``.
        seed: [integer, optional] Reproducibility seed. Default ``2025``.

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
        "fnets_factor: not implemented."
    )
