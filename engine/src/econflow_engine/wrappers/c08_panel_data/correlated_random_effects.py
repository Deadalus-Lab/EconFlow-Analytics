# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``correlated_random_effects`` -- method card #458.

#458 Correlated random effects: Mundlak and Hausman-Taylor

Category 08-panel-data; module ``correlated_random_effects``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_correlated_random_effects",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_correlated_random_effects(
    *,
    data: pd.DataFrame,
    formula: str,
    unit: str,
    time: str,
    estimator: Literal["mundlak", "hausman_taylor", "random_effects"] | None = None,
    exogenous: Sequence[str] | None = None,
    time_invariant: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_correlated_random_effects`` -- method card #458.

    Correlated random effects: Mundlak and Hausman-Taylor.

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        formula: [formula, required] Model formula.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        estimator: [enum, optional] Estimator. Default ``'mundlak'``.
        exogenous: [series_codes, optional] Regressors assumed exogenous for Hausman-Taylor.
        time_invariant: [series_codes, optional] Time-invariant regressors.
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
        "pd_correlated_random_effects: not implemented."
    )
