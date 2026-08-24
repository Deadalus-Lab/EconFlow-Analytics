# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``categorical_association_contingency`` -- method card #257.

#257 Categorical association / contingency tables: a chi-squared test of independence, Fisher's
    exact test, nominal vs ordinal association measures with CIs

Category 25-expectations-surveys; module ``categorical_association_contingency``.

Reference implementation: scipy.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

from econflow_engine.generated.args.c25_expectations_surveys import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ca_associations",
    "ca_chisq",
    "ca_contingency",
    "ca_fisher",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def ca_contingency(
    *,
    x: Any,
    y: Any,
    x_name: str | None = None,
    y_name: str | None = None,
    x_levels: Sequence[float] | None = None,
    y_levels: Sequence[float] | None = None,
    x_labels: Sequence[str] | None = None,
    y_labels: Sequence[str] | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    max_levels: int | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
) -> dict[str, Any]:
    """Node ``ca_contingency`` -- method card #257.

    Categorical association / contingency tables: a chi-squared test of independence, Fisher's exact
    test, nominal vs ordinal association measures with CIs.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a NUMERICALLY CODED VECTOR of OBSERVATIONS for the ROW
            variable (one INTEGER category code PER RESPONDENT; e.g. down=1, same=2, up=3). NOT the
            ready-made contingency table — the table is built by the node. NOT a CONTINUOUS variable
            (discretize first: 00-data-utilities/binning). NOT a factor (hard stop): give int(x) —
            codes 1..k in the order of the levels — and levels(x) as 'x_labels'. CROSS-SECTION ONLY:
            series handles ARE REJECTED and a Ljung-Box whiteness precheck runs.
        y: [raw_handle, required] Handle to the CORRESPONDING coded vector for the COLUMN variable.
            SAME length as 'x' — PAIRED answers from the SAME respondents.
        x_name: [string, optional] LABEL of the ROW variable (NOT data; default 'x'). Used in the
            axis labels and in the cross-section gate's diagnostics. Must differ from 'y_name'.
            Default ``'x'``.
        y_name: [string, optional] LABEL of the COLUMN variable (NOT data; default 'y'). Default
            ``'y'``.
        x_levels: [num_array, optional] OPTIONAL COMPLETE set of INTEGER codes of the row variable
            (e.g. [1,2,3,4] when one questionnaire option was NOT selected by anyone). Must be a
            SUPERSET of the observed codes — otherwise the categorical encoder would SILENTLY turn
            the observations into NA. Useful for IDENTICAL coding between two waves of the same
            survey (comparable cell-by-cell tables). Omitting it, the levels result from the
            OBSERVED codes.
        y_levels: [num_array, optional] Same as 'x_levels', for the COLUMN variable.
        x_labels: [series_codes, optional] OPTIONAL category LABELS (NOT data), ONE-TO-ONE with the
            SORTED codes (e.g. ['down','same','up']). Must be unique and non-empty (duplicates WOULD
            MERGE categories). Default: '<x_name>=<code>'.
        y_labels: [series_codes, optional] Same as 'x_labels', for the COLUMN variable.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the
            cross-tabulation routine SILENTLY drops NA (NA dropped), so the reported n would not be
            the input's n. With 'omit' the removal happens EXPLICITLY PER PAIR and the count is
            returned (n_na). Default ``'fail'``.
        max_levels: [integer, optional] Maximum number of categories PER variable (default 20;
            permitted [2, 50]). Many levels => a sparse table (the chi-square approximation
            collapses) and the EXACT Fisher blows up ("FEXACT error"). It is ALSO a safety net
            against accidentally passing a CONTINUOUS variable. Default ``20``.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0,1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS (observations) carry ORDER
            meaning? True (default, conservative) => the Ljung-Box precheck RUNS. False => genuine
            cross-section (EXCHANGEABLE rows — e.g. survey respondents) and the precheck is
            EXPLICITLY skipped (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER —
            chi-square/Fisher do NOT. The rejection of series handles/series ALWAYS applies. Default
            ``True``.

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
        "ca_contingency: not implemented."
    )


def ca_chisq(
    *,
    x: Any,
    y: Any,
    x_name: str | None = None,
    y_name: str | None = None,
    x_levels: Sequence[float] | None = None,
    y_levels: Sequence[float] | None = None,
    x_labels: Sequence[str] | None = None,
    y_labels: Sequence[str] | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    max_levels: int | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
    alpha: float | None = None,
    rule: Literal["cochran", "strict"] | None = None,
    correct: bool | None = None,
    simulate_p_value: bool | None = None,
    B: int | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``ca_chisq`` -- method card #257.

    Categorical association / contingency tables: a chi-squared test of independence, Fisher's exact
    test, nominal vs ordinal association measures with CIs.

    Category 25-expectations-surveys; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to a NUMERICALLY CODED VECTOR of OBSERVATIONS for the ROW
            variable (one INTEGER category code PER RESPONDENT; e.g. down=1, same=2, up=3). NOT the
            ready-made contingency table — the table is built by the node. NOT a CONTINUOUS variable
            (discretize first: 00-data-utilities/binning). NOT a factor (hard stop): give int(x) —
            codes 1..k in the order of the levels — and levels(x) as 'x_labels'. CROSS-SECTION ONLY:
            series handles ARE REJECTED and a Ljung-Box whiteness precheck runs.
        y: [raw_handle, required] Handle to the CORRESPONDING coded vector for the COLUMN variable.
            SAME length as 'x' — PAIRED answers from the SAME respondents.
        x_name: [string, optional] LABEL of the ROW variable (NOT data; default 'x'). Used in the
            axis labels and in the cross-section gate's diagnostics. Must differ from 'y_name'.
            Default ``'x'``.
        y_name: [string, optional] LABEL of the COLUMN variable (NOT data; default 'y'). Default
            ``'y'``.
        x_levels: [num_array, optional] OPTIONAL COMPLETE set of INTEGER codes of the row variable
            (e.g. [1,2,3,4] when one questionnaire option was NOT selected by anyone). Must be a
            SUPERSET of the observed codes — otherwise the categorical encoder would SILENTLY turn
            the observations into NA. Useful for IDENTICAL coding between two waves of the same
            survey (comparable cell-by-cell tables). Omitting it, the levels result from the
            OBSERVED codes.
        y_levels: [num_array, optional] Same as 'x_levels', for the COLUMN variable.
        x_labels: [series_codes, optional] OPTIONAL category LABELS (NOT data), ONE-TO-ONE with the
            SORTED codes (e.g. ['down','same','up']). Must be unique and non-empty (duplicates WOULD
            MERGE categories). Default: '<x_name>=<code>'.
        y_labels: [series_codes, optional] Same as 'x_labels', for the COLUMN variable.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the
            cross-tabulation routine SILENTLY drops NA (NA dropped), so the reported n would not be
            the input's n. With 'omit' the removal happens EXPLICITLY PER PAIR and the count is
            returned (n_na). Default ``'fail'``.
        max_levels: [integer, optional] Maximum number of categories PER variable (default 20;
            permitted [2, 50]). Many levels => a sparse table (the chi-square approximation
            collapses) and the EXACT Fisher blows up ("FEXACT error"). It is ALSO a safety net
            against accidentally passing a CONTINUOUS variable. Default ``20``.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0,1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS (observations) carry ORDER
            meaning? True (default, conservative) => the Ljung-Box precheck RUNS. False => genuine
            cross-section (EXCHANGEABLE rows — e.g. survey respondents) and the precheck is
            EXPLICITLY skipped (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER —
            chi-square/Fisher do NOT. The rejection of series handles/series ALWAYS applies. Default
            ``True``.
        alpha: [number, optional] Significance level OF THE TEST in the OPEN interval (0,1) —
            default 0.05. Determines ONLY the 'decision' field; it does NOT change the p-value and
            does NOT affect the cross-section gate (which has its OWN 'gate_alpha'). Default
            ``0.05``.
        rule: [enum, optional] Rule for ACCEPTABLE expected frequencies (HARD gate — the usual
            chi-square routines only warn that the approximation may be incorrect). 'cochran'
            (default): no expected value < 1 AND <= 20% of cells < 5 (Cochran 1954). 'strict': NO
            expected value < 5. Failure => use ca_fisher or simulate_p_value=True. Default
            ``'cochran'``.
        correct: [boolean, optional] Yates continuity correction (default True). Applies ONLY to 2x2
            — elsewhere it is ignored SILENTLY by the usual routines; the output field
            'yates_applied' says what ACTUALLY happened. AFFECTS ONLY 'statistic'/'p_value' (the
            TEST's statistic). THE SIZE MEASURES ARE NOT: 'cramers_v' and 'contribution_share' are
            ALWAYS computed from the UNCORRECTED Pearson X² ('statistic_pearson'; Cramér 1946
            §21.9), so they COINCIDE with ca_associations. Default ``True``.
        simulate_p_value: [boolean, optional] Monte-Carlo p-value instead of the asymptotic/exact
            path (default False). It is the WAY OUT when the Cochran rule rejects the chi-square (it
            does not rely on the asymptotic) or when the exact Fisher does not fit in memory
            ("FEXACT error"). Requires a seed for determinism. Default ``False``.
        B: [integer, optional] Monte-Carlo replications when simulate_p_value=True (default 2000;
            minimum 100). Ignored otherwise. Default ``2000``.
        seed: [integer, optional] Seed of the Monte-Carlo path (default 1234). The call runs with
            the seed set AND restores the caller's RNG state => a REPRODUCIBLE p-value without
            contaminating the RNG stream. Ignored on the algebraic (deterministic) paths. Default
            ``1234``.

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
        "ca_chisq: not implemented."
    )


def ca_fisher(
    *,
    x: Any,
    y: Any,
    x_name: str | None = None,
    y_name: str | None = None,
    x_levels: Sequence[float] | None = None,
    y_levels: Sequence[float] | None = None,
    x_labels: Sequence[str] | None = None,
    y_labels: Sequence[str] | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    max_levels: int | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
    alpha: float | None = None,
    alternative: Literal["two.sided", "less", "greater"] | None = None,
    conf_level: float | None = None,
    simulate_p_value: bool | None = None,
    B: int | None = None,
    workspace: float | None = None,
    seed: int | None = None,
) -> dict[str, Any]:
    """Node ``ca_fisher`` -- method card #257.

    Categorical association / contingency tables: a chi-squared test of independence, Fisher's exact
    test, nominal vs ordinal association measures with CIs.

    Category 25-expectations-surveys; memory class ``heavy``.

    Args:
        x: [raw_handle, required] Handle to a NUMERICALLY CODED VECTOR of OBSERVATIONS for the ROW
            variable (one INTEGER category code PER RESPONDENT; e.g. down=1, same=2, up=3). NOT the
            ready-made contingency table — the table is built by the node. NOT a CONTINUOUS variable
            (discretize first: 00-data-utilities/binning). NOT a factor (hard stop): give int(x) —
            codes 1..k in the order of the levels — and levels(x) as 'x_labels'. CROSS-SECTION ONLY:
            series handles ARE REJECTED and a Ljung-Box whiteness precheck runs.
        y: [raw_handle, required] Handle to the CORRESPONDING coded vector for the COLUMN variable.
            SAME length as 'x' — PAIRED answers from the SAME respondents.
        x_name: [string, optional] LABEL of the ROW variable (NOT data; default 'x'). Used in the
            axis labels and in the cross-section gate's diagnostics. Must differ from 'y_name'.
            Default ``'x'``.
        y_name: [string, optional] LABEL of the COLUMN variable (NOT data; default 'y'). Default
            ``'y'``.
        x_levels: [num_array, optional] OPTIONAL COMPLETE set of INTEGER codes of the row variable
            (e.g. [1,2,3,4] when one questionnaire option was NOT selected by anyone). Must be a
            SUPERSET of the observed codes — otherwise the categorical encoder would SILENTLY turn
            the observations into NA. Useful for IDENTICAL coding between two waves of the same
            survey (comparable cell-by-cell tables). Omitting it, the levels result from the
            OBSERVED codes.
        y_levels: [num_array, optional] Same as 'x_levels', for the COLUMN variable.
        x_labels: [series_codes, optional] OPTIONAL category LABELS (NOT data), ONE-TO-ONE with the
            SORTED codes (e.g. ['down','same','up']). Must be unique and non-empty (duplicates WOULD
            MERGE categories). Default: '<x_name>=<code>'.
        y_labels: [series_codes, optional] Same as 'x_labels', for the COLUMN variable.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the
            cross-tabulation routine SILENTLY drops NA (NA dropped), so the reported n would not be
            the input's n. With 'omit' the removal happens EXPLICITLY PER PAIR and the count is
            returned (n_na). Default ``'fail'``.
        max_levels: [integer, optional] Maximum number of categories PER variable (default 20;
            permitted [2, 50]). Many levels => a sparse table (the chi-square approximation
            collapses) and the EXACT Fisher blows up ("FEXACT error"). It is ALSO a safety net
            against accidentally passing a CONTINUOUS variable. Default ``20``.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0,1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS (observations) carry ORDER
            meaning? True (default, conservative) => the Ljung-Box precheck RUNS. False => genuine
            cross-section (EXCHANGEABLE rows — e.g. survey respondents) and the precheck is
            EXPLICITLY skipped (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER —
            chi-square/Fisher do NOT. The rejection of series handles/series ALWAYS applies. Default
            ``True``.
        alpha: [number, optional] Significance level OF THE TEST in the OPEN interval (0,1) —
            default 0.05. Determines ONLY the 'decision' field; it does NOT change the p-value and
            does NOT affect the cross-section gate (which has its OWN 'gate_alpha'). Default
            ``0.05``.
        alternative: [enum, optional] Alternative hypothesis (default 'two.sided'). ONE-SIDED ONLY
            in 2x2: the exact test routine SILENTLY ignores alternative in rxc (it returns the
            two.sided p-value) — the node blocks it explicitly. Incompatible with
            simulate_p_value=True. Default ``'two.sided'``.
        conf_level: [number, optional] Confidence level of the odds ratio CI (default 0.95; 2x2 ONLY
            — an odds ratio is not defined for larger tables). Default ``0.95``.
        simulate_p_value: [boolean, optional] Monte-Carlo p-value instead of the asymptotic/exact
            path (default False). It is the WAY OUT when the Cochran rule rejects the chi-square (it
            does not rely on the asymptotic) or when the exact Fisher does not fit in memory
            ("FEXACT error"). Requires a seed for determinism. Default ``False``.
        B: [integer, optional] Monte-Carlo replications when simulate_p_value=True (default 2000;
            minimum 100). Ignored otherwise. Default ``2000``.
        workspace: [number, optional] Working memory of the exact FEXACT algorithm (documented
            default 2e5; minimum 1e4). LIVE-VERIFIED: 4x4 with n=300 blows up with "FEXACT error 6.
            LDKEY=620 is too small" at 2e5; SOME such tables pass with 2e6, DENSER ones blow up
            THERE too ("FEXACT error 7"); 12x12 blows up even at 2e8 => then ONLY simulate_p_value.
            Default ``200000``.
        seed: [integer, optional] Seed of the Monte-Carlo path (default 1234). The call runs with
            the seed set AND restores the caller's RNG state => a REPRODUCIBLE p-value without
            contaminating the RNG stream. Ignored on the algebraic (deterministic) paths. Default
            ``1234``.

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
        "ca_fisher: not implemented."
    )


