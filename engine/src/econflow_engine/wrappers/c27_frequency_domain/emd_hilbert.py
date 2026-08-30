# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``emd_hilbert`` -- method card #590.

#590 Empirical mode decomposition and the Hilbert-Huang transform

Category 27-frequency-domain; module ``emd_hilbert``.

Reference implementation: EMD-signal.

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
    "fd_emd",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fd_emd(
    *,
    x: pd.Series,
    method: Literal["emd", "eemd", "ceemdan"] | None = None,
    max_imfs: int | None = None,
    n_ensemble: int | None = None,
    noise_strength: float | None = None,
    hilbert: bool | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``fd_emd`` -- method card #590.

    Empirical mode decomposition and the Hilbert-Huang transform.

    Category 27-frequency-domain; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        method: [enum, optional] Variant. Default ``'ceemdan'``.
        max_imfs: [integer, optional] Maximum modes extracted. Default ``10``.
        n_ensemble: [integer, optional] Ensemble size for the noise-assisted variants. Default
            ``100``.
        noise_strength: [number, optional] Added noise standard deviation. Default ``0.2``.
        hilbert: [boolean, optional] Compute the Hilbert spectrum. Default ``True``.
        seed: [integer, required] Seed for the random number generator; required for
            reproducibility.

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
        "fd_emd: not implemented."
    )
