# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``nongaussian_identification`` -- method card #425.

#425 Non-Gaussian higher-moment identification

Category 04-structural-shocks; module ``nongaussian_identification``.

Reference implementation: SVARpy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c04_structural_shocks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ss_nongaussian_svar",
    "ss_nongaussianity_diagnostics",
    "NODE_META",
    "wire_model",
]


def ss_nongaussian_svar(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    moments: Literal["third", "fourth", "third_and_fourth"] | None = None,
    horizons: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_nongaussian_svar`` -- method card #425.

    Non-Gaussian higher-moment identification.

    Category 04-structural-shocks; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] VAR lag order. Default ``4``.
        moments: [enum, optional] Moments used for identification. Default ``'third_and_fourth'``.
        horizons: [integer, optional] Impulse-response horizon. Default ``20``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ss_nongaussian_svar: not implemented."
    )


def ss_nongaussianity_diagnostics(
    *,
    y: pd.DataFrame,
    lags: int | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ss_nongaussianity_diagnostics`` -- method card #425.

    Non-Gaussian higher-moment identification.

    Category 04-structural-shocks; memory class ``light``.

    Args:
        y: [multiseries_handle, required] Endogenous variables.
        lags: [integer, optional] VAR lag order. Default ``4``.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ss_nongaussianity_diagnostics: not implemented."
    )
