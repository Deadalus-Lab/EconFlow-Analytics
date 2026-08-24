# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``kernel_regression`` -- method card #283.

#283 Kernel regression: Nadaraya-Watson, local linear and local polynomial with mixed data

Category 33-nonparametric-semiparametric; module ``kernel_regression``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_kernel_regress",
    "np_local_polynomial",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def np_kernel_regress(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    var_type: str | None = None,
    estimator: Literal["lc", "ll"] | None = None,
    bandwidth: Sequence[float] | None = None,
    grid: Sequence[float] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_kernel_regress`` -- method card #283.

    Kernel regression: Nadaraya-Watson, local linear and local polynomial with mixed data.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Covariates, one column each.
        var_type: [string, optional] One character per covariate: c continuous, o ordered, u
            unordered.
        estimator: [enum, optional] Local estimator. Default ``'ll'``.
        bandwidth: [num_array, optional] Bandwidth per covariate; omitted = data-driven.
        grid: [num_array, optional] Evaluation points; omitted = the observed covariates.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "np_kernel_regress: not implemented."
    )


def np_local_polynomial(
    *,
    y: pd.Series,
    x: pd.Series,
    degree: int | None = None,
    deriv: int | None = None,
    bandwidth: float | None = None,
    kernel: Literal["epanechnikov", "gaussian", "uniform", "triangular", "biweight"] | None = None,
) -> dict[str, Any]:
    """Node ``np_local_polynomial`` -- method card #283.

    Kernel regression: Nadaraya-Watson, local linear and local polynomial with mixed data.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [series_handle, required] Single continuous covariate.
        degree: [integer, optional] Polynomial degree fitted locally. Default ``1``.
        deriv: [integer, optional] Order of the derivative to return. Default ``0``.
        bandwidth: [number, optional] Bandwidth; omitted = plug-in.
        kernel: [enum, optional] Kernel function. Default ``'epanechnikov'``.

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
        "np_local_polynomial: not implemented."
    )
