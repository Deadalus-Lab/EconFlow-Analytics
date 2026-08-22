# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rd_multiple_cutoffs`` -- method card #169.

#169 RD with multiple cutoffs / multiple scores (multi-cutoff & multi-score RD, robust
    bias-corrected)

Category 07-causality-policy; module ``rd_multiple_cutoffs``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rd_multi_cutoff",
    "rd_multi_score",
    "NODE_META",
    "wire_model",
]


def rd_multi_cutoff(
    *,
    Y: Sequence[float],
    X: Sequence[float],
    C: Sequence[float],
    fuzzy: Sequence[float] | None = None,
    covs_mat: Sequence[float] | None = None,
    cluster: Sequence[float] | None = None,
    kernel: Literal["tri", "epanechnikov", "uniform"] | None = None,
    p: int | None = None,
    bwselect: (
        Literal[
            "mserd",
            "msetwo",
            "msesum",
            "msecomb1",
            "msecomb2",
            "cerrd",
            "certwo",
            "cersum",
            "cercomb1",
            "cercomb2",
        ]
        | None
    ) = None,
    level: float | None = None,
    conventional: bool | None = None,
) -> dict[str, Any]:
    """Node ``rd_multi_cutoff`` -- method card #169.

    RD with multiple cutoffs / multiple scores (multi-cutoff & multi-score RD, robust
    bias-corrected).

    Category 07-causality-policy; memory class ``light``.

    Args:
        Y: [num_array, required] Outcome vector (numeric, no NA).
        X: [num_array, required] Running variable vector (same length as Y).
        C: [num_array, required] Per-observation cutoff variable (same length as X; >=2 distinct
            cutoffs).
        fuzzy: [num_array, optional] Treatment-status vector for fuzzy RD (default: sharp).
        covs_mat: [num_array, optional] Covariate vector/matrix (nrow == length of X; no NA).
        cluster: [num_array, optional] Cluster ID vector (same length as X).
        kernel: [enum, optional] Kernel (default tri). Default ``'tri'``.
        p: [integer, optional] Local polynomial degree (default 1). Default ``1``.
        bwselect: [enum, optional] Bandwidth selector (default mserd). Default ``'mserd'``.
        level: [number, optional] Confidence level in (0,100) (default 95). Default ``95``.
        conventional: [boolean, optional] True -> conventional instead of robust bias-corrected
            inference. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rd_multi_cutoff: not implemented."
    )


def rd_multi_score(
    *,
    Y: Sequence[float],
    X: Sequence[float],
    C: Sequence[float],
    xnorm: Sequence[float] | None = None,
    fuzzy: Sequence[float] | None = None,
    covs_mat: Sequence[float] | None = None,
    cluster: Sequence[float] | None = None,
    kernel: Literal["tri", "epanechnikov", "uniform"] | None = None,
    p: int | None = None,
    bwselect: (
        Literal[
            "mserd",
            "msetwo",
            "msesum",
            "msecomb1",
            "msecomb2",
            "cerrd",
            "certwo",
            "cersum",
            "cercomb1",
            "cercomb2",
        ]
        | None
    ) = None,
    level: float | None = None,
    conventional: bool | None = None,
) -> dict[str, Any]:
    """Node ``rd_multi_score`` -- method card #169.

    RD with multiple cutoffs / multiple scores (multi-cutoff & multi-score RD, robust
    bias-corrected).

    Category 07-causality-policy; memory class ``light``.

    Args:
        Y: [num_array, required] Outcome vector (numeric, no NA).
        X: [num_array, required] Running variable vector (same length as Y).
        C: [num_array, required] Vector of cutoff values (e.g. [33,66]; non-empty, no NA).
        xnorm: [num_array, optional] Normalized running variable for the pooled estimate (without it
            pooled=NA).
        fuzzy: [num_array, optional] Treatment-status vector for fuzzy RD (default: sharp).
        covs_mat: [num_array, optional] Covariate vector/matrix (nrow == length of X; no NA).
        cluster: [num_array, optional] Cluster ID vector (same length as X).
        kernel: [enum, optional] Kernel (default tri). Default ``'tri'``.
        p: [integer, optional] Local polynomial degree (default 1). Default ``1``.
        bwselect: [enum, optional] Bandwidth selector (default mserd). Default ``'mserd'``.
        level: [number, optional] Confidence level in (0,100) (default 95). Default ``95``.
        conventional: [boolean, optional] True -> conventional instead of robust bias-corrected
            inference. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "rd_multi_score: not implemented."
    )
