# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``roc_auc_binary`` -- method card #84.

#84 ROC / AUC — binary forecast evaluation

Category 16-limited-dependent; module ``roc_auc_binary``.

Reference implementation: scikit-learn.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "run_roc",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---

import math

import numpy as np
import pandas as pd
from scipy.stats import norm, rankdata

# THE IGNORE IS PER-SITE AND IT IS THE WRONG HOME FOR IT. scikit-learn ships no
# py.typed marker and no stub package worth pinning, exactly like scipy and
# statsmodels -- whose answer is one entry in `[[tool.mypy.overrides]]` in
# engine/pyproject.toml, and `sklearn.*` belongs beside them. That file is owned
# by another change in flight, so the silence is written here instead. When
# `sklearn.*` joins that list this comment and the ignore must go with it in the
# same edit: `--strict` implies `--warn-unused-ignores`, so an ignore left behind
# turns mypy red.
from sklearn.metrics import roc_auc_score, roc_curve  # type: ignore[import-untyped]

from econflow_engine.gates.estimation import (
    refuse_a_combination,
    require_a_declared_option,
    require_an_aligned_index,
    require_finite_estimates,
    require_strictly_inside,
    require_supplied,
)
from econflow_engine.gates.primitives import (
    require_in_range,
    require_min_length,
    require_no_missing,
)

#: The node this module's gate messages name.
_FN = "run_roc"

#: The two orientations, spelled as the card and pROC spell them. ``'<'`` reads
#: "controls below cases", so the HIGHER score belongs to the case, which is the
#: normal reading of a probability score; ``'>'`` is the other way round.
_ASCENDING = "<"
_DESCENDING = ">"

#: The value the caller may send to have the orientation chosen from the data.
#: It is never reported back: the payload always carries the orientation this call
#: RESOLVED, which is what stops an inversion hiding inside a word.
_AUTOMATIC = "auto"

#: The interval's estimator, named in the payload because the standard error of an
#: area is not one quantity. Hanley and McNeil (1982) publish a moment estimator of
#: their own, and it is NOT this one -- see the implementation note.
_INTERVAL_METHOD = "delong"

#: How many levels a binary response has, and how many a refusal names before it
#: stops listing them.
_LEVELS_REQUIRED = 2
_LEVELS_SHOWN = 8

#: What a caller must send in place of an absent ``direction``, and what each value
#: means. Written once because the refusal and the implementation note both use it.
_ORIENTATION_REMEDY = (
    "Send direction='<' when a higher score means a case, which is the normal reading "
    "of a probability; '>' when a lower score does; or 'auto' to have the orientation "
    "chosen as the one giving an area at or above 0.5, which is reported back under "
    "direction so that a label inversion cannot hide inside it."
)


def _declared(argument: str) -> Any:
    """The default ``node-specs.json`` publishes for one argument of this node.

    An omitted optional argument reaches a body as ``None`` -- ``adapt_args`` fills
    in a declared default only when the call comes through the wire, and a direct
    Python call does not. The value is READ FROM THE CONTRACT rather than written
    out here, so the two can never disagree. ``direction`` is absent from that
    mapping, which is why it is refused rather than defaulted.
    """
    return NODE_META[_FN].defaults[argument]


def _index_of(value: Any, length: int) -> pd.Index:
    """The labels the caller gave this argument, or the positions it has instead.

    ``getattr`` GUARDED BY ``isinstance`` AND NOT BY ``hasattr``, because a plain
    Python ``list`` HAS an ``index`` attribute -- the search method -- and a
    ``hasattr`` test would read it as a set of labels.
    """
    index = getattr(value, "index", None)
    return index if isinstance(index, pd.Index) else pd.RangeIndex(length)


