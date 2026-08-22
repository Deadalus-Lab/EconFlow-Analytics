# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``design_matrix_orthogonal`` -- method card #253.

#253 DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (returning the fitted
    coefficients), INTERACTIONS without a formula surface, an allowlisted formula path, a
    COMBINATORIAL factor

Category 00-data-utilities; module ``design_matrix_orthogonal``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import numpy as np
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ply_interaction_categorical",
    "ply_interactions",
    "ply_model_matrix",
    "ply_polynomial",
    "NODE_META",
    "wire_model",
]


def ply_polynomial(
    *,
    x: np.ndarray,
    degree: int | None = None,
    raw: bool | None = None,
    coefs_alpha: Sequence[float] | None = None,
    coefs_norm2: Sequence[float] | None = None,
    name: str | None = None,
) -> dict[str, Any]:
    """Node ``ply_polynomial`` -- method card #253.

    DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (returning the fitted
    coefficients), INTERACTIONS without a formula surface, an allowlisted formula path, a
    COMBINATORIAL factor.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to A SINGLE numeric column (n×1). NOT NA/NaN/Inf (the
            orthogonal-polynomial basis: "missing values are not allowed in 'poly'"). The UNIQUE
            values must be more numerous than the degree.
        degree: [integer, optional] Polynomial degree (default 2). POSITIVE INTEGER strictly less
            than the number of unique values of x ("'degree' must be less than number of unique
            points»). A decimal degree does NOT error in stats — it is SILENTLY truncated downward;
            here it is blocked. Default ``2``.
        raw: [boolean, optional] False (default) = ORTHOGONAL basis: numerically stable,
            uncorrelated columns, the p-values of the lower degrees do NOT change when a higher one
            is added. True = RAW x^1..x^d: interpretable coefficients but STRONG collinearity. ONLY
            the orthogonal basis has fitted params. Default ``False``.
        coefs_alpha: [num_array, optional] FIT/APPLY EXTERNALIZATION (§3b gate 6): the 'coefs_alpha'
            of a PREVIOUS fit (length EXACTLY degree). Required TOGETHER with coefs_norm2 to
            reproduce THE SAME basis on NEW data. Without these, a re-fit gives a DIFFERENT basis
            and the model's coefficients mean nothing.
        coefs_norm2: [num_array, optional] The 'coefs_norm2' of a previous fit (length EXACTLY
            degree+2, strictly positive). Wrong length => the orthogonal-polynomial basis returns a
            SILENTLY NA-filled column; here it is blocked.
        name: [string, optional] Column name prefix (default 'x' -> x_poly1, x_poly2,...). Valid
            identifier. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ply_polynomial: not implemented."
    )


def ply_interactions(
    *,
    data: pd.DataFrame,
    vars: Sequence[str] | None = None,
    order: int | None = None,
    include_main: bool | None = None,
    intercept: bool | None = None,
    contrasts: Literal["contr.treatment", "contr.sum", "contr.helmert", "contr.poly"] | None = None,
    xlev: Any | None = None,
    expect_columns: Sequence[str] | None = None,
    rank_check: Literal["auto", "stop", "report"] | None = None,
    max_levels: int | None = None,
    max_columns: int | None = None,
) -> dict[str, Any]:
    """Node ``ply_interactions`` -- method card #253.

    DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (returning the fitted
    coefficients), INTERACTIONS without a formula surface, an allowlisted formula path, a
    COMBINATORIAL factor.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). Allowed: numeric/categorical/string/logical columns — NOT list-columns, NOT
            NA/Inf in the columns that are used (the model-frame builder SILENTLY DROPS rows and
            breaks the alignment with y). Column names must be valid identifiers.
        vars: [series_codes, optional] Column names that enter the design matrix (default: ALL). The
            formula is built INTERNALLY from these — no expression is parsed (security).
        order: [integer, optional] Interaction order (default 2 = all pairs). 1 = main terms only; 3
            = also triples. Cannot exceed the number of variables. Default ``2``.
        include_main: [boolean, optional] True (default) = main terms + all interactions up to
            'order' (hierarchical principle). False = ONLY the terms of exactly order 'order'
            (requires order >= 2). Default ``True``.
        intercept: [boolean, optional] True (default) = intercept column. False = no intercept AND
            full dummy encoding of the first factor (all levels). Default ``True``.
        contrasts: [enum, optional] Categorical encoding. 'treatment' (default) = dummy relative to
            the FIRST level; 'sum' = deviations from the mean (useful for interpretable
            interactions); 'helmert' = successive contrasts; 'poly' = orthogonal polynomials for
            ORDERED categories. Returned in the 'contrasts' field — part of the fitted params.
        xlev: [raw, optional] FIT/APPLY EXTERNALIZATION (§3b gate 6): named object {column_name:
            [levels]} — EXACTLY the 'xlev' field of a PREVIOUS fit. REQUIRED for out-of-sample
            scoring: without it, new data with fewer levels SILENTLY produce FEWER COLUMNS
            (live-verified) and the model's coefficients apply to the wrong positions. Unknown level
            => hard stop.
        expect_columns: [series_codes, optional] Optional column identity check: the 'column_names'
            of the fit. If the produced matrix does not have EXACTLY these columns in this order,
            the node blocks (blocked-by-gate).
        rank_check: [enum, optional] Policy for RANK DEFICIENCY (aliased/empty combinations of
            levels; the linear-model fit does NOT error — it returns SILENTLY NA coefficients).
            'auto' (default) = 'stop' at FIT (a genuine design error) and 'report' at APPLY (when
            xlev is given; there a missing level is normal). 'stop'/'report' = explicit override.
        max_levels: [integer, optional] Maximum levels PER factor (default 30) — a bound against
            level explosion. Default ``30``.
        max_columns: [integer, optional] Maximum columns of the design matrix (default 200). The
            UPPER BOUND is checked BEFORE construction, so that a gigantic matrix is never built.
            Default ``200``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ply_interactions: not implemented."
    )


