# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``affluence_richness_indices`` -- method card #228.

#228 affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio, the Chakravarty concave T1 index, the FGT convex T2 index, the Medeiros average affluence
    gap, the top income share, the Medeiros affluence line — weighted implementations

Category 22-inequality; module ``affluence_richness_indices``.

Reference implementation: 10.1111/j.1475-4991.2010.00404.x.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c22_inequality import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "affluence_line",
    "income_share_top",
    "richness_index",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def richness_index(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    k: float,
    index: Literal["hc", "cha", "fgt", "med"] | None = None,
    beta: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``richness_index`` -- method card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio, the Chakravarty concave T1 index, the FGT convex T2 index, the Medeiros average affluence
    gap, the top income share, the Medeiros affluence line — weighted implementations.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of incomes (x > 0), length >= 2,
            without NA/Inf.
        weight: [matrix_handle, optional] Handle to optional population weights (same length as x, >
            0); omission => equal weights.
        k: [number, required] Multiple of the median for the affluence line; k > 1 IS REQUIRED
            (UPPER threshold — k<=1 => "everyone is rich").
        index: [enum, optional] hc=richness headcount ratio; cha=concave (Chakravarty,T1);
            fgt=convex (FGT,T2); med=mean affluence gap (Medeiros, absolute). default hc.
        beta: [number, optional] Parameter for index='cha' (beta > 0; default 2).
        alpha: [number, optional] Parameter for index='fgt' (alpha > 1; default 2).

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
        "richness_index: not implemented."
    )


def income_share_top(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    p: float,
) -> dict[str, Any]:
    """Node ``income_share_top`` -- method card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio, the Chakravarty concave T1 index, the FGT convex T2 index, the Medeiros average affluence
    gap, the top income share, the Medeiros affluence line — weighted implementations.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of incomes (x > 0), length >= 2.
        weight: [matrix_handle, optional] Handle to optional weights (same length, > 0); omission =>
            equal.
        p: [number, required] Percentile threshold in (0,1); the index = the share of income of the
            richest (1-p) fraction (e.g. p=0.9 => top 10%).

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
        "income_share_top: not implemented."
    )


def affluence_line(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    k: float,
) -> dict[str, Any]:
    """Node ``affluence_line`` -- method card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio, the Chakravarty concave T1 index, the FGT convex T2 index, the Medeiros average affluence
    gap, the top income share, the Medeiros affluence line — weighted implementations.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of incomes (x > 0), length >= 2.
        weight: [matrix_handle, optional] Handle to optional weights (same length, > 0); omission =>
            equal.
        k: [number, required] POVERTY line as a multiple of the median; 0 < k < 1 IS REQUIRED (LOWER
            threshold — opposite meaning from richness_index).

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
        "affluence_line: not implemented."
    )
