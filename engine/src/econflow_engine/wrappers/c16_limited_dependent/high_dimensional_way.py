# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``high_dimensional_way`` -- METHOD-SELECTION card #206.

#206 High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic
    incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects

Category 16-limited-dependent; module ``high_dimensional_way``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "alpaca_apes",
    "alpaca_feglm",
    "NODE_META",
    "wire_model",
]


def alpaca_feglm(
    *,
    formula: str,
    data: pd.DataFrame,
    family: Literal["logit", "probit", "poisson"] | None = None,
    bias_correct: bool | None = None,
    L: int | None = None,
    panel_structure: Literal["classic", "network"] | None = None,
) -> dict[str, Any]:
    """Node ``alpaca_feglm`` -- METHOD-SELECTION card #206.

    High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic
    incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] FE GLM formula 'y ~ x1 + x2 | fe1 + fe2' — the '| fe' part
            (high-dim fixed effects) is REQUIRED.
        data: [df_handle, required] Handle to a panel DataFrame· response binary (binomial) or
            non-negative integers/counts (poisson), without NA in the variables.
        family: [enum, optional] Family/link (default logit· probit=binomial probit· poisson=count).
        bias_correct: [boolean, optional] Analytical incidental-parameter bias correction
            (Fernández-Val/Weidner)· ONLY binomial (default False). Default ``False``.
        L: [integer, optional] Spectral density bandwidth (Hahn-Kuersteiner)· 0=strictly exogenous,
            1-4 for weakly exogenous (lagged) regressors. Default ``0``.
        panel_structure: [enum, optional] Panel structure for the bias correction (default classic·
            network=bilateral).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "alpaca_feglm: not implemented. The method card is in ./README.md."
    )


def alpaca_apes(
    *,
    object: Any,
    n_pop: int | None = None,
    sampling_fe: Literal["independence", "unrestricted"] | None = None,
    weak_exo: bool | None = None,
) -> dict[str, Any]:
    """Node ``alpaca_apes`` -- METHOD-SELECTION card #206.

    High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic
    incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted (+bias-corrected) feglm model from
            alpaca_feglm· ONLY binary choice (binomial).
        n_pop: [integer, optional] Finite-population correction (population size)·
            empty=delta-method only.
        sampling_fe: [enum, optional] Sampling assumptions for the FPC of the APE covariance
            (default independence).
        weak_exo: [boolean, optional] True if some regressors are weakly exogenous/predetermined
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "alpaca_apes: not implemented. The method card is in ./README.md."
    )
