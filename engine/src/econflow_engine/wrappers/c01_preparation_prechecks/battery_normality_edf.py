# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``battery_normality_edf`` -- METHOD-SELECTION card #247.

#247 A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table

Category 01-preparation-prechecks; module ``battery_normality_edf``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from econflow_engine.generated.args.c01_preparation_prechecks import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "nt_ad_test",
    "nt_cvm_test",
    "nt_lillie_test",
    "nt_normality_battery",
    "nt_pearson_test",
    "nt_sf_test",
    "NODE_META",
    "wire_model",
]


def nt_normality_battery(
    *,
    x: Any,
    tests: Sequence[str] | None = None,
    alpha: float | None = None,
    n_classes: int | None = None,
    adjust: bool | None = None,
    min_expected: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_normality_battery`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        tests: [series_codes, optional] Which tests will run; a subset of
            ['ad','cvm','lillie','pearson','sf'] (default: ALL), without duplicates. The ORDER of
            the OUTPUT is CANONICAL (ad,cvm,lillie,pearson,sf) independent of the order you give
            (determinism). NO silent skip: if a requested test does not meet its min-n (ad/cvm n>7;
            lillie n>4; sf 5<=n<=5000) the call STOPS — remove it EXPLICITLY.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        n_classes: [integer, optional] Number of EQUIPROBABLE classes of the chi-square. Default (if
            omitted) = ceiling(2*n^(2/5)) per Moore (1986). MUST be a positive INTEGER (the package
            silently accepts 4.7 and tabulate silently truncates it), AND df = n_classes-1-2*adjust
            >= 1 (df=0 => p = 0 FOR ANY data), AND n/n_classes >= min_expected (Cochran's rule).
        adjust: [boolean, optional] True (default) => df = n_classes-3 (correction for the 2
            estimated parameters); False => df = n_classes-1. NEITHER of the two IS the correct
            p-value: it lies BETWEEN them (Moore 1986) => run the node BOTH times. Default ``True``.
        min_expected: [number, optional] Minimum EXPECTED frequency per class (>= 1; default 5 =
            Cochran 1954 / Moore 1986 rule). Below this the chi-square approximation does not hold,
            and the usual implementations do not warn => a hard gate with the permitted n_classes
            range in the message. Default ``5``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_normality_battery: not implemented. The method card is in ./README.md."
    )


def nt_ad_test(
    *,
    x: Any,
    alpha: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_ad_test`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_ad_test: not implemented. The method card is in ./README.md."
    )


def nt_cvm_test(
    *,
    x: Any,
    alpha: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_cvm_test`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_cvm_test: not implemented. The method card is in ./README.md."
    )


def nt_lillie_test(
    *,
    x: Any,
    alpha: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_lillie_test`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_lillie_test: not implemented. The method card is in ./README.md."
    )


def nt_pearson_test(
    *,
    x: Any,
    alpha: float | None = None,
    n_classes: int | None = None,
    adjust: bool | None = None,
    min_expected: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_pearson_test`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        n_classes: [integer, optional] Number of EQUIPROBABLE classes of the chi-square. Default (if
            omitted) = ceiling(2*n^(2/5)) per Moore (1986). MUST be a positive INTEGER (the package
            silently accepts 4.7 and tabulate silently truncates it), AND df = n_classes-1-2*adjust
            >= 1 (df=0 => p = 0 FOR ANY data), AND n/n_classes >= min_expected (Cochran's rule).
        adjust: [boolean, optional] True (default) => df = n_classes-3 (correction for the 2
            estimated parameters); False => df = n_classes-1. NEITHER of the two IS the correct
            p-value: it lies BETWEEN them (Moore 1986) => run the node BOTH times. Default ``True``.
        min_expected: [number, optional] Minimum EXPECTED frequency per class (>= 1; default 5 =
            Cochran 1954 / Moore 1986 rule). Below this the chi-square approximation does not hold,
            and the usual implementations do not warn => a hard gate with the permitted n_classes
            range in the message. Default ``5``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_pearson_test: not implemented. The method card is in ./README.md."
    )


def nt_sf_test(
    *,
    x: Any,
    alpha: float | None = None,
    series_name: str | None = None,
) -> dict[str, Any]:
    """Node ``nt_sf_test`` -- METHOD-SELECTION card #247.

    A battery of NORMALITY tests (the composite hypothesis): EDF omnibus tests (Anderson-Darling /
    Cramer-von Mises / Lilliefors) + the Pearson chi-square test on equiprobable classes +
    Shapiro-Francia, with a COMMON alpha and a tidy decision table.

    Category 01-preparation-prechecks; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a UNIVARIATE numeric series (numeric vector or ts) —
            typically model RESIDUALS, returns, or a macro series. FORBIDDEN: matrix/DataFrame (run
            the node per column); NA/NaN (PROJECT POLICY: hard stop — nortest SILENTLY drops them
            while the Jarque-Bera node errors; do imputation first, cat. 00); Inf; zero variance.
        alpha: [number, optional] Significance level in the open interval (0, 1) for the 'decision'
            column (default 0.05). Does NOT change the p-value — only the reject_normality /
            fail_to_reject decision. Default ``0.05``.
        series_name: [string, optional] LABEL of the series in the output (default 'x'; <= 100
            characters). NOT data — fills the data.name of the htest so that the entire vector is
            NOT serialized into JSON. Default ``'x'``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "nt_sf_test: not implemented. The method card is in ./README.md."
    )
