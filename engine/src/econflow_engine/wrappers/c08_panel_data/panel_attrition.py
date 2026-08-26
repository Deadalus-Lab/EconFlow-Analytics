# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_attrition`` -- method card #467.

#467 Attrition tests and inverse probability weighting for unbalanced panels

Category 08-panel-data; module ``panel_attrition``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_attrition_test",
    "pd_attrition_weights",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_attrition_test(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    covariates: Sequence[str] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_attrition_test`` -- method card #467.

    Attrition tests and inverse probability weighting for unbalanced panels.

    Category 08-panel-data; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        outcome: [string, required] Outcome column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        covariates: [series_codes, optional] Covariates entering the retention model.
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
        "pd_attrition_test: not implemented."
    )


def pd_attrition_weights(
    *,
    data: pd.DataFrame,
    unit: str,
    time: str,
    covariates: Sequence[str] | None = None,
    stabilised: bool | None = None,
) -> dict[str, Any]:
    """Node ``pd_attrition_weights`` -- method card #467.

    Attrition tests and inverse probability weighting for unbalanced panels.

    Category 08-panel-data; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        covariates: [series_codes, optional] Covariates entering the retention model.
        stabilised: [boolean, optional] Use stabilised weights. Default ``True``.

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
        "pd_attrition_weights: not implemented."
    )
