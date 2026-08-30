# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_weights_diagnostics`` -- method card #54.

#54 Spatial weights / diagnostics

Category 09-cross-section-networks; module ``spatial_weights_diagnostics``.

Reference implementation: libpysal.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "spw_distance_neighbours",
    "spw_geary_test",
    "spw_grid_neighbours",
    "spw_joincount_test",
    "spw_knn_neighbours",
    "spw_local_moran",
    "spw_moran_test",
    "spw_neighbour_diagnostics",
    "spw_weight_constants",
    "spw_weights",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def spw_knn_neighbours(
    *,
    coords: np.ndarray,
    k: int | None = None,
) -> dict[str, Any]:
    """Node ``spw_knn_neighbours`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``neighbours``, so a later node can consume it as a handle.

    Args:
        coords: [matrix_handle, required] Matrix of point coordinates (n x 2).
        k: [integer, optional] Number of nearest neighbours (default 1). Default ``1``.

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
        "spw_knn_neighbours: not implemented."
    )


def spw_distance_neighbours(
    *,
    coords: np.ndarray,
    d1: float,
    d2: float,
) -> dict[str, Any]:
    """Node ``spw_distance_neighbours`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``neighbours``, so a later node can consume it as a handle.

    Args:
        coords: [matrix_handle, required] Matrix of point coordinates (n x 2).
        d1: [number, required] Lower distance bound.
        d2: [number, required] Upper distance bound (d2 > d1).

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
        "spw_distance_neighbours: not implemented."
    )


def spw_grid_neighbours(
    *,
    nrow: int,
    ncol: int,
    type: Literal["rook", "queen"] | None = None,
    torus: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_grid_neighbours`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``neighbours``, so a later node can consume it as a handle.

    Args:
        nrow: [integer, required] Number of grid rows.
        ncol: [integer, required] Number of grid columns.
        type: [enum, optional] Grid contiguity (default rook).
        torus: [boolean, optional] Grid on a torus (removes edge effects) (default False).

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
        "spw_grid_neighbours: not implemented."
    )


def spw_weights(
    *,
    neighbours: Any,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
) -> dict[str, Any]:
    """Node ``spw_weights`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``spatial_weights``, so a later node can consume it as a handle.

    Args:
        neighbours: [raw_handle, required] 'nb' object (spw_*_nb $handle).
        style: [enum, optional] Coding scheme (default W = row-standardized).

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
        "spw_weights: not implemented."
    )


def spw_neighbour_diagnostics(
    *,
    neighbours: Any,
) -> dict[str, Any]:
    """Node ``spw_neighbour_diagnostics`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        neighbours: [raw_handle, required] 'nb' object (spw_*_nb $handle).

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
        "spw_neighbour_diagnostics: not implemented."
    )


def spw_weight_constants(
    *,
    spatial_weights: Any,
    adjust_n: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_weight_constants`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        spatial_weights: [raw_handle, required] spatial-weights object object (spw_weights $handle).
        adjust_n: [boolean, optional] Remove no-neighbour zones from n (default True).

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
        "spw_weight_constants: not implemented."
    )


def spw_moran_test(
    *,
    x: Any,
    spatial_weights: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    randomisation: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_moran_test`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the spatial weights).
        spatial_weights: [raw_handle, required] spatial-weights object object (spw_weights $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        randomisation: [boolean, optional] Variance under randomisation (default True).

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
        "spw_moran_test: not implemented."
    )


def spw_geary_test(
    *,
    x: Any,
    spatial_weights: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    randomisation: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_geary_test`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the spatial weights).
        spatial_weights: [raw_handle, required] spatial-weights object object (spw_weights $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        randomisation: [boolean, optional] Variance under randomisation (default True).

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
        "spw_geary_test: not implemented."
    )


def spw_local_moran(
    *,
    x: Any,
    spatial_weights: Any,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    conditional: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_local_moran`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the spatial weights).
        spatial_weights: [raw_handle, required] spatial-weights object object (spw_weights $handle).
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        conditional: [boolean, optional] Conditional randomization null (Sokal) (default True).

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
        "spw_local_moran: not implemented."
    )


def spw_joincount_test(
    *,
    fx: Any,
    spatial_weights: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    sampling: Literal["nonfree", "free"] | None = None,
) -> dict[str, Any]:
    """Node ``spw_joincount_test`` -- method card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        fx: [raw_handle, required] Factor (same length as the spatial weights).
        spatial_weights: [raw_handle, required] spatial-weights object object (spw_weights $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        sampling: [enum, optional] Sampling assumption (default nonfree).

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
        "spw_joincount_test: not implemented."
    )
