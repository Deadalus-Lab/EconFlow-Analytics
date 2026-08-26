# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``constraint_discovery`` -- method card #374.

#374 Constraint-based structure learning: PC and FCI

Category 45-causal-discovery-graphs; module ``constraint_discovery``.

Reference implementation: causal-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_fci",
    "cd_pc",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cd_pc(
    *,
    data: pd.DataFrame,
    independence_test: Literal["fisherz", "chisq", "gsq", "kci", "mv_fisherz"] | None = None,
    stable: bool | None = None,
    max_conditioning_set: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cd_pc`` -- method card #374.

    Constraint-based structure learning: PC and FCI.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        data: [df_handle, required] Observational data.
        independence_test: [enum, optional] Conditional independence test. Default ``'fisherz'``.
        stable: [boolean, optional] Use the order-independent stable variant. Default ``True``.
        max_conditioning_set: [integer, optional] Largest conditioning set considered.
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
        "cd_pc: not implemented."
    )


def cd_fci(
    *,
    data: pd.DataFrame,
    independence_test: Literal["fisherz", "chisq", "gsq", "kci"] | None = None,
    max_conditioning_set: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cd_fci`` -- method card #374.

    Constraint-based structure learning: PC and FCI.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        data: [df_handle, required] Observational data.
        independence_test: [enum, optional] Conditional independence test. Default ``'fisherz'``.
        max_conditioning_set: [integer, optional] Largest conditioning set considered.
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
        "cd_fci: not implemented."
    )
