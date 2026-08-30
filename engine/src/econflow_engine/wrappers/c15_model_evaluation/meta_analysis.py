# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``meta_analysis`` -- method card #522.

#522 Meta-analysis and publication bias: meta-regression, PET-PEESE, Egger and funnel

Category 15-model-evaluation; module ``meta_analysis``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c15_model_evaluation import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "me_meta_analysis",
    "me_publication_bias",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def me_meta_analysis(
    *,
    effects: pd.Series,
    standard_errors: pd.Series,
    model: Literal["fixed", "random"] | None = None,
    method: Literal["dersimonian_laird", "reml", "paule_mandel"] | None = None,
    moderators: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``me_meta_analysis`` -- method card #522.

    Meta-analysis and publication bias: meta-regression, PET-PEESE, Egger and funnel.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        effects: [series_handle, required] Study effect estimates.
        standard_errors: [series_handle, required] Study standard errors.
        model: [enum, optional] Model. Default ``'random'``.
        method: [enum, optional] Heterogeneity estimator. Default ``'dersimonian_laird'``.
        moderators: [series_codes, optional] Moderator columns for meta-regression.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

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
        "me_meta_analysis: not implemented."
    )


def me_publication_bias(
    *,
    effects: pd.Series,
    standard_errors: pd.Series,
    method: Literal["egger", "pet_peese", "trim_fill", "begg", "selection_model"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``me_publication_bias`` -- method card #522.

    Meta-analysis and publication bias: meta-regression, PET-PEESE, Egger and funnel.

    Category 15-model-evaluation; memory class ``light``.

    Args:
        effects: [series_handle, required] Study effect estimates.
        standard_errors: [series_handle, required] Study standard errors.
        method: [enum, optional] Method. Default ``'pet_peese'``.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "me_publication_bias: not implemented."
    )
