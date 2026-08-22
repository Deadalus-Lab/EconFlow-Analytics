# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``disagreement_uncertainty`` -- method card #575.

#575 Disagreement and uncertainty from density forecasts

Category 25-expectations-surveys; module ``disagreement_uncertainty``.

Reference implementation: scoringrules.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_disagreement_uncertainty",
    "NODE_META",
    "wire_model",
]


def es_disagreement_uncertainty(
    *,
    densities: pd.DataFrame,
    respondent: str,
    period: str,
    balanced: bool | None = None,
) -> dict[str, Any]:
    """Node ``es_disagreement_uncertainty`` -- method card #575.

    Disagreement and uncertainty from density forecasts.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        densities: [df_handle, required] Fitted individual densities or their moments.
        respondent: [string, required] Respondent identifier.
        period: [string, required] Survey period.
        balanced: [boolean, optional] Restrict to a balanced respondent panel. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_disagreement_uncertainty: not implemented."
    )
