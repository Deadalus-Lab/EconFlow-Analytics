# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``local_projections_lp`` -- method card #22.

#22 Local projections (Jordà) + LP-IV / non-linear state-dependent / panel

Category 04-structural-shocks; module ``local_projections_lp``.

Reference implementation: localprojections.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "lp_linear",
    "lp_linear_iv",
    "lp_nonlinear",
    "lp_nonlinear_iv",
    "lp_panel",
    "lp_panel_nl",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def lp_linear(
    *,
    endog_data: pd.DataFrame,
    lags_endog_lin: int | None = None,
    trend: int | None = None,
    shock_type: int | None = None,
    confint: float | None = None,
    hor: int | None = None,
) -> dict[str, Any]:
    """Node ``lp_linear`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        endog_data: [df_handle, required] Handle to a multivariate numeric DataFrame/ts (T x K, no
            NA).
        lags_endog_lin: [integer, optional] Endogenous lags (default 2). Default ``2``.
        trend: [integer, optional] 0=none, 1=trend, 2=trend+quadratic (default 0). Default ``0``.
        shock_type: [integer, optional] 0=1sd shock, 1=unit shock (default 1). Default ``1``.
        confint: [number, optional] CI multiplier (68%=1, 90%=1.65, 95%=1.96· default 1.96). Default
            ``1.96``.
        hor: [integer, optional] IRF horizon (positive integer, default 10). Default ``10``.

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
        "lp_linear: not implemented."
    )


def lp_linear_iv(
    *,
    endog_data: pd.DataFrame,
    shock: pd.Series,
    lags_endog_lin: int | None = None,
    trend: int | None = None,
    confint: float | None = None,
    hor: int | None = None,
    cumul_mult: bool | None = None,
    use_twosls: bool | None = None,
) -> dict[str, Any]:
    """Node ``lp_linear_iv`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        endog_data: [df_handle, required] Handle to a multivariate numeric DataFrame/ts (T x K).
        shock: [series_handle, required] Handle to an identified shock/instrument (single-column
            series, same rows).
        lags_endog_lin: [integer, optional] Endogenous lags (default 2). Default ``2``.
        trend: [integer, optional] 0=none, 1=trend, 2=trend+quadratic (default 0). Default ``0``.
        confint: [number, optional] CI multiplier (default 1.96). Default ``1.96``.
        hor: [integer, optional] IRF horizon (default 10). Default ``10``.
        cumul_mult: [boolean, optional] Cumulative multipliers (default False). Default ``False``.
        use_twosls: [boolean, optional] 2SLS (requires instrum) (default False). Default ``False``.

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
        "lp_linear_iv: not implemented."
    )


def lp_nonlinear(
    *,
    endog_data: pd.DataFrame,
    switching: pd.Series,
    lags_endog_lin: int | None = None,
    lags_endog_nl: int | None = None,
    trend: int | None = None,
    shock_type: int | None = None,
    confint: float | None = None,
    hor: int | None = None,
    use_logistic: bool | None = None,
    use_hp: bool | None = None,
    lambda_: float | None = None,
    gamma: float | None = None,
) -> dict[str, Any]:
    """Node ``lp_nonlinear`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        endog_data: [df_handle, required] Handle to a multivariate numeric DataFrame/ts (T x K).
        switching: [series_handle, required] Handle to the state-separating variable (numeric,
            length = rows).
        lags_endog_lin: [integer, optional] Linear-part lags (default 2). Default ``2``.
        lags_endog_nl: [integer, optional] Non-linear-part lags (default 2). Default ``2``.
        trend: [integer, optional] 0=none, 1=trend, 2=trend+quadratic (default 0). Default ``0``.
        shock_type: [integer, optional] 0=1sd shock, 1=unit shock (default 1). Default ``1``.
        confint: [number, optional] CI multiplier (default 1.96). Default ``1.96``.
        hor: [integer, optional] IRF horizon (default 10). Default ``10``.
        use_logistic: [boolean, optional] Logistic transition (Auerbach-Gorodnichenko) (default
            True). Default ``True``.
        use_hp: [boolean, optional] HP-filter the switching variable (requires lambda) (default
            False). Default ``False``.
        lambda_ (wire name ``lambda``): [number, optional] HP lambda (e.g. 1600 quarterly)· required
            if use_hp=True.
        gamma: [number, optional] Logistic steepness gamma (default 3). Default ``3``.

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
        "lp_nonlinear: not implemented."
    )


