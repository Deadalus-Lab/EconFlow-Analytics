# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ph_diagnostics`` -- method card #264.

#264 Proportional-hazards diagnostics: Schoenfeld residuals and time-interaction tests

Category 30-duration-survival; module ``ph_diagnostics``.

Reference implementation: lifelines.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_cox_residuals",
    "srv_ph_test",
    "srv_schoenfeld",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def srv_schoenfeld(
    *,
    fit: Any,
    transform: Literal["identity", "log", "rank", "km"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_schoenfeld`` -- method card #264.

    Proportional-hazards diagnostics: Schoenfeld residuals and time-interaction tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Cox model.
        transform: [enum, optional] Time transform applied before the test. Default ``'km'``.

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
        "srv_schoenfeld: not implemented."
    )


def srv_ph_test(
    *,
    fit: Any,
    transform: Literal["identity", "log", "rank", "km"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_ph_test`` -- method card #264.

    Proportional-hazards diagnostics: Schoenfeld residuals and time-interaction tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Cox model.
        transform: [enum, optional] Time transform applied before the test. Default ``'km'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "srv_ph_test: not implemented."
    )


def srv_cox_residuals(
    *,
    fit: Any,
    kind: Literal["martingale", "deviance", "score", "dfbeta"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_cox_residuals`` -- method card #264.

    Proportional-hazards diagnostics: Schoenfeld residuals and time-interaction tests.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Cox model.
        kind: [enum, optional] Residual type. Default ``'martingale'``.

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
        "srv_cox_residuals: not implemented."
    )
