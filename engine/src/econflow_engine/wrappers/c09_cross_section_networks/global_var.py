# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``global_var`` -- method card #50.

#50 Global VAR (GVAR)

Category 09-cross-section-networks; module ``global_var``.

Reference implementation: 10.1198/073500104000000019.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gv_coef",
    "gv_coef_exo",
    "gv_coef_exo_nw",
    "gv_coef_exo_white",
    "gv_coef_nw",
    "gv_coef_white",
    "gv_fit",
    "gv_foreign_variables",
    "gv_residual_correlation",
    "gv_structural",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gv_fit(
    *,
    data: pd.DataFrame,
    weight_matrix: np.ndarray,
    p: int | None = None,
    type: Literal["const", "none", "trend", "both"] | None = None,
    ic: Literal["AIC", "HQ", "SC", "FPE"],
) -> dict[str, Any]:
    """Node ``gv_fit`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Balanced panel DataFrame (ID/Time columns + >=2 variables).
        weight_matrix: [matrix_handle, required] Bilateral trade weight matrix N x N.
        p: [integer, optional] Lag for Xt (1<=p<=2, default 2). Default ``2``.
        type: [enum, optional] Deterministic term (default const).
        ic: [enum, required] Information criterion for country-specific VARselect.

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
        "gv_fit: not implemented."
    )


def gv_foreign_variables(
    *,
    data: pd.DataFrame,
    weight_matrix: np.ndarray,
) -> dict[str, Any]:
    """Node ``gv_foreign_variables`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        data: [df_handle, required] Balanced panel DataFrame.
        weight_matrix: [matrix_handle, required] Bilateral trade weight matrix N x N.

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
        "gv_foreign_variables: not implemented."
    )


def gv_structural(
    *,
    data: pd.DataFrame,
    weight_matrix: np.ndarray,
    p: int | None = None,
    type: Literal["const", "none", "trend", "both"] | None = None,
    ic: Literal["AIC", "HQ", "SC", "FPE"] | None = None,
) -> dict[str, Any]:
    """Node ``gv_structural`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        data: [df_handle, required] Balanced panel DataFrame.
        weight_matrix: [matrix_handle, required] Bilateral trade weight matrix N x N.
        p: [integer, optional] Lag for Xt (default 2). Default ``2``.
        type: [enum, optional] Deterministic term (default const).
        ic: [enum, optional] Information criterion (default AIC).

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
        "gv_structural: not implemented."
    )


def gv_residual_correlation(
    *,
    out: Any,
) -> dict[str, Any]:
    """Node ``gv_residual_correlation`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).

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
        "gv_residual_correlation: not implemented."
    )


def gv_coef(
    *,
    out: Any,
    sheet: int,
) -> dict[str, Any]:
    """Node ``gv_coef`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).
        sheet: [integer, required] Country number (1..N).

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
        "gv_coef: not implemented."
    )


def gv_coef_nw(
    *,
    out: Any,
    sheet: int,
) -> dict[str, Any]:
    """Node ``gv_coef_nw`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).
        sheet: [integer, required] Country number (1..N).

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
        "gv_coef_nw: not implemented."
    )


def gv_coef_white(
    *,
    out: Any,
    sheet: int,
) -> dict[str, Any]:
    """Node ``gv_coef_white`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).
        sheet: [integer, required] Country number (1..N).

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
        "gv_coef_white: not implemented."
    )


def gv_coef_exo(
    *,
    out: Any,
) -> dict[str, Any]:
    """Node ``gv_coef_exo`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).

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
        "gv_coef_exo: not implemented."
    )


def gv_coef_exo_nw(
    *,
    out: Any,
) -> dict[str, Any]:
    """Node ``gv_coef_exo_nw`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).

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
        "gv_coef_exo_nw: not implemented."
    )


def gv_coef_exo_white(
    *,
    out: Any,
) -> dict[str, Any]:
    """Node ``gv_coef_exo_white`` -- method card #50.

    Global VAR (GVAR).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        out: [raw_handle, required] GVARest object (gv_fit $handle).

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
        "gv_coef_exo_white: not implemented."
    )
