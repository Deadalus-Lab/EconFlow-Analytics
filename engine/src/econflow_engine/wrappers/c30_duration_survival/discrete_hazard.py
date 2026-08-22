# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``discrete_hazard`` -- method card #261.

#261 Discrete-time hazard models with complementary log-log and logit links

Category 30-duration-survival; module ``discrete_hazard``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_discrete_expand",
    "srv_discrete_fit",
    "NODE_META",
    "wire_model",
]


def srv_discrete_expand(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    id: str,
) -> dict[str, Any]:
    """Node ``srv_discrete_expand`` -- method card #261.

    Discrete-time hazard models with complementary log-log and logit links.

    Category 30-duration-survival; memory class ``light``.

    Args:
        data: [df_handle, required] One row per unit.
        time: [string, required] Column holding the observed duration in whole intervals.
        event: [string, required] Column holding the event indicator.
        id: [string, required] Column identifying the unit.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_discrete_expand: not implemented."
    )


def srv_discrete_fit(
    *,
    data: pd.DataFrame,
    event: str,
    duration: str,
    covariates: Sequence[str] | None = None,
    link: Literal["cloglog", "logit", "probit"] | None = None,
    baseline: Literal["dummies", "polynomial", "linear", "none"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_discrete_fit`` -- method card #261.

    Discrete-time hazard models with complementary log-log and logit links.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Person-period table: one row per unit per interval at risk.
        event: [string, required] Column holding the within-interval event indicator.
        duration: [string, required] Column holding the interval index.
        covariates: [series_codes, optional] Covariate column names.
        link: [enum, optional] Link function. Default ``'cloglog'``.
        baseline: [enum, optional] How duration dependence enters the model. Default ``'dummies'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_discrete_fit: not implemented."
    )
