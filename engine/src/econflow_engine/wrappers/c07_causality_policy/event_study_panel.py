# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``event_study_panel`` -- method card #454.

#454 Panel event-study construction and pre-trend testing

Category 07-causality-policy; module ``event_study_panel``.

Reference implementation: paneleventstudy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_event_study",
    "cp_pretrend_test",
    "NODE_META",
    "wire_model",
]


def cp_event_study(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    event_time: str,
    window: Sequence[int] | None = None,
    base_period: int | None = None,
    bin_endpoints: bool | None = None,
    cluster: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_event_study`` -- method card #454.

    Panel event-study construction and pre-trend testing.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        outcome: [string, required] Outcome column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        event_time: [string, required] Column holding the treatment date per unit.
        window: [int_array, optional] Relative-period window. Default ``[-5, 5]``.
        base_period: [integer, optional] Omitted relative period. Default ``-1``.
        bin_endpoints: [boolean, optional] Bin periods beyond the window. Default ``True``.
        cluster: [string, optional] Clustering variable.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_event_study: not implemented."
    )


def cp_pretrend_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_pretrend_test`` -- method card #454.

    Panel event-study construction and pre-trend testing.

    Category 07-causality-policy; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted event study.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_pretrend_test: not implemented."
    )
