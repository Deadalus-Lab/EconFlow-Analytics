# SPDX-License-Identifier: AGPL-3.0-only
"""The refusals a body that wraps a FITTED ESTIMATOR needs, and no others.

WHY THIS MODULE EXISTS RATHER THAN FIVE ``raise`` STATEMENTS IN ONE WRAPPER.
``tests/test_gate_discipline.py`` permits exactly two ``raise`` forms anywhere
under ``wrappers/**``: the emitted ``NotImplementedError`` and a bare re-raise
inside an ``except``. A refusal is a CALL, and the call has to land somewhere a
refusal may be written -- which is this package. The eight registry primitives in
:mod:`~econflow_engine.gates.primitives` answer questions about a numeric VECTOR;
none of them answers a question about an estimator's own contract, and the first
wrapper body written in phase 2.2 needed six such questions asked and one
library refusal translated.

WHY THE SECOND BODY ADDED SEVEN MORE, AND WHY THEY ARE NOT REGISTRY PRIMITIVES
EITHER. :data:`~econflow_engine.gates.registry.PRIMITIVES` is keyed by DETAIL
CODE and ``tests/test_gates_registry.py`` asserts that mapping is total in both
directions, so a ninth primitive would need a ninth detail code -- and the code
vocabulary is shared with ``corpus/_vocabulary.json`` and the method-card schema
enum, which a wrapper body must not move. Every refusal below therefore reuses
one of the ten codes already declared, exactly as the first six do. Four of the
seven ask about the caller's DATA rather than about the call, which is a wider
brief than this module opened with: a count that is not whole, an exposure that
is not positive, a design naming one column twice, and three arguments indexed
by different labels are all facts about what arrived, and all four were measured
being accepted in silence by statsmodels 0.14.6.

THE SEVENTH ASKS ABOUT NEITHER, AND IT IS THE ONE A REVIEW HAD TO FIND.
:func:`require_finite_estimates` asks about the fit's OUTPUT. Every other rule
here is asked before the estimator runs, so a body could gate its inputs
fourteen times over and still return a payload of nulls from a fit that
converged on ``nan`` -- which is what the second 2.2 body did until this
landed.

THE THIRD BODY ADDED ONE, AND IT IS THE THIRD CORNER OF A SET THAT NEEDED ALL
THREE. :func:`require_within_bounds` is the CLOSED interval over a VECTOR:
:func:`~econflow_engine.gates.primitives.require_in_range` is closed and takes one
number, :func:`require_strictly_inside` takes a vector and is open, and a response
that is a PROPORTION is the case neither answers -- every observation in ``[0, 1]``
with both endpoints admissible data. It carries the same detail code as its two
siblings and no new one.

THE EIGHTEENTH REPLACES A QUESTION THAT WAS BEING PUT TO THE WRONG WITNESS.
:func:`require_no_separation` asks whether the caller's DESIGN admits a maximum
likelihood estimate at all, which is what :func:`require_convergence` was being
read as answering. It cannot: the flag reports where an iteration stopped, and
under separation an IWLS stalls on a floating-point plateau rather than
diverging, so which way the flag lands is decided by the last bit of the linear
algebra. This is the first rule here whose arithmetic is this module's own -- a
linear programme, not a comparison -- which is why the body that calls it keeps
it OUTSIDE the ``try`` that translates the estimator's exceptions. It too carries
``precondition-degenerate`` and no new code.

THE NINETEENTH IS THE FIRST ABOUT AN ARGUMENT'S VOCABULARY, AND IT EXISTS BECAUSE
AN ANNOTATION WAS MISTAKEN FOR A GUARD. :func:`require_a_declared_option` refuses a
value outside the set an ``enum`` argument declares. The wire model already does
this, so the question is only ever asked of a DIRECT Python call -- and the body
that needed it carried a docstring claiming beartype answered it there. beartype
is a dev dependency installed by ``tests/conftest.py``, so the check existed under
pytest and nowhere else, which is exactly the arrangement in which no test can see
the hole. MEASURED with the hook absent, ``run_roc`` took ``direction='X'``,
inverted the area to 0.0 where ``'<'`` returns 1.0, and reported ``'X'`` back.

TWO OF THE FIRST SIX ARE A SECURITY BOUNDARY AND ARE NOT INTERCHANGEABLE WITH THE
REST.
:func:`require_a_bare_name` and :func:`require_an_allowlisted_specification` guard
the one place a body turns caller input into a string that is EVALUATED. They
were added after a live injection through ``fixef``, and each carries the
measurement that proves what it blocks.

WHAT IS DELIBERATELY NOT HERE. No new detail code: every refusal below carries
one of the ten :data:`~econflow_engine.gates.codes.GATE_DETAIL_CODES` already
declared, so ``PRIMITIVES``, ``corpus/_vocabulary.json`` and the method-card
schema enum do not move. These functions are NOT registry primitives and are not
declarable on a card: a card's ``precondition_gates`` names a rule about the
CALLER'S DATA that a reviewer of the card can judge, and four of the five below
are about the call itself. :mod:`~econflow_engine.gates.cross_section` and
:mod:`~econflow_engine.gates.sliding_window` are already in that position.

THE FIFTH IS THE ONE THAT MATTERS MOST AND IS THE LEAST OBVIOUS.
:func:`refuse_estimator_failure` translates the estimator's own exception into a
``GateError``. Without it a documented precondition -- a dependent variable that
is not binary, a formula naming a column the frame does not carry -- reaches the
caller as a traceback, because ``mcp/make_tool.py`` turns a ``GateError`` into a
clean refusal and lets every other exception escape as a crash.
"""

from __future__ import annotations

import keyword
from typing import NoReturn

import numpy as np
import pandas as pd
from scipy.optimize import linprog

from econflow_engine.errors import GateError
from econflow_engine.formula import validate_formula
from econflow_engine.gates.codes import GateDetailCode, refusal
from econflow_engine.gates.primitives import require_no_missing

__all__ = [
    "is_estimator_refusal",
    "refuse_a_combination",
    "refuse_a_multi_model_fit",
    "refuse_estimator_failure",
    "require_a_bare_name",
    "require_a_column",
    "require_a_declared_option",
    "require_an_aligned_index",
    "require_an_allowlisted_specification",
    "require_an_observed_value",
    "require_at_most_one_spelling",
    "require_convergence",
    "require_counts",
    "require_distinct_column_names",
    "require_finite_estimates",
    "require_no_separation",
    "require_strictly_inside",
    "require_supplied",
    "require_within_bounds",
]

#: The packages whose exceptions are the ESTIMATOR objecting rather than a defect
#: in a wrapper. Adding one is a statement that this engine reads that package's
#: errors as refusals; :func:`is_estimator_refusal` records what was measured.
_ESTIMATOR_PACKAGES: frozenset[str] = frozenset({"formulaic", "pyfixest", "statsmodels"})

