# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``conditional_unconditional_expectiles`` -- method card #193.

#193 Conditional & unconditional expectiles (Expectiles-at-Risk / a GaR analogue, LAWS)

Category 12-distribution-risk; module ``conditional_unconditional_expectiles``.

Reference implementation: 10.2307/1911031.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c12_distribution_risk import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "exr_expectile",
    "exr_expectile_reg",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def exr_expectile_reg(
    *,
    formula: str,
    data: pd.DataFrame,
    estimate: Literal["laws", "restricted", "bundle", "sheets"] | None = None,
    smooth: (
        Literal[
            "schall",
            "ocv",
            "gcv",
            "cvgrid",
            "aic",
            "bic",
            "lcurve",
            "fixed",
        ]
        | None
    ) = None,
    lambda_: float | None = None,
    expectiles: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``exr_expectile_reg`` -- method card #193.

    Conditional & unconditional expectiles (Expectiles-at-Risk / a GaR analogue, LAWS).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        formula: [formula, required] Expectile-regression formula, e.g. 'growth ~ fci + slack'
            (response ~ covariates).
        data: [df_handle, required] Handle to a DataFrame (data-agnostic· time-sorted for the GaR
            interpretation).
        estimate: [enum, optional] Expectile estimation strategy (default laws·
            restricted/bundle/sheets forbid crossing).
        smooth: [enum, optional] Selection of the smoothing penalty lambda (default schall· 'fixed'
            -> use lambda as is).
        lambda_ (wire name ``lambda``): [number, optional] Positive smoothing parameter· active when
            smooth='fixed' (default 1). Default ``1``.
        expectiles: [number, optional] Vector of expectile levels in the open (0,1)· passed WHOLE
            (e.g. [0.05,0.5,0.95]). If missing -> default set 0.01..0.99.
        seed: [integer, optional] Reproducibility seed (defensive· deterministic fit) (default
            2025). Default ``2025``.

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
        "exr_expectile_reg: not implemented."
    )


def exr_expectile(
    *,
    x: Sequence[float],
    probs: float | None = None,
    dec: int | None = None,
) -> dict[str, Any]:
    """Node ``exr_expectile`` -- method card #193.

    Conditional & unconditional expectiles (Expectiles-at-Risk / a GaR analogue, LAWS).

    Category 12-distribution-risk; memory class ``light``.

    Args:
        x: [num_array, required] Numeric vector (series of returns/losses) without NA.
        probs: [number, optional] Vector of expectile levels in [0,1]· passed WHOLE (default
            [0.05,0.5,0.95]· 0.5 = the mean).
        dec: [integer, optional] Rounding decimals of the expectiles (default 4). Default ``4``.

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
        "exr_expectile: not implemented."
    )
