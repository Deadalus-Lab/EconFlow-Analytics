# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fixed_effects_ols`` -- METHOD-SELECTION card #33.

#33 Fixed-effects OLS/IV + event study

Category 07-causality-policy; module ``fixed_effects_ols``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fx_coeftable",
    "fx_confint",
    "fx_feols",
    "fx_fitstat",
    "fx_vcov",
    "NODE_META",
    "wire_model",
]


def fx_feols(
    *,
    fml: str,
    data: pd.DataFrame,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_feols`` -- METHOD-SELECTION card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        fml: [formula, required] Formula, e.g. 'y ~ x1 + x2 | unit + time' (FE after the |; IV: |
            endo ~ inst).
        data: [df_handle, required] Handle to a DataFrame (panel/cross-section).
        vcov: [string, optional] vcov type, e.g. 'hetero' or 'cluster' (default: iid/by FE).
        cluster: [string, optional] Clustering variable name (or formula string) for robust SE.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fx_feols: not implemented. The method card is in ./README.md."
    )


def fx_coeftable(
    *,
    object: Any,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_coeftable`` -- METHOD-SELECTION card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_feols).
        vcov: [string, optional] Recompute SE with a different vcov without re-fitting.
        cluster: [string, optional] Clustering variable for the SE.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fx_coeftable: not implemented. The method card is in ./README.md."
    )


def fx_confint(
    *,
    object: Any,
    level: float | None = None,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_confint`` -- METHOD-SELECTION card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_feols).
        level: [number, optional] Confidence level in (0,1) (default 0.95). Default ``0.95``.
        vcov: [string, optional] Alternative vcov for the intervals.
        cluster: [string, optional] Clustering variable.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fx_confint: not implemented. The method card is in ./README.md."
    )


def fx_vcov(
    *,
    object: Any,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_vcov`` -- METHOD-SELECTION card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_feols).
        vcov: [string, optional] vcov type (e.g. 'hetero','cluster').
        cluster: [string, optional] Clustering variable.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fx_vcov: not implemented. The method card is in ./README.md."
    )


def fx_fitstat(
    *,
    object: Any,
    type: str,
    vcov: str | None = None,
    cluster: str | None = None,
) -> dict[str, Any]:
    """Node ``fx_fitstat`` -- METHOD-SELECTION card #33.

    Fixed-effects OLS/IV + event study.

    Category 07-causality-policy; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fixest model (from fx_feols).
        type: [string, required] Statistic/test (required): e.g. 'r2','rmse','f','wald','ivwald'.
        vcov: [string, optional] Alternative vcov for test statistics.
        cluster: [string, optional] Clustering variable.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "fx_fitstat: not implemented. The method card is in ./README.md."
    )
