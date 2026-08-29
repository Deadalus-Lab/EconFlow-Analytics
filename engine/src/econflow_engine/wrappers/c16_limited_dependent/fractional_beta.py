# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``fractional_beta`` -- method card #527.

#527 Fractional response and beta regression

Category 16-limited-dependent; module ``fractional_beta``.

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
    "ld_fractional_response",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---

import numpy as np
from statsmodels.genmod.families import Binomial
from statsmodels.genmod.families.links import CLogLog, Logit, LogLog, Probit
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.othermod.betareg import BetaModel

from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_combination,
    refuse_estimator_failure,
    require_a_column,
    require_an_aligned_index,
    require_convergence,
    require_distinct_column_names,
    require_finite_estimates,
    require_strictly_inside,
    require_within_bounds,
)
from econflow_engine.gates.primitives import (
    require_full_rank,
    require_min_length,
    require_no_missing,
    require_variance,
)

#: The node this module's gate messages name.
_FN = "ld_fractional_response"

#: The intercept this body adds to the caller's covariates, under the name
#: statsmodels' own ``add_constant`` uses. Neither estimator adds one of its own.
_INTERCEPT = "const"

#: The link objects the node's enum names, all four confirmed present in
#: ``statsmodels.genmod.families.links`` and accepted by BOTH estimators.
_LINKS: dict[str, Any] = {
    "logit": Logit,
    "probit": Probit,
    "cloglog": CLogLog,
    "loglog": LogLog,
}

#: THE ROBUST COVARIANCE THE FRACTIONAL BRANCH IS FITTED WITH, and it is pinned
#: rather than defaulted. Papke and Wooldridge (2008), section 3, on the estimator
#: of Papke and Wooldridge (1996): "In applying the Bernoulli QMLE, one needs to
#: adjust the standard errors." The Bernoulli quasi-likelihood is consistent under
#: a correctly specified mean whatever the true conditional variance, and the
#: model-based standard error is the one that assumes the variance is right. The
#: library's default is that model-based error and nothing warns. HC0 rather than
#: HC1 or HC3 because the paper asks for a heteroskedasticity-robust adjustment
#: and names none of the small-sample variants; no argument of this node reaches
#: the choice, so it is recorded here.
_COVARIANCE = "HC0"


def _declared(argument: str) -> Any:
    """The default ``node-specs.json`` publishes for one argument of this node.

    An omitted optional argument reaches a body as ``None`` -- ``adapt_args``
    fills in a declared default only when the call comes through the wire, and a
    direct Python call does not. The value is READ FROM THE CONTRACT rather than
    written out here, so the two can never disagree; ``precision_covariates`` is
    absent from that mapping because the contract declares no default for it, and
    ``None`` is therefore its only meaning.
    """
    return NODE_META[_FN].defaults[argument]


