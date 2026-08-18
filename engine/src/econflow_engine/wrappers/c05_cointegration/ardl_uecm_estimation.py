# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ardl_uecm_estimation`` -- METHOD-SELECTION card #25.

#25 ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq

Category 05-cointegration; module ``ardl_uecm_estimation``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ardl_auto",
    "ardl_bounds_f",
    "ardl_bounds_t",
    "ardl_coint_eq",
    "ardl_fit",
    "ardl_multipliers",
    "ardl_recm",
    "NODE_META",
    "wire_model",
]


def ardl_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    order: int,
) -> dict[str, Any]:
    """Node ``ardl_fit`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] ARDL formula (e.g. 'y ~ x1 + x2').
        data: [df_handle, required] Handle to a DataFrame or series handle carrying the formula's
            variables.
        order: [integer, required] Lag orders per variable; vector of non-negative integers of
            length #vars.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_fit: not implemented. The method card is in ./README.md."
    )


def ardl_auto(
    *,
    formula: str,
    data: pd.DataFrame,
    max_order: int,
    selection: str | None = None,
    selection_minmax: Literal["min", "max"] | None = None,
    grid: bool | None = None,
) -> dict[str, Any]:
    """Node ``ardl_auto`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] ARDL formula (e.g. 'y ~ x1 + x2').
        data: [df_handle, required] Handle to a DataFrame or series handle carrying the formula's
            variables.
        max_order: [integer, required] Maximum lag for the search; positive integer (or vector).
        selection: [string, optional] Selection criterion (AIC/BIC/R2/adjR2/...) (default AIC).
            Default ``'AIC'``.
        selection_minmax: [enum, optional] Optimization direction of the criterion (default min).
        grid: [boolean, optional] True = exhaustive grid search (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_auto: not implemented. The method card is in ./README.md."
    )


def ardl_bounds_f(
    *,
    object: Any,
    case: int,
    test: Literal["F", "Chisq"] | None = None,
    n_replications: int | None = None,
) -> dict[str, Any]:
    """Node ``ardl_bounds_f`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).
        case: [integer, required] PSS case of deterministic terms; integer 1..5.
        test: [enum, optional] Bounds statistic (default F).
        n_replications: [integer, optional] Simulation replications of the p-value (default 40000).
            Default ``40000``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_bounds_f: not implemented. The method card is in ./README.md."
    )


def ardl_bounds_t(
    *,
    object: Any,
    case: int,
    n_replications: int | None = None,
) -> dict[str, Any]:
    """Node ``ardl_bounds_t`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).
        case: [integer, required] PSS case of deterministic terms; integer 1..5.
        n_replications: [integer, optional] Simulation replications of the p-value (default 40000).
            Default ``40000``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_bounds_t: not implemented. The method card is in ./README.md."
    )


def ardl_recm(
    *,
    object: Any,
    case: int,
) -> dict[str, Any]:
    """Node ``ardl_recm`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).
        case: [integer, required] PSS case of deterministic terms; integer 1..5.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_recm: not implemented. The method card is in ./README.md."
    )


def ardl_multipliers(
    *,
    object: Any,
    type: str | None = None,
    se: bool | None = None,
) -> dict[str, Any]:
    """Node ``ardl_multipliers`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).
        type: [string, optional] 'lr' (long-run, default), 'sr' (short-run), or a non-negative
            integer (interim). Default ``'lr'``.
        se: [boolean, optional] True = return standard errors (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_multipliers: not implemented. The method card is in ./README.md."
    )


def ardl_coint_eq(
    *,
    object: Any,
    case: int,
) -> dict[str, Any]:
    """Node ``ardl_coint_eq`` -- METHOD-SELECTION card #25.

    ARDL / UECM estimation + PSS bounds F/t-test + RECM + multipliers + coint_eq.

    Category 05-cointegration; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to an 'ardl'/'uecm' model (from ardl_fit/ardl_auto).
        case: [integer, required] PSS case of deterministic terms; integer 1..5.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ardl_coint_eq: not implemented. The method card is in ./README.md."
    )
