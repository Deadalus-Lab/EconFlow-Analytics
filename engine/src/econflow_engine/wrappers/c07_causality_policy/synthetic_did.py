# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synthetic_did`` -- method card #444.

#444 Synthetic difference-in-differences

Category 07-causality-policy; module ``synthetic_did``.

Reference implementation: sdid.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_synthetic_did",
    "NODE_META",
    "wire_model",
]


def cp_synthetic_did(
    *,
    data: pd.DataFrame,
    outcome: str,
    unit: str,
    time: str,
    treatment: str,
    inference: Literal["placebo", "jackknife", "bootstrap"] | None = None,
    nboot: int | None = None,
    seed: int,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_synthetic_did`` -- method card #444.

    Synthetic difference-in-differences.

    Category 07-causality-policy; memory class ``heavy``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Panel data.
        outcome: [string, required] Outcome column.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        treatment: [string, required] Treatment indicator column.
        inference: [enum, optional] Inference method. Default ``'placebo'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cp_synthetic_did: not implemented."
    )
