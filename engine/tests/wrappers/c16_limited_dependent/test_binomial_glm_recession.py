# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the wrapper module ``binomial_glm_recession`` -- method card #83.

Scaffolded by ``python scripts/gen_wrappers.py --scaffold-tests binomial_glm_recession``; its home
is ``tests/wrappers/c16_limited_dependent/test_binomial_glm_recession.py``.

FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, C the oracle case and
D determinism.

EVERY FRAME BELOW IS BUILT IN THIS FILE FROM THE ORACLE FIXTURE OR FROM SMALL LITERALS, and no test
here reads a published number: the published comparison is the oracle case under
``tests/oracle/c16_limited_dependent/binomial_glm_recession/``, run by the conformance harness. What
this file asserts is the shape of the result, the refusals, and that two runs agree.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Any, Literal

import numpy as np
import pandas as pd
import pytest

from econflow_engine.chart_spec import assert_pure, chart_spec
from econflow_engine.errors import GateError
from econflow_engine.serialize import to_json, to_mcp
from econflow_engine.wrappers.c16_limited_dependent import (
    binomial_glm_recession as wrapper,
)

MODULE_FNS = ("run_binomial_fe_glm",)

FN = "run_binomial_fe_glm"
ENGINE_ROOT = Path(__file__).resolve().parents[3]

#: The environment variable the payload writes, and the payload that writes it.
#: This is a WORKING exploit against the body as it stood before the ``fixef``
#: gate, kept verbatim so the control asks the question the attacker asked.
INJECTION_MARKER = "EF_RCE"
INJECTION_PAYLOAD = (
    f'__import__("os").environ.__setitem__("{INJECTION_MARKER}","pwned") or era'
)

#: The card's own output field names, read off ``output_key_fields`` prose. The
#: node also declares them in ``node-specs.json``; :class:`TestStructure` asserts
#: the two agree rather than trusting either.
CARD_KEYS = frozenset(
    {
        "coefficients",
        "coeftable",
        "fitted_probabilities",
        "obs_kept",
        "pseudo_r2",
        "loglik",
        "aic",
        "bic",
        "deviance",
        "nobs",
        "link",
        "family",
        "fixef_names",
    }
)


def oring() -> pd.DataFrame:
    """The 138 Bernoulli rows of the oracle fixture, built through the real loader.

    NOT a second transcription. ``build_fixture`` is the same code path the oracle
    case takes, so a change to the dataset moves this file's inputs with it and a
    dataset that stops validating fails here too.
    """
    from tests.conformance.fixtures import build_fixture

    frame: pd.DataFrame = build_fixture("dalal_fowlkes_hoadley_1989_oring_field_joint")
    return frame


