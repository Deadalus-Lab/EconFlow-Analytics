# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``change_point_detection`` -- method card #213.

#213 Change-point detection in mean / variance / mean+variance (PELT/BinSeg/SegNeigh/AMOC)

Category 19-business-cycle-dating; module ``change_point_detection``.

Reference implementation: ruptures.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "changepoint_segments",
    "detect_changepoints",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def detect_changepoints(
    *,
    x: pd.Series,
    statistic: Literal["mean", "variance", "meanvar"] | None = None,
    penalty: (
        Literal[
            "MBIC",
            "SIC",
            "BIC",
            "AIC",
            "Hannan-Quinn",
            "Asymptotic",
            "Manual",
            "None",
        ]
        | None
    ) = None,
    pen_value: float | None = None,
    method: Literal["PELT", "AMOC", "SegNeigh", "BinSeg"] | None = None,
    Q: int | None = None,
    test_stat: str | None = None,
    minseglen: int | None = None,
    know_mean: bool | None = None,
    mu: float | None = None,
    shape: float | None = None,
) -> dict[str, Any]:
    """Node ``detect_changepoints`` -- method card #213.

    Change-point detection in mean / variance / mean+variance (PELT/BinSeg/SegNeigh/AMOC).

    Category 19-business-cycle-dating; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        x: [series_handle, required] Handle to a univariate numeric/ts series (without NA/Inf; not a
            matrix).
        statistic: [enum, optional] Which structure changes: mean (cpt.mean) / variance (cpt.var) /
            meanvar (cpt.meanvar). Default mean.
        penalty: [enum, optional] Penalty for selecting the number of change-points. Default MBIC.
            Manual/Asymptotic require pen_value.
        pen_value: [number, optional] Penalty value: Manual => >0; Asymptotic => type-I error in
            (0,1]. A number only (not a formula). Default ``0``.
        method: [enum, optional] Search algorithm. Default PELT (exact, fast). AMOC=at most 1 cp.
            CSS/CUSUM do NOT work with PELT.
        Q: [integer, optional] Maximum number of change-points (BinSeg) / segments (SegNeigh). Q <
            n/minseglen is required. Default ``5``.
        test_stat: [string, optional] Distribution/statistic: mean∈{Normal,CUSUM};
            variance∈{Normal,CSS}; meanvar∈{Normal,Gamma,Exponential,Poisson}. Default Normal.
        minseglen: [integer, optional] Minimum segment length. Default: 1 (mean) / 2
            (variance,meanvar).
        know_mean: [boolean, optional] ONLY statistic='variance': if True, the mean is considered
            known (mu). Default ``False``.
        mu: [number, optional] ONLY statistic='variance' with know_mean=True: the known value of the
            mean.
        shape: [number, optional] ONLY statistic='meanvar' with test_stat='Gamma': the known shape
            parameter. Default ``1``.

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
        "detect_changepoints: not implemented."
    )


def changepoint_segments(
    *,
    fit: Any,
) -> dict[str, Any]:
    """Node ``changepoint_segments`` -- method card #213.

    Change-point detection in mean / variance / mean+variance (PELT/BinSeg/SegNeigh/AMOC).

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an S4 'cpt' object (from detect_changepoints register
            field 'fit').

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
        "changepoint_segments: not implemented."
    )
