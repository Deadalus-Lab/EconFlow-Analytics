# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``realised_garch`` -- method card #439.

#439 Realised GARCH and HEAVY models

Category 06-volatility-regimes; module ``realised_garch``.

Reference implementation: 10.1002/jae.1234.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c06_volatility_regimes import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "vr_realised_garch",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def vr_realised_garch(
    *,
    y: pd.Series,
    realised: pd.Series,
    model: Literal["realised_garch", "heavy"] | None = None,
    leverage: bool | None = None,
    distribution: Literal["normal", "t", "skewt"] | None = None,
) -> dict[str, Any]:
    """Node ``vr_realised_garch`` -- method card #439.

    Realised GARCH and HEAVY models.

    Category 06-volatility-regimes; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Daily return series.
        realised: [series_handle, required] Daily realised variance measure.
        model: [enum, optional] Model family. Default ``'realised_garch'``.
        leverage: [boolean, optional] Include a leverage function. Default ``True``.
        distribution: [enum, optional] Innovation distribution. Default ``'t'``.

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
        "vr_realised_garch: not implemented."
    )
