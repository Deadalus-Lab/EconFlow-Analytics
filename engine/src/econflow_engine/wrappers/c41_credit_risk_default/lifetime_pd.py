# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lifetime_pd`` -- method card #352.

#352 Time-to-default hazard models and lifetime PD term structures

Category 41-credit-risk-default; module ``lifetime_pd``.

Reference implementation: lifelines.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_lifetime_pd",
    "cr_pd_scenario",
    "NODE_META",
    "wire_model",
]


def cr_lifetime_pd(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    horizon: int | None = None,
    model: Literal["cox", "discrete_cloglog", "weibull", "piecewise"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_lifetime_pd`` -- method card #352.

    Time-to-default hazard models and lifetime PD term structures.

    Category 41-credit-risk-default; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Person-period or duration table.
        time: [string, required] Column holding the duration or period index.
        event: [string, required] Column holding the default indicator.
        covariates: [series_codes, optional] Covariate columns.
        horizon: [integer, optional] Lifetime horizon in periods. Default ``10``.
        model: [enum, optional] Hazard model family. Default ``'cox'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_lifetime_pd: not implemented."
    )


def cr_pd_scenario(
    *,
    fit: Any,
    scenarios: pd.DataFrame,
    weights: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``cr_pd_scenario`` -- method card #352.

    Time-to-default hazard models and lifetime PD term structures.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted lifetime PD model.
        scenarios: [df_handle, required] Macroeconomic scenario paths.
        weights: [num_array, optional] Scenario probability weights.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_pd_scenario: not implemented."
    )
