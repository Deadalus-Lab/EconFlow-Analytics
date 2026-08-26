# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``expectile_extreme_tail`` -- method card #192.

#192 Expectile-based extreme tail risk (extreme/intermediate expectiles + marginal expected
    shortfall + the heavy-tail index)

Category 12-distribution-risk; module ``expectile_extreme_tail``.

Reference implementation: 10.1111/rssb.12254.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "er_expectiles",
    "er_mes",
    "er_tail_index",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def er_expectiles(
    *,
    data: Sequence[float],
    tau: float,
    tau1: float | None = None,
    method: Literal["LAWS", "QB"] | None = None,
    tailest: Literal["Hill", "ExpBased"] | None = None,
    var: bool | None = None,
    varType: Literal["asym-Ind", "asym-Dep"] | None = None,
    bias: bool | None = None,
    bigBlock: int | None = None,
    smallBlock: int | None = None,
    k: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``er_expectiles`` -- method card #192.

    Expectile-based extreme tail risk (extreme/intermediate expectiles + marginal expected shortfall
    + the heavy-tail index).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        data: [num_array, required] Vector of returns/losses (>=20 obs, without NA/Inf,
            non-constant).
        tau: [number, required] Intermediate level tau_n in the open (0,1) (e.g. 0.95).
        tau1: [number, optional] Extreme level tau'_n in (0,1) & > tau· if given -> extreme
            expectile prediction, otherwise intermediate.
        method: [enum, optional] Estimator: LAWS (direct, default) or QB (quantile-based, depends on
            the tail index).
        tailest: [enum, optional] Tail-index estimator when method='QB' (default Hill).
        var: [boolean, optional] True (default) -> asymptotic variance + CI. Default ``True``.
        varType: [enum, optional] Asymptotic variance type: asym-Ind (independent, default) or
            asym-Dep (serial dependence -> requires blocks).
        bias: [boolean, optional] Bias correction (only extreme/predExpectiles· default False).
            Default ``False``.
        bigBlock: [integer, optional] big-block size for the asym-Dep variance (< n).
        smallBlock: [integer, optional] small-block size for the asym-Dep variance (< bigBlock).
        k: [integer, optional] Intermediate sequence k_n in 1..n-1 (order statistics)· if None, it
            is driven by tau.
        alpha: [number, optional] CI significance level (1-alpha)· default 0.05. Default ``0.05``.

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
        "er_expectiles: not implemented."
    )


def er_mes(
    *,
    data: Sequence[float],
    data2: Sequence[float],
    tau: float,
    tau1: float,
    estimator: Literal["quantile", "expectile"] | None = None,
    method: Literal["LAWS", "QB"] | None = None,
    var: bool | None = None,
    varType: Literal["asym-Ind", "asym-Dep"] | None = None,
    bias: bool | None = None,
    bigBlock: int | None = None,
    smallBlock: int | None = None,
    k: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``er_mes`` -- method card #192.

    Expectile-based extreme tail risk (extreme/intermediate expectiles + marginal expected shortfall
    + the heavy-tail index).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        data: [num_array, required] series1 = the variable of interest (whose loss is measured).
        data2: [num_array, required] series2 = the condition· MES = E[series1 | series2 at an
            extreme level] (same length as data).
        tau: [number, required] Intermediate level tau_n in (0,1).
        tau1: [number, required] Extreme level tau'_n in (0,1) & > tau (systemic event level).
        estimator: [enum, optional] quantile -> QuantMES (default)· expectile -> ExpectMES.
        method: [enum, optional] Estimator for ExpectMES (ignored in the quantile MES· default
            LAWS).
        var: [boolean, optional] True (default) -> asymptotic variance + CI. Default ``True``.
        varType: [enum, optional] asym-Ind (default) or asym-Dep (serial dependence -> requires
            blocks).
        bias: [boolean, optional] Bias correction (default False). Default ``False``.
        bigBlock: [integer, optional] big-block size for the asym-Dep variance (< n).
        smallBlock: [integer, optional] small-block size for the asym-Dep variance (< bigBlock).
        k: [integer, optional] Intermediate sequence k_n in 1..n-1· if None, it is driven by tau.
        alpha: [number, optional] CI significance level (1-alpha)· default 0.05. Default ``0.05``.

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
        "er_mes: not implemented."
    )


def er_tail_index(
    *,
    data: Sequence[float],
    k: int,
    tau: float | None = None,
    var: bool | None = None,
    varType: Literal["asym-Ind", "asym-Dep"] | None = None,
    bias: bool | None = None,
    bigBlock: int | None = None,
    smallBlock: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``er_tail_index`` -- method card #192.

    Expectile-based extreme tail risk (extreme/intermediate expectiles + marginal expected shortfall
    + the heavy-tail index).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        data: [num_array, required] Vector of returns/losses (>=20 obs, without NA/Inf,
            non-constant).
        k: [integer, required] Intermediate sequence k_n for the Hill estimator in 1..n-1 (number of
            top order statistics).
        tau: [number, optional] Intermediate level in (0,1) for the expectile-based estimator
            (EBTailIndex)· if None, only the Hill is returned.
        var: [boolean, optional] True (default) -> asymptotic variance + CI of the Hill gamma.
            Default ``True``.
        varType: [enum, optional] asym-Ind (default) or asym-Dep (serial dependence -> requires
            blocks).
        bias: [boolean, optional] Bias-corrected Hill (default False). Default ``False``.
        bigBlock: [integer, optional] big-block size for the asym-Dep variance (< n).
        smallBlock: [integer, optional] small-block size for the asym-Dep variance (< bigBlock).
        alpha: [number, optional] CI significance level (1-alpha)· default 0.05. Default ``0.05``.

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
        "er_tail_index: not implemented."
    )
