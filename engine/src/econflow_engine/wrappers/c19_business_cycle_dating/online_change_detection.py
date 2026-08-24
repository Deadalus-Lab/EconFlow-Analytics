# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``online_change_detection`` -- method card #542.

#542 Online and sequential change detection

Category 19-business-cycle-dating; module ``online_change_detection``.

Reference implementation: skchange.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c19_business_cycle_dating import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "bc_online_change_detection",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def bc_online_change_detection(
    *,
    y: pd.Series,
    method: Literal["cusum", "page_hinkley", "bocpd", "ewma"] | None = None,
    threshold: float | None = None,
    hazard: float | None = None,
    burn_in: int | None = None,
) -> dict[str, Any]:
    """Node ``bc_online_change_detection`` -- method card #542.

    Online and sequential change detection.

    Category 19-business-cycle-dating; memory class ``light``.

    Args:
        y: [series_handle, required] Series.
        method: [enum, optional] Detector. Default ``'bocpd'``.
        threshold: [number, optional] Alarm threshold.
        hazard: [number, optional] Prior change hazard rate for the Bayesian detector. Default
            ``0.01``.
        burn_in: [integer, optional] Observations before detection starts. Default ``50``.

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
        "bc_online_change_detection: not implemented."
    )
