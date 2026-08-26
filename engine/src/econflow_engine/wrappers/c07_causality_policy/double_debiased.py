# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``double_debiased`` -- method card #45.

#45 Double/Debiased ML

Category 07-causality-policy; module ``double_debiased``.

Reference implementation: DoubleML.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c07_causality_policy import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "dml_irm",
    "dml_plr",
    "dml_prepare_data",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def dml_prepare_data(
    *,
    data: pd.DataFrame,
    y_col: str,
    d_cols: Sequence[str],
    x_cols: Sequence[str],
    z_cols: Sequence[str] | None = None,
    use_other_treat_as_covariate: bool | None = None,
) -> dict[str, Any]:
    """Node ``dml_prepare_data`` -- method card #45.

    Double/Debiased ML.

    Category 07-causality-policy; memory class ``light``.

    Registers its result under ``object``, so a later node can consume it as a handle.

    Args:
        data: [df_handle, required] Handle to a cross-sectional DataFrame.
        y_col: [string, required] Outcome column name.
        d_cols: [series_codes, required] Treatment column names (>=1).
        x_cols: [series_codes, required] Covariate/control column names.
        z_cols: [series_codes, optional] Instrument column names (optional).
        use_other_treat_as_covariate: [boolean, optional] Use the other treatments as covariates
            (default True). Default ``True``.

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
        "dml_prepare_data: not implemented."
    )


def dml_plr(
    *,
    data: Any,
    learner: Literal["random_forest", "elastic_net"] | None = None,
    n_folds: int | None = None,
    n_rep: int | None = None,
    score: Literal["partialling out", "IV-type"] | None = None,
    dml_procedure: Literal["dml2", "dml1"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``dml_plr`` -- method card #45.

    Double/Debiased ML.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        data: [raw_handle, required] Handle to a DoubleMLData object (from dml_prepare_data).
        learner: [enum, optional] ML engine for the nuisance functions (default random_forest).
        n_folds: [integer, optional] Cross-fitting folds (default 5). Default ``5``.
        n_rep: [integer, optional] Cross-fitting repetitions (default 1). Default ``1``.
        score: [enum, optional] Score function (default partialling out).
        dml_procedure: [enum, optional] DML procedure (default dml2).
        seed: [integer, required] Seed (required: cross-fitting reproducibility).

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
        "dml_plr: not implemented."
    )


def dml_irm(
    *,
    data: Any,
    learner: Literal["random_forest", "elastic_net"] | None = None,
    n_folds: int | None = None,
    n_rep: int | None = None,
    score: Literal["ATE", "ATTE"] | None = None,
    trimming_rule: Literal["truncate", "drop"] | None = None,
    dml_procedure: Literal["dml2", "dml1"] | None = None,
    seed: int,
) -> dict[str, Any]:
    """Node ``dml_irm`` -- method card #45.

    Double/Debiased ML.

    Category 07-causality-policy; memory class ``heavy``.

    Args:
        data: [raw_handle, required] Handle to a DoubleMLData object (binary treatment).
        learner: [enum, optional] ML engine (default random_forest).
        n_folds: [integer, optional] Cross-fitting folds (default 5). Default ``5``.
        n_rep: [integer, optional] Cross-fitting repetitions (default 1). Default ``1``.
        score: [enum, optional] Estimand (default ATE).
        trimming_rule: [enum, optional] Propensity trimming rule (default truncate).
        dml_procedure: [enum, optional] DML procedure (default dml2).
        seed: [integer, required] Seed (required: cross-fitting reproducibility).

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
        "dml_irm: not implemented."
    )