#: The margin above which :func:`require_no_separation` reads the programme as
#: having found a separating direction, relative to the largest row norm of the
#: oriented design. IT IS A GUARD AGAINST A SOLVER RESIDUAL AND NOT A DIAL: the
#: two populations do not overlap anywhere near it. MEASURED over 2657 random
#: binary designs whose estimate exists (20 to 200 rows, 1 to 6 covariates,
#: column scales spanning 1e-3 to 1e3, outcomes drawn from a logit), the largest
#: margin HiGHS returned was 0.0 EXACTLY. MEASURED at the other edge, a design
#: separated by two rows in 1380 scores 2.439024e-02, and squeezing the
#: separating gap down to 1e-10 leaves the margin at 8.720930e-02 rather than
#: driving it toward zero -- the programme simply scales the direction back out
#: to its own box.
#:
#: THAT SAMPLE WAS STRUCTURALLY BLIND AND THE SENTENCE IT SUPPORTED WAS FALSE.
#: It read "the nearest measured neighbour is six orders of magnitude above this
#: value on one side and exactly zero on the other", and the reason no neighbour
#: was nearer is that every design in it was WELL CONDITIONED: no near-collinear
#: pair, no zero column, no scale disparity beyond 1e3. Those are precisely the
#: regimes in which HiGHS returns a point that violates its own constraints, and
#: the objective attached to such a point lands squarely in the band this constant
#: was said to have to itself. MEASURED over the excluded regimes, 600 designs per
#: band, outcome drawn independently of the design so that nothing but luck
#: separates it -- near-collinear pairs ``x2 = x1 + N(0, eps)`` scoring a margin
#: above this value: eps 1e-12 to 1e-10, 0 of 600; eps 1e-9, 1 of 600, largest
#: margin 1.229480e-08; eps 1e-8, 401 of 600, largest margin 1.138867e-07; eps
#: 1e-7 to 1e-2, 0 of 600. Inside that band a false refusal was the MAJORITY
#: outcome, and every one of the 402 carried a witness violating the programme's
#: own constraints. The band is narrow because it is the band in which the
#: near-collinearity is large enough to unsettle HiGHS and still small enough that
#: its presolve does not simply drop the column. The guard that answers those 402
#: is :data:`_SEPARATION_WITNESS_FEASIBILITY` and not this number.
#:
#: WHAT THIS CONSTANT FACES ONCE THE WITNESS IS VERIFIED, RE-MEASURED OVER THE
#: REGIMES THE OLD SAMPLE EXCLUDED. Two labelled populations, the verdict taken
#: from the fixed gate. Separated by construction, 3000 designs of 20 to 200 rows
#: and 1 to 6 covariates at scales 1e-3 to 1e3: 2999 refused, smallest refused
#: margin 3.174675e-05. Outcome independent of the design, 12500 designs over the
#: whole near-collinear band, all-zero and near-zero columns at 0, 1e-320, 1e-300,
#: 1e-150 and 1e-30, and scale disparities of 1e3 to 1e15: ZERO refusals, and no
#: margin above this value anywhere in them. So the nearest measured neighbour
#: above is 3.174675e-05 -- three and a half orders up, and a genuine separation
#: -- while below it the non-separated population produces nothing this value has
#: to reject. IT IS DEFENSIBLE, and it is defensible only in that order: the
#: feasibility check does the work this number was wrongly credited with.
#:
#: RELATIVE TO THE LARGEST ROW NORM AND NOT TO THEIR SUM. MEASURED on the same
#: two-row separated level, over the O-RING covariates, whose row norms sum to
#: 9738 and whose largest is 82: against the sum it scores 2.053810e-04 inside
#: 138 rows and 2.053810e-05 inside 1380, so any fixed threshold on that ratio
#: refuses the short frame and admits the long one; against the largest row norm
#: it scores 2.439024e-02 in both. THE FRAME IS NAMED BECAUSE THE PAIRED TEST IN
#: tests/test_gates_estimation.py USES A DIFFERENT ONE -- 60 + row % 25, largest
#: row norm 85 -- and therefore reports 2.352941e-02 and 2.000800e-04 /
#: 1.986295e-05 for the same experiment. Two frames, one conclusion; neither set
#: of digits is a correction of the other.
_SEPARATION_MARGIN = 1e-8

#: How far below zero a row of ``oriented @ x`` may fall before
#: :func:`require_no_separation` stops believing the objective attached to ``x``,
#: relative to the same largest row norm the margin is taken against.
#:
#: EVERY FIGURE BELOW IS A PROPERTY OF ONE SOLVER BUILD, WHICH IS scipy 1.18.0's
#: BUNDLED HiGHS, and it is named here because the rest of this module pins the
#: version of every library it quotes and this constant is derived wholly from
#: that one.
#:
#: WHY A SOLVED PROGRAMME NEEDS ITS ANSWER CHECKED AT ALL. HiGHS's default primal
#: feasibility tolerance is 1e-7, so ``success`` True and ``status`` 0 mean it
#: stopped satisfied and NOT that the point it returns satisfies the constraints
#: this module wrote. MEASURED on 120 rows carrying ``b = a + N(0, 1e-9)``, seed
#: 159: ``success`` True, ``status`` 0, ``x`` [0, -1, 1], and yet
#: ``(oriented @ x).min()`` is -3.778144463950639e-09 on 46 of the 120 rows -- a
#: RELATIVE violation of -6.866427e-10 against that design's largest row norm of
#: 5.5023444189556105, which is the quantity the comparison below actually makes
#: -- with an objective of -5.588978524428967e-08 that divides out to a margin of
#: 1.0157449441323413e-08, above :data:`_SEPARATION_MARGIN`, so the design was
#: refused. It does not separate: 65 zeros and 55 ones, controls spanning ``a`` in
#: [-2.251, 2.245] against cases in [-1.860, 1.795], and pyfixest 0.60.0 fits it
#: at Intercept -0.138 and ``a`` 0.397 after dropping ``b`` for multicollinearity.
#: ``method="highs-ds"`` and ``method="highs-ipm"`` return the same infeasible
#: point, so it is not the simplex arm's alone.
#:
#: EVERY VIOLATION QUOTED BELOW IS RELATIVE TO THAT SAME LARGEST ROW NORM, in the
#: unit the comparison uses, and the paragraph above is the only place an absolute
#: one appears -- named as such because it is what a reader reproduces first.
#:
#: WHY A CHECK ON THE WITNESS IS EXACT WHERE A THRESHOLD ON THE OBJECTIVE IS NOT.
#: ``b = 0`` is always feasible with objective 0, so the programme's optimum is
#: never negative and a POSITIVE objective at a FEASIBLE point is Silvapulle's
#: (1981) condition met constructively -- that point IS a separating direction.
#: At an infeasible point the objective bounds nothing, in either direction. So
#: the refusal below is only ever made while holding a witness, which is what its
#: message claims to have.
#:
#: THE VALUE, AND THE ONE CASE IT COSTS. MEASURED over 3499 designs whose answer
#: is honest -- 1499 well-conditioned and 2000 separated by construction -- the
#: worst relative violation was -1.012873e-16, and over the 2000 separated ones
#: not a single witness fell below -1e-14. MEASURED over 12500 designs whose
#: outcome was drawn independently of the design, spanning the whole near-collinear
#: band, all-zero and near-zero columns and scale disparities to 1e15: the shipped
#: gate falsely refused 381 of them, and among those 381 the violation CLOSEST TO
#: ZERO was -5.923896e-10 and the worst -1.518403e-08. This value sits four orders
#: above the worst honest residual and nearly three below the mildest leakage, so
#: neither edge is close. IT IS NOT A PERFECT SEPARATOR AND THE EXCEPTION IS
#: RECORDED RATHER THAN ROUNDED AWAY: over 3000 designs separated by construction,
#: ONE -- 165 rows, 4 columns, margin 1.118970e-01 -- came back with a violation of
#: -2.769367e-08, inside the leakage band, and is therefore admitted rather than
#: refused. NO threshold separates the two populations, because that one design's
#: violation is worse than the leakage's mildest; the choice is which error to
#: make, not whether to make one. Losing it costs a REFUSAL this module already
#: declines to make in two other named cases (see
#: :func:`require_no_separation`'s two gaps); admitting the 381 costs a FALSE
#: STATEMENT about the caller's data. Re-solving it at a tightened
#: ``primal_feasibility_tolerance`` was measured and NOT taken: 1e-9 and 1e-10
#: recover it, 1e-11 and below do not, because HiGHS rejects them with
#: ``OptimizeWarning: Invalid option value`` and silently keeps its own -- so the
#: recovery rests on an undocumented clamp two orders wide, and buying 1 case in
#: 3000 with that is a worse trade than naming it here.
#:
#: THE GAP IS PINNED BY A TEST AND NOT ONLY BY THIS PARAGRAPH. Naming a cost in
#: prose leaves nothing to notice when the cost changes, and the design behind the
#: figures above was never committed, so neither edge of the band could be
#: re-measured. ``tests/test_gates_estimation.py`` now carries an eight-row design
#: -- swept for, then reduced row by row while the verdict held -- that separates
#: under the direction (0, 0.9, 1) with a smallest margin of 0.041406 and that
#: this gate admits, its witness violating feasibility by -1.666092e-08 against a
#: band of -4.833462e-12. That test asserts the WRONG answer deliberately, so
#: moving this constant in either direction turns it red instead of moving the
#: gap in silence: MEASURED, at 1e-8 the same design is refused.
_SEPARATION_WITNESS_FEASIBILITY = 1e-12