def lp_nonlinear_iv(
    *,
    endog_data: pd.DataFrame,
    shock: pd.Series,
    switching: pd.Series,
    lags_endog_nl: int | None = None,
    trend: int | None = None,
    confint: float | None = None,
    hor: int | None = None,
    cumul_mult: bool | None = None,
    use_logistic: bool | None = None,
    use_hp: bool | None = None,
    lambda_: float | None = None,
    gamma: float | None = None,
) -> dict[str, Any]:
    """Node ``lp_nonlinear_iv`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        endog_data: [df_handle, required] Handle to a multivariate numeric DataFrame/ts (T x K).
        shock: [series_handle, required] Handle to an identified shock/instrument (single-column
            series).
        switching: [series_handle, required] Handle to the state-separating variable (numeric).
        lags_endog_nl: [integer, optional] Non-linear-part lags (default 2). Default ``2``.
        trend: [integer, optional] 0=none, 1=trend, 2=trend+quadratic (default 0). Default ``0``.
        confint: [number, optional] CI multiplier (default 1.96). Default ``1.96``.
        hor: [integer, optional] IRF horizon (default 10). Default ``10``.
        cumul_mult: [boolean, optional] Cumulative multipliers (default False). Default ``False``.
        use_logistic: [boolean, optional] Logistic transition (default True). Default ``True``.
        use_hp: [boolean, optional] HP-filter the switching variable (requires lambda) (default
            False). Default ``False``.
        lambda_ (wire name ``lambda``): [number, optional] HP lambda· required if use_hp=True.
        gamma: [number, optional] Logistic steepness gamma (default 3). Default ``3``.

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
        "lp_nonlinear_iv: not implemented."
    )


def lp_panel(
    *,
    data_set: pd.DataFrame,
    endog_data: str,
    shock: str,
    hor: int | None = None,
    confint: float | None = None,
    panel_model: str | None = None,
    panel_effect: str | None = None,
    iv_reg: bool | None = None,
    cumul_mult: bool | None = None,
    diff_shock: bool | None = None,
) -> dict[str, Any]:
    """Node ``lp_panel`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        data_set: [df_handle, required] Handle to a panel DataFrame (1st column cross-section, 2nd
            time, >=3 columns).
        endog_data: [string, required] NAME of the dependent-variable column (not the data).
        shock: [string, required] NAME of the shock column (not the data).
        hor: [integer, optional] IRF horizon (default 10). Default ``10``.
        confint: [number, optional] CI multiplier (default 1.96). Default ``1.96``.
        panel_model: [string, optional] panel estimator (default within = fixed effects). Default
            ``'within'``.
        panel_effect: [string, optional] panel effect dimension (default individual). Default
            ``'individual'``.
        iv_reg: [boolean, optional] IV/GMM (requires instrum) (default False). Default ``False``.
        cumul_mult: [boolean, optional] Cumulative multipliers (default True). Default ``True``.
        diff_shock: [boolean, optional] First-difference the shock (default True). Default ``True``.

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
        "lp_panel: not implemented."
    )


def lp_panel_nl(
    *,
    data_set: pd.DataFrame,
    endog_data: str,
    shock: str,
    switching: str,
    hor: int | None = None,
    confint: float | None = None,
    panel_model: str | None = None,
    panel_effect: str | None = None,
    cumul_mult: bool | None = None,
    diff_shock: bool | None = None,
    use_logistic: bool | None = None,
    use_hp: bool | None = None,
    lambda_: float | None = None,
    gamma: float | None = None,
) -> dict[str, Any]:
    """Node ``lp_panel_nl`` -- method card #22.

    Local projections (Jordà) + LP-IV / non-linear state-dependent / panel.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        data_set: [df_handle, required] Handle to a panel DataFrame (cross-section, time, >=3
            columns).
        endog_data: [string, required] NAME of the dependent-variable column.
        shock: [string, required] NAME of the shock column.
        switching: [string, required] NAME of the regime-variable column.
        hor: [integer, optional] IRF horizon (default 10). Default ``10``.
        confint: [number, optional] CI multiplier (default 1.96). Default ``1.96``.
        panel_model: [string, optional] panel estimator (default within). Default ``'within'``.
        panel_effect: [string, optional] panel effect dimension (default individual). Default
            ``'individual'``.
        cumul_mult: [boolean, optional] Cumulative multipliers (default True). Default ``True``.
        diff_shock: [boolean, optional] First-difference the shock (default True). Default ``True``.
        use_logistic: [boolean, optional] Logistic transition (default True). Default ``True``.
        use_hp: [boolean, optional] HP-filter the switching variable (requires lambda) (default
            False). Default ``False``.
        lambda_ (wire name ``lambda``): [number, optional] HP lambda· required if use_hp=True.
        gamma: [number, optional] Logistic steepness gamma (default 3). Default ``3``.

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
        "lp_panel_nl: not implemented."
    )
