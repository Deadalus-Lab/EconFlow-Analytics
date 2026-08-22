# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``prior_elicitation`` -- method card #510.

#510 Prior elicitation and prior-predictive checks

Category 14-bayesian-toolkit; module ``prior_elicitation``.

Reference implementation: preliz.

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
    "bt_elicit_prior",
    "bt_prior_predictive",
    "NODE_META",
    "wire_model",
]


def bt_prior_predictive(
    *,
    model: Any,
    draws: int | None = None,
    checks: Sequence[str] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``bt_prior_predictive`` -- method card #510.

    Prior elicitation and prior-predictive checks.

    Category 14-bayesian-toolkit; memory class ``mcmc``.

    Args:
        model: [raw, required] Model specification.
        draws: [integer, optional] Prior draws. Default ``1000``.
        checks: [series_codes, optional] Summaries to compute on the simulated data.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_prior_predictive: not implemented."
    )


def bt_elicit_prior(
    *,
    quantiles: Sequence[float],
    values: Sequence[float],
    family: Literal["auto", "normal", "lognormal", "beta", "gamma", "student_t"] | None = None,
    lower: float | None = None,
    upper: float | None = None,
) -> dict[str, Any]:
    """Node ``bt_elicit_prior`` -- method card #510.

    Prior elicitation and prior-predictive checks.

    Category 14-bayesian-toolkit; memory class ``light``.

    Args:
        quantiles: [num_array, required] Quantile levels.
        values: [num_array, required] Values at those quantiles.
        family: [enum, optional] Distribution family. Default ``'auto'``.
        lower: [number, optional] Hard lower bound.
        upper: [number, optional] Hard upper bound.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "bt_elicit_prior: not implemented."
    )
