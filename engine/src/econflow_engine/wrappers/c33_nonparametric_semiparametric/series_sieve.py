# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``series_sieve`` -- method card #287.

#287 Series and sieve estimation with polynomial and spline bases

Category 33-nonparametric-semiparametric; module ``series_sieve``.

Reference implementation: formulaic.

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
    "np_basis",
    "np_series_regress",
    "NODE_META",
    "wire_model",
]


def np_basis(
    *,
    x: pd.Series,
    basis: Literal["polynomial", "bspline", "natural_spline", "fourier", "legendre"] | None = None,
    df: int | None = None,
    degree: int | None = None,
    knots: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``np_basis`` -- method card #287.

    Series and sieve estimation with polynomial and spline bases.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        x: [series_handle, required] Covariate to expand.
        basis: [enum, optional] Basis family. Default ``'bspline'``.
        df: [integer, optional] Basis dimension. Default ``5``.
        degree: [integer, optional] Spline degree. Default ``3``.
        knots: [num_array, optional] Interior knots; omitted = quantile-spaced.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_basis: not implemented."
    )


def np_series_regress(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    basis: Literal["polynomial", "bspline", "natural_spline"] | None = None,
    k_max: int | None = None,
    criterion: Literal["aic", "bic", "cv"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``np_series_regress`` -- method card #287.

    Series and sieve estimation with polynomial and spline bases.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [series_handle, required] Dependent variable.
        x: [multiseries_handle, required] Covariates to expand.
        basis: [enum, optional] Basis family. Default ``'bspline'``.
        k_max: [integer, optional] Largest basis dimension searched. Default ``10``.
        criterion: [enum, optional] Selection criterion. Default ``'aic'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_series_regress: not implemented."
    )
