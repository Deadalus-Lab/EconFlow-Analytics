# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``spatial_weights_diagnostics`` -- METHOD-SELECTION card #54.

#54 Spatial weights / diagnostics

Category 09-cross-section-networks; module ``spatial_weights_diagnostics``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c09_cross_section_networks import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "spw_cell2nb",
    "spw_dnearneigh_nb",
    "spw_geary_test",
    "spw_joincount_test",
    "spw_knn_nb",
    "spw_listw",
    "spw_listw_constants",
    "spw_local_moran",
    "spw_moran_test",
    "spw_nb_diagnostics",
    "NODE_META",
    "wire_model",
]


def spw_knn_nb(
    *,
    coords: np.ndarray,
    k: int | None = None,
) -> dict[str, Any]:
    """Node ``spw_knn_nb`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``neighbours``, so a later node can consume it as a handle.

    Args:
        coords: [matrix_handle, required] Matrix of point coordinates (n x 2).
        k: [integer, optional] Number of nearest neighbours (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_knn_nb: not implemented. The method card is in ./README.md."
    )


def spw_dnearneigh_nb(
    *,
    coords: np.ndarray,
    d1: float,
    d2: float,
) -> dict[str, Any]:
    """Node ``spw_dnearneigh_nb`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``neighbours``, so a later node can consume it as a handle.

    Args:
        coords: [matrix_handle, required] Matrix of point coordinates (n x 2).
        d1: [number, required] Lower distance bound.
        d2: [number, required] Upper distance bound (d2 > d1).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_dnearneigh_nb: not implemented. The method card is in ./README.md."
    )


def spw_cell2nb(
    *,
    nrow: int,
    ncol: int,
    type: Literal["rook", "queen"] | None = None,
    torus: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_cell2nb`` -- METHOD-SELECTION card #54.

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
    """
    raise NotImplementedError(
        "spw_cell2nb: not implemented. The method card is in ./README.md."
    )


def spw_listw(
    *,
    neighbours: Any,
    style: Literal["W", "B", "C", "U", "minmax", "S"] | None = None,
) -> dict[str, Any]:
    """Node ``spw_listw`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Registers its result under ``listw``, so a later node can consume it as a handle.

    Args:
        neighbours: [raw_handle, required] 'nb' object (spw_*_nb $handle).
        style: [enum, optional] Coding scheme (default W = row-standardized).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_listw: not implemented. The method card is in ./README.md."
    )


def spw_nb_diagnostics(
    *,
    neighbours: Any,
) -> dict[str, Any]:
    """Node ``spw_nb_diagnostics`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        neighbours: [raw_handle, required] 'nb' object (spw_*_nb $handle).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_nb_diagnostics: not implemented. The method card is in ./README.md."
    )


def spw_listw_constants(
    *,
    listw: Any,
    adjust_n: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_listw_constants`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        listw: [raw_handle, required] 'listw' object (spw_listw $handle).
        adjust_n: [boolean, optional] Remove no-neighbour zones from n (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_listw_constants: not implemented. The method card is in ./README.md."
    )


def spw_moran_test(
    *,
    x: Any,
    listw: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    randomisation: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_moran_test`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the listw).
        listw: [raw_handle, required] 'listw' object (spw_listw $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        randomisation: [boolean, optional] Variance under randomisation (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_moran_test: not implemented. The method card is in ./README.md."
    )


def spw_geary_test(
    *,
    x: Any,
    listw: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    randomisation: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_geary_test`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the listw).
        listw: [raw_handle, required] 'listw' object (spw_listw $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        randomisation: [boolean, optional] Variance under randomisation (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_geary_test: not implemented. The method card is in ./README.md."
    )


def spw_local_moran(
    *,
    x: Any,
    listw: Any,
    alternative: Literal["two.sided", "greater", "less"] | None = None,
    conditional: bool | None = None,
) -> dict[str, Any]:
    """Node ``spw_local_moran`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        x: [raw_handle, required] Numeric vector (same length as the listw).
        listw: [raw_handle, required] 'listw' object (spw_listw $handle).
        alternative: [enum, optional] Alternative hypothesis (default two.sided).
        conditional: [boolean, optional] Conditional randomization null (Sokal) (default True).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_local_moran: not implemented. The method card is in ./README.md."
    )


def spw_joincount_test(
    *,
    fx: Any,
    listw: Any,
    alternative: Literal["greater", "less", "two.sided"] | None = None,
    sampling: Literal["nonfree", "free"] | None = None,
) -> dict[str, Any]:
    """Node ``spw_joincount_test`` -- METHOD-SELECTION card #54.

    Spatial weights / diagnostics.

    Category 09-cross-section-networks; memory class ``light``.

    Args:
        fx: [raw_handle, required] Factor (same length as the listw).
        listw: [raw_handle, required] 'listw' object (spw_listw $handle).
        alternative: [enum, optional] Alternative hypothesis (default greater).
        sampling: [enum, optional] Sampling assumption (default nonfree).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "spw_joincount_test: not implemented. The method card is in ./README.md."
    )
