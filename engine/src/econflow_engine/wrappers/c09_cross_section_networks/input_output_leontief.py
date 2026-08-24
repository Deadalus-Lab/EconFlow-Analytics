# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``input_output_leontief`` -- method card #48.

#48 Input-Output / Leontief analysis (full)

Category 09-cross-section-networks; module ``input_output_leontief``.

Reference implementation: 10.1017/CBO9780511626982.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "io_build",
    "io_extraction",
    "io_field_of_influence",
    "io_field_of_influence_total",
    "io_ghosh_inverse",
    "io_key_sector",
    "io_leontief_inverse",
    "io_linkages",
    "io_multipliers",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def io_build(
    *,
    Z: np.ndarray,
    RS_label: np.ndarray,
    X: np.ndarray,
    f: np.ndarray | None = None,
    f_label: np.ndarray | None = None,
    V: np.ndarray | None = None,
    V_label: np.ndarray | None = None,
) -> dict[str, Any]:
    """Node ``io_build`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        Z: [matrix_handle, required] Square matrix of intersectoral transactions (transaction
            matrix).
        RS_label: [matrix_handle, required] 2-column matrix of region/sector labels (nrow == the row
            count of Z).
        X: [matrix_handle, required] Total output, ncol=1: X = rowSums(Z)+f.
        f: [matrix_handle, optional] Final demand, ncol=1 (optional).
        f_label: [matrix_handle, optional] Labels of the final demand (optional).
        V: [matrix_handle, optional] Value-added rows (required for io_extraction).
        V_label: [matrix_handle, optional] Labels of the value-added (optional).

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
        "io_build: not implemented."
    )


def io_leontief_inverse(
    *,
    Z: Any,
) -> dict[str, Any]:
    """Node ``io_leontief_inverse`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        Z: [raw_handle, required] InputOutput object (io_build $handle) -> returns the Leontief
            inverse L.

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
        "io_leontief_inverse: not implemented."
    )


def io_ghosh_inverse(
    *,
    Z: Any,
) -> dict[str, Any]:
    """Node ``io_ghosh_inverse`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        Z: [raw_handle, required] InputOutput object (io_build $handle) -> Ghoshian (supply) inverse
            G.

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
        "io_ghosh_inverse: not implemented."
    )


def io_multipliers(
    *,
    io: Any,
    multipliers: Sequence[str],
) -> dict[str, Any]:
    """Node ``io_multipliers`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle).
        multipliers: [series_codes, required] Combination of: output, input, wage,
            employment.closed, employment.physical.

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
        "io_multipliers: not implemented."
    )


def io_linkages(
    *,
    io: Any,
    type: Sequence[str] | None = None,
    normalize: bool | None = None,
) -> dict[str, Any]:
    """Node ``io_linkages`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle).
        type: [series_codes, optional] Combination of 'total'/'direct' (default total).
        normalize: [boolean, optional] Normalized Rasmussen-Hirschman linkages (default False).

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
        "io_linkages: not implemented."
    )


def io_key_sector(
    *,
    io: Any,
    crit: float | None = None,
    type: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``io_key_sector`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle).
        crit: [number, optional] Critical value for key-sector classification (default 1). Default
            ``1``.
        type: [series_codes, optional] Combination of 'total'/'direct' (default direct).

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
        "io_key_sector: not implemented."
    )


def io_field_of_influence(
    *,
    io: Any,
    i: int,
    j: int,
) -> dict[str, Any]:
    """Node ``io_field_of_influence`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle).
        i: [integer, required] Row of the coefficient of interest (1..n).
        j: [integer, required] Column of the coefficient of interest (1..n).

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
        "io_field_of_influence: not implemented."
    )


def io_field_of_influence_total(
    *,
    io: Any,
) -> dict[str, Any]:
    """Node ``io_field_of_influence_total`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle).

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
        "io_field_of_influence_total: not implemented."
    )


def io_extraction(
    *,
    io: Any,
    type: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``io_extraction`` -- method card #48.

    Input-Output / Leontief analysis (full).

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        io: [raw_handle, required] InputOutput object (io_build $handle) -- requires V.
        type: [series_codes, optional] Combination of backward/forward/backward.total/forward.total
            (default backward.total).

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
        "io_extraction: not implemented."
    )
