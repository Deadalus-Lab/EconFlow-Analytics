# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``count_models`` -- method card #524.

#524 Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle

Category 16-limited-dependent; module ``count_models``.

Reference implementation: statsmodels.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Literal

import pandas as pd

from econflow_engine.generated.args.c16_limited_dependent import NODE_META, wire_model

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ld_count_model",
    "ld_overdispersion_test",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---

import math

import numpy as np
from statsmodels.discrete.count_model import (
    ZeroInflatedGeneralizedPoisson,
    ZeroInflatedNegativeBinomialP,
    ZeroInflatedPoisson,
)
from statsmodels.discrete.discrete_model import (
    GeneralizedPoisson,
    NegativeBinomialP,
    Poisson,
)
from statsmodels.discrete.truncated_model import (
    HurdleCountModel,
    TruncatedLFGeneralizedPoisson,
    TruncatedLFNegativeBinomialP,
    TruncatedLFPoisson,
)

from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_combination,
    refuse_estimator_failure,
    require_a_column,
    require_an_aligned_index,
    require_an_observed_value,
    require_convergence,
    require_counts,
    require_distinct_column_names,
    require_finite_estimates,
    require_strictly_inside,
)
from econflow_engine.gates.primitives import (
    require_full_rank,
    require_min_length,
    require_no_missing,
)

#: The node this module's gate messages name.
_FN = "ld_count_model"

#: The intercept this body adds to the caller's covariates, under the name
#: statsmodels' own ``add_constant`` uses. The estimator adds none of its own:
#: MEASURED, a design without it fits a model whose log-mean passes through the
#: origin, silently.
_INTERCEPT = "const"

#: NB2 -- ``Var(y|x) = mu + alpha mu^2``, which is what ``negative_binomial``
#: means here and the default of every negative-binomial class in the library.
_NEGATIVE_BINOMIAL_EXPONENT = 2

#: GP-1, the Consul-Famoye form. PINNED RATHER THAN DEFAULTED, and that is a
#: correction rather than a preference: MEASURED against statsmodels 0.14.6,
#: ``GeneralizedPoisson`` defaults to ``p=1`` while
#: ``ZeroInflatedGeneralizedPoisson`` and ``TruncatedLFGeneralizedPoisson``
#: default to ``p=2``, so one value of this node's ``family`` would otherwise mean
#: two different models depending on ``zeros``.
_GENERALISED_POISSON_EXPONENT = 1

#: The hurdle's zero equation. ``family`` names the distribution of the COUNTS,
#: and the crossing of the hurdle is a binary event; statsmodels spells that
#: binary model ``zerodist='poisson'`` (a censored Poisson) and this node does not
#: expose the choice.
_HURDLE_ZERO_MODEL = "poisson"

#: (zeros, family) -> the class that fits it. Hurdle is absent because it is ONE
#: class parameterised by ``dist``; the two combinations statsmodels does not
#: carry are refused before this mapping is read.
_ESTIMATORS: dict[str, dict[str, Any]] = {
    "none": {
        "poisson": Poisson,
        "negative_binomial": NegativeBinomialP,
        "generalised_poisson": GeneralizedPoisson,
    },
    "zero_inflated": {
        "poisson": ZeroInflatedPoisson,
        "negative_binomial": ZeroInflatedNegativeBinomialP,
        "generalised_poisson": ZeroInflatedGeneralizedPoisson,
    },
    "truncated": {
        "poisson": TruncatedLFPoisson,
        "negative_binomial": TruncatedLFNegativeBinomialP,
        "generalised_poisson": TruncatedLFGeneralizedPoisson,
    },
}

#: The families that estimate a dispersion parameter, which the estimator appends
#: to the coefficient vector as its LAST entry. Poisson estimates none.
_DISPERSED = frozenset({"negative_binomial", "generalised_poisson"})

#: The exponent keyword each family carries, where it carries one.
_EXPONENTS: dict[str, int] = {
    "negative_binomial": _NEGATIVE_BINOMIAL_EXPONENT,
    "generalised_poisson": _GENERALISED_POISSON_EXPONENT,
}


