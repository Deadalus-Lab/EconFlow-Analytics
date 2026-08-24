# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``density_grids`` -- method card #386.

#386 Kernel density and empirical distribution grids

Category 00-data-utilities; module ``density_grids``.

Reference implementation: KDEpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_density_grid",
    "du_ecdf",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_density_grid(
    *,
    x: pd.Series,
    bandwidth: float | None = None,
    kernel: (
        Literal[
            "gaussian",
            "epanechnikov",
            "tophat",
            "exponential",
            "biweight",
            "triweight",
        ]
        | None
    ) = None,
    grid_size: int | None = None,
    bounded: Literal["none", "reflect", "log_transform"] | None = None,
) -> dict[str, Any]:
    """Node ``du_density_grid`` -- method card #386.

    Kernel density and empirical distribution grids.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Data.
        bandwidth: [number, optional] Bandwidth; omitted = plug-in rule.
        kernel: [enum, optional] Kernel function. Default ``'gaussian'``.
        grid_size: [integer, optional] Number of grid points. Default ``512``.
        bounded: [enum, optional] Boundary correction. Default ``'none'``.

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
        "du_density_grid: not implemented."
    )


def du_ecdf(
    *,
    x: pd.Series,
    weights: pd.Series | None = None,
    grid: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``du_ecdf`` -- method card #386.

    Kernel density and empirical distribution grids.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [series_handle, required] Data.
        weights: [series_handle, optional] Observation weights.
        grid: [num_array, optional] Evaluation points; omitted = the sorted data.

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
        "du_ecdf: not implemented."
    )
