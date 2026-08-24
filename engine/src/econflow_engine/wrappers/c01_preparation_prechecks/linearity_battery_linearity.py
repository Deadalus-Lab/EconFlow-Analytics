# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``linearity_battery_linearity`` -- method card #132.

#132 (Non-)linearity tests: a battery of linearity tests (Teraesvirta/White ANN, Keenan, McLeod-Li,
    Tsay, LR-threshold) + an FFT surrogate-data test

Category 01-preparation-prechecks; module ``linearity_battery_linearity``.

Reference implementation: 10.1111/j.1467-9892.1993.tb00139.x.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nlt_nonlinearity",
    "nlt_surrogate",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def nlt_nonlinearity(
    *,
    x: pd.Series,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``nlt_nonlinearity`` -- method card #132.

    (Non-)linearity tests: a battery of linearity tests (Teraesvirta/White ANN, Keenan, McLeod-Li,
    Tsay, LR-threshold) + an FFT surrogate-data test.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series/ts (no NA/Inf, >= 50 obs,
            var > 0).
        seed: [integer, required] Integer seed — the White/Teraesvirta ANN component uses RANDOM
            weights· seeded for reproducibility.
        alpha: [number, optional] Decision significance level per test, in (0,1) (default 0.05).
            Default ``0.05``.

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
        "nlt_nonlinearity: not implemented."
    )


def nlt_surrogate(
    *,
    x: pd.Series,
    seed: int,
    statistic: Literal["timeAsymmetry", "timeAsymmetry2"] | None = None,
    significance: float | None = None,
    one_sided: bool | None = None,
    alternative: Literal["smaller", "larger"] | None = None,
    K: int | None = None,
    tau: int | None = None,
) -> dict[str, Any]:
    """Node ``nlt_surrogate`` -- method card #132.

    (Non-)linearity tests: a battery of linearity tests (Teraesvirta/White ANN, Keenan, McLeod-Li,
    Tsay, LR-threshold) + an FFT surrogate-data test.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Handle to a univariate numeric series/ts (no NA/Inf, >= 50 obs,
            var > 0).
        seed: [integer, required] Integer seed — FFTsurrogate phase randomisation (stochastic·
            MANDATORY).
        statistic: [enum, optional] Discriminating statistic: timeAsymmetry (default) or
            timeAsymmetry2 (requires tau). Default ``'timeAsymmetry'``.
        significance: [number, optional] Significance level· controls the number of surrogates, in
            (0,1) (default 0.05). Default ``0.05``.
        one_sided: [boolean, optional] False=two-sided (default)· True=one-sided (uses alternative).
            Default ``False``.
        alternative: [enum, optional] One-sided direction (ONLY when one.sided=True): smaller
            (default) or larger. Default ``'smaller'``.
        K: [integer, optional] Positive integer· controls surrogates (2K/sig-1 two-sided, K/sig-1
            one-sided) (default 1). Default ``1``.
        tau: [integer, optional] Time-delay for timeAsymmetry2, positive integer (default 1· ignored
            otherwise). Default ``1``.

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
        "nlt_surrogate: not implemented."
    )
