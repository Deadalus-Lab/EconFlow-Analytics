# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fiscal_multipliers`` -- method card #358.

#358 Fiscal multipliers by local projection and state-dependent local projection

Category 42-fiscal-debt-sustainability; module ``fiscal_multipliers``.

Reference implementation: localprojections.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c42_fiscal_debt_sustainability import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "fis_multiplier_lp",
    "fis_multiplier_state_dependent",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def fis_multiplier_lp(
    *,
    output: pd.Series,
    fiscal: pd.Series,
    controls: Sequence[str] | None = None,
    horizons: int | None = None,
    lags: int | None = None,
    cumulative: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_multiplier_lp`` -- method card #358.

    Fiscal multipliers by local projection and state-dependent local projection.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        output: [series_handle, required] Output series.
        fiscal: [series_handle, required] Fiscal shock or instrument.
        controls: [series_codes, optional] Control columns.
        horizons: [integer, optional] Maximum horizon. Default ``20``.
        lags: [integer, optional] Lags of the controls included. Default ``4``.
        cumulative: [boolean, optional] Report the cumulative multiplier. Default ``True``.
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
        "fis_multiplier_lp: not implemented."
    )


def fis_multiplier_state_dependent(
    *,
    output: pd.Series,
    fiscal: pd.Series,
    state: pd.Series,
    transition: Literal["smooth", "indicator"] | None = None,
    horizons: int | None = None,
    lags: int | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``fis_multiplier_state_dependent`` -- method card #358.

    Fiscal multipliers by local projection and state-dependent local projection.

    Category 42-fiscal-debt-sustainability; memory class ``light``.

    Args:
        output: [series_handle, required] Output series.
        fiscal: [series_handle, required] Fiscal shock or instrument.
        state: [series_handle, required] State variable, such as the output gap.
        transition: [enum, optional] How the state enters. Default ``'smooth'``.
        horizons: [integer, optional] Maximum horizon. Default ``20``.
        lags: [integer, optional] Lags of the controls included. Default ``4``.
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
        "fis_multiplier_state_dependent: not implemented."
    )
