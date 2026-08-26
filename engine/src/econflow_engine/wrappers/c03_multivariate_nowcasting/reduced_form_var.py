# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``reduced_form_var`` -- method card #11.

#11 Reduced-form VAR (lag select + Granger + diagnostics + vec2var)

Category 03-multivariate-nowcasting; module ``reduced_form_var``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c03_multivariate_nowcasting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_arch_test",
    "vr_causality",
    "vr_fit",
    "vr_lag_select",
    "vr_normality_test",
    "vr_predict",
    "vr_serial_test",
    "vr_vecm_to_var",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def vr_lag_select(
    *,
    y: pd.DataFrame,
    lag_max: int | None = None,
    type: Literal["const", "trend", "both", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_lag_select`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Handle to a multivariate series (panel, K>=2 columns).
        lag_max: [integer, optional] Maximum lag order to evaluate (default 10). Default ``10``.
        type: [enum, optional] Deterministic part (default const).

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
        "vr_lag_select: not implemented."
    )


def vr_fit(
    *,
    y: pd.DataFrame,
    p: int | None = None,
    type: Literal["const", "trend", "both", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_fit`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Handle to a multivariate series (panel, K>=2 columns, no
            NA).
        p: [integer, optional] VAR(p) lag order (default 1). Default ``1``.
        type: [enum, optional] Deterministic part (default const).

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
        "vr_fit: not implemented."
    )


def vr_predict(
    *,
    model: Any,
    n_ahead: int | None = None,
    ci: float | None = None,
) -> dict[str, Any]:
    """Node ``vr_predict`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a varest/vec2var model (from vr_fit/vr_vecm_to_var).
        n_ahead: [integer, optional] Forecast horizon (default 10). Default ``10``.
        ci: [number, optional] Fan chart confidence level in (0,1) (default 0.95). Default ``0.95``.

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
        "vr_predict: not implemented."
    )


def vr_causality(
    *,
    model: Any,
    cause: str,
    boot: bool | None = None,
    boot_runs: int | None = None,
) -> dict[str, Any]:
    """Node ``vr_causality`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``heavy``.

    Args:
        model: [raw_handle, required] Handle to a varest model (from vr_fit).
        cause: [string, required] Name of the causing variable (a subset of the VAR variables).
        boot: [boolean, optional] Bootstrap p-values (default False). Default ``False``.
        boot_runs: [integer, optional] Number of bootstrap replications (default 100). Default
            ``100``.

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
        "vr_causality: not implemented."
    )


def vr_serial_test(
    *,
    model: Any,
    lags_pt: int | None = None,
    lags_bg: int | None = None,
    type: Literal["PT.asymptotic", "PT.adjusted", "BG", "ES"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_serial_test`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a varest/vec2var model.
        lags_pt: [integer, optional] Portmanteau lags (default 16). Default ``16``.
        lags_bg: [integer, optional] Breusch-Godfrey lags (default 5). Default ``5``.
        type: [enum, optional] Test variant (default PT.asymptotic).

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
        "vr_serial_test: not implemented."
    )


def vr_arch_test(
    *,
    model: Any,
    lags_single: int | None = None,
    lags_multi: int | None = None,
    multivariate_only: bool | None = None,
) -> dict[str, Any]:
    """Node ``vr_arch_test`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a varest/vec2var model.
        lags_single: [integer, optional] Univariate ARCH-LM lags (default 16). Default ``16``.
        lags_multi: [integer, optional] Multivariate ARCH-LM lags (default 5). Default ``5``.
        multivariate_only: [boolean, optional] Multivariate test only (default True). Default
            ``True``.

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
        "vr_arch_test: not implemented."
    )


def vr_normality_test(
    *,
    model: Any,
    multivariate_only: bool | None = None,
) -> dict[str, Any]:
    """Node ``vr_normality_test`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Args:
        model: [raw_handle, required] Handle to a varest/vec2var model.
        multivariate_only: [boolean, optional] Multivariate Jarque-Bera only (default True). Default
            ``True``.

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
        "vr_normality_test: not implemented."
    )


def vr_vecm_to_var(
    *,
    z: Any,
    r: int | None = None,
) -> dict[str, Any]:
    """Node ``vr_vecm_to_var`` -- method card #11.

    Reduced-form VAR (lag select + Granger + diagnostics + vec2var).

    Category 03-multivariate-nowcasting; memory class ``light``.

    Registers its result under ``model``, so a later node can consume it as a handle.

    Args:
        z: [raw_handle, required] Handle to a Johansen Johansen object .
        r: [integer, optional] Cointegration rank r (1..K) (default 1). Default ``1``.

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
        "vr_vecm_to_var: not implemented."
    )