def _declared(argument: str) -> Any:
    """The default ``node-specs.json`` publishes for one argument of this node.

    An omitted optional argument reaches a body as ``None`` -- ``adapt_args``
    fills in a declared default only when the call comes through the wire, and a
    direct Python call does not. The value is READ FROM THE CONTRACT rather than
    written out here, so the two can never disagree: a default this body spelled
    out itself would be a behaviour no client can read out of the contract.
    """
    return NODE_META[_FN].defaults[argument]


def _the_design(y: pd.Series, x: pd.DataFrame) -> pd.DataFrame:
    """The covariates with an intercept in front, gated as one matrix.

    THE GATES BELONG TO THE ASSEMBLED FRAME AND NOT TO THE ARGUMENT, for the same
    reason the first 2.2 body walks its assembled formula: the intercept is added
    here, so a caller's column named ``const`` and a caller's duplicated column
    are the same defect and only the assembled frame can see either.
    """
    require_an_aligned_index(
        x,
        reference=y.index,
        fn=_FN,
        arg="x",
        remedy="Give the covariates the response's own index, row for row.",
    )
    design = pd.concat([pd.Series(1.0, index=y.index, name=_INTERCEPT), x], axis=1)
    # BEFORE THE COLUMN WALK, and the order is load-bearing: `x[name]` on a frame
    # carrying that name twice returns a FRAME, and the numeric primitive would
    # then refuse it for its shape and say nothing about the duplicate.
    require_distinct_column_names(
        design,
        fn=_FN,
        arg="x plus the intercept",
        remedy=(
            f"This node adds the intercept and calls it {_INTERCEPT!r}, so a "
            f"covariate of that name is the same column twice. Rename it, and give "
            f"every other covariate a name of its own."
        ),
    )
    for name in x.columns:
        require_no_missing(x[name], fn=_FN, arg=f'x["{name}"]')
    # AFTER the column walk, because a rank is taken over floats and a column of
    # labels cannot be cast to one.
    require_full_rank(design, fn=_FN, arg="x plus the intercept")
    return design


def _the_inflation_design(
    design: pd.DataFrame, *, x: pd.DataFrame, covariates: Sequence[str] | None
) -> pd.DataFrame:
    """The inflation equation's own design: an intercept, and the named covariates.

    THE NAMES ARE CHECKED AGAINST ``x`` AND NOT AGAINST THE ASSEMBLED FRAME, so
    that ``inflation_covariates=['const']`` names something the caller supplied
    rather than something this body added. MEASURED: an absent name reaches pandas
    as a ``KeyError``, which derives from ``LookupError`` rather than from
    ``ValueError`` and so is not one of the classes the estimator translation
    recognises -- unrefused, it is a traceback.

    An empty selection is the constant alone, which is what the estimator fits when
    it is handed no inflation design at all: MEASURED, ``ZeroInflatedPoisson`` with
    ``exog_infl=None`` and with the constant column return the same
    ``llf = -258.62115252586733``.

    THIS DOCSTRING IS THAT FIGURE'S ONE HOME, as
    :func:`~econflow_engine.gates.estimation.require_counts` is its own figure's.
    Taken from ``engine/``::

        python -c "import sys, pandas as pd
        sys.path.insert(0, '.')
        from statsmodels.discrete.count_model import ZeroInflatedPoisson as M
        from tests.wrappers.c16_limited_dependent.test_count_models import sample
        y, x = sample()
        d = pd.concat([pd.Series(1.0, index=y.index, name='const'), x], axis=1)
        print(M(y, d, exog_infl=None).fit(disp=0).llf,
              M(y, d, exog_infl=d[['const']]).fit(disp=0).llf)"
    """
    names = list(covariates or ())
    for name in names:
        require_a_column(x, column=name, fn=_FN, arg="inflation_covariates")
    inflation = design[[_INTERCEPT, *names]]
    require_distinct_column_names(
        inflation,
        fn=_FN,
        arg="inflation_covariates",
        remedy="Name each inflation covariate once.",
    )
    return inflation


