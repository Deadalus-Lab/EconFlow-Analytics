# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``mixed_frequency_bayesian`` -- METHOD-SELECTION card #17.

#17 Mixed-Frequency Bayesian VAR

Category 03-multivariate-nowcasting; module ``mixed_frequency_bayesian``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mf_estimate",
    "mf_mdd",
    "mf_predict",
    "NODE_META",
    "wire_model",
]


def mf_estimate(
    *,
    Y: Any,
    n_lags: int,
    n_reps: int | None = None,
    n_burnin: int | None = None,
    n_fcst: int | None = None,
    prior: Literal["minn", "ss", "ssng"] | None = None,
    variance: Literal["iw", "diffuse", "csv", "fsv"] | None = None,
    aggregation: Literal["average", "triangular"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mf_estimate`` -- METHOD-SELECTION card #17.

    Mixed-Frequency Bayesian VAR.

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        Y: [raw_handle, required] Handle to a list of >=2 ts of different frequencies (monthly
            before quarterly).
        n_lags: [integer, required] VAR lag order (with aggregation='average' >=3).
        n_reps: [integer, optional] MCMC replications (default 10000). Default ``10000``.
        n_burnin: [integer, optional] Burn-in draws· None -> n_reps/2 (< n_reps).
        n_fcst: [integer, optional] Forecast/nowcast horizon (>0 for mf_predict) (default 0).
            Default ``0``.
        prior: [enum, optional] Prior: Minnesota or steady-state (default minn).
        variance: [enum, optional] Variance structure (default iw· mf_mdd requires iw).
        aggregation: [enum, optional] Low-to-high frequency relation (default average).
        seed: [integer, optional] Seed for reproducibility (optional).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mf_estimate: not implemented. The method card is in ./README.md."
    )


def mf_predict(
    *,
    model: Any,
    pred_bands: float | None = None,
    aggregate_fcst: bool | None = None,
) -> dict[str, Any]:
    """Node ``mf_predict`` -- METHOD-SELECTION card #17.

    Mixed-Frequency Bayesian VAR.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an mfbvar model (from mf_estimate with n_fcst>0).
        pred_bands: [number, optional] Prediction band in (0,1) (default 0.8). Default ``0.8``.
        aggregate_fcst: [boolean, optional] Aggregate high -> low frequency (default True). Default
            ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mf_predict: not implemented. The method card is in ./README.md."
    )


def mf_mdd(
    *,
    model: Any,
    p_trunc: float | None = None,
    method: int | None = None,
) -> dict[str, Any]:
    """Node ``mf_mdd`` -- METHOD-SELECTION card #17.

    Mixed-Frequency Bayesian VAR.

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to an mfbvar model with variance='iw' (model
            comparison).
        p_trunc: [number, optional] Truncation prob for the minn prior in (0,1) (default 0.5).
            Default ``0.5``.
        method: [integer, optional] mdd method (1 or 2) for the steady-state prior (default 1).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mf_mdd: not implemented. The method card is in ./README.md."
    )
