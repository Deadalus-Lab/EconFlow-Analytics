# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``small_area_estimation`` -- METHOD-SELECTION card #233.

#233 Small-area estimation (SAE): the Fay-Herriot area-level EBLUP (+ the analytic Prasad-Rao MSE) &
    the Battese-Harter-Fuller unit-level EBLUP

Category 25-expectations-surveys; module ``small_area_estimation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sae_eblup_bhf",
    "sae_eblup_fh",
    "sae_mse_fh",
    "NODE_META",
    "wire_model",
]


def sae_eblup_fh(
    *,
    data: pd.DataFrame,
    formula: str,
    vardir: str,
    method: Literal["REML", "ML", "FH"] | None = None,
    MAXITER: int | None = None,
    PRECISION: float | None = None,
    B: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sae_eblup_fh`` -- METHOD-SELECTION card #233.

    Small-area estimation (SAE): the Fay-Herriot area-level EBLUP (+ the analytic Prasad-Rao MSE) &
    the Battese-Harter-Fuller unit-level EBLUP.

    Category 25-expectations-surveys; memory class ``heavy``.

    Args:
        data: [df_handle, required] Handle to an area-level DataFrame: ONE row per area/domain with
            the DIRECT estimates (response), the auxiliary variables, and the vardir column. >= 2
            areas.
        formula: [formula, required] response ~ auxiliaries; the response is the direct estimates
            theta-hat_i per area (e.g. "yi ~ x1 + a categorical of (region)").
        vardir: [string, required] NAME of the data column with the sampling VARIANCES psi_i
            (variances = SD^2, NOT SD); known & >= 0 for each area.
        method: [enum, optional] Estimation method of the variance component (default REML; ML;
            FH=Fay-Herriot).
        MAXITER: [integer, optional] Maximum Fisher-scoring iterations (default 100). Default
            ``100``.
        PRECISION: [number, optional] Convergence tolerance (default 1e-4). Default ``0.0001``.
        B: [integer, optional] Bootstrap replicates for the Marhuenda goodness-of-fit (default 0 =
            no bootstrap; >0 = stochastic, seeded). Default ``0``.
        seed: [integer, optional] Seed before the bootstrap when B>0 (determinism; default 1).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sae_eblup_fh: not implemented. The method card is in ./README.md."
    )


def sae_mse_fh(
    *,
    data: pd.DataFrame,
    formula: str,
    vardir: str,
    method: Literal["REML", "ML", "FH"] | None = None,
    MAXITER: int | None = None,
    PRECISION: float | None = None,
    B: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sae_mse_fh`` -- METHOD-SELECTION card #233.

    Small-area estimation (SAE): the Fay-Herriot area-level EBLUP (+ the analytic Prasad-Rao MSE) &
    the Battese-Harter-Fuller unit-level EBLUP.

    Category 25-expectations-surveys; memory class ``heavy``.

    Args:
        data: [df_handle, required] Handle to an area-level DataFrame: ONE row per area/domain with
            the DIRECT estimates (response), the auxiliary variables, and the vardir column. >= 2
            areas.
        formula: [formula, required] response ~ auxiliaries; the response is the direct estimates
            theta-hat_i per area (e.g. "yi ~ x1 + a categorical of (region)").
        vardir: [string, required] NAME of the data column with the sampling VARIANCES psi_i
            (variances = SD^2, NOT SD); known & >= 0 for each area.
        method: [enum, optional] Estimation method of the variance component (default REML; ML;
            FH=Fay-Herriot).
        MAXITER: [integer, optional] Maximum Fisher-scoring iterations (default 100). Default
            ``100``.
        PRECISION: [number, optional] Convergence tolerance (default 1e-4). Default ``0.0001``.
        B: [integer, optional] Bootstrap replicates for the Marhuenda goodness-of-fit (default 0 =
            no bootstrap; >0 = stochastic, seeded). Default ``0``.
        seed: [integer, optional] Seed before the bootstrap when B>0 (determinism; default 1).
            Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sae_mse_fh: not implemented. The method card is in ./README.md."
    )


def sae_eblup_bhf(
    *,
    data: pd.DataFrame,
    formula: str,
    dom: str,
    meanxpop: pd.DataFrame,
    popnsize: pd.DataFrame,
    selectdom: Any | None = None,
    method: Literal["REML", "ML"] | None = None,
) -> dict[str, Any]:
    """Node ``sae_eblup_bhf`` -- METHOD-SELECTION card #233.

    Small-area estimation (SAE): the Fay-Herriot area-level EBLUP (+ the analytic Prasad-Rao MSE) &
    the Battese-Harter-Fuller unit-level EBLUP.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a unit-level DataFrame: ONE row per UNIT (sample) with
            response, auxiliary variables, and the domain column (dom).
        formula: [formula, required] response ~ auxiliaries (unit-level nested-error regression,
            e.g. "y ~ x1 + x2").
        dom: [string, required] NAME of the data column with the area codes (domain codes).
        meanxpop: [df_handle, required] Handle to a DataFrame D×(p+1): 1st column = domain codes;
            the rest = population means of the p auxiliaries per area (p == number of auxiliaries in
            the formula).
        popnsize: [df_handle, required] Handle to a DataFrame D×2: domain codes + population sizes
            (positive).
        selectdom: [raw, optional] (optional) vector of domain codes to estimate (subset of the
            sample's codes); default = all.
        method: [enum, optional] Estimation method of the variance components (default REML; ML).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sae_eblup_bhf: not implemented. The method card is in ./README.md."
    )
