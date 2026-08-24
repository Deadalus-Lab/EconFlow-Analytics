# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``propensity_score`` -- method card #274.

#274 Propensity-score estimation with common-support trimming

Category 32-matching-weighting; module ``propensity_score``.

Reference implementation: causallib.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c32_matching_weighting import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mw_common_support",
    "mw_overlap_diagnostics",
    "mw_pscore_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def mw_pscore_fit(
    *,
    data: pd.DataFrame,
    treatment: str,
    covariates: Sequence[str] | None = None,
    model: Literal["logit", "probit", "gradient_boosting", "random_forest"] | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``mw_pscore_fit`` -- method card #274.

    Propensity-score estimation with common-support trimming.

    Category 32-matching-weighting; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] One row per unit.
        treatment: [string, required] Binary treatment column.
        covariates: [series_codes, optional] Covariate columns entering the score.
        model: [enum, optional] Estimator for the score. Default ``'logit'``.
        seed: [integer, optional] Seed for the random number generator.

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
        "mw_pscore_fit: not implemented."
    )


def mw_common_support(
    *,
    pscore: pd.Series,
    treatment: pd.Series,
    rule: Literal["minmax", "quantile", "fixed", "crump"] | None = None,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``mw_common_support`` -- method card #274.

    Propensity-score estimation with common-support trimming.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        pscore: [series_handle, required] Fitted propensity per unit.
        treatment: [series_handle, required] Binary treatment indicator.
        rule: [enum, optional] Trimming rule. Default ``'minmax'``.
        threshold: [number, optional] Cut-off for the fixed and quantile rules. Default ``0.1``.

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
        "mw_common_support: not implemented."
    )


def mw_overlap_diagnostics(
    *,
    pscore: pd.Series,
    treatment: pd.Series,
    n_bins: int | None = None,
) -> dict[str, Any]:
    """Node ``mw_overlap_diagnostics`` -- method card #274.

    Propensity-score estimation with common-support trimming.

    Category 32-matching-weighting; memory class ``light``.

    Args:
        pscore: [series_handle, required] Fitted propensity per unit.
        treatment: [series_handle, required] Binary treatment indicator.
        n_bins: [integer, optional] Histogram bins for the by-arm score distribution. Default
            ``20``.

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
        "mw_overlap_diagnostics: not implemented."
    )
