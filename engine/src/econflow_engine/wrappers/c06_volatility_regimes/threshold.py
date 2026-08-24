# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``threshold`` -- method card #32.

#32 Threshold models (SETAR/LSTAR/STAR)

Category 06-volatility-regimes; module ``threshold``.

Reference implementation: 10.2202/1558-3708.1024.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "lstar_fit",
    "setar_fit",
    "setar_select",
    "setar_test",
    "star_fit",
    "thr_predict",
    "thr_regime",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def setar_fit(
    *,
    x: pd.Series,
    m: int,
    d: int | None = None,
    thDelay: int | None = None,
    include: Literal["const", "trend", "none", "both"] | None = None,
    common: Literal["none", "include", "lags", "both"] | None = None,
    model: Literal["TAR", "MTAR"] | None = None,
    nthresh: int | None = None,
    trim: float | None = None,
) -> dict[str, Any]:
    """Node ``setar_fit`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series (without NA).
        m: [integer, required] Embedding dimension / maximum lag (positive integer).
        d: [integer, optional] Time delay for the embedding (default 1). Default ``1``.
        thDelay: [integer, optional] Lag of the threshold variable, 0..(m-1) (default 0). Default
            ``0``.
        include: [enum, optional] Deterministic terms (default const).
        common: [enum, optional] Common coefficients across regimes (default none).
        model: [enum, optional] TAR (levels) or MTAR (momentum, default TAR).
        nthresh: [integer, optional] Number of thresholds: 1 or 2 (default 1). Default ``1``.
        trim: [number, optional] Minimum share per regime in (0,0.5) (default 0.15). Default
            ``0.15``.

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
        "setar_fit: not implemented."
    )


def lstar_fit(
    *,
    x: pd.Series,
    m: int,
    d: int | None = None,
    thDelay: int | None = None,
    gamma: float | None = None,
    include: Literal["const", "trend", "none", "both"] | None = None,
) -> dict[str, Any]:
    """Node ``lstar_fit`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series (without NA).
        m: [integer, required] Embedding dimension / maximum lag (positive integer).
        d: [integer, optional] Time delay for the embedding (default 1). Default ``1``.
        thDelay: [integer, optional] Lag of the threshold variable (default: internal selection).
        gamma: [number, optional] Initial smoothness value (>0· default: internal estimate).
        include: [enum, optional] Deterministic terms (default const).

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
        "lstar_fit: not implemented."
    )


def star_fit(
    *,
    x: pd.Series,
    noRegimes: int,
    m: int | None = None,
    d: int | None = None,
    sig: float | None = None,
) -> dict[str, Any]:
    """Node ``star_fit`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series (without NA).
        noRegimes: [integer, required] Maximum number of regimes to test (>=2).
        m: [integer, optional] Embedding dimension / maximum lag (default 2). Default ``2``.
        d: [integer, optional] Time delay for the embedding (default 1). Default ``1``.
        sig: [number, optional] Significance level for adding a regime (default 0.05). Default
            ``0.05``.

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
        "star_fit: not implemented."
    )


def setar_select(
    *,
    x: pd.Series,
    m: int,
    thDelay: int | None = None,
    nthresh: int | None = None,
    trim: float | None = None,
    criterion: Literal["pooled-AIC", "AIC", "BIC", "SSR"] | None = None,
    include: Literal["const", "trend", "none", "both"] | None = None,
    model: Literal["TAR", "MTAR"] | None = None,
) -> dict[str, Any]:
    """Node ``setar_select`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series (without NA).
        m: [integer, required] Maximum lag / embedding dimension (positive integer).
        thDelay: [integer, optional] Threshold delay to test, 0..(m-1) (default 0). Default ``0``.
        nthresh: [integer, optional] Number of thresholds: 1 or 2 (default 1). Default ``1``.
        trim: [number, optional] Minimum share per regime in (0,0.5) (default 0.15). Default
            ``0.15``.
        criterion: [enum, optional] Selection criterion (default pooled-AIC).
        include: [enum, optional] Deterministic terms (default const).
        model: [enum, optional] TAR or MTAR (default TAR).

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
        "setar_select: not implemented."
    )


def setar_test(
    *,
    x: pd.Series,
    m: int,
    thDelay: int | None = None,
    trim: float | None = None,
    include: Literal["const", "trend", "none", "both"] | None = None,
    nboot: int | None = None,
    test: Literal["1vs", "2vs3"] | None = None,
    boot_scheme: Literal["resample", "resample_block", "wild1", "wild2", "check"] | None = None,
) -> dict[str, Any]:
    """Node ``setar_test`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series (without NA).
        m: [integer, required] Maximum lag / embedding dimension (positive integer).
        thDelay: [integer, optional] Threshold delay (default 0). Default ``0``.
        trim: [number, optional] Minimum share per regime in (0,0.5) (default 0.1). Default ``0.1``.
        include: [enum, optional] Deterministic terms (default const).
        nboot: [integer, optional] Bootstrap replications (seeded, default 100). Default ``100``.
        test: [enum, optional] 1vs=linear vs SETAR· 2vs3=1 vs 2 thresholds (default 1vs).
        boot_scheme: [enum, optional] Bootstrap scheme (default resample).

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
        "setar_test: not implemented."
    )


def thr_predict(
    *,
    object: Any,
    n_ahead: int | None = None,
    type: Literal["naive", "MC", "bootstrap", "block-bootstrap"] | None = None,
    nboot: int | None = None,
    ci: float | None = None,
) -> dict[str, Any]:
    """Node ``thr_predict`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        object: [raw_handle, required] Handle to an 'nlar' model (from
            setar_fit/lstar_fit/star_fit).
        n_ahead: [integer, optional] Forecast horizon (default 1). Default ``1``.
        type: [enum, optional] naive=point· MC/bootstrap=distribution (seeded, default naive).
        nboot: [integer, optional] Replications for MC/bootstrap (default 100). Default ``100``.
        ci: [number, optional] Prediction interval level in (0,1) (default 0.95). Default ``0.95``.

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
        "thr_predict: not implemented."
    )


def thr_regime(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``thr_regime`` -- method card #32.

    Threshold models (SETAR/LSTAR/STAR).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'setar'/'lstar' model (from setar_fit/lstar_fit).

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
        "thr_regime: not implemented."
    )
