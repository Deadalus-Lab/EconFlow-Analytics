# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``binomial_glm_recession`` -- method card #83.

#83 Binomial GLM (probit/logit) — recession probability (Estrella-Mishkin)

Category 16-limited-dependent; module ``binomial_glm_recession``.

Reference implementation: pyfixest.

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
    "run_binomial_fe_glm",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---

import math
import warnings

import numpy as np

# NOT `import pyfixest as pf`. `pyfixest.estimation.feglm` is re-exported on the
# package, and the package ALSO holds a submodule of the same name; pyright
# resolves the attribute to the module and reports the call as uncallable, where
# mypy resolves it to the function. Naming the function is what both agree on.
from pyfixest.estimation import Felogit, Feprobit, feglm

# The estimator's OWN model-matrix construction, which is what `feglm` reaches
# for at `models/feols_.py:405`. pyfixest's deprecation notice on the retired
# `model_matrix_fixest` names this pair as its replacement; neither is exported
# on the package root, and a second formula grammar beside the estimator's would
# gate a design it never fits.
from pyfixest.estimation.formula.model_matrix import create_model_matrix
from pyfixest.estimation.formula.parse import Formula

from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_multi_model_fit,
    refuse_estimator_failure,
    require_a_bare_name,
    require_a_column,
    require_a_declared_option,
    require_an_allowlisted_specification,
    require_at_most_one_spelling,
    require_convergence,
    require_no_separation,
    require_supplied,
)
from econflow_engine.gates.primitives import (
    require_min_length,
    require_no_missing,
)

#: The node this module's one gate message names.
_FN = "run_binomial_fe_glm"

#: MEASURED against pyfixest 0.60.0: two observations raise ``ZeroDivisionError``
#: out of the IWLS rather than refusing, and one observation raises the
#: estimator's own "two unique values" ``ValueError``. Three is where the
#: estimator stops crashing, so three is where this refusal stops. It is a floor
#: on the CALL, not a claim that three observations estimate anything: a fit that
#: short is caught downstream by the convergence gate or by the estimator itself.
_MIN_OBSERVATIONS = 3

#: The response distribution, which is fixed for this node. ``link`` selects the
#: link function within it; the estimator's ``family`` argument conflates the two.
_FAMILY = "binomial"

#: formulaic's own name for the constant column, taken rather than invented: it is
#: the label a caller reads in the separation refusal, and it has to be the one
#: ``matrix.independent`` already uses on the specifications that carry one.
_INTERCEPT = "Intercept"

#: What to send instead, wherever the estimator itself objects. Named once
#: because the two blocks that translate its refusals -- the design build and the
#: fit -- run the same parser over the same specification and reject the same
#: two things.
_ESTIMATOR_REMEDY = (
    "The formula must name columns the data carries, and the variable on its left "
    "must be binary -- exactly two levels, coded 0 and 1."
)

#: What a caller must send in place of an absent or undeclared ``link``, and what
#: each value means. Written once because both refusals on that argument use it.
_LINK_REMEDY = (
    "Pass link='probit' for the Estrella-Mishkin specification, or link='logit'."
)


def _options(argument: str) -> tuple[str, ...]:
    """The values ``node-specs.json`` declares for one ``enum`` argument of this node.

    READ FROM THE CONTRACT rather than written out here, so the set this body
    refuses against and the set ``mcp/make_tool.py`` validates a wire call against
    cannot disagree. ``NodeArgMeta.enum`` is ``None`` for an argument of any other
    kind; the empty tuple that produces refuses every value, which is the safe
    direction for a module that may not raise.
    """
    declared = next(arg for arg in NODE_META[_FN].args if arg.name == argument)
    return declared.enum or ()


def _usable_numbers(data: pd.DataFrame) -> None:
    """Refuse a frame carrying a missing or non-finite value, column by column.

    WHY THE WHOLE FRAME AND NOT ONLY THE MODEL'S OWN VARIABLES. MEASURED against
    pyfixest 0.60.0 on the 23 Challenger flights: one missing response returns a
    fit over 22 rows with ``na_index`` EMPTY, so nothing in the result says a row
    was dropped, and the coefficients move from 15.043 to 16.031. An infinite
    value is dropped too, behind a ``UserWarning`` and nothing else. Naming the
    model's own variables would need a second formula parser beside the
    estimator's, so the rule is stated over the frame the caller supplied and the
    message says how to satisfy it.

    A non-numeric column -- a fixed-effect key is usually one -- cannot go
    through the numeric primitive, so its null positions are handed over as the
    one thing that primitive refuses.
    """
    for name in data.columns:
        column = data[name]
        label = f'data["{name}"]'
        if pd.api.types.is_numeric_dtype(column) and not pd.api.types.is_bool_dtype(column):
            require_no_missing(column, fn=_FN, arg=label)
        else:
            require_no_missing(
                np.where(column.isna(), np.nan, 0.0), fn=_FN, arg=label
            )


