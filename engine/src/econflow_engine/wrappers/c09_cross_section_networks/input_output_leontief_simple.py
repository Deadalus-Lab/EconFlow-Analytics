# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``input_output_leontief_simple`` -- method card #49.

#49 Input-Output / Leontief (simple)

Category 09-cross-section-networks; module ``input_output_leontief_simple``.

Reference implementation: 10.1017/CBO9780511626982.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "lt_augmented_input_requirement",
    "lt_backward_linkage",
    "lt_employment_multiplier",
    "lt_employment_number",
    "lt_equilibrium_output",
    "lt_forward_linkage",
    "lt_income_multiplier",
    "lt_input_requirement",
    "lt_leontief_inverse",
    "lt_multiplier_product_matrix",
    "lt_output_allocation",
    "lt_output_multiplier",
    "lt_power_dispersion",
    "lt_power_dispersion_cv",
    "lt_sensitivity_dispersion",
    "lt_sensitivity_dispersion_cv",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def lt_input_requirement(
    *,
    X: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_input_requirement`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        d: [raw_handle, required] Numeric vector of final demand (length the row count of X,
            non-zero).

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
        "lt_input_requirement: not implemented."
    )


def lt_augmented_input_requirement(
    *,
    X: np.ndarray,
    w: Any,
    c: Any,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_augmented_input_requirement`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        w: [raw_handle, required] Numeric vector of wages.
        c: [raw_handle, required] Numeric vector of household consumption.
        d: [raw_handle, required] Numeric vector of final demand (non-zero).

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
        "lt_augmented_input_requirement: not implemented."
    )


def lt_output_allocation(
    *,
    X: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_output_allocation`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        d: [raw_handle, required] Numeric vector of final demand (non-zero).

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
        "lt_output_allocation: not implemented."
    )


def lt_leontief_inverse(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_leontief_inverse`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Square matrix of direct coefficients A -> L = solve(I - A).

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
        "lt_leontief_inverse: not implemented."
    )


def lt_equilibrium_output(
    *,
    L: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_equilibrium_output`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        d: [raw_handle, required] Numeric vector of final demand.

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
        "lt_equilibrium_output: not implemented."
    )


def lt_output_multiplier(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_output_multiplier`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_output_multiplier: not implemented."
    )


def lt_income_multiplier(
    *,
    L: np.ndarray,
    w: Any,
) -> dict[str, Any]:
    """Node ``lt_income_multiplier`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        w: [raw_handle, required] Numeric vector of ALREADY-normalized wages (w/d).

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
        "lt_income_multiplier: not implemented."
    )


def lt_employment_multiplier(
    *,
    L: np.ndarray,
    e: Any,
) -> dict[str, Any]:
    """Node ``lt_employment_multiplier`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        e: [raw_handle, required] Numeric vector of ALREADY-normalized employment coefficients
            (e/d).

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
        "lt_employment_multiplier: not implemented."
    )


def lt_backward_linkage(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_backward_linkage`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Matrix of direct coefficients A (square).

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
        "lt_backward_linkage: not implemented."
    )


def lt_forward_linkage(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_forward_linkage`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Matrix of direct coefficients A (square).

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
        "lt_forward_linkage: not implemented."
    )


def lt_power_dispersion(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_power_dispersion`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_power_dispersion: not implemented."
    )


def lt_power_dispersion_cv(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_power_dispersion_cv`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_power_dispersion_cv: not implemented."
    )


def lt_sensitivity_dispersion(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_sensitivity_dispersion`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_sensitivity_dispersion: not implemented."
    )


def lt_sensitivity_dispersion_cv(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_sensitivity_dispersion_cv`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_sensitivity_dispersion_cv: not implemented."
    )


def lt_multiplier_product_matrix(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_multiplier_product_matrix`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

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
        "lt_multiplier_product_matrix: not implemented."
    )


def lt_employment_number(
    *,
    L: np.ndarray,
    e: Any,
    c: Any,
) -> dict[str, Any]:
    """Node ``lt_employment_number`` -- method card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        e: [raw_handle, required] Numeric vector of employment coefficients.
        c: [raw_handle, required] Numeric vector of the change in final demand.

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
        "lt_employment_number: not implemented."
    )