def _refuse(fn: str, message: str, code: GateDetailCode) -> GateError:
    """The one refusal shape, with the node that blocked the call named first."""
    return refusal(f"{fn}: {message}", code)


def require_supplied(value: object, *, fn: str, arg: str, remedy: str) -> None:
    """Refuse ``None`` for an argument the CONTRACT carries no default for.

    THE CASE THIS IS FOR, stated precisely because inventing a default here is
    the tempting alternative. A node argument may be optional and still have no
    entry in ``NODE_META[fn].defaults``; ``adapt_args`` then passes nothing and
    the body sees ``None``. Where the method has no meaning without the value,
    the body's only honest answers are to refuse it or to choose a default the
    wire contract does not publish -- and a default a client cannot read out of
    ``node-specs.json`` is a behaviour nobody agreed to. ``remedy`` names the
    admissible values, so the message tells the caller what to send.
    """
    if value is None:
        raise _refuse(
            fn,
            f'"{arg}" was not supplied, and this method has no meaning without it. '
            f"The node declares the argument optional, but the contract carries no "
            f"default for it, so nothing was filled in on your behalf and nothing "
            f"will be: a default this method invented would be one no client can "
            f"read out of the contract. {remedy}",
            "precondition-domain",
        )


def require_a_declared_option(
    value: object, *, allowed: tuple[str, ...], fn: str, arg: str, remedy: str
) -> None:
    """Refuse a value outside the set an ``enum`` argument declares.

    THE WIRE PATH ALREADY DOES THIS AND THE DIRECT PATH DOES NOT, WHICH IS THE
    WHOLE CASE FOR THE FUNCTION. ``mcp/make_tool.py`` builds a pydantic model from
    the node's contract and an ``enum`` argument is validated against the
    contract's own list before a body runs, so nothing reaching a node THROUGH THE
    WIRE can arrive outside it. A direct Python call has no such model in front of
    it.

    THE ANNOTATION IS NOT THE GUARD, AND BELIEVING IT WAS IS HOW THIS SHIPPED.
    ``tests/conftest.py`` installs ``beartype.claw`` over ``econflow_engine``,
    which does enforce every ``Literal`` -- but beartype is a DEV dependency and
    that hook is installed by pytest alone; conftest's own comment says it must
    never move into the package. So the suite runs with the check and the shipped
    package runs without it, which is precisely the arrangement in which no test
    can see the hole. MEASURED on a direct call to ``run_roc`` with the hook
    absent: ``direction='X'`` returned an area of 0.0 where ``'<'`` returns 1.0,
    with ``'X'`` echoed back under ``direction`` -- an inverted area and an
    orientation outside the declared enum, and no refusal. ``'less'`` and ``''``
    behaved the same way.

    IT CARRIES ``precondition-domain`` AND NOT ``gate-argument``. The value came
    from the CALLER and the caller can fix it by sending a declared one; the
    author-error code would tell a wrapper author to go looking at their own code
    for something a user typed.
    """
    if not isinstance(value, str) or value not in allowed:
        listed = ", ".join(repr(option) for option in allowed)
        raise _refuse(
            fn,
            f'"{arg}" was sent as {value!r}, which is not one of the values this '
            f"argument declares: {listed}. It is not resolved to a nearest match "
            f"and it is not defaulted -- every value here selects a different "
            f"answer, so guessing which one was meant would return a number the "
            f"caller did not ask for. {remedy}",
            "precondition-domain",
        )


def require_a_column(frame: pd.DataFrame, *, column: str, fn: str, arg: str) -> None:
    """Refuse a column name the frame does not carry, before the estimator sees it.

    The estimator's own failure here is a formula-engine error naming a factor
    rather than a column, which says nothing about which argument was wrong.

    PANDAS IS IMPORTED AT RUN TIME AND NOT UNDER ``TYPE_CHECKING``, which is not a
    style choice. ``tests/conftest.py`` installs ``beartype.claw`` over
    ``econflow_engine``, so every annotation in this package is RESOLVED when the
    function is called; a ``pd.DataFrame`` whose ``pd`` exists only for a type
    checker raises ``BeartypeCallHintForwardRefException`` at the first real call.
    Measured on this function before the import was moved.
    """
    if column not in frame.columns:
        raise _refuse(
            fn,
            f'"{arg}" names the column {column!r}, which the supplied data does not '
            f"carry. Its columns are {sorted(str(c) for c in frame.columns)}.",
            "precondition-shape",
        )


