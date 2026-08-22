# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``kernel_density`` -- method card #285.

#285 Multivariate and conditional kernel density estimation

Category 33-nonparametric-semiparametric; module ``kernel_density``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c33_nonparametric_semiparametric import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "np_conditional_kde",
    "np_ecdf_grid",
    "np_kde",
    "NODE_META",
    "wire_model",
]


def np_kde(
    *,
    x: pd.DataFrame,
    var_type: str | None = None,
    bandwidth: Sequence[float] | None = None,
    grid_size: int | None = None,
) -> dict[str, Any]:
    """Node ``np_kde`` -- method card #285.

    Multivariate and conditional kernel density estimation.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        x: [multiseries_handle, required] Data, one column per dimension.
        var_type: [string, optional] One character per dimension: c, o or u.
        bandwidth: [num_array, optional] Bandwidth per dimension; omitted = data-driven.
        grid_size: [integer, optional] Points per dimension in the evaluation grid. Default ``50``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_kde: not implemented."
    )


def np_conditional_kde(
    *,
    y: pd.DataFrame,
    x: pd.DataFrame,
    var_type_y: str | None = None,
    var_type_x: str | None = None,
    grid_size: int | None = None,
) -> dict[str, Any]:
    """Node ``np_conditional_kde`` -- method card #285.

    Multivariate and conditional kernel density estimation.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Dependent variables.
        x: [multiseries_handle, required] Conditioning variables.
        var_type_y: [string, optional] Kind characters for y.
        var_type_x: [string, optional] Kind characters for x.
        grid_size: [integer, optional] Points per dimension in the evaluation grid. Default ``50``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_conditional_kde: not implemented."
    )


def np_ecdf_grid(
    *,
    x: pd.Series,
    grid: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``np_ecdf_grid`` -- method card #285.

    Multivariate and conditional kernel density estimation.

    Category 33-nonparametric-semiparametric; memory class ``light``.

    Args:
        x: [series_handle, required] Data.
        grid: [num_array, optional] Evaluation points; omitted = the sorted data.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "np_ecdf_grid: not implemented."
    )