def _the_design(y: pd.Series, x: pd.DataFrame) -> pd.DataFrame:
    """The covariates with an intercept in front, gated as one matrix.

    THE GATES BELONG TO THE ASSEMBLED FRAME AND NOT TO THE ARGUMENT, for the
    reason the sibling count-model body states: the intercept is added here, so a
    caller's column named ``const`` and a caller's duplicated column are the same
    defect and only the assembled frame can see either.
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


def _the_precision_design(
    design: pd.DataFrame, *, x: pd.DataFrame, covariates: Sequence[str] | None
) -> pd.DataFrame | None:
    """The precision equation's own design: an intercept, and the named covariates.

    ``None`` FOR AN EMPTY SELECTION, WHICH IS A STATEMENT ABOUT BYTES RATHER THAN
    ABOUT MODELS. An intercept-only precision design and no precision design at
    all are the same model -- MEASURED, they reach the same optimum,
    ``llf = 45.33350932122222`` against ``45.33350932122192`` on the published
    food-expenditure table -- but by different optimiser paths, so they are not the
    same bytes. Returning ``None`` puts an empty selection on the library's own
    default path, and ``precision_covariates=[]`` then serialises identically to
    ``precision_covariates=None``.

    THE NAMES ARE CHECKED AGAINST ``x`` AND NOT AGAINST THE ASSEMBLED FRAME, so
    that ``precision_covariates=['const']`` names something the caller supplied
    rather than something this body added. MEASURED: an absent name reaches pandas
    as ``KeyError: "['nope'] not in index"``, which derives from ``LookupError``
    rather than from ``ValueError`` and so is not one of the classes the estimator
    translation recognises -- unrefused, it is a traceback.

    NO RANK RULE HERE, AND THAT IS AN ARGUMENT RATHER THAN AN OMISSION. A
    rank-deficient precision design IS fitted in silence by statsmodels 0.14.6 --
    measured, ``const``, ``income`` and twice ``income`` returns coefficients that
    look like estimates beside standard errors that are all non-finite -- but this
    body cannot build one. The frame below is the intercept plus a SUBSET of the
    columns of a design ``_the_design`` has already proven full rank, and a subset
    of a linearly independent set is linearly independent; the only way to repeat a
    column is to name it twice, which the rule above refuses first.
    """
    names = list(covariates or ())
    if not names:
        return None
    for name in names:
        require_a_column(x, column=name, fn=_FN, arg="precision_covariates")
    precision = design[[_INTERCEPT, *names]]
    require_distinct_column_names(
        precision,
        fn=_FN,
        arg="precision_covariates",
        remedy="Name each precision covariate once.",
    )
    return precision


def _refuse_what_no_estimator_fits(
    *, model: str, on_a_boundary: int, covariates: Sequence[str] | None
) -> None:
    """The three requests this node cannot honour, refused rather than approximated.

    THE FIRST HAS NO IMPLEMENTATION ANYWHERE. ``statsmodels.othermod.betareg`` on
    0.14.6 exports ``BetaModel``, ``BetaResults`` and ``BetaResultsWrapper`` and
    nothing else, so there is no zero-or-one-inflated mixture to call, and no
    primary source for one has been chosen. Card #527's ``validation_notes``
    records the decision: the enum value stays, because the node signature is
    frozen and dropping it is a contract change, and the branch refuses, because a
    plain beta fit returned under this name would be worse than a refusal.

    THE SECOND IS THE ONE THAT WOULD CRASH. Ferrari and Cribari-Neto's
    log-likelihood, their equation (7), is -infinity at ``y = 0`` and at ``y = 1``.
    MEASURED against statsmodels 0.14.6: ``BetaModel`` answers a boundary
    observation with a bare ``AssertionError`` carrying an EMPTY message, raised
    from ``assert np.all((0 < etmp) & (etmp < 1))``. ``AssertionError`` is neither
    a ``ValueError`` nor a class of the library's own, so
    :func:`~econflow_engine.gates.estimation.is_estimator_refusal` cannot see it:
    a body that translated only the estimator's own refusals would hand the caller
    a traceback with no message in it at all.

    THE THIRD WOULD BE IGNORED IN SILENCE. The fractional branch is a Bernoulli
    quasi-likelihood with no precision parameter and no second equation, so a
    precision design there is a request nothing would fit.
    """
    if model == "zero_one_inflated_beta":
        refuse_a_combination(
            fn=_FN,
            combination="model='zero_one_inflated_beta'",
            reason=(
                "statsmodels 0.14.6 carries no zero-or-one-inflated beta mixture: "
                "its othermod.betareg module defines BetaModel, BetaResults and "
                "BetaResultsWrapper and nothing else, and no primary source has "
                "been chosen for one, so there is no estimator behind this name."
            ),
            remedy=(
                "Use model='fractional', whose quasi-likelihood admits a response "
                "at exactly zero or one without a mixture; boundary_share reports "
                "how much of the sample sits there."
            ),
        )
    if model == "beta" and on_a_boundary > 0:
        refuse_a_combination(
            fn=_FN,
            combination=(
                f"model='beta' over a response with {on_a_boundary} "
                f"observation(s) at exactly 0 or 1"
            ),
            reason=(
                "the beta density is undefined at either boundary -- Ferrari and "
                "Cribari-Neto (2004) equation (7) is minus infinity there -- and "
                "statsmodels 0.14.6 answers with a bare AssertionError carrying no "
                "message. Squeezing the data off the boundary is an arbitrary "
                "transformation that changes the estimates, so it is not done here."
            ),
            remedy=(
                "Use model='fractional': the Bernoulli quasi-likelihood of Papke "
                "and Wooldridge (1996) multiplies log G by y and log(1 - G) by "
                "1 - y, so a boundary observation contributes one term and never "
                "the logarithm of zero."
            ),
        )
    if covariates is not None and model != "beta":
        refuse_a_combination(
            fn=_FN,
            combination=f"precision_covariates with model={model!r}",
            reason=(
                "only a beta regression estimates a precision parameter; the "
                "fractional response estimator is a quasi-likelihood with no "
                "second equation to put them in."
            ),
            remedy="Pass model='beta' to fit that equation, or drop precision_covariates.",
        )


def _fit_the_model(
    *,
    model: str,
    link: Any,
    y: pd.Series,
    design: pd.DataFrame,
    precision: pd.DataFrame | None,
) -> Any:
    """Build the estimator this model names and fit it. Refuses, never crashes.

    THE FIT RUNS UNDER numpy's ERROR STATE AND NOT UNDER THE CALLER'S, and all
    four states are relaxed because all four were MEASURED firing inside a fit
    that is behaving normally. Under ``np.seterr(all='raise')`` -- which is how
    this repository's suite runs -- a beta fit over a covariate drawn at a scale of
    1e8 raises ``FloatingPointError: overflow encountered in exp``, and both
    estimators raise ``FloatingPointError: underflow encountered in dot`` over a
    covariate multiplied by 1e100. An underflow in a dot product is the likelihood
    evaluated far out in the tail, where the answer IS zero; numpy's own shipped
    state ignores it, and it is the caller's ``seterr`` rather than the data that
    turns it into an exception.

    WHAT THIS DOES NOT SILENCE. The block encloses the estimator's call and
    nothing else, so none of this engine's own arithmetic is inside it, and a fit
    that reached a degenerate optimum is caught where it belongs -- by the
    convergence and finiteness gates at the call site, on what the estimator
    reported, rather than by whichever intermediate happened to overflow first.
    """
    try:
        with np.errstate(
            divide="ignore", invalid="ignore", over="ignore", under="ignore"
        ):
            if model == "beta":
                return BetaModel(y, design, exog_precision=precision, link=link).fit()
            return GLM(y, design, family=Binomial(link=link)).fit(cov_type=_COVARIANCE)
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error,
            fn=_FN,
            code="precondition-degenerate",
            remedy=(
                "The response and the covariates must describe a model the "
                "likelihood can be maximised for: a share with some variation in "
                "it, and covariates that neither determine the response exactly "
                "nor one another."
            ),
        )


def _the_statistics(fit: Any, *, level: float) -> pd.DataFrame:
    """Every number this body reports about the fit, one row per estimated parameter.

    ASSEMBLED FOR THE WHOLE COEFFICIENT VECTOR AND NOT FOR THE MEAN EQUATION
    ALONE, so that the finiteness rule below sees the precision equation too.

    THE READ IS INSIDE numpy's RELAXED ERROR STATE FOR THE SAME REASON THE FIT IS,
    and this paragraph is a correction of what it first said. Every attribute here
    is computed LAZILY by the estimator on first access, so the arithmetic inside
    this block is statsmodels' and not this engine's. MEASURED under
    ``np.seterr(all='raise')``, which is how this repository's suite runs: a design
    carrying a covariate equal to ``1 + 1e-10 * row`` converges, and reading
    ``bse`` raises ``FloatingPointError: invalid value encountered in sqrt`` from
    ``np.sqrt(np.diag(self.cov_params()))`` at
    ``statsmodels/base/model.py:1431`` -- the library silences the RuntimeWarning
    that line expects and cannot silence a caller's error state. The first version
    of this function had no guard, on a probe that happened to use an input whose
    covariance produced its ``nan`` by a different route; the test written for the
    rule is what found it.

    SO THE NON-FINITE VALUE ARRIVES AS A VALUE, which is what
    :func:`~econflow_engine.gates.estimation.require_finite_estimates` at the call
    site is for. Relaxing the state here does not hide it: it turns a crash into a
    refusal that names the term and the statistic.
    """
    with np.errstate(divide="ignore", invalid="ignore", over="ignore", under="ignore"):
        interval = np.asarray(fit.conf_int(alpha=1.0 - level), dtype=float)
        return pd.DataFrame(
            {
                "estimate": np.asarray(fit.params, dtype=float),
                "std_error": np.asarray(fit.bse, dtype=float),
                "z_value": np.asarray(fit.tvalues, dtype=float),
                "p_value": np.asarray(fit.pvalues, dtype=float),
                "conf_low": interval[:, 0],
                "conf_high": interval[:, 1],
            },
            index=[str(term) for term in fit.params.index],
        )


def _flat(table: pd.DataFrame) -> pd.Series:
    """The table as one labelled vector, for a rule that asks about every number."""
    return pd.Series(
        {
            f"the {statistic} of {term}": float(value)
            for statistic in table.columns
            for term, value in table[statistic].items()
        }
    )


def _the_precision(
    values: np.ndarray, *, model: str, precision: pd.DataFrame | None, width: int
) -> float | dict[str, float] | None:
    """``phi`` where it is one number, and the equation that produces it where it is not.

    THREE ANSWERS, AND THE BRANCH IS THE MODEL RATHER THAN THE ARGUMENT. The
    fractional response estimator fits no precision parameter, so the field is
    empty. A beta regression with a constant precision has exactly one, and
    statsmodels estimates its LOGARITHM -- ``link_precision`` defaults to ``Log``
    -- so the natural-scale value the paper prints is the exponential of the last
    coefficient. A beta regression with a precision design has a precision that
    varies by observation, which is not one number at all: MEASURED, ``persons``
    in the precision equation gives 151.53, 21.90 and 57.61 for the first three
    published households. The field then carries the equation instead, keyed by
    the precision design's own column names and on the log scale it is fitted
    through.

    ``np.exp`` UNDER A RELAXED OVERFLOW **AND UNDERFLOW** STATE, and the second
    half of that was missing until a review found it. MEASURED under
    ``np.seterr(all='raise')``: ``np.exp(-800)`` raises ``FloatingPointError:
    underflow encountered in exp`` with ``over='ignore'`` alone and returns ``0.0``
    with both relaxed. A precision below ``exp(-745)`` is zero to double precision,
    which is a number; raising there would have been a crash rather than a
    refusal. The sibling count-model body relaxes both states around the same
    ``np.exp`` for the same reason.

    THE OVERFLOW HALF, and the reason is the second
    critical the sibling count-model body shipped rather than an input measured
    here. No response was found that drives the log-precision anywhere near the
    709 above which the exponential has no value in double precision -- the
    optimiser reports failure long before, and the convergence gate refuses that --
    but this is arithmetic THIS BODY performs on the fit's output, an infinity
    reaches the wire as ``null``, and ``null`` is exactly what this field carries
    on purpose on the fractional branch. The two must not be indistinguishable, so
    the exponential is taken where it cannot raise and the result is gated.
    """
    if model != "beta":
        return None
    if precision is None:
        with np.errstate(over="ignore", under="ignore"):
            return float(np.exp(values[-1]))
    # KEYED BY THE PRECISION DESIGN'S OWN COLUMN NAMES, VERBATIM. This used to
    # strip the estimator's ``precision-`` prefix, which was wrong twice over and
    # a security review found it: these labels are the CALLER'S column names and
    # never carry that prefix -- the estimator puts it on its OWN index, where
    # ``fit.params.index`` reads ``precision-const``, ``precision-a``,
    # ``precision-precision-a`` for caller columns ``const``, ``a``,
    # ``precision-a``. So the strip was a no-op on the source it was written for
    # and fired only on a name the caller chose. MEASURED: a design carrying
    # ``a`` and ``precision-a`` returned a precision mapping of two keys where
    # three coefficients had been estimated, the stripped name silently replacing
    # the real one -- exactly the defect ``require_distinct_column_names`` exists
    # to prevent, reintroduced after that gate had passed.
    return {
        str(name): float(value)
        for name, value in zip(precision.columns, values[width:], strict=True)
    }


def _the_marginal_effects(
    fit: Any, *, link: Any, names: Sequence[str], estimates: np.ndarray
) -> dict[str, float]:
    """The average effect of each covariate on the PROPORTION, not on the link scale.

    THE AVERAGE MARGINAL EFFECT, and the average is over the sample rather than at
    its mean. ``dE(y|x)/dx_j`` is ``g'(x_t'beta) * beta_j`` with ``g'`` the
    derivative of the link's inverse, so the reported effect is the sample mean of
    that derivative times the coefficient.

    ONE ARITHMETIC FOR BOTH BRANCHES, AND THE SEAM IS ASSERTED RATHER THAN
    ASSUMED. ``BetaResults`` has no ``get_margeff`` on statsmodels 0.14.6 --
    ``hasattr`` is False -- so the beta branch's effects have to be computed here.
    The fractional branch's results object DOES have one, and
    ``tests/wrappers/c16_limited_dependent/test_fractional_beta.py`` asserts that
    this expression reproduces ``get_margeff(at='overall', method='dydx')`` on all
    four links, so what is computed where the library offers nothing is what the
    library computes where it does.

    THE INTERCEPT IS EXCLUDED, because a derivative with respect to a column of
    ones is not a quantity -- which is also what ``get_margeff`` does with it.

    THE READ IS INSIDE numpy's RELAXED ERROR STATE FOR THE REASON
    :func:`_the_statistics` gives, and this function was missing the guard until a
    security review found it. ``fittedvalues`` is computed LAZILY, so the
    arithmetic is the estimator's and it runs at the point of access, under the
    caller's error state. MEASURED under ``np.seterr(all='raise')``, which is how
    this repository's suite runs: a perfectly separated response on the fractional
    branch under ``cloglog`` or ``loglog`` raises ``FloatingPointError: underflow
    encountered in exp`` out of ``links.py``'s ``1 - np.exp(-np.exp(z))``, and
    ``FloatingPointError`` is not a ``GateError``, so it left this node as a CRASH
    through the gateway rather than as a refusal. An underflow in ``exp`` is the
    inverse link evaluated far out in the tail, where the answer IS zero; a
    non-finite slope is caught by the finiteness rule at the call site instead.
    """
    with np.errstate(divide="ignore", invalid="ignore", over="ignore", under="ignore"):
        mean = np.asarray(fit.fittedvalues, dtype=float)
        slope = float(np.mean(1.0 / np.asarray(link.deriv(mean), dtype=float)))
    return {
        str(name): slope * float(value)
        for name, value in zip(names, estimates, strict=True)
        if name != _INTERCEPT
    }


def ld_fractional_response(
    *,
    y: pd.Series,
    x: pd.DataFrame,
    model: Literal["fractional", "beta", "zero_one_inflated_beta"] | None = None,
    link: Literal["logit", "probit", "cloglog", "loglog"] | None = None,
    precision_covariates: Sequence[str] | None = None,
    conf_level: float | None = None,
) -> dict[str, Any]:
    """Node ``ld_fractional_response`` -- method card #527.

    Fractional response and beta regression.

    Category 16-limited-dependent; memory class ``light``.

    Registers its result under ``fit``, so a later node can consume it as a handle.

    Args:
        y: [series_handle, required] Bounded outcome.
        x: [df_handle, required] Covariate table.
        model: [enum, optional] Model. Default ``'fractional'``.
        link: [enum, optional] Link function. Default ``'logit'``.
        precision_covariates: [series_codes, optional] Covariates modelling the precision parameter.
        conf_level: [number, optional] Confidence level for intervals. Default ``0.95``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - model='zero_one_inflated_beta' must refuse with a GateError until a source is chosen: no
          zero-or-one-inflated beta mixture exists in statsmodels 0.14.6, whose
          statsmodels.othermod.betareg defines only BetaModel, BetaResults and BetaResultsWrapper,
          and no primary source for the mixture has been selected
        - the enum value stays because the node signature is frozen; dropping it is a contract
          change and an owner decision, and a branch quietly returning a plain beta fit under this
          name would be worse than a refusal

    .. gen_wrappers: end of generated docstring

    Examples:
        Ferrari and Cribari-Neto's food-expenditure application: 38 households, the
        share of income spent on food against income and household size, with a
        logit link. Their Table 2 prints the three coefficients as -0.62255,
        -0.01230 and 0.11846, and rounding this fit to the five decimals the page
        carries reproduces all three::

            >>> import pandas as pd
            >>> food = pd.Series([
            ...     15.998, 16.652, 21.741, 7.431, 10.481, 13.548, 23.256, 17.976,
            ...     14.161, 8.825, 14.184, 19.604, 13.728, 21.141, 17.446, 9.629,
            ...     14.005, 9.16, 18.831, 7.641, 13.882, 9.67, 21.604, 10.866,
            ...     28.98, 10.882, 18.561, 11.629, 18.067, 14.539, 19.192, 25.918,
            ...     28.833, 15.869, 14.91, 9.55, 23.066, 14.751])
            >>> income = pd.Series([
            ...     62.476, 82.304, 74.679, 39.151, 64.724, 36.786, 83.052, 86.935,
            ...     88.233, 38.695, 73.831, 77.122, 45.519, 82.251, 59.862, 26.563,
            ...     61.818, 29.682, 50.825, 71.062, 41.99, 37.324, 86.352, 45.506,
            ...     69.929, 61.041, 82.469, 44.208, 49.467, 25.905, 79.178, 75.811,
            ...     82.718, 48.311, 42.494, 40.573, 44.872, 27.167])
            >>> persons = pd.Series([
            ...     1, 5, 3, 3, 5, 3, 4, 1, 2, 2, 7, 3, 2, 2, 3, 3, 2, 1, 5, 4, 4,
            ...     3, 5, 2, 6, 2, 1, 2, 5, 5, 5, 3, 6, 4, 5, 4, 6, 7])
            >>> covariates = pd.DataFrame({"income": income, "persons": persons})
            >>> fit = ld_fractional_response(
            ...     y=food / income, x=covariates, model="beta"
            ... )
            >>> [round(fit["params"][term]["estimate"], 5)
            ...  for term in ("const", "income", "persons")]
            [-0.62255, -0.0123, 0.11846]

        The precision parameter is on its natural scale, which is the scale the
        paper prints it on. The comparison against the published 35.60975 is made
        by the oracle case under ``tests/oracle/c16_limited_dependent/``, and this
        is the number it compares::

            >>> round(fit["precision"], 5)
            35.60973

        No household in that table spends nothing or everything on food, which is
        what made a beta regression admissible for it::

            >>> fit["boundary_share"]
            0.0

        A coefficient is on the link scale; the effect on the share itself is the
        marginal effect, and the intercept has none::

            >>> round(fit["marginal_effects"]["persons"], 6)
            0.023889
            >>> sorted(fit["marginal_effects"])
            ['income', 'persons']

        Move one household onto each boundary and the beta likelihood no longer
        exists, so the fit is refused rather than squeezed::

            >>> boundary = food / income
            >>> boundary.iloc[0], boundary.iloc[-1] = 0.0, 1.0
            >>> ld_fractional_response(y=boundary, x=covariates, model="beta")
            Traceback (most recent call last):
            econflow_engine.errors.GateError: ld_fractional_response: model='beta' over...

        The default model admits them, which is the whole reason the node offers
        two::

            >>> quasi = ld_fractional_response(y=boundary, x=covariates)
            >>> round(quasi["boundary_share"], 6)
            0.052632

    Note:
        FUNCTIONS USED. statsmodels 0.14.6 (BSD-3-Clause), one estimator per
        ``model``: ``othermod.betareg.BetaModel`` fitted with ``.fit()`` at the
        library's own optimiser and iteration limit for ``beta``, and
        ``genmod.generalized_linear_model.GLM`` with a ``Binomial`` family fitted
        with ``.fit(cov_type="HC0")`` for ``fractional`` -- the Bernoulli
        quasi-MLE of Papke and Wooldridge (1996),
        doi:10.1002/(SICI)1099-1255(199611)11:6<619::AID-JAE418>3.0.CO;2-1, which
        is an ordinary binomial likelihood evaluated at a non-binary response. The
        four links are ``genmod.families.links``' ``Logit``, ``Probit``,
        ``CLogLog`` and ``LogLog``, and both estimators accept all four.
        ``pandas`` 2.3.3 assembles the two designs and the statistics table,
        ``numpy`` 2.5.2 reads the coefficient vector, exponentiates the
        log-precision and averages the inverse link's derivative. The estimator
        supplies the coefficients, their standard errors, z statistics, p-values
        and confidence intervals; ``marginal_effects``, ``precision`` on its
        natural scale and ``boundary_share`` are arithmetic over that fit and over
        the response, not second estimates.

        WHAT EACH ARGUMENT MEANS HERE. ``model='fractional'`` is the
        cross-sectional Bernoulli QMLE, consistent under a correctly specified
        conditional mean whatever the true variance -- which is why ``HC0`` is
        pinned rather than defaulted, and Papke and Wooldridge (2008),
        doi:10.1016/j.jeconom.2008.05.009, section 3 is where the requirement is
        stated: "In applying the Bernoulli QMLE, one needs to adjust the standard
        errors." ``model='beta'`` is Ferrari and Cribari-Neto (2004),
        doi:10.1080/0266476042000214501, in their ``(mu, phi)`` parameterisation,
        their equation (4). ``link`` is the mean equation's link on both branches;
        the precision equation's own link is the library's ``Log`` and this node
        does not expose it. ``precision_covariates`` names columns of ``x`` and
        selects the precision design, to which this body prepends its own
        intercept. The intercept is added here on both equations and named
        ``const``.

        WHAT THIS ENGINE DOES NOT COMPUTE, AND WHY. ``model='zero_one_inflated_beta'``
        IS REFUSED ON EVERY INPUT. There is no zero-or-one-inflated beta mixture
        anywhere in statsmodels 0.14.6 -- ``othermod.betareg`` exports
        ``BetaModel``, ``BetaResults`` and ``BetaResultsWrapper`` and nothing else
        -- and no primary source for the mixture has been chosen, so writing one
        here would be an estimator invented under a published name. The enum value
        stays because the node signature is frozen and removing it is a contract
        change; the refusal names ``fractional``, which is what carries a boundary
        mass in the meantime. This is a defect in the card, recorded there in
        ``validation_notes`` and here rather than papered over.

        THE STANDARD ERRORS ARE THE OBSERVED-INFORMATION ONES ON THE BETA BRANCH,
        and they are NOT the ones Ferrari and Cribari-Neto print. Their Table 2
        gives 0.22385, 0.00304 and 0.03534, computed from the EXPECTED information
        matrix -- the closed-form ``W`` following their equation (9).
        ``BetaResults`` is a ``GenericLikelihoodModel`` and its ``bse`` inverts the
        OBSERVED numerical Hessian: MEASURED, 0.22137, 0.00308 and 0.03574 on the
        same data. Two estimators of one quantity, disagreeing by about 1.1e-02
        relative at worst. Reproducing the published pair means implementing the
        expected information in this engine and reporting it in place of the value
        the library gives, which is a larger change than this method; the oracle
        case claims none of them and says so, and the disagreement is pinned by a
        test so that a release moving it is visible.

        DELIBERATELY OMITTED. The pseudo R-squared: the paper prints 0.3878 for
        this fit, ``BetaResults.prsquared`` returns 0.4088, and the two definitions
        were not reconciled, so neither is reported. A standard error or an
        interval for a marginal effect: the fractional branch's results object
        offers one and the beta branch has none at all, and reporting inference on
        one branch only would be worse than reporting none. The response on a known
        interval ``(a, b)``, which Ferrari and Cribari-Neto handle by modelling
        ``(y - a) / (b - a)``: the contract's response is a proportion. HC1 and HC3:
        no argument of this node reaches ``cov_type``. A chart: card #527 declares
        ``chart_kind: table`` and this payload carries no frame to build one from,
        the coefficients being a mapping keyed by term, so ``chart_spec`` is not
        called -- the same mismatch between a declared kind and an emitter branch
        that the sibling count-model body records against its own frame.

        GATES ADDED, AND THE SOURCE OF EACH. THE FIRST IS THE ONE THAT DECIDES THIS
        BODY'S SHAPE, and it is a crash rather than a silence: ``BetaModel`` handed
        a response at exactly 0 or exactly 1, outside [0, 1], or carrying a ``nan``
        raises a bare ``AssertionError`` WITH AN EMPTY MESSAGE from ``assert
        np.all((0 < etmp) & (etmp < 1))``. That class is defined in ``builtins``
        and derives from neither ``ValueError`` nor anything of the library's, so
        nothing translates it and the caller receives a traceback with no text in
        it. THE REST ARE SILENT ACCEPTANCES, every one measured on the 38 published
        households. The fractional branch fits a response OUTSIDE the unit interval
        without a word -- the shares with the first replaced by 1.4 return
        ``llf = -17.215557434559905``, and with -0.3, ``llf = -15.03350281799101``,
        neither raising nor warning under ``warnings.simplefilter('always')`` --
        which is how a share reported in percent is estimated as though it were a
        share. A constant response is fitted by both: the beta branch returns
        ``llf = 606.98046875`` with the precision running away, the fractional
        branch ``llf = -15.461508215318748``. A collinear design is fitted by
        ``BetaModel`` in silence and returns ``llf = 45.333509321237926`` against
        the identified fit's ``45.33350932122192`` -- the same number to eleven
        digits, beside a coefficient no data identifies -- and a rank-deficient
        PRECISION design is fitted the same way with every standard error
        non-finite. Two columns sharing a name are fitted and one of the two
        coefficients disappears from any mapping keyed by name. An argument whose
        index is not the response's is read row by row as given. A confidence level
        of exactly 1 is an interval of ``-inf`` to ``inf``, which the inclusive
        range primitive admits. An unknown precision covariate reaches pandas as a
        ``KeyError``, which is a traceback rather than a refusal.

        TWO GATES ASK ABOUT THE FIT'S OUTPUT RATHER THAN ITS INPUTS, which is the
        half the sibling count-model body first lacked and had to have added by
        review. MEASURED: ``income`` multiplied by 1e6 -- nothing but a change of
        units -- leaves the beta optimiser reporting ``converged`` false with a
        coefficient vector shaped exactly like an estimate. The second is narrower
        and worse, and finding an input that reaches it took the search the rule
        deserves: every rescaling large enough to break the covariance is ALSO
        rank-deficient to ``np.linalg.matrix_rank``, so the rank rule refuses it
        first and the finiteness rule never fires. A fourth covariate equal to
        ``1 + 1e-10 * row`` is what gets past both -- the intercept in all but the
        tenth decimal, rank 4 of 4 -- and the fractional branch then reports
        ``converged`` TRUE, finite coefficients, standard errors that are not
        numbers, AND NO WARNING AT ALL. At 1e-6 the same column is harmless and at
        1e-14 the rank rule catches it, which is how narrow the band between the
        two rules is. Serialised there is no ``NaN`` token, so the payload would be
        well-formed JSON whose inference is simply absent -- and ``precision`` is
        null ON PURPOSE on the fractional branch, so a caller could not tell the
        two apart. The finiteness rule is therefore asked of every number the fit
        reports, before the payload is assembled, and again of the two numbers this
        body derives from it.

        NO ARGUMENT OF THIS NODE REACHES AN EVALUATOR, and that is checked rather
        than assumed, because the first 2.2 body shipped a remote code execution
        through an argument of kind ``string`` spliced into a formula. There is no
        formula here and no query: ``y`` and ``x`` arrive as pandas objects and are
        passed to constructors that take arrays; ``model`` and ``link`` are enums
        the wire model has already checked against the contract's own lists and are
        used as mapping keys, never interpolated; ``conf_level`` is a number that
        reaches ``conf_int(alpha=...)``. ``precision_covariates`` is kind
        ``series_codes``, which ``kinds.py`` types as ``list[str]`` with NO
        constraint on the contents, and it is the one argument carrying
        caller-chosen text onward -- into a pandas COLUMN SELECTION,
        ``design[[...]]``, which is a hash lookup and not an expression.
        ``require_a_bare_name`` is therefore NOT applied to it: it would narrow the
        contract, since a column may legitimately be called ``age 45-54``, and it
        would guard a path that evaluates nothing. ``require_a_column`` is applied
        instead, so an unknown name is a refusal rather than the ``KeyError``
        pandas would raise, and a test feeds the injection payload in as a column
        name and asserts in a ``finally`` that no side effect occurred.
    """
    chosen_model = str(model if model is not None else _declared("model"))
    chosen_link = str(link if link is not None else _declared("link"))
    level = float(conf_level if conf_level is not None else _declared("conf_level"))

    require_strictly_inside(level, low=0.0, high=1.0, fn=_FN, arg="conf_level")
    # THE LENGTH RULE IS ASKED BEFORE ANY QUESTION ABOUT THE RESPONSE'S CONTENT,
    # because a sample shorter than its own parameter count is also a sample with
    # no variance and no rank, and "variance is undefined below 2" is the wrong
    # account of three rows against five parameters. BOTH EQUATIONS ARE COUNTED: a
    # beta regression estimates a precision equation beside the mean.
    width = len(x.columns) + 1
    estimated = width + (
        1 + len(precision_covariates or ()) if chosen_model == "beta" else 0
    )
    require_min_length(y, minimum=estimated + 1, fn=_FN, arg="y")
    require_within_bounds(
        y,
        low=0.0,
        high=1.0,
        fn=_FN,
        arg="y",
        remedy=(
            "This method's response is a proportion. If it is a percentage, divide "
            "it by 100; if it is a count of successes out of a known total, card "
            "#527 points at a binomial model instead."
        ),
    )
    require_variance(y, fn=_FN, arg="y")
    # EXACT EQUALITY AND NOT A TOLERANCE. This field exists to tell a reader
    # whether a beta regression was legitimate at all, and a share that is nearly
    # zero is not a share that is zero.
    response = np.asarray(y, dtype=float)
    on_a_boundary = (response == 0.0) | (response == 1.0)
    share = float(on_a_boundary.mean())
    _refuse_what_no_estimator_fits(
        model=chosen_model,
        on_a_boundary=int(on_a_boundary.sum()),
        covariates=precision_covariates,
    )
    design = _the_design(y, x)
    precision_design = (
        _the_precision_design(design, x=x, covariates=precision_covariates)
        if chosen_model == "beta"
        else None
    )
    link_object = _LINKS[chosen_link]()
    fit = _fit_the_model(
        model=chosen_model,
        link=link_object,
        y=y,
        design=design,
        precision=precision_design,
    )
    require_convergence(
        converged=bool(
            fit.mle_retvals["converged"] if chosen_model == "beta" else fit.converged
        ),
        fn=_FN,
        estimator="maximum-likelihood" if chosen_model == "beta" else "reweighted least-squares",
        remedy=(
            "A share model that does not converge is usually a covariate on a very "
            "different scale from the others, or a response the covariates predict "
            "exactly: rescale the first, and check the second against "
            "boundary_share."
        ),
    )
    table = _the_statistics(fit, level=level)
    # THE CONVERGENCE FLAG IS NOT A STATEMENT THAT THE NUMBERS ARE NUMBERS.
    # MEASURED, on the input the gates above let through: a fourth covariate equal
    # to `1 + 1e-10 * row` -- the intercept in all but the tenth decimal, and full
    # rank to `np.linalg.matrix_rank` -- converges with finite coefficients,
    # standard errors that are not numbers, and NO WARNING AT ALL.
    # ASKED OF THE FIT'S OWN TABLE AND NOT OF THE ASSEMBLED PAYLOAD, because
    # `precision` is null ON PURPOSE on the fractional branch and a finiteness
    # rule over the whole mapping would refuse a quasi-likelihood for estimating
    # no precision.
    require_finite_estimates(
        _flat(table),
        fn=_FN,
        quantity="estimates and their inference",
        remedy=(
            "The iteration reported success and the numbers it stopped at are not "
            "numbers, which is a covariate whose units the linear predictor cannot "
            "hold: dividing a covariate by 1000 multiplies its coefficient by 1000 "
            "and leaves the fit untouched. Rescale it."
        ),
    )
    estimates = np.asarray(table["estimate"], dtype=float)
    names = [str(name) for name in design.columns]
    result: dict[str, Any] = {
        "params": {
            term: {str(statistic): float(value) for statistic, value in row.items()}
            for term, row in table.iloc[:width].iterrows()
        },
        "marginal_effects": _the_marginal_effects(
            fit, link=link_object, names=names, estimates=estimates[:width]
        ),
        "precision": _the_precision(
            estimates, model=chosen_model, precision=precision_design, width=width
        ),
        "boundary_share": share,
    }
    # THE SECOND HALF OF THE SAME RULE, OVER THE NUMBERS THIS BODY DERIVED rather
    # than the ones the fit reported: the exponential of the log-precision, and the
    # average marginal effects. Both are arithmetic on the fit's output, and both
    # reach the wire as `null` if they have no representable value.
    #
    # EVERY LABEL SAYS WHICH QUANTITY IT IS, for the reason `_flat` builds its
    # labels the same way, and this loop did not until a review found it. Both
    # mappings are keyed by COVARIATE NAME -- `marginal_effects` by the columns of
    # `x`, `precision` by the intercept plus a SUBSET of those same columns -- so a
    # plain `update` had every precision covariate overwrite its own marginal
    # effect before the rule could read it. MEASURED, one covariate in both
    # equations: the rule saw `{'persons': -0.467, 'const': 5.182}` and checked NO
    # marginal effect at all, which is the silent null this gate exists to refuse.
    derived = {f"the marginal effect of {term}": value
               for term, value in result["marginal_effects"].items()}
    if isinstance(result["precision"], float):
        derived["the precision"] = result["precision"]
    elif isinstance(result["precision"], dict):
        derived.update(
            {f"the precision coefficient on {term}": value
             for term, value in result["precision"].items()}
        )
    require_finite_estimates(
        pd.Series(derived),
        fn=_FN,
        quantity="marginal effects and precision",
        remedy=(
            "These are this method's own arithmetic over a fit that converged: an "
            "average derivative and, for a beta regression, the exponential of the "
            "fitted log-precision, which has no value in double precision above "
            "about 709. Rescale the covariates and refit."
        ),
    )
    return result