def require_counts(
    value: pd.Series, *, minimum: int, fn: str, arg: str, remedy: str
) -> None:
    """Refuse a response that is not a vector of whole numbers at or above ``minimum``.

    THE TWO SILENT ACCEPTANCES THIS BLOCKS, MEASURED against statsmodels 0.14.6 on
    the ten rows of Doll and Hill's table. ``Poisson(deaths + 0.5, X, exposure=t)``
    FITS: it returns ``llf = -33.269482`` and emits NOTHING under
    ``warnings.simplefilter('always')``. ``Poisson(deaths - 40, X, exposure=t)``
    raises nothing either and returns ``llf = nan``. A count likelihood is defined
    on the non-negative integers; handed anything else it either estimates a model
    nobody asked for or reports a number that is not one.

    ``minimum`` IS 1 FOR A ZERO-TRUNCATED MODEL AND 0 EVERYWHERE ELSE, which is the
    other half of the same rule rather than a second gate. MEASURED:
    ``TruncatedLFPoisson`` handed a sample WITH zeros returns the fit of the
    positives alone -- the same ``llf = -125.74492925346851`` either way -- so the
    zeros are dropped and the caller is told nothing.

    THIS DOCSTRING IS THAT FIGURE'S ONE HOME. The test that exercises the rule
    names it rather than restating it: the number it replaced was wrong in three
    files at once because each of the three had written it down separately. Taken
    from ``engine/``, with the engine importable::

        python -c "import sys, pandas as pd
        sys.path.insert(0, '.')
        from statsmodels.discrete.truncated_model import TruncatedLFPoisson as M
        from tests.wrappers.c16_limited_dependent.test_count_models import positives, sample
        def llf(y, x):
            d = pd.concat([pd.Series(1.0, index=y.index, name='const'), x], axis=1)
            return M(y, d).fit(disp=0).llf
        print(llf(*sample()), llf(*positives()))"

    MISSING IS CHECKED FIRST, by the primitive that owns that question. A vector
    carrying a ``nan`` is not a vector of counts, and asking about integrality
    before finiteness would report ``nan`` as "not a whole number", which is true
    and useless.
    """
    require_no_missing(value, fn=fn, arg=arg)
    array = np.asarray(value, dtype=float)
    fractional = array[array != np.floor(array)]
    if fractional.size:
        raise _refuse(
            fn,
            f'"{arg}" carries {fractional.size} value(s) that are not whole numbers '
            f"(the first is {fractional[0]}). This method is a count model: its "
            f"likelihood is defined on the non-negative integers, and a response "
            f"that is not one is fitted without complaint and reported as though it "
            f"were. {remedy}",
            "precondition-domain",
        )
    below = array[array < minimum]
    if below.size:
        raise _refuse(
            fn,
            f'"{arg}" carries {below.size} value(s) below {minimum} (the first is '
            f"{below[0]}). {remedy}",
            "precondition-domain",
        )


def require_strictly_inside(
    value: float | pd.Series, *, low: float, high: float, fn: str, arg: str
) -> None:
    """Refuse a value on or outside the OPEN interval ``(low, high)``.

    THE OPEN INTERVAL IS THE WHOLE REASON THIS EXISTS BESIDE
    :func:`~econflow_engine.gates.primitives.require_in_range`, which is inclusive
    by design and cannot express either rule this is called for. A confidence level
    of exactly 1 is an interval of infinite width, and an exposure of exactly 0 is
    an offset of minus infinity: both are endpoints, and both are admitted by an
    inclusive bound.

    MEASURED against statsmodels 0.14.6: an exposure carrying a single zero returns
    ``llf = nan`` from a fit that raised nothing, and a negative one does the same.

    A SERIES AND A SCALAR TAKE THE SAME RULE AND DIFFERENT MESSAGES, because what a
    reader needs to know differs: for one number it is the number, for a vector it
    is how many values broke the rule and where the first of them is.
    """
    interval = f"({low}, {high})"
    if isinstance(value, pd.Series):
        require_no_missing(value, fn=fn, arg=arg)
        array = np.asarray(value, dtype=float)
        outside = array[(array <= low) | (array >= high)]
        if outside.size:
            raise _refuse(
                fn,
                f'"{arg}" carries {outside.size} value(s) outside the open interval '
                f"{interval} (the first is {outside[0]}). The quantity this method "
                f"computes from it does not exist there.",
                "precondition-domain",
            )
        return
    if not low < float(value) < high:
        raise _refuse(
            fn,
            f'"{arg}" = {value} lies outside the open interval {interval}. The '
            f"endpoints are excluded rather than rounded to: at {low} and at {high} "
            f"the quantity this method reports is degenerate rather than extreme.",
            "precondition-domain",
        )


def require_within_bounds(
    value: pd.Series, *, low: float, high: float, fn: str, arg: str, remedy: str
) -> None:
    """Refuse a VECTOR carrying a value outside the CLOSED interval ``[low, high]``.

    THE THIRD CORNER OF A SET THAT NEEDED ALL THREE.
    :func:`~econflow_engine.gates.primitives.require_in_range` is closed and takes
    ONE number; :func:`require_strictly_inside` takes a vector and is open. A
    response that is a PROPORTION is the case neither answers: every observation
    must lie in ``[0, 1]``, and both endpoints are admissible data -- a household
    that spends none of its income on food, a plan in which nobody participates.
    Asking the open rule would refuse them, and asking the closed scalar rule
    would only see one number.

    MEASURED against statsmodels 0.14.6 on the 38 food-expenditure households of
    Ferrari and Cribari-Neto (2004). The Bernoulli quasi-likelihood of Papke and
    Wooldridge (1996) FITS a response outside the unit interval and says nothing:
    the published shares with the first replaced by 1.4 return
    ``llf = -17.215557434559905``, and with it replaced by -0.3,
    ``llf = -15.03350281799101``. Neither raises, and neither warns under
    ``warnings.simplefilter('always')``. A share reported in percent is how a
    caller reaches that by accident, which is what ``remedy`` is for.

    MISSING IS CHECKED FIRST, by the primitive that owns that question, for the
    reason :func:`require_counts` states: a ``nan`` is not outside the interval,
    it is not a number, and reporting it as out of range is true and useless.
    """
    if low > high:
        raise _refuse(
            fn,
            f"the gate was given low = {low} above high = {high} for \"{arg}\".",
            "gate-argument",
        )
    require_no_missing(value, fn=fn, arg=arg)
    array = np.asarray(value, dtype=float)
    outside = array[(array < low) | (array > high)]
    if outside.size:
        raise _refuse(
            fn,
            f'"{arg}" carries {outside.size} value(s) outside [{low}, {high}] (the '
            f"first is {outside[0]}). Both endpoints are admissible and everything "
            f"beyond them is not: this method is defined on that interval and fits "
            f"anything else without complaint, reporting an estimate of a model "
            f"nobody specified. {remedy}",
            "precondition-domain",
        )


