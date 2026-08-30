# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multivariate_imputation`` -- method card #384.

#384 Multivariate imputation: MICE, iterative, KNN and EM

Category 00-data-utilities; module ``multivariate_imputation``.

Reference implementation: miceforest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np
import pandas as pd

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_impute",
    "du_pool_imputations",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_impute(
    *,
    data: pd.DataFrame,
    method: Literal["mice", "iterative", "knn", "em", "mean", "median"] | None = None,
    n_imputations: int | None = None,
    max_iter: int | None = None,
    columns: Sequence[str] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``du_impute`` -- method card #384.

    Multivariate imputation: MICE, iterative, KNN and EM.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Table with missing values.
        method: [enum, optional] Imputation method. Default ``'mice'``.
        n_imputations: [integer, optional] Number of imputations for the multiple methods. Default
            ``5``.
        max_iter: [integer, optional] Iterations per chain. Default ``10``.
        columns: [series_codes, optional] Columns to impute; omitted = all with missing values.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "du_impute: not implemented."
    )


def du_pool_imputations(
    *,
    estimates: np.ndarray,
    variances: np.ndarray,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``du_pool_imputations`` -- method card #384.

    Multivariate imputation: MICE, iterative, KNN and EM.

    Category 00-data-utilities; memory class ``light``.

    Args:
        estimates: [matrix_handle, required] Estimates, one row per imputation.
        variances: [matrix_handle, required] Corresponding variances.
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
        "du_pool_imputations: not implemented."
    )
