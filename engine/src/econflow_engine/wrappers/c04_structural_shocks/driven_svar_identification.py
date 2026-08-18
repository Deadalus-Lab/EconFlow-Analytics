# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``driven_svar_identification`` -- METHOD-SELECTION card #20.

#20 Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap

Category 04-structural-shocks; module ``driven_svar_identification``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "svar_cf",
    "svar_fevd",
    "svar_hd",
    "svar_id_chol",
    "svar_id_cv",
    "svar_id_dc",
    "svar_id_ngml",
    "svar_irf",
    "svar_mb_boot",
    "svar_wild_boot",
    "NODE_META",
    "wire_model",
]


def svar_id_chol(
    *,
    model: Any,
) -> dict[str, Any]:
    """Node ``svar_id_chol`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (recursive/Cholesky ID).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_id_chol: not implemented. The method card is in ./README.md."
    )


def svar_id_cv(
    *,
    model: Any,
    SB: int,
    max_iter: int | None = None,
    crit: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_cv`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (changes-in-volatility,
            Rigobon).
        SB: [integer, required] Structural break: number of pre-break observations (integer).
        max_iter: [integer, optional] Maximum EM iterations (default 50). Default ``50``.
        crit: [number, optional] Convergence criterion (default 0.001). Default ``0.001``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_id_cv: not implemented. The method card is in ./README.md."
    )


def svar_id_dc(
    *,
    model: Any,
    PIT: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_dc`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (distance-covariance ID).
        PIT: [boolean, optional] Probability integral transform of the residuals (default False).
            Default ``False``.
        seed: [integer, optional] Reproducibility seed (stochastic steadyICA, default 2025). Default
            ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_id_dc: not implemented. The method card is in ./README.md."
    )


def svar_id_ngml(
    *,
    model: Any,
    stage3: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_id_ngml`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        model: [raw_handle, required] Handle to a reduced-form 'varest' (non-Gaussian ML, Lanne et
            al.).
        stage3: [boolean, optional] Stage-3 GLS refinement (default False). Default ``False``.
        seed: [integer, optional] Reproducibility seed (default 2025). Default ``2025``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_id_ngml: not implemented. The method card is in ./README.md."
    )


def svar_irf(
    *,
    x: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_irf`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (from svar_id_*).
        n_ahead: [integer, optional] IRF horizon (positive integer, default 10). Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_irf: not implemented. The method card is in ./README.md."
    )


def svar_fevd(
    *,
    x: Any,
    n_ahead: int | None = None,
) -> dict[str, Any]:
    """Node ``svar_fevd`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (from svar_id_*).
        n_ahead: [integer, optional] FEVD horizon (positive integer, default 10). Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_fevd: not implemented. The method card is in ./README.md."
    )


def svar_hd(
    *,
    x: Any,
    series: int | None = None,
    transition: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_hd`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (historical decomposition).
        series: [integer, optional] Variable index 1..K (default 1). Default ``1``.
        transition: [number, optional] Transition-period share in [0,1) (default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_hd: not implemented. The method card is in ./README.md."
    )


def svar_cf(
    *,
    x: Any,
    series: int | None = None,
    transition: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_cf`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (counterfactual).
        series: [integer, optional] Variable index 1..K (default 1). Default ``1``.
        transition: [number, optional] Transition-period share in [0,1) (default 0). Default ``0``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_cf: not implemented. The method card is in ./README.md."
    )


def svar_wild_boot(
    *,
    x: Any,
    n_ahead: int | None = None,
    nboot: int | None = None,
    design: Literal["fixed", "recursive"] | None = None,
    distr: Literal["rademacher", "mammen", "gaussian"] | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_wild_boot`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (wild bootstrap,
            Gonçalves-Kilian).
        n_ahead: [integer, optional] IRF horizon (default 20). Default ``20``.
        nboot: [integer, optional] Number of bootstrap draws (default 500). Default ``500``.
        design: [enum, optional] Bootstrap design (default fixed).
        distr: [enum, optional] Distribution of the wild multiplier (default rademacher).
        lower_q: [number, optional] Lower quantile of the band (default 0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the band (default 0.84). Default ``0.84``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_wild_boot: not implemented. The method card is in ./README.md."
    )


def svar_mb_boot(
    *,
    x: Any,
    n_ahead: int | None = None,
    nboot: int | None = None,
    b_length: int | None = None,
    design: Literal["recursive", "fixed"] | None = None,
    lower_q: float | None = None,
    upper_q: float | None = None,
) -> dict[str, Any]:
    """Node ``svar_mb_boot`` -- METHOD-SELECTION card #20.

    Data-driven SVAR identification (Cholesky / changes-in-vol / distance-cov / non-Gaussian ML) +
    HD + counterfactual + wild/mb bootstrap.

    Category 04-structural-shocks; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to an identified 'svars' (moving-block bootstrap,
            Brüggemann et al.).
        n_ahead: [integer, optional] IRF horizon (default 20). Default ``20``.
        nboot: [integer, optional] Number of bootstrap draws (default 500). Default ``500``.
        b_length: [integer, optional] Block length (default 15). Default ``15``.
        design: [enum, optional] Bootstrap design (default recursive).
        lower_q: [number, optional] Lower quantile of the band (default 0.16). Default ``0.16``.
        upper_q: [number, optional] Upper quantile of the band (default 0.84). Default ``0.84``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "svar_mb_boot: not implemented. The method card is in ./README.md."
    )
