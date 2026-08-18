# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``affluence_richness_indices`` -- METHOD-SELECTION card #228.

#228 affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio (r.hc), the Chakravarty concave T1 index (r.cha), the FGT convex T2 index (r.fgt), the
    Medeiros average affluence gap (r.med), the top income share (r.is), the Medeiros affluence line
    (line.med) — weighted implementations

Category 22-inequality; module ``affluence_richness_indices``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
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


def richness_index(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    k: float,
    index: Literal["hc", "cha", "fgt", "med"] | None = None,
    beta: float | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``richness_index`` -- METHOD-SELECTION card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio (r.hc), the Chakravarty concave T1 index (r.cha), the FGT convex T2 index (r.fgt), the
    Medeiros average affluence gap (r.med), the top income share (r.is), the Medeiros affluence line
    (line.med) — weighted implementations.

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
    """
    raise NotImplementedError(
        "richness_index: not implemented. The method card is in ./README.md."
    )


def income_share_top(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    p: float,
) -> dict[str, Any]:
    """Node ``income_share_top`` -- METHOD-SELECTION card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio (r.hc), the Chakravarty concave T1 index (r.cha), the FGT convex T2 index (r.fgt), the
    Medeiros average affluence gap (r.med), the top income share (r.is), the Medeiros affluence line
    (line.med) — weighted implementations.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of incomes (x > 0), length >= 2.
        weight: [matrix_handle, optional] Handle to optional weights (same length, > 0); omission =>
            equal.
        p: [number, required] Percentile threshold in (0,1); the index = the share of income of the
            richest (1-p) fraction (e.g. p=0.9 => top 10%).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "income_share_top: not implemented. The method card is in ./README.md."
    )


def affluence_line(
    *,
    x: np.ndarray,
    weight: np.ndarray | None = None,
    k: float,
) -> dict[str, Any]:
    """Node ``affluence_line`` -- METHOD-SELECTION card #228.

    affluence/richness indices (the top-tail mirror of poverty indices): the richness headcount
    ratio (r.hc), the Chakravarty concave T1 index (r.cha), the FGT convex T2 index (r.fgt), the
    Medeiros average affluence gap (r.med), the top income share (r.is), the Medeiros affluence line
    (line.med) — weighted implementations.

    Category 22-inequality; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a numeric vector of incomes (x > 0), length >= 2.
        weight: [matrix_handle, optional] Handle to optional weights (same length, > 0); omission =>
            equal.
        k: [number, required] POVERTY line as a multiple of the median; 0 < k < 1 IS REQUIRED (LOWER
            threshold — opposite meaning from richness_index).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "affluence_line: not implemented. The method card is in ./README.md."
    )
