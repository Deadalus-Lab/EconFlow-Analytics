# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``missingness_patterns_pattern`` -- METHOD-SELECTION card #249.

#249 Analysis of MISSINGNESS PATTERNS (CROSS-VARIABLE): a pattern matrix 1=observed/0=missing +
    counts per pattern + an EXACT MONOTONICITY check (Van Buuren) · NA runs/spans per variable (a
    ragged edge / mixed frequency) · co-missingness per PAIR (rr/rm/mr/mm)

Category 01-preparation-prechecks; module ``missingness_patterns_pattern``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "mp_pairs",
    "mp_pattern",
    "mp_runs",
    "NODE_META",
    "wire_model",
]


def mp_pattern(
    *,
    data: pd.DataFrame,
    time: str | None = None,
    sort_by: Literal["count", "missingness"] | None = None,
) -> dict[str, Any]:
    """Node ``mp_pattern`` -- METHOD-SELECTION card #249.

    Analysis of MISSINGNESS PATTERNS (CROSS-VARIABLE): a pattern matrix 1=observed/0=missing +
    counts per pattern + an EXACT MONOTONICITY check (Van Buuren) · NA runs/spans per variable (a
    ragged edge / mixed frequency) · co-missingness per PAIR (rr/rm/mr/mm).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations/TIME, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / matrix-column / DataFrame-column / POSIXlt / complex. Missing =
            is.na: NaN COUNTS as missing, ±Inf does NOT. NO imputation and no dropping — the node
            only DIAGNOSES.
        time: [string, optional] OPTIONAL name of the time-axis column
            (Date/POSIXct/numeric/character). If given: it is EXCLUDED from the variables (it is the
            axis, not a variable) and is used as the span LABEL. GATES: it exists, NO NA, STRICTLY
            INCREASING (otherwise "row order = time" is False and the NA runs are MEANINGLESS), and
            >= 1 variable remains after removing it.
        sort_by: [enum, optional] EXPLICIT ordering of the ROWS of the pattern matrix (the COLUMNS
            ALWAYS remain in input order): 'count' (default) = DESCENDING row count -> ASCENDING
            count of missing variables -> ASCENDING pattern key; 'missingness' = the meaning of the
            mice («increasing amounts of missing information") BUT with a full tie-break: ASCENDING
            missing -> DESCENDING count -> ASCENDING key. Both are TOTAL orderings (radix,
            locale-independent) => DETERMINISTIC.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mp_pattern: not implemented. The method card is in ./README.md."
    )


def mp_runs(
    *,
    data: pd.DataFrame,
    time: str | None = None,
) -> dict[str, Any]:
    """Node ``mp_runs`` -- METHOD-SELECTION card #249.

    Analysis of MISSINGNESS PATTERNS (CROSS-VARIABLE): a pattern matrix 1=observed/0=missing +
    counts per pattern + an EXACT MONOTONICITY check (Van Buuren) · NA runs/spans per variable (a
    ragged edge / mixed frequency) · co-missingness per PAIR (rr/rm/mr/mm).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations/TIME, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / matrix-column / DataFrame-column / POSIXlt / complex. Missing =
            is.na: NaN COUNTS as missing, ±Inf does NOT. NO imputation and no dropping — the node
            only DIAGNOSES.
        time: [string, optional] OPTIONAL name of the time-axis column
            (Date/POSIXct/numeric/character). If given: it is EXCLUDED from the variables (it is the
            axis, not a variable) and is used as the span LABEL. GATES: it exists, NO NA, STRICTLY
            INCREASING (otherwise "row order = time" is False and the NA runs are MEANINGLESS), and
            >= 1 variable remains after removing it.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mp_runs: not implemented. The method card is in ./README.md."
    )


def mp_pairs(
    *,
    data: pd.DataFrame,
    time: str | None = None,
) -> dict[str, Any]:
    """Node ``mp_pairs`` -- METHOD-SELECTION card #249.

    Analysis of MISSINGNESS PATTERNS (CROSS-VARIABLE): a pattern matrix 1=observed/0=missing +
    counts per pattern + an EXACT MONOTONICITY check (Van Buuren) · NA runs/spans per variable (a
    ragged edge / mixed frequency) · co-missingness per PAIR (rr/rm/mr/mm).

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations/TIME, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / matrix-column / DataFrame-column / POSIXlt / complex. Missing =
            is.na: NaN COUNTS as missing, ±Inf does NOT. NO imputation and no dropping — the node
            only DIAGNOSES.
        time: [string, optional] OPTIONAL name of the time-axis column
            (Date/POSIXct/numeric/character). If given: it is EXCLUDED from the variables (it is the
            axis, not a variable) and is used as the span LABEL. GATES: it exists, NO NA, STRICTLY
            INCREASING (otherwise "row order = time" is False and the NA runs are MEANINGLESS), and
            >= 1 variable remains after removing it.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "mp_pairs: not implemented. The method card is in ./README.md."
    )
