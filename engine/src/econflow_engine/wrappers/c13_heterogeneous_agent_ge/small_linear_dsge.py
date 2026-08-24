# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``small_linear_dsge`` -- method card #200.

#200 Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition

Category 13-heterogeneous-agent-ge; module ``small_linear_dsge``.

Reference implementation: linearsolve.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c13_heterogeneous_agent_ge import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dsge_estimate",
    "dsge_forecast",
    "dsge_irf",
    "dsge_shock_decomposition",
    "dsge_solve",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dsge_solve(
    *,
    obs_eqs: Sequence[str],
    state_eqs: Sequence[str],
    unobs_eqs: Sequence[str] | None = None,
    fixed: Any | None = None,
    params: Any,
    shock_sd: Any | None = None,
    tol: float | None = None,
) -> dict[str, Any]:
    """Node ``dsge_solve`` -- method card #200.

    Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        obs_eqs: [series_codes, required] Observed control equations 'lhs ~ rhs' (lead/E for forward
            expectations).
        state_eqs: [series_codes, required] Exogenous AR state equations with shock (#state_eqs ==
            #obs_eqs).
        unobs_eqs: [series_codes, optional] Unobserved control equations (optional).
        fixed: [raw, optional] Named-numeric map of fixed parameters (e.g. {beta:0.96}).
        params: [raw, required] Named-numeric map of parameter values for the solution.
        shock_sd: [raw, optional] Named-numeric map of shock SD (>0)· default 1 per shock.
        tol: [number, optional] Tolerance for classifying an eigenvalue as stable (default 1e-6).
            Default ``1e-06``.

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
        "dsge_solve: not implemented."
    )


def dsge_estimate(
    *,
    obs_eqs: Sequence[str],
    state_eqs: Sequence[str],
    unobs_eqs: Sequence[str] | None = None,
    fixed: Any | None = None,
    start: Any | None = None,
    data: pd.DataFrame,
    method: Literal["BFGS", "Nelder-Mead", "CG", "L-BFGS-B"] | None = None,
    demean: bool | None = None,
    maxit: int | None = None,
) -> dict[str, Any]:
    """Node ``dsge_estimate`` -- method card #200.

    Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        obs_eqs: [series_codes, required] Observed control equations 'lhs ~ rhs' (names = data
            columns).
        state_eqs: [series_codes, required] Exogenous AR state equations with shock (#state_eqs ==
            #obs_eqs).
        unobs_eqs: [series_codes, optional] Unobserved control equations (optional).
        fixed: [raw, optional] Named-numeric map of fixed parameters.
        start: [raw, optional] Named-numeric map of initial values for the free params.
        data: [df_handle, required] Handle to a DataFrame/matrix/ts· columns = names of the observed
            controls.
        method: [enum, optional] Optimizer optim (default BFGS).
        demean: [boolean, optional] Removal of the mean from the observed before estimation (default
            True). Default ``True``.
        maxit: [integer, optional] Maximum optimizer iterations (default 500). Default ``500``.

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
        "dsge_estimate: not implemented."
    )


def dsge_irf(
    *,
    object: Any,
    periods: int | None = None,
    impulse: Sequence[str] | None = None,
    response: Sequence[str] | None = None,
    se: bool | None = None,
    level: float | None = None,
) -> dict[str, Any]:
    """Node ``dsge_irf`` -- method card #200.

    Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a dsge_solution (dsge_solve) or a dsge_fit
            (dsge_estimate).
        periods: [integer, optional] IRF horizon in periods (default 20). Default ``20``.
        impulse: [series_codes, optional] Names of shocks for the impulse (default all).
        response: [series_codes, optional] Names of response variables (default all).
        se: [boolean, optional] Delta-method SE + CI bands (applies ONLY to dsge_fit· default True).
            Default ``True``.
        level: [number, optional] Confidence level for the bands ∈ (0,1) (default 0.95). Default
            ``0.95``.

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
        "dsge_irf: not implemented."
    )


def dsge_forecast(
    *,
    object: Any,
    horizon: int | None = None,
) -> dict[str, Any]:
    """Node ``dsge_forecast`` -- method card #200.

    Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a dsge_fit (dsge_estimate)· requires filtered
            states.
        horizon: [integer, optional] Forecast horizon in periods (default 12). Default ``12``.

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
        "dsge_forecast: not implemented."
    )


def dsge_shock_decomposition(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``dsge_shock_decomposition`` -- method card #200.

    Small linear(ized) DSGE: Klein (2000) solution + Kalman-filter ML estimation, structural IRFs,
    forecasts and historical shock decomposition.

    Category 13-heterogeneous-agent-ge; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a dsge_fit (dsge_estimate)· Kalman smoother.

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
        "dsge_shock_decomposition: not implemented."
    )