def era() -> pd.DataFrame:
    """The same 138 rows with a two-level grouping, for the fixed-effect calls.

    The split is at flight 12 and is chosen so BOTH levels carry an incident --
    four early and five late. A grouping whose levels are all-zero separates, and
    a separated fixed effect is the subject of its own test rather than a hazard
    to smuggle into these.
    """
    frame = oring()
    frame["era"] = ["early" if row // 6 < 12 else "late" for row in range(len(frame))]
    return frame


def small(*, ones: int = 3, rows: int = 8) -> pd.DataFrame:
    """A tiny well-separated-enough binary frame, for the boundary refusals."""
    x = [float(i) for i in range(rows)]
    y = [1.0 if i % 2 == 0 and i // 2 < ones else 0.0 for i in range(rows)]
    return pd.DataFrame({"x": x, "y": y})


def fitted() -> dict[str, Any]:
    """One passing call, used by several structural assertions."""
    return wrapper.run_binomial_fe_glm(
        formula="incident ~ temperature", data=oring(), link="logit"
    )


class TestGatesBlock:
    """Class A -- one passing and one refused input for every declared gate."""

    def test_a_supplied_link_passes_and_an_absent_one_is_refused(self) -> None:
        """GATE 1. ``link`` is optional in the spec and carries no default there."""
        assert fitted()["link"] == "logit"

        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(formula="incident ~ temperature", data=oring())
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert '"link" was not supplied' in str(refused.value)
        assert "probit" in str(refused.value) and "logit" in str(refused.value)

    def test_a_clean_frame_passes_and_a_missing_value_is_refused(self) -> None:
        """GATE 2. MEASURED: pyfixest drops the NaN row and records it NOWHERE.

        ``feglm`` on the 23 flights with one missing response returns ``_N`` 22
        with ``na_index`` empty, so the caller is handed a fit on a sample it
        cannot see. The frame is refused instead.
        """
        assert fitted()["nobs"] == 138

        holed = oring()
        holed.loc[holed.index[0], "temperature"] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature", data=holed, link="logit"
            )
        assert refused.value.detail_code == "precondition-missing"
        assert "1 missing" in str(refused.value)

    def test_a_finite_frame_passes_and_an_infinity_is_refused(self) -> None:
        """GATE 2, the other half. MEASURED: an infinite row is dropped behind a warning."""
        assert math.isfinite(fitted()["deviance"])

        infinite = oring()
        infinite.loc[infinite.index[0], "temperature"] = float("inf")
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature", data=infinite, link="logit"
            )
        assert refused.value.detail_code == "precondition-missing"
        assert "1 non-finite" in str(refused.value)

    def test_a_long_enough_frame_passes_and_two_rows_are_refused(self) -> None:
        """GATE 3. MEASURED: two observations raise ZeroDivisionError inside the IWLS."""
        assert wrapper.run_binomial_fe_glm(formula="y ~ x", data=small(), link="logit")

        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="y ~ x", data=small().iloc[:2], link="logit"
            )
        assert refused.value.detail_code == "precondition-sample-size"
        assert "2 observation(s)" in str(refused.value)

    def test_a_named_fixef_column_passes_and_an_absent_one_is_refused(self) -> None:
        """GATE 4. The card's own precondition: the column must exist in the data."""
        assert wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature", data=era(), link="logit", fixef="era"
        )["fixef_names"] == ["era"]

        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature",
                data=oring(),
                link="logit",
                fixef="not_a_column",
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "'not_a_column'" in str(refused.value)

    def test_a_bare_name_fixef_passes_and_an_executable_one_is_refused(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """GATE 4b. THE CONTROL FOR A LIVE INJECTION, and it is the SIDE EFFECT it asserts.

        MEASURED against pyfixest 0.60.0 / formulaic 1.2.2 before the gate
        existed: ``fixef`` was concatenated into the estimator specification,
        pyfixest split it on ``|`` and wrapped each fixed effect as
        ``__fixed_effect__(<text>)``, and formulaic evaluated that factor with
        ``eval(compiled, {}, ...)``. Empty globals means CPython injects
        ``__builtins__``, so the payload below ran and left ``EF_RCE`` set in the
        process environment. The call still ended in a ``ValueError``, which is
        why asserting that it raised proves nothing: the successful exploit
        raised too. What separates the two states is the marker.
        """
        monkeypatch.delenv(INJECTION_MARKER, raising=False)
        assert wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature", data=era(), link="logit", fixef="era"
        )["fixef_names"] == ["era"]

        frame = era()
        frame[INJECTION_PAYLOAD] = frame["era"]
        # THE MARKER CHECK IS IN A ``finally`` SO THAT IT, AND NOT THE EXCEPTION
        # TYPE, IS WHAT TURNS THIS RED. Against the ungated body the call raised
        # a ValueError out of pyfixest, which would escape ``pytest.raises`` and
        # end the test before any assertion about the side effect ran. Raised
        # from ``finally``, the marker's own message replaces it.
        try:
            with pytest.raises(GateError) as refused:
                wrapper.run_binomial_fe_glm(
                    formula="incident ~ temperature",
                    data=frame,
                    link="logit",
                    fixef=INJECTION_PAYLOAD,
                )
        finally:
            assert os.environ.get(INJECTION_MARKER) is None, (
                "THE PAYLOAD EXECUTED. Whatever the call ended with, the formula "
                "engine had already evaluated it -- an exception afterwards is "
                "not a refusal."
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "is not a plain column name" in str(refused.value)

    def test_one_spelling_of_the_fixed_effect_passes_and_two_are_refused(self) -> None:
        """GATE 5. ``fixef`` and the formula's ``| col`` are one specification."""
        assert wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature | era", data=era(), link="logit"
        )["fixef_names"] == ["era"]

        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature | era",
                data=era(),
                link="logit",
                fixef="era",
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "two spellings" in str(refused.value)

    @pytest.mark.parametrize("link", ["logit", "probit"])
    def test_an_estimable_frame_passes_and_a_separated_one_is_refused_on_both_links(
        self, link: Literal["probit", "logit"]
    ) -> None:
        """GATE 6. THE PREMISE THIS TEST USED TO CARRY WAS FALSE ON BOTH LINKS.

        It asserted that ``convergence`` detects separation, and quoted "perfect
        separation returns coefficients of about +-57". Neither half survives
        measurement.

        THE LOGIT HALF IS A LOTTERY. pyfixest 0.60.0 stops the IWLS at
        ``|dev - dev_old| / (0.1 + |dev_old|) < 1e-8``
        (``pyfixest/estimation/models/feglm_.py`` 358-360, 426-440). Under
        separation the iteration does not diverge -- it stalls on a plateau at
        deviance 0.019002321852144635, where that denominator is 0.119 and the
        flag therefore fires whenever a step moves the deviance by less than
        1.19e-9. Which side of that a run lands on is decided by the last bit of
        the linear algebra, and numpy's wheel builds OpenBLAS ``DYNAMIC_ARCH``,
        so the GEMM kernel is chosen from the CPU at run time and a heterogeneous
        runner fleet is a coin toss. Perturbing the IWLS step by ONE ULP flips
        the flag to True in 21 of 25 perturbations while the frame is unchanged.
        That is the observed CI failure: this assertion failed with DID NOT RAISE
        on a tree byte-identical to a run where it passed.

        THE PROBIT HALF NEEDS NO LOTTERY AND IS WRONG TODAY, EVERY TIME. The same
        eight rows under ``link='probit'`` return ``convergence`` True, deviance
        0.5033898356102827 and coefficients -15.752136 and 3.500475 carrying
        p-values 0.149716 and 0.147083 -- a maximum-likelihood estimate that does
        not exist, handed back as a valid fit with inference attached.

        WHAT REPLACES IT. The body now asks a question about the DATA before it
        fits: Konis (2007) linear-programming feasibility, which is 0 for every
        frame this suite fits and 4.4444e-01 for the eight rows below -- an
        objective of 4.0 against a largest row norm of 9 -- on both links and
        under all 25 perturbations. So this frame is still refused -- for the
        reason it is actually inadmissible, and on whichever kernel the runner
        picked.
        """
        assert wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature", data=oring(), link=link
        )["coefficients"]

        separated = pd.DataFrame(
            {
                "x": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
                "y": [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
            }
        )
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(formula="y ~ x", data=separated, link=link)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the design separates the outcome" in str(refused.value)
        assert "maximum-likelihood estimate does not exist" in str(refused.value)
        assert "'x'" in str(refused.value)
        # THE REFUSAL IS THIS ENGINE'S AND MUST NOT BE ATTRIBUTED TO THE LIBRARY.
        # ``GateError`` derives from ``ValueError``, so a gate call moved inside
        # either estimator ``try`` is read by ``is_estimator_refusal`` as pyfixest
        # objecting and comes back wrapped -- with this whole message quoted
        # inside it, so every assertion above still passes. This is the one that
        # does not.
        assert "the estimator refused these inputs" not in str(refused.value)

    @pytest.mark.parametrize(
        ("formula", "fixef"), [("y ~ x", "g"), ("y ~ x | g", None)]
    )
    def test_a_design_of_nothing_but_zeros_is_refused_rather_than_divided_by(
        self, formula: str, fixef: str | None
    ) -> None:
        """THE MARGIN'S DENOMINATOR IS THE LARGEST ROW NORM, AND IT CAN BE ZERO.

        A FIXED EFFECT IS WHAT MAKES THIS REACHABLE, and it is worth saying why
        rather than treating the ``fixef`` as decoration. MEASURED, the design the
        gate sees is ``matrix.independent``: ``y ~ x`` leaves it holding
        ['Intercept', 'x'] and ``y ~ x | g`` leaves it holding ['x'] alone,
        because the fixed effect absorbs the intercept. With ``x`` all zero the
        second is a matrix of nothing but zeros, its largest row norm is 0.0, and
        ``float(-programme.fun) / 0.0`` raised ``ZeroDivisionError: float division
        by zero`` -- which escapes the gateway, since ``mcp/make_tool.py`` turns a
        ``GateError`` into a refusal and lets every other exception out as a
        crash.

        AND IT WAS A REGRESSION, WHICH IS THE HALF THAT DECIDES HOW IT IS FIXED.
        MEASURED: the identical frame with ``x`` at 1e-320 rather than 0.0 was
        never a crash -- it reaches the estimator and comes back as the refusal
        below. So a working refusal was replaced by a crash, and restoring it is
        what this asserts: the gate declines to answer a question that has no
        answer, and pyfixest's own objection is translated as it always was.
        """
        zero = pd.DataFrame(
            {
                "y": [0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0],
                "x": [0.0] * 8,
                "g": ["a", "a", "b", "b", "a", "a", "b", "b"],
            }
        )
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula=formula, data=zero, link="logit", fixef=fixef
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(refused.value)
        assert "All variables are collinear" in str(refused.value)
        # The frame that was NEVER a crash, asserted beside the one that was, so
        # that a fix which merely swallows the zero shows up here as a difference
        # between the two.
        with pytest.raises(GateError) as tiny:
            wrapper.run_binomial_fe_glm(
                formula=formula, data=zero.assign(x=1e-320), link="logit", fixef=fixef
            )
        assert str(tiny.value) == str(refused.value)

    def test_a_near_collinear_design_is_fitted_rather_than_called_separated(self) -> None:
        """A SOLVER RESIDUAL IS NOT A FACT ABOUT THE CALLER'S DATA.

        HiGHS's default primal feasibility tolerance is 1e-7, so on this design it
        returned ``success`` True and ``status`` 0 at a point violating the
        programme's own constraints by -3.778144463950639e-09 on 46 of the 120
        rows, with an objective that divided out to a margin of 1.015745e-08 --
        above the threshold, so the node refused the call and told the caller
        their design separates the outcome.

        IT DOES NOT. MEASURED on this frame: 65 zeros and 55 ones, controls
        spanning ``a`` in [-2.251, 2.245] against cases in [-1.860, 1.795], and
        the fit below exists -- pyfixest 0.60.0 returns ``convergence`` True at
        Intercept -0.138024 and ``a`` 0.397434 once it drops ``b`` for
        multicollinearity. The refusal was a false statement about the frame
        standing in front of a fit that was there all along, which is why the
        coefficients are asserted here and not merely the absence of a raise.
        """
        rng = np.random.default_rng(159)
        rows = 120
        base = rng.normal(size=rows)
        frame = pd.DataFrame(
            {
                "y": (rng.random(rows) < 0.5).astype(float),
                "a": base,
                "b": base + rng.normal(scale=1e-9, size=rows),
            }
        )
        assert int((frame["y"] == 0.0).sum()) == 65
        assert int((frame["y"] == 1.0).sum()) == 55
        with pytest.warns(UserWarning, match="multicollinearity"):
            fitted = wrapper.run_binomial_fe_glm(
                formula="y ~ a + b", data=frame, link="logit"
            )
        assert fitted["coefficients"]["Intercept"] == pytest.approx(-0.13802399948033858)
        assert fitted["coefficients"]["a"] == pytest.approx(0.39743371919950254)
        # ``b`` is gone because pyfixest dropped it, not because anything here
        # refused it, and all 120 rows survive: the frame is estimable whole.
        assert "b" not in fitted["coefficients"]
        assert len(fitted["obs_kept"]) == rows

    def test_a_fixed_effect_level_that_never_varies_is_the_named_gap(self) -> None:
        """NOT A GATE. THE NAMED GAP, PINNED SO THAT CLOSING IT IS A VISIBLE DIFF.

        THIS TEST ASSERTED A REFUSAL UNTIL THE DESIGN WAS NARROWED TO THE
        COVARIATES, and it is written the other way round now rather than
        deleted. Expanding the fixed-effect levels into indicators is what
        reached this frame -- and the same expansion refused the ordinary
        high-dimensional panel ``fixef`` exists for, because a level whose
        outcome is constant is the ORDINARY case there: MEASURED, 25 of 100 firms
        at five years, and a margin of 2.7035e+01. The levels left the design,
        and this case left the gate's scope with them.

        WHAT HAPPENS INSTEAD, MEASURED against pyfixest 0.60.0: its own
        separation check removes the twelve rows of the level carrying no
        incident, behind ``UserWarning: 12 observations removed because of
        separation.``, fits the remaining 126 and returns ``convergence`` True.
        The estimate it hands back EXISTS -- the margin over those 126 rows is
        0.0 with the levels expanded and 0.0 without them -- so what is uncovered
        here is the SILENCE about the twelve rather than a fit with no maximum.
        The warning and the shortened ``obs_kept`` are the whole of what the
        caller is told, which is why both are asserted below.

        WHAT TURNS THIS RED, STATED PRECISELY, BECAUSE THE FIRST VERSION OF THIS
        SENTENCE WAS WRONG. Merely re-running the programme after the row
        dropping does NOT: MEASURED, the margin over the surviving 126 rows is
        0.0 with the levels expanded, so the gate would pass and every assertion
        below would stay green. What turns it red is refusing this frame BEFORE
        the drop, or reporting the twelve rows to the caller as something other
        than a warning -- which is what closing the gap actually means.
        """
        quiet = era()
        outcome = quiet["incident"].to_numpy()
        never = [row for row in range(len(quiet)) if outcome[row] == 0.0][:12]
        groups = ["main"] * len(quiet)
        for row in never:
            groups[row] = "quiet"
        quiet["grp"] = groups

        with pytest.warns(UserWarning, match="12 observations removed"):
            admitted = wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature | grp", data=quiet, link="logit"
            )
        assert admitted["nobs"] == 126
        assert len(admitted["obs_kept"]) == 126
        assert not {row + 1 for row in never} & set(admitted["obs_kept"])

    def test_a_fit_reporting_non_convergence_is_still_refused(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """GATE 6b. THE BLOCK SIDE OF ``require_convergence``, WHICH LOST ITS ONLY
        TEST WHEN THE SEPARATION GATE TOOK OVER THE FRAME THAT USED TO DRIVE IT.

        The old test drove this gate with the separated eight rows. Those are now
        refused earlier, by ``require_no_separation``, so nothing reached
        ``require_convergence``'s blocking branch any more while the gate stayed
        wired at the call site and listed among the node's gates. A gate with no
        block test is the failure mode this suite exists to prevent.

        WHAT IS SUBSTITUTED AND WHAT IS NOT. The estimator's flag is an INPUT to
        this node's logic, and it is the input that is replaced here -- with a
        real ``Felogit`` from a real fit, its ``convergence`` set to the value the
        gate is meant to act on. Nothing about pyfixest's behaviour is asserted;
        what is asserted is that this node refuses on that input, with the reason
        code, the detail code and the remedy it promises. Provoking the flag from
        data instead is what the whole change abandoned: it is a BLAS lottery,
        measured at 21 of 25 one-ULP perturbations.
        """
        from pyfixest.estimation import Felogit, Feprobit
        from pyfixest.estimation import feglm as real

        def stalled(*args: Any, **kwargs: Any) -> Any:
            model = real(*args, **kwargs)
            assert isinstance(model, Felogit | Feprobit)
            model.convergence = False
            return model

        monkeypatch.setattr(wrapper, "feglm", stalled)

        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature", data=oring(), link="logit"
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "did not converge" in str(refused.value)
        # THE REMEDY MUST NOT CLAIM SEPARATION IS RULED OUT. It is ruled out
        # across the sample and not within a fixed effect, and a message that
        # says otherwise sends a caller whose grouping separates off to rescale
        # a predictor. That sentence was live until the narrowing was reviewed.
        assert "not WITHIN a fixed effect" in str(refused.value)
        assert "check whether a level of the grouping carries only one outcome" in str(
            refused.value
        )
        assert "Separation has already been ruled out" not in str(refused.value)

    def test_an_all_one_level_is_the_same_gap_with_no_signal_at_all(self) -> None:
        """THE MIRROR OF THE TEST ABOVE, AND IT IS NOT SYMMETRIC.

        MEASURED against pyfixest 0.60.0: its separation check removes a level
        that is ALL-ZERO and KEEPS one that is ALL-ONE. Six incident rows given a
        level of their own score 7.3171e-02 with the indicators and 0.0 without
        them -- so the estimate does not exist -- and ``feglm`` keeps all 138
        rows, returns ``convergence`` True and raises NO WARNING.

        That is why this mirror is written out rather than folded into the test
        above. There, the caller at least gets a warning and a shortened
        ``obs_kept``; here they get neither, and the payload is indistinguishable
        from a sound fit. MEASURED on the panels the narrowing was justified by,
        the split is the ordinary one: 100 firms at five years carries ten
        all-zero levels and fifteen all-one, and after the drop the ten are gone
        and all fifteen remain.
        """
        always = era()
        outcome = always["incident"].to_numpy()
        incidents = [row for row in range(len(always)) if outcome[row] == 1.0][:6]
        groups = ["main"] * len(always)
        for row in incidents:
            groups[row] = "always"
        always["grp"] = groups

        admitted = wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature | grp", data=always, link="logit"
        )
        assert admitted["nobs"] == 138
        assert len(admitted["obs_kept"]) == 138

    def test_separation_inside_every_level_is_the_second_named_gap(self) -> None:
        """THE WORSE HALF OF THE GAP, AND NOT THE SAME CASE AS THE ONE ABOVE.

        A covariate can order the outcome WITHIN each level at a different cut
        per level, and then no single hyperplane orders the pooled sample. The
        eight rows below are cut at 0 inside level ``A`` and at 10 inside level
        ``B``: MEASURED, the programme scores 0.0 over the covariate and
        1.0256e-01 with the levels expanded, so the covariate-only design admits
        a frame whose unconditional maximum-likelihood estimate does not exist.

        WHAT COMES BACK IS THAT NON-EXISTENT ESTIMATE, REPORTED AS A FIT.
        MEASURED against pyfixest 0.60.0: ``convergence`` True, deviance
        6.016594756162403e-08, coefficient 19.697788 and a standard error of
        6795.277043 -- the deviance at the floor and the error four orders above
        the estimate are the signature, and neither is a refusal. Unlike the
        constant-outcome level above, pyfixest drops nothing here and warns about
        nothing.

        This is asserted as it stands rather than left to prose. Closing the gap
        turns it red, and the note it is pinned against says what closing it
        takes -- a complete row drop, which pyfixest's own is measurably not.
        """
        cut = pd.DataFrame(
            {
                "x": [-2.0, -1.0, 1.0, 2.0, 8.0, 9.0, 11.0, 12.0],
                "y": [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0],
                "g": ["A", "A", "A", "A", "B", "B", "B", "B"],
            }
        )
        admitted = wrapper.run_binomial_fe_glm(
            formula="y ~ x | g", data=cut, link="logit"
        )
        assert admitted["nobs"] == 8
        assert admitted["deviance"] < 1e-6
        assert admitted["coeftable"]["std_error"][0] > 1000.0

    def test_the_frame_the_caller_supplied_is_not_rewritten_by_the_call(self) -> None:
        """THE GATE READS THE FRAME AND MUST NOT REWRITE IT.

        MEASURED: ``feglm`` passes ``copy_data=True`` and never touches the
        caller's object, while ``create_model_matrix`` -- which the separation
        gate calls directly -- opens with
        ``data.reset_index(drop=True, inplace=True)``. Before the copy, a frame
        indexed 10..17 came back from this node indexed 0..7.
        """
        shifted = small()
        shifted.index = pd.RangeIndex(start=10, stop=18)
        expected = list(shifted.index)
        columns = list(shifted.columns)

        wrapper.run_binomial_fe_glm(formula="y ~ x", data=shifted, link="logit")

        assert list(shifted.index) == expected
        assert list(shifted.columns) == columns

    def test_a_formula_naming_the_wrappers_own_state_is_refused_not_resolved(self) -> None:
        """THE EVALUATION ENVIRONMENT IS PINNED EMPTY, AND IT DEFAULTS TO OPEN.

        ``create_model_matrix``'s ``context`` argument is a STACK FRAME OFFSET,
        not a namespace: ``capture_context(0)`` resolves to ``sys._getframe(3)``,
        which through a direct call is the CALLING function's frame and through
        ``feglm`` is a pyfixest-internal one. Its mapping is merged on the right,
        so it also shadows the estimator's own ``log``, ``i`` and
        ``__fixed_effect__``.

        MEASURED before ``context={}`` was pinned: ``y ~ specification`` and
        ``y ~ formulas`` resolved the gate helper's own locals as model factors
        and escaped this node as a raw ``TypeError`` -- on a body whose formula
        surface has already carried one live injection. The names below are the
        helper's parameters and locals; none of them is a column of the frame.
        """
        for leaked in ("specification", "data", "formulas"):
            with pytest.raises(GateError) as refused:
                wrapper.run_binomial_fe_glm(
                    formula=f"y ~ {leaked}", data=small(), link="logit"
                )
            assert refused.value.detail_code in {
                "precondition-degenerate",
                "precondition-domain",
            }, leaked
            assert "TypeError" not in str(refused.value), leaked

    def test_a_binary_response_passes_and_a_three_level_one_is_refused(self) -> None:
        """GATE 7. The estimator's own refusal, translated rather than crashed on."""
        assert fitted()["family"] == "binomial"

        three = small()
        three.loc[three.index[0], "y"] = 2.0
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(formula="y ~ x", data=three, link="logit")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(refused.value)

    def test_a_formula_naming_an_absent_column_is_refused_not_crashed_on(self) -> None:
        """GATE 7, the arm no ``ValueError`` reaches.

        MEASURED: formulaic raises ``FactorEvaluationError``, which derives from
        ``Exception`` and not from ``ValueError``, so a type-based catch misses
        it and the caller gets a traceback.
        """
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident ~ nosuchcolumn", data=oring(), link="logit"
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "FactorEvaluationError" in str(refused.value)

    def test_one_model_passes_and_a_multi_response_formula_is_refused(self) -> None:
        """GATE 8. The branch ``refuse_a_multi_model_fit`` guards, reached through the body.

        IT IS NOT DEAD CODE AND THE ROUTE IS NOT ``sw()``. The allowlist walk that
        now runs over the assembled specification refuses ``sw()`` and ``csw()``
        before the estimator sees them, which leaves this branch looking
        unreachable. MEASURED against pyfixest 0.60.0: ``incident + distress ~
        temperature`` is admitted by the allowlist -- ``+`` and ``~`` are on it --
        and returns a ``FixestMulti``, one fit per response. So the refusal is
        live, and this is the input that reaches it.
        """
        assert fitted()["nobs"] == 138

        several = oring()
        several["distress"] = [
            1.0 if temperature < 65.0 else 0.0 for temperature in several["temperature"]
        ]
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(
                formula="incident + distress ~ temperature", data=several, link="logit"
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-shape"
        assert "more than one model" in str(refused.value)
        assert "FixestMulti" in str(refused.value)
        assert "This node reports one model." in str(refused.value)

    def test_an_undeclared_argument_is_refused_before_the_body_runs(self) -> None:
        """The wire contract, not the body: ``extra="forbid"`` on the model."""
        model = wrapper.wire_model(FN)
        with pytest.raises(ValueError, match="unknown_argument") as refused:
            model.model_validate(
                {
                    "formula": "incident ~ temperature",
                    "data": "handle",
                    "unknown_argument": 1,
                }
            )
        assert "extra" in str(refused.value).lower()


class TestStructure:
    """Class B -- the shape of the result, and that the wire can carry it."""

    def test_the_result_carries_exactly_the_declared_output_keys(self) -> None:
        """EXACT in both directions, against the node's own declaration."""
        declared = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        record = next(n for n in declared["nodes"] if n["fn"] == FN)["output_keys"]
        assert record["status"] == "declared", record
        assert set(record["keys"]) == CARD_KEYS

        result = fitted()
        assert isinstance(result, dict)
        assert set(result) == CARD_KEYS

    def test_the_payload_walks_to_mcp_with_no_serialisation_stub(self) -> None:
        """A stub in the payload is a value the wire cannot carry."""
        payload = to_mcp(fitted())

        def stubs(value: object) -> list[str]:
            if isinstance(value, dict):
                if value.get("@mcp_serialized") is False:
                    return [str(value.get("@mcp_class"))]
                return [hit for item in value.values() for hit in stubs(item)]
            if isinstance(value, list):
                return [hit for item in value for hit in stubs(item)]
            return []

        assert stubs(payload) == []
        assert set(payload) == CARD_KEYS

    def test_the_payload_round_trips_through_to_json(self) -> None:
        """No NaN token, no Infinity token: what orjson writes, json.loads reads."""
        payload = to_mcp(fitted())
        blob = to_json(payload)
        assert "NaN" not in blob and "Infinity" not in blob
        assert json.loads(blob) == payload

    def test_the_node_registers_nothing_so_the_result_is_the_whole_answer(self) -> None:
        """The scaffold's register test, answered: card #83 declares no register."""
        assert wrapper.NODE_META[FN].register_field is None

    def test_the_fitted_probabilities_are_a_chart_this_engine_can_emit(self) -> None:
        """Card #83 declares ``chart_kind: line`` over the score it produces."""
        result = fitted()
        spec = chart_spec(
            pd.Series(result["fitted_probabilities"], name="fitted_probabilities")
        )
        assert spec is not None
        assert_pure(spec)
        assert spec["series"]

    def test_every_reported_field_describes_the_same_retained_sample(self) -> None:
        """The card's alignment trap, asserted rather than documented."""
        result = fitted()
        assert result["nobs"] == len(result["obs_kept"])
        assert result["nobs"] == len(result["fitted_probabilities"])
        assert result["obs_kept"] == list(range(1, 139))
        assert all(0.0 <= p <= 1.0 for p in result["fitted_probabilities"])
        assert result["coeftable"].shape == (2, 5)
        assert list(result["coeftable"].columns) == [
            "term",
            "estimate",
            "std_error",
            "z_value",
            "p_value",
        ]
        assert set(result["coefficients"]) == {"Intercept", "temperature"}

    @pytest.mark.parametrize("position", [0, 68, 137], ids=["first", "middle", "last"])
    def test_a_dropped_row_shortens_obs_kept_rather_than_the_report(
        self, position: int
    ) -> None:
        """MEASURED: a singleton fixed effect drops a row and ``na_index`` stays empty.

        ``obs_kept`` is therefore read off the retained frame's positional index,
        which is the ONE derivation that accounts for a singleton drop as well as
        for a separation drop.

        THE THREE POSITIONS ARE THE POINT AND ONLY ONE OF THEM USED TO BE HERE.
        With the anomaly on the LAST row the retained positions are ``0..136`` and
        any indexing of the 137-long retained response by them happens to be
        in-bounds, so a body that indexed one by the other passed. MEASURED on
        pyfixest 0.60.0: an anomaly anywhere else leaves ``max(_data.index)``
        at 137 against a response of length 137 and the body raised
        ``IndexError: index 137 is out of bounds for axis 0 with size 137`` --
        a bare crash on the ordinary panel case ``fixef`` exists for.
        """
        panel = oring()
        groups = ["a"] * 138
        groups[position] = "z"
        panel["grp"] = groups
        with pytest.warns(UserWarning, match="singleton"):
            result = wrapper.run_binomial_fe_glm(
                formula="incident ~ temperature | grp", data=panel, link="logit"
            )
        assert result["nobs"] == 137
        assert len(result["obs_kept"]) == 137
        assert position + 1 not in result["obs_kept"]
        assert len(result["fitted_probabilities"]) == 137

    def test_the_derived_fit_statistics_are_the_documented_arithmetic(self) -> None:
        """MEASURED: pyfixest 0.60.0 exposes none of these for a binary GLM.

        ``get_performance()`` returns ``None`` and the object carries no
        ``loglik``, ``aic`` or ``bic``, so all four are this engine's arithmetic
        over the deviance and are checked against their own definitions here.
        """
        result = fitted()
        assert result["loglik"] == pytest.approx(-result["deviance"] / 2.0)
        assert result["aic"] == pytest.approx(2.0 * 2 - 2.0 * result["loglik"])
        assert result["bic"] == pytest.approx(
            2 * math.log(result["nobs"]) - 2.0 * result["loglik"]
        )
        assert 0.0 < result["pseudo_r2"] < 1.0

    def test_the_probit_link_reaches_a_different_family_than_the_logit(self) -> None:
        """Both admissible links run, and they are not the same fit."""
        logit = fitted()
        probit = wrapper.run_binomial_fe_glm(
            formula="incident ~ temperature", data=oring(), link="probit"
        )
        assert probit["link"] == "probit"
        assert probit["coefficients"]["temperature"] != logit["coefficients"]["temperature"]


class TestOracleCase:
    """Class C -- a published number, its citation and its tolerance class."""

    def test_the_published_number_is_reproduced_within_its_tolerance(self) -> None:
        """The committed case, loaded and run through the conformance harness itself.

        NOT a second comparison written here: ``admissible_calls`` applies the
        four load-time rules and ``disagreement`` is the harness's own two-step
        comparison, so this test cannot be greener than the corpus gate is.
        """
        from tests.conformance.test_conformance import (
            admissible_calls,
            disagreement,
            run_call,
        )

        cases = [case for case in admissible_calls() if case.fn == FN]
        assert len(cases) == 1, [case.id for case in cases]
        case = cases[0]
        assert case.tolerance_class == "estimate-1e-4"

        state, payload = run_call(case)
        assert state == "succeeded", payload
        assert (
            disagreement(payload, case.expected, case.unchecked_keys, case.rtol, case.atol)
            is None
        )

        # THE CLASS IS NOT THE REPRODUCTION, and until this assertion existed only
        # the class was enforced. `estimate-1e-4` is named for what the PAPER
        # PRINTS -- four decimal places, so no tighter band can be claimed against
        # the page -- but what the engine actually achieves is two orders better,
        # and that was recorded in the fixture's notes where nothing could hold it.
        # MEASURED on the pinned libraries: Intercept 4.477813e-06, temperature
        # 1.009191e-05. The band below is twice the worse of the two, so an
        # ordinary library patch does not move it, while a reproduction decaying
        # towards the class's own 1e-4 does. Its worth is that the fixture's prose
        # had ALREADY drifted -- it claimed 8.7e-6 for a gap that measures
        # 1.009191e-05 -- which is what a number kept outside a gate does.
        for name, published in case.expected["coefficients"].items():
            relative = abs(payload["coefficients"][name] - published) / abs(published)
            assert relative < 2e-5, (name, published, payload["coefficients"][name], relative)


class TestDeterminism:
    """Class D -- identical inputs, identical bytes."""

    def test_two_identical_calls_serialise_to_identical_bytes(self) -> None:
        """``run_binomial_fe_glm`` is not in ``stochastic_unseeded_fns``; read that."""
        specs = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        assert FN not in specs["vocabulary"]["stochastic_unseeded_fns"]

        first = to_json(to_mcp(fitted()))
        second = to_json(to_mcp(fitted()))
        assert first == second
        assert len(first) > 0


def test_the_module_exports_every_function_its_cards_name() -> None:
    """The one assertion a scaffold can make truthfully before a body exists."""
    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]
    assert not missing, missing
