# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``frailty`` -- method card #263.

#263 Frailty and shared-frailty models for unobserved heterogeneity

Category 30-duration-survival; module ``frailty``.

Reference implementation: lifelines.

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
    "srv_frailty_fit",
    "srv_frailty_test",
    "NODE_META",
    "wire_model",
]


def srv_frailty_fit(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    cluster: str,
    frailty: Literal["gamma", "lognormal", "inverse_gaussian"] | None = None,
) -> dict[str, Any]:
    """Node ``srv_frailty_fit`` -- method card #263.

    Frailty and shared-frailty models for unobserved heterogeneity.

    Category 30-duration-survival; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table holding durations, the event indicator and covariates.
        time: [string, required] Column holding the observed duration.
        event: [string, required] Column holding the event indicator.
        covariates: [series_codes, optional] Covariate column names.
        cluster: [string, required] Column identifying the frailty group.
        frailty: [enum, optional] Distribution of the shared frailty term. Default ``'gamma'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_frailty_fit: not implemented."
    )


def srv_frailty_test(
    *,
    fit: Any,
) -> dict[str, Any]:
    """Node ``srv_frailty_test`` -- method card #263.

    Frailty and shared-frailty models for unobserved heterogeneity.

    Category 30-duration-survival; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted frailty model.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "srv_frailty_test: not implemented."
    )