def require_an_observed_value(
    value: pd.Series, *, level: float, fn: str, arg: str, remedy: str
) -> None:
    """Refuse a sample carrying no instance of the value the model is about.

    MEASURED against statsmodels 0.14.6: ``ZeroInflatedPoisson`` fitted to 95
    strictly positive counts CONVERGES, reporting an inflation probability that
    nothing in the sample identifies -- ``llf = -149.38423446264113``,
    ``converged`` true. A model of excess zeros over a sample with no zeros is not
    an extreme case of the model; it is a different one, estimated in silence.

    THIS DOCSTRING IS THAT FIGURE'S ONE HOME, for the reason
    :func:`require_counts` states. Taken from ``engine/``::

        python -c "import sys, pandas as pd
        sys.path.insert(0, '.')
        from statsmodels.discrete.count_model import ZeroInflatedPoisson as M
        from tests.wrappers.c16_limited_dependent.test_count_models import positives
        y, x = positives()
        d = pd.concat([pd.Series(1.0, index=y.index, name='const'), x], axis=1)
        r = M(y, d).fit(disp=0)
        print(r.llf, r.mle_retvals['converged'])"
    """
    if not bool((np.asarray(value, dtype=float) == level).any()):
        raise _refuse(
            fn,
            f'"{arg}" carries no value equal to {level:g}, and this model is about '
            f"how many of them there are. Fitted to a sample without one it still "
            f"returns a parameter, estimated from nothing. {remedy}",
            "precondition-degenerate",
        )


def require_distinct_column_names(
    frame: pd.DataFrame, *, fn: str, arg: str, remedy: str
) -> None:
    """Refuse a design whose columns cannot be told apart by name.

    MEASURED against statsmodels 0.14.6: a design carrying ``smokes`` twice is
    FITTED, with ``exog_names`` holding the name twice and the log-likelihood equal
    to the fit without the copy. Read back into a mapping keyed by name -- which is
    what a payload of coefficients is -- one of the two coefficients silently
    replaces the other.

    THE FRAME TO ASK ABOUT IS THE ASSEMBLED ONE, for the same reason
    :func:`require_an_allowlisted_specification` walks the assembled formula: a body
    that adds an intercept column of its own creates this collision itself, and the
    argument as the caller sent it cannot show it.
    """
    names = [str(name) for name in frame.columns]
    repeated = sorted({name for name in names if names.count(name) > 1})
    if repeated:
        raise _refuse(
            fn,
            f'"{arg}" names {repeated} more than once. Every column of this model is '
            f"reported under its name, so two columns sharing one leaves a result in "
            f"which one of them is simply absent. {remedy}",
            "precondition-shape",
        )


def require_an_aligned_index(
    value: pd.Series | pd.DataFrame,
    *,
    reference: pd.Index,
    fn: str,
    arg: str,
    remedy: str,
) -> None:
    """Refuse an argument whose labels are not the reference's, in the same order.

    WHY LABELS AND NOT LENGTH. pandas aligns on labels and this estimator does not:
    it takes the values. MEASURED against statsmodels 0.14.6 on Doll and Hill's ten
    rows -- an exposure holding the same ten person-year figures under a REVERSED
    index is used row by row as given and returns ``llf = -41.974688`` where the
    aligned one returns ``-33.600153``. Nothing in the result records which of the
    two happened. The estimator does refuse a mismatched endog/exog pair, with
    ``ValueError: The indices for endog and exog are not aligned``; it makes no such
    check on the exposure, and the rule is stated once here for every argument.
    """
    if not value.index.equals(reference):
        raise _refuse(
            fn,
            f'"{arg}" is not aligned with the response: its index carries '
            f"{len(value.index)} label(s) against the response's {len(reference)}, "
            f"and the two are not the same labels in the same order. This method "
            f"reads its arguments row by row rather than by label, so a difference "
            f"here silently pairs each observation with another one's covariates. "
            f"{remedy}",
            "precondition-shape",
        )


def require_a_bare_name(value: str, *, fn: str, arg: str) -> None:
    """Refuse a name that is not one plain identifier, BEFORE it is spliced into a formula.

    WHAT THIS BLOCKS, MEASURED against pyfixest 0.60.0 and the formulaic 1.2.2 it
    parses with. A body that concatenates this argument into an estimator
    specification hands it to a parser that splits on ``|``
    (``estimation/formula/parse.py``) and wraps each fixed effect as
    ``__fixed_effect__(<text>)`` (``estimation/formula/utils.py``); formulaic then
    evaluates that factor with ``eval(compiled, {}, LayeredMapping(...))``
    (``utils/stateful_transforms.py``). Empty globals means CPython injects
    ``__builtins__``, so ``__import__`` is reachable and the argument is
    EXECUTABLE CODE rather than a value. Live-measured: a ``fixef`` of
    ``__import__("os").environ.__setitem__("EF_RCE","pwned") or unit`` set that
    variable in this process.

    :func:`require_a_column` DOES NOT STOP IT. A caller who names a column with
    the payload satisfies it, and column names are caller-supplied -- a CSV
    header, or a frame fixture's ``columns`` list.

    ONE IDENTIFIER IS THE WHOLE RULE because an identifier cannot express a call,
    an attribute access, a subscript or an operator. It narrows nothing the
    contract promised: the argument names ONE column, and a column called ``a^b``
    was going to be mis-parsed by the formula engine anyway.
    """
    if not value.isidentifier() or keyword.iskeyword(value):
        raise _refuse(
            fn,
            f'"{arg}" is {value!r}, which is not a plain column name. This argument '
            f"is spliced into the formula the estimator is given, and that formula "
            f"is EVALUATED, so only a single bare name is accepted here -- no "
            f"operator, no call, no separator, no keyword. Name the column, or "
            f"rename a column whose name is not a plain name.",
            "precondition-domain",
        )


def require_an_allowlisted_specification(specification: str, *, fn: str) -> None:
    """Re-walk the ASSEMBLED estimator specification against the formula allowlist.

    THE SECOND OF THE TWO ENFORCEMENTS THE c00 NODE DOCUMENTATION ALREADY
    DECLARES -- "restricted to the formula allowlist (default-deny, enforced
    TWICE: at the argument boundary and again in the node)". The boundary walk in
    :mod:`econflow_engine.formula` sees the ``formula`` argument as the caller
    sent it. It never sees the string a body BUILDS from that argument and
    others, and the built string is what reaches the estimator. This asks the
    same default-deny question of what is actually handed over.

    THE FIXED-EFFECT SEPARATOR SURVIVES THE WALK, which is what makes this
    check usable on an assembled specification rather than only on a bare
    formula: ``|`` is in ``FORMULA_ALLOWED_CALLS``, and measured,
    ``validate_formula("y ~ x | unit")`` returns ok while the payload above
    returns ``formula-parse``.
    """
    result = validate_formula(specification)
    if not result.ok:
        raise _refuse(
            fn,
            f"the estimator specification {specification!r} was refused by the "
            f"formula allowlist, which is default-deny. {result.message} The "
            f"specification is built from the formula and the fixed effect, so "
            f"either of them may be the cause.",
            "precondition-domain",
        )


def require_at_most_one_spelling(
    *, fn: str, first: tuple[str, bool], second: tuple[str, bool], remedy: str
) -> None:
    """Refuse two spellings of one specification, rather than silently ranking them.

    Each argument is ``(name, is_present)``. Where a node offers two ways to say
    the same thing and its card does not say which wins, choosing one in the body
    settles a contract question in a place no reviewer of the card can see it.
    """
    if first[1] and second[1]:
        raise _refuse(
            fn,
            f'"{first[0]}" and "{second[0]}" were both supplied, and they are two '
            f"spellings of one specification. The method card does not say which of "
            f"the two wins, so neither is chosen here. {remedy}",
            "precondition-domain",
        )


