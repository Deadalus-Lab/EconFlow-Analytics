# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rdd_robust`` -- METHOD-SELECTION card #38.

#38 RDD robust (Calonico-Cattaneo-Titiunik)

Category 07-causality-policy; module ``rdd_robust``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "wrap_rdbwselect",
    "wrap_rdrobust",
    "NODE_META",
    "wire_model",
]


def wrap_rdrobust(
    *,
    y: Any,
    x: Any,
    c: float | None = None,
    fuzzy: Any | None = None,
    p: int | None = None,
    kernel: Literal["tri", "epanechnikov", "uniform"] | None = None,
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
    vce: Literal["nn", "hc0", "hc1", "hc2", "hc3", "cr1", "cr2", "cr3"] | None = None,
    level: float | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdrobust`` -- METHOD-SELECTION card #38.

    RDD robust (Calonico-Cattaneo-Titiunik).

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (numeric, no NA).
        x: [raw_handle, required] Handle to a running variable vector (same length as y).
        c: [number, optional] Cutoff of the running variable (default 0). Default ``0``.
        fuzzy: [raw_handle, optional] Handle to a treatment-status vector for fuzzy RD (default:
            sharp).
        p: [integer, optional] Local polynomial degree (default 1).
        kernel: [enum, optional] Kernel (default tri).
        bwselect: [enum, optional] Bandwidth selector (default mserd).
        vce: [enum, optional] Variance estimator (default nn).
        level: [number, optional] Confidence level (0-100, default 95). Default ``95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdrobust: not implemented. The method card is in ./README.md."
    )


def wrap_rdbwselect(
    *,
    y: Any,
    x: Any,
    c: float | None = None,
    p: int | None = None,
    kernel: Literal["tri", "epanechnikov", "uniform"] | None = None,
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
    vce: Literal["nn", "hc0", "hc1", "hc2", "hc3", "cr1", "cr2", "cr3"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdbwselect`` -- METHOD-SELECTION card #38.

    RDD robust (Calonico-Cattaneo-Titiunik).

    Category 07-causality-policy; memory class ``light``.

    Args:
        y: [raw_handle, required] Handle to an outcome vector.
        x: [raw_handle, required] Handle to a running variable vector.
        c: [number, optional] Cutoff (default 0). Default ``0``.
        p: [integer, optional] Polynomial degree (default 1).
        kernel: [enum, optional] Kernel (default tri).
        bwselect: [enum, optional] Bandwidth selector (default mserd).
        vce: [enum, optional] Variance estimator (default nn).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdbwselect: not implemented. The method card is in ./README.md."
    )
