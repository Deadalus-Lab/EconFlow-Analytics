# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``identification`` -- method card #377.

#377 Graph identification: backdoor, frontdoor, instruments and estimand derivation

Category 45-causal-discovery-graphs; module ``identification``.

Reference implementation: dowhy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c45_causal_discovery_graphs import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cd_adjustment_sets",
    "cd_estimate_effect",
    "cd_identify_effect",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cd_identify_effect(
    *,
    graph: str,
    treatment: str,
    outcome: str,
    method: Literal["auto", "backdoor", "frontdoor", "iv", "mediation"] | None = None,
) -> dict[str, Any]:
    """Node ``cd_identify_effect`` -- method card #377.

    Graph identification: backdoor, frontdoor, instruments and estimand derivation.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Registers its result under ``estimand``, so a later node can consume it as a handle.

    Args:
        graph: [string, required] Causal graph in DOT or GML form.
        treatment: [string, required] Treatment variable.
        outcome: [string, required] Outcome variable.
        method: [enum, optional] Identification strategy to attempt. Default ``'auto'``.

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
        "cd_identify_effect: not implemented."
    )


def cd_adjustment_sets(
    *,
    graph: str,
    treatment: str,
    outcome: str,
    max_sets: int | None = None,
) -> dict[str, Any]:
    """Node ``cd_adjustment_sets`` -- method card #377.

    Graph identification: backdoor, frontdoor, instruments and estimand derivation.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        graph: [string, required] Causal graph in DOT or GML form.
        treatment: [string, required] Treatment variable.
        outcome: [string, required] Outcome variable.
        max_sets: [integer, optional] Maximum sets to return. Default ``10``.

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
        "cd_adjustment_sets: not implemented."
    )


def cd_estimate_effect(
    *,
    estimand: Any,
    data: pd.DataFrame,
    method: (
        Literal[
            "linear_regression",
            "propensity_matching",
            "propensity_weighting",
            "instrumental_variable",
            "two_stage_regression",
        ]
        | None
    ) = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cd_estimate_effect`` -- method card #377.

    Graph identification: backdoor, frontdoor, instruments and estimand derivation.

    Category 45-causal-discovery-graphs; memory class ``light``.

    Args:
        estimand: [raw_handle, required] Handle to a derived estimand.
        data: [df_handle, required] Data to estimate on.
        method: [enum, optional] Estimator. Default ``'linear_regression'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "cd_estimate_effect: not implemented."
    )
