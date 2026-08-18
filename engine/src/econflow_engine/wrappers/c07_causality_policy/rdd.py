# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rdd`` -- METHOD-SELECTION card #39.

#39 RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only)

Category 07-causality-policy; module ``rdd``.

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
    "wrap_rdd_bw_ik",
    "wrap_rdd_data",
    "wrap_rdd_reg_lm",
    "wrap_rdd_reg_np",
    "NODE_META",
    "wire_model",
]


def wrap_rdd_data(
    *,
    y: Any,
    x: Any,
    cutpoint: float,
    z: Any | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdd_data`` -- METHOD-SELECTION card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        y: [raw_handle, required] Handle to an outcome vector (no NA).
        x: [raw_handle, required] Handle to a running variable vector (same length as y).
        cutpoint: [number, required] Cutpoint inside the range of x.
        z: [raw_handle, optional] Handle to a binary (0/1) treatment vector for fuzzy RD.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdd_data: not implemented. The method card is in ./README.md."
    )


def wrap_rdd_reg_lm(
    *,
    rdd_object: Any,
    order: int | None = None,
    slope: Literal["separate", "same"] | None = None,
    bw: float | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdd_reg_lm`` -- METHOD-SELECTION card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object (from wrap_rdd_data).
        order: [integer, optional] Polynomial degree (default 1). Default ``1``.
        slope: [enum, optional] Slope on each side of the cutpoint (default separate).
        bw: [number, optional] Bandwidth (default: all the data / global).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdd_reg_lm: not implemented. The method card is in ./README.md."
    )


def wrap_rdd_reg_np(
    *,
    rdd_object: Any,
    bw: float | None = None,
    slope: Literal["separate", "same"] | None = None,
    inference: Literal["np", "lm"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdd_reg_np`` -- METHOD-SELECTION card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object (SHARP only).
        bw: [number, optional] Bandwidth (default: IK optimal).
        slope: [enum, optional] Slope on each side of the cutpoint (default separate).
        inference: [enum, optional] Inference type (default np).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdd_reg_np: not implemented. The method card is in ./README.md."
    )


def wrap_rdd_bw_ik(
    *,
    rdd_object: Any,
    kernel: Literal["Triangular", "Uniform", "Normal"] | None = None,
) -> dict[str, Any]:
    """Node ``wrap_rdd_bw_ik`` -- METHOD-SELECTION card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object.
        kernel: [enum, optional] Kernel for the IK bandwidth (default Triangular).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "wrap_rdd_bw_ik: not implemented. The method card is in ./README.md."
    )
