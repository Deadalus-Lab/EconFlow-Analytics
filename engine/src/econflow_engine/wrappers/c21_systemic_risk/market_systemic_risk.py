# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``market_systemic_risk`` -- method card #221.

#221 Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures

Category 21-systemic-risk; module ``market_systemic_risk``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from econflow_engine.generated.args.c21_systemic_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sys_correlation_network_measures",
    "sys_covar_delta_covar",
    "sys_covar_delta_covar_t",
    "sys_scale",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sys_covar_delta_covar(
    *,
    returns: np.ndarray,
) -> dict[str, Any]:
    """Node ``sys_covar_delta_covar`` -- method card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        returns: [matrix_handle, required] Handle to a numeric matrix of returns; column 1 = the
            system/market index, columns 2..p = institutions (>= 2 institutions, i.e. >= 3 columns);
            >= 30 rows; without NA/NaN/Inf. q=0.95 is hardcoded in the package.

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
        "sys_covar_delta_covar: not implemented."
    )


def sys_covar_delta_covar_t(
    *,
    returns: np.ndarray,
    state_variables: np.ndarray,
) -> dict[str, Any]:
    """Node ``sys_covar_delta_covar_t`` -- method card #221.

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
        "sys_covar_delta_covar_t: not implemented."
    )


def sys_correlation_network_measures(
    *,
    returns: np.ndarray,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``sys_correlation_network_measures`` -- method card #221.

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
        "sys_correlation_network_measures: not implemented."
    )


def sys_scale(
    *,
    x: np.ndarray,
) -> dict[str, Any]:
    """Node ``sys_scale`` -- method card #221.

    Market-based systemic risk: CoVaR / Delta-CoVaR (Adrian-Brunnermeier) + correlation-network
    measures.

    Category 21-systemic-risk; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector (>= 2 elements, non-constant,
            without NA/NaN/Inf); min-max into [0,1].

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
        "sys_scale: not implemented."
    )
