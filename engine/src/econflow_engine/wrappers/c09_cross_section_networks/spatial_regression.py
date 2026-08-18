# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_regression`` -- METHOD-SELECTION card #53.

#53 Spatial regression (lag/error)

Category 09-cross-section-networks; module ``spatial_regression``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "spr_bptest",
    "spr_fit_error",
    "spr_fit_lag",
    "spr_fit_sac",
    "spr_hausman_test",
    "spr_impacts",
    "spr_lr_test",
    "spr_summary",
    "NODE_META",
    "wire_model",
]


def spr_fit_lag(
    *,
    formula: str,
    data: pd.DataFrame,
    listw: Any,
    Durbin: bool | None = None,
    method: (
        Literal[
            "eigen",
            "spam",
            "Matrix_J",
            "Matrix",
            "spam_update",
            "LU",
            "Chebyshev",
            "MC",
            "SE_classic",
            "SE_whichMin",
            "SE_interp",
        ]
        | None
    ) = None,
    zero_policy: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_fit_lag`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial lag (SAR) model formula, e.g. 'y ~ x1 + x2'.
        data: [df_handle, required] DataFrame with the variables (same order as the listw).
        listw: [raw_handle, required] 'listw' spatial weights (spw_listw $handle).
        Durbin: [boolean, optional] True -> Durbin (SDM) lagged X terms (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_fit_lag: not implemented. The method card is in ./README.md."
    )


def spr_fit_error(
    *,
    formula: str,
    data: pd.DataFrame,
    listw: Any,
    Durbin: bool | None = None,
    method: (
        Literal[
            "eigen",
            "spam",
            "Matrix_J",
            "Matrix",
            "spam_update",
            "LU",
            "Chebyshev",
            "MC",
            "SE_classic",
            "SE_whichMin",
            "SE_interp",
        ]
        | None
    ) = None,
    zero_policy: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_fit_error`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial error (SEM) model formula.
        data: [df_handle, required] DataFrame with the variables.
        listw: [raw_handle, required] 'listw' spatial weights (spw_listw $handle).
        Durbin: [boolean, optional] True -> spatial Durbin error (SDEM) (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_fit_error: not implemented. The method card is in ./README.md."
    )


def spr_fit_sac(
    *,
    formula: str,
    data: pd.DataFrame,
    listw: Any,
    listw2: Any | None = None,
    Durbin: bool | None = None,
    method: (
        Literal[
            "eigen",
            "spam",
            "Matrix_J",
            "Matrix",
            "spam_update",
            "LU",
            "Chebyshev",
            "MC",
            "SE_classic",
            "SE_whichMin",
            "SE_interp",
        ]
        | None
    ) = None,
    zero_policy: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_fit_sac`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] SAC/SARAR (lag + error) model formula.
        data: [df_handle, required] DataFrame with the variables.
        listw: [raw_handle, required] 'listw' spatial weights (spw_listw $handle).
        listw2: [raw_handle, optional] 2nd 'listw' (default same as listw).
        Durbin: [boolean, optional] True -> Durbin terms (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_fit_sac: not implemented. The method card is in ./README.md."
    )


def spr_impacts(
    *,
    obj: Any,
    listw: Any | None = None,
    n_simulations: int | None = None,
) -> dict[str, Any]:
    """Node ``spr_impacts`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``heavy``.

    Args:
        obj: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        listw: [raw_handle, optional] 'listw' spatial weights (required if tr is not given).
        n_simulations: [integer, optional] Number of simulations (mvrnorm) for
            distributions/z-stats.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_impacts: not implemented. The method card is in ./README.md."
    )


def spr_summary(
    *,
    object: Any,
    correlation: bool | None = None,
    Nagelkerke: bool | None = None,
    Hausman: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_summary`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        correlation: [boolean, optional] Parameter correlation matrix (default False).
        Nagelkerke: [boolean, optional] Nagelkerke pseudo R^2 (default False).
        Hausman: [boolean, optional] Spatial Hausman test (error models only) (default False).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_summary: not implemented. The method card is in ./README.md."
    )


def spr_lr_test(
    *,
    x: Any,
    y: Any,
) -> dict[str, Any]:
    """Node ``spr_lr_test`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] 'Sarlm'/'logLik' object (model 1).
        y: [raw_handle, required] 'Sarlm'/'logLik' object (nested model 2).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_lr_test: not implemented. The method card is in ./README.md."
    )


def spr_hausman_test(
    *,
    object: Any,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``spr_hausman_test`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' error object (spr_fit_error $handle).
        tol: [number, optional] Tolerance for solve (default None).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_hausman_test: not implemented. The method card is in ./README.md."
    )


def spr_bptest(
    *,
    object: Any,
    studentize: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_bptest`` -- METHOD-SELECTION card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        studentize: [boolean, optional] Studentized (Koenker) version (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spr_bptest: not implemented. The method card is in ./README.md."
    )
