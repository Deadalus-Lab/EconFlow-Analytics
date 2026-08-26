# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``hdfe_absorption`` -- method card #456.

#456 High-dimensional fixed-effect absorption

Category 07-causality-policy; module ``hdfe_absorption``.

Reference implementation: pyfixest.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cp_connected_components",
    "cp_hdfe_regress",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cp_hdfe_regress(
    *,
    data: pd.DataFrame,
    formula: str,
    absorb: Sequence[str],
    cluster: Sequence[str] | None = None,
    tolerance: float | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``cp_hdfe_regress`` -- method card #456.

    High-dimensional fixed-effect absorption.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Data.
        formula: [formula, required] Model formula for the non-absorbed part.
        absorb: [series_codes, required] Columns whose fixed effects are absorbed.
        cluster: [series_codes, optional] Clustering variables.
        tolerance: [number, optional] Convergence tolerance of the projection. Default ``1e-08``.
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
        "cp_hdfe_regress: not implemented."
    )


def cp_connected_components(
    *,
    data: pd.DataFrame,
    dimensions: Sequence[str],
) -> dict[str, Any]:
    """Node ``cp_connected_components`` -- method card #456.

    High-dimensional fixed-effect absorption.

    Category 07-causality-policy; memory class ``light``.

    Args:
        data: [df_handle, required] Data.
        dimensions: [series_codes, required] The two fixed-effect columns.

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
        "cp_connected_components: not implemented."
    )