def refuse_a_combination(
    *, fn: str, combination: str, reason: str, remedy: str
) -> NoReturn:
    """Refuse a combination of arguments this node cannot honour. Always raises.

    THE ALTERNATIVE IS A CRASH OR A SILENCE, and both were measured against
    statsmodels 0.14.6. ``HurdleCountModel`` handed an exposure raises
    ``NotImplementedError: Offset and exposure are not yet implemented``, and asked
    for a generalised-Poisson component raises ``NotImplementedError: dist and
    zerodist must be "poisson","negbin"``. ``NotImplementedError`` derives from
    ``RuntimeError`` and is defined in ``builtins``, so :func:`is_estimator_refusal`
    cannot recognise it by class or by module and must not: it is the same
    exception a stub raises. The silence is the other shape -- an argument that a
    branch simply ignores is a request the caller believes was honoured.

    ``reason`` says WHY the combination is unavailable and ``remedy`` says what to
    send instead; neither is optional, because a refusal that names only the
    combination tells a caller what they did and not what to do.
    """
    raise _refuse(
        fn,
        f"{combination} is not available. {reason} {remedy}",
        "precondition-domain",
    )


def require_convergence(*, converged: bool, fn: str, estimator: str, remedy: str) -> None:
    """Refuse the coefficients of a fit whose iteration did not converge.

    An iteratively reweighted least-squares fit that runs out of iterations still
    RETURNS -- with whatever the last step held. The flag is a boolean a caller
    can ignore, and the numbers beside it look exactly like an estimate.
    """
    if not converged:
        raise _refuse(
            fn,
            f"the {estimator} iteration did not converge, so the coefficients it "
            f"returned are the last step's values rather than an estimate. They are "
            f"not reported. {remedy}",
            "precondition-degenerate",
        )


def require_finite_estimates(
    values: pd.Series, *, fn: str, quantity: str, remedy: str
) -> None:
    """Refuse a number a fit cannot report, before the wire reports it as nothing.

    THE OTHER HALF OF :func:`require_convergence`, and the half every gate in this
    module was missing. The flag says the iteration FINISHED; nothing said what it
    finished with is a number. MEASURED against statsmodels 0.14.6 over the
    200-row sample in ``tests/wrappers/c16_limited_dependent/test_count_models.py``:
    a Poisson whose covariate is multiplied by 1e6 -- the scale of a population, a
    market capitalisation or a currency amount -- converges with ``converged``
    true, raises nothing, and returns ``llf = nan`` beside coefficients that are
    all ``nan``::

        ld_count_model(y=y, x=x.assign(w=x["w"] * 1e6), family="poisson")
        -> {"llf": nan, "params": {"const": nan, "w": nan, "v": nan}, ...}

    WHY THE NULL IS WORSE THAN A WRONG NUMBER WOULD BE.
    :func:`~econflow_engine.serialize.to_mcp` renders ``nan`` as ``null`` and
    ``to_json`` writes no ``NaN`` token, so what reaches the caller is well-formed
    JSON in which the estimate is simply empty -- and a payload of this kind
    already carries fields that are empty ON PURPOSE, such as the dispersion a
    Poisson estimates none of. Nothing distinguishes the two.

    ``inf`` IS REFUSED BESIDE ``nan``, for the reason
    :func:`~econflow_engine.gates.primitives.require_no_missing` refuses it on the
    way in: a quantity too large for a double has no reportable value, and it
    reaches the wire as that same ``null``.

    ``precondition-degenerate`` RATHER THAN A CODE OF ITS OWN. The vocabulary in
    :data:`~econflow_engine.gates.codes.GATE_DETAIL_CODES` is closed and shared
    with the corpus; this is the code :func:`require_convergence` and
    :func:`require_an_observed_value` already carry, and it says the same thing --
    the fit is a shape rather than an estimate.
    """
    array = np.asarray(values, dtype=float)
    unusable = ~np.isfinite(array)
    if not bool(unusable.any()):
        return
    labels = [str(name) for name in values.index]
    named = sorted({name for name, bad in zip(labels, unusable, strict=True) if bad})
    raise _refuse(
        fn,
        f"the {quantity} this method reports are not numbers: {named} (the first "
        f"is {array[unusable][0]}). They are not reported: each would reach you as "
        f"a null, which is also how this method reports a field it leaves empty on "
        f"purpose, so the two would be indistinguishable. {remedy}",
        "precondition-degenerate",
    )


