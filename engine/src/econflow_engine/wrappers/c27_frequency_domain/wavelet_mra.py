# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``wavelet_mra`` -- method card #587.

#587 Discrete wavelet multi-resolution analysis

Category 27-frequency-domain; module ``wavelet_mra``.

Reference implementation: PyWavelets.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c27_frequency_domain import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fd_wavelet_mra",
    "fd_wavelet_variance",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fd_wavelet_mra(
    *,
    x: pd.Series,
    wavelet: Literal["haar", "d4", "la8", "la16", "c6", "sym8"] | None = None,
    transform: Literal["dwt", "modwt", "swt"] | None = None,
    levels: int | None = None,
    boundary: Literal["periodic", "reflection", "zero"] | None = None,
) -> dict[str, Any]:
    """Node ``fd_wavelet_mra`` -- method card #587.

    Discrete wavelet multi-resolution analysis.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        wavelet: [enum, optional] Wavelet filter. Default ``'la8'``.
        transform: [enum, optional] Transform. Default ``'modwt'``.
        levels: [integer, optional] Decomposition levels; omitted = maximum admissible.
        boundary: [enum, optional] Boundary handling. Default ``'reflection'``.

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
        "fd_wavelet_mra: not implemented."
    )


def fd_wavelet_variance(
    *,
    x: pd.Series,
    y: pd.Series | None = None,
    wavelet: Literal["haar", "d4", "la8", "la16", "c6", "sym8"] | None = None,
    levels: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fd_wavelet_variance`` -- method card #587.

    Discrete wavelet multi-resolution analysis.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] First series.
        y: [series_handle, optional] Second series for cross-correlation.
        wavelet: [enum, optional] Wavelet filter. Default ``'la8'``.
        levels: [integer, optional] Scales computed.
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
        "fd_wavelet_variance: not implemented."
    )
