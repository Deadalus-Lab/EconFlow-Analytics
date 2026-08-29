# SPDX-License-Identifier: AGPL-3.0-only
"""The thirteen estimator refusals, each with the input it passes and the one it blocks.

PAIRED THROUGHOUT, for the reason every gate suite in this package is paired: a
rule tested only on the input it refuses is indistinguishable from one that
refuses everything, and that rule reads as a working gate right up until somebody
tries to use the method.

:func:`~econflow_engine.gates.estimation.is_estimator_refusal` gets the most
attention here because it is the one function whose WRONG answer is silent. Read
one way it turns a defect in a wrapper into a polite refusal the caller cannot
act on; read the other it turns a documented precondition into a traceback. Both
directions are asserted, and the exception classes it is asked about are the real
ones raised by the installed pyfixest and formulaic rather than stand-ins.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from econflow_engine.errors import GateError
from econflow_engine.gates.estimation import (
    is_estimator_refusal,
    refuse_a_combination,
    refuse_a_multi_model_fit,
    refuse_estimator_failure,
    require_a_bare_name,
    require_a_column,
    require_an_aligned_index,
    require_an_allowlisted_specification,
    require_an_observed_value,
    require_at_most_one_spelling,
    require_convergence,
    require_counts,
    require_distinct_column_names,
    require_finite_estimates,
    require_strictly_inside,
    require_supplied,
)
from econflow_engine.gates.primitives import require_in_range

FRAME = pd.DataFrame({"spread": [1.0, 2.0], "recession": [0.0, 1.0]})


class TestRequireSupplied:
    """An optional argument the contract carries no default for."""

    def test_a_value_passes(self) -> None:
        """The pass side of the pair: a supplied value returns, it does not raise."""
        require_supplied("logit", fn="f", arg="link", remedy="Pass one.")

    def test_none_is_refused_and_the_message_names_the_argument_and_the_remedy(self) -> None:
        with pytest.raises(GateError) as refused:
            require_supplied(None, fn="f", arg="link", remedy="Pass link='logit'.")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert '"link" was not supplied' in str(refused.value)
        assert "Pass link='logit'." in str(refused.value)

    def test_a_falsy_value_that_is_not_none_passes(self) -> None:
        """0 and "" are values somebody chose; only ``None`` is an absence."""
        require_supplied(0, fn="f", arg="lag", remedy="-")
        require_supplied("", fn="f", arg="label", remedy="-")


class TestRequireAColumn:
    """A column name against the frame that is supposed to carry it."""

    def test_a_present_column_passes(self) -> None:
        """The pass side: a column the frame carries is not refused."""
        require_a_column(FRAME, column="spread", fn="f", arg="fixef")

    def test_an_absent_column_is_refused_and_the_message_lists_what_is_there(self) -> None:
        with pytest.raises(GateError) as refused:
            require_a_column(FRAME, column="year", fn="f", arg="fixef")
        assert refused.value.detail_code == "precondition-shape"
        assert "'year'" in str(refused.value)
        assert "['recession', 'spread']" in str(refused.value)


class TestRequireABareName:
    """A caller-supplied name that is about to be SPLICED into a formula string."""

    @pytest.mark.parametrize(
        "name", ["era", "unit", "Country", "x1", "gdp_growth", "_leading", "sigma"]
    )
    def test_a_plain_name_passes(self, name: str) -> None:
        """The pass side: every spelling a real column name takes is admissible."""
        require_a_bare_name(name, fn="f", arg="fixef")

    @pytest.mark.parametrize(
        "name",
        [
            '__import__("os").environ.__setitem__("EF_RCE","pwned") or unit',
            "unit)[a] or __import__('os').system('id')",
            "a + b",
            "a|b",
            "a.b",
            "a b",
            "",
            "1unit",
            "class",
            "lambda",
        ],
        ids=[
            "the-measured-payload",
            "a-factor-escape",
            "an-operator",
            "a-separator",
            "an-attribute-access",
            "a-space",
            "the-empty-string",
            "a-leading-digit",
            "a-keyword",
            "another-keyword",
        ],
    )
    def test_anything_that_is_not_a_plain_name_is_refused(self, name: str) -> None:
        with pytest.raises(GateError) as refused:
            require_a_bare_name(name, fn="f", arg="fixef")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert '"fixef"' in str(refused.value)
        assert "is not a plain column name" in str(refused.value)


class TestRequireAnAllowlistedSpecification:
    """The assembled estimator specification, re-walked against the formula allowlist."""

    @pytest.mark.parametrize(
        "specification",
        ["incident ~ temperature", "y ~ x | era", "y ~ log(x) + I(x^2) | year + firm"],
    )
    def test_a_specification_the_allowlist_admits_passes(self, specification: str) -> None:
        """The pass side, and it includes the ``|`` form the concatenation produces."""
        require_an_allowlisted_specification(specification, fn="f")

    @pytest.mark.parametrize(
        "specification",
        [
            'y ~ x | __import__("os").environ.__setitem__("EF_RCE","pwned") or unit',
            "y ~ system('rm -rf /')",
            "y ~ x; z ~ w",
            "y + x",
        ],
        ids=["the-measured-payload", "the-canonical-attack", "two-expressions", "no-tilde"],
    )
    def test_a_specification_outside_the_allowlist_is_refused(
        self, specification: str
    ) -> None:
        with pytest.raises(GateError) as refused:
            require_an_allowlisted_specification(specification, fn="f")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "the formula allowlist" in str(refused.value)

    def test_the_message_carries_the_allowlist_own_diagnosis(self) -> None:
        """The walk's reason is the only account of WHICH rule blocked the string."""
        with pytest.raises(GateError) as refused:
            require_an_allowlisted_specification("y ~ system('id')", fn="f")
        assert "system" in str(refused.value)


