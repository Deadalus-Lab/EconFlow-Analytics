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

import numpy as np

# NOT `import pyfixest as pf`. `pyfixest.estimation.feglm` is re-exported on the
# package, and the package ALSO holds a submodule of the same name; pyright
# resolves the attribute to the module and reports the call as uncallable, where
# mypy resolves it to the function. Naming the function is what both agree on.
from pyfixest.estimation import Felogit, Feprobit, feglm

from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_multi_model_fit,
    refuse_estimator_failure,
    require_a_bare_name,
    require_a_column,
    require_an_allowlisted_specification,
    require_at_most_one_spelling,
    require_convergence,
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
        by the node's enum. Multi-model syntax: one node, one model.

        GATES ADDED, AND THE SOURCE OF EACH. ``link`` supplied -- the node spec
        declares the argument with no default while its description names one,
        and re-materialising a default the contract does not carry is forbidden.
        No missing or non-finite value -- the card's own ``data`` description,
        and the measured silent row drop above. At least three observations -- a
        measured ``ZeroDivisionError`` below that. ``fixef`` is a bare name and
        ``fixef`` names a real column -- the card's own ``fixef`` description,
        and the injection below. ``fixef`` and ``| col`` not both supplied -- the
        card does not say which wins. The fit converged -- a separated fit
        returns coefficients near +-57 with ``convergence`` false. The
        estimator's own refusals are translated rather than crashed on.

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
        crash, though: it raises inside the ``try`` below, and the only call in
        that block is the estimator's, so ``is_estimator_refusal`` reads it as the
        estimator objecting and it is reported as a refusal carrying the class and
        the original text. MEASURED: numpy raises ``FloatingPointError`` for an
        overflow under a raising error state, not ``OverflowError``, and both
        derive from ``ArithmeticError``. A likelihood with no maximum is refused
        through ``convergence`` rather than through an exception that depends on
        the caller's settings.

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
    require_supplied(
        link,
        fn=_FN,
        arg="link",
        remedy="Pass link='probit' for the Estrella-Mishkin specification, or link='logit'.",
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
        # block encloses no arithmetic of this engine's own. What the estimator does with a
        # genuinely degenerate likelihood is then visible where it belongs, in
        # `convergence`: the separated fit below returns False and is refused.
        with np.errstate(divide="ignore", invalid="ignore"):
            model = feglm(specification, data, family=str(link))
    except Exception as error:
        if not is_estimator_refusal(error):
            raise
        refuse_estimator_failure(
            error,
            fn=_FN,
            code="precondition-degenerate",
            remedy=(
                "The formula must name columns the data carries, and the variable on "
                "its left must be binary -- exactly two levels, coded 0 and 1."
            ),
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
            "This is what perfect or quasi-separation looks like: a predictor that "
            "splits the outcome leaves the likelihood without a maximum. Drop the "
            "separating predictor, or pool the levels that separate."
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
