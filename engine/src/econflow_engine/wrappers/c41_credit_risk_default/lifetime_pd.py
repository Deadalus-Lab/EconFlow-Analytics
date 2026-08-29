# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``lifetime_pd`` -- method card #352.

#352 Time-to-default hazard models and lifetime PD term structures

Category 41-credit-risk-default; module ``lifetime_pd``.

Reference implementation: lifelines.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c41_credit_risk_default import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cr_lifetime_pd",
    "cr_pd_scenario",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cr_lifetime_pd(
    *,
    data: pd.DataFrame,
    time: str,
    event: str,
    covariates: Sequence[str] | None = None,
    horizon: int | None = None,
    model: Literal["cox", "discrete_cloglog", "weibull", "piecewise"] | None = None,
) -> dict[str, Any]:
    """Node ``cr_lifetime_pd`` -- method card #352.

    Time-to-default hazard models and lifetime PD term structures.

    Category 41-credit-risk-default; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Person-period or duration table.
        time: [string, required] Column holding the duration or period index.
        event: [string, required] Column holding the default indicator.
        covariates: [series_codes, optional] Covariate columns.
        horizon: [integer, optional] Lifetime horizon in periods. Default ``10``.
        model: [enum, optional] Hazard model family. Default ``'cox'``.

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
        "cr_lifetime_pd: not implemented."
    )


def cr_pd_scenario(
    *,
    fit: Any,
    scenarios: pd.DataFrame,
    weights: Sequence[float] | None = None,
) -> dict[str, Any]:
    """Node ``cr_pd_scenario`` -- method card #352.

    Time-to-default hazard models and lifetime PD term structures.

    Category 41-credit-risk-default; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted lifetime PD model.
        scenarios: [df_handle, required] Macroeconomic scenario paths.
        weights: [num_array, optional] Scenario probability weights.

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
        "cr_pd_scenario: not implemented."
    )
