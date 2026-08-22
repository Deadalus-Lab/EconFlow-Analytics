# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``agreement_measures`` -- method card #578.

#578 Ordinal and rank agreement: Kendall W, kappa, Cronbach alpha and polychoric

Category 25-expectations-surveys; module ``agreement_measures``.

Reference implementation: pingouin.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "es_agreement",
    "es_polychoric",
    "NODE_META",
    "wire_model",
]


def es_agreement(
    *,
    data: pd.DataFrame,
    measure: (
        Literal[
            "kendall_w",
            "cohen_kappa",
            "fleiss_kappa",
            "cronbach_alpha",
            "icc",
        ]
        | None
    ) = None,
    nboot: int | None = None,
    seed: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``es_agreement`` -- method card #578.

    Ordinal and rank agreement: Kendall W, kappa, Cronbach alpha and polychoric.

    Category 25-expectations-surveys; memory class ``heavy``.

    Args:
        data: [df_handle, required] Ratings: items by raters.
        measure: [enum, optional] Measure. Default ``'kendall_w'``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``1000``.
        seed: [integer, optional] Seed for the random number generator.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_agreement: not implemented."
    )


def es_polychoric(
    *,
    data: pd.DataFrame,
    method: Literal["two_step", "mle"] | None = None,
) -> dict[str, Any]:
    """Node ``es_polychoric`` -- method card #578.

    Ordinal and rank agreement: Kendall W, kappa, Cronbach alpha and polychoric.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Ordinal item responses.
        method: [enum, optional] Estimator. Default ``'two_step'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "es_polychoric: not implemented."
    )
