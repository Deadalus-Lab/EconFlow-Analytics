# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``input_output_leontief_2`` -- METHOD-SELECTION card #49.

#49 Input-Output / Leontief (simple)

Category 09-cross-section-networks; module ``input_output_leontief_2``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

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


def lt_input_requirement(
    *,
    X: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_input_requirement`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        d: [raw_handle, required] Numeric vector of final demand (length the row count of X,
            non-zero).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_input_requirement: not implemented. The method card is in ./README.md."
    )


def lt_augmented_input_requirement(
    *,
    X: np.ndarray,
    w: Any,
    c: Any,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_augmented_input_requirement`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        w: [raw_handle, required] Numeric vector of wages.
        c: [raw_handle, required] Numeric vector of household consumption.
        d: [raw_handle, required] Numeric vector of final demand (non-zero).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_augmented_input_requirement: not implemented. The method card is in ./README.md."
    )


def lt_output_allocation(
    *,
    X: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_output_allocation`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        X: [matrix_handle, required] Square transaction matrix.
        d: [raw_handle, required] Numeric vector of final demand (non-zero).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_output_allocation: not implemented. The method card is in ./README.md."
    )


def lt_leontief_inverse(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_leontief_inverse`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Square matrix of direct coefficients A -> L = solve(I - A).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_leontief_inverse: not implemented. The method card is in ./README.md."
    )


def lt_equilibrium_output(
    *,
    L: np.ndarray,
    d: Any,
) -> dict[str, Any]:
    """Node ``lt_equilibrium_output`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        d: [raw_handle, required] Numeric vector of final demand.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_equilibrium_output: not implemented. The method card is in ./README.md."
    )


def lt_output_multiplier(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_output_multiplier`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_output_multiplier: not implemented. The method card is in ./README.md."
    )


def lt_income_multiplier(
    *,
    L: np.ndarray,
    w: Any,
) -> dict[str, Any]:
    """Node ``lt_income_multiplier`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        w: [raw_handle, required] Numeric vector of ALREADY-normalized wages (w/d).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_income_multiplier: not implemented. The method card is in ./README.md."
    )


def lt_employment_multiplier(
    *,
    L: np.ndarray,
    e: Any,
) -> dict[str, Any]:
    """Node ``lt_employment_multiplier`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        e: [raw_handle, required] Numeric vector of ALREADY-normalized employment coefficients
            (e/d).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_employment_multiplier: not implemented. The method card is in ./README.md."
    )


def lt_backward_linkage(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_backward_linkage`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Matrix of direct coefficients A (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_backward_linkage: not implemented. The method card is in ./README.md."
    )


def lt_forward_linkage(
    *,
    A: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_forward_linkage`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        A: [matrix_handle, required] Matrix of direct coefficients A (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_forward_linkage: not implemented. The method card is in ./README.md."
    )


def lt_power_dispersion(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_power_dispersion`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_power_dispersion: not implemented. The method card is in ./README.md."
    )


def lt_power_dispersion_cv(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_power_dispersion_cv`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_power_dispersion_cv: not implemented. The method card is in ./README.md."
    )


def lt_sensitivity_dispersion(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_sensitivity_dispersion`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_sensitivity_dispersion: not implemented. The method card is in ./README.md."
    )


def lt_sensitivity_dispersion_cv(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_sensitivity_dispersion_cv`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_sensitivity_dispersion_cv: not implemented. The method card is in ./README.md."
    )


def lt_multiplier_product_matrix(
    *,
    L: np.ndarray,
) -> dict[str, Any]:
    """Node ``lt_multiplier_product_matrix`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_multiplier_product_matrix: not implemented. The method card is in ./README.md."
    )


def lt_employment_number(
    *,
    L: np.ndarray,
    e: Any,
    c: Any,
) -> dict[str, Any]:
    """Node ``lt_employment_number`` -- METHOD-SELECTION card #49.

    Input-Output / Leontief (simple).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        L: [matrix_handle, required] Leontief inverse (square).
        e: [raw_handle, required] Numeric vector of employment coefficients.
        c: [raw_handle, required] Numeric vector of the change in final demand.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lt_employment_number: not implemented. The method card is in ./README.md."
    )
