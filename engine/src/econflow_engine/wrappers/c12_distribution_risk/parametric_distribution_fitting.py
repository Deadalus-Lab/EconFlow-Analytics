# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``parametric_distribution_fitting`` -- METHOD-SELECTION card #196.

#196 Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs)

Category 12-distribution-risk; module ``parametric_distribution_fitting``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_bootdist",
    "fd_descdist",
    "fd_fit",
    "fd_gof",
    "NODE_META",
    "wire_model",
]


def fd_fit(
    *,
    data: Sequence[float],
    distr: (
        Literal[
            "norm",
            "lnorm",
            "gamma",
            "weibull",
            "exp",
            "pois",
            "nbinom",
            "beta",
        ]
        | None
    ) = None,
    method: Literal["mle", "mme", "qme", "mge"] | None = None,
    probs: Sequence[float] | None = None,
    gof: Literal["CvM", "KS", "AD", "ADR", "ADL", "AD2R", "AD2L", "AD2"] | None = None,
    fix_arg: Any | None = None,
) -> dict[str, Any]:
    """Node ``fd_fit`` -- METHOD-SELECTION card #196.

    Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs).

    Category 12-distribution-risk; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [num_array, required] Vector of numbers (returns/losses/counts)· >=4 values, without
            NA/Inf, with variance.
        distr: [enum, optional] Distribution family (closed set· default norm). The support is
            checked (positive>0· beta∈(0,1)· pois/nbinom non-negative integers).
        method: [enum, optional] Estimator: mle (default)· mme (moments)· qme (quantile matching —
            requires probs)· mge (max GOF distance).
        probs: [num_array, optional] Probabilities in (0,1) for method='qme' (e.g. [0.333,0.667])·
            ignored elsewhere.
        gof: [enum, optional] GOF-distance measure for method='mge' (default CvM)· ignored
            elsewhere.
        fix_arg: [raw, optional] Optional named list of fixed parameters (e.g. {rate:1}) that are
            NOT estimated.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_fit: not implemented. The method card is in ./README.md."
    )


def fd_gof(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``fd_gof`` -- METHOD-SELECTION card #196.

    Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitdist fit (from fd_fit). Continuous ->
            KS/CvM/AD· discrete -> chisq (KS/CvM/AD = NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_gof: not implemented. The method card is in ./README.md."
    )


def fd_descdist(
    *,
    data: Sequence[float],
    discrete: bool | None = None,
    method: Literal["unbiased", "sample"] | None = None,
    boot: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fd_descdist`` -- METHOD-SELECTION card #196.

    Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs).

    Category 12-distribution-risk; memory class ``heavy``.

    Args:
        data: [num_array, required] Vector of numbers· >=4 values, without NA/Inf. Returns
            Cullen-Frey descriptives (NUMBERS, no plot at all).
        discrete: [boolean, optional] True if the data are discrete/counts (default False). Default
            ``False``.
        method: [enum, optional] Estimator skewness/kurtosis (default unbiased).
        boot: [integer, optional] Number of bootstrap samples for the skewness/kurtosis cloud
            (chart-data· >=10 active· None/0 = without). Default ``200``.
        seed: [integer, optional] Reproducibility seed for the bootstrap cloud (default 2025).
            Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_descdist: not implemented. The method card is in ./README.md."
    )


def fd_bootdist(
    *,
    object: Any,
    bootmethod: Literal["param", "nonparam"] | None = None,
    niter: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``fd_bootdist`` -- METHOD-SELECTION card #196.

    Parametric distribution fitting (fit/GOF/Cullen-Frey/bootstrap CIs).

    Category 12-distribution-risk; memory class ``mcmc``.

    Args:
        object: [raw_handle, required] Handle to a fitdist fit (from fd_fit)· bootstrap CIs of the
            parameters.
        bootmethod: [enum, optional] param (default· simulate from the fitted) or nonparam (resample
            of the data).
        niter: [integer, optional] Number of bootstrap replications (>=10· default 200). Default
            ``200``.
        seed: [integer, optional] Reproducibility seed (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fd_bootdist: not implemented. The method card is in ./README.md."
    )
