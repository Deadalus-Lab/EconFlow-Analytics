# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``rdd`` -- method card #39.

#39 RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only)

Category 07-causality-policy; module ``rdd``.

Reference implementation: 10.1093/restud/rdr043.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "rd_bandwidth_ik",
    "rd_prepare_data",
    "rd_reg_nonparametric",
    "rd_reg_parametric",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def rd_prepare_data(
    *,
    y: Any,
    x: Any,
    cutpoint: float,
    z: Any | None = None,
) -> dict[str, Any]:
    """Node ``rd_prepare_data`` -- method card #39.

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
        "rd_prepare_data: not implemented."
    )


def rd_reg_parametric(
    *,
    rdd_object: Any,
    order: int | None = None,
    slope: Literal["separate", "same"] | None = None,
    bw: float | None = None,
) -> dict[str, Any]:
    """Node ``rd_reg_parametric`` -- method card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object (from rd_prepare_data).
        order: [integer, optional] Polynomial degree (default 1). Default ``1``.
        slope: [enum, optional] Slope on each side of the cutpoint (default separate).
        bw: [number, optional] Bandwidth (default: all the data / global).

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
        "rd_reg_parametric: not implemented."
    )


def rd_reg_nonparametric(
    *,
    rdd_object: Any,
    bw: float | None = None,
    slope: Literal["separate", "same"] | None = None,
    inference: Literal["np", "lm"] | None = None,
) -> dict[str, Any]:
    """Node ``rd_reg_nonparametric`` -- method card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object (SHARP only).
        bw: [number, optional] Bandwidth (default: IK optimal).
        slope: [enum, optional] Slope on each side of the cutpoint (default separate).
        inference: [enum, optional] Inference type (default np).

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
        "rd_reg_nonparametric: not implemented."
    )


def rd_bandwidth_ik(
    *,
    rdd_object: Any,
    kernel: Literal["Triangular", "Uniform", "Normal"] | None = None,
) -> dict[str, Any]:
    """Node ``rd_bandwidth_ik`` -- method card #39.

    RDD (IK bandwidth, object-oriented; fuzzy->rdd_reg_lm only).

    Category 07-causality-policy; memory class ``light``.

    Args:
        rdd_object: [raw_handle, required] Handle to an rdd_data object.
        kernel: [enum, optional] Kernel for the IK bandwidth (default Triangular).

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
        "rd_bandwidth_ik: not implemented."
    )
