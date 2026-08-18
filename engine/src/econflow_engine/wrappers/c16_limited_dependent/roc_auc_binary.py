# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``roc_auc_binary`` -- METHOD-SELECTION card #84.

#84 ROC / AUC — binary forecast evaluation

Category 16-limited-dependent; module ``roc_auc_binary``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_roc",
    "NODE_META",
    "wire_model",
]


def run_roc(
    *,
    response: Any,
    predictor: Any,
    direction: Literal["auto", "<", ">"] | None = None,
    ci: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``run_roc`` -- METHOD-SELECTION card #84.

    ROC / AUC — binary forecast evaluation.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        response: [raw_handle, required] Handle to a binary target (logical, numeric 0/1 or
            categorical/string with 2 levels).
        predictor: [raw_handle, required] Handle to a numeric score/prediction (e.g. the
            fitted_probabilities of #83), of the same length as the response.
        direction: [enum, optional] Relation of controls to cases (default auto· '<' = normal
            prob-score).
        ci: [boolean, optional] Computation of the DeLong CI of the AUC (default True). Default
            ``True``.
        conf_level: [number, optional] Confidence level of the CI of the AUC, in (0,1) (default
            0.95). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "run_roc: not implemented. The method card is in ./README.md."
    )
