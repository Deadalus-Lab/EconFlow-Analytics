# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``empirical_likelihood`` -- method card #296.

#296 Empirical likelihood and generalised empirical likelihood

Category 34-gmm-mestimation-partial-id; module ``empirical_likelihood``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_el_test",
    "gme_empirical_likelihood",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_empirical_likelihood(
    *,
    data: pd.DataFrame,
    moments: str,
    family: Literal["el", "et", "cue", "hd"] | None = None,
    max_iter: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_empirical_likelihood`` -- method card #296.

    Empirical likelihood and generalised empirical likelihood.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data the moments are evaluated on.
        moments: [formula, required] Moment-condition specification.
        family: [enum, optional] GEL family member. Default ``'el'``.
        max_iter: [integer, optional] Maximum outer iterations. Default ``100``.
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
        "gme_empirical_likelihood: not implemented."
    )


def gme_el_test(
    *,
    fit: Any,
    restriction: str,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_el_test`` -- method card #296.

    Empirical likelihood and generalised empirical likelihood.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted empirical-likelihood model.
        restriction: [formula, required] Restriction under the null.
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
        "gme_el_test: not implemented."
    )
