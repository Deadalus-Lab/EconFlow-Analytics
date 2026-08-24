# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ensemble_kalman`` -- method card #483.

#483 Ensemble Kalman and square-root filters

Category 10-trend-cycle-statespace; module ``ensemble_kalman``.

Reference implementation: filterpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c10_trend_cycle_statespace import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tc_ensemble_kalman",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tc_ensemble_kalman(
    *,
    y: pd.DataFrame,
    transition: np.ndarray,
    observation: np.ndarray,
    state_cov: np.ndarray,
    obs_cov: np.ndarray,
    filter_type: Literal["standard", "square_root", "ensemble", "unscented"] | None = None,
    ensemble_size: int | None = None,
    smooth: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tc_ensemble_kalman`` -- method card #483.

    Ensemble Kalman and square-root filters.

    Category 10-trend-cycle-statespace; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Observations.
        transition: [matrix_handle, required] State transition matrix.
        observation: [matrix_handle, required] Observation matrix.
        state_cov: [matrix_handle, required] State noise covariance.
        obs_cov: [matrix_handle, required] Observation noise covariance.
        filter_type: [enum, optional] Filter variant. Default ``'square_root'``.
        ensemble_size: [integer, optional] Ensemble members. Default ``100``.
        smooth: [boolean, optional] Also run the smoother. Default ``True``.
        seed: [integer, optional] Seed for the random number generator.

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
        "tc_ensemble_kalman: not implemented."
    )
