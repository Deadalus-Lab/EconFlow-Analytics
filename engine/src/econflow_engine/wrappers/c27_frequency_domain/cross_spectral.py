# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``cross_spectral`` -- method card #586.

#586 Cross-spectral analysis: coherence, phase and gain

Category 27-frequency-domain; module ``cross_spectral``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_cross_spectrum",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fd_cross_spectrum(
    *,
    x: pd.Series,
    y: pd.Series,
    method: Literal["welch", "multitaper", "bartlett", "periodogram"] | None = None,
    nperseg: int | None = None,
    detrend: Literal["none", "constant", "linear"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fd_cross_spectrum`` -- method card #586.

    Cross-spectral analysis: coherence, phase and gain.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] First series.
        y: [series_handle, required] Second series.
        method: [enum, optional] Spectral estimator. Default ``'welch'``.
        nperseg: [integer, optional] Segment length.
        detrend: [enum, optional] Detrending applied per segment. Default ``'linear'``.
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
        "fd_cross_spectrum: not implemented."
    )
