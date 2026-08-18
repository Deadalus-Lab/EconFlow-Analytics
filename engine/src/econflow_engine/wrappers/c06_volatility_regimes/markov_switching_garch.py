# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``markov_switching_garch`` -- METHOD-SELECTION card #31.

#31 Markov-switching GARCH

Category 06-volatility-regimes; module ``markov_switching_garch``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "msg_fit_mcmc",
    "msg_fit_ml",
    "msg_predict",
    "msg_risk",
    "msg_sim",
    "msg_spec",
    "msg_state",
    "NODE_META",
    "wire_model",
]


def msg_spec(
    *,
    model: Literal["sGARCH", "sARCH", "eGARCH", "gjrGARCH", "tGARCH"] | None = None,
    distribution: Literal["norm", "snorm", "std", "sstd", "ged", "sged"] | None = None,
    K: int | None = None,
    do_mix: bool | None = None,
) -> dict[str, Any]:
    """Node ``msg_spec`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        model: [enum, optional] Variance model per regime (recycled to K, default sGARCH).
        distribution: [enum, optional] Distribution per regime (recycled to K, default norm).
        K: [integer, optional] Number of regimes (default 2). Default ``2``.
        do_mix: [boolean, optional] Mixture (True) instead of Markov-switching (False, default).
            Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_spec: not implemented. The method card is in ./README.md."
    )


def msg_fit_ml(
    *,
    spec: Any,
    data: pd.Series,
) -> dict[str, Any]:
    """Node ``msg_fit_ml`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        spec: [raw_handle, required] Handle to an 'MSGARCH_SPEC' (from msg_spec).
        data: [series_handle, required] Handle to a univariate numeric series (returns, without NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_fit_ml: not implemented. The method card is in ./README.md."
    )


def msg_fit_mcmc(
    *,
    spec: Any,
    data: pd.Series,
) -> dict[str, Any]:
    """Node ``msg_fit_mcmc`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``heavy``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        spec: [raw_handle, required] Handle to an 'MSGARCH_SPEC' (from msg_spec).
        data: [series_handle, required] Handle to a univariate numeric series (returns, without NA).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_fit_mcmc: not implemented. The method card is in ./README.md."
    )


def msg_predict(
    *,
    fit: Any,
    nahead: int | None = None,
    do_cumulative: bool | None = None,
) -> dict[str, Any]:
    """Node ``msg_predict`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from
            msg_fit_*).
        nahead: [integer, optional] Volatility forecast horizon (default 1). Default ``1``.
        do_cumulative: [boolean, optional] Cumulative (aggregated) volatility forecast. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_predict: not implemented. The method card is in ./README.md."
    )


def msg_state(
    *,
    fit: Any,
) -> dict[str, Any]:
    """Node ``msg_state`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from
            msg_fit_*).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_state: not implemented. The method card is in ./README.md."
    )


def msg_sim(
    *,
    fit: Any,
    nsim: int | None = None,
    nahead: int | None = None,
    nburn: int | None = None,
) -> dict[str, Any]:
    """Node ``msg_sim`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``heavy``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from
            msg_fit_*).
        nsim: [integer, optional] Number of simulated paths (default 1· seeded). Default ``1``.
        nahead: [integer, optional] Length of each path (default 1). Default ``1``.
        nburn: [integer, optional] Burn-in observations (default 500). Default ``500``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_sim: not implemented. The method card is in ./README.md."
    )


def msg_risk(
    *,
    fit: Any,
    do_es: bool | None = None,
    nahead: int | None = None,
) -> dict[str, Any]:
    """Node ``msg_risk`` -- METHOD-SELECTION card #31.

    Markov-switching GARCH.

    Category 06-volatility-regimes; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to an 'MSGARCH_ML_FIT'/'MSGARCH_MCMC_FIT' (from
            msg_fit_*).
        do_es: [boolean, optional] Compute Expected Shortfall in addition to VaR. Default ``True``.
        nahead: [integer, optional] VaR/ES horizon (default 1). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "msg_risk: not implemented. The method card is in ./README.md."
    )