def _refuse_what_the_library_cannot_fit(
    *, family: str, zeros: str, exposure: pd.Series | None, covariates: Sequence[str] | None
) -> None:
    """The three argument combinations that have no fit behind them.

    TWO OF THEM WOULD CRASH AND ONE WOULD BE IGNORED IN SILENCE, all three
    measured against statsmodels 0.14.6. ``HurdleCountModel`` raises
    ``NotImplementedError`` for an exposure and for a generalised-Poisson
    component, and ``NotImplementedError`` is neither a ``ValueError`` nor a class
    of the library's own, so nothing translates it into a refusal. The third is
    ours: no estimator here has an inflation equation unless ``zeros`` asks for
    one, so inflation covariates would simply not be fitted.
    """
    if zeros == "hurdle" and exposure is not None:
        refuse_a_combination(
            fn=_FN,
            combination="zeros='hurdle' together with an exposure",
            reason=(
                "statsmodels 0.14.6 raises NotImplementedError for an offset or an "
                "exposure on a hurdle model, so there is no fit to report."
            ),
            remedy=(
                "Fit the hurdle without the exposure, or keep the exposure and "
                "choose zeros='zero_inflated', which admits one."
            ),
        )
    if zeros == "hurdle" and family == "generalised_poisson":
        refuse_a_combination(
            fn=_FN,
            combination="zeros='hurdle' with family='generalised_poisson'",
            reason=(
                "statsmodels 0.14.6 implements the hurdle for the Poisson and the "
                "negative binomial only."
            ),
            remedy="Choose family='poisson' or family='negative_binomial'.",
        )
    if covariates is not None and zeros != "zero_inflated":
        refuse_a_combination(
            fn=_FN,
            combination=f"inflation_covariates with zeros={zeros!r}",
            reason="Only a zero-inflated model has an inflation equation to put them in.",
            remedy=(
                "Pass zeros='zero_inflated' to fit that equation, or drop "
                "inflation_covariates."
            ),
        )


def _fit_the_model(
    *,
    family: str,
    zeros: str,
    y: pd.Series,
    design: pd.DataFrame,
    inflation: pd.DataFrame | None,
    exposure: pd.Series | None,
) -> Any:
    """Build the estimator this combination names and fit it. Refuses, never crashes.

    ``exposure`` IS PASSED ON ITS NATURAL SCALE. The estimator logs it and adds it
    to the linear prediction with a coefficient fixed at one, which is what card
    #524's third trap asks for; a caller's own ``log`` would be applied twice.

    THE FIT RUNS UNDER numpy's ERROR STATE AND NOT UNDER THE CALLER'S, and all
    four states are relaxed because all four were MEASURED firing inside a fit
    that is behaving normally. Under ``np.seterr(all='raise')`` -- which is how
    this repository's suite runs -- a negative-binomial search over Doll and Hill's
    ten rows raises ``FloatingPointError: invalid value encountered in log``, and a
    zero-inflated negative binomial over 200 rows raises ``FloatingPointError:
    underflow encountered in exp``. An underflow in ``exp`` is the likelihood
    evaluated far out in the tail, where the answer IS zero; numpy's own shipped
    state ignores it, and it is the caller's ``seterr`` rather than the data that
    turns it into an exception.

    WHAT THIS DOES NOT SILENCE. The block encloses the estimator's call and
    nothing else, so none of this engine's own arithmetic is inside it, and a fit
    that reached a degenerate optimum is caught where it belongs -- by the
    convergence gate at the call site, on a flag the estimator sets, rather than by
    whichever intermediate happened to overflow first.
    """
    keywords: dict[str, Any] = {}
    if exposure is not None:
        keywords["exposure"] = exposure
    if family in _EXPONENTS:
        keywords["p"] = _EXPONENTS[family]
    if zeros == "hurdle":
        constructor: Any = HurdleCountModel
        keywords["dist"] = "negbin" if family == "negative_binomial" else "poisson"
        keywords["zerodist"] = _HURDLE_ZERO_MODEL
    else:
        constructor = _ESTIMATORS[zeros][family]
        if inflation is not None:
            keywords["exog_infl"] = inflation
    try:
        with np.errstate(
            divide="ignore", invalid="ignore", over="ignore", under="ignore"
        ):
            # `disp=0` because the optimiser PRINTS its iteration log otherwise,
            # and nothing in this engine writes to stdout.
            return constructor(y, design, **keywords).fit(disp=0)
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error,
            fn=_FN,
            code="precondition-degenerate",
            remedy=(
                "The response and the covariates must describe a model the "
                "likelihood can be maximised for: a response with some variation "
                "in it, and covariates that are not determined by one another."
            ),
        )


