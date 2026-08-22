# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lgd_ead`` -- method card #351.

#351 Loss given default and exposure at default models

Category 41-credit-risk-default; module ``lgd_ead``.

Reference implementation: statsmodels.

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
    "cr_ead_model",
    "cr_lgd_model",
    "NODE_META",
    "wire_model",
]


def cr_lgd_model(
    *,
    data: pd.DataFrame,
    lgd: str,
    covariates: Sequence[str] | None = None,
    model: Literal["beta", "fractional", "two_part", "tobit", "linear"] | None = None,
    downturn: str | None = None,
) -> dict[str, Any]:
    """Node ``cr_lgd_model`` -- method card #351.

    Loss given default and exposure at default models.

    Category 41-credit-risk-default; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table of resolved defaults.
        lgd: [string, required] Column holding realised loss given default.
        covariates: [series_codes, optional] Covariate columns.
        model: [enum, optional] Model family. Default ``'fractional'``.
        downturn: [string, optional] Indicator column marking downturn periods.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_lgd_model: not implemented."
    )


def cr_ead_model(
    *,
    data: pd.DataFrame,
    ccf: str,
    covariates: Sequence[str] | None = None,
    model: Literal["beta", "fractional", "two_part", "linear"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_ead_model`` -- method card #351.

    Loss given default and exposure at default models.

    Category 41-credit-risk-default; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Table of resolved defaults.
        ccf: [string, required] Column holding the realised credit conversion factor.
        covariates: [series_codes, optional] Covariate columns.
        model: [enum, optional] Model family. Default ``'fractional'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "cr_ead_model: not implemented."
    )