def _the_labels(response: Any) -> np.ndarray:
    """The response as a 1-D object array, refused where it is not one.

    THE MISSING-VALUE RULE IS PUT TO A MASK RATHER THAN TO THE RESPONSE, and that
    is the only way this question can be asked here at all. A response is
    legitimately a column of words or of booleans -- card #84 admits "logical,
    numeric 0/1 or categorical/string with 2 levels" -- and
    :func:`~econflow_engine.gates.primitives.require_no_missing` reduces its
    argument to a NUMERIC vector, refusing both dtypes outright. The mask is
    ``nan`` exactly where the response is missing and ``0.0`` everywhere else, so
    one rule answers for every dtype the card admits, and the shape arm answers
    beside it: a frame or a 2-D array produces a 2-D mask and is refused for its
    shape rather than reaching pandas.

    WHY THE QUESTION HAS TO BE ASKED AT ALL, MEASURED against scikit-learn 1.9.0.
    A missing label is not one refusal but two: a float response carrying a ``nan``
    raises ``ValueError: Input y_true contains NaN`` behind ``RuntimeWarning:
    invalid value encountered in cast`` -- and this repository's suite runs under
    ``-W error``, so the warning arrives first and ``sklearn.exceptions`` is not a
    package :func:`~econflow_engine.gates.estimation.is_estimator_refusal` reads as
    an estimator. An OBJECT response carrying ``None`` raises ``ValueError: unknown
    format is not supported`` instead, which names nothing a caller can act on.
    """
    observed = np.asarray(response, dtype=object)
    require_no_missing(np.where(pd.isna(observed), np.nan, 0.0), fn=_FN, arg="response")
    return observed


def _the_levels_label(distinct: list[Any]) -> str:
    """The argument label the level-count rule refuses under.

    THE LIST IS BUILT ONLY WHERE IT WILL BE READ, AND IT IS CAPPED. What a caller
    needs first is which values were found, so the message names them -- but a
    response is DATA rather than a schema, and a column handed to this node by
    mistake can carry as many distinct values as it has rows. Rendering and sorting
    all of them on the PASSING path would be work done for a message nobody sees,
    and putting all of them on the wire would answer a two-level question with a
    dump of the input.
    """
    if len(distinct) == _LEVELS_REQUIRED:
        return "the number of distinct levels in response"
    shown = sorted(distinct, key=repr)[:_LEVELS_SHOWN]
    beyond = len(distinct) - len(shown)
    tail = "" if beyond == 0 else f" and {beyond} more"
    return f"the number of distinct levels in response, of which {shown}{tail}"


def _the_levels(observed: np.ndarray) -> tuple[Any, Any]:
    """The control level and the case level, in that order. Exactly two, and ordered.

    TWO SILENT WRONGS AND ONE CRASH, all measured against scikit-learn 1.9.0.
    A response of ONE level returns ``nan`` from ``roc_auc_score`` behind
    ``UndefinedMetricWarning: Only one class is present in y_true``, and a
    false-positive rate that is ``nan`` in every row from ``roc_curve`` behind a
    warning of its own -- so under warnings-as-warnings the area reaches the wire as
    ``null`` and under this suite's ``-W error`` it is a crash. A response of THREE
    levels raises ``ValueError: multi_class must be in ('ovo', 'ovr')``, a message
    about an argument this node does not carry.

    THE COUNT IS PUT TO THE INCLUSIVE RANGE RULE WITH BOTH BOUNDS AT TWO, which is
    the registered primitive for "this number must lie here" and carries
    ``precondition-domain``. The levels themselves are named in the argument label,
    by :func:`_the_levels_label`, which builds that list only where it is read.

    WHICH LEVEL IS THE CASE IS DECIDED BY ORDER, and the rule is scikit-learn's own:
    ``roc_auc_score`` binarises against ``np.unique``, so the LATER of the two
    labels becomes the case. MEASURED, that is exactly how card #84's critical trap
    fires -- handed the words Hanley and McNeil print, ``roc_auc_score`` returns
    0.10682893847194047 because `normal` sorts after `abnormal` and silently becomes
    the case, while ``roc_curve`` REFUSES the same column outright (``ValueError:
    y_true takes value in {'abnormal', 'normal'} and pos_label is not specified``).
    The two halves of the method disagree about one input. This node applies the one
    rule to both halves and REPORTS it under ``controls_level`` and ``cases_level``.

    AND WHERE THE TWO LEVELS HAVE NO ORDER, THE ANSWER IS A REFUSAL AND NOT A ROW
    ORDER. A column of zeros whose missing values were written as the string ``NA``
    has exactly two levels, and Python answers ``0 < 'NA'`` with a ``TypeError`` --
    which is not a ``GateError`` and would leave this node as a crash through the
    gateway. Falling back to the order the rows arrive in would make which label is
    the case a property of the file rather than of the data.
    """
    distinct = pd.unique(observed).tolist()
    require_in_range(
        float(len(distinct)), low=2.0, high=2.0, fn=_FN, arg=_the_levels_label(distinct)
    )
    try:
        ordered = sorted(distinct)
    except TypeError:
        refuse_a_combination(
            fn=_FN,
            combination=(
                f"ranking the two levels of the response "
                f"({distinct[0]!r} and {distinct[1]!r})"
            ),
            reason=(
                "they have no order between them, and this node decides which label "
                "is the case by taking the higher of the two -- the rule "
                "scikit-learn's own binariser applies. Ranking them by the order the "
                "rows happen to arrive in would make that a property of the file "
                "rather than of the data."
            ),
            remedy=(
                "Give the response a single dtype: two integers, two strings, or a "
                "boolean. If one of the levels is a missing-value marker written as "
                "text, replace it with a real missing value, which is refused rather "
                "than counted as a level."
            ),
        )
    else:
        return ordered[0], ordered[1]


