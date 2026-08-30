# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``ordered_choice`` -- method card #523.

#523 Ordered logit and probit

Category 16-limited-dependent; module ``ordered_choice``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_ordered_choice",
    "ld_proportional_odds_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---

import math

import numpy as np
import statsmodels.api as sm
from scipy import stats
from statsmodels.miscmodels.ordinal_model import OrderedModel

from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_combination,
    refuse_estimator_failure,
    require_a_declared_option,
    require_an_aligned_index,
    require_convergence,
    require_distinct_column_names,
    require_finite_estimates,
    require_no_separation,
    require_strictly_inside,
)
from econflow_engine.gates.primitives import (
    require_full_rank,
    require_in_range,
    require_min_length,
    require_no_missing,
)

#: The two nodes this module carries, named once because every gate message opens with one.
_FIT_FN = "ld_ordered_choice"
_TEST_FN = "ld_proportional_odds_test"

#: The link whose coefficients are log odds ratios, and therefore the only one Brant's test is
#: defined for. Named rather than written into the comparison, so that it is visibly the same
#: string as the key :data:`_DISTRIBUTIONS` carries and the word the fit reports back.
_LOGIT = "logit"

#: What each declared link becomes on the way to ``OrderedModel(distr=...)``. TWO OF THE THREE ARE
#: THE LIBRARY'S OWN STRINGS AND THE THIRD IS OURS. ``distr='cloglog'`` is not a value statsmodels
#: 0.14.6 accepts: ``__init__`` maps only ``'probit'`` and ``'logit'`` and assigns anything else
#: straight to ``self.distr`` expecting a scipy distribution, so the contract's own third link
#: raises ``AttributeError: 'str' object has no attribute 'name'``. ``scipy.stats.gumbel_l`` IS the
#: complementary log-log link -- its CDF is ``1 - exp(-exp(x))``, and MEASURED the two agree to the
#: bit at 0.3, both 0.7407231340091724.
_DISTRIBUTIONS: dict[str, Any] = {
    "logit": "logit",
    "probit": "probit",
    "cloglog": stats.gumbel_l,
}

#: The optimiser and the tolerance it stops at, both pinned. THEY ARE PART OF THE ANSWER AND NOT A
#: DETAIL, because a published estimate is only reproducible to wherever the iteration stopped, and
#: the library's shipped defaults do not get there.
#:
#: WHAT THE DEFAULTS COST, MEASURED ON TWO PUBLISHED TABLES AT ONCE. Against the six figures
#: Stata's [R] ologit prints for its Example 1 -- one coefficient, four cut points and a
#: log-likelihood -- the worst relative disagreement is 1.4631e-05 for ``nm``, which is what
#: ``OrderedModel.fit`` takes when nothing is passed, 1.6109e-05 for ``bfgs`` and 2.1959e-06 for
#: ``lbfgs``. All three would clear ``estimate-1e-4``. The SECOND table is what decides it:
#: McCullagh (1980) prints his Delta-hat as ``0.603``, and ``lbfgs`` at its shipped tolerance
#: returns 0.6024545471073262, WHICH ROUNDS TO 0.602. The estimator had not finished --
#: ``llf = -1477.747438715890`` against -1477.747438240050 at the optimum -- and the third decimal
#: of a published figure was the first thing to go.
#:
#: WHY ``pgtol`` AND NOT SOMETHING ELSE, AND WHAT THE PIN IS NOT LOAD-BEARING FOR. At
#: ``pgtol=1e-10`` the same fit returns 0.6026415259338052, which rounds to the printed 0.603.
#: THE ORACLE CASE DOES NOT DEPEND ON THIS SETTING AT ALL, and saying so is what keeps the pin
#: from being credited with work it does not do: MEASURED to the bit, the coefficient, the four
#: cut points and the log-likelihood of the Stata fit are IDENTICAL at the library's default and
#: at this pin -- worst relative disagreement 2.1959e-06 either way. The pin buys McCullagh's
#: third decimal, and nothing else.
#:
#: TIGHTER STILL IS MORE ACCURATE AND IS NOT TAKEN, AND THE REASON IS NOT A WARNING. This
#: paragraph replaces a claim that there was one. ``pgtol=1e-12`` with ``factr=1.0`` reaches
#: 0.6026492397459533 and takes the Stata disagreement from 2.1959e-06 down to 1.1659e-07;
#: MEASURED on BOTH published tables, at all three settings, under
#: ``warnings.catch_warnings(record=True)`` with ``simplefilter("always")``, touching ``params``,
#: ``bse``, ``tvalues``, ``pvalues``, ``conf_int``, ``llf`` and ``summary()`` -- not one warning
#: is raised anywhere, and no ``HessianInversionWarning`` at any of them.
#:
#: WHAT REFUSES IT IS THAT THE EXTRA ACCURACY IS PRECISION THIS MODULE DECLINES TO CLAIM.
#: ``factr=1.0`` asks L-BFGS-B to stop only once the relative reduction in the objective reaches
#: machine epsilon, so which iterate is the last one is settled by the final bits of a
#: floating-point reduction -- and numpy's wheel builds OpenBLAS ``DYNAMIC_ARCH``, which chooses
#: the kernel producing those bits from the CPU at run time. This engine's determinism gate
#: compares two runs on ONE machine and cannot see a difference between two. That is an argument
#: rather than a measurement, and it is the same one the oracle case's own notes make in refusing
#: ``statistic-1e-6``: agreeing to 1e-07 would pin two optimisers' stopping points against each
#: other, and neither Stata's nor statsmodels' is a closed form anybody can appeal to. 1e-10 buys
#: the printed decimal and stops.
#:
#: ``newton`` IS THE MOST ACCURATE OF ALL OF THEM AND IS NOT TAKEN EITHER. It reaches 1.1636e-07 on
#: the Stata figures, and MEASURED it raises ``numpy.linalg.LinAlgError: Singular matrix`` on a
#: three-row sample, on a design carrying an all-zero column and on a covariate scaled to 1e9.
#: ``LinAlgError`` derives from ``ValueError``, so
#: :func:`~econflow_engine.gates.estimation.is_estimator_refusal` would read an optimiser artefact
#: as a statement about the caller's data.
_METHOD = "lbfgs"
_STOPPING_TOLERANCE = 1e-10

#: Iterations allowed before the optimiser gives up. Four times the library's own 500, so that
#: ``converged`` false means the problem and not the budget.
_MAXITER = 2000

#: How a threshold is named in the payload: the two levels it separates, in order. The library's
#: own ``'0/1'`` spelling names the same boundary but is also the label of the STORED parameter,
#: which is not the cut point (see :func:`_cut_points`), so the two are spelled differently on
#: purpose.
_BOUNDARY = "|"

#: What a caller must send in place of an outcome this method cannot read as ordered.
_ORDER_REMEDY = (
    "Send y as a pandas Categorical with ordered=True and its categories listed lowest first, or "
    "as a numeric column whose values already run in the outcome's own order. The level order IS "
    "the model here: every coefficient and every cut point is a statement about moving up that "
    "order, so it cannot be inferred from the data."
)


def _declared(fn: str, argument: str) -> Any:
    """The default ``node-specs.json`` publishes for one argument of one of these nodes.

    An omitted optional argument reaches a body as ``None`` -- ``adapt_args`` fills in a declared
    default only when the call comes through the wire, and a direct Python call does not. The value
    is READ FROM THE CONTRACT rather than written out here, so the two can never disagree.
    """
    return NODE_META[fn].defaults[argument]


def _options(fn: str, argument: str) -> tuple[str, ...]:
    """The values ``node-specs.json`` declares for one ``enum`` argument.

    READ FROM THE CONTRACT rather than written out here, so the set this body refuses against and
    the set ``mcp/make_tool.py`` validates a wire call against cannot disagree.
    """
    declared = next(arg for arg in NODE_META[fn].args if arg.name == argument)
    return declared.enum or ()


