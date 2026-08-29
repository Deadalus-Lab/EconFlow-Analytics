# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sparse_dynamic_factor`` -- method card #144.

#144 Sparse Dynamic Factor Model (EM with LASSO sparse loadings; arbitrary missing data /
    ragged-edge nowcasting; PCA/2Stage/EM/EM-sparse)

Category 03-multivariate-nowcasting; module ``sparse_dynamic_factor``.

Reference implementation: 10.1007/s11222-023-10378-1.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sdf_factors",
    "sdf_fit",
    "sdf_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sdf_fit(
    *,
    X: pd.DataFrame,
    r: int,
    method: Literal["EM-sparse", "PCA", "2Stage", "EM"] | None = None,
    err: Literal["IID", "AR1"] | None = None,
    q: int | None = None,
    alpha: Sequence[float] | None = None,
    standardize: bool | None = None,
    max_iter: int | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``sdf_fit`` -- method card #144.

    Sparse Dynamic Factor Model (EM with LASSO sparse loadings; arbitrary missing data / ragged-edge
    nowcasting; PCA/2Stage/EM/EM-sparse).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        X: [multiseries_handle, required] Handle to panel data (T x p, >=2 columns, T>=10· NA
            allowed).
        r: [integer, required] Number of factors· positive integer with 1 <= r < the column count of
            X.
        method: [enum, optional] Estimation algorithm (default EM-sparse = LASSO sparse loadings).
        err: [enum, optional] Idiosyncratic errors (default IID· AR1 does NOT support sdf_predict).
        q: [integer, optional] The first q series are NOT made sparse (default 0· 0 <= q < the
            column count of X). Default ``0``.
        alpha: [num_array, optional] Grid LASSO penalties (>=0)· None -> logspace(-2,3,100) default
            (EM-sparse).
        standardize: [boolean, optional] Standardise the data before estimation (default True).
            Default ``True``.
        max_iter: [integer, optional] Maximum EM iterations (default 100). Default ``100``.
        threshold: [number, optional] Convergence tolerance of the EM iterates (default 1e-4).
            Default ``0.0001``.

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
        "sdf_fit: not implemented."
    )


def sdf_predict(
    *,
    model: Any,
    h: int | None = None,
    standardize: bool | None = None,
) -> dict[str, Any]:
    """Node ``sdf_predict`` -- method card #144.

    Sparse Dynamic Factor Model (EM with LASSO sparse loadings; arbitrary missing data / ragged-edge
    nowcasting; PCA/2Stage/EM/EM-sparse).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a sparseDFM model (from sdf_fit· requires
            err='IID').
        h: [integer, optional] Forecast/nowcast horizon (default 1). Default ``1``.
        standardize: [boolean, optional] Output in standardised units (default False = original
            units). Default ``False``.

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
        "sdf_predict: not implemented."
    )


def sdf_factors(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``sdf_factors`` -- method card #144.

    Sparse Dynamic Factor Model (EM with LASSO sparse loadings; arbitrary missing data / ragged-edge
    nowcasting; PCA/2Stage/EM/EM-sparse).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a sparseDFM model (extracts factor paths +
            covariances).

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
        "sdf_factors: not implemented."
    )