def _the_curve(indicator: np.ndarray, oriented: np.ndarray, direction: str) -> pd.DataFrame:
    """The empirical curve, one row per operating point, on the caller's own scale.

    ``drop_intermediate=False`` IS THE WHOLE REASON THIS FUNCTION EXISTS, because
    the library's default deletes a row of the card's own promise. MEASURED on
    Hanley and McNeil's 109 images: the shipped default returns five thresholds,
    ``[inf, 5, 4, 2, 1]``, and ``drop_intermediate=False`` returns six,
    ``[inf, 5, 4, 3, 2, 1]``. The rating-3 operating point -- `questionable`, the
    middle of the paper's own five-point scale -- is the one that disappears, and
    nothing warns.

    THE FIRST ROW IS DROPPED AND IT IS NOT AN OFF-BY-ONE. ``thresholds[0]`` is
    ``inf`` on every call: it is the operating point at which nothing is called
    positive, and the card asks for the sentinels to be removed. It also cannot be
    reported -- :func:`~econflow_engine.serialize.to_mcp` renders an infinity as
    ``null``, so leaving it in would put a null threshold on the wire beside a
    sensitivity of zero. It is the ONLY non-finite row: every other threshold is a
    value the predictor took, and those are gated finite on the way in.

    ONE CONSEQUENCE, STATED SO NOBODY REDISCOVERS IT: the trapezoid area over the
    rows REPORTED here is not ``auc``, because the origin of the curve went with the
    sentinel. ``auc`` comes from ``roc_auc_score`` over the whole sample and not
    from this frame.

    ``direction='>'`` IS COMPUTED ON THE NEGATED SCORE AND REPORTED ON THE
    CALLER'S. scikit-learn has no orientation argument at all, so the other
    orientation is expressed by negating the score; the thresholds it then returns
    are values of ``-score`` and are negated back, so that every threshold a reader
    sees is a value the predictor actually took. What changes with the orientation
    is what a row MEANS: at ``'<'`` the sensitivity is the share of cases scoring at
    or above the threshold, at ``'>'`` the share scoring at or below it.
    """
    false_positive, true_positive, edges = roc_curve(
        indicator, oriented, pos_label=1.0, drop_intermediate=False
    )
    return pd.DataFrame(
        {
            "threshold": edges[1:] if direction == _ASCENDING else -edges[1:],
            "sensitivity": true_positive[1:],
            "specificity": 1.0 - false_positive[1:],
        }
    )


def _the_best(curve: pd.DataFrame) -> pd.DataFrame:
    """Every row of the curve at the Youden maximum, ties included.

    ``J = sensitivity + specificity - 1`` (Youden 1950), maximised over the rows
    this node REPORTS rather than over the library's own array, so that a caller can
    always find the returned row in ``roc_curve``. The sentinel the curve drops
    scores ``J = 0`` and is never the maximum unless nothing is.

    A FRAME AND NOT A ROW, because the card promises "several rows on ties" and a
    tie is not exotic: on four controls scoring 1, 2, 3, 4 against four cases
    scoring 3, 4, 5, 6 the maximum is attained three times over.
    """
    youden = curve["sensitivity"].to_numpy() + curve["specificity"].to_numpy() - 1.0
    best: pd.DataFrame = curve.loc[youden == youden.max()]
    return best.reset_index(drop=True)