def _the_levels(y: pd.Series) -> tuple[Any, ...]:
    """The outcome's levels, lowest first, or a refusal saying why there is no such order.

    THE WORST SILENT WRONG THIS METHOD HAS, MEASURED against statsmodels 0.14.6.
    ``pd.Categorical(["low", "mid", "high"] * 22)`` carries no order, and the order it ends up
    with is LEXICOGRAPHIC -- ``['high', 'low', 'mid']``. ``OrderedModel`` builds on that order and
    fits, and what comes back is an estimate of a model in which `high` is the lowest category. The
    only complaint is a bare ``Warning``: "the endog has ordered == False, risk of capturing a
    wrong order for the categories". A plain column of the same words does not even get that far --
    ``ValueError: Pandas data cast to numpy dtype of object`` -- which is true and says nothing
    about ordering.

    A DECLARED LEVEL NOBODY OBSERVED IS REFUSED BESIDE IT, and it is the same question rather than
    a second one: the model estimates one cut point per boundary between DECLARED levels, and a
    boundary with nothing on one side of it has no likelihood. MEASURED, four declared categories
    over three observed ones raise ``ValueError: shapes (240,2) and (1,) not aligned: 2 (dim 1) !=
    1 (dim 0)`` from inside the likelihood, naming no level. It is also what makes every dichotomy
    of :func:`ld_proportional_odds_test` non-empty, so it is gated here rather than argued there.

    THE ORDER QUESTION IS ASKED BEFORE THE MISSING-VALUE ONE, AND THE MISSING-VALUE ONE IS PUT TO A
    MASK. A column of words is a legitimate outcome here once it declares an order, and
    :func:`~econflow_engine.gates.primitives.require_no_missing` reduces its argument to a NUMERIC
    vector, so asking it first would refuse an ordered Categorical of words for its dtype and say
    nothing about the order that was present. The mask is ``nan`` exactly where the outcome is
    missing and ``0.0`` everywhere else, so one rule answers for every dtype this method admits --
    including a Categorical, whose ``cat.codes`` writes a missing value as ``-1`` rather than as a
    ``nan`` and would therefore pass a numeric check unnoticed.
    """
    if isinstance(y.dtype, pd.CategoricalDtype):
        if not bool(y.cat.ordered):
            refuse_a_combination(
                fn=_FIT_FN,
                combination=(
                    f"reading \"y\" as an ordered outcome, whose categories are "
                    f"{[str(level) for level in y.cat.categories]}"
                ),
                reason=(
                    "the column is a Categorical that declares no order, and pandas sorts the "
                    "categories of such a column LEXICOGRAPHICALLY -- so 'high' comes before "
                    "'low' and the model would be fitted with the scale upside down. The "
                    "estimator accepts it with a warning and returns an estimate of a model "
                    "nobody specified."
                ),
                remedy=_ORDER_REMEDY,
            )
        require_no_missing(np.where(y.isna(), np.nan, 0.0), fn=_FIT_FN, arg="y")
        levels = tuple(y.cat.categories)
        observed = set(y.astype(object))
        missing = [str(level) for level in levels if level not in observed]
        if missing:
            refuse_a_combination(
                fn=_FIT_FN,
                combination='estimating a cut point at every boundary of "y"',
                reason=(
                    f"the outcome declares the level(s) {missing} and no observation carries "
                    f"any of them. A cut point is the boundary between two levels, and a "
                    f"boundary with nothing on one side of it is not identified by anything in "
                    f"this sample."
                ),
                remedy=(
                    "Drop the unused categories -- pandas spells that "
                    "y.cat.remove_unused_categories() -- or supply the observations that realise "
                    "them."
                ),
            )
        return levels
    if not pd.api.types.is_numeric_dtype(y):
        refuse_a_combination(
            fn=_FIT_FN,
            combination=f"reading \"y\" as an ordered outcome, whose dtype is {y.dtype}",
            reason=(
                "this method needs to know which level is higher than which, and a column of "
                "that dtype carries no such statement. The estimator refuses it too, with "
                "'Pandas data cast to numpy dtype of object', which names numpy rather than the "
                "order that is missing."
            ),
            remedy=_ORDER_REMEDY,
        )
    require_no_missing(np.where(y.isna(), np.nan, 0.0), fn=_FIT_FN, arg="y")
    return tuple(np.sort(pd.unique(y.to_numpy())).tolist())


def _the_design(y: pd.Series, x: pd.DataFrame) -> None:
    """Refuse a covariate table the estimator would accept and misreport.

    THE THREE ACCEPTANCES THIS BLOCKS, all measured against statsmodels 0.14.6. A design naming one
    column TWICE is fitted and returns the log-likelihood of the fit WITHOUT the copy --
    -85.90816143633305 either way on the published table -- while ``exog_names`` holds the name
    twice, so a payload keyed by name reports one of the two coefficients and silently drops the
    other. A design carrying a COLLINEAR pair under different names is fitted with no warning at
    all: on a three-level sample a column and its copy came back as -33.759 and +43.664, neither
    identified. A design with NO columns is fitted too, returning the thresholds alone.

    MISSING VALUES ARE ASKED COLUMN BY COLUMN because the numeric primitive answers about one
    vector, and AFTER the duplicate-name rule because ``x[name]`` on a frame carrying that name
    twice returns a frame rather than a column. The rank question comes last, because a rank is
    taken over floats and a column carrying a ``nan`` has no rank worth reporting.
    """
    require_an_aligned_index(
        x,
        reference=y.index,
        fn=_FIT_FN,
        arg="x",
        remedy="Give the covariates the outcome's own index, row for row.",
    )
    require_distinct_column_names(
        x,
        fn=_FIT_FN,
        arg="x",
        remedy="Give every covariate a name of its own.",
    )
    for name in x.columns:
        require_no_missing(x[name], fn=_FIT_FN, arg=f'x["{name}"]')
    require_full_rank(x, fn=_FIT_FN, arg="x")


def _the_existence_question(
    y: pd.Series, x: pd.DataFrame, levels: tuple[Any, ...]
) -> tuple[pd.DataFrame, pd.Series]:
    """This model written as ONE binary design, so that Konis's programme answers for it.

    WHAT IS BEING ASKED, AND WHY THE SIBLING NODE'S RULE CANNOT ANSWER IT. The ordered
    log-likelihood reaches its supremum only at infinity -- so no maximum-likelihood estimate
    exists -- exactly when some direction ``d_b`` in the covariates and some cut points ``d_t``
    satisfy, for every observation ``i`` in category ``j``::

        x_i'd_b - d_t[j - 1] >= 0     (j > 1)
        d_t[j] - x_i'd_b     >= 0     (j < J)

    with at least one inequality strict; the log-likelihood is then non-decreasing along the whole
    ray and, the likelihood being concave for every link this node offers, has no interior maximum.
    Each of those two lines IS one row of a binary design whose columns are the covariates and one
    per boundary: the row for boundary ``k`` is ``[x_i, -e_k]`` and its response is that boundary's
    own cumulative dichotomy ``1{y_i > k}``. That is the proportional-odds model stacked as a
    single binary regression with a boundary-specific intercept -- so the existence question for
    the ordered model is Silvapulle's condition on THAT design, and
    :func:`~econflow_engine.gates.estimation.require_no_separation` already solves it. The
    programme, its measured tolerances, its solver-failure posture and its witness check all stay
    in one place rather than being written a second time here.

    ONE ROW PER OBSERVATION PER ADJACENT BOUNDARY, AND NOT PER BOUNDARY. The constraints at
    non-adjacent boundaries are implied: satisfying the adjacent ones at every observation forces
    ``d_t`` to be non-decreasing -- every declared level is observed, which this module gates in
    :func:`_the_levels` -- and the rest follows by chaining. Keeping only the adjacent rows leaves
    the feasible set unchanged and the design at ``2n`` rows rather than ``n(J - 1)``.

    WHAT IT COSTS BESIDE THE FIT IT GUARDS, MEASURED where a level count large enough to matter is
    the whole worry: the design is ``2n x (p + J - 1)``, and at 400 rows over 100 levels the
    programme is (792, 100) and runs in 0.006 s against 1.462 s for the fit itself, at 800 rows
    over 200 levels (1592, 200) and 0.020 s against 7.277 s. Peak RSS does not move on either.
    ``require_min_length`` already ties ``J`` to the sample, so the estimator reaches its own limit
    first.

    WHY THIS IS NOT THE QUESTION :func:`ld_proportional_odds_test` ASKS, MEASURED on both committed
    tables with the per-dichotomy rule::

        Stata 1977 repair records (the oracle)     ['ok', 'ok', 'ok', 'SEPARATED']
        McCullagh 1980 tonsil table (the payload)  ['ok', 'ok']

    Stata's fourth cumulative dichotomy separates and its ordered fit is nevertheless published to
    seven significant digits, so asking the per-dichotomy rule of this node would refuse the oracle
    case's own dataset. The programme below scores 0.0 on both tables and 1.466667e+01 and
    1.100000e+01 on the two reproducers in this module's tests, which is the discrimination the
    sibling rule cannot make.
    """
    codes = np.asarray(
        pd.Categorical(y, categories=list(levels), ordered=True).codes, dtype=int
    )
    covariates = x.to_numpy(dtype=float)
    boundaries = len(levels) - 1
    rows: list[np.ndarray] = []
    above: list[float] = []
    for position, level in enumerate(codes):
        for boundary, exceeded in ((level - 1, 1.0), (level, 0.0)):
            if 0 <= boundary < boundaries:
                cut = np.zeros(boundaries)
                cut[boundary] = -1.0
                rows.append(np.concatenate((covariates[position], cut)))
                above.append(exceeded)
    names = [
        *(str(name) for name in x.columns),
        *(
            f"the cut point {lower}{_BOUNDARY}{upper}"
            for lower, upper in zip(levels[:-1], levels[1:], strict=True)
        ),
    ]
    stacked = pd.DataFrame(np.asarray(rows, dtype=float), columns=names)
    return stacked, pd.Series(above, index=stacked.index)


