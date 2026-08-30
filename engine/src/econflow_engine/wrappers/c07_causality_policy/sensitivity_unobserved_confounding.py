# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``sensitivity_unobserved_confounding`` -- method card #170.

#170 Sensitivity analysis to unobserved confounding / omitted-variable bias (robustness value + OVB
    bounds)

Category 07-causality-policy; module ``sensitivity_unobserved_confounding``.

Reference implementation: PySensemakr.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sens_analyze",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def sens_analyze(
    *,
    treatment: str,
    benchmark_covariates: Sequence[str],
    formula: str | None = None,
    data: pd.DataFrame | None = None,
    object: Any | None = None,
    kd: Sequence[float] | None = None,
    ky: Sequence[float] | None = None,
    q: float | None = None,
    alpha: float | None = None,
    reduce: bool | None = None,
) -> dict[str, Any]:
    """Node ``sens_analyze`` -- method card #170.

    Sensitivity analysis to unobserved confounding / omitted-variable bias (robustness value + OVB
    bounds).

    Category 07-causality-policy; memory class ``light``.

    Args:
        treatment: [string, required] Name of the treatment coefficient (ONE coef name of the lm,
            not the intercept).
        benchmark_covariates: [series_codes, required] Covariate names (>=1) used as the benchmark
            for confounding strength; a subset of the coef names \\ {treatment}.
        formula: [formula, optional] OLS formula, e.g. 'y ~ d + x1 + x2' (fit path; ALSO requires
            data). Alternatively supply object.
        data: [df_handle, optional] Handle to a DataFrame holding the variables of the formula (fit
            path).
        object: [raw_handle, optional] Handle to an ALREADY fitted 'lm' model (consume path;
            mutually exclusive with formula+data).
        kd: [num_array, optional] Multipliers of the confounder~treatment strength relative to the
            benchmark (>0, default 1; e.g. [1,2,3]). Default ``1``.
        ky: [num_array, optional] Multipliers of the confounder~outcome strength (>0; default = kd).
        q: [number, optional] Fraction of effect reduction treated as problematic for the robustness
            value (>0, default 1 = complete disappearance). Default ``1``.
        alpha: [number, optional] Significance level for the robustness value with statistical
            significance, in (0,1) (default 0.05). Default ``0.05``.
        reduce: [boolean, optional] True: the confounder REDUCES the estimate (default); False: it
            increases it. Default ``True``.

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
        "sens_analyze: not implemented."
    )
