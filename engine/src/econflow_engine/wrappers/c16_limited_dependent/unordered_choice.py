# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``unordered_choice`` -- method card #528.

#528 Multinomial and conditional logit for unordered outcomes

Category 16-limited-dependent; module ``unordered_choice``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_unordered_choice",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ld_unordered_choice(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["multinomial", "conditional", "multinomial_probit"] | None = None,
    base: str | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_unordered_choice`` -- method card #528.

    Multinomial and conditional logit for unordered outcomes.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Categorical outcome.
        x: [df_handle, required] Covariate table.
        model: [enum, optional] Model. Default ``'multinomial'``.
        base: [string, optional] Base alternative.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - model='multinomial_probit' must refuse with a GateError: statsmodels 0.14.6 carries no
          multinomial probit, established by a regex sweep of the installed package, by the
          statsmodels.api namespace and by the rendered discrete-model documentation for that
          version
        - the enum value stays because the node signature is frozen; dropping it is a contract
          change and an owner decision. The blocker is not a missing source -- Train 2009 above
          documents the simulated-likelihood estimator -- but the seed argument it needs, which this
          node does not declare and which would contradict the node's recorded cacheability

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "ld_unordered_choice: not implemented."
    )