def _the_fit(y: pd.Series, x: pd.DataFrame, link: str) -> tuple[OrderedModel, Any]:
    """The model and its fit, with the estimator's own refusals translated.

    ONLY ``GateError`` BECOMES A CLEAN REFUSAL. ``mcp/make_tool.py`` turns one into a
    ``ToolResult(ok=False, ...)`` and lets every other exception escape as a crash, so the
    estimator's own objections have to be carried across. THE ONE THAT MATTERS IS ABOUT THE
    INTERCEPT: no intercept is identified in this model -- an intercept is a common shift of every
    cut point -- and statsmodels says so itself, ``ValueError: There should not be a constant in
    the model``. Under this suite's ``-W error`` a ``ConvergenceWarning`` arrives here as an
    exception raised from inside the fit and is read the same way; with warnings left as warnings
    the fit returns and :func:`~econflow_engine.gates.estimation.require_convergence` refuses it
    instead. MEASURED on the published table beside a covariate spanning 1e9, the caller's warning
    filter changes the message and not the verdict.
    """
    try:
        # THE CONSTRUCTOR IS INSIDE THE BLOCK AND NOT ABOVE IT: the constant check is in
        # ``OrderedModel.__init__``, so a design carrying one raises before ``fit`` is reached.
        # `disp=0` because the optimiser PRINTS its iteration log otherwise, and nothing in this
        # engine writes to stdout.
        model = OrderedModel(y, x, distr=_DISTRIBUTIONS[link])
        fit = model.fit(
            method=_METHOD, disp=0, maxiter=_MAXITER, pgtol=_STOPPING_TOLERANCE
        )
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error,
            fn=_FIT_FN,
            code="precondition-degenerate",
            remedy=(
                "This model identifies no intercept, so the covariates must carry none: no "
                "constant column, and no set of columns that adds up to one. They must also be "
                "on a scale the likelihood can be maximised over -- a covariate spanning many "
                "orders of magnitude stops the iteration before it reaches an estimate."
            ),
        )
    require_convergence(
        converged=bool(fit.mle_retvals["converged"]),
        fn=_FIT_FN,
        estimator="ordered-model maximum likelihood",
        remedy=(
            "Rescale a covariate that spans many orders of magnitude, or drop one the sample "
            "cannot separate from the others."
        ),
    )
    return model, fit


def _cut_points(model: OrderedModel, fit: Any) -> np.ndarray:
    """The estimated cut points, which are NOT the parameters the library stores.

    ``OrderedModel.transform_threshold_params`` is
    ``concatenate((th[:1], exp(th[1:]))).cumsum()``: the first stored parameter IS the first cut
    point, and every later one is the LOG of the increment to the next. MEASURED on Stata's 66
    cars, where five categories mean four cut points, the stored vector is
    (-2.7655669, 0.5705317, 0.6621604, 0.7796616) against cut points
    (-2.7655669, -0.9963594, 0.9426174, 3.1233515) -- the second entry differs by 1.567 and by its
    SIGN. The stored vector is monotone increasing, so reporting it as the cut points would be
    silently wrong and would still pass any ordering check a reader might apply.

    The returned array is the interior cut points alone: the transform brackets them with
    ``-inf`` and ``+inf``, which are the two boundaries the model does not estimate.
    """
    transformed = model.transform_threshold_params(fit.params[model.k_vars :])
    return np.asarray(transformed, dtype=float)[1:-1]


def _density(model: OrderedModel) -> Any:
    """The link's DENSITY, out of an attribute the library annotates as a string.

    ``OrderedModel.__init__`` takes ``distr='logit'`` and REPLACES it with
    ``scipy.stats.logistic``, so the attribute's declared type describes the argument that was
    passed rather than what is stored. MEASURED: ``model.distr is scipy.stats.logistic`` is True
    for ``distr='logit'`` and ``model.distr is scipy.stats.norm`` for ``'probit'``. A type checker
    reading the annotation therefore refuses ``model.distr.pdf``, and this is the one place that
    disagreement is written down.
    """
    return model.distr


def _covariate_names(model: OrderedModel) -> list[str]:
    """The covariates' names alone, out of a list that also holds the thresholds'.

    ``exog_names`` is ``['foreign', '1/2', '2/3', '3/4', '4/5']`` for a five-level fit on one
    covariate: the estimator appends one name per boundary, because they are parameters of the
    same vector. ``k_vars`` is where the covariates stop.

    ``or ()`` RATHER THAN AN ASSERTION, because a model with no names is a model with no
    covariates and that is already a refusal:
    :func:`~econflow_engine.gates.primitives.require_full_rank` answers a design of no columns
    with "has no columns" before any fit is attempted. The attribute is typed optional by the
    library, so the empty case has to be spelled somewhere; spelling it as a name list of length
    zero is what the rest of this module already handles.
    """
    named = list(model.exog_names or ())
    return [str(name) for name in named[: model.k_vars]]


def _marginal_effects(
    model: OrderedModel, fit: Any, cut_points: np.ndarray, levels: tuple[Any, ...]
) -> dict[str, dict[str, float]]:
    """The average effect of each covariate on the SHARE in each category.

    ``OrderedResults`` HAS NO ``get_margeff`` on statsmodels 0.14.6 -- ``hasattr`` is False -- and
    neither does its ``predict`` offer a linear predictor to build one from: ``linear=True`` is not
    a keyword it takes and ``which='linear'`` raises ``ValueError: `which` is not available``. So
    every number here is this engine's, from the derivative of the observation probability::

        dP(y = j | x) / dx_k = [ f(mu_j - x'b) - f(mu_{j+1} - x'b) ] b_k

    with ``f`` the density of the link's distribution and ``f(+-inf) = 0``. The average is over the
    sample rather than at its mean. The module's own tests check it against a central finite
    difference of the fitted probabilities on all three links.

    THE BRACKET IS EVALUATED WHERE THE ARGUMENT IS FINITE AND SET TO ZERO WHERE IT IS NOT, rather
    than handed ``+-inf`` and cleaned afterwards: this repository's suite runs under
    ``np.seterr(all='raise')``, and a density evaluated at an infinity is exactly the kind of
    intermediate that raises there.
    """
    beta = np.asarray(fit.params[: model.k_vars], dtype=float)
    linear = np.asarray(model.exog, dtype=float) @ beta
    edges = np.concatenate(([-np.inf], cut_points, [np.inf]))[:, None] - linear[None, :]
    finite = np.isfinite(edges)
    density = np.where(finite, _density(model).pdf(np.where(finite, edges, 0.0)), 0.0)
    bracket = (density[:-1] - density[1:]).mean(axis=1)
    return {
        str(name): {
            str(level): float(bracket[position] * slope)
            for position, level in enumerate(levels)
        }
        for name, slope in zip(_covariate_names(model), beta, strict=True)
    }


def _coefficient_table(model: OrderedModel, fit: Any, level: float) -> pd.DataFrame:
    """One row per covariate, and NO ROW FOR A THRESHOLD.

    ``bse`` reports the standard errors of the parameters the library STORES, and the last
    ``J - 2`` of those belong to log increments rather than to cut points. MEASURED against the
    standard errors Stata's [R] ologit prints for the same fit: the coefficient agrees at
    9.2315e-08 and the FIRST cut point at 6.1775e-08 -- both are stored as themselves -- while the
    other three are 4.3718e-02, 4.5772e-01 and 6.0102e-01 away. A row pairing a transformed cut
    point with an untransformed parameter's uncertainty would be wrong in a way nothing downstream
    could see, so the thresholds are reported as estimates and carry no inference at all.
    """
    width = model.k_vars
    interval = np.asarray(fit.conf_int(alpha=1.0 - level), dtype=float)[:width]
    return pd.DataFrame(
        {
            "term": _covariate_names(model),
            "estimate": np.asarray(fit.params[:width], dtype=float),
            "std_error": np.asarray(fit.bse[:width], dtype=float),
            "z_value": np.asarray(fit.tvalues[:width], dtype=float),
            "p_value": np.asarray(fit.pvalues[:width], dtype=float),
            "conf_low": interval[:, 0],
            "conf_high": interval[:, 1],
        }
    )


