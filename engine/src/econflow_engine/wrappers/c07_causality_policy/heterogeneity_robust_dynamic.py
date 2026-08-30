# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``heterogeneity_robust_dynamic`` -- method card #166.

#166 Heterogeneity-robust dynamic DiD event study (de Chaisemartin & D'Haultfoeuille;
    non-binary/non-absorbing treatments)

Category 07-causality-policy; module ``heterogeneity_robust_dynamic``.

Reference implementation: diff-diff.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "didm_dynamic",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def didm_dynamic(
    *,
    df: pd.DataFrame,
    outcome: str,
    group: str,
    time: str,
    treatment: str,
    effects: int | None = None,
    placebo: int | None = None,
    controls: Sequence[str] | None = None,
    cluster: str | None = None,
    weight: str | None = None,
    normalized: bool | None = None,
    trends_lin: bool | None = None,
    continuous: int | None = None,
    effects_equal: bool | None = None,
    ci_level: int | None = None,
    bootstrap: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``didm_dynamic`` -- method card #166.

    Heterogeneity-robust dynamic DiD event study (de Chaisemartin & D'Haultfoeuille;
    non-binary/non-absorbing treatments).

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        df: [df_handle, required] Handle to a long-format panel DataFrame (group x time,
            evenly-spaced time).
        outcome: [string, required] Outcome column name.
        group: [string, required] Group column name (cross-sectional unit: county/firm/...).
        time: [string, required] Time column name (evenly-spaced periods).
        treatment: [string, required] Treatment column name (may be non-binary AND/OR
            non-absorbing).
        effects: [integer, optional] Number of event-study effects (ℓ=1..effects; default 1).
            Default ``1``.
        placebo: [integer, optional] Number of placebo (pre-trends) estimators; MUST be <= effects
            (default 0). Default ``0``.
        controls: [series_codes, optional] Covariate column names (residualized first-differences;
            default: none).
        cluster: [string, optional] Column name for SE clustering (>= group level; default
            clustering at the group).
        weight: [string, optional] Column name of the estimation weights (default: unweighted/number
            of obs).
        normalized: [boolean, optional] Normalized effects (weighted avg of current+lagged
            treatment; default False). Default ``False``.
        trends_lin: [boolean, optional] Group-specific linear trends (THEN the ATE is NOT computed;
            default False). Default ``False``.
        continuous: [integer, optional] Polynomial order for continuous period-one treatment
            (bootstrap recommended).
        effects_equal: [boolean, optional] F-test of equality of all effects (requires effects>=2;
            default False). Default ``False``.
        ci_level: [integer, optional] Confidence level, integer in (0,100) (default 95). Default
            ``95``.
        bootstrap: [integer, optional] Bootstrap replications (None = analytical SE);
            seed-reproducible.
        seed: [integer, optional] Bootstrap reproducibility seed (default 2025). Default ``2025``.

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
        "didm_dynamic: not implemented."
    )
