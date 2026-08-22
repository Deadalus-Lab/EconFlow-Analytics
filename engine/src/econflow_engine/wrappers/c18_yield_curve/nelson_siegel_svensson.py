# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nelson_siegel_svensson`` -- method card #87.

#87 Nelson-Siegel / Svensson / Diebold-Li yield-curve factors

Category 18-yield-curve; module ``nelson_siegel_svensson``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c18_yield_curve import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fit_nelson_siegel",
    "fit_svensson",
    "NODE_META",
    "wire_model",
]


def fit_nelson_siegel(
    *,
    rates: np.ndarray,
    maturities: np.ndarray,
) -> dict[str, Any]:
    """Node ``fit_nelson_siegel`` -- method card #87.

    Nelson-Siegel / Svensson / Diebold-Li yield-curve factors.

    Category 18-yield-curve; memory class ``light``.

    Args:
        rates: [matrix_handle, required] Handle to a yield matrix [n_obs x n_maturities] (rows =
            dates, columns = maturities).
        maturities: [matrix_handle, required] Handle to a strictly increasing numeric vector of
            maturities (>= 4 pillars; same count as the columns of rates).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fit_nelson_siegel: not implemented."
    )


def fit_svensson(
    *,
    rates: np.ndarray,
    maturities: np.ndarray,
    which_rate: Literal["Spot", "Forward"] | None = None,
) -> dict[str, Any]:
    """Node ``fit_svensson`` -- method card #87.

    Nelson-Siegel / Svensson / Diebold-Li yield-curve factors.

    Category 18-yield-curve; memory class ``light``.

    Args:
        rates: [matrix_handle, required] Handle to a yield matrix [n_obs x n_maturities] (rows =
            dates, columns = maturities).
        maturities: [matrix_handle, required] Handle to a strictly increasing numeric vector of
            maturities (>= 6 pillars; same count as the columns of rates).
        which_rate: [enum, optional] Curve type for fitted/residuals; default 'Spot' = the quantity
            comparable to the observed yields.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fit_svensson: not implemented."
    )
