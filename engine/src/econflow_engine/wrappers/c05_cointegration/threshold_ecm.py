# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``threshold_ecm`` -- method card #435.

#435 Threshold and asymmetric error correction: Hansen-Seo TVECM and Enders-Siklos TAR

Category 05-cointegration; module ``threshold_ecm``.

Reference implementation: 10.1016/S0304-4076(02)00097-0.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c05_cointegration import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ci_threshold_ecm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ci_threshold_ecm(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["tar", "m_tar", "tvecm"] | None = None,
    threshold: float | None = None,
    trim: float | None = None,
    nboot: int | None = None,
    seed: int,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ci_threshold_ecm`` -- method card #435.

    Threshold and asymmetric error correction: Hansen-Seo TVECM and Enders-Siklos TAR.

    Category 05-cointegration; memory class ``heavy``.

    Args:
        y: [series_handle, required] Dependent series.
        x: [multiseries_handle, required] Regressor series.
        model: [enum, optional] Threshold specification. Default ``'tar'``.
        threshold: [number, optional] Threshold; omitted = estimated by grid search.
        trim: [number, optional] Fraction trimmed from each end of the threshold grid. Default
            ``0.15``.
        nboot: [integer, optional] Number of bootstrap replications. Default ``999``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.
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
        "ci_threshold_ecm: not implemented."
    )