def ca_associations(
    *,
    x: Any,
    y: Any,
    x_name: str | None = None,
    y_name: str | None = None,
    x_levels: Sequence[float] | None = None,
    y_levels: Sequence[float] | None = None,
    x_labels: Sequence[str] | None = None,
    y_labels: Sequence[str] | None = None,
    na_action: Literal["fail", "omit"] | None = None,
    max_levels: int | None = None,
    lb_lag: int | None = None,
    gate_alpha: float | None = None,
    ordered: bool | None = None,
    scale: Literal["nominal", "ordinal"] | None = None,
    conf_level: float | None = None,
    cramer_method: Literal["ncchisq", "ncchisqadj", "fisher", "fisheradj"] | None = None,
    correct: bool | None = None,
) -> dict[str, Any]:
    """Node ``ca_associations`` -- method card #257.

    Categorical association / contingency tables: a chi-squared test of independence, Fisher's exact
    test, nominal vs ordinal association measures with CIs.

    Category 25-expectations-surveys; memory class ``light``.

    Args:
        x: [raw_handle, required] Handle to a NUMERICALLY CODED VECTOR of OBSERVATIONS for the ROW
            variable (one INTEGER category code PER RESPONDENT; e.g. down=1, same=2, up=3). NOT the
            ready-made contingency table — the table is built by the node. NOT a CONTINUOUS variable
            (discretize first: 00-data-utilities/binning). NOT a factor (hard stop): give int(x) —
            codes 1..k in the order of the levels — and levels(x) as 'x_labels'. CROSS-SECTION ONLY:
            series handles ARE REJECTED and a Ljung-Box whiteness precheck runs.
        y: [raw_handle, required] Handle to the CORRESPONDING coded vector for the COLUMN variable.
            SAME length as 'x' — PAIRED answers from the SAME respondents.
        x_name: [string, optional] LABEL of the ROW variable (NOT data; default 'x'). Used in the
            axis labels and in the cross-section gate's diagnostics. Must differ from 'y_name'.
            Default ``'x'``.
        y_name: [string, optional] LABEL of the COLUMN variable (NOT data; default 'y'). Default
            ``'y'``.
        x_levels: [num_array, optional] OPTIONAL COMPLETE set of INTEGER codes of the row variable
            (e.g. [1,2,3,4] when one questionnaire option was NOT selected by anyone). Must be a
            SUPERSET of the observed codes — otherwise the categorical encoder would SILENTLY turn
            the observations into NA. Useful for IDENTICAL coding between two waves of the same
            survey (comparable cell-by-cell tables). Omitting it, the levels result from the
            OBSERVED codes.
        y_levels: [num_array, optional] Same as 'x_levels', for the COLUMN variable.
        x_labels: [series_codes, optional] OPTIONAL category LABELS (NOT data), ONE-TO-ONE with the
            SORTED codes (e.g. ['down','same','up']). Must be unique and non-empty (duplicates WOULD
            MERGE categories). Default: '<x_name>=<code>'.
        y_labels: [series_codes, optional] Same as 'x_labels', for the COLUMN variable.
        na_action: [enum, optional] EXPLICIT NA policy (default 'fail' = hard stop). the
            cross-tabulation routine SILENTLY drops NA (NA dropped), so the reported n would not be
            the input's n. With 'omit' the removal happens EXPLICITLY PER PAIR and the count is
            returned (n_na). Default ``'fail'``.
        max_levels: [integer, optional] Maximum number of categories PER variable (default 20;
            permitted [2, 50]). Many levels => a sparse table (the chi-square approximation
            collapses) and the EXACT Fisher blows up ("FEXACT error"). It is ALSO a safety net
            against accidentally passing a CONTINUOUS variable. Default ``20``.
        lb_lag: [integer, optional] Lag of the Ljung-Box whiteness precheck (cross-section gate). If
            omitted: the documented rule min(10, n/5) (Hyndman & Athanasopoulos, FPP 3rd ed. §5.4).
            MUST be a positive integer < n.
        gate_alpha: [number, optional] Level OF THE CROSS-SECTION GATE in the OPEN interval (0,1) —
            default 0.05. Rejection threshold ONLY of the Ljung-Box whiteness precheck. ⚠️ It IS a
            TEST OF SIZE gate_alpha: it blocks, by construction, ~gate_alpha of the proportion of
            VALID i.i.d. input (live: n=200 -> 1.6%/5.7%/10.1% at 0.01/0.05/0.10). Hence it is
            DECOUPLED from the test's 'alpha'. Default ``0.05``.
        ordered: [boolean, optional] EXPLICIT declaration: do the ROWS (observations) carry ORDER
            meaning? True (default, conservative) => the Ljung-Box precheck RUNS. False => genuine
            cross-section (EXCHANGEABLE rows — e.g. survey respondents) and the precheck is
            EXPLICITLY skipped (decision = 'pass-unordered'). ⚠️ Ljung-Box depends on ORDER —
            chi-square/Fisher do NOT. The rejection of series handles/series ALWAYS applies. Default
            ``True``.
        scale: [enum, optional] MEASUREMENT SCALE of the categories — NEVER guessed (default
            'nominal' = safe). With 'ordinal', the ORDINAL measures are added (Goodman-Kruskal
            Gamma, Kendall tau-b, Stuart tau-c, Somers' D, Pearson/Spearman correlation), which
            presuppose that the CODES ENCODE ORDER; on a nominal scale they are uninterpretable (the
            sign changes with the arbitrary order of the categories). CAUTION: Goodman-Kruskal TAU
            is a NOMINAL PRE measure and is ALWAYS returned. Default ``'nominal'``.
        conf_level: [number, optional] Confidence level of the CI of ALL the measures (default
            0.95). Default ``0.95``.
        cramer_method: [enum, optional] Confidence interval method of the Cramér's V (DescTools·
            default 'ncchisq' = non-central chi-square). 'fisher' is the Fisher z-transformation —
            NO simulation, all options are DETERMINISTIC. Does NOT change the estimate. Default
            ``'ncchisq'``.
        correct: [boolean, optional] Yates continuity correction on the chi-square-based measures (V
            / C / T; default False). Allowed ONLY in 2x2 — elsewhere the usual implementations
            ignore it SILENTLY, so this node errors explicitly instead. Default ``False``.

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
        "ca_associations: not implemented."
    )