def _the_reported_outcome(y: pd.Series, levels: tuple[Any, ...]) -> pd.Series:
    """The outcome as an ORDERED CATEGORICAL, whatever dtype it arrived as.

    WHY THE PAYLOAD CARRIES THE SAMPLE AT ALL, WHICH IS THE ONE DESIGN DECISION IN THIS MODULE
    A READER WILL WANT ARGUED. ``ld_proportional_odds_test`` re-fits ``J - 1`` binary logistic
    regressions on the rows this model was estimated over, and its only argument is a
    ``raw_handle`` -- the registry hands it back whatever this node returned, and nothing else.
    The obvious answer, returning the fitted object, is CLOSED: ``registry_put`` stores the whole
    return and :func:`~econflow_engine.serialize.to_mcp` renders a foreign object as an explicit
    serialisation stub, which ``tests/controls/double_run.py`` refuses outright -- "the digest is
    taken over a class name and this gate has not run the body". Its own docstring names the seam
    that would change that, says it belongs in a change of its own, and states the consequence
    plainly: until it lands, a body whose result is not serialisable cannot satisfy the gate. So
    what travels is DATA, which is also what the two sibling bodies in this category do.

    AN ORDERED CATEGORICAL RATHER THAN A COLUMN OF CODES, because it carries three things a
    column of codes does not: the level LABELS, their ORDER, and the fact that the order was
    declared rather than inferred. The consumer needs all three -- the labels to name a boundary
    in a refusal, the order to build ``1{y > j}``, and the declaration to know it is reading this
    node's own output rather than a frame somebody else registered.

    ALL THREE NOW TRAVEL, AND FOR A WHILE ONLY TWO OF THEM DID IN PROCESS AND ONE ON THE WIRE.
    ``to_mcp`` dispatches on the argument's CLASS, so the ``pd.Categorical`` handler never sees a
    categorical COLUMN: this Series went through the ``pd.Series`` handler, whose ``tolist()``
    flattened it to its labels alone. MEASURED, what reached a caller was ``{'values': [...],
    'name': 'tonsil_size'}`` -- the paragraph above, true of the object, false of the payload. The
    Series handler now reports ``levels`` and ``ordered`` for a categorical column, which is where
    the fix belongs: the index is why this is a Series and not a bare Categorical.
    """
    return pd.Series(
        pd.Categorical(y, categories=list(levels), ordered=True),
        index=y.index,
        name=y.name,
    )


def _the_stored_sample(fit: Any) -> tuple[str, pd.Series, pd.DataFrame]:
    """The link, the outcome and the design behind a handle, or a refusal saying what was wanted.

    ``fit`` is a ``raw_handle``: the registry hands back whatever the producing node returned,
    untouched, and nothing in the wire contract says which node that was. Reading a key that is not
    there would reach the caller as a ``KeyError`` traceback rather than as a refusal naming the
    node they should have run, so every field this node needs is checked for its SHAPE and not
    merely for its presence.
    """
    stored = fit if isinstance(fit, dict) else {}
    link = stored.get("link")
    outcome = stored.get("outcome")
    design = stored.get("design")
    if (
        link not in _DISTRIBUTIONS
        or not isinstance(outcome, pd.Series)
        or not isinstance(outcome.dtype, pd.CategoricalDtype)
        or not bool(outcome.cat.ordered)
        or not isinstance(design, pd.DataFrame)
        or not outcome.index.equals(design.index)
    ):
        refuse_a_combination(
            fn=_TEST_FN,
            combination=(
                f"testing proportional odds on a handle holding a {type(fit).__name__}"
            ),
            reason=(
                "this node re-fits the binary logistic regressions the test compares, so it "
                "needs the ordered outcome and the covariates the model was estimated on, "
                "indexed alike, and the link they were estimated under. The handle it was given "
                "does not carry them."
            ),
            remedy=(
                "Pass the handle ld_ordered_choice registered, which is the whole result of that "
                "node and not one field of it."
            ),
        )
    return str(link), outcome, design


def _brant_blocks(
    design: np.ndarray, indicators: list[np.ndarray], names: list[str], outcome: str,
    levels: tuple[Any, ...],
) -> tuple[np.ndarray, np.ndarray]:
    """The stacked binary slopes and their JOINT covariance, Brant (1990) section 3.

    THE OFF-DIAGONAL BLOCKS ARE THE POINT OF THE PAPER. The ``J - 1`` binary logits are fitted on
    the same rows and are therefore correlated, and for ``j <= l`` the joint event ``y > j`` and
    ``y > l`` is just ``y > l``, so::

        Cov(b_j, b_l) = (X' W_jj X)^-1 (X' W_jl X) (X' W_ll X)^-1
        W_jl = diag( pi_max(j,l) - pi_j pi_l ),    pi_j = P-hat(y > j)

    MEASURED, and it is worth writing down because the mistake is invisible: using ``min(j, l)``
    there instead of ``max(j, l)`` returns a NEGATIVE chi-squared -- -0.13397014178700709 on
    McCullagh's table -- and a p-value of exactly 1.0. A Wald statistic cannot be negative, which
    is why one is refused rather than reported.

    THE INTERCEPT ROWS AND COLUMNS ARE DROPPED AFTER INVERSION rather than before: the intercepts
    differ between cut points by construction -- they are the cut points -- and it is only the
    SLOPES the restriction is about, but each block has to be formed from the full design before
    the intercept can be taken out of it.

    NOTHING OF THIS ENGINE'S OWN IS INSIDE THE ``try``, AND THAT IS THE WHOLE ARRANGEMENT OF THIS
    FUNCTION. ``GateError`` is a ``ValueError`` (``errors.py``) and
    :func:`~econflow_engine.gates.estimation.is_estimator_refusal` admits any ``ValueError``, so a
    refusal raised inside the block below would be caught and re-reported as the ESTIMATOR
    objecting to the caller's data -- MEASURED on the sibling node's oracle dataset: two stacked
    ``ld_proportional_odds_test:`` prefixes, the class name ``GateError`` quoted at the caller and
    the authored per-dichotomy remedy buried inside a sentence about a fit that could not be
    estimated. ``np.linalg.inv`` is out of it for the mirror-image reason: it is this engine's
    arithmetic, and inside the block a singular cross-product came back as "It reported
    LinAlgError: Singular matrix". The gate's own docstring and the sibling body at
    ``binomial_glm_recession.py`` both spell out the same discipline.
    """
    width = len(names)
    frame = pd.DataFrame(design, columns=["(intercept)", *names])
    require_full_rank(frame, fn=_TEST_FN, arg="the design these regressions carry an intercept on")
    for cut, indicator in enumerate(indicators):
        require_no_separation(
            frame,
            response=pd.Series(indicator, index=frame.index),
            fn=_TEST_FN,
            remedy=(
                f"The dichotomy this test could not fit is 1{{{outcome} > "
                f"{levels[cut]}}}, the {cut + 1} of {len(indicators)} binary logistic "
                f"regressions Brant's test compares. Every level of the outcome has to be "
                f"reachable from both sides of every boundary: a category no observation of "
                f"one group ever takes is what puts this method out of reach for these data, "
                f"and the ordered model's own estimate is unaffected by it."
            ),
        )
    slopes: list[np.ndarray] = []
    probabilities: list[np.ndarray] = []
    try:
        for indicator in indicators:
            binary = sm.Logit(indicator, design).fit(disp=0)
            slopes.append(np.asarray(binary.params, dtype=float))
            probabilities.append(np.asarray(binary.predict(), dtype=float))
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error,
            fn=_TEST_FN,
            code="precondition-degenerate",
            remedy=(
                "Brant's test re-fits one binary logistic regression per boundary of the "
                "outcome, on the same covariates plus an intercept, and one of them could not be "
                "estimated."
            ),
        )
    inverses = [
        np.linalg.inv(design.T @ (design * (probability * (1.0 - probability))[:, None]))
        for probability in probabilities
    ]
    cuts = len(indicators)
    joint = np.zeros((cuts * (width + 1), cuts * (width + 1)))
    for first in range(cuts):
        for second in range(cuts):
            shared = (
                probabilities[max(first, second)]
                - probabilities[first] * probabilities[second]
            )
            joint[
                first * (width + 1) : (first + 1) * (width + 1),
                second * (width + 1) : (second + 1) * (width + 1),
            ] = inverses[first] @ (design.T @ (design * shared[:, None])) @ inverses[second]
    keep = [cut * (width + 1) + column for cut in range(cuts) for column in range(1, width + 1)]
    return np.concatenate(slopes)[keep], joint[np.ix_(keep, keep)]


