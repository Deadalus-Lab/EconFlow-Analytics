# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``bayes_factors_rope`` -- method card #508.

#508 Bayes factors, Savage-Dickey ratios and ROPE decisions

Category 14-bayesian-toolkit; module ``bayes_factors_rope``.

Reference implementation: arviz.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c14_bayesian_toolkit import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bt_bayes_factor",
    "bt_rope",
    "NODE_META",
    "wire_model",
]


def bt_bayes_factor(
    *,
    fit: Any,
    parameter: str,
    null_value: float | None = None,
    method: Literal["savage_dickey", "bridge_sampling"] | None = None,
) -> dict[str, Any]:
    """Node ``bt_bayes_factor`` -- method card #508.

    Bayes factors, Savage-Dickey ratios and ROPE decisions.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Bayesian model.
        parameter: [string, required] Parameter tested.
        null_value: [number, optional] Null value. Default ``0.0``.
        method: [enum, optional] Method. Default ``'savage_dickey'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_bayes_factor: not implemented."
    )


def bt_rope(
    *,
    fit: Any,
    parameter: str,
    rope: Sequence[float],
    hdi_prob: float | None = None,
) -> dict[str, Any]:
    """Node ``bt_rope`` -- method card #508.

    Bayes factors, Savage-Dickey ratios and ROPE decisions.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted Bayesian model.
        parameter: [string, required] Parameter assessed.
        rope: [num_array, required] Bounds of the region of practical equivalence.
        hdi_prob: [number, optional] Credible interval mass. Default ``0.94``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_rope: not implemented."
    )
