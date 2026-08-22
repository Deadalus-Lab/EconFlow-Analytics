# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``vecm_estimate_johansen`` -- method card #24.

#24 VECM estimate + Johansen rank_test (ML-only) + rank selection + predict

Category 05-cointegration; module ``vecm_estimate_johansen``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vecm_estimate",
    "vecm_predict",
    "vecm_rank_select",
    "vecm_rank_test",
    "NODE_META",
    "wire_model",
]


def vecm_estimate(
    *,
    data: np.ndarray,
    lag: int,
    r: int | None = None,
    include: Literal["const", "trend", "none", "both"] | None = None,
    estim: Literal["2OLS", "ML"] | None = None,
    LRinclude: Literal["none", "const", "trend", "both"] | None = None,
) -> dict[str, Any]:
    """Node ``vecm_estimate`` -- method card #24.

    VECM estimate + Johansen rank_test (ML-only) + rank selection + predict.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns
            I(1)).
        lag: [integer, required] Lag order (in differences); positive integer.
        r: [integer, optional] Cointegration rank; integer 1..(ncol-1) (default 1). Default ``1``.
        include: [enum, optional] Deterministic terms (default const).
        estim: [enum, optional] Estimator; ML is required for vecm_rank_test (default 2OLS).
        LRinclude: [enum, optional] Deterministics in the long-run relation (default none).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vecm_estimate: not implemented."
    )


def vecm_rank_test(
    *,
    vecm: Any,
    type: Literal["eigen", "trace"] | None = None,
    cval: float | None = None,
) -> dict[str, Any]:
    """Node ``vecm_rank_test`` -- method card #24.

    VECM estimate + Johansen rank_test (ML-only) + rank selection + predict.

    Category 05-cointegration; memory class ``light``.

    Args:
        vecm: [raw_handle, required] Handle to a 'VECM' estimated with estim='ML' (from
            vecm_estimate).
        type: [enum, optional] Johansen statistic (default eigen).
        cval: [number, optional] Significance level in (0,1) (default 0.05). Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vecm_rank_test: not implemented."
    )


def vecm_rank_select(
    *,
    data: np.ndarray,
    lag_max: int,
    include: Literal["const", "trend", "none", "both"] | None = None,
) -> dict[str, Any]:
    """Node ``vecm_rank_select`` -- method card #24.

    VECM estimate + Johansen rank_test (ML-only) + rank selection + predict.

    Category 05-cointegration; memory class ``light``.

    Args:
        data: [matrix_handle, required] Handle to a multivariate system (matrix/panel, >=2 columns).
        lag_max: [integer, required] Maximum lag for the search; positive integer.
        include: [enum, optional] Deterministic terms (default const).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vecm_rank_select: not implemented."
    )


def vecm_predict(
    *,
    vecm: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``vecm_predict`` -- method card #24.

    VECM estimate + Johansen rank_test (ML-only) + rank selection + predict.

    Category 05-cointegration; memory class ``light``.

    Args:
        vecm: [raw_handle, required] Handle to a 'VECM' (from vecm_estimate).
        n_ahead: [integer, optional] Forecast horizon; positive integer (default 5). Default ``5``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "vecm_predict: not implemented."
    )