def _separation_design(
    specification: str, data: pd.DataFrame
) -> tuple[pd.DataFrame, pd.Series] | None:
    """The design and the response the estimator is about to fit, ``None`` where
    the specification carries no single binary model to ask about.

    THE ESTIMATOR'S OWN PARSER, NOT A SECOND ONE. ``Formula.parse`` and
    ``create_model_matrix`` are the two calls ``Feols.prepare_model_matrix``
    makes (``pyfixest/estimation/models/feols_.py`` 405-413), and pyfixest's own
    deprecation notice on the retired ``model_matrix_fixest`` names them as the
    replacement. Reaching for ``formulaic`` directly would put a second formula
    grammar beside the estimator's and gate a design it never fits.

    THE DESIGN IS ``matrix.independent`` PLUS AN INTERCEPT, AND THE FIXED-EFFECT
    LEVELS ARE NOT IN IT. The intercept is the gate's stated contract for
    ``design`` -- every column whose coefficient the likelihood is maximised over
    -- and formulaic supplies it for ``y ~ x`` and withholds it for ``y ~ x | g``,
    which is why it is added here rather than relied on. THE REASON THE LEVELS ARE
    OUT IS NOT THAT EXPANDING THEM GAVE WRONG ANSWERS -- IT DID NOT --
    BUT THAT IT ANSWERED THE WRONG QUESTION, AND THIS PARAGRAPH SAYS SO BECAUSE
    THE FIRST DRAFT OF IT CLAIMED OTHERWISE. With the complete indicator set in
    the design the programme scores above zero exactly when some level carries a
    constant outcome, or when the covariates order the outcome inside every mixed
    level; both are precisely non-existence of the UNCONDITIONAL maximum
    likelihood estimate, so no estimable design was ever refused.

    THE TROUBLE IS THAT THE UNCONDITIONAL ESTIMATE IS NOT WHAT A BINARY PANEL IS
    FOR, AND A CONSTANT-OUTCOME LEVEL IS THE ORDINARY CASE. MEASURED on logit
    panels carrying a firm effect and one covariate -- constant-outcome firms,
    then margin with the levels before and after ``feglm``'s own row dropping:
    25 of 100 firms and 2.7035e+01 -> 1.6221e+01 over 100 firms x 5 years;
    16 of 100 and 3.4040e+01 -> 1.9147e+01 over 100 x 10; 2 of 100 and
    7.9761e+00 -> 0.0 over 100 x 20; 44 of 300 and 7.5204e+01 -> 4.6148e+01 over
    300 x 8. Over the covariates alone all four score 0.0. Such a level's effect
    is +/-infinity, it contributes nothing to the CONDITIONAL likelihood, and
    dropping its rows is the standard treatment -- so refusing the whole fit for
    it turns a routine panel into an error.

    THE LEVELS ALSO DENSIFIED THE DESIGN. ``pd.get_dummies`` built an ``n`` x
    ``levels`` float64 matrix on a node that takes a caller-supplied handle.
    MEASURED over 20000 rows and 10000 levels, two rows to a level so that none
    is dropped: a design of (20000, 10001) and 7852 MB of peak RSS through the
    programme, against (20000, 1) and 237 MB over the covariates.

    WHAT THE COVARIATES-AND-INTERCEPT PROGRAMME ASKS IS A THIRD QUESTION --
    whether one hyperplane orders the POOLED sample -- which is neither of the two
    above. It keeps every unambiguous refusal (see the two links in the body's
    docstring) and gives up the fixed-effect half entirely; the gap below says
    what that costs and what would close it properly. The intercept is what makes
    it a hyperplane rather than a half-space through the origin, and refusing on
    it says nothing false about a conditional estimate: a direction that orders
    the pooled sample orders it inside every level too, so the within-level
    likelihood is non-decreasing along the same ray.

    ``drop_singletons=True`` MIRRORS ``feglm``'s ``fixef_rm='singleton'``
    DEFAULT, which ``_drop_singletons`` turns into exactly this flag
    (``pyfixest/estimation/FixestMulti_.py`` 249, 758). IT IS THE ROW SET THAT
    NEEDS IT AND NO LONGER THE MARGIN, which corrects the reason recorded here
    while the levels were in the design: a singleton was then its own indicator
    column and separated on it alone, MEASURED on the 138 O-ring rows with one
    row given a level of its own, at positions 0, 68 and 137 -- 0.0 with it
    dropped and 1.2195e-02 with it kept. Over the covariates alone all six of
    those score 0.0, so the flag changes no answer here. It stays because it
    aligns this design with the estimator's -- PARTLY: ``feglm`` drops further
    rows after this point, for separation, which this function does not see.

    TWO CASES THIS LEAVES UNCOVERED. NAMED RATHER THAN DROPPED, BOTH MEASURED.

    (1) A FIXED-EFFECT LEVEL WHOSE OUTCOME NEVER VARIES. MEASURED on the 138
    O-ring rows carrying a twelve-row level with no incident in it: the margin is
    1.4634e-01 with the indicators in the design and 0.0 without them. pyfixest
    0.60.0 answers this one itself -- it removes the twelve behind
    ``UserWarning: 12 observations removed because of separation.``, fits the
    remaining 126 and returns ``convergence`` True -- and the estimate it hands
    back EXISTS: MEASURED, the margin over those 126 rows is 0.0 with the levels
    and without them. What is uncovered is the SILENCE about the twelve rather
    than a fit with no maximum; the caller is told by that warning and by a
    shorter ``obs_kept``, and by nothing else.

    (1b) AND THE MIRROR OF IT IS NOT SYMMETRIC, WHICH IS WHY IT IS WRITTEN OUT.
    pyfixest's check removes a level that is ALL-ZERO and keeps one that is
    ALL-ONE. MEASURED on the same 138 rows with six incident rows given a level
    of their own: the margin is 7.3171e-02 with the indicators and 0.0 without
    them, and ``feglm`` keeps all 138 rows, returns ``convergence`` True and
    raises NO WARNING AT ALL. MEASURED on the panels above, where the split is
    plain: 100 firms x 5 years carries ten all-zero levels and fifteen all-one,
    and after the drop the all-zero are gone and all fifteen all-one remain.
    Here the caller gets no signal whatever -- not a warning, not a shortened
    ``obs_kept`` -- so this half is worse than (1) and shares its cause.

    (2) SEPARATION INSIDE EVERY LEVEL BUT NOT ACROSS THEM, WHICH IS THE WORSE
    HALF AND IS NOT THE SAME CASE. A covariate can order the outcome within each
    level at a DIFFERENT cut per level, and then no single hyperplane orders the
    pooled sample and the covariates alone score 0.0. MEASURED on eight rows and
    two levels, ``x`` cutting level A at 0 and level B at 10: 0.0 over the
    covariate, 1.0256e-01 with the levels, and ``feglm`` returns ``convergence``
    True, deviance 6.016594756162403e-08 and a coefficient of 19.697788 with a
    standard error of 6795.277043. That is a maximum-likelihood estimate that
    does not exist, reported as a fit -- the defect this gate exists for, in its
    fixed-effect form -- and this design admits it.

    WHAT WOULD CLOSE THEM, AND WHAT WOULD NOT. Re-running this programme after
    the estimator's own row dropping would NOT: MEASURED, pyfixest's check leaves
    fifteen all-one levels in the 100 x 5 panel and the programme over the rows
    it kept still scores 1.6221e+01, so that route refuses the same routine
    panels the levels did. What closes both is asking the CONDITIONAL question
    the panel is actually about, which needs no indicator matrix: (a) any level
    with a constant outcome, found by one groupby; (b) for the rest, whether one
    ``b`` orders the outcome inside every mixed level, which is a programme over
    the WITHIN-LEVEL DIFFERENCES ``x_i - x_j`` taken for ``y_i = 1, y_j = 0`` --
    as many columns as covariates, and no ``n`` x ``levels`` matrix anywhere.
    That is a different question from the one asked here, with its own probe, its
    own paired tests and its own owner decision. It is not made here.

    THE TWO ``None`` ANSWERS ARE THE TWO STATES IN WHICH THE QUESTION HAS NO
    MEANING, AND THE ESTIMATOR REFUSES BOTH A FEW LINES BELOW. A specification
    naming several models parses to several formulas and returns a
    ``FixestMulti``; a response that is not two-valued 0/1 raises the estimator's
    own "The dependent variable must have two unique values." Separation is
    defined for one binary model, and answering for a response of ``{0.0}`` or
    ``{0.0, 1.0, 2.0}`` would replace a refusal that says what is wrong with one
    that does not.

    THE SUPPRESSED WARNING IS THE ESTIMATOR'S, RAISED ONE LINE EARLY. This build
    and ``feglm``'s take the same formula, the same frame and the same arguments,
    so MEASURED they emit the identical ``UserWarning`` about dropped singletons
    -- twice, once each. The caller must see it once, from the fit; and where
    this gate refuses, there is no fit and the refusal is the message.
    """
    formulas = Formula.parse(specification)
    if len(formulas) != 1:
        return None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        matrix = create_model_matrix(
            # `data.copy()` AND `context={}`, BOTH MEASURED, NEITHER OPTIONAL.
            #
            # `feglm` passes `copy_data=True` and so never touches the frame the
            # caller handed over; `create_model_matrix` opens with
            # `data.reset_index(drop=True, inplace=True)` and, for a `^`
            # interaction, writes the encoded column back. MEASURED: a frame
            # indexed 10..17 came back indexed 0..7, and `y ~ x | era^dec` left
            # a new `era_dec` column on the CALLER's object. A gate that reads
            # must not rewrite what it read.
            #
            # `context` defaults to 0, a STACK FRAME OFFSET: `capture_context(0)`
            # is `sys._getframe(3)`, which through this direct call is THIS
            # function's frame and through `feglm` is a pyfixest-internal one.
            # Its mapping is merged on the RIGHT, so it also shadows pyfixest's
            # own `log`, `i` and `__fixed_effect__`. MEASURED before pinning it:
            # `y ~ specification` and `y ~ formulas` resolved this function's
            # locals as factors and escaped as a raw `TypeError`, on a body whose
            # formula surface has already carried one live injection. An empty
            # mapping is the environment the estimator's own path offers.
            formula=formulas[0],
            data=data.copy(),
            drop_singletons=True,
            context={},
        )
    response = matrix.dependent.iloc[:, 0]
    if set(response.unique()) != {0.0, 1.0}:
        return None
    design = matrix.independent
    if _INTERCEPT not in design.columns:
        # THE GATE'S ``design`` CONTRACT, OBEYED ON BOTH PATHS RATHER THAN ON ONE.
        # `matrix.independent` carries an ``Intercept`` for ``y ~ x`` and none for
        # ``y ~ x | g``, because the fixed effect absorbs it -- so the same question
        # was put to two different designs, and nobody chose the second. MEASURED,
        # what that left open is the ordinary case of a dummy regressor: over the
        # covariate alone the eight rows of this module's paired test score 0.0 and
        # are admitted, and with the intercept 2.0; on Stata's 66 repair records the
        # same shape reads 0.0 against 2.250000e+01. ONE COLUMN IS NOT THE INDICATOR
        # MATRIX, which is what the levels were removed for: MEASURED over four
        # seeded logit panels with a firm effect and one covariate -- 100 x 5,
        # 100 x 10, 100 x 20 and 300 x 8 -- the margin is 0.0 over the covariates and
        # 0.0 with the intercept in all four, while the levels score 3.2464e+01,
        # 1.8916e+01, 1.7923e+01 and 7.7471e+01.
        design = design.copy()
        design.insert(0, _INTERCEPT, 1.0)
    return design, response


