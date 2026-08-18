# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``profiling_quality_report`` -- METHOD-SELECTION card #248.

#248 Data profiling / a quality report: a PER-COLUMN profile (type/missing/uniqueness/Joanes-Gill
    moments) + a dataset-level summary + RULE-BASED quality flags (blocker/warning) with a rule and
    a source

Category 01-preparation-prechecks; module ``profiling_quality_report``.

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
    "dp_column_profile",
    "dp_profile",
    "dp_quality_flags",
    "NODE_META",
    "wire_model",
]


def dp_profile(
    *,
    data: pd.DataFrame,
    quantile_type: int | None = None,
    moment_type: Literal["type1", "type2", "type3"] | None = None,
) -> dict[str, Any]:
    """Node ``dp_profile`` -- METHOD-SELECTION card #248.

    Data profiling / a quality report: a PER-COLUMN profile (type/missing/uniqueness/Joanes-Gill
    moments) + a dataset-level summary + RULE-BASED quality flags (blocker/warning) with a rule and
    a source.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / POSIXlt / complex / unknown S3 class (e.g. difftime).
            Non-numeric columns are NEVER silently coerced.
        quantile_type: [integer, optional] Quantile estimator, integer 1..9 (Hyndman & Fan 1996;
            default 7). Returned in the output: two profiles are comparable ONLY under the SAME
            estimator. Default ``7``.
        moment_type: [enum, optional] Skewness/kurtosis estimator per Joanes & Gill (1998), same
            typology as e1071: type1 = moment-based g1/g2 (default); type2 = SAS/SPSS G1/G2
            (unbiased under normality; requires n>=3 / n>=4); type3 = MINITAB/BMDP b1/b2. KURTOSIS
            IS ALWAYS EXCESS (normal => 0).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dp_profile: not implemented. The method card is in ./README.md."
    )


def dp_column_profile(
    *,
    data: pd.DataFrame,
    column: str,
    quantile_type: int | None = None,
    moment_type: Literal["type1", "type2", "type3"] | None = None,
    bins: int | None = None,
    top_n: int | None = None,
) -> dict[str, Any]:
    """Node ``dp_column_profile`` -- METHOD-SELECTION card #248.

    Data profiling / a quality report: a PER-COLUMN profile (type/missing/uniqueness/Joanes-Gill
    moments) + a dataset-level summary + RULE-BASED quality flags (blocker/warning) with a rule and
    a source.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / POSIXlt / complex / unknown S3 class (e.g. difftime).
            Non-numeric columns are NEVER silently coerced.
        column: [string, required] ONE non-empty column name that EXISTS in the dataset (otherwise
            the node blocks and returns the list of available ones).
        quantile_type: [integer, optional] Quantile estimator, integer 1..9 (Hyndman & Fan 1996;
            default 7). Returned in the output: two profiles are comparable ONLY under the SAME
            estimator. Default ``7``.
        moment_type: [enum, optional] Skewness/kurtosis estimator per Joanes & Gill (1998), same
            typology as e1071: type1 = moment-based g1/g2 (default); type2 = SAS/SPSS G1/G2
            (unbiased under normality; requires n>=3 / n>=4); type3 = MINITAB/BMDP b1/b2. KURTOSIS
            IS ALWAYS EXCESS (normal => 0).
        bins: [integer, optional] Number of EQUAL-WIDTH histogram bins for the NUMERIC column
            (default 10; positive integer). the default histogram binning is NOT used (its 'pretty'
            breaks are not reproducible); for a constant column, ONE degenerate bin is returned.
            Default ``10``.
        top_n: [integer, optional] Number of top values of the frequency table for a NON-numeric
            column (default 10). Ordering: descending count, tie-break lexicographically (C-locale,
            radix => locale-independent). Default ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dp_column_profile: not implemented. The method card is in ./README.md."
    )


def dp_quality_flags(
    *,
    data: pd.DataFrame,
    max_missing_pct: float | None = None,
    max_unique_ratio: float | None = None,
    min_rows: int | None = None,
    quantile_type: int | None = None,
    moment_type: Literal["type1", "type2", "type3"] | None = None,
) -> dict[str, Any]:
    """Node ``dp_quality_flags`` -- METHOD-SELECTION card #248.

    Data profiling / a quality report: a PER-COLUMN profile (type/missing/uniqueness/Joanes-Gill
    moments) + a dataset-level summary + RULE-BASED quality flags (blocker/warning) with a rule and
    a source.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame (rows = observations, columns =
            variables). >= 1 row AND >= 1 column ARE REQUIRED, non-empty and NON-DUPLICATE column
            names, NO list-column / POSIXlt / complex / unknown S3 class (e.g. difftime).
            Non-numeric columns are NEVER silently coerced.
        max_missing_pct: [number, optional] Missing-value threshold per column as a PERCENTAGE
            [0,100] (default 10) above which a 'high_missing' flag is issued (warning); a column
            missing IN ITS ENTIRETY is always blocker. Default ``10``.
        max_unique_ratio: [number, optional] Threshold for the ratio of unique/valid values in the
            (0,1] (default 0.95) for a CATEGORICAL column: above this the column looks like an
            identifier (id), not a variable. Default ``0.95``.
        min_rows: [integer, optional] Minimum row count (default 8) below which a 'few_rows' flag is
            issued: the normality tests have a per-test min-n (ad/cvm n>7· lillie n>4· sf/shapiro
            n>=5/3). Default ``8``.
        quantile_type: [integer, optional] Quantile estimator, integer 1..9 (Hyndman & Fan 1996;
            default 7). Returned in the output: two profiles are comparable ONLY under the SAME
            estimator. Default ``7``.
        moment_type: [enum, optional] Skewness/kurtosis estimator per Joanes & Gill (1998), same
            typology as e1071: type1 = moment-based g1/g2 (default); type2 = SAS/SPSS G1/G2
            (unbiased under normality; requires n>=3 / n>=4); type3 = MINITAB/BMDP b1/b2. KURTOSIS
            IS ALWAYS EXCESS (normal => 0).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "dp_quality_flags: not implemented. The method card is in ./README.md."
    )
