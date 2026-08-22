# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``competing_risks`` -- method card #262.

#262 Competing risks: cause-specific hazards, cumulative incidence and the Fine-Gray subdistribution
    model

Category 30-duration-survival; module ``competing_risks``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c30_duration_survival import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "srv_cause_specific",
    "srv_cif_fit",
    "srv_finegray_fit",
    "srv_gray_test",
    "NODE_META",
    "wire_model",
]


def srv_cif_fit(
    *,
    time: pd.Series,
    event: pd.Series,
    weights: pd.Series | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_cif_fit`` -- method card #262.

    Competing risks: cause-specific hazards, cumulative incidence and the Fine-Gray subdistribution
    model.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration.
        event: [series_handle, required] Cause code: 0 = censored, 1..K = the competing causes.
        weights: [series_handle, optional] Optional observation weights.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_cif_fit: not implemented."
    )


def srv_cause_specific(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    cause: int,
    covariates: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``srv_cause_specific`` -- method card #262.

    Competing risks: cause-specific hazards, cumulative incidence and the Fine-Gray subdistribution
    model.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table holding durations, the cause code and covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the cause code.
        cause: [integer, required] The cause to model; all others are treated as censoring.
        covariates: [series_codes, optional] Covariate column names.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_cause_specific: not implemented."
    )


def srv_finegray_fit(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    cause: int,
    covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``srv_finegray_fit`` -- method card #262.

    Competing risks: cause-specific hazards, cumulative incidence and the Fine-Gray subdistribution
    model.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table holding durations, the cause code and covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the cause code.
        cause: [integer, required] The cause whose cumulative incidence is modelled.
        covariates: [series_codes, optional] Covariate column names.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_finegray_fit: not implemented."
    )


def srv_gray_test(
    *,
    time: pd.Series,
    event: pd.Series,
    group: pd.Series,
    cause: int,
) -> dict[str, Any]:
    """Node ``srv_gray_test`` -- method card #262.

    Competing risks: cause-specific hazards, cumulative incidence and the Fine-Gray subdistribution
    model.

    Category 30-duration-survival; memory class ``light``.

    Args:
        time: [series_handle, required] Observed duration.
        event: [series_handle, required] Cause code.
        group: [series_handle, required] Group label.
        cause: [integer, required] The cause being compared.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_gray_test: not implemented."
    )