def _null_deviance(response: np.ndarray) -> float:
    """The deviance of the intercept-only Bernoulli model, in closed form.

    McFadden's pseudo-R2 is a ratio against the intercept-only log-likelihood, and
    for a Bernoulli response that model has one parameter with a closed-form
    maximum at the sample proportion, so no second fit is needed::

        D0 = -2 [ m log(m/n) + (n - m) log(1 - m/n) ]

    MEASURED against a real refit of ``incident ~ 1`` on the 23 flights: both
    return 28.267152734293497, bit for bit. The closed form is used because a
    refit would need the response's name parsed back out of the formula, and an
    expression on the left-hand side has no name to parse.
    """
    n = int(response.size)
    ones = float(response.sum())
    proportion = ones / n
    return -2.0 * (ones * math.log(proportion) + (n - ones) * math.log1p(-proportion))


def run_binomial_fe_glm(
    *,
    formula: str,
    data: pd.DataFrame,
    link: Literal["probit", "logit"] | None = None,
    fixef: str | None = None,
) -> dict[str, Any]:
    """Node ``run_binomial_fe_glm`` -- method card #83.

    Binomial GLM (probit/logit) — recession probability (Estrella-Mishkin).

    Category 16-limited-dependent; memory class ``light``.

    Args:
        formula: [formula, required] Binary model formula, e.g. 'recession ~ spread'· high-dim fixed
            effects also via '| year'.
        data: [df_handle, required] Handle to a DataFrame· LHS binary (0/1, logical or 2-level
            factor), without NA in the variables.
        link: [enum, optional] Link function (default probit — Estrella-Mishkin).
        fixef: [string, optional] Column name of the high-dim fixed effect (alternatively via '|
            col' in the formula)· the column must exist in the data.

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

        - separation is refused ACROSS the sample and is NOT checked WITHIN a fixed effect, and that
          is a deliberate boundary rather than an oversight. The body puts Konis (2007)
          linear-programming feasibility -- Silvapulle's (1981) existence condition solved as a
          programme -- to the COVARIATES alone, because expanding the fixed-effect levels into
          indicators answers a different question: with the levels in the design the programme
          scores above zero whenever any level carries a constant outcome, which is the ORDINARY
          case in a binary panel and whose effect is infinite and contributes nothing to the
          conditional likelihood. MEASURED on logit panels with a firm effect and one covariate,
          constant-outcome firms against the margin with the levels in: 25 of 100 firms and
          2.7035e+01 over 100 firms x 5 years, 44 of 300 and 7.5204e+01 over 300 x 8 -- while over
          the covariates alone all of them score 0.0. So refusing on the expanded design would turn
          routine panels into errors, and the narrower question is asked instead
        - the case that boundary leaves open is a covariate that orders the outcome inside EVERY
          level at a different cut per level, which no single hyperplane over the pooled sample can
          see. MEASURED on eight rows and two levels cut at 0 and at 10: the covariates score 0.0
          and the levels 1.0256e-01, and feglm returns convergence TRUE with deviance
          6.016594756162403e-08 and a coefficient of 19.697788 whose standard error is 6795.277043
          -- a maximum-likelihood estimate that does not exist, reported as a fit. Read the standard
          errors and obs_kept rather than the convergence flag: a coefficient near 20 beside a
          standard error in the thousands is separation inside a level, not an effect
        - a fixed-effect level whose outcome never varies is dropped by the estimator rather than by
          this node, and the two halves of that are NOT symmetric. MEASURED against pyfixest 0.60.0:
          an ALL-ZERO level is removed behind 'UserWarning: N observations removed because of
          separation.' and shortens obs_kept, while an ALL-ONE level is KEPT with no warning and no
          change to obs_kept at all -- on 138 rows with six positive rows given a level of their
          own, all 138 are kept and convergence is TRUE. The estimate that comes back is one that
          exists, so this is silence about which rows were used rather than a fit with no maximum;
          compare obs_kept against the frame's own length before reading the coefficients as an
          answer about the whole sample

    .. gen_wrappers: end of generated docstring

    Examples:
        The Challenger field-joint O-rings, one row per O-ring, as a logit on the
        joint temperature. Eight flights of Dalal, Fowlkes and Hoadley's Table 1
        are enough to show the shape of the result. THE COEFFICIENT BELOW IS THIS
        48-ROW SUBSET'S OWN and is not the published number: the full 138-row
        fixture returns -0.1156, and the oracle case under
        ``tests/oracle/c16_limited_dependent/`` is where that comparison is
        made::

            >>> import pandas as pd
            >>> flights = [(66, 0), (70, 1), (57, 1), (63, 1), (53, 2), (75, 2), (58, 1), (81, 0)]
            >>> frame = pd.DataFrame(
            ...     [
            ...         (float(temperature), 1.0 if ring < incidents else 0.0)
            ...         for temperature, incidents in flights
            ...         for ring in range(6)
            ...     ],
            ...     columns=["temperature", "incident"],
            ... )
            >>> fit = run_binomial_fe_glm(
            ...     formula="incident ~ temperature", data=frame, link="logit"
            ... )
            >>> fit["nobs"], len(fit["obs_kept"])
            (48, 48)
            >>> round(fit["coefficients"]["temperature"], 4)
            -0.0376
            >>> sorted(fit["coeftable"].columns)
            ['estimate', 'p_value', 'std_error', 'term', 'z_value']

        An absent ``link`` is refused rather than filled in, because the node
        contract carries no default for it::

            >>> run_binomial_fe_glm(formula="incident ~ temperature", data=frame)
            Traceback (most recent call last):
            econflow_engine.errors.GateError: run_binomial_fe_glm: "link" was not...

    Note:
        FUNCTIONS USED. ``pyfixest.estimation.feglm`` (pyfixest 0.60.0, MIT), with ``family``
        set from ``link`` and the fixed effect folded into the formula after
        ``|``; ``pandas`` 2.3.3 and ``numpy`` 2.5.2 for the frame and the
        arithmetic. The estimator supplies the coefficients, the coefficient
        table, the fitted probabilities, the deviance, the convergence flag and
        the fixed-effect levels, and nothing else this card promises.

        WHAT THIS ENGINE COMPUTES ITSELF, AND WHY. MEASURED: pyfixest 0.60.0
        exposes no log-likelihood, AIC, BIC or pseudo-R2 for a binary GLM --
        ``get_performance()`` is declared ``() -> None`` and returns ``None``, and
        the fitted object carries no such attribute. For a Bernoulli response the
        saturated log-likelihood is zero, so ``loglik`` is ``-deviance / 2``;
        ``aic`` is ``2k - 2 loglik`` and ``bic`` is ``k log n - 2 loglik`` with
        ``k`` the estimated coefficients plus the fixed-effect levels the fit
        reports; ``pseudo_r2`` is McFadden's ``1 - loglik / loglik0`` against the
        intercept-only model, whose deviance is taken in closed form.

        ``z_value`` AND ``p_value`` ARE RENAMES, NOT RE-DERIVATIONS. pyfixest
        labels the two columns ``t value`` and ``Pr(>|t|)``. MEASURED on the
        O-ring fit: the printed 0.04638166535467736 is the two-sided NORMAL tail
        for 1.991903, and the t-distribution on 21 degrees of freedom gives
        0.0595 -- so the numbers are already a z-test and only the labels say
        otherwise. The card's names are used and the numbers are carried through.

        ``obs_kept`` IS READ OFF THE RETAINED FRAME'S POSITIONAL INDEX, which is
        the one derivation that is right. MEASURED: ``na_index`` records the rows
        a separation check dropped and NOT the rows a singleton fixed effect
        dropped -- a singleton drop leaves it empty while the sample shrinks --
        so subtracting it from the row count is wrong in exactly the case card
        #83's second interpretation trap warns about.

        DELIBERATELY OMITTED. Weights: ``feglm`` has no ``weights`` argument in
        0.60.0, so card #83's "+ weights" clause cannot be honoured and is
        reported rather than approximated. Clustered, HAC and Driscoll-Kraay
        standard errors: no node argument reaches ``vcov``, so every standard
        error here is the ``iid`` default and the card's "SE clustered if a
        cluster was supplied" clause is unreachable through this contract. The
        small-sample correction is likewise the estimator's default; MEASURED on
        Dalal, Fowlkes and Hoadley's Model (3.2), it returns 3.063664 where the
        paper prints 3.052, and the difference is that correction. Marginal
        effects: the coefficients are on the link scale by design, per the card's
        first trap. The ``gaussian`` family the estimator also offers: forbidden
        by the node's enum, and that sentence was FALSE until the enum was gated
        here -- see ``link`` declared, below. Multi-model syntax: one node, one
        model.

        GATES ADDED, AND THE SOURCE OF EACH. ``link`` supplied -- the node spec
        declares the argument with no default while its description names one,
        and re-materialising a default the contract does not carry is forbidden.
        ``link`` declared -- the node spec's own enum, read out of ``NODE_META``
        rather than retyped, because the annotation is not the guard: beartype is
        a dev dependency installed by ``tests/conftest.py`` alone, so the shipped
        package enforced no ``Literal`` and the value went to
        ``feglm(family=...)`` as it stood. MEASURED with the hook absent,
        ``link='gaussian'`` fitted a LINEAR PROBABILITY MODEL and the class check
        below read the Fegaussian as the multi-response case, so the node told the
        caller to drop a multi-model operator from a formula that carries none.
        No missing or non-finite value -- the card's own ``data`` description,
        and the measured silent row drop above. At least three observations -- a
        measured ``ZeroDivisionError`` below that. ``fixef`` is a bare name and
        ``fixef`` names a real column -- the card's own ``fixef`` description,
        and the injection below. ``fixef`` and ``| col`` not both supplied -- the
        card does not say which wins. The COVARIATES AND THE INTERCEPT do not
        separate the outcome
        -- the next paragraph, and note the words: separation WITHIN a fixed effect
        is not asked about here and is the gap named on
        :func:`_separation_design`. The fit converged -- which therefore still
        covers a separated fixed effect as well as an iteration that ran out of
        steps, and the node exposes no limit to raise. The estimator's own
        refusals are translated rather than crashed on.

        SEPARATION IS REFUSED FROM THE DATA, AND THE CONVERGENCE FLAG CANNOT DO
        IT. This paragraph replaces a claim that was true only on the machine it
        was written on: "a separated fit returns coefficients near +-57 with
        ``convergence`` false". Reproduce with::

            import numpy as np, pandas as pd
            from pyfixest.estimation import feglm
            frame = pd.DataFrame({"x": [1., 2, 3, 4, 5, 6, 7, 8],
                                  "y": [0., 0, 0, 0, 1, 1, 1, 1]})
            for link in ("logit", "probit"):
                with np.errstate(divide="ignore", invalid="ignore"):
                    fit = feglm("y ~ x", frame, family=link)
                print(link, bool(fit.convergence), fit.deviance, dict(fit.coef()))

            logit False 0.019002321852144635 {'Intercept': -57.16580917955002,
                                              'x': 12.703513151011114}
            probit True 0.5033898356102827 {'Intercept': -15.752135995812294,
                                            'x': 3.5004746657360624}

        SO THE FLAG IS FALSE FOR ONE LINK AND TRUE FOR THE OTHER ON THE SAME
        EIGHT ROWS. The probit half is deterministic and is a fit that does not
        exist reported as one that does, p-values 0.149716 and 0.147083 attached.
        The logit half is a lottery: pyfixest stops the IWLS at
        ``|dev - dev_old| / (0.1 + |dev_old|) < 1e-8``
        (``pyfixest/estimation/models/feglm_.py`` 358-360, 426-440), separation
        stalls it on a plateau at deviance 0.019002321852144635 where that
        denominator is 0.119, and the flag therefore fires on a step smaller than
        1.19e-9 -- decided by the last bit of the linear algebra. numpy's wheel
        builds OpenBLAS ``DYNAMIC_ARCH``, so the GEMM kernel is chosen from the
        CPU at run time; perturbing the IWLS step by one ULP flips the flag to
        True in 21 of 25 perturbations of an unchanged frame. What is asked
        instead is Konis (2007) linear-programming feasibility over the design --
        objective 4.0 and margin 4.4444e-01 on those eight rows in all 25, 0.0 on
        every frame this engine's suite fits.
        :func:`~econflow_engine.gates.estimation.require_no_separation` carries
        the arithmetic and the measured tolerance.

        THE TWO GATES ON THE SPECIFICATION ARE A SECURITY BOUNDARY, and they
        exist because this body BUILDS a string that is then EVALUATED. MEASURED
        against pyfixest 0.60.0 and formulaic 1.2.2: ``fixef`` is kind ``string``,
        which carries no constraint at the argument boundary, and concatenating
        it after ``|`` put it through ``__fixed_effect__(<text>)`` into
        ``eval(compiled, {}, ...)`` with empty globals -- so ``__import__`` was
        reachable and a ``fixef`` of ``__import__("os").environ.__setitem__(...)``
        RAN. ``require_a_column`` did not stop it: the caller names a column with
        the payload. ``require_a_bare_name`` refuses anything that is not one
        identifier, and ``require_an_allowlisted_specification`` re-walks the
        ASSEMBLED string against the default-deny formula allowlist, which is the
        second of the two enforcements the c00 node documentation already
        declares. The second gate also means the multi-model refusal below is now
        reached only by a specification the allowlist admits, which ``sw()`` and
        ``csw()`` are not. IT IS STILL REACHED. MEASURED: ``incident + distress ~
        temperature`` is built only from ``+`` and ``~``, both on the allowlist,
        and returns a ``FixestMulti`` -- so the refusal is live and not a device
        kept for the ``isinstance`` narrowing alone.

        THE ESTIMATOR RUNS UNDER numpy's SHIPPED ERROR STATE. MEASURED: a probit
        fit over these data converges to finite coefficients while its IWLS takes
        ``log(0)`` on an intermediate, so under ``np.seterr(all="raise")`` a
        correct fit raises rather than returning. ``divide`` and ``invalid`` are
        relaxed around the call and nothing else is, so an overflow or an
        underflow is NOT SILENCED -- it raises. It does not reach the caller as a
        crash, though: it raises inside a ``try`` below, and neither of the two
        encloses arithmetic of this engine's own, so ``is_estimator_refusal``
        reads it as the estimator objecting and it is reported as a refusal
        carrying the class and the original text. MEASURED: numpy raises ``FloatingPointError``
        for an overflow under a raising error state, not ``OverflowError``, and
        both derive from ``ArithmeticError``. THAT IS WHY THE SEPARATION GATE SITS
        BETWEEN THE TWO BLOCKS RATHER THAN INSIDE EITHER: it is this engine's own
        linear-programming arithmetic, and a fault in it caught by either handler
        would be reported to the caller as the library's objection to their data.
        A likelihood the COVARIATES leave without a maximum is refused from the
        design before the estimator runs, so that case never depends on the
        caller's error state at all. A fixed effect that separates still reaches
        the estimator, by the gap named on :func:`_separation_design`.

        TWO PRIVATE ATTRIBUTES ARE READ, THERE IS NO PUBLIC ROUTE TO EITHER, AND
        THEY ARE ON DIFFERENT INDEX SPACES. ``_data.index`` holds the retained
        rows' positions IN THE FRAME THE CALLER SUPPLIED, while
        ``_Y_untransformed`` is the response of the retained rows only, already
        subset and aligned with ``_data`` -- ``resid()`` is the IWLS working
        residual and does not recover it. MEASURED on 0.60.0 with a singleton
        fixed effect at row 0 of 24: ``_data.index`` runs 1..23 and
        ``_Y_untransformed`` has length 23, so subscripting the second by the
        first is out of bounds wherever the dropped rows are not a trailing
        suffix. A public accessor for either would retire this note.
    """
    require_supplied(link, fn=_FN, arg="link", remedy=_LINK_REMEDY)
    # BEFORE THE ESTIMATOR SEES IT, because the estimator's account of an
    # undeclared link is about anything but the word the caller sent. MEASURED
    # with the beartype hook absent, on `incident ~ temperature`:
    # `link='gaussian'` fits a LINEAR PROBABILITY MODEL, and the Felogit/Feprobit
    # check below reads the Fegaussian it returns as the multi-response case --
    # so the node told a caller to "drop the multi-model operator from the
    # formula" over a formula that carries none. The other four spellings came
    # back as the estimator objecting to their data.
    require_a_declared_option(
        link, allowed=_options("link"), fn=_FN, arg="link", remedy=_LINK_REMEDY
    )
    require_min_length(data, minimum=_MIN_OBSERVATIONS, fn=_FN, arg="data")
    _usable_numbers(data)
    require_at_most_one_spelling(
        fn=_FN,
        first=("fixef", fixef is not None),
        second=("formula", "|" in formula),
        remedy=(
            "Name the fixed effect once: either after '|' inside the formula, or in "
            "fixef, and leave the other out."
        ),
    )
    if fixef is not None:
        # BEFORE `require_a_column`, because that gate is satisfied by a column
        # NAMED with the payload and column names are caller-supplied. See the
        # gate's own docstring for the measured evaluation path.
        require_a_bare_name(fixef, fn=_FN, arg="fixef")
        require_a_column(data, column=fixef, fn=_FN, arg="fixef")

    specification = formula if fixef is None else f"{formula} | {fixef}"
    # The allowlist walked `formula` at the argument boundary; it never saw the
    # string built here, which is the one the estimator parses.
    require_an_allowlisted_specification(specification, fn=_FN)
    # ITS OWN ``try``, AND NOT THE ESTIMATOR'S BELOW. Neither block encloses
    # arithmetic of this engine's own, which is what makes reading an
    # ``ArithmeticError`` out of either as the estimator objecting safe. This one
    # is not purely a library call -- `_separation_design` also copies the frame,
    # takes a column and compares a set -- but the only failure those reach is an
    # ``IndexError``, which ``is_estimator_refusal`` does not accept. The
    # separation gate itself sits BETWEEN the two blocks because it IS this
    # engine's arithmetic: inside either, a fault in it would be reported to the
    # caller as the library's objection to their data.
    try:
        separation = _separation_design(specification, data)
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error, fn=_FN, code="precondition-degenerate", remedy=_ESTIMATOR_REMEDY
        )
    if separation is not None:
        design, outcome = separation
        require_no_separation(
            design,
            response=outcome,
            fn=_FN,
            remedy=(
                "Drop the separating predictor, or pool the levels that separate. "
                "This is asked of the data rather than of the fit, so the answer "
                "does not depend on where an iteration stopped."
            ),
        )
    try:
        # THE ESTIMATOR IS RUN UNDER numpy's OWN ERROR STATE AND NOT UNDER THE
        # CALLER'S, for the two conditions its IWLS is written to expect. MEASURED
        # on pyfixest 0.60.0: a probit fit over the Challenger O-rings converges to
        # finite coefficients while taking log(0) on an intermediate, because the
        # normal CDF underflows in the tails; under np.seterr(all="raise") -- which
        # is how this engine's own suite runs -- that correct fit raises instead of
        # returning. Narrowed to the two states measured, so an overflow or an
        # underflow is not silenced; it raises, and the except below then reports
        # it as the estimator's refusal rather than letting it escape -- this
        # block encloses no arithmetic of this engine's own. A likelihood the
        # COVARIATES leave without a maximum never reaches here; one a fixed
        # effect leaves without a maximum still does, and comes back as a fit.
        with np.errstate(divide="ignore", invalid="ignore"):
            model = feglm(specification, data, family=str(link))
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error, fn=_FN, code="precondition-degenerate", remedy=_ESTIMATOR_REMEDY
        )
    if not isinstance(model, Felogit | Feprobit):
        # THE TWO CLASSES THE TWO ADMISSIBLE LINKS PRODUCE, measured on 0.60.0:
        # `family="logit"` returns a Felogit and `family="probit"` a Feprobit.
        # Anything else is the multi-model case -- `incident + distress ~
        # temperature` returns a FixestMulti, which carries no single fit at all.
        # That spelling and not `sw()`: the allowlist walk above refuses `sw()`,
        # and a multi-response formula is the route that survives it. The node
        # declares one model, so the collection is refused rather than sampled. Naming the two
        # concrete classes rather than their `Feols` base is also what gives the
        # type checkers `convergence` and a non-None `deviance`, which the base
        # does not declare.
        refuse_a_multi_model_fit(
            fn=_FN,
            produced=type(model).__name__,
            remedy=(
                "Drop the multi-model operator from the formula and call this node "
                "once per specification."
            ),
        )
    require_convergence(
        converged=bool(model.convergence),
        fn=_FN,
        estimator="iteratively reweighted least-squares",
        remedy=(
            "Separation has been ruled out ACROSS the sample but not WITHIN a fixed "
            "effect, so either is possible here: check whether a level of the "
            "grouping carries only one outcome, or whether a predictor splits the "
            "outcome inside every level. Otherwise rescale a predictor whose units "
            "are far larger than the others, or drop one that is nearly collinear "
            "with another. This node exposes no iteration limit to raise."
        ),
    )

    kept = [int(position) for position in model._data.index]  # noqa: SLF001 - see the note
    # NOT `[kept]`. MEASURED: the two attributes are on DIFFERENT index spaces --
    # `_data.index` holds positions into the frame the caller supplied, while
    # `_Y_untransformed` is already the retained response. Indexing one by the
    # other was in-bounds only while the dropped rows formed a trailing suffix.
    response = np.asarray(model._Y_untransformed).ravel()  # noqa: SLF001 - see the note
    probabilities = np.asarray(model.predict(type="response"), dtype=float)
    table = model.tidy()
    fixed_effects = model.FixestFormula.fixed_effects
    levels = 0 if fixed_effects is None else sum(len(group) for group in model.fixef().values())

    # `Feglm.__init__` writes `self.deviance = None` and the IWLS fills it in, so
    # both checkers read the attribute's type as `None`. The value is a float on
    # every fit that reached this line -- `require_convergence` above has already
    # refused the only state in which the iteration did not run -- and the ignore
    # is narrowed to that one library annotation.
    deviance = float(model.deviance)  # type: ignore[arg-type]
    loglik = -deviance / 2.0
    null_loglik = -_null_deviance(response) / 2.0
    parameters = len(table) + levels
    nobs = int(probabilities.size)

    return {
        "coefficients": {str(term): float(value) for term, value in model.coef().items()},
        "coeftable": pd.DataFrame(
            {
                "term": [str(term) for term in table.index],
                "estimate": table["Estimate"].to_numpy(dtype=float),
                "std_error": table["Std. Error"].to_numpy(dtype=float),
                "z_value": table["t value"].to_numpy(dtype=float),
                "p_value": table["Pr(>|t|)"].to_numpy(dtype=float),
            }
        ),
        "fitted_probabilities": probabilities,
        "obs_kept": [position + 1 for position in kept],
        "pseudo_r2": 1.0 - loglik / null_loglik,
        "loglik": loglik,
        "aic": 2.0 * parameters - 2.0 * loglik,
        "bic": parameters * math.log(nobs) - 2.0 * loglik,
        "deviance": deviance,
        "nobs": nobs,
        "link": str(link),
        "family": _FAMILY,
        "fixef_names": (
            [] if fixed_effects is None else [name.strip() for name in fixed_effects.split("+")]
        ),
    }