def _blocks(fit: Any, *, family: str, width: int) -> tuple[int, int]:
    """Where the COUNT equation's coefficients start and stop in the vector.

    ONE RULE FOR EVERY BRANCH, AND IT IS POSITIONAL BY MEASUREMENT. Across all
    eleven combinations statsmodels 0.14.6 fits, the count coefficients are the
    last ``width`` entries before the dispersion parameter, and whatever precedes
    them is the zero equation -- ``inflate_*`` for a zero-inflated model, ``zm_*``
    for a hurdle, nothing at all for the others.

    NOT KEYED ON THE NAME ``alpha``, which is the tempting reading and is wrong:
    MEASURED, a covariate called ``alpha`` puts that name in the vector twice, and
    a Poisson with such a covariate would be read as carrying a dispersion
    parameter it never estimated. The family says whether one was estimated.
    """
    end = len(np.asarray(fit.params)) - (1 if family in _DISPERSED else 0)
    return end - width, end


def _the_result(
    fit: Any,
    *,
    family: str,
    zeros: str,
    y: pd.Series,
    design: pd.DataFrame,
    inflation: pd.DataFrame | None,
    level: float,
) -> dict[str, Any]:
    """The payload card #524 promises, every field read off one fit.

    A PREFIX IS THE ESTIMATOR'S AND A SUFFIX IS THIS BODY'S, on both equations.
    MEASURED against statsmodels 0.14.6: ``HurdleCountModel`` labels BOTH of its
    equations positionally, so over a design of ``const``, ``age``, ``x1`` it
    reports ``zm_const``, ``zm_x1``, ``zm_x2`` and ``const``, ``x1``, ``x2`` --
    and a caller with a covariate genuinely called ``x1`` reads ``zm_x1`` as its
    zero-equation coefficient when it is ``age``'s. The ``inflate_`` and ``zm_``
    prefixes say WHICH EQUATION a row belongs to and nothing else in the table
    does, so they are kept; the suffix is a position and is replaced by the
    design's own column name. ``ZeroInflated*`` needs no such repair: MEASURED, it
    names its inflation rows after the frame it is handed -- ``inflate_age`` for
    ``inflation_covariates=['age']`` -- so there the estimator's labels are already
    the caller's.
    """
    values = np.asarray(fit.params, dtype=float)
    start, end = _blocks(fit, family=family, width=len(design.columns))
    names = [str(name) for name in design.columns]
    reported = [str(term) for term in fit.params.index]
    coefficients = dict(zip(names, values[start:end], strict=True))
    # A hurdle fits the zero equation on the SAME design, so its block is this
    # design's columns under the estimator's prefix. Every other branch's zero
    # block is the estimator's own and is already named after a frame.
    zero_equation = (
        [f"zm_{name}" for name in names] if zeros == "hurdle" else reported[:start]
    )
    # `np.exp` UNDER A RELAXED OVERFLOW STATE, so that a coefficient with no
    # representable exponential arrives as `inf` and the gate below can name the
    # term it belongs to. `math.exp` raises `OverflowError` instead -- an
    # `ArithmeticError` this body would then have to translate, and translating
    # arithmetic of the ENGINE'S OWN as the estimator's would report a fit that
    # converged as a fit that failed. An underflow keeps numpy's answer: exp of a
    # coefficient below about -745 IS zero to double precision.
    with np.errstate(over="ignore", under="ignore"):
        ratios = pd.Series(np.exp(values[start:end]), index=names)
    require_finite_estimates(
        ratios,
        fn=_FN,
        quantity="rate ratios",
        remedy=(
            "exp(beta) has no value in double precision above a coefficient of "
            "about 709, and a coefficient that large is the covariate's units "
            "rather than its effect: dividing a covariate by 1000 multiplies its "
            "coefficient by 1000 and leaves the fit untouched. Rescale it."
        ),
    )
    interval = np.asarray(fit.conf_int(alpha=1.0 - level), dtype=float)
    return {
        "params": {term: float(value) for term, value in coefficients.items()},
        "rate_ratios": {term: float(value) for term, value in ratios.items()},
        "coeftable": pd.DataFrame(
            {
                "term": [*zero_equation, *names, *reported[end:]],
                "estimate": values,
                "std_error": np.asarray(fit.bse, dtype=float),
                "z_value": np.asarray(fit.tvalues, dtype=float),
                "p_value": np.asarray(fit.pvalues, dtype=float),
                "conf_low": interval[:, 0],
                "conf_high": interval[:, 1],
            }
        ),
        "dispersion": float(values[-1]) if family in _DISPERSED else None,
        "zero_inflation": (
            None
            if inflation is None
            else {
                str(term): float(value)
                for term, value in zip(inflation.columns, values[:start], strict=True)
            }
        ),
        "vuong": None,
        "fitted_values": pd.Series(
            np.asarray(fit.predict(), dtype=float), index=y.index, name="fitted_values"
        ),
        "llf": float(fit.llf),
        "aic": float(fit.aic),
        "bic": float(fit.bic),
        "nobs": int(fit.nobs),
        "family": family,
        "zeros": zeros,
    }


