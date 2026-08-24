# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``high_dimensional_way`` -- method card #206.

#206 High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic
    incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects

Category 16-limited-dependent; module ``high_dimensional_way``.

Reference implementation: 10.1016/j.jeconom.2015.12.014.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "hdfe_average_partial_effects",
    "hdfe_glm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def hdfe_glm(
    *,
    formula: str,
    data: pd.DataFrame,
    family: Literal["logit", "probit", "poisson"] | None = None,
    bias_correct: bool | None = None,
    L: int | None = None,
    panel_structure: Literal["classic", "network"] | None = None,
) -> dict[str, Any]:
    """Node ``hdfe_glm`` -- method card #206.

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

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "hdfe_glm: not implemented."
    )


def hdfe_average_partial_effects(
    *,
    object: Any,
    n_pop: int | None = None,
    sampling_fe: Literal["independence", "unrestricted"] | None = None,
    weak_exo: bool | None = None,
) -> dict[str, Any]:
    """Node ``hdfe_average_partial_effects`` -- method card #206.

    High-dimensional k-way fixed-effects GLM (binary logit/probit, Poisson count) with an analytic
    incidental-parameter bias correction (Fernández-Val/Weidner) + average partial effects.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a fitted (+bias-corrected) feglm model from
            hdfe_glm· ONLY binary choice (binomial).
        n_pop: [integer, optional] Finite-population correction (population size)·
            empty=delta-method only.
        sampling_fe: [enum, optional] Sampling assumptions for the FPC of the APE covariance
            (default independence).
        weak_exo: [boolean, optional] True if some regressors are weakly exogenous/predetermined
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "hdfe_average_partial_effects: not implemented."
    )
