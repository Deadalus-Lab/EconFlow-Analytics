# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``instrumental_variables_2sls`` -- method card #165.

#165 Instrumental variables / 2SLS (a three-part formula) + weak-instruments / Wu-Hausman / Sargan
    diagnostics

Category 07-causality-policy; module ``instrumental_variables_2sls``.

Reference implementation: linearmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "iv_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def iv_fit(
    *,
    formula: str,
    data: pd.DataFrame,
    method: Literal["OLS", "M", "MM"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``iv_fit`` -- method card #165.

    Instrumental variables / 2SLS (a three-part formula) + weak-instruments / Wu-Hausman / Sargan
    diagnostics.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        formula: [formula, required] Three-part IV formula 'y ~ exog | endog | instruments' (modern
            ivreg; all 3 parts required).
        data: [df_handle, required] Handle to a DataFrame holding every variable of the formula (no
            NA).
        method: [enum, optional] Estimator: classical 2SLS (OLS, default) or robust M/MM (both
            require robustbase). Default ``'OLS'``.
        conf_level: [number, optional] Confidence level for the coefficient CIs, in (0,1) (default
            0.95). Default ``0.95``.

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
        "iv_fit: not implemented."
    )
