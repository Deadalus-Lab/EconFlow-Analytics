# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``design_complex_survey`` -- METHOD-SELECTION card #232.

#232 Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc)

Category 25-expectations-surveys; module ``design_complex_survey``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "sv_svyby",
    "sv_svydesign",
    "sv_svymean",
    "sv_svyquantile",
    "sv_svytotal",
    "NODE_META",
    "wire_model",
]


def sv_svydesign(
    *,
    df: pd.DataFrame,
    ids: Sequence[str] | None = None,
    strata: Sequence[str] | None = None,
    weights: Sequence[str] | None = None,
    probs: Sequence[str] | None = None,
    fpc: Sequence[str] | None = None,
    nest: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_svydesign`` -- METHOD-SELECTION card #232.

    Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc).

    Category 25-expectations-surveys; memory class ``light``.

    Registers its result under ``design``, so a later node can consume it as a handle.

    Args:
        df: [df_handle, required] Handle to a survey-microdata DataFrame (one row per respondent; >=
            2 rows). The data pass ONLY as a handle; ids/strata/weights/probs/fpc are its column
            NAMES.
        ids: [series_codes, optional] Cluster/PSU identifiers: "1" (or "0") for NO clusters
            (default), or the name(s) of cluster columns (multistage sampling, from the broadest to
            the narrowest stage). Default ``'1'``.
        strata: [series_codes, optional] Stratification column names (one stratified estimator per
            stratum); None = no strata. Requires nest=True if the cluster ids are reused within
            strata.
        weights: [series_codes, optional] ONE sampling-weights column (design weight = 1/prob;
            positive, finite). Mutually exclusive with 'probs'. None & without probs =>
            equal-weighted SRS.
        probs: [series_codes, optional] ONE column of selection probabilities in (0,1] (weights =
            1/probs); mutually exclusive with 'weights'.
        fpc: [series_codes, optional] Finite population correction: column(s) with population size
            (or sampling fraction) per stage; reduces the SE when the sample is a large fraction of
            the population. None = with-replacement (without fpc).
        nest: [boolean, optional] True => the cluster ids are nested within the strata (re-labelling
            per stratum). Default False. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_svydesign: not implemented. The method card is in ./README.md."
    )


def sv_svymean(
    *,
    design: Any,
    vars: Sequence[str],
    deff: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_svymean`` -- METHOD-SELECTION card #232.

    Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc).

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        design: [raw_handle, required] Handle to the survey.design from sv_svydesign (register field
            'design').
        vars: [series_codes, required] NUMERIC variables of the design for the mean estimation (one
            or more column names; factor is not supported here).
        deff: [boolean, optional] Return the design effect (Var_design / Var_SRS); >1 => the
            clustering/weighting increases the variance. Default True. Default ``True``.
        na_rm: [boolean, optional] Removal of NA in the variables before the estimation. Default
            False. Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_svymean: not implemented. The method card is in ./README.md."
    )


def sv_svytotal(
    *,
    design: Any,
    vars: Sequence[str],
    deff: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_svytotal`` -- METHOD-SELECTION card #232.

    Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc).

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        design: [raw_handle, required] Handle to the survey.design from sv_svydesign (register field
            'design').
        vars: [series_codes, required] NUMERIC variables for the population TOTAL estimation
            (population total; weighted sum).
        deff: [boolean, optional] Design effect (see sv_svymean). Default True. Default ``True``.
        na_rm: [boolean, optional] Removal of NA before the estimation. Default False. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_svytotal: not implemented. The method card is in ./README.md."
    )


def sv_svyquantile(
    *,
    design: Any,
    vars: Sequence[str],
    quantiles: Sequence[float] | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_svyquantile`` -- METHOD-SELECTION card #232.

    Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc).

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        design: [raw_handle, required] Handle to the survey.design from sv_svydesign (register field
            'design').
        vars: [series_codes, required] NUMERIC variables for the weighted quantiles estimation.
        quantiles: [num_array, optional] Quantile probabilities STRICTLY in (0,1) (default
            [0.25,0.5,0.75]); 0 or 1 are rejected (infinite quantiles).
        na_rm: [boolean, optional] Removal of NA before the estimation. Default False. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_svyquantile: not implemented. The method card is in ./README.md."
    )


def sv_svyby(
    *,
    design: Any,
    vars: Sequence[str],
    by: Sequence[str],
    statistic: Literal["svymean", "svytotal"] | None = None,
    deff: bool | None = None,
    na_rm: bool | None = None,
) -> dict[str, Any]:
    """Node ``sv_svyby`` -- METHOD-SELECTION card #232.

    Design-based complex-survey estimation (means/totals/quantiles/domains) with correct design
    variances (stratification, clustering, weights, fpc).

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        design: [raw_handle, required] Handle to the survey.design from sv_svydesign (register field
            'design').
        vars: [series_codes, required] NUMERIC variables for the per-domain estimation.
        by: [series_codes, required] >= 1 grouping column of the design (domains/subpopulations);
            the estimation is repeated per level combination with the correct design SE per domain.
        statistic: [enum, optional] Statistic per domain: svymean (default) or svytotal.
        deff: [boolean, optional] Design effect per domain. Default False. Default ``False``.
        na_rm: [boolean, optional] Removal of NA before the estimation. Default False. Default
            ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "sv_svyby: not implemented. The method card is in ./README.md."
    )
