# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``compositional_transforms`` -- method card #390.

#390 Compositional log-ratio transforms: CLR, ILR and ALR

Category 00-data-utilities; module ``compositional_transforms``.

Reference implementation: composition-stats.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "du_log_ratio_inverse",
    "du_log_ratio_transform",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def du_log_ratio_transform(
    *,
    data: pd.DataFrame,
    transform: Literal["clr", "ilr", "alr"] | None = None,
    reference: str | None = None,
    zero_replacement: Literal["none", "multiplicative", "additive", "bayesian"] | None = None,
    delta: float | None = None,
) -> dict[str, Any]:
    """Node ``du_log_ratio_transform`` -- method card #390.

    Compositional log-ratio transforms: CLR, ILR and ALR.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Compositional data, rows summing to a constant.
        transform: [enum, optional] Transform family. Default ``'clr'``.
        reference: [string, optional] Reference part for the additive transform.
        zero_replacement: [enum, optional] Zero handling. Default ``'multiplicative'``.
        delta: [number, optional] Replacement value for zeros. Default ``1e-06``.

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
        "du_log_ratio_transform: not implemented."
    )


def du_log_ratio_inverse(
    *,
    data: pd.DataFrame,
    transform: Literal["clr", "ilr", "alr"] | None = None,
    reference: str | None = None,
) -> dict[str, Any]:
    """Node ``du_log_ratio_inverse`` -- method card #390.

    Compositional log-ratio transforms: CLR, ILR and ALR.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Data in log-ratio coordinates.
        transform: [enum, optional] Transform that was applied. Default ``'clr'``.
        reference: [string, optional] Reference part used by the additive transform.

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
        "du_log_ratio_inverse: not implemented."
    )
