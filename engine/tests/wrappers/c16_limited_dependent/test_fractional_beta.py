# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the wrapper module ``fractional_beta`` -- method card #527.

Scaffolded by ``python scripts/gen_wrappers.py --scaffold-tests fractional_beta``; its home is
``tests/wrappers/c16_limited_dependent/test_fractional_beta.py``.

FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, C the oracle case and
D determinism.

THE DATA IS THE PUBLISHED TABLE AND NOTHING ELSE. Ferrari and Cribari-Neto's 38 food-expenditure
households live in ``tests/fixtures/ferrari_cribari_neto_2004_*`` and are reached through
``build_fixture``, which is the code path the oracle case takes -- so a change to either dataset
moves this file's inputs with it. Every input that needs a shape the published table does not have
is DERIVED from it by a stated transformation (a share moved onto a boundary, a covariate
rescaled), never drawn from a generator: the second body written in phase 2.2 published three
log-likelihoods measured against a synthetic sample whose generator then moved, and all three were
wrong by the time they were read.

TWO OF THE THREE MODELS THIS NODE DECLARES CAN BE FITTED, AND THE THIRD IS REFUSED.
``model='zero_one_inflated_beta'`` has no implementation anywhere in statsmodels 0.14.6 and no
primary source has been chosen for one, so the branch refuses; card #527's ``validation_notes``
records that decision and :class:`TestGatesBlock` asserts it.
"""

from __future__ import annotations

import json
import math
import os
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

from econflow_engine.errors import GateError
from econflow_engine.serialize import to_json, to_mcp
from econflow_engine.wrappers.c16_limited_dependent import (
    fractional_beta as wrapper,
)

MODULE_FNS = ("ld_fractional_response",)

FN = "ld_fractional_response"
ENGINE_ROOT = Path(__file__).resolve().parents[3]

#: The payload this node promises, read off card #527's ``output_key_fields``.
#: :class:`TestStructure` asserts that ``node-specs.json`` declares the same set rather
#: than trusting either copy.
CARD_KEYS = frozenset({"params", "marginal_effects", "precision", "boundary_share"})

#: The six numbers reported for every estimated mean-equation coefficient.
COEFFICIENT_FIELDS = frozenset(
    {"estimate", "std_error", "z_value", "p_value", "conf_low", "conf_high"}
)

#: The environment variable the payload writes, and the payload that writes it.
#: Both are the ones that RAN against the first 2.2 body before its formula gate,
#: kept verbatim so the control asks the question the attacker asked.
INJECTION_MARKER = "EF_RCE"
INJECTION_PAYLOAD = (
    f'__import__("os").environ.__setitem__("{INJECTION_MARKER}","pwned") or persons'
)

#: The optimiser noise statsmodels raises through ``warnings.warn``. The suite runs
#: under ``-W error``, so a test that means to reach this body's own convergence
#: refusal has to let the fit finish first.
_OPTIMISER_NOISE = (
    "ignore::statsmodels.tools.sm_exceptions.ConvergenceWarning",
    "ignore::statsmodels.tools.sm_exceptions.HessianInversionWarning",
)


def published() -> tuple[pd.Series, pd.DataFrame]:
    """The 38 published households, built through the real fixture loader.

    NOT a second transcription: ``build_fixture`` is the code path the oracle case
    takes, so a change to either dataset moves this file's inputs with it.
    """
    from tests.conformance.fixtures import build_fixture

    share: pd.Series = build_fixture("ferrari_cribari_neto_2004_food_share")
    covariates: pd.DataFrame = build_fixture(
        "ferrari_cribari_neto_2004_income_and_persons"
    )
    return share, covariates


def with_boundaries() -> pd.Series:
    """The published shares with the first moved to 0 and the last to 1.

    THE ONE SHAPE THE PUBLISHED TABLE CANNOT SUPPLY. Every household in it spends
    a strictly positive share of a strictly larger income, so no response is at a
    boundary -- and a boundary is exactly what separates the two estimators this
    node offers. The move is stated rather than generated: two named rows, two
    named values, and ``boundary_share`` is 2/38 by construction.
    """
    share, _ = published()
    moved = share.copy()
    moved.iloc[0] = 0.0
    moved.iloc[-1] = 1.0
    return moved


def fitted(**overrides: Any) -> dict[str, Any]:
    """One passing beta call on the published table, used by many assertions."""
    share, covariates = published()
    call: dict[str, Any] = {"y": share, "x": covariates, "model": "beta"}
    call.update(overrides)
    return wrapper.ld_fractional_response(**call)


def stubs_free(payload: object) -> bool:
    """No ``to_mcp`` refusal record anywhere in this payload."""
    if isinstance(payload, dict):
        if payload.get("@mcp_serialized") is False:
            return False
        return all(stubs_free(value) for value in payload.values())
    if isinstance(payload, list):
        return all(stubs_free(value) for value in payload)
    return True


class TestGatesBlock:
    """Class A -- one passing and one refused input for every declared gate."""

    def test_the_two_fitted_models_pass_and_the_inflated_beta_is_refused(self) -> None:
        """GATE 1. The enum carries a value with no estimator behind it anywhere.

        MEASURED: ``statsmodels.othermod.betareg`` on 0.14.6 exports ``BetaModel``,
        ``BetaResults`` and ``BetaResultsWrapper`` and nothing else, so there is no
        zero-or-one-inflated mixture to call. The enum value stays because the node
        signature is frozen; what it does here is refuse, because a branch quietly
        returning a plain beta fit under this name would be worse.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="fractional")

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share, x=covariates, model="zero_one_inflated_beta"
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "zero_one_inflated_beta" in str(refused.value)
        assert "statsmodels 0.14.6" in str(refused.value)

    def test_a_level_inside_the_unit_interval_passes_and_an_endpoint_is_refused(
        self,
    ) -> None:
        """GATE 2. MEASURED: ``conf_int(alpha=0.0)`` is an interval of -inf to inf.

        Both bounds reach this payload, and ``to_mcp`` renders an infinity as
        ``null``, so an endpoint would arrive as a confidence interval that is
        simply absent.
        """
        assert fitted(conf_level=0.5)["params"]["income"]["conf_low"] < 0.0

        with pytest.raises(GateError) as refused:
            fitted(conf_level=1.0)
        assert refused.value.detail_code == "precondition-domain"
        assert "open interval (0.0, 1.0)" in str(refused.value)

    def test_a_response_inside_the_unit_interval_passes_and_one_outside_is_refused(
        self,
    ) -> None:
        """GATE 3. MEASURED: the fractional branch fits an out-of-range response.

        ``GLM(y, X, family=Binomial()).fit()`` over the published shares with the
        first replaced by 1.4 returns ``llf = -17.215557434559905`` and emits
        NOTHING under ``warnings.simplefilter('always')``. A response of -0.3 does
        the same at ``llf = -15.03350281799101``. The quasi-likelihood is defined
        on the closed unit interval, and a share reported in percent is the way a
        caller reaches this by accident.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates)

        for bad in (1.4, -0.3):
            broken = share.copy()
            broken.iloc[0] = bad
            with pytest.raises(GateError) as refused:
                wrapper.ld_fractional_response(y=broken, x=covariates)
            assert refused.value.detail_code == "precondition-domain"
            assert "[0.0, 1.0]" in str(refused.value)
            assert "divide it by 100" in str(refused.value)

    def test_a_complete_response_passes_and_a_missing_one_is_refused(self) -> None:
        """GATE 4. MEASURED, and the two branches fail in two unusable ways.

        ``BetaModel`` handed a ``nan`` raises a bare ``AssertionError`` with an
        EMPTY message; the fractional branch raises ``ValueError: The first guess
        on the deviance function returned a nan.``. Neither says which argument
        was wrong, and the first is not even a class this engine reads as the
        estimator objecting.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        broken = share.copy()
        broken.iloc[2] = np.nan
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(y=broken, x=covariates, model="beta")
        assert refused.value.detail_code == "precondition-missing"

    @pytest.mark.parametrize("model", ["beta", "fractional"])
    def test_a_varying_response_passes_and_a_constant_one_is_refused(
        self, model: str
    ) -> None:
        """GATE 5. MEASURED: both branches answer a constant response with a number.

        ``BetaModel`` over 38 identical shares returns ``llf = 606.98046875`` --
        the precision parameter runs away, because a response with no spread is a
        beta density with infinite precision. The fractional branch is worse,
        because it does not even fail to converge: it reports ``converged`` true
        with slopes of -6.938893903907228e-18 and standard errors to match, behind
        a ``PerfectSeparationWarning`` that a caller outside this repository's
        ``-W error`` never sees.

        THE VALUE 0.3 IS THE POINT AND NOT AN ARBITRARY CHOICE. It is not a dyadic
        rational, so ``np.var(np.full(38, 0.3), ddof=1)`` is
        1.2659085472296641e-32 rather than zero, and the variance primitive
        admitted this vector until the exact ``min == max`` arm was added beside
        the variance one. At 0.5 the same 38 rows give exactly 0.0 and were always
        refused.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share,
            x=covariates,
            model=model,  # type: ignore[arg-type]
        )

        flat = pd.Series(np.full(len(share), 0.3), index=share.index, name="flat")
        assert float(np.var(np.asarray(flat), ddof=1)) > 0.0
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=flat,
                x=covariates,
                model=model,  # type: ignore[arg-type]
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "constant" in str(refused.value)

    def test_a_beta_fit_passes_inside_the_interval_and_is_refused_at_a_boundary(
        self,
    ) -> None:
        """GATE 6. THE MEASUREMENT THAT DECIDES THIS BODY'S SHAPE.

        Ferrari and Cribari-Neto's log-likelihood, their equation (7), is -infinity
        at ``y = 0`` and at ``y = 1``: the density is undefined there. MEASURED
        against statsmodels 0.14.6, ``BetaModel`` answers a boundary observation
        with a bare ``AssertionError`` carrying an EMPTY message, raised from
        ``assert np.all((0 < etmp) & (etmp < 1))``. ``AssertionError`` is neither a
        ``ValueError`` nor a class of the library's own, so
        :func:`~econflow_engine.gates.estimation.is_estimator_refusal` cannot see
        it and a body that wrapped only the estimator's own refusals would hand the
        caller a traceback with no message in it.

        The refusal names ``fractional``, because that is the whole reason the node
        offers two models.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=with_boundaries(), x=covariates, model="beta"
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "model='beta'" in str(refused.value)
        assert "model='fractional'" in str(refused.value)
        assert "2 observation(s) at exactly 0 or 1" in str(refused.value)

    def test_the_fractional_branch_admits_the_boundary_the_beta_branch_refuses(
        self,
    ) -> None:
        """GATE 6, the other half. Papke and Wooldridge's estimator is defined there.

        Their quasi-log-likelihood multiplies ``log G`` by ``y`` and ``log(1 - G)``
        by ``1 - y``, so a boundary observation contributes one of the two terms and
        never the logarithm of zero. This is the pair's whole point and it is
        asserted rather than described.
        """
        _, covariates = published()
        result = wrapper.ld_fractional_response(
            y=with_boundaries(), x=covariates, model="fractional"
        )
        assert result["boundary_share"] == pytest.approx(2.0 / 38.0)
        assert math.isfinite(result["params"]["income"]["estimate"])

    def test_precision_covariates_pass_on_a_beta_fit_and_are_refused_elsewhere(
        self,
    ) -> None:
        """GATE 7. Only a beta model has a precision parameter to model.

        The fractional branch is a quasi-likelihood with no second equation, so a
        precision design there is a request that would simply not be fitted.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share, x=covariates, model="beta", precision_covariates=["persons"]
        )["precision"]

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=covariates,
                model="fractional",
                precision_covariates=["persons"],
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "precision_covariates" in str(refused.value)

    def test_a_named_precision_covariate_passes_and_an_absent_one_is_refused(
        self,
    ) -> None:
        """GATE 8. MEASURED: an absent name reaches pandas as a ``KeyError``.

        ``design[['const', 'nope']]`` raises ``KeyError: "['nope'] not in index"``.
        ``KeyError`` derives from ``LookupError`` and not from ``ValueError``, so it
        is not a class the estimator translation recognises: unrefused, the caller
        gets a traceback.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share, x=covariates, model="beta", precision_covariates=["income"]
        )

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=covariates,
                model="beta",
                precision_covariates=["not_a_column"],
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "'not_a_column'" in str(refused.value)

    def test_distinct_precision_covariates_pass_and_a_repeated_one_is_refused(
        self,
    ) -> None:
        """GATE 9. A precision equation reported by name loses a repeated column."""
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share,
            x=covariates,
            model="beta",
            precision_covariates=["income"],
        )

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=covariates,
                model="beta",
                precision_covariates=["persons", "persons"],
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "precision_covariates" in str(refused.value)

    def test_a_long_enough_sample_passes_and_a_short_one_is_refused(self) -> None:
        """GATE 10. Counted over BOTH equations, because a beta fit estimates two."""
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share.iloc[:3], x=covariates.iloc[:3], model="beta"
            )
        assert refused.value.detail_code == "precondition-sample-size"
        assert "3 observation(s)" in str(refused.value)

    def test_an_aligned_design_passes_and_a_shifted_index_is_refused(self) -> None:
        """GATE 11. The estimator reads its arguments row by row, never by label."""
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        shifted = covariates.copy()
        shifted.index = shifted.index + 1
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(y=share, x=shifted, model="beta")
        assert refused.value.detail_code == "precondition-shape"
        assert "not aligned with the response" in str(refused.value)

    def test_a_complete_design_passes_and_a_missing_covariate_is_refused(self) -> None:
        """GATE 12. statsmodels reports this as ``exog contains inf or nans``."""
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        broken = covariates.copy()
        broken.iloc[4, 0] = np.nan
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(y=share, x=broken, model="beta")
        assert refused.value.detail_code == "precondition-missing"
        assert 'x["income"]' in str(refused.value)

    def test_a_design_without_an_intercept_passes_and_one_carrying_const_is_refused(
        self,
    ) -> None:
        """GATE 13. This node adds the intercept, so a covariate of that name collides."""
        share, covariates = published()
        assert set(wrapper.ld_fractional_response(y=share, x=covariates)["params"]) == {
            "const",
            "income",
            "persons",
        }

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share, x=covariates.assign(const=1.0), model="beta"
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "['const'] more than once" in str(refused.value)

    def test_a_full_rank_design_passes_and_a_collinear_one_is_refused(self) -> None:
        """GATE 14. MEASURED: ``BetaModel`` fits a collinear design in SILENCE.

        The published design with ``income`` repeated at twice its scale returns
        ``llf = 45.333509321237926`` against the identified fit's
        ``45.33350932122192`` -- the same number to eleven digits, beside a
        coefficient vector one column longer that no data identifies.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=covariates.assign(twice=covariates["income"] * 2.0),
                model="beta",
            )
        assert refused.value.detail_code == "precondition-rank"
        assert "rank 3 over 4 column(s)" in str(refused.value)

    def test_a_rank_deficient_precision_design_is_unreachable_by_construction(
        self,
    ) -> None:
        """GATE 15's ABSENCE, ASSERTED RATHER THAN ASSUMED.

        A rank-deficient precision design IS fitted in silence by statsmodels
        0.14.6, so the missing rule looks like a hole. It is not reachable through
        this node: the precision design is the intercept plus a SUBSET of the
        columns of a mean design already proven full rank, and a subset of a
        linearly independent set is linearly independent. The only way to repeat a
        column is to name it twice, which the rule above refuses first. This asserts
        the premise -- the collinear frame never gets past the MEAN design's rank
        rule, whatever the precision selection says.
        """
        share, covariates = published()
        widened = covariates.assign(twice=covariates["income"] * 2.0)
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=widened,
                model="beta",
                precision_covariates=["income", "twice"],
            )
        assert refused.value.detail_code == "precondition-rank"
        assert "x plus the intercept" in str(refused.value)

    @pytest.mark.filterwarnings(*_OPTIMISER_NOISE)
    def test_a_converged_fit_passes_and_one_that_gave_up_is_refused(self) -> None:
        """GATE 16. MEASURED: ``income`` rescaled by 1e6 stops the beta optimiser.

        It returns ``converged`` false with a coefficient vector shaped exactly like
        an estimate. The two optimiser warnings are silenced on THIS test alone so
        that the body's own refusal is what fires; under the suite's ``-W error``
        the first warning would otherwise be raised inside the fit and reported as
        the estimator's.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(y=share, x=covariates, model="beta")

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share,
                x=covariates.assign(income=covariates["income"] * 1e6),
                model="beta",
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "did not converge" in str(refused.value)

    def test_a_fit_that_reported_numbers_passes_and_one_that_did_not_is_refused(
        self,
    ) -> None:
        """GATE 17. MEASURED: a converged fit whose standard errors are not numbers.

        A fourth covariate equal to ``1 + 1e-10 * row`` is the intercept in all but
        the tenth decimal. ``np.linalg.matrix_rank`` admits the design -- 4 of 4 --
        so the rank rule does not fire; the fractional branch then reports
        ``converged`` true with finite coefficients, standard errors that are not
        numbers, AND NO WARNING AT ALL. ``to_mcp`` renders a ``nan`` and an ``inf``
        alike as ``null`` and ``to_json`` writes no ``NaN`` token, so the payload
        would be well-formed JSON whose inference is simply absent -- and this
        card's ``precision`` field is null ON PURPOSE on the fractional branch, so
        nothing would distinguish the two.

        AT 1e-6 THE SAME COLUMN IS HARMLESS and at 1e-14 the rank rule catches it,
        which is how narrow the band is between the two rules.
        """
        share, covariates = published()
        assert math.isfinite(fitted()["params"]["income"]["std_error"])

        shadow = covariates.assign(
            flatish=1.0 + 1e-10 * np.arange(float(len(covariates)))
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(y=share, x=shadow, model="fractional")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "are not numbers" in str(refused.value)
        assert "the std_error of" in str(refused.value)

    def test_the_estimator_s_own_refusal_is_translated_rather_than_crashed_on(
        self,
    ) -> None:
        """GATE 18. A perfectly separated response raises out of the fit.

        MEASURED: a binary response equal to ``income > 60`` is fitted by the
        fractional branch under a ``PerfectSeparationWarning``, and the suite's
        ``-W error`` turns that warning into an exception raised from inside the
        estimator. It is defined in ``statsmodels.tools.sm_exceptions``, so
        :func:`~econflow_engine.gates.estimation.is_estimator_refusal` recognises it
        by module and it reaches the caller as a refusal rather than a traceback.
        """
        share, covariates = published()
        separated = pd.Series(
            (np.asarray(covariates["income"]) > 60.0).astype(float),
            index=share.index,
            name="separated",
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=separated, x=covariates, model="fractional"
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(refused.value)

    @pytest.mark.parametrize("link", ["logit", "probit", "cloglog", "loglog"])
    def test_a_separated_response_refuses_on_every_link_and_never_crashes(
        self, link: str
    ) -> None:
        """GATE 19. THE ONE A SECURITY REVIEW HAD TO FIND, AND IT WAS A CRASH.

        ``make_tool`` turns a ``GateError`` into a clean refusal and lets every
        other exception escape as a crash, so a body has one job at its boundary:
        never raise anything else. MEASURED under ``np.seterr(all='raise')``, which
        is how this suite runs: a perfectly separated response on the fractional
        branch under ``cloglog`` and under ``loglog`` raised ``FloatingPointError:
        underflow encountered in exp`` from ``_the_marginal_effects``, out of
        ``links.py``'s ``1 - np.exp(-np.exp(z))``, and left this node as a
        traceback. ``fittedvalues`` is computed LAZILY, so the estimator's own
        arithmetic runs at the point of access and under the caller's error state
        -- the same trap the statistics read had already been fixed for, and not
        carried across to its sibling.

        THE PARAMETRISATION IS THE POINT: two of the four links crashed and two did
        not, so a single-link test would have gone green over it.
        """
        share, covariates = published()
        separated = pd.Series(
            (np.asarray(covariates["income"]) > 60.0).astype(float),
            index=share.index,
            name="separated",
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=separated,
                x=covariates,
                model="fractional",
                link=link,  # type: ignore[arg-type]
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"

    def test_a_covariate_in_both_equations_keeps_both_of_its_numbers(self) -> None:
        """GATE 20's FIRST HALF, and the defect a review found in its second.

        The two mappings this rule reads are BOTH keyed by covariate name --
        ``marginal_effects`` by the columns of ``x``, ``precision`` by the
        intercept plus a subset of those same columns -- so the rule assembled them
        into one mapping with a plain update, and every precision covariate
        overwrote its own marginal effect before the rule could read it. MEASURED
        with one covariate in both equations: the rule saw
        ``{'persons': -0.467, 'const': 5.182}`` and checked NO marginal effect at
        all, in the gate whose whole purpose is to refuse a silent null.

        This asserts the payload keeps both numbers; the next test asserts the rule
        now sees both.
        """
        share, covariates = published()
        result = wrapper.ld_fractional_response(
            y=share,
            x=covariates[["persons"]],
            model="beta",
            precision_covariates=["persons"],
        )
        assert set(result["marginal_effects"]) == {"persons"}
        assert set(result["precision"]) == {"const", "persons"}
        assert math.isfinite(result["marginal_effects"]["persons"])
        assert result["marginal_effects"]["persons"] != result["precision"]["persons"]

    def test_a_derived_number_that_is_not_a_number_is_refused_and_named(self) -> None:
        """GATE 20's SECOND HALF, ASSERTED AT THE SEAM, AND WHY IT IS ASSERTED THERE.

        NO INPUT WAS FOUND THAT REACHES THIS RULE THROUGH THE BODY, and the search
        is recorded rather than the conclusion assumed. The marginal-effect slope
        is the sample mean of the inverse link's derivative, which is bounded: even
        where the fit drives a fitted value to exactly 0 or 1 -- measured, 35 of 38
        under ``cloglog`` on a perfectly separated response -- the derivative comes
        back infinite and its reciprocal is a finite zero, so the slope stays
        finite. The other derived number is ``exp`` of the log-precision, and no
        response was found that drives that past 709: the optimiser reports failure
        long before, and the convergence rule refuses it there.

        So the rule is exercised on the mapping the body actually builds, with the
        label it actually writes. That label is the assertion: before the fix above
        a ``nan`` marginal effect on a covariate that also sits in the precision
        equation was not merely unnamed, it was absent.
        """
        from econflow_engine.gates.estimation import require_finite_estimates

        derived = pd.Series(
            {
                "the marginal effect of persons": float("nan"),
                "the precision coefficient on const": 5.182181524956077,
                "the precision coefficient on persons": -0.4670852826063419,
            }
        )
        with pytest.raises(GateError) as refused:
            require_finite_estimates(
                derived, fn=FN, quantity="marginal effects and precision", remedy="-"
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the marginal effect of persons" in str(refused.value)

    def test_a_covariate_name_carrying_a_payload_is_selected_and_never_evaluated(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """THE CONTROL FOR THE ONE ARGUMENT THAT CARRIES CALLER-CHOSEN TEXT ONWARD.

        ``precision_covariates`` is kind ``series_codes``, which ``kinds.py`` types
        as ``list[str]`` with no constraint on the contents, and this body puts it
        into a pandas column selection. The first 2.2 body shipped a live remote
        code execution through an argument of kind ``string`` spliced into a
        formula, so the question is asked here rather than assumed: the payload
        below is the one that ran in that body, and a column selection must merely
        FIND it. The marker is asserted in a ``finally`` so that it, and not the
        exception type, is what turns this red.
        """
        monkeypatch.delenv(INJECTION_MARKER, raising=False)
        share, covariates = published()
        # Squared rather than copied: a copy of a column is a linear combination of
        # the design and the rank gate refuses it before the name is ever used.
        frame = covariates.assign(**{INJECTION_PAYLOAD: covariates["persons"] ** 2})
        try:
            result = wrapper.ld_fractional_response(
                y=share,
                x=frame,
                model="beta",
                precision_covariates=[INJECTION_PAYLOAD],
            )
        finally:
            assert os.environ.get(INJECTION_MARKER) is None, (
                "THE PAYLOAD EXECUTED. A column name reached something that "
                "evaluates it, and this node's contract says nothing here does."
            )
        assert INJECTION_PAYLOAD in result["precision"]
        assert INJECTION_PAYLOAD in result["params"]

    def test_an_undeclared_argument_is_refused_before_the_body_runs(self) -> None:
        """The wire contract, not the body: ``extra="forbid"`` on the model."""
        model = wrapper.wire_model(FN)
        with pytest.raises(ValueError, match="unknown_argument") as refused:
            model.model_validate({"y": "handle", "x": "handle", "unknown_argument": 1})
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
        assert stubs_free(payload)
        assert set(payload) == CARD_KEYS

    def test_the_payload_round_trips_through_to_json(self) -> None:
        """No NaN token, no Infinity token: what orjson writes, json.loads reads."""
        payload = to_mcp(fitted())
        blob = to_json(payload)
        assert "NaN" not in blob and "Infinity" not in blob
        assert json.loads(blob) == payload

    def test_the_registered_object_is_the_whole_serialisable_result(self) -> None:
        """Card #527 registers under ``fit``, and the registry holds what is returned.

        THE FITTED OBJECT IS DELIBERATELY NOT IN IT. ``registry_put`` stores the
        return value whole, and ``tests/controls/double_run.py`` refuses a payload
        carrying a ``to_mcp`` refusal record -- so a live results object here would
        take this node out of the determinism gate altogether.
        """
        assert wrapper.NODE_META[FN].register_field == "fit"
        result = fitted()
        assert all(
            not hasattr(value, "mle_retvals") for value in result.values()
        ), sorted(result)

    def test_every_coefficient_carries_its_own_inference(self) -> None:
        """``params`` is keyed by term and each term carries the same six numbers."""
        result = fitted()
        assert set(result["params"]) == {"const", "income", "persons"}
        for term, record in result["params"].items():
            assert set(record) == COEFFICIENT_FIELDS, term
            assert record["conf_low"] < record["estimate"] < record["conf_high"]
            assert record["z_value"] == pytest.approx(
                record["estimate"] / record["std_error"]
            )

    def test_the_marginal_effects_are_the_library_s_own_on_every_link(self) -> None:
        """THE SEAM BETWEEN THE LIBRARY AND THE PAPER, ASSERTED AT ITS JOIN.

        ``BetaResults`` has no ``get_margeff`` -- ``hasattr`` is False on 0.14.6 --
        so the beta branch's proportion-scale effects are this engine's own
        arithmetic: the sample mean of the inverse link's derivative times the
        coefficient. The fractional branch's results object DOES carry
        ``get_margeff``, and this asserts the two agree on all four links, so the
        arithmetic used where the library offers nothing is the arithmetic the
        library performs where it does.
        """
        import statsmodels.api as sm
        from statsmodels.genmod.families import links as link_classes

        share, covariates = published()
        design = pd.concat(
            [pd.Series(1.0, index=share.index, name="const"), covariates], axis=1
        )
        for name, link in (
            ("logit", link_classes.Logit),
            ("probit", link_classes.Probit),
            ("cloglog", link_classes.CLogLog),
            ("loglog", link_classes.LogLog),
        ):
            ours = wrapper.ld_fractional_response(
                y=share,
                x=covariates,
                model="fractional",
                link=name,  # type: ignore[arg-type]
            )["marginal_effects"]
            library = sm.GLM(
                share, design, family=sm.families.Binomial(link=link())
            ).fit(cov_type="HC0").get_margeff(at="overall", method="dydx")
            assert list(ours) == ["income", "persons"], name
            for term, value in zip(
                library.summary_frame().index, library.margeff, strict=True
            ):
                assert ours[str(term)] == pytest.approx(float(value), rel=1e-12), name

    def test_the_intercept_carries_a_coefficient_and_no_marginal_effect(self) -> None:
        """A derivative with respect to a column of ones is not a quantity."""
        result = fitted()
        assert "const" in result["params"]
        assert "const" not in result["marginal_effects"]
        assert set(result["marginal_effects"]) == {"income", "persons"}

    def test_the_precision_is_a_number_for_beta_and_empty_for_a_fractional_fit(
        self,
    ) -> None:
        """``precision`` is the beta parameter, and the quasi-likelihood has none.

        Reporting a number where none was estimated would be reporting a fitted
        value nobody fitted, so the field is present and empty instead -- which is
        what RULE 5 of the oracle harness requires, the key set being the same on
        every branch.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share, x=covariates, model="fractional"
        )["precision"] is None
        assert fitted()["precision"] == pytest.approx(35.60973310373236, rel=1e-9)

    def test_a_precision_design_reports_its_equation_rather_than_one_number(
        self,
    ) -> None:
        """Where the precision VARIES it is not one number, and the payload says so.

        With ``persons`` in the precision equation the fitted precision differs row
        by row -- MEASURED, 151.53, 21.90 and 57.61 for the first three households
        -- so the field carries the equation that produces it, on the log scale the
        estimator fits it through, keyed by the design's own column names.
        """
        share, covariates = published()
        result = wrapper.ld_fractional_response(
            y=share, x=covariates, model="beta", precision_covariates=["persons"]
        )
        assert set(result["precision"]) == {"const", "persons"}
        assert result["precision"]["const"] == pytest.approx(5.5043097066207, rel=1e-6)
        assert result["precision"]["persons"] == pytest.approx(
            -0.4835233243008437, rel=1e-6
        )
        assert set(result["params"]) == {"const", "income", "persons"}

    def test_a_precision_covariate_named_after_the_estimator_s_prefix_keeps_its_name(
        self,
    ) -> None:
        """A COEFFICIENT THAT WENT MISSING, found by a security review.

        The precision mapping used to strip the estimator's ``precision-`` prefix
        from these labels. That was wrong on both sides: the labels here are the
        CALLER'S column names and never carry the prefix -- MEASURED,
        ``fit.params.index`` for caller columns ``const``, ``a`` and
        ``precision-a`` reads ``precision-const``, ``precision-a``,
        ``precision-precision-a``, so the prefix is on the estimator's OWN index
        -- and the strip therefore fired only on a name the caller chose. A design
        carrying ``a`` beside ``precision-a`` came back with a precision mapping of
        TWO keys where three coefficients had been estimated, the stripped name
        silently replacing the real one. That is the defect
        ``require_distinct_column_names`` exists to prevent, reintroduced in the
        payload after that gate had already passed.
        """
        share, covariates = published()
        colliding = pd.DataFrame(
            {
                "a": np.asarray(covariates["persons"], dtype=float),
                "precision-a": np.asarray(covariates["income"], dtype=float),
            },
            index=share.index,
        )
        result = wrapper.ld_fractional_response(
            y=share,
            x=colliding,
            model="beta",
            precision_covariates=["a", "precision-a"],
        )
        assert set(result["precision"]) == {"const", "a", "precision-a"}
        assert len(result["precision"]) == 3
        assert set(result["params"]) == {"const", "a", "precision-a"}

    def test_an_empty_precision_selection_is_the_constant_precision_model(self) -> None:
        """An empty list asks for no covariate, which is the model with none.

        MEASURED: the library fitted with ``exog_precision`` holding the intercept
        alone and fitted with ``exog_precision=None`` reach the same optimum by
        different paths -- ``llf = 45.33350932122222`` against
        ``45.33350932122192`` -- so the two are the same model and NOT the same
        bytes. The empty selection therefore takes the library's own default path,
        and this asserts the bytes rather than the model.
        """
        share, covariates = published()
        empty = wrapper.ld_fractional_response(
            y=share, x=covariates, model="beta", precision_covariates=[]
        )
        assert to_json(to_mcp(empty)) == to_json(to_mcp(fitted()))

    def test_the_boundary_share_counts_exact_zeros_and_ones_only(self) -> None:
        """Exact equality, not a tolerance: the field exists to tell a reader
        whether a beta regression was legitimate at all."""
        share, covariates = published()
        assert fitted()["boundary_share"] == 0.0
        assert wrapper.ld_fractional_response(
            y=with_boundaries(), x=covariates, model="fractional"
        )["boundary_share"] == pytest.approx(2.0 / 38.0)

    def test_a_wider_confidence_level_widens_the_interval(self) -> None:
        """``conf_level`` reaches the interval and nothing else."""
        narrow = fitted(conf_level=0.5)["params"]
        wide = fitted(conf_level=0.99)["params"]
        for term, record in wide.items():
            assert record["conf_high"] > narrow[term]["conf_high"], term
            assert record["conf_low"] < narrow[term]["conf_low"], term
            assert record["estimate"] == narrow[term]["estimate"], term

    @pytest.mark.parametrize(
        ("model", "link", "has_precision"),
        [
            ("fractional", "logit", False),
            ("fractional", "probit", False),
            ("fractional", "cloglog", False),
            ("fractional", "loglog", False),
            ("beta", "logit", True),
            ("beta", "probit", True),
            ("beta", "loglog", True),
        ],
    )
    def test_every_branch_returns_the_same_keys_with_its_own_content(
        self, model: str, link: str, has_precision: bool
    ) -> None:
        """The key set does not depend on the branch; what fills it does."""
        share, covariates = published()
        result = wrapper.ld_fractional_response(
            y=share,
            x=covariates,
            model=model,  # type: ignore[arg-type]
            link=link,  # type: ignore[arg-type]
        )
        assert set(result) == CARD_KEYS
        assert set(result["params"]) == {"const", "income", "persons"}
        assert (result["precision"] is not None) is has_precision
        assert result["boundary_share"] == 0.0
        assert all(
            math.isfinite(value) for value in result["marginal_effects"].values()
        )
        assert stubs_free(to_mcp(result))

    def test_every_link_the_contract_declares_has_an_implementation(self) -> None:
        """THE ENUM AND THE MAPPING ARE ONE LIST, asserted rather than assumed.

        ``_LINKS`` is keyed by the enum's own values and a missing key is a
        ``KeyError`` -- not a ``GateError``, so a crash through the gateway rather
        than a refusal. The wire contract makes that unreachable TODAY, and this is
        what keeps it unreachable if card #527 ever declares a fifth link.
        """
        declared = next(
            argument
            for argument in wrapper.NODE_META[FN].args
            if argument.name == "link"
        ).enum
        assert declared is not None
        assert set(declared) == set(wrapper._LINKS)

    def test_the_declared_defaults_are_read_from_the_contract_and_not_invented(
        self,
    ) -> None:
        """An omitted argument takes the value ``node-specs.json`` publishes, and no other."""
        defaults = wrapper.NODE_META[FN].defaults
        assert defaults["model"] == "fractional"
        assert defaults["link"] == "logit"
        assert defaults["conf_level"] == 0.95
        assert "precision_covariates" not in defaults

        share, covariates = published()
        implied = wrapper.ld_fractional_response(y=share, x=covariates)
        named = wrapper.ld_fractional_response(
            y=share, x=covariates, model="fractional", link="logit", conf_level=0.95
        )
        assert to_json(to_mcp(implied)) == to_json(to_mcp(named))

    def test_the_two_models_disagree_about_the_same_data(self) -> None:
        """A quasi-likelihood and a beta likelihood are different estimators.

        Asserted because the alternative failure is silent: a body that ignored
        ``model`` and fitted one estimator twice would satisfy every other test in
        this class.
        """
        share, covariates = published()
        quasi = wrapper.ld_fractional_response(
            y=share, x=covariates, model="fractional"
        )
        beta = wrapper.ld_fractional_response(y=share, x=covariates, model="beta")
        assert quasi["params"]["income"]["estimate"] != pytest.approx(
            beta["params"]["income"]["estimate"], rel=1e-6
        )
        assert quasi["params"]["income"]["std_error"] != pytest.approx(
            beta["params"]["income"]["std_error"], rel=1e-6
        )

    def test_the_link_reaches_the_estimator(self) -> None:
        """Four links, four different coefficient vectors on one dataset."""
        share, covariates = published()
        estimates = {
            link: wrapper.ld_fractional_response(
                y=share,
                x=covariates,
                model="fractional",
                link=link,
            )["params"]["persons"]["estimate"]
            for link in ("logit", "probit", "cloglog", "loglog")
        }
        assert len(set(estimates.values())) == 4, estimates
        assert estimates["logit"] == pytest.approx(0.1275341003086081, rel=1e-9)

    @pytest.mark.filterwarnings(*_OPTIMISER_NOISE)
    def test_the_beta_branch_does_not_converge_on_this_table_under_cloglog(
        self,
    ) -> None:
        """A MEASUREMENT ABOUT THIS DATASET, not a defect and not a missing branch.

        Three of the four links fit the published food-expenditure table as a beta
        regression; the complementary log-log does not. MEASURED against
        statsmodels 0.14.6: ``converged`` false behind a ``ConvergenceWarning``,
        while the same link on the fractional branch converges without a word. The
        refusal is what a caller gets rather than the last step of an abandoned
        search, and it is asserted here so that a release which fixes the optimiser
        is visible rather than silent.
        """
        share, covariates = published()
        assert wrapper.ld_fractional_response(
            y=share, x=covariates, model="fractional", link="cloglog"
        )["params"]["persons"]["estimate"] != 0.0

        with pytest.raises(GateError) as refused:
            wrapper.ld_fractional_response(
                y=share, x=covariates, model="beta", link="cloglog"
            )
        assert refused.value.detail_code == "precondition-degenerate"


class TestOracleCase:
    """Class C -- a published number, its citation and its tolerance class."""

    def test_the_published_number_is_reproduced_within_its_tolerance(self) -> None:
        """The committed case, loaded and run through the conformance harness itself.

        NOT a second comparison written here: ``admissible_calls`` applies the load
        rules and ``disagreement`` is the harness's own two-step comparison, so this
        test cannot be greener than the corpus gate is.
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

    def test_the_published_standard_errors_are_not_claimed_and_the_gap_is_measured(
        self,
    ) -> None:
        """WHY THE CASE CHECKS NO STANDARD ERROR, asserted rather than asserted-about.

        Ferrari and Cribari-Neto's Table 2 prints 0.22385, 0.00304 and 0.03534, and
        those come from the EXPECTED information matrix -- the closed-form ``W`` of
        their section 2. ``BetaResults`` is a ``GenericLikelihoodModel`` and its
        ``bse`` comes from the OBSERVED numerical Hessian. The two are different
        estimators of the same quantity and they do not agree to oracle precision;
        this pins the disagreement so that a future release moving it is visible.
        """
        reported = fitted()["params"]
        published_errors = {"const": 0.22385, "income": 0.00304, "persons": 0.03534}
        gaps = {
            term: abs(reported[term]["std_error"] - value) / value
            for term, value in published_errors.items()
        }
        assert max(gaps.values()) > 1e-4, gaps
        assert max(gaps.values()) < 0.02, gaps


class TestDeterminism:
    """Class D -- identical inputs, identical bytes."""

    def test_two_identical_calls_serialise_to_identical_bytes(self) -> None:
        """``ld_fractional_response`` is not in ``stochastic_unseeded_fns``; read that."""
        specs = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        assert FN not in specs["vocabulary"]["stochastic_unseeded_fns"]

        first = to_json(to_mcp(fitted()))
        second = to_json(to_mcp(fitted()))
        assert first == second
        assert len(first) > 0

    def test_the_default_branch_reproduces_its_own_bytes(self) -> None:
        """The DEFAULT model has no published fit to compare with, so this is what
        proves it: Papke and Wooldridge's own application is 4734 401(k) plans and
        no smaller published fractional-response fit was found, so the fractional
        branch ships proven by structure and determinism rather than by an oracle.
        """
        share, covariates = published()

        def once() -> str:
            return to_json(
                to_mcp(wrapper.ld_fractional_response(y=share, x=covariates))
            )

        assert once() == once()


def test_the_module_exports_every_function_its_cards_name() -> None:
    """The one assertion a scaffold can make truthfully before a body exists."""
    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]
    assert not missing, missing
