# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``multinomial_conditional_logit`` -- method card #271.

#271 Multinomial and conditional logit

Category 31-discrete-choice-demand; module ``multinomial_conditional_logit``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from econflow_engine.generated.args.c31_discrete_choice_demand import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dcd_clogit_fit",
    "dcd_iia_test",
    "dcd_mnlogit_fit",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dcd_mnlogit_fit(
    *,
    data: pd.DataFrame,
    choice: str,
    covariates: Sequence[str] | None = None,
    base: str | None = None,
) -> dict[str, Any]:
    """Node ``dcd_mnlogit_fit`` -- method card #271.

    Multinomial and conditional logit.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] One row per chooser.
        choice: [string, required] Column holding the chosen alternative.
        covariates: [series_codes, optional] Chooser-varying covariate columns.
        base: [string, optional] Base alternative; omitted = the first observed.

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
        "dcd_mnlogit_fit: not implemented."
    )


def dcd_clogit_fit(
    *,
    data: pd.DataFrame,
    chooser: str,
    chosen: str,
    covariates: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``dcd_clogit_fit`` -- method card #271.

    Multinomial and conditional logit.

    Category 31-discrete-choice-demand; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] One row per chooser per alternative.
        chooser: [string, required] Column identifying the chooser.
        chosen: [string, required] Column flagging the chosen row.
        covariates: [series_codes, optional] Alternative-varying covariate columns.

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
        "dcd_clogit_fit: not implemented."
    )


def dcd_iia_test(
    *,
    fit: Any,
    drop: Sequence[str],
) -> dict[str, Any]:
    """Node ``dcd_iia_test`` -- method card #271.

    Multinomial and conditional logit.

    Category 31-discrete-choice-demand; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted multinomial or conditional logit.
        drop: [series_codes, required] Alternatives removed to form the restricted model.

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
        "dcd_iia_test: not implemented."
    )
