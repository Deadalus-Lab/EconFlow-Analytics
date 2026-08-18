# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hierarchical_multilevel_linear`` -- METHOD-SELECTION card #175.

#175 Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling)

Category 08-panel-data; module ``hierarchical_multilevel_linear``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "lme_glmer",
    "lme_lmer",
    "lme_ranef",
    "lme_varcorr",
    "NODE_META",
    "wire_model",
]


def lme_lmer(
    *,
    formula: str,
    data: pd.DataFrame,
    REML: bool | None = None,
) -> dict[str, Any]:
    """Node ``lme_lmer`` -- METHOD-SELECTION card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Mixed-model formula with a random-effects term, e.g. 'y ~ x +
            (1 | group)'.
        data: [df_handle, required] Handle to a DataFrame (variables of the formula + grouping
            factor).
        REML: [boolean, optional] True=REML (default, unbiased variance components), False=ML (for
            comparing fixed effects). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lme_lmer: not implemented. The method card is in ./README.md."
    )


def lme_glmer(
    *,
    formula: str,
    data: pd.DataFrame,
    family: Literal["binomial", "poisson", "Gamma", "inverse.gaussian"] | None = None,
    nAGQ: int | None = None,
) -> dict[str, Any]:
    """Node ``lme_glmer`` -- METHOD-SELECTION card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] GLMM formula with a random-effects term, e.g. 'y ~ x + (1 |
            group)'.
        data: [df_handle, required] Handle to a DataFrame (variables of the formula + grouping
            factor).
        family: [enum, optional] Response distribution (closed set· default binomial). NOT gaussian
            (use lme_lmer).
        nAGQ: [integer, optional] Adaptive Gauss-Hermite quadrature points (default 1· >1 = more
            accurate likelihood, only single scalar RE). Default ``1``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lme_glmer: not implemented. The method card is in ./README.md."
    )


def lme_ranef(
    *,
    object: Any,
    condVar: bool | None = None,
) -> dict[str, Any]:
    """Node ``lme_ranef`` -- METHOD-SELECTION card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a merMod model (from lme_lmer/lme_glmer).
        condVar: [boolean, optional] Computation of conditional variances -> condsd in the records
            (default True). Default ``True``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lme_ranef: not implemented. The method card is in ./README.md."
    )


def lme_varcorr(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``lme_varcorr`` -- METHOD-SELECTION card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a merMod model (from lme_lmer/lme_glmer).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "lme_varcorr: not implemented. The method card is in ./README.md."
    )
