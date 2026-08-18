# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``confidence_set`` -- METHOD-SELECTION card #75.

#75 Model Confidence Set (Hansen-Lunde-Nason)

Category 15-model-evaluation; module ``confidence_set``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "compute_loss_level",
    "compute_loss_vol",
    "run_mcs_procedure",
    "NODE_META",
    "wire_model",
]


def run_mcs_procedure(
    *,
    Loss: np.ndarray,
    alpha: float | None = None,
    B: int | None = None,
    statistic: Literal["Tmax", "TR"] | None = None,
    k: int | None = None,
    min_k: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``run_mcs_procedure`` -- METHOD-SELECTION card #75.

    Model Confidence Set (Hansen-Lunde-Nason).

    Category 15-model-evaluation; memory class ``heavy``.

    Args:
        Loss: [matrix_handle, required] Handle to a loss matrix (rows=observations, columns=models,
            >=2 columns).
        alpha: [number, optional] Confidence level = 1 - alpha (alpha in (0,1), default 0.15).
            Default ``0.15``.
        B: [integer, optional] Number of block-bootstrap replications (positive integer, default
            1000). Default ``1000``.
        statistic: [enum, optional] Equality test statistic (default Tmax).
        k: [integer, optional] Block length of the bootstrap (None = auto· positive integer).
        min_k: [integer, optional] Minimum block length (>= 1, default 3). Default ``3``.
        seed: [integer, optional] Seed for reproducibility of the bootstrap (integer).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_mcs_procedure: not implemented. The method card is in ./README.md."
    )


def compute_loss_level(
    *,
    realized: pd.Series,
    evaluated: np.ndarray,
    which: Literal["SE", "AE"] | None = None,
) -> dict[str, Any]:
    """Node ``compute_loss_level`` -- METHOD-SELECTION card #75.

    Model Confidence Set (Hansen-Lunde-Nason).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        realized: [series_handle, required] Handle to the series of realized values (realized).
        evaluated: [matrix_handle, required] Handle to a matrix of point-forecasts (one column per
            model, same rows).
        which: [enum, optional] Loss function: SE=squared, AE=absolute error (default SE).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "compute_loss_level: not implemented. The method card is in ./README.md."
    )


def compute_loss_vol(
    *,
    realized: pd.Series,
    evaluated: np.ndarray,
    which: Literal["SE1", "SE2", "QLIKE", "R2LOG", "AE1", "AE2"] | None = None,
) -> dict[str, Any]:
    """Node ``compute_loss_vol`` -- METHOD-SELECTION card #75.

    Model Confidence Set (Hansen-Lunde-Nason).

    Category 15-model-evaluation; memory class ``light``.

    Args:
        realized: [series_handle, required] Handle to the realized volatility/variance series
            (proxy).
        evaluated: [matrix_handle, required] Handle to a matrix of volatility-forecasts (one column
            per model).
        which: [enum, optional] Robust volatility loss family (default SE1· QLIKE is robust to the
            proxy).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "compute_loss_vol: not implemented. The method card is in ./README.md."
    )
