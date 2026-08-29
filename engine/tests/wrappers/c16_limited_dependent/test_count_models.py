# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the wrapper module ``count_models`` -- method card #524.

Scaffolded by ``python scripts/gen_wrappers.py --scaffold-tests count_models``; its home is
``tests/wrappers/c16_limited_dependent/test_count_models.py``.

FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, C the oracle case and
D determinism.

ONLY ``ld_count_model`` HAS A BODY. ``ld_overdispersion_test`` is still the emitted stub, and this
file says so once rather than testing it: its argument is a handle to a FITTED object, and a
registered payload cannot carry one -- see the note in the wrapper module and
``tests/controls/double_run.py`` on why a foreign object in a payload is refused.

THE DATA. The published table lives in ``tests/fixtures/doll_hill_1966_*`` and is reached through
the oracle case, which is where the comparison against the page is made. Everything else here is
drawn once from a pinned generator, because the branches this node offers -- three families times
four zero rules -- need a sample with zeros, with positives, and with enough of both to identify a
two-equation model, and no published table of that shape was found.
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

from econflow_engine.chart_spec import assert_pure, chart_spec
from econflow_engine.errors import GateError
from econflow_engine.serialize import to_json, to_mcp
from econflow_engine.wrappers.c16_limited_dependent import (
    count_models as wrapper,
)

MODULE_FNS = ("ld_count_model", "ld_overdispersion_test")

FN = "ld_count_model"
ENGINE_ROOT = Path(__file__).resolve().parents[3]

#: The payload this node promises, read off card #524's rewritten ``output_key_fields``.
#: :class:`TestStructure` asserts that ``node-specs.json`` declares the same set rather
#: than trusting either copy.
CARD_KEYS = frozenset(
    {
        "params",
        "rate_ratios",
        "coeftable",
        "dispersion",
        "zero_inflation",
        "vuong",
        "fitted_values",
        "llf",
        "aic",
        "bic",
        "nobs",
        "family",
        "zeros",
    }
)

#: The environment variable the payload writes, and the payload that writes it.
#: Both are the ones that RAN against the first 2.2 body before its formula gate,
#: kept verbatim so the control asks the question the attacker asked.
INJECTION_MARKER = "EF_RCE"
INJECTION_PAYLOAD = (
    f'__import__("os").environ.__setitem__("{INJECTION_MARKER}","pwned") or w'
)

#: The two warnings statsmodels raises through ``warnings.warn`` when an optimiser
#: gives up. The suite runs under ``-W error``, so a test that means to reach this
#: body's own convergence refusal has to let the fit finish first.
_OPTIMISER_NOISE = (
    "ignore::statsmodels.tools.sm_exceptions.ConvergenceWarning",
    "ignore::statsmodels.tools.sm_exceptions.HessianInversionWarning",
)


def sample() -> tuple[pd.Series, pd.DataFrame]:
    """A 200-row count sample with excess zeros, from a pinned generator.

    Two covariates, one of them with a real effect, and about a third of the rows
    forced to zero so that a zero-inflated and a hurdle model are identified. The
    seed is fixed, so every number this file asserts is the same on every run.
    """
    rng = np.random.default_rng(11)
    n = 200
    x = pd.DataFrame({"w": rng.normal(size=n), "v": rng.normal(size=n)})
    mean = np.exp(0.4 + 0.8 * x["w"].to_numpy())
    counts = rng.poisson(mean).astype(float)
    counts[rng.random(n) < 0.30] = 0.0
    return pd.Series(counts, name="events"), x


def positives() -> tuple[pd.Series, pd.DataFrame]:
    """The same sample with the zeros dropped -- what a truncated model is defined on."""
    y, x = sample()
    kept = y[y > 0]
    return kept, x.loc[kept.index]


def counts_and_design() -> tuple[pd.Series, pd.DataFrame, pd.Series]:
    """The published table, built through the real fixture loader.

    NOT a second transcription: ``build_fixture`` is the code path the oracle case
    takes, so a change to the dataset moves this file's inputs with it.
    """
    from tests.conformance.fixtures import build_fixture

    y: pd.Series = build_fixture("doll_hill_1966_coronary_deaths")
    x: pd.DataFrame = build_fixture("doll_hill_1966_smoking_and_age_indicators")
    exposure: pd.Series = build_fixture("doll_hill_1966_person_years")
    return y, x, exposure


