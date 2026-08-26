# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``univariate_garch_variants`` -- method card #154.

#154 Univariate GARCH family (vanilla/egarch/gjr/aparch/component)

Category 06-volatility-regimes; module ``univariate_garch_variants``.

Reference implementation: arch.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "tg_backtest",
    "tg_estimate",
    "tg_predict",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def tg_estimate(
    *,
    y: Sequence[float],
    model: Literal["garch", "egarch", "gjrgarch", "aparch", "cgarch"] | None = None,
    constant: bool | None = None,
    order: Sequence[int] | None = None,
    distribution: (
        Literal[
            "norm",
            "std",
            "ged",
            "snorm",
            "sstd",
            "sged",
            "nig",
            "gh",
            "jsu",
            "ghst",
        ]
        | None
    ) = None,
    variance_targeting: bool | None = None,
    solver: str | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tg_estimate`` -- method card #154.

    Univariate GARCH family (vanilla/egarch/gjr/aparch/component).

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [num_array, required] Numeric vector of returns (without NA/Inf, non-constant, >=25).
        model: [enum, optional] GARCH type (default garch· egarch/gjrgarch/aparch=asymmetric,
            cgarch=component).
        constant: [boolean, optional] Estimate a constant (mean) term for the returns (default
            True). Default ``True``.
        order: [int_array, optional] GARCH order [p,q] (default [1,1]).
        distribution: [enum, optional] Innovation distribution (default norm· std/ged for fat tails,
            s*=skew).
        variance_targeting: [boolean, optional] Variance targeting (omega from the sample uncond.
            variance, default False). Default ``False``.
        solver: [string, optional] ML optimizer (default 'nloptr'). Default ``'nloptr'``.
        seed: [integer, optional] Seed (estimation is deterministic· default 2025). Default
            ``2025``.

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
        "tg_estimate: not implemented."
    )


def tg_predict(
    *,
    object: Any,
    h: int | None = None,
    nsim: int | None = None,
    sim_method: Literal["parametric", "bootstrap"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tg_predict`` -- method card #154.

    Univariate GARCH family (vanilla/egarch/gjr/aparch/component).

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        object: [raw_handle, required] Handle to a 'tsgarch.estimate' (from tg_estimate).
        h: [integer, optional] Forecast horizon for conditional sigma/mean (>=1, default 1). Default
            ``1``.
        nsim: [integer, optional] Simulated paths for the forecast distribution (0=point forecast,
            default 0· seeded). Default ``0``.
        sim_method: [enum, optional] Simulation method when nsim>0 (default parametric).
        seed: [integer, optional] Seed for the stochastic simulation (default 2025). Default
            ``2025``.

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
        "tg_predict: not implemented."
    )


def tg_backtest(
    *,
    y: Sequence[float],
    model: Literal["garch", "egarch", "gjrgarch", "aparch", "cgarch"] | None = None,
    constant: bool | None = None,
    order: Sequence[int] | None = None,
    distribution: (
        Literal[
            "norm",
            "std",
            "ged",
            "snorm",
            "sstd",
            "sged",
            "nig",
            "gh",
            "jsu",
            "ghst",
        ]
        | None
    ) = None,
    start: int | None = None,
    end: int | None = None,
    h: int | None = None,
    estimate_every: int | None = None,
    rolling: bool | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``tg_backtest`` -- method card #154.

    Univariate GARCH family (vanilla/egarch/gjr/aparch/component).

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        y: [num_array, required] Numeric vector of returns (without NA/Inf, non-constant, >=40).
        model: [enum, optional] GARCH type (default garch).
        constant: [boolean, optional] Estimate a constant (mean) term (default True). Default
            ``True``.
        order: [int_array, optional] GARCH order [p,q] (default [1,1]).
        distribution: [enum, optional] Innovation distribution (default norm).
        start: [integer, optional] Out-of-sample start index (>=10, default floor(n/2)).
        end: [integer, optional] End index (<=length(y), default length(y)).
        h: [integer, optional] Forecast horizon per step (default 1). Default ``1``.
        estimate_every: [integer, optional] Re-estimate every n steps (default 1). Default ``1``.
        rolling: [boolean, optional] Rolling (True) vs expanding (False, default) window. Default
            ``False``.
        seed: [integer, optional] Seed (default 2025). Default ``2025``.

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
        "tg_backtest: not implemented."
    )