def ld_count_model(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    family: Literal["poisson", "negative_binomial", "generalised_poisson"] | None = None,
    zeros: Literal["none", "zero_inflated", "hurdle", "truncated"] | None = None,
    exposure: pd.Series | None = None,
    inflation_covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_count_model`` -- method card #524.

    Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Count outcome.
        x: [df_handle, required] Covariate table.
        family: [enum, optional] Count family. Default ``'negative_binomial'``.
        zeros: [enum, optional] Zero handling. Default ``'none'``.
        exposure: [series_handle, optional] Exposure entering as an offset.
        inflation_covariates: [series_codes, optional] Covariates in the inflation equation.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    .. gen_wrappers: end of generated docstring

    Examples:
        Doll and Hill's British doctors, ten rows of coronary deaths against
        person-years at risk, as a Poisson rate model on smoking and age. This is
        the fit the oracle case under ``tests/oracle/c16_limited_dependent/``
        compares with the published table, and the two numbers below are the ones
        that table prints::

            >>> import pandas as pd
            >>> deaths = pd.Series([32, 104, 206, 186, 102, 2, 12, 28, 28, 31])
            >>> person_years = pd.Series(
            ...     [52407, 43248, 28612, 12663, 5317, 18790, 10673, 5710, 2585, 1462]
            ... )
            >>> band = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
            >>> covariates = pd.DataFrame(
            ...     {"smokes": [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]}
            ...     | {f"age_{k}": [int(b == k) for b in band] for k in (1, 2, 3, 4)}
            ... )
            >>> fit = ld_count_model(
            ...     y=deaths, x=covariates, family="poisson", exposure=person_years
            ... )
            >>> round(fit["llf"], 6)
            -33.600153
            >>> round(fit["rate_ratios"]["smokes"], 6)
            1.425519
            >>> fit["nobs"], sorted(fit["params"])[:2]
            (10, ['age_1', 'age_2'])

        A Poisson estimates no dispersion parameter, so the field the card
        promises for it is empty rather than zero::

            >>> fit["dispersion"] is None
            True

        An exposure of zero is refused rather than logged::

            >>> ld_count_model(
            ...     y=deaths, x=covariates, family="poisson",
            ...     exposure=person_years * 0,
            ... )
            Traceback (most recent call last):
            econflow_engine.errors.GateError: ld_count_model: "exposure" carries 10...

    Note:
        FUNCTIONS USED. statsmodels 0.14.6 (BSD-3-Clause), one estimator class per
        (``family``, ``zeros``) pair: ``discrete_model.Poisson``,
        ``NegativeBinomialP`` and ``GeneralizedPoisson``; ``count_model``'s three
        ``ZeroInflated*`` classes; ``truncated_model.HurdleCountModel`` and the
        three ``TruncatedLF*`` classes. Each is fitted with ``.fit(disp=0)`` at the
        library's own optimiser and iteration limit. ``pandas`` 2.3.3 assembles the
        design and the coefficient table, ``numpy`` 2.5.2 reads the coefficient
        vector and exponentiates it. The estimator supplies the coefficients,
        their standard errors,
        z statistics, p-values and confidence intervals, the log-likelihood, the
        information criteria and the fitted means; ``rate_ratios`` is
        ``exp(params)``, which is arithmetic and not a second estimate.

        WHAT EACH ARGUMENT MEANS HERE, WHERE THE LIBRARY LEAVES IT OPEN.
        ``negative_binomial`` is NB2 -- ``Var(y|x) = mu + alpha mu^2`` -- which is
        every negative-binomial class's own default. ``generalised_poisson`` is
        GP-1, PINNED rather than defaulted: MEASURED, ``GeneralizedPoisson``
        defaults to ``p=1`` while ``ZeroInflatedGeneralizedPoisson`` and
        ``TruncatedLFGeneralizedPoisson`` default to ``p=2``, so leaving it to the
        library would make one ``family`` mean two models. ``zeros='truncated'`` is
        truncation at zero, the library's own default. A hurdle's zero equation is
        a censored Poisson (``zerodist='poisson'``) and ``family`` names the
        distribution of the counts alone. The inflation link is the logit of
        Lambert (1992). The intercept is added here and named ``const``.

        WHAT THIS ENGINE DOES NOT COMPUTE, AND WHY. ``vuong`` IS NULL ON EVERY
        BRANCH. Card #524 promises a comparison of the zero-inflated model against
        the plain one, and MEASURED, statsmodels 0.14.6 carries no Vuong test:
        ``grep -rniE 'vuong' site-packages/statsmodels/ --include=*.py`` returns
        nothing. The statistic of Vuong (1989), doi:10.2307/1912557, would
        therefore be arithmetic this engine owns, and no published fit of a
        zero-inflated model on a small, fully-listed table was found to check it
        against -- so the field is present and empty rather than filled with a
        number nobody can verify. This is a defect in the card, recorded here
        rather than papered over.

        DELIBERATELY OMITTED. Robust and cluster-robust standard errors: no
        argument of this node reaches ``fit(cov_type=...)``, so every standard
        error here is the model-based one, which is exactly the choice card #524's
        first trap is about -- overdispersion leaves the Poisson coefficients
        consistent and its standard errors too small. Marginal effects: the
        results objects expose ``get_margeff``, and the card asks for coefficients
        on the log-mean scale. NB1, the negative-binomial exponents other than 2
        and the generalised-Poisson exponents other than 1: the node's enum names a
        family, not an exponent. ``offset`` as a separate argument from
        ``exposure``: the contract carries one, and it is the exposure.

        GATES ADDED, AND THE SOURCE OF EACH. THE FIRST TWO ARE THE SILENT
        ACCEPTANCES, both measured on the ten rows above. A response that is not
        whole: ``Poisson(deaths + 0.5, X, exposure=t)`` fits and returns
        ``llf = -33.269482`` under ``warnings.simplefilter('always')`` with NO
        warning at all. A response below zero: ``Poisson(deaths - 40, ...)`` raises
        nothing and returns ``llf = nan``. Cameron and Trivedi (2013) chapter 1 and
        Lambert (1992) section 2 both define these models on the non-negative
        integers. THE REST, each with what it was measured blocking: an exposure on
        or below zero returns ``llf = nan`` from a fit that raised nothing (the
        offset is ``log t``); an argument whose index is a PERMUTATION of the
        response's is used row by row as given -- the same ten person-year figures
        under a reversed index return ``llf = -41.974688`` against ``-33.600153``,
        and nothing in the result says which happened; a design of rank 6 over 7
        columns is fitted SILENTLY and reports the full-rank fit's own
        log-likelihood beside coefficients that are not identified, with
        ``check_rank`` at its default; two columns sharing a name are fitted and
        one of the two coefficients disappears from any mapping keyed by name; a
        zero-inflated fit over a sample with no zeros CONVERGES, estimating an
        inflation probability from nothing; a zero-truncated fit over a sample WITH
        zeros silently drops them and reports the positives' own fit; four
        observations against seven parameters raise ``LinAlgError`` out of the
        optimiser, which says "Singular matrix" where the rule is about degrees of
        freedom; a confidence level of exactly 1 is an interval of infinite width,
        which the inclusive range primitive admits; and a fit that gave up returns
        a result object shaped exactly like a fit, with ``converged`` false and
        every standard error ``nan``. Two combinations are refused before any of
        that, because statsmodels raises ``NotImplementedError`` for them and
        ``NotImplementedError`` is the exception an unwritten body raises: a hurdle
        with an exposure, and a hurdle with a generalised-Poisson component. One
        more is ours: inflation covariates outside a zero-inflated model would be
        accepted and never fitted.

        TWO GATES ASK ABOUT THE FIT'S OUTPUT RATHER THAN ITS INPUTS, and they were
        added by review after every one of the rules above had been written: this
        body gated what arrived fourteen times and gated what it returned not at
        all. MEASURED, both on the 200-row sample of the test module. A covariate
        multiplied by 1e6 -- the scale of a population, a currency amount or a
        market value -- CONVERGES and returns ``llf`` and every coefficient
        ``nan``; forty rows against an exposure of 1e-307 do the same. Serialised
        there is no ``NaN`` token, so the payload is well-formed JSON whose
        estimates are null -- and three of this card's fields are null ON PURPOSE,
        so a caller cannot tell the two apart. That is why the rule is asked of
        ``fit.params`` and ``fit.llf`` and never of the assembled mapping. The
        second is the same rule over a DERIVED number: a covariate divided by 1000
        leaves the fit untouched and multiplies its coefficient by 1000, and
        ``exp`` of 820.81 has no value in double precision -- which used to raise
        ``OverflowError`` out of this body, past ``make_tool`` (``GateError``
        only) and past ``run_method`` (``NotImplementedError`` only), to the
        caller as a crash.

        NO ARGUMENT OF THIS NODE REACHES AN EVALUATOR, and that is checked rather
        than assumed, because the first 2.2 body shipped a remote-code-execution
        through an argument of kind ``string`` spliced into a formula. There is no
        formula here: ``y``, ``x`` and ``exposure`` arrive as pandas objects and are
        passed to a constructor that takes arrays; ``family`` and ``zeros`` are
        enums the wire model has already checked against the contract's own lists
        and are used as mapping keys, never interpolated; ``conf_level`` is a
        number. ``inflation_covariates`` is kind ``series_codes``, which
        ``kinds.py`` types as ``list[str]`` with NO constraint on the contents, and
        it is the one argument that carries caller-chosen text into anything -- a
        pandas COLUMN LOOKUP, ``design[[...]]``, which is a hash lookup and not an
        expression. ``require_a_bare_name`` is therefore NOT applied to it: it
        would narrow the contract, since a column may legitimately be called
        ``age 45-54``, and it would guard a path that evaluates nothing.
        ``require_a_column`` is applied instead, so an unknown name is a refusal
        rather than the ``KeyError`` pandas would raise.
    """
    chosen_family = str(family if family is not None else _declared("family"))
    chosen_zeros = str(zeros if zeros is not None else _declared("zeros"))
    level = float(conf_level if conf_level is not None else _declared("conf_level"))

    require_strictly_inside(level, low=0.0, high=1.0, fn=_FN, arg="conf_level")
    require_counts(
        y,
        minimum=1 if chosen_zeros == "truncated" else 0,
        fn=_FN,
        arg="y",
        remedy=(
            "Supply the counts themselves rather than a rate or a share; a rate "
            "belongs in this model as the response over an exposure."
            if chosen_zeros != "truncated"
            else "A zero-truncated model is defined where no zero can be observed."
        ),
    )
    if chosen_zeros in {"zero_inflated", "hurdle"}:
        require_an_observed_value(
            y,
            level=0.0,
            fn=_FN,
            arg="y",
            remedy=(
                "Both of these models are about where the zeros come from. With "
                "none in the sample, fit zeros='none' instead."
            ),
        )
    _refuse_what_the_library_cannot_fit(
        family=chosen_family,
        zeros=chosen_zeros,
        exposure=exposure,
        covariates=inflation_covariates,
    )
    # THE LENGTH RULE IS ASKED BEFORE THE DESIGN IS BUILT, because a sample too
    # short for its own model is also rank-deficient, and "at least one column is
    # a linear combination of the others" is the wrong account of four rows
    # against seven parameters. THE ZERO EQUATION IS COUNTED TOO: a hurdle
    # estimates the design twice and a zero-inflated model estimates the inflation
    # design beside it.
    width = len(x.columns) + 1
    estimated = (
        width
        + (width if chosen_zeros == "hurdle" else 0)
        + (1 + len(inflation_covariates or ()) if chosen_zeros == "zero_inflated" else 0)
        + (1 if chosen_family in _DISPERSED else 0)
    )
    require_min_length(y, minimum=estimated + 1, fn=_FN, arg="y")
    design = _the_design(y, x)
    inflation = (
        _the_inflation_design(design, x=x, covariates=inflation_covariates)
        if chosen_zeros == "zero_inflated"
        else None
    )
    if exposure is not None:
        require_an_aligned_index(
            exposure,
            reference=y.index,
            fn=_FN,
            arg="exposure",
            remedy="Give the exposure the response's own index, row for row.",
        )
        require_strictly_inside(
            exposure, low=0.0, high=math.inf, fn=_FN, arg="exposure"
        )
    fit = _fit_the_model(
        family=chosen_family,
        zeros=chosen_zeros,
        y=y,
        design=design,
        inflation=inflation,
        exposure=exposure,
    )
    # MEASURED: a hurdle reports a LIST -- one flag per sub-fit -- where every
    # other class reports one boolean. Both are the same question.
    reported = fit.mle_retvals["converged"]
    require_convergence(
        converged=all(reported) if isinstance(reported, list) else bool(reported),
        fn=_FN,
        estimator="maximum-likelihood",
        remedy=(
            "A count model that does not converge is usually a mean the covariates "
            "cannot reach: check for an outlying count, for a covariate on a very "
            "different scale from the others, and for a zero rule the sample does "
            "not support."
        ),
    )
    # THE CONVERGENCE FLAG IS NOT A STATEMENT THAT THE NUMBERS ARE NUMBERS.
    # MEASURED: the same 200 rows with `w` multiplied by 1e6 converge, raise
    # nothing, and come back with every coefficient and the log-likelihood `nan`.
    # ASKED HERE AND NOT OF THE ASSEMBLED PAYLOAD, because three of that mapping's
    # fields are null ON PURPOSE and a finiteness rule over the whole of it would
    # refuse a Poisson for estimating no dispersion.
    require_finite_estimates(
        pd.concat([fit.params, pd.Series({"llf": float(fit.llf)})]),
        fn=_FN,
        quantity="coefficients and log-likelihood",
        remedy=(
            "The iteration reported success and the numbers it stopped at are not "
            "numbers, which is a linear predictor the exponential cannot hold: "
            "look for a covariate in units of population, currency or market "
            "value, or an exposure so small that its logarithm dominates every "
            "coefficient, and rescale it."
        ),
    )
    return _the_result(
        fit,
        family=chosen_family,
        zeros=chosen_zeros,
        y=y,
        design=design,
        inflation=inflation,
        level=level,
    )


def ld_overdispersion_test(
    *,
    fit: Any,
    alpha: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_overdispersion_test`` -- method card #524.

    Count models: Poisson, negative binomial, generalised Poisson, zero-inflated and hurdle.

    Category 16-limited-dependent; memory class ``light``.

    Args:
        fit: [raw_handle, required] Handle to a fitted count model.
        alpha: [number, optional] Significance level. Default ``0.05``.

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
        "ld_overdispersion_test: not implemented."
    )
