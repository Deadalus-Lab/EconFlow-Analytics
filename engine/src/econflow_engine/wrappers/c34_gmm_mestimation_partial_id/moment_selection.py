# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``moment_selection`` -- method card #294.

#294 Overidentification and moment-selection tests

Category 34-gmm-mestimation-partial-id; module ``moment_selection``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c34_gmm_mestimation_partial_id import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "gme_c_test",
    "gme_moment_selection",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def gme_c_test(
    *,
    fit: Any,
    subset: Sequence[str],
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``gme_c_test`` -- method card #294.

    Overidentification and moment-selection tests.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted GMM or IV model.
        subset: [series_codes, required] Instruments whose validity is being tested.
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
        "gme_c_test: not implemented."
    )


def gme_moment_selection(
    *,
    data: pd.DataFrame,
    moments: str,
    candidates: Sequence[str] | None = None,
    criterion: Literal["aic", "bic", "hqic"] | None = None,
) -> dict[str, Any]:
    """Node ``gme_moment_selection`` -- method card #294.

    Overidentification and moment-selection tests.

    Category 34-gmm-mestimation-partial-id; memory class ``light``.

    Args:
        data: [df_handle, required] Data the moments are evaluated on.
        moments: [formula, required] Moment-condition specification.
        candidates: [series_codes, optional] Candidate instrument columns.
        criterion: [enum, optional] Selection criterion. Default ``'bic'``.

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
        "gme_moment_selection: not implemented."
    )
