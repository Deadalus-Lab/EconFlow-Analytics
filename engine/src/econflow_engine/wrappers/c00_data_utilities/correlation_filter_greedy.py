# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``correlation_filter_greedy`` -- method card #252.

#252 CORRELATION FILTER: greedy removal of highly correlated variables (over a VALIDATED correlation
    matrix) + an out-of-sample APPLY with the fitted column names

Category 00-data-utilities; module ``correlation_filter_greedy``.

Reference implementation: 10.1007/978-1-4614-6849-3.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import numpy as np

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "cf_cor_matrix",
    "cf_filter",
    "cf_find_correlation",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def cf_cor_matrix(
    *,
    x: np.ndarray,
    method: Literal["pearson", "spearman", "kendall"] | None = None,
) -> dict[str, Any]:
    """Node ``cf_cor_matrix`` -- method card #252.

    CORRELATION FILTER: greedy removal of highly correlated variables (over a VALIDATED correlation
    matrix) + an out-of-sample APPLY with the fitted column names.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×variables matrix (rows =
            observations, columns = candidate variables). It requires p >= 2 columns, n >= 3 rows (n
            = 1 -> the correlation routine gives ALL NA WITHOUT a warning; n = 2 -> every |r| = 1 by
            definition), NO zero-variance column (the cor emits ONLY a warning and returns NA), NO
            NA/NaN/Inf, NO duplicate column names. CROSS-SECTION/PANEL: in LEVELS of non-stationary
            time series the sample correlation does not converge (spurious) — give DIFFERENCES.
        method: [enum, optional] Correlation measure of the correlation routine (default pearson = a
            LINEAR relation). spearman/kendall = a MONOTONE relation on the ranks (robust to
            outliers/non-linearity; kendall is O(n²) and is slow for large n).

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
        "cf_cor_matrix: not implemented."
    )


def cf_find_correlation(
    *,
    cor_matrix: np.ndarray,
    cutoff: float | None = None,
    exact: bool | None = None,
) -> dict[str, Any]:
    """Node ``cf_find_correlation`` -- method card #252.

    CORRELATION FILTER: greedy removal of highly correlated variables (over a VALIDATED correlation
    matrix) + an out-of-sample APPLY with the fitted column names.

    Category 00-data-utilities; memory class ``light``.

    Args:
        cor_matrix: [matrix_handle, required] Handle to a p×p CORRELATION MATRIX — NOT raw data
            (typically the 'cor' of a cf_cor_matrix node). It is checked to be SQUARE, SYMMETRIC,
            with a UNIT diagonal, |r| <= 1 and without NA: the upstream routine SILENTLY accepts raw
            data when exact = False and returns a result as if they were correlations.
        cutoff: [number, optional] Threshold of the ABSOLUTE pairwise correlation (default 0.9;
            typically 0.75-0.95). STRICTLY inside (0,1): the upstream routine does NOT check — with
            cutoff = 1.5 it silently filters NOTHING and with cutoff <= 0 it removes almost
            EVERYTHING. A smaller cutoff => more aggressive filtering. Default ``0.9``.
        exact: [boolean, optional] True (default) = recomputation of the mean correlations at EVERY
            step (removes FEWER variables, slower); False = a fixed ranking (fast for very large p).
            PINNED EXPLICITLY: the upstream default is the column count of x < 100, i.e. the
            ALGORITHM CHANGES at 100 columns and the two paths give DIFFERENT sets => not
            reproducible. Default ``True``.

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
        "cf_find_correlation: not implemented."
    )


def cf_filter(
    *,
    x: np.ndarray,
    cutoff: float | None = None,
    exact: bool | None = None,
    method: Literal["pearson", "spearman", "kendall"] | None = None,
    keep: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``cf_filter`` -- method card #252.

    CORRELATION FILTER: greedy removal of highly correlated variables (over a VALIDATED correlation
    matrix) + an out-of-sample APPLY with the fitted column names.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        x: [matrix_handle, required] Handle to a NUMERIC observations×variables matrix (rows =
            observations, columns = candidate variables). It requires p >= 2 columns, n >= 3 rows (n
            = 1 -> the correlation routine gives ALL NA WITHOUT a warning; n = 2 -> every |r| = 1 by
            definition), NO zero-variance column (the cor emits ONLY a warning and returns NA), NO
            NA/NaN/Inf, NO duplicate column names. CROSS-SECTION/PANEL: in LEVELS of non-stationary
            time series the sample correlation does not converge (spurious) — give DIFFERENCES.
        cutoff: [number, optional] Threshold of the ABSOLUTE pairwise correlation (default 0.9;
            typically 0.75-0.95). STRICTLY inside (0,1): the upstream routine does NOT check — with
            cutoff = 1.5 it silently filters NOTHING and with cutoff <= 0 it removes almost
            EVERYTHING. A smaller cutoff => more aggressive filtering. Default ``0.9``.
        exact: [boolean, optional] True (default) = recomputation of the mean correlations at EVERY
            step (removes FEWER variables, slower); False = a fixed ranking (fast for very large p).
            PINNED EXPLICITLY: the upstream default is the column count of x < 100, i.e. the
            ALGORITHM CHANGES at 100 columns and the two paths give DIFFERENT sets => not
            reproducible. Default ``True``.
        method: [enum, optional] Correlation measure of the correlation routine (default pearson = a
            LINEAR relation). spearman/kendall = a MONOTONE relation on the ranks (robust to
            outliers/non-linearity; kendall is O(n²) and is slow for large n).
        keep: [series_codes, optional] OPTIONAL column names to keep = the 'keep_names' of a
            PREVIOUS fit (fit/apply externalization): it applies THE SAME filter to NEW data WITHOUT
            re-estimation (n >= 1 suffices; cutoff/exact/method are ignored). CRITICAL: if the
            filter is re-estimated on the test set, the set of columns CHANGES and the model breaks.
            Omitting it, the filter IS ESTIMATED.

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
        "cf_filter: not implemented."
    )
