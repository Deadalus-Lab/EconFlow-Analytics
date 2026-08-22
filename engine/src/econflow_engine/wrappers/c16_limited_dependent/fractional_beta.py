# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fractional_beta`` -- method card #527.

#527 Fractional response and beta regression

Category 16-limited-dependent; module ``fractional_beta``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_fractional_response",
    "NODE_META",
    "wire_model",
]


def ld_fractional_response(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["fractional", "beta", "zero_one_inflated_beta"] | None = None,
    link: Literal["logit", "probit", "cloglog", "loglog"] | None = None,
    precision_covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_fractional_response`` -- method card #527.

    Fractional response and beta regression.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Bounded outcome.
        x: [df_handle, required] Covariate table.
        model: [enum, optional] Model. Default ``'fractional'``.
        link: [enum, optional] Link function. Default ``'logit'``.
        precision_covariates: [series_codes, optional] Covariates modelling the precision parameter.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ld_fractional_response: not implemented."
    )