def _wald(contrast: np.ndarray, slopes: np.ndarray, covariance: np.ndarray) -> float:
    """``(D b)' [D V D']^-1 (D b)``, the statistic Brant's section 3 writes down.

    A CONTRAST COVARIANCE THAT CANNOT BE INVERTED IS ANSWERED WITH A ``nan``, NOT WITH A CRASH.
    ``np.linalg.solve`` raises ``LinAlgError`` on a singular system; this call sits outside every
    ``try`` in this module, deliberately, because the arithmetic is this engine's own -- and
    :func:`~econflow_engine.gates.estimation.require_finite_estimates` runs AFTER it. So the raw
    exception left through the gateway as a crash, and the remedy that gate already carries -- "it
    has no value where their joint covariance cannot be inverted" -- described a path nothing could
    reach. The statistic genuinely has no value there, which is what a ``nan`` says and what the
    gate two lines later refuses.
    """
    difference = contrast @ slopes
    try:
        solved = np.linalg.solve(contrast @ covariance @ contrast.T, difference)
    except np.linalg.LinAlgError:
        return math.nan
    return float(difference @ solved)


def ld_ordered_choice(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    link: Literal["logit", "probit", "cloglog"] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_ordered_choice`` -- method card #523.

    Ordered logit and probit.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Ordered categorical outcome.
        x: [df_handle, required] Covariate table.
        link: [enum, optional] Link function. Default ``'logit'``.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        Declared on the method card:

        - precondition-domain
        - precondition-missing
        - precondition-rank
        - precondition-sample-size
        - precondition-degenerate

    Validation:
        Documented on the method card:

        - thresholds reports the CUT POINTS and not the parameters statsmodels stores: the last J-2
          stored parameters are the LOGARITHMS of the increments between adjacent cut points, and
          the stored vector is monotone increasing, so reporting it would be silently wrong and
          would pass any ordering check a reader applied
        - coeftable carries the covariates and no threshold row, because bse reports the standard
          errors of the stored parameterisation; measured against the standard errors Stata's [R]
          ologit prints for the same fit, the coefficient and the first cut point agree to 1e-7
          while the other three cut points are 4.4e-02, 4.6e-01 and 6.0e-01 away
        - the body also raises precondition-shape, which this field cannot name: a covariate table
          whose row labels are not the outcome's, one naming a column twice, and one with no columns
          at all are refused under that code, and gates/registry.py PRIMITIVES registers no
          primitive for it, so the closed vocabulary of precondition_gates has no entry to declare
          it with
        - link='cloglog' has no implementation in statsmodels 0.14.6 and is supplied here as
          scipy.stats.gumbel_l, whose CDF is the complementary log-log transform exactly; the
          library raises AttributeError on the string rather than refusing it
        - ld_proportional_odds_test is defined for the PROPORTIONAL-ODDS model alone: Brant (1990)
          compares the slopes of J-1 binary LOGISTIC regressions, so a fit made under the probit or
          the complementary log-log link is refused rather than tested under a restriction it was
          never estimated under
        - there is no oracle case for ld_proportional_odds_test and none can be written from the
          literature found: Brant (1990) prints an omnibus statistic of 11.2 on 6 degrees of freedom
          for 83 donated livers and never prints the 83 x 7 design behind it, and McCullagh (1980)
          prints his data and no Brant statistic. The arithmetic is checked instead against the
          scalar identity the three-category case reduces to, and against two contingency tables
          built to satisfy and to violate the restriction

    .. gen_wrappers: end of generated docstring

    Examples:
        The 66 cars whose 1977 repair record Stata's [R] ologit tabulates, by origin of
        manufacture. Five ordered records, one binary covariate, and the page prints
        the fit to seven significant digits::

            >>> import pandas as pd
            >>> counts = {1: (2, 1), 2: (10, 1), 3: (20, 7), 4: (13, 7), 5: (0, 5)}
            >>> record, origin = [], []
            >>> for level, (domestic, imported) in counts.items():
            ...     record += [level] * (domestic + imported)
            ...     origin += [0.0] * domestic + [1.0] * imported
            >>> rep77 = pd.Series(record, name="rep77")
            >>> cars = pd.DataFrame({"foreign": origin})
            >>> fit = ld_ordered_choice(y=rep77, x=cars)
            >>> round(fit["params"]["foreign"], 6)
            1.455878
            >>> fit["nobs"], round(fit["llf"], 6)
            (66, -85.908161)

        The cut points are the transformed ones, and the difference is not
        cosmetic: what the library stores for the second boundary is +0.570543,
        while the boundary itself is at -0.996359::

            >>> [round(cut, 6) for cut in fit["thresholds"].values()]
            [-2.765567, -0.996359, 0.942617, 3.123352]
            >>> list(fit["thresholds"])
            ['1|2', '2|3', '3|4', '4|5']

        The coefficient is positive and three of the five marginal effects are
        negative, which is the direction a coefficient's sign does not tell you::

            >>> effects = fit["marginal_effects"]["foreign"]
            >>> [round(effects[str(level)], 6) for level in (1, 2, 3, 4, 5)]
            [-0.061901, -0.167404, -0.079478, 0.206836, 0.101948]
            >>> round(sum(effects.values()), 12)
            0.0

        An outcome whose order was never declared is refused rather than sorted
        into one::

            >>> words = pd.Series(pd.Categorical(["low", "mid", "high"] * 22))
            >>> list(words.cat.categories)
            ['high', 'low', 'mid']
            >>> ld_ordered_choice(y=words, x=pd.DataFrame({"g": [0.0, 1.0] * 33}))
            Traceback (most recent call last):
            econflow_engine.errors.GateError: ld_ordered_choice: reading "y" as an ordered...

    Note:
        FUNCTIONS USED. statsmodels 0.14.6 (BSD-3-Clause), one estimator:
        ``miscmodels.ordinal_model.OrderedModel(y, x, distr=...)`` fitted with
        ``method='lbfgs'``, from which ``params``, ``bse``, ``tvalues``,
        ``pvalues``, ``conf_int``, ``llf``, ``nobs`` and
        ``transform_threshold_params`` are read. ``scipy`` 1.18.0 supplies
        ``stats.gumbel_l`` for the complementary log-log link and the three
        distributions' densities; ``numpy`` 2.5.2 and ``pandas`` 2.3.3 carry the
        arithmetic and the table. The likelihood and the fit are the library's;
        ``thresholds``, ``marginal_effects`` and the cloglog link are this
        engine's.

        WHERE THE NUMBERS COME FROM. The model is McCullagh (1980),
        doi:10.1111/j.2517-6161.1980.tb01109.x, equation (2.3):
        ``log[gamma_j / (1 - gamma_j)] = theta_j - beta' x`` with ``gamma_j`` the
        cumulative probability, which is the sign convention statsmodels uses. The
        latent formulation and the estimator are McKelvey and Zavoina (1975),
        doi:10.1080/0022250X.1975.9989847, which card #523 cites and which could
        not be read: no open-access record via Unpaywall or OpenAlex, so its
        equation numbers are not quoted and its own application is not used. The
        marginal effect is the derivative of the observation probability, written
        out in :func:`_marginal_effects`.

        THE ORACLE IS NOT THIS METHOD'S OWN PAPER, AND THE REASON IS ARITHMETIC.
        McCullagh's Table 1 prints the whole 2 x 3 tonsil-size table of 1398
        children and pp. 112-113 print the fit -- ``Delta-hat = 0.603``,
        ``theta-hat_1 = -0.810``, ``theta-hat_2 = 1.061``, ``G^2 = 0.302`` -- to
        THREE DECIMALS. MEASURED here, this body returns 0.6026415259338052,
        -0.809828952110833, 1.0613983374271192 and a deviance of
        0.3021876724632646, which round to every printed figure and sit 5.9448e-04,
        2.1117e-04, 3.7544e-04 and 6.2143e-04 away from them. Half a unit in the
        third decimal of 0.603 is 8.3e-04 of it, so no fit however converged can
        agree to the 1e-04 that ``estimate-1e-4`` allows, and ``pvalue-1e-3`` is
        documented for a p-value and would describe neither the number nor the
        reason. The paper's four figures are therefore asserted at the precision
        the page carries, by ``round``, in this module's tests, and the oracle case
        is Stata's [R] ologit Example 1, whose data is a printed cross-tabulation
        and whose fit is printed to seven significant digits.

        NO STANDARD ERROR IS CLAIMED ANYWHERE. McCullagh prints ``0.225`` beside
        his Delta-hat and this fit gives 0.22741574250766616 -- 1.0737e-02 apart,
        an order of magnitude beyond three printed decimals. His own p. 112 quotes
        the same 0.225 for the generalized-empirical-logit estimator immediately
        above, whose variance is his equation (2.6), an expected-information
        formula; statsmodels reports the observed-information one. Two estimators
        of one quantity, and neither is evidence about the other.

        DELIBERATELY OMITTED. McKelvey and Zavoina's pseudo-R-squared: ``prsquared``
        on this results object is McFadden's, and reporting one under a card citing
        the other would be a false attribution. The standard errors of the marginal
        effects: they need a delta method over the coefficients and the cut points
        together, no ``output_key_fields`` entry asks for them, and no published
        value was found to check them against. ``pred_table`` and ``resid_prob``,
        which exist and are cheap and which the card does not promise.
        ``missing='drop'``: MEASURED, it takes 240 rows to 239 and says nothing,
        which is the silent NA handling this project refuses.

        GATES ADDED, AND THE SOURCE OF EACH. THREE ARE SILENT ACCEPTANCES.
        An unordered ``Categorical`` is sorted LEXICOGRAPHICALLY --
        ``['high', 'low', 'mid']`` -- behind a bare ``Warning``, and the level order
        IS the model. A covariate table naming one column twice is fitted and
        returns the log-likelihood of the fit without the copy. A collinear pair
        under different names is fitted with no warning at all. THREE ARE CRASHES
        WHOSE MESSAGES NAME NOTHING A CALLER CAN ACT ON: a missing outcome, a
        missing or infinite covariate (``exog contains inf or nans``), and a
        declared level nobody observed (``shapes (240,2) and (1,) not aligned``).
        ONE IS SILENT GARBAGE: three rows, one covariate and three categories
        return a coefficient of 40.435 with ``converged`` true and not one warning,
        which is why the sample-size floor is tied to what is being estimated --
        one parameter per covariate, one per cut point, and one observation more.
        ONE IS AN ARGUMENT NOTHING VALIDATES: ``conf_int`` accepts an alpha of 0
        and returns an infinite interval, an alpha of 1 and returns a point, and an
        alpha of 2 and returns an interval whose lower bound is above its upper
        one.

        TWO ASK ABOUT THIS BODY'S OWN OUTPUT rather than about an argument.
        :func:`~econflow_engine.gates.estimation.require_convergence` reads
        ``mle_retvals``, because an iteration that runs out of budget still returns
        whatever the last step held. :func:`~econflow_engine.gates.estimation.
        require_finite_estimates` covers every number this payload carries, and the
        input that reaches it is narrow enough to be worth writing down:
        ``conf_level = 0.9999999999999999`` is strictly less than 1.0 as a double
        and passes the domain rule, but ``1 - (1 - it) / 2`` evaluates to exactly
        ``1.0``, the normal quantile is infinite and ``conf_int`` returns
        ``[-inf, inf]``. ``to_mcp`` renders an infinity as ``null`` and ``to_json``
        writes no ``Infinity`` token, so what a caller would receive is well-formed
        JSON whose interval is simply empty. Reporting it is not a weaker refusal;
        it is the silent-null defect.

        ONE ASKS WHETHER THE ESTIMATE EXISTS AT ALL, and neither of the two above
        can. MEASURED on 66 rows, three ordered levels and one covariate that
        orders them, before it: ``params`` 40.43612810638999, thresholds 21.357
        and 62.490, ``llf`` -3.5997591548270875e-07 -- the likelihood is 1 and
        every observation is predicted exactly -- with a standard error of
        6794.844753480861, a p-value of 0.9952518161849278, ``converged`` True and
        not one warning under ``-W error``. Growing the sample does not rescue the
        finiteness rule either: the same three blocks at 300 and 900 rows return
        3150.8642906652785 and 1820.6365189014734, both finite. The rule is
        :func:`~econflow_engine.gates.estimation.require_no_separation` asked of
        the design :func:`_the_existence_question` builds, which is this model
        stacked as one binary regression with a boundary-specific intercept, and
        it is asked OUTSIDE :func:`_the_fit`'s ``try`` because it is this engine's
        arithmetic rather than the estimator's.

        WHAT IS ARGUED RATHER THAN GATED, so that nobody adds a rule that cannot
        fire. The cut-point transform is ``exp`` of a cumulative sum, and MEASURED
        it overflows to ``inf`` once a stored increment reaches about 710 -- but no
        input probed for this module drove one past 3.5, so the finiteness rule
        above is what stands behind it rather than a bound on the parameter. The
        marginal effects are finite by construction once the estimates are: a
        density is bounded and the two infinite edges are set to zero before the
        subtraction rather than after it, which is what keeps the arithmetic inside
        ``np.seterr(all='raise')``. And every dichotomy
        :func:`ld_proportional_odds_test` builds is non-constant BECAUSE of the
        rule about unrealised levels here: with every declared level observed, the
        lowest and the highest both occur, so ``1{y > j}`` takes both values at
        every boundary.

        NO ARGUMENT OF THIS NODE REACHES AN EVALUATOR, and that is checked rather
        than assumed, because the first 2.2 body shipped a remote code execution
        through an argument of kind ``string`` spliced into a formula. Neither node
        declares an argument of that kind. ``link`` is an ``enum`` the wire model
        checks against the contract's own list before the body runs, and
        :func:`~econflow_engine.gates.estimation.require_a_declared_option` checks
        it on a direct call -- beartype enforces the ``Literal`` under pytest and
        beartype is a DEV dependency the shipped package does not install, which is
        exactly the arrangement in which no test can see the hole. ``conf_level``
        and ``alpha`` are numbers that reach arithmetic. ``y`` and ``x`` are data
        handles, so their CONTENT is caller-chosen, and that content is the only
        text carried onward: column names become keys of ``params``,
        ``marginal_effects`` and ``coeftable``, and level labels become keys of
        ``thresholds``. Both are compared, formatted and reported; neither reaches a
        parser, a query or a path. The module's tests feed the payload that ran
        against the first 2.2 body in as a COLUMN NAME and assert in a ``finally``
        that no side effect occurred.
    """
    selected = link if link is not None else _declared(_FIT_FN, "link")
    require_a_declared_option(
        selected,
        allowed=_options(_FIT_FN, "link"),
        fn=_FIT_FN,
        arg="link",
        remedy=(
            "Send link='logit' for the proportional-odds model, 'probit' for the ordered probit, "
            "or 'cloglog' for the complementary log-log. The three fit different likelihoods and "
            "return different coefficients, so there is no nearest match to resolve to."
        ),
    )
    chosen = str(selected)
    level = float(conf_level if conf_level is not None else _declared(_FIT_FN, "conf_level"))
    require_strictly_inside(level, low=0.0, high=1.0, fn=_FIT_FN, arg="conf_level")

    levels = _the_levels(y)
    require_in_range(
        float(len(levels)),
        low=2.0,
        high=math.inf,
        fn=_FIT_FN,
        arg="the number of ordered levels in y",
    )
    _the_design(y, x)
    require_min_length(
        y,
        minimum=x.shape[1] + len(levels),
        fn=_FIT_FN,
        arg="y",
    )
    # OUTSIDE EVERY ``try``, BECAUSE THE PROGRAMME IS THIS ENGINE'S ARITHMETIC AND NOT THE
    # ESTIMATOR'S. `is_estimator_refusal` admits any ValueError and GateError is one, so inside
    # `_the_fit`'s block this refusal would reach the caller as the estimator objecting to their
    # data. See `_brant_blocks`, where exactly that had happened.
    stacked, exceeded = _the_existence_question(y, x, levels)
    require_no_separation(
        stacked,
        response=exceeded,
        fn=_FIT_FN,
        remedy=(
            "The question is the ORDERED model's own and not one dichotomy's: a single direction "
            "in the covariates, together with one cut point per boundary, places every "
            "observation inside its declared category, so the likelihood climbs without ever "
            "turning over. Each row of the programme is one observation at one of the boundaries "
            "it lies next to, and that row's outcome is the boundary's cumulative dichotomy "
            "1{y > j}. Drop the covariate that orders the outcome, or pool the levels it orders "
            "and fit the coarser scale."
        ),
    )

    model, fit = _the_fit(y, x, chosen)
    cut_points = _cut_points(model, fit)
    effects = _marginal_effects(model, fit, cut_points, levels)
    table = _coefficient_table(model, fit, level)
    thresholds = {
        f"{lower}{_BOUNDARY}{upper}": float(cut)
        for lower, upper, cut in zip(levels[:-1], levels[1:], cut_points, strict=True)
    }
    reported = {
        **{f"params[{name}]": value for name, value in zip(
            table["term"], table["estimate"], strict=True)},
        **{f"thresholds[{label}]": value for label, value in thresholds.items()},
        **{
            f"{column}[{term}]": value
            for column in ("std_error", "z_value", "p_value", "conf_low", "conf_high")
            for term, value in zip(table["term"], table[column], strict=True)
        },
        **{
            f"marginal_effects[{name}][{label}]": value
            for name, by_level in effects.items()
            for label, value in by_level.items()
        },
        "llf": float(fit.llf),
    }
    require_finite_estimates(
        pd.Series(reported),
        fn=_FIT_FN,
        quantity="estimates, thresholds, effects and intervals",
        remedy=(
            "A confidence level below 1 can still round to 1 in double precision -- "
            "1 - (1 - 0.9999999999999999) / 2 is exactly 1.0 -- and the normal quantile there is "
            "infinite. Ask for a level a double can hold away from the endpoint."
        ),
    )
    return {
        "params": {
            str(name): float(value)
            for name, value in zip(table["term"], table["estimate"], strict=True)
        },
        "thresholds": thresholds,
        "marginal_effects": effects,
        "coeftable": table,
        "llf": float(fit.llf),
        "nobs": int(fit.nobs),
        "link": chosen,
        "outcome": _the_reported_outcome(y, levels),
        "design": x,
    }


def ld_proportional_odds_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_proportional_odds_test`` -- method card #523.

    Ordered logit and probit.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted ordered model.
        alpha: [number, optional] Significance level. Default ``0.05``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        Declared on the method card:

        - precondition-domain
        - precondition-missing
        - precondition-rank
        - precondition-sample-size
        - precondition-degenerate

    Validation:
        Documented on the method card:

        - thresholds reports the CUT POINTS and not the parameters statsmodels stores: the last J-2
          stored parameters are the LOGARITHMS of the increments between adjacent cut points, and
          the stored vector is monotone increasing, so reporting it would be silently wrong and
          would pass any ordering check a reader applied
        - coeftable carries the covariates and no threshold row, because bse reports the standard
          errors of the stored parameterisation; measured against the standard errors Stata's [R]
          ologit prints for the same fit, the coefficient and the first cut point agree to 1e-7
          while the other three cut points are 4.4e-02, 4.6e-01 and 6.0e-01 away
        - the body also raises precondition-shape, which this field cannot name: a covariate table
          whose row labels are not the outcome's, one naming a column twice, and one with no columns
          at all are refused under that code, and gates/registry.py PRIMITIVES registers no
          primitive for it, so the closed vocabulary of precondition_gates has no entry to declare
          it with
        - link='cloglog' has no implementation in statsmodels 0.14.6 and is supplied here as
          scipy.stats.gumbel_l, whose CDF is the complementary log-log transform exactly; the
          library raises AttributeError on the string rather than refusing it
        - ld_proportional_odds_test is defined for the PROPORTIONAL-ODDS model alone: Brant (1990)
          compares the slopes of J-1 binary LOGISTIC regressions, so a fit made under the probit or
          the complementary log-log link is refused rather than tested under a restriction it was
          never estimated under
        - there is no oracle case for ld_proportional_odds_test and none can be written from the
          literature found: Brant (1990) prints an omnibus statistic of 11.2 on 6 degrees of freedom
          for 83 donated livers and never prints the 83 x 7 design behind it, and McCullagh (1980)
          prints his data and no Brant statistic. The arithmetic is checked instead against the
          scalar identity the three-category case reduces to, and against two contingency tables
          built to satisfy and to violate the restriction

    .. gen_wrappers: end of generated docstring

    Examples:
        McCullagh's Table 1, the tonsil sizes of 1398 children by whether they
        carry *Streptococcus pyogenes*. Three ordered categories and one covariate,
        so the omnibus test has one degree of freedom::

            >>> import numpy as np
            >>> import pandas as pd
            >>> counts = {"present": (19, 497), "enlarged": (29, 560),
            ...           "greatly enlarged": (24, 269)}
            >>> size, group = [], []
            >>> for level, (carriers, others) in counts.items():
            ...     size += [level] * (carriers + others)
            ...     group += [0.5] * carriers + [-0.5] * others
            >>> tonsils = pd.Series(pd.Categorical(
            ...     size, categories=list(counts), ordered=True), name="tonsil_size")
            >>> carrier = pd.DataFrame({"carrier": group})
            >>> fitted = ld_ordered_choice(y=tonsils, x=carrier)
            >>> checked = ld_proportional_odds_test(fit=fitted)
            >>> round(checked["brant_test"]["statistic"], 6)
            0.31557
            >>> checked["brant_test"]["parameter"], round(checked["brant_test"]["p_value"], 6)
            (1, 0.574282)
            >>> checked["reject"], checked["alpha"]
            (False, 0.05)

        The verdict is taken at the level asked for, and nothing else moves with
        it::

            >>> generous = ld_proportional_odds_test(fit=fitted, alpha=0.6)
            >>> generous["reject"], generous["brant_test"] == checked["brant_test"]
            (True, True)

    Note:
        FUNCTIONS USED. statsmodels 0.14.6 (BSD-3-Clause), one estimator repeated:
        ``api.Logit(indicator, design).fit()``, once per boundary of the outcome,
        for its coefficients and its fitted probabilities. Everything else --
        the joint covariance, the differencing contrast, the quadratic form and the
        chi-squared tail -- is this engine's, with ``numpy`` 2.5.2 for the linear
        algebra and ``scipy`` 1.18.0 for ``stats.chi2.sf``. THERE IS NO BRANT TEST
        IN statsmodels 0.14.6: ``grep -ril brant`` over the installed package
        returns nothing.

        WHERE THE NUMBERS COME FROM. Brant, R. (1990), *Assessing Proportionality
        in the Proportional Odds Model for Ordinal Logistic Regression*, Biometrics
        46(4), 1171-1178, doi:10.2307/2532457, section 3. The model is embedded in
        the augmented family ``logit gamma_j(x) = theta_j - beta_j' x`` with one
        slope vector per boundary, and the null is that they are all equal; the
        statistic is the Wald form ``(D b)' [D V D']^-1 (D b)`` on ``(J - 2) p``
        degrees of freedom, with ``D`` the differencing contrast and ``V`` the
        joint covariance whose off-diagonal blocks are the paper's own
        contribution. The per-covariate entries under ``by_variable`` restrict
        ``D`` to one covariate's block and are ``chi-squared`` on ``J - 2``.

        NO PUBLISHED NUMBER PROVES THIS NODE, AND THAT IS STATED RATHER THAN LEFT
        AS A GAP. Brant's own paper prints ``X^2 = 11.2`` on 6 degrees of freedom
        for 83 donated livers and describes the seven covariates without ever
        printing the design, so nothing can be rebuilt to compare against;
        McCullagh prints his data and no Brant statistic; and the dataset the
        sibling node's oracle case uses has a separated dichotomy, so this node
        refuses it. What stands in place of a published number is two independent
        checks, both in the module's tests: with three categories and one covariate
        the omnibus statistic reduces to ``(b_1 - b_2)^2 / Var(b_1 - b_2)``, which
        is rebuilt from the same two binary logits by a second route and agrees to
        1.7e-16; and two contingency tables, one satisfying the restriction exactly
        and one reversing the odds ratio between boundaries, are watched returning
        a statistic of 2.09e-28 and one of 72.81. Neither is an oracle and neither
        is labelled as one.

        DELIBERATELY OMITTED. Brant's SECOND, directional statistic, which targets
        a common multiplicative shift across boundaries and is chi-squared on
        ``J - 2``: card #523 promises one test, and the alternatives it names put
        the escape from a rejection in the generalised ordered model rather than in
        a second diagnostic here. Its BOOTSTRAP variant with it, which would also
        make this node stochastic while the contract declares no ``seed`` argument
        and ``cacheability.stochastic_unseeded`` false.

        GATES ADDED, AND THE SOURCE OF EACH. ``fit`` is a ``raw_handle``, so the
        registry hands back whatever the producing node returned and nothing in the
        contract says which node that was; a handle that does not carry an ordered
        outcome, a design indexed alike and a declared link is refused rather than
        reaching a ``KeyError``. TWO OF THE SIBLING NODE'S OWN RULES ARE ASKED
        AGAIN HERE FOR THE SAME REASON -- a handle carries no guarantee across, and
        both had been reaching the caller as the estimator objecting to their data.
        A ``nan`` in the design came back as "It reported ValueError: Invalid input
        for linprog: c must not contain values inf, nan, or None", which is scipy
        complaining from inside this engine's own programme; and a design that is
        collinear ONCE THE INTERCEPT IS ADDED came back as "It reported LinAlgError:
        Singular matrix". The second is not the sibling node's rank rule under
        another name: a constant column is full rank beside one covariate and is
        rank deficient beside that covariate AND the intercept these regressions
        carry, which is the design that is actually fitted. A fit made
        under the probit or complementary log-log link is refused because the
        restriction being tested is about log ODDS. ``alpha`` decides ``reject`` and
        is checked on the open unit interval. A binary outcome leaves ``(J - 2) p``
        at zero, and a chi-squared statistic on no degrees of freedom has a p-value
        of 0 whatever the data. THE ONE THAT MATTERS MOST IS ABOUT SEPARATION, and
        it is asked of each dichotomy in turn by
        :func:`~econflow_engine.gates.estimation.require_no_separation`, which
        solves Konis's (2007) linear programme rather than reading a convergence
        flag. MEASURED on the sibling node's own oracle dataset: no domestic car
        has an Excellent 1977 repair record, so ``1{rep77 > 4}`` is 45 zeros
        against no ones for one group, ``sm.Logit`` returns ``[-21.146504,
        19.983354]`` behind a ``ConvergenceWarning`` alone, and the estimate does
        not exist. The other three dichotomies of that table and both of
        McCullagh's are admitted, so the rule discriminates rather than blocks. It
        is NOT the question the sibling node asks of the ordered model itself: a
        separated dichotomy does not put the ordered estimate out of reach, and
        this very table is the oracle case, published to seven significant digits.

        THE QUESTION IS ASKED OF THE DESIGN INCLUDING THE INTERCEPT, and that is
        load-bearing rather than incidental -- it is also the contract that gate's
        ``design`` parameter now states. MEASURED: over the covariate alone the
        same fourth dichotomy scores an objective of zero and is ADMITTED, because
        the covariate is an indicator and no direction in it alone orders the
        outcome; it is the intercept that makes the separating hyperplane exist.
        The binary logits this node fits carry an intercept, so that is the design
        the existence question belongs to.

        AND IT IS ASKED OUTSIDE THE ``try`` THAT TRANSLATES THE ESTIMATOR'S
        EXCEPTIONS. ``GateError`` is a ``ValueError`` and
        :func:`~econflow_engine.gates.estimation.is_estimator_refusal` admits any
        ``ValueError``, so inside that block this gate's own refusal was caught and
        re-reported as the estimator's -- MEASURED on the oracle dataset: two
        stacked ``ld_proportional_odds_test:`` prefixes, the class name
        ``GateError`` quoted at the caller, and the authored per-dichotomy remedy
        buried inside a sentence about a fit that could not be estimated.

        A NEGATIVE STATISTIC IS REFUSED RATHER THAN REPORTED, and the reason is a
        mistake made while writing this. The joint covariance uses
        ``pi_max(j,l) - pi_j pi_l`` because for ``j <= l`` the event ``y > j`` and
        ``y > l`` is ``y > l``; using ``min`` there instead returned an omnibus
        statistic of -0.13397014178700709 on McCullagh's table with a p-value of
        exactly 1.0. A Wald statistic cannot be negative, and a p-value of 1 is
        exactly what a reader wants to see, so nothing about that output would have
        looked wrong.

        NO ARGUMENT OF THIS NODE REACHES AN EVALUATOR. ``alpha`` is a number
        reaching a comparison. ``fit`` is a ``raw_handle`` whose content is
        whatever the sibling node registered: the covariate names travel from it
        into ``by_variable``'s keys and into gate messages, and the outcome's name
        and level labels into the separation refusal's remedy. All of them are
        formatted and reported; none reaches a parser, a query or a path.
    """
    link, outcome, covariates = _the_stored_sample(fit)
    if link != _LOGIT:
        refuse_a_combination(
            fn=_TEST_FN,
            combination=f"testing proportional odds on a fit made with the {link} link",
            reason=(
                "Brant's test compares the slopes of J-1 binary LOGISTIC regressions, so the "
                "restriction it examines is a statement about log odds ratios. Under any other "
                "link the fitted coefficients are not log odds ratios and the augmented family "
                "the test compares against is not the one the model was estimated under."
            ),
            remedy=(
                "Re-run ld_ordered_choice with link='logit' and test that fit, or read the "
                "probit or complementary log-log fit without this diagnostic."
            ),
        )
    significance = float(alpha if alpha is not None else _declared(_TEST_FN, "alpha"))
    require_strictly_inside(significance, low=0.0, high=1.0, fn=_TEST_FN, arg="alpha")

    names = [str(name) for name in covariates.columns]
    for name in covariates.columns:
        # THE SIBLING NODE'S OWN RULE, ASKED AGAIN BECAUSE A HANDLE CARRIES NO GUARANTEE ACROSS.
        # ``fit`` is a raw_handle and a caller may register any mapping, so the design reaching
        # this node's arithmetic has not necessarily passed anything. Without this, a ``nan`` in it
        # reached the caller as "It reported ValueError: Invalid input for linprog: c must not
        # contain values inf, nan, or None" -- scipy complaining from inside the separation gate.
        require_no_missing(covariates[name], fn=_TEST_FN, arg=f'design["{name}"]')
    levels = tuple(outcome.cat.categories)
    degrees = (len(levels) - 2) * len(names)
    require_in_range(
        float(degrees),
        low=1.0,
        high=math.inf,
        fn=_TEST_FN,
        arg="the degrees of freedom of the Brant test",
    )

    codes = np.asarray(outcome.cat.codes, dtype=float)
    design = np.column_stack(
        [np.ones(len(codes)), covariates.to_numpy(dtype=float)]
    )
    indicators = [(codes > cut).astype(float) for cut in range(len(levels) - 1)]
    slopes, covariance = _brant_blocks(
        design, indicators, names, str(outcome.name), levels
    )

    width = len(names)
    boundaries = len(levels) - 1
    contrast = np.zeros(((boundaries - 1) * width, boundaries * width))
    for boundary in range(boundaries - 1):
        for column in range(width):
            contrast[boundary * width + column, column] = 1.0
            contrast[boundary * width + column, (boundary + 1) * width + column] = -1.0
    statistic = _wald(contrast, slopes, covariance)
    per_variable = {
        name: _wald(
            contrast[[boundary * width + column for boundary in range(boundaries - 1)], :],
            slopes,
            covariance,
        )
        for column, name in enumerate(names)
    }

    require_finite_estimates(
        pd.Series({"the omnibus statistic": statistic, **per_variable}),
        fn=_TEST_FN,
        quantity="chi-squared statistics",
        remedy=(
            "The statistic is a quadratic form in the differences between the boundaries' "
            "slopes; it has no value where their joint covariance cannot be inverted."
        ),
    )
    for label, value in (("the omnibus statistic", statistic), *per_variable.items()):
        require_in_range(
            value, low=0.0, high=math.inf, fn=_TEST_FN, arg=f"the Brant chi-squared for {label}"
        )
    p_value = float(stats.chi2.sf(statistic, degrees))
    return {
        "brant_test": {
            "statistic": statistic,
            "parameter": degrees,
            "p_value": p_value,
            "method": "Brant (1990) omnibus Wald test of proportional odds",
        },
        "by_variable": {
            name: {
                "statistic": value,
                "parameter": len(levels) - 2,
                "p_value": float(stats.chi2.sf(value, len(levels) - 2)),
            }
            for name, value in per_variable.items()
        },
        "alpha": significance,
        "reject": bool(p_value < significance),
    }
