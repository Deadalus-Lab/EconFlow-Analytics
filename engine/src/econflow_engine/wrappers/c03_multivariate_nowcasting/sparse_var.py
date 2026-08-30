# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sparse_var`` -- method card #423.

#423 Sparse and regularised VAR via penalised multi-task regression

Category 03-multivariate-nowcasting; module ``sparse_var``.

Reference implementation: skglm.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mn_sparse_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mn_sparse_var(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    penalty: Literal["lasso", "ridge", "elastic_net", "group_lasso", "hierarchical"] | None = None,
    lambda_: float | None = None,
    n_folds: int | None = None,
    own_lag_penalty: float | None = None,
) -> dict[str, Any]:
    """Node ``mn_sparse_var`` -- method card #423.

    Sparse and regularised VAR via penalised multi-task regression.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] Maximum lag order. Default ``12``.
        penalty: [enum, optional] Penalty family. Default ``'lasso'``.
        lambda_: [number, optional] Penalty strength; omitted = cross-validated.
        n_folds: [integer, optional] Time-series cross-validation folds. Default ``5``.
        own_lag_penalty: [number, optional] Relative penalty on own lags. Default ``0.5``.

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
        "mn_sparse_var: not implemented."
    )
