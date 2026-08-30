# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``stress_scenarios`` -- method card #497.

#497 Stress-scenario design: historical, hypothetical and reverse

Category 12-distribution-risk; module ``stress_scenarios``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dr_reverse_stress",
    "dr_stress_scenarios",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dr_stress_scenarios(
    *,
    factors: pd.DataFrame,
    method: (
        Literal[
            "historical",
            "hypothetical",
            "worst_case",
            "principal_component",
        ]
        | None
    ) = None,
    episode: str | None = None,
    severity: float | None = None,
    n_scenarios: int | None = None,
) -> dict[str, Any]:
    """Node ``dr_stress_scenarios`` -- method card #497.

    Stress-scenario design: historical, hypothetical and reverse.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        factors: [df_handle, required] Risk-factor history.
        method: [enum, optional] Scenario construction. Default ``'historical'``.
        episode: [string, optional] Historical episode to replay.
        severity: [number, optional] Severity in standard deviations. Default ``3.0``.
        n_scenarios: [integer, optional] Scenarios to generate. Default ``10``.

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
        "dr_stress_scenarios: not implemented."
    )


def dr_reverse_stress(
    *,
    factors: pd.DataFrame,
    exposures: pd.Series,
    target_loss: float,
) -> dict[str, Any]:
    """Node ``dr_reverse_stress`` -- method card #497.

    Stress-scenario design: historical, hypothetical and reverse.

    Category 12-distribution-risk; memory class ``light``.

    Args:
        factors: [df_handle, required] Risk-factor history.
        exposures: [series_handle, required] Portfolio sensitivities to the factors.
        target_loss: [number, required] Loss level to explain.

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
        "dr_reverse_stress: not implemented."
    )
