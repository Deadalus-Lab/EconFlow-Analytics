# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``high_dimensional_penalized`` -- method card #142.

#142 High-dimensional penalized VAR (structured penalties + rolling-CV lambda)

Category 03-multivariate-nowcasting; module ``high_dimensional_penalized``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bvr_coef",
    "bvr_fit",
    "bvr_predict",
    "NODE_META",
    "wire_model",
]


def bvr_fit(
    *,
    Y: pd.DataFrame,
    p: int | None = None,
    struct: (
        Literal[
            "Basic",
            "Lag",
            "SparseLag",
            "OwnOther",
            "SparseOO",
            "HLAGC",
            "HLAGOO",
            "HLAGELEM",
            "Tapered",
            "EFX",
            "BGR",
        ]
        | None
    ) = None,
    gran: Sequence[int] | None = None,
    h: int | None = None,
    cv: Literal["Rolling", "LOO"] | None = None,
    T1: int | None = None,
    T2: int | None = None,
    IC: bool | None = None,
    ONESE: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvr_fit`` -- method card #142.

    High-dimensional penalized VAR (structured penalties + rolling-CV lambda).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        Y: [multiseries_handle, required] Handle to a multivariate series (panel, T x k, k>=2, no
            NA).
        p: [integer, optional] Maximum VAR lag order (positive integer, default 1). Default ``1``.
        struct: [enum, optional] Penalty structure (default Basic· HLAG*/Tapered VAR-only· EFX
            VARX-only).
        gran: [int_array, optional] [penalty_grid_depth, n_lambda] — two positive integers (default
            [50,10]).
        h: [integer, optional] Forecast horizon for the CV (positive integer, default 1). Default
            ``1``.
        cv: [enum, optional] Cross-validation: Rolling (default) or LOO leave-one-out.
        T1: [integer, optional] CV start index (default floor(T/3)· requires p < T1 < T2).
        T2: [integer, optional] Forecast-evaluation start index (default floor(2T/3)· T1 < T2 <= T).
        IC: [boolean, optional] Include AIC/BIC benchmarks (default True). Default ``True``.
        ONESE: [boolean, optional] One-Standard-Error heuristic for lambda selection (default
            False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvr_fit: not implemented."
    )


def bvr_predict(
    *,
    model: Any,
    n_ahead: int | None = None,
    confint: bool | None = None,
) -> dict[str, Any]:
    """Node ``bvr_predict`` -- method card #142.

    High-dimensional penalized VAR (structured penalties + rolling-CV lambda).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a BigVAR.results model (from bvr_fit).
        n_ahead: [integer, optional] Horizon· returns a forecast path n.ahead x k (default 1).
            Default ``1``.
        confint: [boolean, optional] Return the 95% CI (lower/upper) in addition to the point
            forecast (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvr_predict: not implemented."
    )


def bvr_coef(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``bvr_coef`` -- method card #142.

    High-dimensional penalized VAR (structured penalties + rolling-CV lambda).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a BigVAR.results model (sparse coefficient matrix k
            x kp+1).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bvr_coef: not implemented."
    )
