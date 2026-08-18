# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``quantifying_qualitative_survey`` -- METHOD-SELECTION card #231.

#231 Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations
    series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression
    approach, conditional expectations

Category 25-expectations-surveys; module ``quantifying_qualitative_survey``.

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
    "qn_balance",
    "qn_carlson_parkin",
    "qn_conditional_expectations",
    "qn_regression",
    "NODE_META",
    "wire_model",
]


def qn_balance(
    *,
    data: pd.DataFrame,
    forecast_horizon: int,
    first_period: int | None = None,
    last_period: int | None = None,
    growth_limit: float | None = None,
    suppress_warnings: bool | None = None,
) -> dict[str, Any]:
    """Node ``qn_balance`` -- METHOD-SELECTION card #231.

    Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations
    series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression
    approach, conditional expectations.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame {y (numeric realized series, e.g.
            inflation), up, same, down (non-negative shares/counts of respondents who expect y to
            rise/stay the same/fall)}; all 4 columns of the SAME length, >= 3 periods.
        forecast_horizon: [integer, required] Forecast horizon of the survey in periods (positive
            integer): how many periods ahead the qualitative question looks.
        first_period: [integer, optional] Index of the first period of the survey window (positive
            integer); default 1 (bal/cp/ra), 11 (ce, needs history).
        last_period: [integer, optional] Index of the last period of the survey window; default n -
            forecast_horizon. first_period < last_period is required and last_period +
            forecast_horizon <= n.
        growth_limit: [number, optional] Upper bound (cap) on the absolute value of the quantified
            change, for outlier control (default: no bound).
        suppress_warnings: [boolean, optional] Suppression of the package's runtime warnings
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qn_balance: not implemented. The method card is in ./README.md."
    )


def qn_carlson_parkin(
    *,
    data: pd.DataFrame,
    forecast_horizon: int,
    first_period: int | None = None,
    last_period: int | None = None,
    limen_type: (
        Literal[
            "carlson.parkin",
            "weber.fechner",
            "constant",
            "symm.series",
            "asymm.series",
        ]
        | None
    ) = None,
    const_limen: float | None = None,
    user_symm_limen: Sequence[float] | None = None,
    user_upper_limen: Sequence[float] | None = None,
    user_lower_limen: Sequence[float] | None = None,
    correct_zero: bool | None = None,
    correct_by: float | None = None,
    growth_limit: float | None = None,
    distrib_type: Literal["normal", "logistic", "t"] | None = None,
    distrib_mean: float | None = None,
    distrib_sd: float | None = None,
    distrib_log_location: float | None = None,
    distrib_log_scale: float | None = None,
    distrib_t_df: float | None = None,
    suppress_warnings: bool | None = None,
) -> dict[str, Any]:
    """Node ``qn_carlson_parkin`` -- METHOD-SELECTION card #231.

    Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations
    series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression
    approach, conditional expectations.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame {y (numeric realized series, e.g.
            inflation), up, same, down (non-negative shares/counts of respondents who expect y to
            rise/stay the same/fall)}; all 4 columns of the SAME length, >= 3 periods.
        forecast_horizon: [integer, required] Forecast horizon of the survey in periods (positive
            integer): how many periods ahead the qualitative question looks.
        first_period: [integer, optional] Index of the first period of the survey window (positive
            integer); default 1 (bal/cp/ra), 11 (ce, needs history).
        last_period: [integer, optional] Index of the last period of the survey window; default n -
            forecast_horizon. first_period < last_period is required and last_period +
            forecast_horizon <= n.
        limen_type: [enum, optional] Method for computing the indifference limen (default
            carlson.parkin=time-varying symmetric): weber.fechner=proportional to the level;
            constant=fixed (const_limen); symm.series=user symmetric (user_symm_limen);
            asymm.series=user asymmetric (user_upper/lower_limen).
        const_limen: [number, optional] limen_type='constant': fixed limen > 0.
        user_symm_limen: [num_array, optional] limen_type='symm.series': symmetric limen per period,
            of length n.
        user_upper_limen: [num_array, optional] limen_type='asymm.series': upper limen per period,
            of length n.
        user_lower_limen: [num_array, optional] limen_type='asymm.series': lower limen per period,
            of length n.
        correct_zero: [boolean, optional] Correction of zero shares by correct_by so that the
            inversion is defined (Nardo 2003; default True). Default ``True``.
        correct_by: [number, optional] Amount of the zero-shares correction (default 0.01). Default
            ``0.01``.
        growth_limit: [number, optional] Upper bound (cap) on the absolute value of the quantified
            change, for outlier control (default: no bound).
        distrib_type: [enum, optional] Expectations distribution for probability-inversion (default
            normal): normal · logistic · t (Student, with distrib_t_df).
        distrib_mean: [number, optional] Mean of the normal distribution (default 0).
        distrib_sd: [number, optional] Standard deviation of the normal distribution (default 1, >
            0).
        distrib_log_location: [number, optional] Location of the logistic distribution (default 0).
        distrib_log_scale: [number, optional] Scale of the logistic distribution (default 1, > 0).
        distrib_t_df: [number, optional] Degrees of freedom of the Student-t (positive; only for
            distrib_type='t').
        suppress_warnings: [boolean, optional] Suppression of the package's runtime warnings
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qn_carlson_parkin: not implemented. The method card is in ./README.md."
    )


