# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``cross_sectional_dependence`` -- method card #396.

#396 Panel cross-sectional dependence: Pesaran CD, LM and scaled LM

Category 01-preparation-prechecks; module ``cross_sectional_dependence``.

Reference implementation: 10.1007/s00181-020-01875-7.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pp_cross_sectional_dependence",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pp_cross_sectional_dependence(
    *,
    residuals: pd.DataFrame,
    unit: str,
    time: str,
    test: Literal["cd", "lm", "scaled_lm", "bias_corrected_lm"] | None = None,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pp_cross_sectional_dependence`` -- method card #396.

    Panel cross-sectional dependence: Pesaran CD, LM and scaled LM.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        residuals: [df_handle, required] Panel residuals or the variable itself.
        unit: [string, required] Column identifying the unit.
        time: [string, required] Column identifying the period.
        test: [enum, optional] Test variant. Default ``'cd'``.
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
        "pp_cross_sectional_dependence: not implemented."
    )
