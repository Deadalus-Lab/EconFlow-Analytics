# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``gmm_nonlinear`` -- method card #292.

#292 General nonlinear GMM: one-step, two-step, iterated and continuously-updated

Category 34-gmm-mestimation-partial-id; module ``gmm_nonlinear``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_fit",
    "gme_j_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_fit(
    *,
    data: pd.DataFrame,
    moments: str,
    instruments: Sequence[str] | None = None,
    method: Literal["onestep", "twostep", "iterated", "cue"] | None = None,
    weighting: Literal["identity", "robust", "hac", "cluster"] | None = None,
    max_iter: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_fit`` -- method card #292.

    General nonlinear GMM: one-step, two-step, iterated and continuously-updated.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data the moments are evaluated on.
        moments: [formula, required] Moment-condition specification.
        instruments: [series_codes, optional] Instrument columns.
        method: [enum, optional] GMM variant. Default ``'twostep'``.
        weighting: [enum, optional] Weighting matrix. Default ``'robust'``.
        max_iter: [integer, optional] Maximum iterations for the iterated variant. Default ``100``.
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
        "gme_fit: not implemented."
    )


def gme_j_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_j_test`` -- method card #292.

    General nonlinear GMM: one-step, two-step, iterated and continuously-updated.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted GMM model.
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
        "gme_j_test: not implemented."
    )