def qn_regression(
    *,
    data: pd.DataFrame,
    forecast_horizon: int,
    first_period: int | None = None,
    last_period: int | None = None,
    distrib_type: Literal["normal", "logistic", "t"] | None = None,
    distrib_mean: float | None = None,
    distrib_sd: float | None = None,
    distrib_log_location: float | None = None,
    distrib_log_scale: float | None = None,
    distrib_t_df: float | None = None,
    growth_limit: float | None = None,
    symmetry_error: Literal["white", "small.sample"] | None = None,
    suppress_warnings: bool | None = None,
) -> dict[str, Any]:
    """Node ``qn_regression`` -- METHOD-SELECTION card #231.

    Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations
    series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression
    approach, conditional expectations.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame {y (numeric realized series, e.g.
            inflation), up, same, down (non-negative shares/counts of respondents who expect y to
            rise/stay the same/fall)}; all 4 columns of the SAME length, >= 3 periods.
        forecast_horizon: [integer, required] Forecast horizon of the survey in periods (positive
            integer): how many periods ahead the qualitative question looks.
        first_period: [integer, optional] Index of the first period of the survey window (positive
            integer); default 1 (bal/cp/ra), 11 (ce, needs history).
        last_period: [integer, optional] Index of the last period of the survey window; default n -
            forecast_horizon. first_period < last_period is required and last_period +
            forecast_horizon <= n.
        distrib_type: [enum, optional] Expectations distribution for probability-inversion (default
            normal): normal · logistic · t (Student, with distrib_t_df).
        distrib_mean: [number, optional] Mean of the normal distribution (default 0).
        distrib_sd: [number, optional] Standard deviation of the normal distribution (default 1, >
            0).
        distrib_log_location: [number, optional] Location of the logistic distribution (default 0).
        distrib_log_scale: [number, optional] Scale of the logistic distribution (default 1, > 0).
        distrib_t_df: [number, optional] Degrees of freedom of the Student-t (positive; only for
            distrib_type='t').
        growth_limit: [number, optional] Upper bound (cap) on the absolute value of the quantified
            change, for outlier control (default: no bound).
        symmetry_error: [enum, optional] Standard errors of the limen-symmetry test (default
            white=heteroskedasticity-consistent· small.sample=HC small-sample correction,
            MacKinnon-White 1985).
        suppress_warnings: [boolean, optional] Suppression of the package's runtime warnings
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qn_regression: not implemented. The method card is in ./README.md."
    )


def qn_conditional_expectations(
    *,
    data: pd.DataFrame,
    forecast_horizon: int,
    first_period: int | None = None,
    last_period: int | None = None,
    exp_horizon_type: Literal["moving", "fix"] | None = None,
    mov_horizon_length: int | None = None,
    fix_horizon_start: int | None = None,
    fix_horizon_end: int | None = None,
    distrib_param: Literal["mean", "median"] | None = None,
    suppress_warnings: bool | None = None,
) -> dict[str, Any]:
    """Node ``qn_conditional_expectations`` -- METHOD-SELECTION card #231.

    Quantifying QUALITATIVE survey expectations (up/same/down shares -> a numeric expectations
    series): the balance approach, Carlson-Parkin (+limen/distribution extensions), the regression
    approach, conditional expectations.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        data: [df_handle, required] Handle to a DataFrame {y (numeric realized series, e.g.
            inflation), up, same, down (non-negative shares/counts of respondents who expect y to
            rise/stay the same/fall)}; all 4 columns of the SAME length, >= 3 periods.
        forecast_horizon: [integer, required] Forecast horizon of the survey in periods (positive
            integer): how many periods ahead the qualitative question looks.
        first_period: [integer, optional] Index of the first period of the survey window (positive
            integer); default 1 (bal/cp/ra), 11 (ce, needs history).
        last_period: [integer, optional] Index of the last period of the survey window; default n -
            forecast_horizon. first_period < last_period is required and last_period +
            forecast_horizon <= n.
        exp_horizon_type: [enum, optional] Experience horizon over the distribution of past
            realizations of y (default moving=rolling window of mov_horizon_length periods;
            fix=fixed window [fix_horizon_start, fix_horizon_end]).
        mov_horizon_length: [integer, optional] exp_horizon_type='moving': length of the rolling
            experience window (positive integer; default 10). Default ``10``.
        fix_horizon_start: [integer, optional] exp_horizon_type='fix': first period of the fixed
            window (default 1). Default ``1``.
        fix_horizon_end: [integer, optional] exp_horizon_type='fix': last period of the fixed window
            (default 10; >= fix_horizon_start). Default ``10``.
        distrib_param: [enum, optional] Distribution parameter of y for the conditional expectation
            (default mean; median more robust to outliers).
        suppress_warnings: [boolean, optional] Suppression of the package's runtime warnings
            (default False). Default ``False``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "qn_conditional_expectations: not implemented. The method card is in ./README.md."
    )
