# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``entropy_diagnostics`` -- method card #404.

#404 Entropy diagnostics: sample, permutation, approximate and spectral entropy

Category 01-preparation-prechecks; module ``entropy_diagnostics``.

Reference implementation: antropy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_entropy",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_entropy(
    *,
    x: pd.Series,
    measures: Sequence[str] | None = None,
    embedding_dimension: int | None = None,
    tolerance: float | None = None,
    normalise: bool | None = None,
) -> dict[str, Any]:
    """Node ``pp_entropy`` -- method card #404.

    Entropy diagnostics: sample, permutation, approximate and spectral entropy.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [series_handle, required] Series.
        measures: [series_codes, optional] Measures to compute; omitted = the standard set.
        embedding_dimension: [integer, optional] Embedding dimension. Default ``3``.
        tolerance: [number, optional] Tolerance as a fraction of the standard deviation. Default
            ``0.2``.
        normalise: [boolean, optional] Normalise to the unit interval where possible. Default
            ``True``.

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
        "pp_entropy: not implemented."
    )
