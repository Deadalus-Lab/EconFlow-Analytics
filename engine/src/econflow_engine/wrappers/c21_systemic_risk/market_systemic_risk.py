# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``market_systemic_risk`` -- METHOD-SELECTION card #221.

#221 Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures

Category 21-systemic-risk; module ``market_systemic_risk``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "syr_correlation_network_measures",
    "syr_covar_delta_covar",
    "syr_covar_delta_covar_t",
    "syr_scale",
    "NODE_META",
    "wire_model",
]


def syr_covar_delta_covar(
    *,
    returns: np.ndarray,
) -> dict[str, Any]:
    """Node ``syr_covar_delta_covar`` -- METHOD-SELECTION card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a numeric matrix of returns; column 1 = the
            system/market index, columns 2..p = institutions (>= 2 institutions, i.e. >= 3 columns);
            >= 30 rows; without NA/NaN/Inf. q=0.95 is hardcoded in the package.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "syr_covar_delta_covar: not implemented. The method card is in ./README.md."
    )


def syr_covar_delta_covar_t(
    *,
    returns: np.ndarray,
    state_variables: np.ndarray,
) -> dict[str, Any]:
    """Node ``syr_covar_delta_covar_t`` -- METHOD-SELECTION card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a numeric matrix of returns; column 1 = the
            system, columns 2..p = institutions (>= 3 columns); >= 50 rows; without NA/NaN/Inf.
        state_variables: [matrix_handle, required] Handle to a numeric matrix of state variables
            (e.g. VIX, spreads); >= 2 columns (NSV=1 breaks the package); same number of rows as
            returns; without NA/NaN/Inf.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "syr_covar_delta_covar_t: not implemented. The method card is in ./README.md."
    )


def syr_correlation_network_measures(
    *,
    returns: np.ndarray,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``syr_correlation_network_measures`` -- METHOD-SELECTION card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a numeric matrix of daily returns; >= 3
            columns; >= 90 rows (coarse pre-gate) AND >= 3 full calendar months (~>= 100 rows;
            post-gate n_months>=3, otherwise blocked-by-gate: with < 3 months the monthly min-max
            degenerates to {0,1}); without NA/NaN/Inf. All columns become network nodes.
        seed: [integer, optional] Seed (default 123) — stabilizes the eigenvector-centrality routine
            (ARPACK) for determinism.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "syr_correlation_network_measures: not implemented. The method card is in ./README.md."
    )


def syr_scale(
    *,
    x: np.ndarray,
) -> dict[str, Any]:
    """Node ``syr_scale`` -- METHOD-SELECTION card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector (>= 2 elements, non-constant,
            without NA/NaN/Inf); min-max into [0,1].

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "syr_scale: not implemented. The method card is in ./README.md."
    )
