# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``grouped_level_penalized`` -- method card #220.

#220 Grouped / bi-level penalized regression (group lasso, group MCP/SCAD, gel/cMCP)

Category 20-highdim-shrinkage-ml; module ``grouped_level_penalized``.

Reference implementation: skglm.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c20_highdim_shrinkage_ml import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cv_group_penalized_regression",
    "group_penalized_regression",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def group_penalized_regression(
    *,
    X: np.ndarray,
    y: np.ndarray,
    group: Sequence[int] | None = None,
    penalty: Literal["grLasso", "grMCP", "grSCAD", "gel", "cMCP"] | None = None,
    family: Literal["gaussian", "binomial", "poisson"] | None = None,
    nlambda: int | None = None,
    gamma: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``group_penalized_regression`` -- method card #220.

    Grouped / bi-level penalized regression (group lasso, group MCP/SCAD, gel/cMCP).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        X: [matrix_handle, required] Handle to a numeric design matrix X (n x p; >=1 column, >=2
            rows, without NA/Inf). The columns correspond to the group labels.
        y: [matrix_handle, required] Handle to a numeric response y of length the row count of X.
            binomial -> exactly {0,1}; poisson -> non-negative; without NA/Inf.
        group: [int_array, optional] Grouping vector, length == the column count of X: the group
            integer of each column (0 = unpenalized/always-in group). None -> each column its own
            group (ordinary lasso).
        penalty: [enum, optional] Penalty: grLasso/grMCP/grSCAD select ENTIRE groups together;
            gel/cMCP are bi-level (select groups AND variables within a group). Default grLasso.
        family: [enum, optional] Family: gaussian (continuous y), binomial (binary y {0,1}), poisson
            (non-negative counts). Default gaussian.
        nlambda: [integer, optional] Number of lambda values in the regularization path (>=2,
            default 100). Default ``100``.
        gamma: [number, optional] Concavity parameter for MCP/SCAD (>1; default 3, or 4 for grSCAD).
        alpha: [number, optional] Balance of group-penalty vs ridge, in (0,1] (default 1 = pure
            group penalty). Default ``1``.

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
        "group_penalized_regression: not implemented."
    )


def cv_group_penalized_regression(
    *,
    X: np.ndarray,
    y: np.ndarray,
    group: Sequence[int] | None = None,
    penalty: Literal["grLasso", "grMCP", "grSCAD", "gel", "cMCP"] | None = None,
    family: Literal["gaussian", "binomial", "poisson"] | None = None,
    nfolds: int | None = None,
    seed: int | None = None,
    nlambda: int | None = None,
    gamma: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cv_group_penalized_regression`` -- method card #220.

    Grouped / bi-level penalized regression (group lasso, group MCP/SCAD, gel/cMCP).

    Category 20-highdim-shrinkage-ml; memory class ``light``.

    Args:
        X: [matrix_handle, required] Handle to a numeric design matrix X (n x p; >=1 column, >=2
            rows, without NA/Inf). The columns correspond to the group labels.
        y: [matrix_handle, required] Handle to a numeric response y of length the row count of X.
            binomial -> exactly {0,1}; poisson -> non-negative; without NA/Inf.
        group: [int_array, optional] Grouping vector, length == the column count of X: the group
            integer of each column (0 = unpenalized/always-in group). None -> each column its own
            group (ordinary lasso).
        penalty: [enum, optional] Penalty: grLasso/grMCP/grSCAD select ENTIRE groups together;
            gel/cMCP are bi-level (select groups AND variables within a group). Default grLasso.
        family: [enum, optional] Family: gaussian (continuous y), binomial (binary y {0,1}), poisson
            (non-negative counts). Default gaussian.
        nfolds: [integer, optional] Number of folds in the cross-validation (>=3, <= n; default 10).
            Default ``10``.
        seed: [integer, optional] Seed for the RANDOM assignment of folds (reproducibility; default
            20240720). Same seed -> identical lambda_min. Default ``20240720``.
        nlambda: [integer, optional] Number of lambda values in the regularization path (>=2,
            default 100). Default ``100``.
        gamma: [number, optional] Concavity parameter for MCP/SCAD (>1; default 3, or 4 for grSCAD).
        alpha: [number, optional] Balance of group-penalty vs ridge, in (0,1] (default 1 = pure
            group penalty). Default ``1``.

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
        "cv_group_penalized_regression: not implemented."
    )