def require_no_separation(
    design: pd.DataFrame, *, response: pd.Series, fn: str, remedy: str
) -> None:
    """Refuse a binary design whose maximum-likelihood estimate does not exist.

    THE QUESTION :func:`require_convergence` WAS BEING ASKED AND CANNOT ANSWER.
    Under perfect or quasi-complete separation the likelihood of a binomial GLM
    has no interior maximum -- the estimate runs off to infinity -- and every
    number an iteration returns is where it stopped. Reading the estimator's
    convergence flag to detect that reads the STOPPING RULE rather than the data.

    WHY THAT IS NOT A CONSERVATIVE READING BUT A LOTTERY. MEASURED against
    pyfixest 0.60.0, whose IWLS stops at
    ``|dev - dev_old| / (0.1 + |dev_old|) < 1e-8``
    (``pyfixest/estimation/models/feglm_.py`` 358-360, 426-440): a separated
    logit does not diverge, it stalls on a floating-point plateau at deviance
    0.019002321852144635, where that denominator is 0.119 -- so the flag fires
    the moment a step moves the deviance by less than 1.19e-9, which on a plateau
    is decided by the last bit of the linear algebra. numpy's wheel builds
    OpenBLAS ``DYNAMIC_ARCH``, so its GEMM kernel is chosen from the CPU at run
    time; a heterogeneous runner fleet therefore decides it afresh each run.
    Perturbing the IWLS step by ONE ULP flips the flag to True in 21 of 25
    perturbations of an unchanged frame, while the programme below scores an
    objective of 4.0 -- a margin of 4.4444e-01 against a largest row norm of 9 --
    in all 25.
    And a separated PROBIT needs no perturbation at all: it returns
    ``convergence`` True, deviance 0.5033898356102827 and coefficients
    -15.752136 and 3.500475 with p-values 0.149716 and 0.147083.

    WHAT IS ASKED INSTEAD -- Konis (2007) ch. 4, the linear-programming
    feasibility test, which is Silvapulle's (1981) existence condition solved as
    a programme rather than inspected. With ``z_i = 2 y_i - 1``::

        maximise  sum_i z_i x_i'b   subject to   z_i x_i'b >= 0 for all i,
                                                 |b_j| <= 1

    ``b = 0`` is always feasible, so the optimum is at least 0; it is EXACTLY 0
    when no hyperplane orders the two classes, which is precisely when the
    estimate exists. It is a question about the DATA, so its answer does not
    depend on where an iteration happened to stop, on how many iterations it was
    allowed, or on which kernel the machine chose.

    THE CALLER PASSES THE COVARIATES, AND A FIXED-EFFECT LEVEL IS NOT ONE OF
    THEM -- NOT BECAUSE THE LEVELS GAVE WRONG ANSWERS BUT BECAUSE THEY ANSWERED
    THE WRONG QUESTION. With the complete indicator set in the design this
    programme scores above zero exactly when some level carries a constant
    outcome, or when the covariates order the outcome inside every mixed level;
    both are non-existence of the UNCONDITIONAL estimate, so no estimable design
    was refused. But a constant-outcome level is the ORDINARY case in a binary
    panel and its effect is +/-infinity, contributing nothing to the conditional
    likelihood. MEASURED on logit panels with a firm effect and one covariate --
    constant-outcome firms, then margin with the levels before and after the
    estimator's own row dropping: 25 of 100 and 2.7035e+01 -> 1.6221e+01 over
    100 firms x 5 years; 16 of 100 and 3.4040e+01 -> 1.9147e+01 over 100 x 10;
    2 of 100 and 7.9761e+00 -> 0.0 over 100 x 20; 44 of 300 and 7.5204e+01 ->
    4.6148e+01 over 300 x 8. Over the covariates alone all four score 0.0.

    TWO GAPS THAT LEAVES, NAMED SO SOMEBODY CAN CLOSE THEM. A FIXED-EFFECT LEVEL
    WHOSE OUTCOME NEVER VARIES is not seen here. MEASURED on 138 rows carrying a
    twelve-row level with no positive outcome: 1.4634e-01 with the indicators and
    0.0 without them. pyfixest 0.60.0 answers that one itself -- it removes the
    twelve behind ``UserWarning: 12 observations removed because of separation.``
    and fits the remaining 126 -- and the estimate it reports EXISTS, MEASURED:
    the margin over those 126 is 0.0 either way. What is uncovered is the silence
    about the dropped rows, not a fit with no maximum. SEPARATION INSIDE EVERY
    LEVEL BUT NOT ACROSS THEM is the second and the worse: a covariate can order
    the outcome within each level at a different cut per level, and MEASURED on
    eight rows and two levels cut at 0 and at 10 the covariate scores 0.0 while
    the levels score 1.0256e-01, with ``feglm`` returning ``convergence`` True,
    deviance 6.016594756162403e-08 and a coefficient of 19.697788 whose standard
    error is 6795.277043 -- an estimate that does not exist, reported as a fit.

    RE-RUNNING THIS AFTER THE ESTIMATOR'S ROW DROPPING WOULD NOT CLOSE THEM:
    MEASURED, pyfixest removes an ALL-ZERO level and keeps an ALL-ONE one, so a
    100-firm five-year panel keeps fifteen of them and the programme over the
    rows it kept still scores 1.6221e+01. What closes both is the CONDITIONAL
    question -- a groupby for the constant-outcome levels, then this programme
    over the WITHIN-LEVEL DIFFERENCES ``x_i - x_j`` for ``y_i = 1, y_j = 0``,
    which needs as many columns as covariates and no indicator matrix. That is a
    different question, and its own change.

    A THIRD THING IT DECLINES TO ANSWER, AND THE PRINCIPLE BEHIND ALL THREE.
    Where the programme does not solve, or solves to a point that violates its own
    constraints, this returns rather than refuses. "The solver could not answer"
    and "the design separates" are different facts and only the second is about
    the caller's data, so a refusal built from the first states a falsehood about
    a frame nobody examined -- and MEASURED, the frames it stated it about are
    ordinary: 401 of 600 designs in one near-collinear band, and the one of those
    checked against the estimator is fitted by pyfixest at Intercept -0.138024 and
    ``a`` 0.397434. The refusal below therefore names the columns of a witness it
    has verified, and where there is no verified witness there is no claim. That
    is the same posture as the two gaps above, and it is deliberate: this gate's
    silence already means "not demonstrated" rather than "shown to be fine", and
    the estimator, :func:`require_convergence` and
    :func:`require_finite_estimates` all still stand behind it. Its cost is
    measured in :data:`_SEPARATION_WITNESS_FEASIBILITY` -- one separated design in
    3000 admitted -- against 381 falsely refused and 403 crashed in a population of
    12500 whose outcome no design orders.

    THIS IS ASKED OF ONE NODE TODAY. ``ld_count_model`` and
    ``ld_fractional_response`` are the same family and the same question belongs
    on both -- a Poisson with fixed effects separates the same way -- but each is
    its own change, with its own probe and its own paired tests, and neither is
    made here.
    """
    if design.shape[1] == 0:
        # A DESIGN WITH NO COLUMNS HAS NO DIRECTION TO SEPARATE ALONG, and it is
        # reachable rather than hypothetical: MEASURED, ``y ~ 0`` is admitted by
        # the formula allowlist and returns a converged intercept-free fit from
        # pyfixest 0.60.0, while ``linprog`` given an empty objective raises
        # "Invalid input for linprog: c must be a 1-D array". Answering the
        # question is what is wrong there, not the fit.
        return
    signs = 2.0 * np.asarray(response, dtype=float).ravel() - 1.0
    oriented = signs[:, None] * design.to_numpy(dtype=float)
    scale = float(np.abs(oriented).sum(axis=1).max())
    if scale == 0.0:
        # AN ALL-ZERO DESIGN HAS NO DIRECTION TO SEPARATE ALONG EITHER, and it
        # divided by that zero. MEASURED at the node: eight rows of alternating
        # outcome with ``x`` all zero and a fixed effect on ``g`` reached
        # ``ZeroDivisionError: float division by zero``, which escapes the gateway
        # -- ``mcp/make_tool.py`` turns a GateError into a refusal and lets every
        # other exception out as a crash. THE FIXED EFFECT IS WHAT MAKES IT
        # REACHABLE rather than incidental: it is the Intercept that keeps the
        # design non-zero, and ``y ~ x | g`` leaves ``matrix.independent`` holding
        # ['x'] alone where ``y ~ x`` leaves ['Intercept', 'x']. It is a
        # REGRESSION -- the same frame with ``x`` at 1e-320 still refuses through
        # the estimator's own "All variables are collinear".
        return
    programme = linprog(
        c=-oriented.sum(axis=0),
        A_ub=-oriented,
        b_ub=np.zeros(oriented.shape[0]),
        bounds=(-1.0, 1.0),
        method="highs",
    )
    if not programme.success:
        # THE SOLVER DID NOT ANSWER, WHICH IS NOT A FACT ABOUT THE CALLER'S DATA.
        # ``success`` is exactly ``status == 0``; of the four failing statuses,
        # infeasible (2) and unbounded (3) cannot describe THIS programme -- b = 0
        # is always feasible and the box bounds every direction -- so the only
        # honest readings left are an iteration limit (1) and numerical difficulty
        # (4). MEASURED that it is reachable and that reading it as separation was
        # never the alternative: 60 rows with one covariate scaled to 1e15 return
        # ``success`` False, ``status`` 2 and the message "(HiGHS Status 2: Model
        # error)" with ``fun`` and ``x`` both None, on which the line below raised
        # ``TypeError: bad operand type for unary -: 'NoneType'`` and escaped the
        # gateway. Refusing here would state that a design separates on the
        # strength of a programme that produced no answer about it.
        return
    margin = float(-programme.fun) / scale
    if margin <= _SEPARATION_MARGIN:
        return
    witness = np.asarray(programme.x, dtype=float)
    if float((oriented @ witness).min()) < -_SEPARATION_WITNESS_FEASIBILITY * scale:
        # THE OBJECTIVE IS ONLY WORTH READING AT A POINT THAT SATISFIES THE
        # CONSTRAINTS, and HiGHS's own primal feasibility tolerance is 1e-7 rather
        # than zero. See :data:`_SEPARATION_WITNESS_FEASIBILITY` for the measured
        # band in which it returns a violating point with a margin above the
        # threshold, and for the one separated design in 3000 this declines to
        # refuse as a result.
        return
    separating = sorted(
        str(name)
        for name, weight in zip(design.columns, witness, strict=True)
        if abs(float(weight)) > _SEPARATION_MARGIN
    )
    raise _refuse(
        fn,
        f"the design separates the outcome. A linear combination of {separating} "
        f"orders every observation, so the likelihood has no interior maximum and "
        f"the maximum-likelihood estimate does not exist. What an iteration returns "
        f"for it is where the iteration stopped rather than an estimate, and it is "
        f"not reported. {remedy}",
        "precondition-degenerate",
    )


