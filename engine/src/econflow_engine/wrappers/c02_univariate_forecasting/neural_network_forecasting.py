# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``neural_network_forecasting`` -- method card #133.

#133 Neural-network univariate forecasting: MLP ensemble and extreme learning machine

Category 02-univariate-forecasting; module ``neural_network_forecasting``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c02_univariate_forecasting import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nn_elm",
    "nn_mlp",
    "NODE_META",
    "wire_model",
]


def nn_mlp(
    *,
    y: pd.Series,
    seed: int,
    h: int | None = None,
    hd: int | None = None,
    reps: int | None = None,
    comb: Literal["median", "mean", "mode"] | None = None,
    sel_lag: bool | None = None,
    det_type: Literal["auto", "bin", "trg"] | None = None,
    exog: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``nn_mlp`` -- method card #133.

    Neural-network univariate forecasting: MLP ensemble and extreme learning machine.

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts/msts (the series to forecast).
        seed: [integer, required] REQUIRED seed (seeded before the random weights; cache key;
            uncacheable without it).
        h: [integer, optional] Forecast horizon (positive integer; None -> frequency(y)).
        hd: [integer, optional] Number of hidden nodes (small default 3; keeps the node cheap).
        reps: [integer, optional] Ensemble size (number of networks; default 2; docs 20).
        comb: [enum, optional] Ensemble combination operator (default median).
        sel_lag: [boolean, optional] Automatic lag selection (default True).
        det_type: [enum, optional] Type of deterministic seasonal dummies (default auto).
        exog: [exog_handle, optional] Exogenous regressors (matrix, length >= n+h; NOT a data
            frame).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nn_mlp: not implemented."
    )


def nn_elm(
    *,
    y: pd.Series,
    seed: int,
    h: int | None = None,
    hd: int | None = None,
    type: Literal["lasso", "ridge", "step", "lm"] | None = None,
    reps: int | None = None,
    comb: Literal["median", "mean", "mode"] | None = None,
    sel_lag: bool | None = None,
    direct: bool | None = None,
    det_type: Literal["auto", "bin", "trg"] | None = None,
    exog: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``nn_elm`` -- method card #133.

    Neural-network univariate forecasting: MLP ensemble and extreme learning machine.

    Category 02-univariate-forecasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Handle to a univariate ts/msts.
        seed: [integer, required] REQUIRED seed (seeded before the random hidden weights; cache
            key).
        h: [integer, optional] Forecast horizon (positive integer; None -> frequency(y)).
        hd: [integer, optional] Number of hidden nodes (small default 3).
        type: [enum, optional] Estimation of output-layer weights (default lasso).
        reps: [integer, optional] Ensemble size (default 2).
        comb: [enum, optional] Ensemble combination operator (default median).
        sel_lag: [boolean, optional] Automatic lag selection (default True).
        direct: [boolean, optional] Direct input-output connections for linear effects (default
            False).
        det_type: [enum, optional] Type of deterministic seasonal dummies (default auto).
        exog: [exog_handle, optional] Exogenous regressors (matrix, length >= n+h; NOT a data
            frame).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nn_elm: not implemented."
    )
