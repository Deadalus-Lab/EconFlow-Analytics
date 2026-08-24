# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``panel_decomposition`` -- method card #466.

#466 Between and within variance decomposition and poolability tests

Category 08-panel-data; module ``panel_decomposition``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c08_panel_data import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "pd_slope_homogeneity_test",
    "pd_variance_decomposition",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def pd_variance_decomposition(
    *,
    data: pd.DataFrame,
    variables: Sequence[str] | None = None,
    unit: str,
    time: str,
    threshold: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_variance_decomposition`` -- method card #466.

    Between and within variance decomposition and poolability tests.

    Category 08-panel-data; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        variables: [series_codes, optional] Variables to decompose.
        unit: [string, required] Unit identifier.
        time: [string, required] Time identifier.
        threshold: [number, optional] Within-share below which a variable is flagged. Default
            ``0.05``.

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
        "pd_variance_decomposition: not implemented."
    )


def pd_slope_homogeneity_test(
    *,
    data: pd.DataFrame,
    formula: str,
    unit: str,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``pd_slope_homogeneity_test`` -- method card #466.

    Between and within variance decomposition and poolability tests.

    Category 08-panel-data; memory class ``light``.

    Args:
        data: [df_handle, required] Panel data.
        formula: [formula, required] Model formula.
        unit: [string, required] Unit identifier.
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
        "pd_slope_homogeneity_test: not implemented."
    )