def is_estimator_refusal(error: object) -> bool:
    """Is this exception the ESTIMATOR objecting, rather than a defect in the body?

    THE TWO ARMS ARE MEASURED, NOT GUESSED, against pyfixest 0.60.0 and the
    formulaic 1.2.2 it parses formulas with. A refusal about the caller's data
    arrives as one of:

    * ``ValueError`` -- "The dependent variable must have two unique values.",
      "The dependent variable must be binary (0 or 1)."
    * ``ArithmeticError`` -- ``ZeroDivisionError`` raised out of the IWLS when the
      sample is two observations long, and ``FloatingPointError`` wherever a
      caller has put ``np.seterr`` into a raising state around an intermediate
      the estimator expects to underflow. THE WHOLE CLASS, INCLUDING AN OVERFLOW,
      and that is deliberate rather than an oversight in the spelling: a caller
      whose error state raises on overflow gets ``FloatingPointError`` from numpy
      and not ``OverflowError`` -- measured -- so excluding ``OverflowError``
      would exclude the one class an overflow does not arrive as. A body calls
      this from an ``except`` around the ESTIMATOR CALL ALONE, which is what makes
      the whole class safe to read as the estimator's: none of this engine's own
      arithmetic is inside that block.
    * an exception class defined by the estimator or its formula engine --
      ``formulaic.errors.FactorEvaluationError`` for a column the frame does not
      carry, ``pyfixest.errors.FormulaSyntaxError`` for a malformed formula.
      NEITHER derives from ``ValueError``; both derive straight from
      ``Exception``, so a type-based catch cannot reach them.

    ``statsmodels`` JOINED THE SET WITH THE SECOND 2.2 BODY, AND WHAT IT CONTRIBUTES
    IS TWO SHAPES. Its own error classes in ``statsmodels.tools.sm_exceptions`` --
    ``PerfectSeparationError``, ``MissingDataError`` -- derive straight from
    ``Exception`` and are unreachable by class, exactly as formulaic's are. Its
    WARNINGS live in the same module, and under a caller that turns warnings into
    errors -- which is how this repository's own suite runs -- an optimiser's
    warning arrives here as an exception raised from inside the fit. Reading it as
    the estimator objecting is deliberate.

    WHAT WAS MEASURED ABOUT THAT, AND WHAT WAS NOT. One node and one input:
    ``ld_count_model(family='negative_binomial', zeros='zero_inflated')`` over the
    200-row sample of ``tests/wrappers/c16_limited_dependent/test_count_models.py``
    is refused BOTH ways. Under ``-W error`` a ``HessianInversionWarning`` -- not
    the ``ConvergenceWarning`` one would expect, it simply arrives first -- reaches
    this predicate and the call is refused as the estimator's; with the warnings
    allowed to be warnings the fit returns and :func:`require_convergence` refuses
    it. So on that case the caller's filter changes the message and not the
    verdict. THAT IS NOT ASSERTED AS A GENERAL PROPERTY and nothing here measures
    one: a warning about something other than the optimiser would be read as a
    refusal by this predicate with no gate behind it to agree, and only a body that
    gates the same fact twice earns the equivalence above.

    What is NOT covered, and must not be: ``NotImplementedError``
    for a model combination the library does not carry. It is defined in
    ``builtins``, it is the exception an unwritten body raises, and a wrapper that
    read it as a refusal would report its own stubs as the caller's problem --
    :func:`refuse_a_combination` is what those two measured cases go through.

    THE DEFINING MODULE IS READ OFF THE CLASS AND THE CLASS IS NOT IMPORTED.
    ``formulaic`` is a transitive dependency of ``pyfixest``; importing it to
    name its base class would declare a dependency this engine does not take, and
    ``deptry`` is right to object to that.

    Everything else -- an ``AttributeError``, a ``TypeError``, a ``KeyError``
    raised by this engine's own code -- is a defect in the wrapper and must reach
    the caller as the crash it is.
    """
    if isinstance(error, ValueError | ArithmeticError):
        return True
    return type(error).__module__.split(".", 1)[0] in _ESTIMATOR_PACKAGES


def refuse_estimator_failure(
    error: Exception, *, fn: str, code: GateDetailCode, remedy: str
) -> NoReturn:
    """Translate the estimator's own refusal into this engine's refusal. Always raises.

    THE ORIGINAL MESSAGE IS CARRIED VERBATIM and the class is named beside it: it
    is the only account of what the estimator actually objected to, and a
    paraphrase here would be this engine guessing at a library's reasoning.
    ``raise ... from error`` at the call site keeps the traceback for a developer
    while the wire sees the refusal.
    """
    raise _refuse(
        fn,
        f"the estimator refused these inputs. It reported "
        f"{type(error).__name__}: {error}. {remedy}",
        code,
    )


def refuse_a_multi_model_fit(*, fn: str, produced: str, remedy: str) -> NoReturn:
    """Refuse a fit that is SEVERAL models, where the node's contract is one. Always raises.

    A fixest-style formula language can ask for a family of models in one string
    -- ``sw()``, ``csw()``, several variables on the left -- and the estimator
    then returns a COLLECTION rather than a fit. Every node in this catalogue
    declares one result, so the collection has nowhere to go: reading the first
    of its models would answer a question the caller did not ask, and reading
    none of them would report success over an empty result.

    ``-> NoReturn`` IS PART OF THE CONTRACT AND NOT DECORATION. Called under an
    ``isinstance`` guard it narrows the fit's type for the checker as well as for
    the reader, which is what lets a body reach the single model's attributes
    without a cast that asserts what this call has already established.
    """
    raise _refuse(
        fn,
        f"the formula asked for more than one model and the estimator returned a "
        f"{produced} rather than a fit. This node reports one model. {remedy}",
        "precondition-shape",
    )