def _the_interval(area: float, *, cases: np.ndarray, controls: np.ndarray,
                  level: float) -> dict[str, Any]:
    """DeLong's interval for the area, from the placement values of the two samples.

    THE VARIANCE IS DeLONG, DeLONG AND CLARKE-PEARSON (1988), COMPUTED BY THE
    MIDRANK IDENTITY OF SUN AND XU (2014), which is the form pROC's own ``ci.auc``
    documentation states it uses. With ``r`` the midranks of the pooled sample and
    ``r_A``, ``r_N`` the midranks within each sample,
    ``V10_i = (r_i - r_A_i) / n_N`` and ``V01_j = 1 - (r_j - r_N_j) / n_A`` are the
    placement values, and ``Var = S10 / n_A + S01 / n_N`` with ``S10``, ``S01``
    their sample variances. It is the same quantity as the mean of Hanley and
    McNeil's kernel over all ``n_A x n_N`` pairs and is ``O(n log n)`` rather than
    ``O(n_A n_N)``; the test module computes it the slow way from the kernel itself
    and asserts the two agree, so the fast form is checked against the definition
    rather than trusted.

    THERE IS NO DeLONG ANYWHERE IN scikit-learn:
    ``[n for n in dir(sklearn.metrics) if 'delong' in n.lower()]`` is ``[]`` on
    1.9.0. Every number in this function is this engine's own arithmetic.

    A VARIANCE OF ZERO IS REFUSED RATHER THAN REPORTED, and the open-interval rule
    is what says so. MEASURED, three ways to reach it: a constant score gives an
    area of 0.5 and a variance of exactly 0.0, a perfectly separated score gives
    1.0 and 0.0, and a perfectly inverted one gives 0.0 and 0.0. In each the
    reported interval would have no width at all -- ``(0.5, 0.5)``, ``(1.0, 1.0)``
    -- presented as though it were a 95 % interval, when what has happened is that
    the normal approximation has nothing to approximate. TWO OF THE THREE CANNOT BE
    SEEN FROM ANY ARGUMENT: a separated score is not constant, not tied, not missing
    and not degenerate by any question asked of the input, which is why the rule is
    asked of the variance this body COMPUTED.

    THE INTERVAL IS NOT CLIPPED TO [0, 1]. MEASURED on eight rows: an area of 0.875
    with a standard error of 0.125 reaches 1.1199954980675066. Clipping would report
    a bound the arithmetic did not produce and would hide the case where the normal
    approximation should be trusted least.
    """
    together = rankdata(np.concatenate([cases, controls]), method="average")
    v10 = (together[: cases.size] - rankdata(cases, method="average")) / controls.size
    v01 = 1.0 - (together[cases.size :] - rankdata(controls, method="average")) / cases.size
    variance = float(np.var(v10, ddof=1)) / cases.size + float(np.var(v01, ddof=1)) / controls.size
    require_strictly_inside(
        variance,
        low=0.0,
        high=math.inf,
        fn=_FN,
        arg="the DeLong variance of the AUC",
    )
    half = float(norm.ppf(1.0 - (1.0 - level) / 2.0)) * math.sqrt(variance)
    return {
        "low": area - half,
        "high": area + half,
        "conf_level": level,
        "method": _INTERVAL_METHOD,
    }


