# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``correspondence_analysis`` -- method card #601.

#601 Correspondence analysis, MCA and FAMD for mixed data

Category 29-unsupervised-clustering; module ``correspondence_analysis``.

Reference implementation: prince.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c29_unsupervised_clustering import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "uc_correspondence_analysis",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def uc_correspondence_analysis(
    *,
    x: pd.DataFrame,
    method: Literal["ca", "mca", "famd", "mfa"] | None = None,
    n_components: int | None = None,
    correction: Literal["none", "benzecri", "greenacre"] | None = None,
) -> dict[str, Any]:
    """Node ``uc_correspondence_analysis`` -- method card #601.

    Correspondence analysis, MCA and FAMD for mixed data.

    Category 29-unsupervised-clustering; memory class ``light``.

    Args:
        x: [df_handle, required] Categorical or mixed data.
        method: [enum, optional] Method. Default ``'mca'``.
        n_components: [integer, optional] Dimensions retained. Default ``2``.
        correction: [enum, optional] Inertia correction for MCA. Default ``'benzecri'``.

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
        "uc_correspondence_analysis: not implemented."
    )
