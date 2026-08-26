# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hierarchical_multilevel_linear`` -- method card #175.

#175 Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling)

Category 08-panel-data; module ``hierarchical_multilevel_linear``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "lme_fit",
    "lme_fit_glm",
    "lme_random_effects",
    "lme_variance_components",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def lme_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    REML: bool | None = None,
) -> dict[str, Any]:
    """Node ``lme_fit`` -- method card #175.

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
        "lme_fit: not implemented."
    )


def lme_fit_glm(
    *,
    formula: str,
    data: pd.DataFrame,
    family: Literal["binomial", "poisson", "Gamma", "inverse.gaussian"] | None = None,
    nAGQ: int | None = None,
) -> dict[str, Any]:
    """Node ``lme_fit_glm`` -- method card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] GLMM formula with a random-effects term, e.g. 'y ~ x + (1 |
            group)'.
        data: [df_handle, required] Handle to a DataFrame (variables of the formula + grouping
            factor).
        family: [enum, optional] Response distribution (closed set· default binomial). NOT gaussian
            (use lme_fit).
        nAGQ: [integer, optional] Adaptive Gauss-Hermite quadrature points (default 1· >1 = more
            accurate likelihood, only single scalar RE). Default ``1``.

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
        "lme_fit_glm: not implemented."
    )


def lme_random_effects(
    *,
    object: Any,
    condVar: bool | None = None,
) -> dict[str, Any]:
    """Node ``lme_random_effects`` -- method card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a merMod model (from lme_fit/lme_fit_glm).
        condVar: [boolean, optional] Computation of conditional variances -> condsd in the records
            (default True). Default ``True``.

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
        "lme_random_effects: not implemented."
    )


def lme_variance_components(
    *,
    object: Any,
) -> dict[str, Any]:
    """Node ``lme_variance_components`` -- method card #175.

    Hierarchical / multilevel (mixed) models — linear & generalized (partial pooling).

    Category 08-panel-data; memory class ``light``.

    Args:
        object: [raw_handle, required] Handle to a merMod model (from lme_fit/lme_fit_glm).

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
        "lme_variance_components: not implemented."
    )
