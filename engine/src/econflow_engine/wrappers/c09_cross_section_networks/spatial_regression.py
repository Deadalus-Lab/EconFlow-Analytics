# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_regression`` -- method card #53.

#53 Spatial regression (lag/error)

Category 09-cross-section-networks; module ``spatial_regression``.

Reference implementation: spreg.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
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

# --- gen_wrappers: header end ---


def spr_fit_lag(
    *,
    formula: str,
    data: pd.DataFrame,
    spatial_weights: Any,
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
    """Node ``spr_fit_lag`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial lag (SAR) model formula, e.g. 'y ~ x1 + x2'.
        data: [df_handle, required] DataFrame with the variables (same order as the spatial
            weights).
        spatial_weights: [raw_handle, required] spatial-weights object spatial weights (spw_weights
            $handle).
        Durbin: [boolean, optional] True -> Durbin (SDM) lagged X terms (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

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
        "spr_fit_lag: not implemented."
    )


def spr_fit_error(
    *,
    formula: str,
    data: pd.DataFrame,
    spatial_weights: Any,
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
    """Node ``spr_fit_error`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Spatial error (SEM) model formula.
        data: [df_handle, required] DataFrame with the variables.
        spatial_weights: [raw_handle, required] spatial-weights object spatial weights (spw_weights
            $handle).
        Durbin: [boolean, optional] True -> spatial Durbin error (SDEM) (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

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
        "spr_fit_error: not implemented."
    )


def spr_fit_sac(
    *,
    formula: str,
    data: pd.DataFrame,
    spatial_weights: Any,
    spatial_weights2: Any | None = None,
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
    """Node ``spr_fit_sac`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] SAC/SARAR (lag + error) model formula.
        data: [df_handle, required] DataFrame with the variables.
        spatial_weights: [raw_handle, required] spatial-weights object spatial weights (spw_weights
            $handle).
        spatial_weights2: [raw_handle, optional] 2nd spatial-weights object (default same as spatial
            weights).
        Durbin: [boolean, optional] True -> Durbin terms (default False).
        method: [enum, optional] Log-determinant method (default eigen).
        zero_policy: [boolean, optional] Allow zones with no neighbours (default False).

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
        "spr_fit_sac: not implemented."
    )


def spr_impacts(
    *,
    obj: Any,
    spatial_weights: Any | None = None,
    n_simulations: int | None = None,
) -> dict[str, Any]:
    """Node ``spr_impacts`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``heavy``.

    Args:
        obj: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        spatial_weights: [raw_handle, optional] spatial-weights object spatial weights (required if
            tr is not given).
        n_simulations: [integer, optional] Number of simulations (mvrnorm) for
            distributions/z-stats.

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
        "spr_impacts: not implemented."
    )


def spr_summary(
    *,
    object: Any,
    correlation: bool | None = None,
    Nagelkerke: bool | None = None,
    Hausman: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_summary`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        correlation: [boolean, optional] Parameter correlation matrix (default False).
        Nagelkerke: [boolean, optional] Nagelkerke pseudo R^2 (default False).
        Hausman: [boolean, optional] Spatial Hausman test (error models only) (default False).

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
        "spr_summary: not implemented."
    )


def spr_lr_test(
    *,
    x: Any,
    y: Any,
) -> dict[str, Any]:
    """Node ``spr_lr_test`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] 'Sarlm'/'logLik' object (model 1).
        y: [raw_handle, required] 'Sarlm'/'logLik' object (nested model 2).

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
        "spr_lr_test: not implemented."
    )


def spr_hausman_test(
    *,
    object: Any,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``spr_hausman_test`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' error object (spr_fit_error $handle).
        tol: [number, optional] Tolerance for solve (default None).

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
        "spr_hausman_test: not implemented."
    )


def spr_bptest(
    *,
    object: Any,
    studentize: bool | None = None,
) -> dict[str, Any]:
    """Node ``spr_bptest`` -- method card #53.

    Spatial regression (lag/error).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        object: [raw_handle, required] 'Sarlm' object (spr_fit_* $handle).
        studentize: [boolean, optional] Studentized (Koenker) version (default True).

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
        "spr_bptest: not implemented."
    )