def run_roc(
    *,
    response: Any,
    predictor: Any,
    direction: Literal["auto", "<", ">"] | None = None,
    ci: bool | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``run_roc`` -- method card #84.

    ROC / AUC — binary forecast evaluation.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        response: [raw_handle, required] Handle to a binary target (logical, numeric 0/1 or
            categorical/string with 2 levels).
        predictor: [raw_handle, required] Handle to a numeric score/prediction (e.g. the
            fitted_probabilities of #83), of the same length as the response.
        direction: [enum, optional] Relation of controls to cases (default auto· '<' = normal
            prob-score).
        ci: [boolean, optional] Computation of the DeLong CI of the AUC (default True). Default
            ``True``.
        conf_level: [number, optional] Confidence level of the CI of the AUC, in (0,1) (default
            0.95). Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        Declared on the method card:

        - precondition-sample-size
        - precondition-missing
        - precondition-degenerate
        - precondition-domain

    Validation:
        Documented on the method card:

        - direction has no default in the contract and its own description claims one:
          node-specs.json gives the argument has_default false while the description reads 'default
          auto'. An omitted optional reaches a body as None and stays None, so an absent direction
          is REFUSED rather than filled in with 'auto' -- a default a client cannot read out of the
          contract is a behaviour nobody agreed to, and the two orientations return an area and one
          minus it, so there is no neutral answer. Correcting the description changes the node's
          contract_hash and is an owner decision, so the tension is recorded here rather than
          reconciled in code
        - the body also raises precondition-shape, which this field cannot name: a response or a
          predictor that is not a single vector, and a predictor whose row labels are not the
          response's, are refused under that code, and gates/registry.py PRIMITIVES registers no
          primitive for it, so the closed vocabulary of precondition_gates has no entry to declare
          it with
        - which observed label is the case is decided by ORDER -- the lower of the two levels is the
          control, the higher is the case -- which is the rule scikit-learn's own binariser applies,
          and it is REPORTED under controls_level and cases_level rather than left implicit. Two
          levels with no order between them, such as the integer 0 beside the string 'NA', are
          refused rather than ranked by the order the rows arrive in

    .. gen_wrappers: end of generated docstring

    Examples:
        Four controls scoring 1, 2, 3, 4 against four cases scoring 3, 4, 5, 6. The
        area is 14/16 by hand -- Hanley and McNeil's kernel gives 2.5 + 3.5 + 4 + 4
        over the sixteen pairs, the two half-credits being the ties at 3 and at 4::

            >>> import pandas as pd
            >>> truth = pd.Series([0, 0, 0, 0, 1, 1, 1, 1])
            >>> score = pd.Series([1.0, 2.0, 3.0, 4.0, 3.0, 4.0, 5.0, 6.0])
            >>> evaluation = run_roc(response=truth, predictor=score, direction="<")
            >>> evaluation["auc"]
            0.875
            >>> evaluation["n_cases"], evaluation["n_controls"]
            (4, 4)

        Which label was read as the case is never left implicit::

            >>> evaluation["controls_level"], evaluation["cases_level"]
            (0, 1)
            >>> evaluation["direction"], evaluation["percent"]
            ('<', False)

        The curve keeps every operating point, and the Youden maximum here is a
        three-way tie -- which is why ``best_threshold`` is a frame::

            >>> list(evaluation["roc_curve"]["threshold"])
            [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
            >>> list(evaluation["roc_curve"]["sensitivity"])
            [0.25, 0.5, 0.75, 1.0, 1.0, 1.0]
            >>> list(evaluation["best_threshold"]["threshold"])
            [5.0, 4.0, 3.0]

        The interval is DeLong's and it is not clipped: on eight rows the upper
        bound is above 1, which is the normal approximation saying so rather than a
        defect::

            >>> round(evaluation["auc_ci"]["low"], 6)
            0.630005
            >>> round(evaluation["auc_ci"]["high"], 6)
            1.119995
            >>> evaluation["auc_ci"]["method"]
            'delong'

        Negating the score inverts the orientation and nothing else. ``'auto'``
        follows it and says so; a strict ``'<'`` reports the inverted area instead
        of hiding it::

            >>> run_roc(response=truth, predictor=-score, direction="auto")["direction"]
            '>'
            >>> run_roc(response=truth, predictor=-score, direction="auto")["auc"]
            0.875
            >>> run_roc(response=truth, predictor=-score, direction="<")["auc"]
            0.125

        A score that orders nothing has an area of 0.5 and no interval at all, so
        the interval is refused rather than reported as a point::

            >>> flat = pd.Series([2.0] * 8)
            >>> run_roc(response=truth, predictor=flat, direction="<", ci=False)["auc"]
            0.5
            >>> run_roc(response=truth, predictor=flat, direction="<")
            Traceback (most recent call last):
            econflow_engine.errors.GateError: run_roc: "the DeLong variance of the AUC" = 0.0...

    Note:
        FUNCTIONS USED. scikit-learn 1.9.0 (BSD-3-Clause), two calls:
        ``metrics.roc_auc_score(indicator, score)`` for the area and
        ``metrics.roc_curve(indicator, score, pos_label=1.0,
        drop_intermediate=False)`` for the curve. ``numpy`` 2.5.2 builds the
        indicator and the placement variances, ``scipy`` 1.18.0 supplies
        ``stats.rankdata`` for the midranks and ``stats.norm.ppf`` for the quantile,
        and ``pandas`` 2.3.3 carries the curve and the levels. The area and the
        operating points are the library's; ``auc_ci``, ``best_threshold``,
        ``n_cases``, ``n_controls``, ``controls_level``, ``cases_level``,
        ``direction`` and ``percent`` are this engine's.

        WHERE THE NUMBERS COME FROM. The area is the Mann-Whitney statistic W of
        Hanley and McNeil (1982), doi:10.1148/radiology.143.1.7063747, section IV,
        p. 31, with a tie counted as half a win; their p. 32 states that it agrees
        exactly with the trapezoidal area, which is why one published figure checks
        both the statistic and the curve. The interval is the variance of DeLong,
        DeLong and Clarke-Pearson (1988), doi:10.2307/2531595, in the midrank form
        of Sun and Xu (2014), doi:10.1109/LSP.2014.2337313, with a normal quantile.
        The operating point is Youden (1950),
        doi:10.1002/1097-0142(1950)3:1<32::AID-CNCR2820030106>3.0.CO;2-3.

        THE ONE CLAIM THIS METHOD DOES NOT MAKE, AND IT IS ABOUT THE INTERVAL.
        Hanley and McNeil print a standard error of 0.032 for their own 109 images
        and it is NOT DeLong's: it is their own moment estimator, their Formula (1)
        on p. 32, evaluated at the Q1 = 0.8182 and Q2 = 0.8313 of their Table II.
        MEASURED on the committed fixtures, that formula with their own Q1 and Q2
        returns 0.03200416314832256 -- reproducing the printed 3.2 % -- while the
        DeLong standard error is 0.030724408379381122, 4.0 % away. The two
        estimators disagree about their own ingredients as well: computed from the
        placement values, Q1 is 0.8288830990184423 and Q2 is 0.81607538214745,
        because Table II's counting scheme handles the ties of a five-point scale
        differently from the placement-value moments. So quoting 0.032 as the DeLong
        standard error would be a false claim about which estimator produced it, and
        the oracle case claims the area and the two sample sizes and no interval.

        DELIBERATELY OMITTED. Partial AUC (``max_fpr``) and multiclass ROC
        (``multi_class``): card #84's ``when_not`` puts both outside this wrapper.
        The paired comparison of two curves and the bootstrap and smoothed
        intervals: its ``alternatives`` put those outside as well, and the card
        fixes the interval method to DeLong. ``sample_weight``: no argument of this
        node carries weights. The binormal smooth area, which the paper reports as
        0.911 for the same data: it is a different estimator under a distributional
        assumption this node does not make, and comparing the two would be comparing
        an empirical area with a fitted one.

        GATES ADDED, AND THE SOURCE OF EACH. THE FIRST IS A REFUSAL WHERE A DEFAULT
        WOULD BE EASIER. ``direction`` carries no default in the contract while its
        own description claims one, and inventing ``'auto'`` here would settle a
        contract question in a place no client can read; the two orientations return
        an area and one minus it, so there is no neutral answer to fall back on.
        THE REST ARE MEASURED SILENT ACCEPTANCES OR CRASHES, all against
        scikit-learn 1.9.0. A single-class response returns ``nan`` behind an
        ``UndefinedMetricWarning``, and a three-level one raises ``ValueError:
        multi_class must be in ('ovo', 'ovr')`` -- a message about an argument this
        node does not have. Two Series whose labels do not overlap at all are paired
        POSITIONALLY and return the same area with no warning, because pandas aligns
        on labels and this library does not. A missing label raises two different
        ``ValueError``s depending on the response's dtype, neither naming an
        argument, and one of them behind a ``RuntimeWarning`` that this suite's
        ``-W error`` turns into a crash first. A missing or infinite score raises
        ``ValueError: Input contains NaN`` and ``ValueError: Input contains
        infinity``, naming neither argument. A ``conf_level`` of exactly 1 makes
        ``norm.ppf`` return ``inf`` and one of exactly 0 makes it return 0.0, so one
        endpoint is an interval of infinite width and the other an interval of none.
        Two levels of different types crash on the comparison that decides which is
        the case.

        TWO GATES ASK ABOUT THIS BODY'S OWN OUTPUT, which is the half the sibling
        count-model body had to have added by review. THE FIRST IS THE DeLONG
        VARIANCE, and it catches an input no rule about an argument could see: a
        perfectly separated score is not constant, not tied and not degenerate by
        any question asked of the predictor, and its variance is exactly 0.0, so the
        interval would be ``(1.0, 1.0)`` -- no width, presented as 95 %. THE SECOND
        IS THE INTERVAL ITSELF, and the input that reaches it is narrow enough to
        be worth writing down: ``conf_level = 0.9999999999999999`` is strictly less
        than 1.0 as a double and passes the domain rule, but ``1 - (1 - it) / 2``
        evaluates to exactly ``1.0``, ``norm.ppf`` returns ``inf`` and both bounds
        are infinite. ``to_mcp`` renders an infinity as ``null`` and ``to_json``
        writes no ``Infinity`` token, so what a caller would receive is well-formed
        JSON whose interval is simply empty -- which is also how this payload reports
        ``auc_ci`` when ``ci`` is false. The two must not be indistinguishable.

        WHAT IS ARGUED RATHER THAN GATED, so that nobody adds a rule that cannot
        fire. Every value in ``roc_curve`` is finite by construction once the gates
        above have run: a sensitivity is a count over ``n_cases`` and a specificity
        a count over ``n_controls``, both positive because the response has exactly
        two levels; and every threshold is a value the predictor took, which the
        missing-value rule has already proven finite. The one non-finite row
        scikit-learn does produce, the ``inf`` sentinel, is dropped by name. For the
        same reason the two library calls are NOT wrapped in a translation of the
        estimator's own exceptions: after these gates the arguments they receive are
        a 0/1 indicator with both levels present and a finite 1-D score of the same
        length, which is the case ``_binary_clf_curve`` cannot refuse. A refusal
        from either would be a hole in a gate and belongs to the caller as the crash
        it is, not as a message about their data.

        NO ARGUMENT OF THIS NODE REACHES AN EVALUATOR, and that is checked rather
        than assumed, because the first 2.2 body shipped a remote code execution
        through an argument of kind ``string`` spliced into a formula. This node
        declares no argument of that kind at all. ``direction`` is an ``enum`` the
        wire model checks against the contract's own list before the body runs, and
        :func:`~econflow_engine.gates.estimation.require_a_declared_option` checks
        on a direct call; it is used as a comparison operand and is never
        interpolated into anything that is parsed.

        THAT GATE REPLACES A CLAIM THAT WAS FALSE IN THE SHIPPED PACKAGE, and the
        way it was false is worth keeping. This paragraph said beartype enforced
        the ``Literal`` on a direct call. It does -- but beartype is a DEV
        dependency installed by ``tests/conftest.py``, whose own comment says the
        hook must never move into the package, so the check existed under pytest
        and nowhere else. That is exactly the arrangement in which no test can see
        the hole, and MEASURED with the hook absent it was a real one:
        ``direction='X'`` returned an area of 0.0 where ``'<'`` returns 1.0, with
        ``'X'`` reported back under ``direction``. An orientation outside the
        declared enum and an inverted area, refused by nothing.
        ``ci`` is a boolean read by an ``if``, and ``conf_level`` is a number that
        reaches ``norm.ppf`` and arithmetic. ``response`` and ``predictor`` are
        ``raw_handle``, so their CONTENT is entirely caller-chosen, and that content
        is the only text this node carries onward: the two level labels are compared
        with ``==``, reported verbatim under ``controls_level`` and ``cases_level``,
        and interpolated into gate messages through ``repr``. None of those is a
        parser, a query or a path. ``tests/wrappers/c16_limited_dependent/
        test_roc_auc_binary.py`` feeds the payload that ran against the first body in
        as a response LABEL and asserts in a ``finally`` that no side effect
        occurred.
    """
    require_supplied(direction, fn=_FN, arg="direction", remedy=_ORIENTATION_REMEDY)
    require_a_declared_option(
        direction,
        allowed=(_ASCENDING, _DESCENDING, _AUTOMATIC),
        fn=_FN,
        arg="direction",
        remedy=_ORIENTATION_REMEDY,
    )
    wants_interval = bool(ci if ci is not None else _declared("ci"))
    level = float(conf_level if conf_level is not None else _declared("conf_level"))
    # ASKED EVEN WHERE NO INTERVAL IS WANTED, because an argument a branch would
    # silently ignore is a request the caller believes was honoured.
    require_strictly_inside(level, low=0.0, high=1.0, fn=_FN, arg="conf_level")

    observed = _the_labels(response)
    require_no_missing(predictor, fn=_FN, arg="predictor")
    scores = np.asarray(predictor, dtype=float)
    require_an_aligned_index(
        pd.Series(scores, index=_index_of(predictor, int(scores.size))),
        reference=_index_of(response, int(observed.size)),
        fn=_FN,
        arg="predictor",
        remedy=(
            "Pass the response and the score as two pandas objects sharing one "
            "index, or as two plain arrays of the same length. A labelled series "
            "beside an unlabelled array can only be paired by position, and this "
            "method will not do that without being told to."
        ),
    )
    controls_level, cases_level = _the_levels(observed)
    indicator = np.asarray(observed == cases_level, dtype=float)

    ascending = float(roc_auc_score(indicator, scores))
    resolved = (
        (_ASCENDING if ascending >= 0.5 else _DESCENDING)
        if direction == _AUTOMATIC
        else str(direction)
    )
    oriented = scores if resolved == _ASCENDING else -scores
    # NOT ``1 - ascending``. MEASURED on the published table: the library returns
    # 0.1068289384719405 for the negated score and one minus its own answer is
    # 0.10682893847194053 -- 0x1.b59242d00dd8ep-4 against 0x1.b59242d00dd90p-4, one
    # ulp apart. Two different doubles for one quantity, and the reported area is
    # the one the library computed for the orientation reported beside it.
    area = ascending if resolved == _ASCENDING else float(roc_auc_score(indicator, oriented))

    curve = _the_curve(indicator, oriented, resolved)
    reported = {"the area under the curve": area}
    interval = None
    if wants_interval:
        cases = oriented[indicator == 1.0]
        controls = oriented[indicator == 0.0]
        # BEFORE THE VARIANCE AND NOT AFTER IT. MEASURED: ``np.var(x, ddof=1)`` over
        # one observation raises ``RuntimeWarning: Degrees of freedom <= 0 for
        # slice``, which this suite's ``-W error`` makes a crash, and returns ``nan``
        # with warnings left as warnings.
        require_min_length(
            cases, minimum=2, fn=_FN, arg=f"the scores of the {cases_level!r} observations"
        )
        require_min_length(
            controls, minimum=2, fn=_FN, arg=f"the scores of the {controls_level!r} observations"
        )
        interval = _the_interval(area, cases=cases, controls=controls, level=level)
        reported["the lower bound of the interval"] = interval["low"]
        reported["the upper bound of the interval"] = interval["high"]
    require_finite_estimates(
        pd.Series(reported),
        fn=_FN,
        # NOT "area and interval this method reports": the gate writes "the
        # {quantity} this method reports", so that spelling reached the caller as
        # "the area and interval this method reports this method reports are not
        # numbers".
        quantity="area and interval",
        remedy=(
            "A confidence level below 1 can still round to 1 in double precision -- "
            "1 - (1 - 0.9999999999999999) / 2 is exactly 1.0 -- and the normal "
            "quantile there is infinite. Ask for a level a double can hold away from "
            "the endpoint, or pass ci=false to report the area alone."
        ),
    )
    return {
        "auc": area,
        "auc_ci": interval,
        "roc_curve": curve,
        "best_threshold": _the_best(curve),
        "n_cases": int(indicator.sum()),
        "n_controls": int(indicator.size - indicator.sum()),
        "controls_level": controls_level,
        "cases_level": cases_level,
        "direction": resolved,
        "percent": False,
    }
