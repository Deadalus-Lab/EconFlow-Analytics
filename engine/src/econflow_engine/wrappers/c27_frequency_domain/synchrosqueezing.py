# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``synchrosqueezing`` -- method card #591.

#591 Synchrosqueezing and reassigned time-frequency transforms

Category 27-frequency-domain; module ``synchrosqueezing``.

Reference implementation: ssqueezepy.

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
    "fd_synchrosqueeze",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fd_synchrosqueeze(
    *,
    x: pd.Series,
    transform: Literal["cwt", "stft"] | None = None,
    squeeze: bool | None = None,
    wavelet: Literal["morlet", "bump", "gmw"] | None = None,
    extract_ridges: int | None = None,
) -> dict[str, Any]:
    """Node ``fd_synchrosqueeze`` -- method card #591.

    Synchrosqueezing and reassigned time-frequency transforms.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        transform: [enum, optional] Transform. Default ``'cwt'``.
        squeeze: [boolean, optional] Apply synchrosqueezing. Default ``True``.
        wavelet: [enum, optional] Analysing wavelet. Default ``'morlet'``.
        extract_ridges: [integer, optional] Ridges to extract; 0 = none. Default ``0``.

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
        "fd_synchrosqueeze: not implemented."
    )