def ply_model_matrix(
    *,
    data: pd.DataFrame,
    formula: str,
    contrasts: Literal["contr.treatment", "contr.sum", "contr.helmert", "contr.poly"] | None = None,
    xlev: Any | None = None,
    expect_columns: Sequence[str] | None = None,
    rank_check: Literal["auto", "stop", "report"] | None = None,
    max_levels: int | None = None,
    max_columns: int | None = None,
) -> dict[str, Any]:
    """Node ``ply_model_matrix`` -- method card #253.

    DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (returning the fitted
    coefficients), INTERACTIONS without a formula surface, an allowlisted formula path, a
    COMBINATORIAL factor.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). Allowed: numeric/categorical/string/logical columns — NOT list-columns, NOT
            NA/Inf in the columns that are used (the model-frame builder SILENTLY DROPS rows and
            breaks the alignment with y). Column names must be valid identifiers.
        formula: [formula, required] ONE-SIDED formula over the columns of 'data' (e.g. "~ gdp *
            regime + I(infl^2)"). WITHOUT a response variable — the node builds a DESIGN MATRIX, it
            does not fit a model. Calls are restricted to the formula allowlist (default-deny,
            enforced TWICE: at the argument boundary and again in the node); every symbol must be a
            column of 'data' ('.' is NOT supported). For simple interactions prefer ply_interactions
            (no formula surface).
        contrasts: [enum, optional] Categorical encoding. 'treatment' (default) = dummy relative to
            the FIRST level; 'sum' = deviations from the mean (useful for interpretable
            interactions); 'helmert' = successive contrasts; 'poly' = orthogonal polynomials for
            ORDERED categories. Returned in the 'contrasts' field — part of the fitted params.
        xlev: [raw, optional] FIT/APPLY EXTERNALIZATION (§3b gate 6): named object {column_name:
            [levels]} — EXACTLY the 'xlev' field of a PREVIOUS fit. REQUIRED for out-of-sample
            scoring: without it, new data with fewer levels SILENTLY produce FEWER COLUMNS
            (live-verified) and the model's coefficients apply to the wrong positions. Unknown level
            => hard stop.
        expect_columns: [series_codes, optional] Optional column identity check: the 'column_names'
            of the fit. If the produced matrix does not have EXACTLY these columns in this order,
            the node blocks (blocked-by-gate).
        rank_check: [enum, optional] Policy for RANK DEFICIENCY (aliased/empty combinations of
            levels; the linear-model fit does NOT error — it returns SILENTLY NA coefficients).
            'auto' (default) = 'stop' at FIT (a genuine design error) and 'report' at APPLY (when
            xlev is given; there a missing level is normal). 'stop'/'report' = explicit override.
        max_levels: [integer, optional] Maximum levels PER factor (default 30) — a bound against
            level explosion. Default ``30``.
        max_columns: [integer, optional] Maximum columns of the design matrix (default 200). The
            UPPER BOUND is checked BEFORE construction, so that a gigantic matrix is never built.
            Default ``200``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ply_model_matrix: not implemented."
    )


def ply_interaction_categorical(
    *,
    data: pd.DataFrame,
    vars: Sequence[str],
    drop: bool | None = None,
    sep: str | None = None,
    lex_order: bool | None = None,
    indicator: bool | None = None,
    max_levels: int | None = None,
) -> dict[str, Any]:
    """Node ``ply_interaction_categorical`` -- method card #253.

    DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (returning the fitted
    coefficients), INTERACTIONS without a formula surface, an allowlisted formula path, a
    COMBINATORIAL factor.

    Category 00-data-utilities; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). Allowed: numeric/categorical/string/logical columns — NOT list-columns, NOT
            NA/Inf in the columns that are used (the model-frame builder SILENTLY DROPS rows and
            breaks the alignment with y). Column names must be valid identifiers.
        vars: [series_codes, required] >= 2 CATEGORICAL columns (categorical/string/logical)
            combined into ONE factor. NUMERIC columns are rejected: the factor-interaction builder
            does NOT error, it makes ONE LEVEL PER UNIQUE VALUE (silent-wrong) — discretize first.
        drop: [boolean, optional] False (default, like base) = keeps ALL level combinations,
            INCLUDING the EMPTY — the empty ones are reported explicitly in
            'empty_levels'/'n_empty_levels'. True = only the combinations that appear. Default
            ``False``.
        sep: [string, optional] Level name separator (default '.'). Default ``'.'``.
        lex_order: [boolean, optional] False (default) = level order following the base convention
            (first factor varies fastest). True = lexicographic. Default ``False``.
        indicator: [boolean, optional] True = also returns the 0/1 indicator matrix (n×levels).
            BLOCKED if EMPTY levels exist: each empty one gives a column FULL OF ZEROS => rank
            deficiency => SILENTLY NA coefficients in lm. Set drop=True. Default ``False``.
        max_levels: [integer, optional] Maximum levels of the combinatorial factor (default 200).
            With drop=False the PRODUCT of the levels is checked BEFORE the call. Default ``200``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ply_interaction_categorical: not implemented."
    )