class TestRequireAtMostOneSpelling:
    """Two ways of saying one thing, supplied together."""

    @pytest.mark.parametrize(
        ("first", "second"), [(False, False), (True, False), (False, True)]
    )
    def test_fewer_than_two_pass(self, first: bool, second: bool) -> None:
        """Neither, or either alone, is a single specification and is admissible."""
        require_at_most_one_spelling(
            fn="f", first=("fixef", first), second=("formula", second), remedy="-"
        )

    def test_both_together_are_refused_and_both_names_appear(self) -> None:
        with pytest.raises(GateError) as refused:
            require_at_most_one_spelling(
                fn="f",
                first=("fixef", True),
                second=("formula", True),
                remedy="Name it once.",
            )
        assert refused.value.detail_code == "precondition-domain"
        assert '"fixef"' in str(refused.value) and '"formula"' in str(refused.value)
        assert "Name it once." in str(refused.value)


class TestRequireConvergence:
    """The flag an estimator sets beside numbers that look like an estimate."""

    def test_a_converged_fit_passes(self) -> None:
        """The pass side: a converged fit is reported, not refused."""
        require_convergence(converged=True, fn="f", estimator="IWLS", remedy="-")

    def test_a_fit_that_did_not_converge_is_refused(self) -> None:
        with pytest.raises(GateError) as refused:
            require_convergence(
                converged=False, fn="f", estimator="IWLS", remedy="Drop the predictor."
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "IWLS iteration did not converge" in str(refused.value)
        assert "Drop the predictor." in str(refused.value)


class TestRequireFiniteEstimates:
    """The numbers a fit came back with, asked about before they are reported.

    THE OTHER HALF OF :class:`TestRequireConvergence`. That flag says the
    iteration finished; this says what it finished with is a number. A payload
    field holding ``nan`` reaches the wire as ``null``, which is also how a field
    a method leaves empty ON PURPOSE reaches it -- so the two are
    indistinguishable to a caller unless one of them is refused.
    """

    def test_ordinary_numbers_pass(self) -> None:
        """The pass side: a coefficient vector and its log-likelihood are reported."""
        require_finite_estimates(
            pd.Series({"const": -7.919325, "smokes": 0.354536, "llf": -33.600153}),
            fn="f",
            quantity="coefficients and log-likelihood",
            remedy="-",
        )

    def test_a_nan_is_refused_and_every_term_carrying_one_is_named(self) -> None:
        with pytest.raises(GateError) as refused:
            require_finite_estimates(
                pd.Series({"const": float("nan"), "w": 1.0, "llf": float("nan")}),
                fn="f",
                quantity="coefficients and log-likelihood",
                remedy="Rescale the covariate.",
            )
        message = str(refused.value)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "coefficients and log-likelihood" in message
        assert "['const', 'llf']" in message
        assert "the first is nan" in message
        assert "Rescale the covariate." in message

    def test_an_infinity_is_refused_beside_a_nan(self) -> None:
        """Both reach the wire as the same ``null``, so both are the same defect."""
        with pytest.raises(GateError) as refused:
            require_finite_estimates(
                pd.Series({"v": 2.0, "w": float("inf")}),
                fn="f",
                quantity="rate ratios",
                remedy="-",
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "rate ratios" in str(refused.value)
        assert "['w']" in str(refused.value)
        assert "the first is inf" in str(refused.value)

    def test_a_label_the_vector_carries_twice_is_reported_once(self) -> None:
        """An estimator's parameter index is not a set; the message it produces is."""
        doubled = pd.Series([float("nan"), float("nan")], index=["zm_x1", "zm_x1"])
        with pytest.raises(GateError) as refused:
            require_finite_estimates(doubled, fn="f", quantity="coefficients", remedy="-")
        assert "['zm_x1']" in str(refused.value)


class TestIsEstimatorRefusal:
    """Which exceptions are the estimator objecting, and which are a defect here."""

    @pytest.mark.parametrize(
        "error",
        [
            ValueError("The dependent variable must be binary (0 or 1)."),
            ZeroDivisionError("division by zero"),
            FloatingPointError("divide by zero encountered in log"),
            OverflowError("math range error"),
            ArithmeticError("some other arithmetic failure"),
        ],
    )
    def test_the_type_based_arm_admits_what_was_measured(self, error: Exception) -> None:
        assert is_estimator_refusal(error)

    def test_an_overflow_is_admitted_and_the_class_it_arrives_as_is_measured(self) -> None:
        """THE READING THE WRAPPER DOCSTRINGS USED TO CONTRADICT, pinned here.

        The body's ``np.errstate`` note claimed an overflow "still reaches the
        caller". It does not: an overflow raised out of the estimator call is an
        ``ArithmeticError`` and this arm reads it as a refusal. Excluding
        ``OverflowError`` would not have changed that, and this asserts why --
        numpy raises ``FloatingPointError`` for an overflow under a raising error
        state, so ``OverflowError`` is not the class an overflow inside the IWLS
        arrives as.
        """
        with np.errstate(over="raise"), pytest.raises(FloatingPointError) as raised:
            np.float64(1e308) * np.float64(10.0)
        assert not isinstance(raised.value, OverflowError)
        assert isinstance(raised.value, ArithmeticError)
        assert is_estimator_refusal(raised.value)

    @pytest.mark.parametrize(
        ("formula", "expected_class"),
        [
            ("recession ~ nosuchcolumn", "FactorEvaluationError"),
            ("recession", "FormulaSyntaxError"),
        ],
        ids=["a-column-the-frame-lacks", "a-formula-with-no-tilde"],
    )
    def test_the_module_based_arm_admits_the_real_formula_engine_errors(
        self, formula: str, expected_class: str
    ) -> None:
        """PROVOKED, NOT NAMED. The classes are reached by making the library raise.

        Both derive from ``Exception`` and NOT from ``ValueError``, so the
        type-based arm cannot see them and only the module-based one can. They are
        raised here rather than imported for two reasons: the shipped module must
        not declare a dependency on ``formulaic``, and a class named in a test can
        drift out of the set the library actually raises without the test noticing.
        """
        import pyfixest as pf

        with pytest.raises(Exception) as raised:  # noqa: B017 - the class IS the subject
            pf.feglm(formula, FRAME, family="logit")

        error = raised.value
        assert type(error).__name__ == expected_class, type(error)
        assert not isinstance(error, ValueError | ArithmeticError), type(error)
        assert is_estimator_refusal(error)

    def test_the_module_based_arm_admits_a_real_statsmodels_error(self) -> None:
        """``statsmodels`` JOINED THE SET WITH THE SECOND 2.2 BODY AND WAS NEVER ASKED.

        The module arm was exercised against ``formulaic`` and ``pyfixest`` alone,
        so the third name in ``_ESTIMATOR_PACKAGES`` was a claim rather than a
        measurement. ``MissingDataError`` is raised by the CONSTRUCTOR, derives
        straight from ``Exception`` and is not a ``ValueError``, so the type-based
        arm cannot see it and only the module arm can. Provoked rather than named,
        for the reason the formula-engine classes are: a class named in a test can
        drift out of the set the library actually raises without the test noticing.
        """
        import statsmodels.api as sm

        holed = pd.Series([1.0, 2.0, float("nan"), 4.0])
        design = sm.add_constant(pd.Series([1.0, 2.0, 3.0, 4.0]))
        with pytest.raises(Exception) as raised:  # noqa: B017 - the class IS the subject
            sm.Poisson(holed, design, missing="raise")

        error = raised.value
        assert type(error).__name__ == "MissingDataError", type(error)
        assert type(error).__module__.split(".", 1)[0] == "statsmodels", type(error)
        assert not isinstance(error, ValueError | ArithmeticError), type(error)
        assert is_estimator_refusal(error)

    @pytest.mark.parametrize(
        "error",
        [
            AttributeError("'NoneType' object has no attribute 'coef'"),
            TypeError("unsupported operand type(s)"),
            KeyError("temperature"),
            RuntimeError("something in this engine went wrong"),
        ],
    )
    def test_a_defect_in_the_body_is_not_an_estimator_refusal(
        self, error: Exception
    ) -> None:
        """THE HALF THAT MATTERS. A wrapper's own bug must crash, not refuse politely."""
        assert not is_estimator_refusal(error)


class TestRefuseEstimatorFailure:
    """The translation, which always raises."""

    def test_it_carries_the_class_the_message_and_the_remedy(self) -> None:
        original = ValueError("The dependent variable must be binary (0 or 1).")
        with pytest.raises(GateError) as refused:
            refuse_estimator_failure(
                original, fn="f", code="precondition-degenerate", remedy="Recode it."
            )
        message = str(refused.value)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "ValueError" in message
        assert "must be binary (0 or 1)" in message
        assert "Recode it." in message

    def test_the_code_it_is_given_is_the_code_it_carries(self) -> None:
        with pytest.raises(GateError) as refused:
            refuse_estimator_failure(
                ValueError("x"), fn="f", code="precondition-shape", remedy="-"
            )
        assert refused.value.detail_code == "precondition-shape"


class TestRefuseAMultiModelFit:
    """The seventh refusal, which also always raises.

    THE PAIR IS SPLIT ACROSS TWO LEVELS BECAUSE THE FUNCTION IS ``NoReturn``.
    There is no input it returns on, so the pass half cannot live here: it is the
    ``isinstance`` guard at the call site, and it is asserted against a real fit
    in ``tests/wrappers/c16_limited_dependent/test_binomial_glm_recession.py``,
    where one single-model call passes and ``incident + distress ~ temperature``
    reaches this refusal through the estimator. What is asserted here is what the
    refusal CARRIES.
    """

    def test_it_names_the_collection_the_estimator_returned_and_the_remedy(self) -> None:
        with pytest.raises(GateError) as refused:
            refuse_a_multi_model_fit(
                fn="f", produced="FixestMulti", remedy="Call it once per specification."
            )
        message = str(refused.value)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-shape"
        assert "f: " in message
        assert "more than one model" in message
        assert "FixestMulti" in message
        assert "This node reports one model." in message
        assert "Call it once per specification." in message

    def test_the_class_it_is_given_is_the_class_it_reports(self) -> None:
        """The produced type is the caller's only account of WHAT came back."""
        with pytest.raises(GateError) as refused:
            refuse_a_multi_model_fit(fn="f", produced="FixestMultiEstimation", remedy="-")
        assert "FixestMultiEstimation" in str(refused.value)


class TestRequireCounts:
    """A response that is a count, at or above the floor the zero rule sets."""

    def test_whole_non_negative_numbers_pass(self) -> None:
        require_counts(pd.Series([0.0, 1.0, 7.0]), minimum=0, fn="f", arg="y", remedy="-")
        require_counts(pd.Series([3, 4, 5]), minimum=1, fn="f", arg="y", remedy="-")

    def test_a_fractional_value_is_refused_and_the_message_shows_it(self) -> None:
        with pytest.raises(GateError) as refused:
            require_counts(
                pd.Series([1.0, 2.5, 3.0]),
                minimum=0,
                fn="f",
                arg="y",
                remedy="Round the response, or fit a continuous model.",
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "not whole numbers" in str(refused.value)
        assert "2.5" in str(refused.value)
        assert "Round the response" in str(refused.value)

    def test_a_value_below_the_floor_is_refused(self) -> None:
        with pytest.raises(GateError) as refused:
            require_counts(pd.Series([2.0, -1.0]), minimum=0, fn="f", arg="y", remedy="-")
        assert refused.value.detail_code == "precondition-domain"
        assert "below 0" in str(refused.value)

    def test_the_floor_is_the_one_the_caller_names(self) -> None:
        """A zero-truncated model takes 1, and the same zero that passes at 0 fails."""
        require_counts(pd.Series([0.0, 2.0]), minimum=0, fn="f", arg="y", remedy="-")
        with pytest.raises(GateError) as refused:
            require_counts(pd.Series([0.0, 2.0]), minimum=1, fn="f", arg="y", remedy="-")
        assert "below 1" in str(refused.value)

    def test_a_missing_value_is_refused_before_integrality_is_asked_about(self) -> None:
        """``nan`` is not a whole number either, and that is not what is wrong with it."""
        with pytest.raises(GateError) as refused:
            require_counts(
                pd.Series([1.0, float("nan")]), minimum=0, fn="f", arg="y", remedy="-"
            )
        assert refused.value.detail_code == "precondition-missing"
        assert "1 missing" in str(refused.value)


class TestRequireStrictlyInside:
    """The OPEN interval, which the inclusive primitive cannot express."""

    def test_a_value_inside_passes(self) -> None:
        require_strictly_inside(0.95, low=0.0, high=1.0, fn="f", arg="conf_level")
        require_strictly_inside(
            pd.Series([1.0, 2.5]), low=0.0, high=float("inf"), fn="f", arg="exposure"
        )

    def test_an_endpoint_is_refused_where_require_in_range_would_admit_it(self) -> None:
        """THE WHOLE POINT OF THE PAIR: 1.0 is inside [0, 1] and outside (0, 1)."""
        require_in_range(1.0, low=0.0, high=1.0, fn="f", arg="conf_level")
        with pytest.raises(GateError) as refused:
            require_strictly_inside(1.0, low=0.0, high=1.0, fn="f", arg="conf_level")
        assert refused.value.detail_code == "precondition-domain"
        assert "open interval (0.0, 1.0)" in str(refused.value)
        assert '"conf_level" = 1.0' in str(refused.value)

    def test_a_vector_reports_how_many_values_broke_the_rule_and_the_first(self) -> None:
        with pytest.raises(GateError) as refused:
            require_strictly_inside(
                pd.Series([2.0, 0.0, -3.0]),
                low=0.0,
                high=float("inf"),
                fn="f",
                arg="exposure",
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "2 value(s) outside the open interval" in str(refused.value)
        assert "the first is 0.0" in str(refused.value)

    def test_a_missing_value_in_a_vector_is_refused_as_missing(self) -> None:
        with pytest.raises(GateError) as refused:
            require_strictly_inside(
                pd.Series([1.0, float("nan")]),
                low=0.0,
                high=float("inf"),
                fn="f",
                arg="exposure",
            )
        assert refused.value.detail_code == "precondition-missing"


class TestRequireAnObservedValue:
    """A model about a level, over a sample that carries none of it."""

    def test_a_sample_carrying_the_level_passes(self) -> None:
        require_an_observed_value(
            pd.Series([0.0, 3.0, 1.0]), level=0.0, fn="f", arg="y", remedy="-"
        )

    def test_a_sample_without_it_is_refused(self) -> None:
        with pytest.raises(GateError) as refused:
            require_an_observed_value(
                pd.Series([2.0, 3.0]),
                level=0.0,
                fn="f",
                arg="y",
                remedy="Fit zeros='none' instead.",
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "no value equal to 0" in str(refused.value)
        assert "Fit zeros='none' instead." in str(refused.value)


class TestRequireDistinctColumnNames:
    """Two columns under one name are one column in any payload keyed by name."""

    def test_distinct_names_pass(self) -> None:
        require_distinct_column_names(FRAME, fn="f", arg="design", remedy="-")

    def test_a_repeated_name_is_refused_and_is_named(self) -> None:
        doubled = pd.concat([FRAME, FRAME[["spread"]]], axis=1)
        with pytest.raises(GateError) as refused:
            require_distinct_column_names(
                doubled, fn="f", arg="design", remedy="Drop the duplicate column."
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "['spread'] more than once" in str(refused.value)
        assert "Drop the duplicate column." in str(refused.value)

    def test_every_repeated_name_is_reported_once(self) -> None:
        crowded = pd.concat([FRAME, FRAME], axis=1)
        with pytest.raises(GateError) as refused:
            require_distinct_column_names(crowded, fn="f", arg="design", remedy="-")
        assert "['recession', 'spread']" in str(refused.value)


class TestRequireAnAlignedIndex:
    """Labels, in order, because the estimator reads values and not labels."""

    def test_the_same_labels_in_the_same_order_pass(self) -> None:
        require_an_aligned_index(
            FRAME, reference=pd.Index([0, 1]), fn="f", arg="x", remedy="-"
        )
        require_an_aligned_index(
            pd.Series([1.0, 2.0]),
            reference=pd.Index([0, 1]),
            fn="f",
            arg="exposure",
            remedy="-",
        )

    def test_a_permutation_of_the_same_labels_is_refused(self) -> None:
        """THE CASE LENGTH CANNOT SEE, and the one that silently changes the fit."""
        reversed_labels = pd.Series([2.0, 1.0], index=pd.Index([1, 0]))
        with pytest.raises(GateError) as refused:
            require_an_aligned_index(
                reversed_labels,
                reference=pd.Index([0, 1]),
                fn="f",
                arg="exposure",
                remedy="Sort it by the response's index.",
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "not aligned with the response" in str(refused.value)
        assert "Sort it by the response's index." in str(refused.value)

    def test_a_different_length_is_refused_and_both_lengths_are_reported(self) -> None:
        with pytest.raises(GateError) as refused:
            require_an_aligned_index(
                pd.Series([1.0]),
                reference=pd.Index([0, 1]),
                fn="f",
                arg="exposure",
                remedy="-",
            )
        assert "1 label(s) against the response's 2" in str(refused.value)


class TestRefuseACombination:
    """A pair of arguments the reference implementation cannot honour.

    THE PAIR IS SPLIT ACROSS TWO LEVELS, as it is for the other ``NoReturn``
    refusal: there is no input this returns on, so the passing half is the ``if``
    at the call site and it is asserted against a real fit in
    ``tests/wrappers/c16_limited_dependent/test_count_models.py``, where a hurdle
    without an exposure runs and the same hurdle with one is refused here.
    """

    def test_it_names_the_combination_the_reason_and_the_remedy(self) -> None:
        with pytest.raises(GateError) as refused:
            refuse_a_combination(
                fn="f",
                combination="zeros='hurdle' with an exposure",
                reason="statsmodels 0.14.6 raises NotImplementedError for it.",
                remedy="Divide the response by the exposure, or drop the hurdle.",
            )
        message = str(refused.value)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "f: zeros='hurdle' with an exposure is not available." in message
        assert "statsmodels 0.14.6 raises NotImplementedError for it." in message
        assert "Divide the response by the exposure, or drop the hurdle." in message