def fitted(**overrides: Any) -> dict[str, Any]:
    """One passing Poisson call on the published table, used by many assertions."""
    y, x, exposure = counts_and_design()
    call: dict[str, Any] = {"y": y, "x": x, "family": "poisson", "exposure": exposure}
    call.update(overrides)
    return wrapper.ld_count_model(**call)


class TestGatesBlock:
    """Class A -- one passing and one refused input for every declared gate."""

    def test_a_whole_number_response_passes_and_a_fractional_one_is_refused(self) -> None:
        """GATE 1. MEASURED: ``Poisson`` fits a fractional response with NO warning.

        ``Poisson(deaths + 0.5, X).fit()`` returns ``llf = -33.269482`` and emits
        nothing at all under ``warnings.simplefilter('always')``. A response that
        is not a count is a different model, silently.
        """
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y + 0.5, x=x, family="poisson", exposure=exposure
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "not whole numbers" in str(refused.value)

    def test_a_non_negative_response_passes_and_a_negative_one_is_refused(self) -> None:
        """GATE 1, the other half. MEASURED: a negative response fits and returns nan.

        ``Poisson(deaths - 40, X).fit()`` raises nothing; the log-likelihood comes
        back ``nan`` behind numpy's own overflow warnings.
        """
        assert fitted()["llf"] < 0.0

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y - 40, x=x, family="poisson", exposure=exposure
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "below 0" in str(refused.value)

    def test_a_truncated_model_passes_on_positives_and_is_refused_on_zeros(self) -> None:
        """GATE 2. MEASURED: a truncated fit on data WITH zeros silently drops them.

        The figure below is measured once and lives in
        ``gates.estimation.require_counts``, which is the rule's home; it is named
        here rather than restated.

        ``TruncatedLFPoisson`` over the 200 rows returns the log-likelihood it
        returns over the 95 positive rows alone -- the same fit, reported over a
        sample the caller believes was used.
        """
        y, x = positives()
        assert wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="truncated"
        )["nobs"] == len(y)

        whole, design = sample()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=whole, x=design, family="poisson", zeros="truncated"
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "below 1" in str(refused.value)

    def test_a_zero_model_passes_with_zeros_and_is_refused_without_them(self) -> None:
        """GATE 3. MEASURED: a zero-inflated fit on data with NO zeros converges.

        ``ZeroInflatedPoisson`` over the 95 positive rows comes back with
        ``converged`` true, having estimated an inflation probability that nothing
        in the sample identifies. The log-likelihood it reports is measured once
        and lives in ``gates.estimation.require_an_observed_value``, the rule's own
        home.
        """
        y, x = sample()
        assert wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="zero_inflated"
        )["zero_inflation"] is not None

        kept, design = positives()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=kept, x=design, family="poisson", zeros="zero_inflated"
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "no value equal to 0" in str(refused.value)

    def test_a_complete_response_passes_and_a_missing_one_is_refused(self) -> None:
        """GATE 4. MEASURED: one NaN in the response returns ``llf = nan``, silently.

        No warning is emitted -- ``missing='none'`` is the constructor's default and
        it means "do not look", not "there are none".
        """
        assert math.isfinite(fitted()["llf"])

        y, x, exposure = counts_and_design()
        holed = y.astype(float)
        holed.iloc[0] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=holed, x=x, family="poisson", exposure=exposure)
        assert refused.value.detail_code == "precondition-missing"
        assert "1 missing" in str(refused.value)

    def test_a_complete_design_passes_and_a_missing_covariate_is_refused(self) -> None:
        """GATE 4, over the design. Every column is checked, one at a time."""
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        holed = x.astype(float)
        holed.iloc[0, 1] = float("inf")
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=y, x=holed, family="poisson", exposure=exposure)
        assert refused.value.detail_code == "precondition-missing"
        assert "1 non-finite" in str(refused.value)

    def test_a_numeric_design_passes_and_a_text_column_is_refused(self) -> None:
        """GATE 4, the dtype half. A column of labels is not a covariate."""
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        labelled = x.astype(object)
        labelled["agecat"] = ["35-44", "45-54", "55-64", "65-74", "75-84"] * 2
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=y, x=labelled, family="poisson", exposure=exposure)
        assert refused.value.detail_code == "precondition-shape"
        assert "is not numeric" in str(refused.value)

    def test_an_aligned_design_passes_and_a_shifted_index_is_refused(self) -> None:
        """GATE 5. The estimator reads three arguments POSITIONALLY, not by label."""
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x.set_index(x.index + 100), family="poisson", exposure=exposure
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "aligned" in str(refused.value)

    def test_an_aligned_exposure_passes_and_a_reordered_one_is_refused(self) -> None:
        """GATE 5, over the exposure, and this is the measurement that demanded it.

        MEASURED: an exposure whose index is REVERSED -- the same ten values, each
        against a different row -- is used positionally and returns
        ``llf = -41.974688`` where the aligned one returns ``-33.600153``. Nothing
        in the result says which of the two happened.
        """
        assert fitted()["llf"] == pytest.approx(-33.6001534405, abs=1e-8)

        y, x, exposure = counts_and_design()
        reversed_labels = pd.Series(
            exposure.to_numpy()[::-1], index=exposure.index[::-1], name=exposure.name
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", exposure=reversed_labels
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "aligned" in str(refused.value)

    def test_a_positive_exposure_passes_and_a_zero_one_is_refused(self) -> None:
        """GATE 6. MEASURED: an exposure of zero returns ``llf = nan``.

        The offset is ``log(exposure)``, so a zero is minus infinity and a negative
        value is not a number at all; both come back as a fitted model.
        """
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", exposure=exposure.mask(exposure.index == 1, 0)
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "open interval" in str(refused.value)

    @pytest.mark.parametrize("level", [0.0, 1.0, 1.5, -0.1])
    def test_a_level_inside_the_unit_interval_passes_and_an_endpoint_is_refused(
        self, level: float
    ) -> None:
        """GATE 7. A confidence level of exactly 1 is an infinite interval."""
        assert fitted(conf_level=0.9)["coeftable"].shape[0] == 6

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", exposure=exposure, conf_level=level
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "conf_level" in str(refused.value)

    def test_distinct_column_names_pass_and_a_repeated_one_is_refused(self) -> None:
        """GATE 8. MEASURED: two columns of one name fit silently.

        ``Poisson`` accepts a design whose ``exog_names`` carries 'smokes' twice and
        returns the same log-likelihood as the design without the copy. Read back
        into a mapping keyed by name, one of the two coefficients disappears.
        """
        assert set(fitted()["params"]) == {
            "const", "smokes", "age_45_54", "age_55_64", "age_65_74", "age_75_84",
        }

        y, x, exposure = counts_and_design()
        twice = pd.concat([x, x[["smokes"]]], axis=1)
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=y, x=twice, family="poisson", exposure=exposure)
        assert refused.value.detail_code == "precondition-shape"
        assert "more than once" in str(refused.value)

    def test_a_design_without_an_intercept_passes_and_one_carrying_const_is_refused(
        self,
    ) -> None:
        """GATE 8, the collision this node creates for itself.

        The intercept is added here and named ``const``, so a covariate of that name
        would be the same column twice and the caller's would be the one lost.
        """
        assert fitted()["params"]["const"] == pytest.approx(-7.919325711859, rel=1e-9)

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x.assign(const=1.0), family="poisson", exposure=exposure
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "more than once" in str(refused.value)

    def test_a_full_rank_design_passes_and_a_collinear_one_is_refused(self) -> None:
        """GATE 9. MEASURED: a rank-deficient design fits SILENTLY.

        ``check_rank`` is the constructor's default and did not stop a design of
        rank 6 over 7 columns: the fit returned ``llf = -33.60015344052124``, which
        is the full-rank fit's own value, with coefficients that are not identified.
        """
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x.assign(copy_of_smokes=x["smokes"]), family="poisson",
                exposure=exposure,
            )
        assert refused.value.detail_code == "precondition-rank"
        assert "linear combination" in str(refused.value)

    def test_a_long_enough_sample_passes_and_a_short_one_is_refused(self) -> None:
        """GATE 10. MEASURED: two rows raise ``LinAlgError: Singular matrix``.

        The message that reaches a caller from the estimator names a matrix. The
        rule is about degrees of freedom, and it says so.
        """
        assert fitted()["nobs"] == 10

        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y.iloc[:4], x=x.iloc[:4], family="poisson", exposure=exposure.iloc[:4]
            )
        assert refused.value.detail_code == "precondition-sample-size"
        assert "4 observation(s)" in str(refused.value)

    def test_a_hurdle_without_exposure_passes_and_one_with_it_is_refused(self) -> None:
        """GATE 11. MEASURED: ``HurdleCountModel`` refuses an exposure by RAISING.

        ``NotImplementedError: Offset and exposure are not yet implemented`` derives
        from ``RuntimeError`` and is defined in ``builtins``, so no translation of a
        library's own exception reaches it: unrefused, it is a crash.
        """
        y, x = sample()
        assert wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="hurdle"
        )["zeros"] == "hurdle"

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", zeros="hurdle",
                exposure=pd.Series(np.full(len(y), 2.0), index=y.index),
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "hurdle" in str(refused.value)
        assert "exposure" in str(refused.value)

    def test_a_poisson_hurdle_passes_and_a_generalised_poisson_one_is_refused(self) -> None:
        """GATE 11, the other combination the library does not carry.

        MEASURED: ``HurdleCountModel(dist='genpoisson')`` raises
        ``NotImplementedError: dist and zerodist must be "poisson","negbin"``.
        """
        y, x = sample()
        assert wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="hurdle"
        )["dispersion"] is None

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="generalised_poisson", zeros="hurdle"
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "generalised_poisson" in str(refused.value)

    def test_inflation_covariates_pass_on_a_zero_inflated_fit_and_are_refused_elsewhere(
        self,
    ) -> None:
        """GATE 12. An argument this branch would silently ignore is refused instead."""
        y, x = sample()
        inflated = wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="zero_inflated",
            inflation_covariates=["w"],
        )
        assert set(inflated["zero_inflation"]) == {"const", "w"}

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", zeros="none", inflation_covariates=["w"]
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "inflation_covariates" in str(refused.value)

    def test_a_named_inflation_covariate_passes_and_an_absent_one_is_refused(self) -> None:
        """GATE 13. MEASURED: an absent name reaches pandas as a ``KeyError``.

        ``KeyError`` derives from ``LookupError`` and not from ``ValueError``, so it
        is not one of the classes the estimator translation recognises: unrefused,
        the caller gets a traceback.
        """
        y, x = sample()
        assert wrapper.ld_count_model(
            y=y, x=x, family="poisson", zeros="zero_inflated",
            inflation_covariates=["v"],
        )["zero_inflation"] is not None

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", zeros="zero_inflated",
                inflation_covariates=["not_a_column"],
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "'not_a_column'" in str(refused.value)

    def test_a_covariate_name_carrying_a_payload_is_selected_and_never_evaluated(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """THE CONTROL FOR THE ONE ARGUMENT THAT CARRIES CALLER-CHOSEN TEXT ONWARD.

        ``inflation_covariates`` is kind ``series_codes``, which ``kinds.py`` types
        as ``list[str]`` with no constraint on the contents, and this body puts it
        into a pandas column selection. The first 2.2 body shipped a live remote
        code execution through an argument of kind ``string`` spliced into a
        formula, so the question is asked here rather than assumed: the payload
        below is the one that ran in that body, and a column selection must merely
        FIND it. The marker is asserted in a ``finally`` so that it, and not the
        exception type, is what turns this red.
        """
        monkeypatch.delenv(INJECTION_MARKER, raising=False)
        y, x = sample()
        # Squared rather than copied: a copy of a column is a linear combination
        # of the design and the rank gate refuses it before the name is used.
        frame = x.assign(**{INJECTION_PAYLOAD: x["w"] ** 2})
        try:
            result = wrapper.ld_count_model(
                y=y,
                x=frame,
                family="poisson",
                zeros="zero_inflated",
                inflation_covariates=[INJECTION_PAYLOAD],
            )
        finally:
            assert os.environ.get(INJECTION_MARKER) is None, (
                "THE PAYLOAD EXECUTED. A column name reached something that "
                "evaluates it, and this node's contract says nothing here does."
            )
        assert INJECTION_PAYLOAD in result["zero_inflation"]
        assert INJECTION_PAYLOAD in result["params"]

    @pytest.mark.filterwarnings(*_OPTIMISER_NOISE)
    def test_a_converged_fit_passes_and_one_that_gave_up_is_refused(self) -> None:
        """GATE 14. MEASURED: a zero-inflated negative binomial on this sample stops.

        It returns ``converged`` false with every standard error ``nan`` and a
        log-likelihood of ``nan`` -- a result object shaped exactly like a fit. The
        two optimiser warnings are silenced on THIS test alone so that the body's
        own refusal is what fires; under the suite's ``-W error`` the first warning
        would otherwise be raised inside the fit and reported as the estimator's.
        """
        y, x = sample()
        assert wrapper.ld_count_model(y=y, x=x, family="negative_binomial")["llf"] < 0.0

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="negative_binomial", zeros="zero_inflated"
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "did not converge" in str(refused.value)

    def test_the_estimator_s_own_refusal_is_translated_rather_than_crashed_on(self) -> None:
        """GATE 15. A response of all zeros raises out of the optimiser.

        MEASURED: ``LinAlgError: Singular matrix`` -- which derives from
        ``ValueError`` -- behind a ``PerfectSeparationWarning``. Under the suite's
        ``-W error`` the warning is what arrives first; both are the estimator
        objecting to the data, and both must reach the caller as a refusal.
        """
        y, x, exposure = counts_and_design()
        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y * 0, x=x, family="poisson", exposure=exposure
            )
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(refused.value)

    def test_a_fit_that_returned_numbers_passes_and_one_that_returned_nan_is_refused(
        self,
    ) -> None:
        """GATE 16. MEASURED: a covariate rescaled by 1e6 CONVERGES ON ``nan``.

        ``x["w"] * 1e6`` is the scale of a population, a market capitalisation or a
        currency amount. The fit reports ``converged`` true, raises nothing, and
        returns ``llf = nan`` beside coefficients that are all ``nan``; ``to_json``
        writes no ``NaN`` token, so what a caller receives is well-formed JSON
        whose estimates are null -- indistinguishable from ``dispersion``,
        ``zero_inflation`` and ``vuong``, which this card leaves empty on purpose.

        THE SECOND ROUTE IS AN EXPOSURE RATHER THAN A COVARIATE, and it is here
        because it reaches the same all-null payload with every covariate
        untouched: forty rows against an exposure of 1e-307 converge on ``nan``
        the same way. (An exposure of 1e-305 does NOT, on this draw: it returns
        ``llf = -56.83391073960135`` with ``const = 702.2515809408649``, which is
        how narrow the margin is.)
        """
        y, x = sample()
        assert math.isfinite(wrapper.ld_count_model(y=y, x=x, family="poisson")["llf"])

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=y, x=x.assign(w=x["w"] * 1e6), family="poisson")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "coefficients and log-likelihood" in str(refused.value)
        assert "'llf'" in str(refused.value)

        thin = pd.Series(np.full(40, 1e-307), index=y.index[:40])
        with pytest.raises(GateError) as underflowed:
            wrapper.ld_count_model(
                y=y.iloc[:40], x=x.iloc[:40], family="poisson", exposure=thin
            )
        assert underflowed.value.detail_code == "precondition-degenerate"
        assert "are not numbers" in str(underflowed.value)

    def test_a_representable_rate_ratio_passes_and_an_unrepresentable_one_is_refused(
        self,
    ) -> None:
        """GATE 17. MEASURED: a covariate rescaled by 1e-3 has no rate ratio at all.

        Dividing a covariate by 1000 is a change of units and leaves the fit
        alone -- the log-likelihood is unmoved -- but it multiplies the
        coefficient by 1000, and ``exp`` of 820.81 has no value in double
        precision. Before this gate that arithmetic raised ``OverflowError: math
        range error`` from inside the body: ``make_tool`` catches only
        ``GateError`` and ``run_method`` catches only ``NotImplementedError``, so
        it left the gateway as an uncaught crash.
        """
        y, x = sample()
        passing = wrapper.ld_count_model(y=y, x=x, family="poisson")
        assert passing["params"]["w"] == pytest.approx(0.8208142382100729, rel=1e-9)
        assert passing["rate_ratios"]["w"] == pytest.approx(math.exp(passing["params"]["w"]))

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(y=y, x=x.assign(w=x["w"] * 1e-3), family="poisson")
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-degenerate"
        assert "rate ratios" in str(refused.value)
        assert "['w']" in str(refused.value)
        assert "the first is inf" in str(refused.value)

    def test_distinct_inflation_covariates_pass_and_a_repeated_one_is_refused(
        self,
    ) -> None:
        """GATE 8, over the inflation design this body assembles for itself.

        ``design[['const', 'w', 'w']]`` carries ``w`` twice, and the mapping this
        body reports the inflation equation in is keyed by name -- so one of the
        two coefficients would simply be absent from it. The count design's own
        duplicate gate cannot see this: the caller's frame carries ``w`` once, and
        it is ``inflation_covariates`` that names it twice.
        """
        y, x = sample()
        assert set(
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", zeros="zero_inflated",
                inflation_covariates=["w", "v"],
            )["zero_inflation"]
        ) == {"const", "w", "v"}

        with pytest.raises(GateError) as refused:
            wrapper.ld_count_model(
                y=y, x=x, family="poisson", zeros="zero_inflated",
                inflation_covariates=["w", "w"],
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "inflation_covariates" in str(refused.value)
        assert "['w'] more than once" in str(refused.value)

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

    def test_the_registered_object_is_the_whole_serialisable_result(self) -> None:
        """Card #524 registers under ``fit``, and the registry holds what is returned.

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

    def test_the_coefficient_table_is_a_chart_this_engine_can_emit(self) -> None:
        """What ``chart_spec`` returns for this payload, and it is NOT the card's kind.

        MEASURED against chart_spec as it stands. Card #524 declares
        ``chart_kind: table``, and the emitter reaches its table branch only for a
        value that is not a frame: ``_frame_spec`` falls back to a table when NO
        column is numeric, so a coefficient table -- one label column and six
        numeric ones -- comes back as six LINES over the row number. The wire form
        is no better: ``to_mcp`` renders the frame as a list of row mappings, and
        the list branch flattens it into a single column.

        This test asserts what the engine emits rather than what the card declares,
        and records the difference instead of hiding it. It is a defect in the
        emitter's frame branch (box 2.1.12) rather than in this payload, and it
        reaches every card whose declared kind is ``table``.
        """
        spec = chart_spec(fitted()["coeftable"], title="count model")
        assert spec is not None
        assert_pure(spec)
        assert [series["name"] for series in spec["series"]] == [
            "estimate", "std_error", "z_value", "p_value", "conf_low", "conf_high",
        ]
        assert len(spec["series"][0]["data"]) == 6
        assert "dataset" not in spec

    def test_the_rate_ratios_are_the_exponentiated_coefficients(self) -> None:
        """The card's first trap: a coefficient is a semi-elasticity, not a ratio."""
        result = fitted()
        assert set(result["rate_ratios"]) == set(result["params"])
        for term, coefficient in result["params"].items():
            assert result["rate_ratios"][term] == pytest.approx(math.exp(coefficient))

    def test_every_reported_field_describes_the_same_sample(self) -> None:
        """Alignment, asserted rather than documented."""
        result = fitted()
        assert result["nobs"] == 10
        assert len(result["fitted_values"]) == result["nobs"]
        assert list(result["fitted_values"].index) == list(range(1, 11))
        assert result["coeftable"].shape == (6, 7)
        assert list(result["coeftable"].columns) == [
            "term", "estimate", "std_error", "z_value", "p_value", "conf_low", "conf_high",
        ]
        assert list(result["coeftable"]["term"]) == list(result["params"])
        assert result["family"] == "poisson"
        assert result["zeros"] == "none"

    def test_the_exposure_enters_as_an_offset_and_not_as_a_regressor(self) -> None:
        """Card #524's third trap, made observable.

        The fitted values are on the scale of the counts, so they are the rate times
        the person-years; the coefficient vector has one entry per COLUMN of the
        design and none for the exposure, which is what "an offset with coefficient
        one" means.
        """
        result = fitted()
        assert len(result["params"]) == 6
        y, _, exposure = counts_and_design()
        rate = np.asarray(result["fitted_values"]) / np.asarray(exposure, dtype=float)
        assert float(np.max(rate)) < 0.05
        assert float(np.sum(np.asarray(result["fitted_values"]))) == pytest.approx(
            float(y.sum()), rel=1e-6
        )

    def test_a_wider_confidence_level_widens_the_interval(self) -> None:
        """``conf_level`` reaches the interval and nothing else."""
        narrow = fitted(conf_level=0.5)["coeftable"]
        wide = fitted(conf_level=0.99)["coeftable"]
        assert (wide["conf_high"] > narrow["conf_high"]).all()
        assert (wide["conf_low"] < narrow["conf_low"]).all()
        assert wide["estimate"].tolist() == narrow["estimate"].tolist()

    def test_a_poisson_reports_no_dispersion_and_a_negative_binomial_reports_one(
        self,
    ) -> None:
        """``dispersion`` is null where none is estimated, and never 0.0.

        A Poisson has no dispersion parameter at all, so reporting a number there
        would be reporting a fitted value nobody estimated.
        """
        y, x = sample()
        assert wrapper.ld_count_model(y=y, x=x, family="poisson")["dispersion"] is None
        overdispersed = wrapper.ld_count_model(y=y, x=x, family="negative_binomial")
        assert overdispersed["dispersion"] is not None
        assert overdispersed["dispersion"] > 0.0

    @pytest.mark.parametrize(
        ("family", "zeros", "has_dispersion", "has_inflation"),
        [
            ("poisson", "none", False, False),
            ("negative_binomial", "none", True, False),
            ("generalised_poisson", "none", True, False),
            ("poisson", "zero_inflated", False, True),
            ("poisson", "hurdle", False, False),
        ],
        ids=["poisson", "negbin", "genpoisson", "zero-inflated", "hurdle"],
    )
    def test_every_branch_returns_the_same_keys_with_its_own_content(
        self, family: str, zeros: str, has_dispersion: bool, has_inflation: bool
    ) -> None:
        """The key set does not depend on the branch; what fills it does."""
        y, x = sample()
        result = wrapper.ld_count_model(y=y, x=x, family=family, zeros=zeros)  # type: ignore[arg-type]
        assert set(result) == CARD_KEYS
        assert result["family"] == family
        assert result["zeros"] == zeros
        assert (result["dispersion"] is not None) is has_dispersion
        assert (result["zero_inflation"] is not None) is has_inflation
        assert set(result["params"]) == {"const", "w", "v"}
        assert result["nobs"] == len(y)
        assert math.isfinite(result["llf"])
        assert stubs_free(to_mcp(result))

    def test_a_hurdle_reports_its_zero_equation_in_the_table_and_not_as_inflation(
        self,
    ) -> None:
        """Card #524's second trap, enforced by the payload's shape.

        A hurdle's zero equation is not an inflation probability -- all its zeros
        come from one process -- so ``zero_inflation`` stays null and the equation
        is reported row by row in the table, under the estimator's ``zm_`` prefix
        and the design's own column names.

        THE COVARIATES ARE NAMED SO THAT A POSITIONAL LABEL WOULD COLLIDE WITH A
        REAL ONE, which is what the sample's ``w`` and ``v`` could never show.
        MEASURED against statsmodels 0.14.6: over a design of ``const``, ``age``,
        ``x1`` the estimator labels the zero equation ``zm_const``, ``zm_x1``,
        ``zm_x2`` -- so its ``zm_x1`` is AGE's coefficient, while a covariate
        genuinely called ``x1`` is three rows below under its own name. The prefix
        says which equation a row belongs to and is kept; the suffix is a position
        and is replaced.

        THE SWAP IS WHAT PROVES THE LABEL NAMES A COLUMN RATHER THAN A SLOT. The
        same two covariates in the opposite order must put the same number under
        ``zm_age``; under a positional suffix that row is called something else
        entirely.
        """
        y, x = sample()
        colliding = x.rename(columns={"w": "age", "v": "x1"})
        result = wrapper.ld_count_model(
            y=y, x=colliding, family="poisson", zeros="hurdle"
        )
        assert result["zero_inflation"] is None
        terms = list(result["coeftable"]["term"])
        assert [term for term in terms if term.startswith("zm_")] == [
            "zm_const", "zm_age", "zm_x1",
        ]
        assert terms[-3:] == ["const", "age", "x1"]

        swapped = wrapper.ld_count_model(
            y=y, x=colliding[["x1", "age"]], family="poisson", zeros="hurdle"
        )
        rows = dict(zip(terms, result["coeftable"]["estimate"], strict=True))
        swapped_rows = dict(
            zip(swapped["coeftable"]["term"], swapped["coeftable"]["estimate"], strict=True)
        )
        assert swapped_rows["zm_age"] == pytest.approx(rows["zm_age"], rel=1e-6)
        assert swapped_rows["zm_x1"] == pytest.approx(rows["zm_x1"], rel=1e-6)

    def test_the_vuong_field_is_null_on_every_branch_and_says_so(self) -> None:
        """The card promises a statistic the reference implementation does not carry.

        ``grep -rniE 'vuong' site-packages/statsmodels/ --include=*.py`` returns
        nothing on 0.14.6. Writing one here is arithmetic this engine would own, and
        no published value was found to check it against, so the field is present
        and empty rather than filled with a number nobody can verify.
        """
        y, x = sample()
        for zeros in ("none", "zero_inflated", "hurdle"):
            result = wrapper.ld_count_model(y=y, x=x, family="poisson", zeros=zeros)
            assert result["vuong"] is None

    def test_the_declared_defaults_are_read_from_the_contract_and_not_invented(
        self,
    ) -> None:
        """An omitted enum takes the value ``node-specs.json`` publishes, and no other."""
        defaults = wrapper.NODE_META[FN].defaults
        assert defaults["family"] == "negative_binomial"
        assert defaults["zeros"] == "none"
        assert defaults["conf_level"] == 0.95

        y, x = sample()
        implied = wrapper.ld_count_model(y=y, x=x)
        named = wrapper.ld_count_model(
            y=y, x=x, family="negative_binomial", zeros="none", conf_level=0.95
        )
        assert to_json(to_mcp(implied)) == to_json(to_mcp(named))


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


class TestDeterminism:
    """Class D -- identical inputs, identical bytes."""

    def test_two_identical_calls_serialise_to_identical_bytes(self) -> None:
        """``ld_count_model`` is not in ``stochastic_unseeded_fns``; read that."""
        specs = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        assert FN not in specs["vocabulary"]["stochastic_unseeded_fns"]

        first = to_json(to_mcp(fitted()))
        second = to_json(to_mcp(fitted()))
        assert first == second
        assert len(first) > 0


def stubs_free(payload: object) -> bool:
    """No ``to_mcp`` refusal record anywhere in this payload."""
    if isinstance(payload, dict):
        if payload.get("@mcp_serialized") is False:
            return False
        return all(stubs_free(value) for value in payload.values())
    if isinstance(payload, list):
        return all(stubs_free(value) for value in payload)
    return True


def test_the_module_exports_every_function_its_cards_name() -> None:
    """The one assertion a scaffold can make truthfully before a body exists."""
    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]
    assert not missing, missing


def test_the_second_node_of_this_card_is_still_the_emitted_stub() -> None:
    """``ld_overdispersion_test`` has no body, and this file states it rather than skipping.

    Its ``fit`` argument is a handle to a fitted object; the object this node
    registers is the serialisable payload, so the dispersion test cannot be written
    against it without either a live-object seam or the ingredients in the payload.
    That is a contract question for card #524 rather than something to settle here.
    """
    with pytest.raises(NotImplementedError, match="ld_overdispersion_test"):
        wrapper.ld_overdispersion_test(fit=object())
