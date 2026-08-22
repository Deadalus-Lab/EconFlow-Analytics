# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``dynamic_ardl_ecm`` -- method card #26.

#26 Dynamic ARDL/ECM + stochastic simulation + PSS bounds + residual diagnostics

Category 05-cointegration; module ``dynamic_ardl_ecm``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dyn_ardl",
    "dyn_autocorr",
    "dyn_pss_bounds",
    "NODE_META",
    "wire_model",
]


def dyn_ardl(
    *,
    formula: str,
    data: pd.DataFrame,
    diffs: Sequence[str] | None = None,
    levels: Sequence[str] | None = None,
    ec: bool | None = None,
    trend: bool | None = None,
    constant: bool | None = None,
    simulate: bool | None = None,
    shockvar: str | None = None,
    sims: int | None = None,
    range: int | None = None,
) -> dict[str, Any]:
    """Node ``dyn_ardl`` -- method card #26.

    Dynamic ARDL/ECM + stochastic simulation + PSS bounds + residual diagnostics.

    Category 05-cointegration; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] ARDL/ECM formula (e.g. 'y ~ x1 + x2').
        data: [df_handle, required] Handle to a DataFrame (NOT ts; dynardl builds lags/diffs on its
            own).
        diffs: [series_codes, optional] Variable names in first differences (array of strings).
        levels: [series_codes, optional] Variable names in levels (array of strings).
        ec: [boolean, optional] True = error-correction parameterization (required for
            dyn_pss_bounds). Default ``False``.
        trend: [boolean, optional] True = deterministic trend (default False). Default ``False``.
        constant: [boolean, optional] True = constant term (default True). Default ``True``.
        simulate: [boolean, optional] True = stochastic simulation of the counterfactual response
            (chart-data). Default ``False``.
        shockvar: [string, optional] Variable to shock (required when simulate=True; one of the
            RHS).
        sims: [integer, optional] Monte Carlo replications of the simulation (default 1000). Default
            ``1000``.
        range: [integer, optional] Horizon of the response path (default 20). Default ``20``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dyn_ardl: not implemented."
    )


def dyn_pss_bounds(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``dyn_pss_bounds`` -- method card #26.

    Dynamic ARDL/ECM + stochastic simulation + PSS bounds + residual diagnostics.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'dynardl' estimated with ec=True (from dyn_ardl).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dyn_pss_bounds: not implemented."
    )


def dyn_autocorr(
    *,
    object: Any,
    bg_type: Literal["Chisq", "F"] | None = None,
    order: int | None = None,
) -> dict[str, Any]:
    """Node ``dyn_autocorr`` -- method card #26.

    Dynamic ARDL/ECM + stochastic simulation + PSS bounds + residual diagnostics.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a 'dynardl' model (from dyn_ardl).
        bg_type: [enum, optional] Breusch-Godfrey statistic (default Chisq).
        order: [integer, optional] AR order of the autocorrelation test (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dyn_autocorr: not implemented."
    )
