# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the wrapper module ``ordered_choice`` -- method card #523.

FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, C the oracle case and
D determinism.

THE DATA, AND THERE ARE TWO PUBLISHED TABLES HERE RATHER THAN ONE.

``tests/fixtures/stata_r_ologit_1977_*`` is the cross-tabulation Stata's manual prints for
``ologit rep77 foreign`` -- 66 cars, five ordered repair records, one binary covariate -- and it is
reached through ``build_fixture``, the code path the oracle case takes, so a change to the
transcription moves this file's inputs with it. It is the case's dataset because the page prints
SEVEN significant digits beside it. It is also the harder of the two datasets in three separate
ways, which is why it is the one most assertions use: it has FIVE categories rather than three, so
a body that read the threshold parameters as cut points cannot hide behind a single boundary; its
coefficient is POSITIVE while three of its five marginal effects are NEGATIVE, which is the card's
second interpretation trap on the published data rather than on a sample chosen to show it; and one
of its ten cells is EMPTY -- no domestic car has an Excellent 1977 record -- so its fourth
dichotomy separates and the proportional-odds test must refuse the very fit the oracle case runs.

McCullagh's Table 1 is card #523's own source and is built in :func:`mccullagh` from the six counts
the page prints. It is here because it is the only published fit of this model whose data is fully
listed AND whose proportional-odds test is computable: three categories, one covariate, no empty
cell, no separated dichotomy. Its four published figures are asserted at the precision the page
carries -- three decimals, by ``round`` -- because no tolerance class in
``tests/oracle/_policy.json`` can express a three-decimal claim. Saying so at length is what
``stata_r_ologit_example_1_repair_records.json`` does.

TWO CONTINGENCY TABLES ARE BUILT HERE AND ARE NOT PUBLISHED, and they are labelled as such:
:func:`proportional` satisfies the proportional-odds restriction EXACTLY, by construction, and
:func:`crossed` violates it as hard as a 3 x 2 table can -- the odds ratio is 15.5 at the first cut
point and 0.064 at the second. Neither carries a published number and neither is used as one; they
exist so that the test of the restriction is watched saying yes and saying no.
"""

from __future__ import annotations

import importlib.util
import json
import math
import os
import subprocess
import sys
import textwrap
import warnings
from pathlib import Path
from types import ModuleType
from typing import Any, Literal

import numpy as np
import pandas as pd
import pytest
from scipy import stats

from econflow_engine.chart_spec import assert_pure, chart_spec
from econflow_engine.errors import GateError
from econflow_engine.serialize import to_json, to_mcp
from econflow_engine.wrappers.c16_limited_dependent import (
    ordered_choice as wrapper,
)

MODULE_FNS = ("ld_ordered_choice", "ld_proportional_odds_test")

FIT_FN = "ld_ordered_choice"
TEST_FN = "ld_proportional_odds_test"
ENGINE_ROOT = Path(__file__).resolve().parents[3]

#: The payload ``ld_ordered_choice`` promises, read off card #523's rewritten
#: ``output_key_fields``. :class:`TestStructure` asserts that ``node-specs.json`` declares the
#: same set rather than trusting either copy.
FIT_KEYS = frozenset(
    {
        "params", "thresholds", "marginal_effects", "coeftable", "llf", "nobs", "link",
        "outcome", "design",
    }
)

#: The payload ``ld_proportional_odds_test`` promises, on the same footing.
TEST_KEYS = frozenset({"brant_test", "by_variable", "alpha", "reject"})

#: What StataCorp, Stata Base Reference Manual, [R] ologit, Example 1, p. 4 prints for
#: ``ologit rep77 foreign``. The oracle case is where these are compared against the page; this
#: file uses them wherever a passing call has to assert a value.
PUBLISHED_COEFFICIENT = 1.455878
PUBLISHED_THRESHOLDS = {
    "1|2": -2.765562,
    "2|3": -0.9963603,
    "3|4": 0.9426153,
    "4|5": 3.123351,
}
PUBLISHED_LLF = -85.908161
PUBLISHED_NOBS = 66

#: The standard errors the same page prints, in the order ``bse`` reports them. THEY ARE NOT ALL
#: COMPARABLE, which is what ``test_the_threshold_standard_errors_are_another_parameterisations``
#: is about: the first two are, and the last three are the standard errors of a LOG INCREMENT
#: rather than of a cut point.
PUBLISHED_STANDARD_ERRORS = (0.5308951, 0.5988208, 0.3217706, 0.3136398, 0.5423257)

#: McCullagh (1980), doi:10.1111/j.2517-6161.1980.tb01109.x, p. 112 for the three estimates and
#: p. 113 for the deviance. THREE DECIMALS, which is the whole reason they are asserted here with
#: ``round`` and not in an oracle case.
MCCULLAGH_DELTA = 0.603
MCCULLAGH_THETA = (-0.810, 1.061)
MCCULLAGH_DEVIANCE = 0.302

#: The environment variable a column name would set if anything evaluated it, and the name that
#: would set it. Both are the ones that RAN against the first 2.2 body before its formula gate.
INJECTION_MARKER = "EF_RCE"
INJECTION_PAYLOAD = (
    f'__import__("os").environ.__setitem__("{INJECTION_MARKER}","pwned") or foreign'
)


def published() -> tuple[pd.Series, pd.DataFrame]:
    """Stata's 66 cars, through the real fixture loader.

    NOT a second transcription: ``build_fixture`` is the code path the oracle case takes, so a
    change to either dataset moves this file's inputs with it.
    """
    from tests.conformance.fixtures import build_fixture

    y: pd.Series = build_fixture("stata_r_ologit_1977_repair_record")
    x: pd.DataFrame = build_fixture("stata_r_ologit_1977_foreign")
    return y, x


def fitted(**overrides: Any) -> dict[str, Any]:
    """One passing call on the published table, used by many assertions."""
    y, x = published()
    call: dict[str, Any] = {"y": y, "x": x}
    call.update(overrides)
    return wrapper.ld_ordered_choice(**call)


def _expand(counts: dict[Any, tuple[int, int]], name: str) -> tuple[pd.Series, pd.DataFrame]:
    """A two-group contingency table, one row per observation, group coded 0 then 1."""
    levels: list[Any] = []
    group: list[float] = []
    for level, (first, second) in counts.items():
        levels += [level] * (first + second)
        group += [0.0] * first + [1.0] * second
    index = pd.RangeIndex(1, len(levels) + 1)
    return (
        pd.Series(levels, index=index, name="y"),
        pd.DataFrame({name: group}, index=index),
    )


def mccullagh() -> tuple[pd.Series, pd.DataFrame]:
    """McCullagh (1980) Table 1, p. 111, through the real fixture loader.

    "Tonsil size of carriers and non-carriers of Streptococcus pyogenes", the original data of
    Holmes and Williams (1954): carriers 19, 29 and 24 over the three ordered sizes against
    non-carriers 497, 560 and 269. It is committed rather than built here because the invocation
    payload that reaches ``ld_proportional_odds_test`` names the same two datasets, so the
    transcription this file asserts against is the one that gate runs.

    THE COVARIATE IS +1/2 AND -1/2 AND NOT 1 AND 0, because that is the parameterisation the page's
    own numbers belong to. His equation (2.4) writes the two groups as ``theta_j -/+ Delta/2``, so
    the group enters symmetrically and the slope IS his Delta; coding it 0/1 would move both cut
    points by half of it and the published ``theta_1`` and ``theta_2`` would no longer be what this
    method reports.
    """
    from tests.conformance.fixtures import build_fixture

    y: pd.Series = build_fixture("mccullagh_1980_tonsil_size")
    x: pd.DataFrame = build_fixture("mccullagh_1980_streptococcus_carrier")
    return y, x


def mccullagh_labelled() -> tuple[pd.Series, pd.DataFrame]:
    """The same table with its three sizes as an ORDERED CATEGORICAL of the page's own words.

    A dataset file declares one dtype and a column of phrases builds as a plain object Series, so
    the committed transcription is the published CODING -- 1, 2, 3 in the order the table prints.
    This wraps it in the labels for the assertions that are about a Categorical outcome rather
    than about a numeric one.
    """
    y, x = mccullagh()
    levels = ["present", "enlarged", "greatly enlarged"]
    labelled = pd.Series(
        pd.Categorical(
            [levels[int(code) - 1] for code in y], categories=levels, ordered=True
        ),
        index=y.index,
        name="tonsil_size",
    )
    return labelled, x


def proportional() -> tuple[pd.Series, pd.DataFrame]:
    """A 3 x 2 table on which proportional odds holds EXACTLY, by construction.

    The odds ratio is 19 at both cut points -- ``(50/5)/(45/45)`` and ``(95/5)/(50/50)`` -- so the
    restriction the test examines is true of these counts rather than approximately true of them.
    """
    return _expand({0: (5, 50), 1: (45, 45), 2: (50, 5)}, "group")


def crossed() -> tuple[pd.Series, pd.DataFrame]:
    """A 3 x 2 table on which proportional odds fails as hard as three categories allow.

    MEASURED on these counts: the odds ratio is 15.545455 at the first cut point and 0.064327 at
    the second, so the two cut points disagree about the DIRECTION of the effect. The table is
    symmetric under reversing the levels and swapping the groups, which is why the single
    proportional-odds slope it forces is exactly zero: the two effects cancel, and a reader of that
    coefficient alone would conclude the group does not matter at all.
    """
    return _expand({0: (5, 45), 1: (90, 10), 2: (5, 45)}, "group")


def reported_codes(y: pd.Series) -> np.ndarray:
    """The 0-based level index of an outcome, whatever dtype it arrived as."""
    ordered = pd.Categorical(y, categories=list(np.sort(pd.unique(y.to_numpy()))), ordered=True)
    return np.asarray(ordered.codes, dtype=float)


#: The one expression Brant's off-diagonal blocks turn on, and the two ways of getting it wrong
#: that the body's own docstrings name. ``min`` for ``max`` is the mistake that was actually made
#: while this module was written; the product is the mistake of treating the ``J - 1`` fits as
#: independent, which is the assumption the paper exists to correct.
JOINT_PROBABILITY = "probabilities[max(first, second)]"
JOINT_WITH_MIN = "probabilities[min(first, second)]"
JOINT_AS_INDEPENDENT = "probabilities[first] * probabilities[second]"


def with_one_expression_changed(tmp_path: Path, before: str, after: str) -> ModuleType:
    """The wrapper's REAL source with one expression rewritten, imported as a second module.

    NEITHER A MOCK NOR A MONKEYPATCH. What runs is the body itself, on real data, with a real
    mistake put back into it -- which is the only way to watch a rule that no admissible INPUT can
    reach. ``tests/test_double_run_methods.py`` plants its controls the same way, by mirroring the
    tree with one thing changed; this is that device at the size of one expression.

    The substitution is asserted to match EXACTLY ONCE, so a rewrite of the block that moved the
    expression turns this red rather than quietly mutating nothing and leaving the assertions
    below to pass against an unmodified body.
    """
    source = Path(wrapper.__file__).read_text(encoding="utf-8")
    assert source.count(before) == 1, f"{before!r} appears {source.count(before)} time(s)"
    target = tmp_path / "ordered_choice_with_one_expression_changed.py"
    target.write_text(source.replace(before, after), encoding="utf-8")
    spec = importlib.util.spec_from_file_location(target.stem, target)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def payload_stubs(payload: object) -> list[str]:
    """Every ``@mcp_class`` a ``to_mcp`` refusal record names, anywhere in this payload."""
    found: list[str] = []
    if isinstance(payload, dict):
        if payload.get("@mcp_serialized") is False:
            return [str(payload["@mcp_class"][0])]
        for value in payload.values():
            found += payload_stubs(value)
    elif isinstance(payload, list):
        for item in payload:
            found += payload_stubs(item)
    return found


def finite_difference_effects(
    y: pd.Series, x: pd.DataFrame, *, link: str, step: float = 1e-5
) -> dict[str, dict[str, float]]:
    """The average marginal effects the SLOW way, from the fitted probabilities themselves.

    THE INDEPENDENT WITNESS FOR THE BODY'S OWN ARITHMETIC. The body evaluates equation (ME) --
    ``[f(mu_j - x'b) - f(mu_{j+1} - x'b)] b_k`` averaged over the sample -- which is the derivative
    written down. This re-fits nothing: it perturbs the DESIGN by +/- ``step`` and takes a central
    difference of ``OrderedModel.predict``, which is the definition of the same quantity by another
    route. Written here rather than imported, because importing the body's helper would compare
    that helper with itself.

    THE ARITHMETIC IS INDEPENDENT AND THE STOPPING RULE IS NOT, AND THE DIFFERENCE IS THE POINT.
    What this compares is two derivatives of the SAME fit, so the witness has to be standing at the
    same optimum: the optimiser, its iteration budget and its tolerance are read off the module
    under test rather than written a second time here. This used to pass ``method='lbfgs'`` and
    ``maxiter=2000`` with NO ``pgtol`` while the body pinned ``pgtol=1e-10``, and it passed only
    because it was run on the one table where the two optima coincide. MEASURED on McCullagh's,
    worst ``|analytic - numeric|``: 5.3365e-12 at the body's setting against 4.2554e-05 at the
    library default under the logit link, and 4.3622e-12 against 6.0719e-05 under the
    complementary log-log -- four orders past the ``abs`` this test asserts.
    """
    from statsmodels.miscmodels.ordinal_model import OrderedModel

    distribution: Any = stats.gumbel_l if link == "cloglog" else link
    model = OrderedModel(y, x, distr=distribution)
    result = model.fit(
        method=wrapper._METHOD,
        disp=0,
        maxiter=wrapper._MAXITER,
        pgtol=wrapper._STOPPING_TOLERANCE,
    )
    design = np.asarray(model.exog, dtype=float)
    effects: dict[str, dict[str, float]] = {}
    for column, name in enumerate(x.columns):
        up, down = design.copy(), design.copy()
        up[:, column] += step
        down[:, column] -= step
        slope = (
            np.asarray(model.predict(result.params, exog=up))
            - np.asarray(model.predict(result.params, exog=down))
        ) / (2.0 * step)
        effects[str(name)] = {
            str(level): float(value)
            for level, value in zip(model.labels, slope.mean(axis=0), strict=True)
        }
    return effects


class TestGatesBlock:
    """Class A -- one passing and one refused input for every declared gate."""

    def test_a_declared_link_passes_and_an_undeclared_one_is_refused_in_the_shipped_package(
        self,
    ) -> None:
        """GATE 1. THE SUITE CANNOT SEE THIS DEFECT FROM INSIDE ITSELF.

        ``tests/conftest.py`` installs ``beartype.claw`` over ``econflow_engine``, so under pytest
        a direct call with an undeclared ``link`` is stopped by the annotation before any gate
        runs. beartype is a DEV dependency and that comment says the hook must never move into the
        package, so the SHIPPED package has no such check. The three declared links return three
        different fits -- MEASURED on the published table, ``llf`` is -85.90816143633305 for logit,
        -85.64704926392842 for probit and -83.84775290215052 for cloglog -- so a value outside the
        set cannot be resolved to a nearest match without answering a different question.

        SO THE CALL IS MADE IN A SUBPROCESS, which loads no ``conftest`` and therefore installs no
        hook. That is the only configuration in which this assertion is about the package a user
        installs rather than about beartype.
        """
        assert fitted(link="probit")["link"] == "probit"
        assert fitted(link="cloglog")["link"] == "cloglog"

        program = textwrap.dedent(
            """
            import json
            import pandas as pd
            from econflow_engine.errors import GateError
            from econflow_engine.wrappers.c16_limited_dependent import ordered_choice

            counts = {1: (2, 1), 2: (10, 1), 3: (20, 7), 4: (13, 7), 5: (0, 5)}
            record, origin = [], []
            for level, (domestic, imported) in counts.items():
                record += [level] * (domestic + imported)
                origin += [0.0] * domestic + [1.0] * imported
            y = pd.Series(record, name="rep77")
            x = pd.DataFrame({"foreign": origin})
            out = {"module": ordered_choice.__file__}
            out["beartyped"] = hasattr(
                ordered_choice.ld_ordered_choice, "__beartype_wrapper__"
            )
            out["logit"] = ordered_choice.ld_ordered_choice(y=y, x=x, link="logit")["link"]
            for bad in ("X", "logistic", "", "LOGIT"):
                try:
                    got = ordered_choice.ld_ordered_choice(y=y, x=x, link=bad)
                    out[bad] = {"accepted": got["link"]}
                except GateError as exc:
                    out[bad] = {"refused": str(exc), "code": exc.detail_code}
            print(json.dumps(out))
            """
        )
        # PYTHONPATH IS PINNED TO THIS TREE'S OWN src/, AND THAT IS THE ASSERTION BEHIND THE
        # ASSERTION. pyproject.toml sets `pythonpath = ["src"]`, which pytest applies to ITSELF and
        # cannot pass to a child; a bare `python -c` from engine/ therefore imports whatever
        # econflow_engine is installed, and a green run against another checkout's source is the
        # one outcome this file must never produce.
        finished = subprocess.run(  # noqa: S603 - fixed argv, no shell
            [sys.executable, "-c", program],
            capture_output=True,
            text=True,
            check=False,
            timeout=180,
            cwd=ENGINE_ROOT,
            env={**os.environ, "PYTHONPATH": str(ENGINE_ROOT / "src")},
        )
        assert finished.returncode == 0, (
            f"the child exited {finished.returncode}; stderr:\n{finished.stderr}"
        )
        answered = json.loads(finished.stdout)
        assert answered["module"] == str(
            ENGINE_ROOT / "src/econflow_engine/wrappers/c16_limited_dependent/ordered_choice.py"
        ), f"the child imported {answered['module']}, which is not the tree under test"
        assert answered["beartyped"] is False
        assert answered["logit"] == "logit"
        for bad in ("X", "logistic", "", "LOGIT"):
            assert "refused" in answered[bad], f"{bad!r} was accepted: {answered[bad]}"
            assert answered[bad]["code"] == "precondition-domain"
            assert "is not one of the values this argument declares" in answered[bad]["refused"]
            assert repr(bad) in answered[bad]["refused"]

    @pytest.mark.parametrize("level", [0.0, 1.0, 1.5, -0.1])
    def test_a_level_inside_the_unit_interval_passes_and_an_endpoint_is_refused(
        self, level: float
    ) -> None:
        """GATE 2. MEASURED: ``conf_int`` validates nothing at all.

        On the published fit, ``conf_int(alpha=0.0)`` returns ``(-inf, inf)``, ``alpha=1.0``
        returns a point interval whose two bounds are the estimate, ``alpha=-1.0`` returns
        ``(nan, nan)`` and ``alpha=2.0`` returns ``(inf, -inf)`` -- an interval whose lower bound is
        above its upper one. Nothing in statsmodels refuses any of them.
        """
        assert fitted(conf_level=0.9)["coeftable"]["conf_low"].iloc[0] < PUBLISHED_COEFFICIENT

        y, x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=x, conf_level=level)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "conf_level" in str(refused.value)
        assert "open interval (0.0, 1.0)" in str(refused.value)

    def test_an_aligned_design_passes_and_a_shifted_index_is_refused(self) -> None:
        """GATE 3. pandas aligns on labels and this estimator does not: it takes the values."""
        assert fitted()["nobs"] == PUBLISHED_NOBS

        y, x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=x.set_axis(x.index + 66))
        assert refused.value.detail_code == "precondition-shape"
        assert "is not aligned with the response" in str(refused.value)

    def test_distinct_column_names_pass_and_a_repeated_one_is_refused(self) -> None:
        """GATE 4. MEASURED: a design naming one column twice is FITTED and says nothing.

        Handed ``foreign`` twice, statsmodels 0.14.6 returns the log-likelihood of the fit WITHOUT
        the copy -- -85.90816143633305 either way -- and puts the name in ``exog_names`` twice. Read
        back into a mapping keyed by name, which is what ``params`` is, one of the two coefficients
        silently replaces the other.
        """
        assert set(fitted()["params"]) == {"foreign"}

        y, x = published()
        twice = pd.concat([x, x], axis=1)
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=twice)
        assert refused.value.detail_code == "precondition-shape"
        assert "names ['foreign'] more than once" in str(refused.value)

    def test_a_complete_design_passes_and_a_missing_covariate_is_refused(self) -> None:
        """GATE 5. MEASURED: ``MissingDataError: exog contains inf or nans``.

        The message names neither the argument nor the column, and the same one answers for an
        infinity. THE HOLE IS PUT IN THE MIDDLE OF THE TABLE, not at either end: the first and last
        rows are the two positions an off-by-one in a scan would still reach.
        """
        assert fitted()["llf"] == pytest.approx(PUBLISHED_LLF, rel=1e-4)

        y, x = published()
        holed = x.copy()
        holed.iloc[33, 0] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=holed)
        assert refused.value.detail_code == "precondition-missing"
        assert 'x["foreign"]' in str(refused.value)
        assert "contains 1 missing" in str(refused.value)

    def test_a_finite_design_passes_and_an_infinite_covariate_is_refused(self) -> None:
        """GATE 5, the other half. The same library message answers for an infinity."""
        assert fitted()["nobs"] == PUBLISHED_NOBS

        y, x = published()
        holed = x.copy()
        holed.iloc[17, 0] = float("inf")
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=holed)
        assert refused.value.detail_code == "precondition-missing"
        assert "0 missing and 1 non-finite" in str(refused.value)

    def test_a_full_rank_design_passes_and_a_collinear_pair_is_refused(self) -> None:
        """GATE 6. MEASURED: a duplicated column under a DIFFERENT name is fitted silently.

        On a three-level sample, ``x`` carrying ``g`` and a copy called ``g2`` returned
        ``{'g': -33.759, 'b': 4.476, 'g2': 43.664}`` -- two coefficients for one column, neither of
        them identified, and no error. THE COPY IS GIVEN ITS OWN NAME on purpose: under the same
        name the duplicate-name rule answers first and this one is never reached.
        """
        assert set(fitted()["params"]) == {"foreign"}

        y, x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=x.assign(copy_of_foreign=x["foreign"]))
        assert refused.value.detail_code == "precondition-rank"
        assert "at least one column is a linear combination of the others" in str(refused.value)

    def test_a_design_with_columns_passes_and_one_with_none_is_refused(self) -> None:
        """GATE 6, the other edge. An ordered model with no covariates FITS.

        MEASURED: handed a frame of no columns statsmodels estimates the thresholds alone and
        returns ``llf = -65.91673732008657`` on a 60-row three-level sample. It is the null model
        rather than a mistake -- but every field this node promises about covariates would then be
        an empty mapping, and a payload of empty mappings reports nothing while looking like a
        result.
        """
        y, x = published()
        assert wrapper.ld_ordered_choice(y=y, x=x)["params"]

        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=pd.DataFrame(index=x.index))
        assert refused.value.detail_code == "precondition-shape"
        assert "has no columns" in str(refused.value)

    def test_an_ordered_outcome_passes_and_an_unordered_categorical_is_refused(self) -> None:
        """GATE 7. THE SILENT WRONG THIS BLOCKS IS THE WORST ONE THIS METHOD HAS.

        MEASURED against statsmodels 0.14.6: ``pd.Categorical(["low", "mid", "high"] * 22)``
        carries no order, and the level order it ends up with is LEXICOGRAPHIC --
        ``['high', 'low', 'mid']``. The model is built on that order and fits happily; what comes
        back is an estimate of a model in which "high" is the lowest category. The only complaint
        is a bare ``Warning`` -- not a subclass of any category a caller is likely to be filtering
        for -- reading "the endog has ordered == False, risk of capturing a wrong order for the
        categories". Under this suite's ``-W error`` that is a crash; in the shipped package it is
        a line on stderr, and the level order IS the model.
        """
        ordered_y, ordered_x = mccullagh_labelled()
        assert ordered_y.cat.ordered is True
        assert list(wrapper.ld_ordered_choice(y=ordered_y, x=ordered_x)["thresholds"]) == [
            "present|enlarged",
            "enlarged|greatly enlarged",
        ]

        unordered = pd.Series(
            pd.Categorical(ordered_y.astype(str)), index=ordered_y.index, name="tonsil_size"
        )
        assert unordered.cat.ordered is False
        assert list(unordered.cat.categories) == ["enlarged", "greatly enlarged", "present"], (
            "the level order this refusal exists to prevent is no longer the lexicographic one"
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=unordered, x=ordered_x)
        assert refused.value.detail_code == "precondition-domain"
        assert "is not available" in str(refused.value)
        assert "LEXICOGRAPHICALLY" in str(refused.value)

    def test_a_numeric_outcome_passes_and_a_column_of_words_is_refused(self) -> None:
        """GATE 7, the dtype with no order at all.

        MEASURED: a plain object column of the same words raises ``ValueError: Pandas data cast to
        numpy dtype of object. Check input data with np.asarray(data).`` -- a message about numpy
        that says nothing about ordering, which is the thing that was missing.
        """
        assert fitted()["nobs"] == PUBLISHED_NOBS

        ordered_y, ordered_x = mccullagh_labelled()
        words = pd.Series(
            ordered_y.astype(str).to_numpy(), index=ordered_y.index, dtype=object, name="size"
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=words, x=ordered_x)
        assert refused.value.detail_code == "precondition-domain"
        # "is not available" ALONE WOULD PROVE NOTHING: it is the boilerplate prefix every
        # refuse_a_combination message carries, so it stays green through any rewrite of the
        # authored reason. What this gate exists to say is asserted instead.
        assert 'whose dtype is object' in str(refused.value)
        assert "carries no such statement" in str(refused.value)
        assert "pandas Categorical with ordered=True" in str(refused.value)

    def test_a_complete_outcome_passes_and_a_missing_one_is_refused(self) -> None:
        """GATE 8. MEASURED: ``ValueError: NaN in dependent variable detected.``"""
        assert fitted()["nobs"] == PUBLISHED_NOBS

        y, x = published()
        holed = y.astype(float)
        holed.iloc[40] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=holed, x=x)
        assert refused.value.detail_code == "precondition-missing"
        assert '"y" contains 1 missing' in str(refused.value)

    def test_every_declared_level_realised_passes_and_an_empty_one_is_refused(self) -> None:
        """GATE 9. MEASURED: a declared level nobody observed is an unreadable crash.

        An ordered ``Categorical`` declaring four categories where the data realises three raises
        ``ValueError: shapes (240,2) and (1,) not aligned: 2 (dim 1) != 1 (dim 0)`` from deep inside
        the likelihood, and nothing in it names the level. It is also the fact that makes every
        dichotomy of the proportional-odds test non-empty, so it is gated here rather than argued.
        """
        ordered_y, ordered_x = mccullagh_labelled()
        assert len(wrapper.ld_ordered_choice(y=ordered_y, x=ordered_x)["thresholds"]) == 2

        widened = pd.Series(
            ordered_y.cat.add_categories(["colossal"]),
            index=ordered_y.index,
            name="tonsil_size",
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=widened, x=ordered_x)
        assert refused.value.detail_code == "precondition-domain"
        assert "colossal" in str(refused.value)
        assert "is not available" in str(refused.value)

    def test_two_levels_pass_and_a_constant_outcome_is_refused(self) -> None:
        """GATE 10. MEASURED: one level is a crash whose message is about array shapes.

        ``ValueError: shapes (240,2) and (0,) not aligned: 2 (dim 1) != 0 (dim 0)``, behind a
        ``RuntimeWarning: invalid value encountered in subtract``. TWO levels are ADMITTED: an
        ordered model over two categories is the ordinary binary logit, which is a real answer even
        though the test of proportional odds then has nothing to compare.
        """
        y, x = published()
        binary = pd.Series(
            np.where(y.to_numpy() > 3, 1, 0), index=y.index, name="rep77"
        )
        assert len(wrapper.ld_ordered_choice(y=binary, x=x)["thresholds"]) == 1

        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y * 0 + 3, x=x)
        assert refused.value.detail_code == "precondition-domain"
        assert "lies outside [2.0, inf]" in str(refused.value)

    def test_enough_observations_pass_and_too_few_are_refused(self) -> None:
        """GATE 11. MEASURED: three rows, one covariate and three categories is SILENT GARBAGE.

        statsmodels returns ``{'a': 40.435, '1/2': 21.355, '2/3': 3.717}`` with
        ``converged`` true and NOT ONE WARNING under ``warnings.simplefilter('always')`` -- the
        estimate has run off to infinity and every diagnostic says the fit is fine. The floor is
        tied to what is being estimated: one parameter per covariate, one per cut point, and at
        least one observation more than that.
        """
        assert fitted()["nobs"] == PUBLISHED_NOBS

        tiny_y = pd.Series([1, 2, 3], index=pd.RangeIndex(1, 4), name="y")
        tiny_x = pd.DataFrame({"a": [0.0, 1.0, 2.0]}, index=tiny_y.index)
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=tiny_y, x=tiny_x)
        assert refused.value.detail_code == "precondition-sample-size"
        assert "carries 3 observation(s); this method requires at least 4" in str(refused.value)

    def test_a_design_without_a_constant_passes_and_one_with_a_constant_is_refused(self) -> None:
        """GATE 12. The estimator's OWN refusal, translated rather than left as a traceback.

        No intercept is identified in this model: an intercept is a common shift of every cut
        point. statsmodels says so itself -- ``ValueError: There should not be a constant in the
        model`` -- and that exception escapes ``mcp/make_tool.py`` as a crash unless it is
        translated here, because only ``GateError`` becomes a clean refusal.
        """
        assert fitted()["nobs"] == PUBLISHED_NOBS

        y, x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=x.assign(const=1.0))
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(refused.value)
        assert "There should not be a constant in the model" in str(refused.value)

    def test_a_converged_fit_passes_and_one_that_stopped_early_is_refused(self) -> None:
        """GATE 13. ONE INPUT, TWO ROUTES, AND THE CALLER'S WARNING FILTER PICKS WHICH.

        MEASURED: a covariate on the scale of a population -- the published indicator beside a
        column of +/- 1e9 -- stops with ``converged`` FALSE and a ``ConvergenceWarning``. Under
        this suite's ``-W error`` the warning arrives first, from inside the fit, and is refused as
        the estimator's own objection; with warnings left as warnings the fit RETURNS, carrying
        whatever the last step held, and the convergence flag is the only thing that says so. The
        two are asserted separately because a body that gated only one of them would be correct
        under exactly one caller's settings.

        THE COLUMN ALTERNATES RATHER THAN RISING, AND THAT IS WHAT KEEPS THIS TEST ABOUT
        CONVERGENCE. It used to be ``np.linspace(-1, 1, 66) * 1e9``, which rises with the row
        number -- and the fixture's repair records are stored in ascending order, so that column
        ORDERS the outcome and GATE 15 now answers first. MEASURED, the alternating column reaches
        the estimator exactly as the rising one did and stops in the same place: existence margin
        0.0 against 4.355932e-08, ``converged`` False either way, and ``llf`` -89.89509769159048 in
        both. The scale is what defeats the optimiser here; the ordering was never part of it.
        """
        assert fitted()["llf"] == pytest.approx(PUBLISHED_LLF, rel=1e-4)

        y, x = published()
        enormous = x.assign(scaled=np.tile([-1.0, 1.0], len(x) // 2) * 1e9)
        with pytest.raises(GateError) as under_error:
            wrapper.ld_ordered_choice(y=y, x=enormous)
        assert under_error.value.detail_code == "precondition-degenerate"
        assert "the estimator refused these inputs" in str(under_error.value)

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with pytest.raises(GateError) as as_warnings:
                wrapper.ld_ordered_choice(y=y, x=enormous)
        assert as_warnings.value.detail_code == "precondition-degenerate"
        assert "did not converge" in str(as_warnings.value)

    def test_a_reportable_interval_passes_and_one_of_infinities_is_refused(self) -> None:
        """GATE 14. THE OUTPUT RULE, AND THE INPUT THAT REACHES IT IS NARROW.

        ``conf_level`` is refused at 1.0 by GATE 2, but 0.9999999999999999 is strictly less than
        1.0 as a double and passes it. MEASURED: ``1 - (1 - 0.9999999999999999) / 2`` evaluates to
        exactly ``1.0``, so the normal quantile is infinite and ``conf_int`` returns
        ``[-inf, inf]``. ``to_mcp`` renders both bounds as ``null`` and ``to_json`` writes no
        ``Infinity`` token, so a caller would receive well-formed JSON whose interval is simply
        empty -- and "empty" is not distinguishable from "not computed". Reporting it is not a
        weaker refusal; it IS the silent-null defect.
        """
        assert math.isfinite(fitted(conf_level=0.999999)["coeftable"]["conf_high"].iloc[0])

        y, x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_ordered_choice(y=y, x=x, conf_level=0.9999999999999999)
        assert refused.value.detail_code == "precondition-degenerate"
        assert "are not numbers" in str(refused.value)
        assert "conf_low" in str(refused.value)

    def test_a_likelihood_with_a_maximum_passes_and_a_separated_sample_is_refused(self) -> None:
        """GATE 15. AN ESTIMATE THAT DOES NOT EXIST, RETURNED AS A CLEAN SUCCESS.

        MEASURED before this rule, on 66 rows, three ordered levels and one covariate that orders
        them -- ``v = 0, 1, 2`` on the three blocks of 22::

            params {'v': 40.43612810638999}
            thresholds {'low|mid': 21.357, 'mid|high': 62.49}
            llf -3.5997591548270875e-07        <- the likelihood is 1, every row predicted exactly
            std_error 6794.844753480861  p_value 0.9952518161849278
            conf_low -13277.214869257039  conf_high 13358.08712546982

        ``converged`` was True, ``require_convergence`` passed, ``require_finite_estimates`` passed
        because every one of those numbers IS finite, and not one warning was raised under this
        suite's ``-W error``. THE REALISTIC FORM IS WORSE BECAUSE THE DESIGN LOOKS ORDINARY: with
        ``v`` a plain 0/1 indicator equal to 1 exactly on the top level, MEASURED
        ``params['v'] = 41.38347831712234``, ``std_error`` 8557.303858286064 and ``p_value``
        0.9961414120307419 -- and there the log-likelihood is -30.498, so nothing about the fit
        looks degenerate at all.

        THE FINITENESS RULE IS NOT THE ANSWER, AND THAT IS MEASURED RATHER THAN ASSUMED. Growing
        the same three blocks does not drive the standard error off the reals -- it merely shrinks
        it: 6794.844753480861 at 66 rows, 3150.8642906652785 at 300 and 1820.6365189014734 at 900,
        all with ``converged`` True and a log-likelihood at the floor. So a rule about the
        payload's numbers never sees this, however large the sample.

        BOTH COMMITTED TABLES ARE ADMITTED, and that is what keeps this from being a blanket rule.
        The ordered model's existence question is NOT the per-dichotomy one
        ``ld_proportional_odds_test`` asks: Stata's fourth cumulative dichotomy separates -- GATE 20
        refuses it -- and its ordered fit is published to seven significant digits all the same.
        """
        assert fitted()["llf"] == pytest.approx(PUBLISHED_LLF, rel=1e-4)
        tonsil_y, tonsil_x = mccullagh_labelled()
        assert wrapper.ld_ordered_choice(y=tonsil_y, x=tonsil_x)["nobs"] == 1398

        ordered_levels = ["low"] * 22 + ["mid"] * 22 + ["high"] * 22
        separated = pd.Series(
            pd.Categorical(ordered_levels, categories=["low", "mid", "high"], ordered=True),
            name="y",
        )
        for column in ([0.0] * 22 + [1.0] * 22 + [2.0] * 22, [0.0] * 44 + [1.0] * 22):
            with pytest.raises(GateError) as refused:
                wrapper.ld_ordered_choice(y=separated, x=pd.DataFrame({"v": column}))
            assert refused.value.detail_code == "precondition-degenerate"
            assert "the design separates the outcome" in str(refused.value)
            assert "'v'" in str(refused.value)
            assert "the ORDERED model's own" in str(refused.value)

    def test_a_column_name_carrying_a_payload_is_reported_and_never_evaluated(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """THE CONTROL FOR THE ONLY CALLER-CHOSEN TEXT THIS NODE CARRIES ONWARD.

        Neither node declares an argument of kind ``string``: ``link`` is an ``enum`` the wire
        model checks against the contract's own list, and ``conf_level`` and ``alpha`` are numbers.
        What IS caller-chosen text is the COLUMN NAMES of ``x`` and the LEVEL LABELS of ``y``, both
        of which become keys of this payload and are interpolated into refusal messages. The first
        2.2 body shipped a live remote code execution through an argument spliced into a formula,
        so the question is asked here rather than assumed: the payload below is the one that ran in
        that body, and a column name must merely be CARRIED and REPORTED. The marker is asserted in
        a ``finally`` so that it, and not the exception type, is what turns this red.
        """
        monkeypatch.delenv(INJECTION_MARKER, raising=False)
        y, x = published()
        named = x.rename(columns={"foreign": INJECTION_PAYLOAD})
        try:
            result = wrapper.ld_ordered_choice(y=y, x=named)
        finally:
            assert os.environ.get(INJECTION_MARKER) is None, (
                "THE PAYLOAD EXECUTED. A column name reached something that evaluates it, and "
                "this node's contract says nothing here does."
            )
        assert set(result["params"]) == {INJECTION_PAYLOAD}
        assert result["params"][INJECTION_PAYLOAD] == pytest.approx(
            PUBLISHED_COEFFICIENT, rel=1e-4
        )
        assert to_json(to_mcp(result))

    def test_an_undeclared_argument_is_refused_before_the_body_runs(self) -> None:
        """The wire contract, not the body: ``extra="forbid"`` on the model."""
        model = wrapper.wire_model(FIT_FN)
        with pytest.raises(ValueError, match="unknown_argument") as refused:
            model.model_validate({"y": "handle", "x": "handle", "unknown_argument": 1})
        assert "extra" in str(refused.value).lower()


class TestProportionalOddsGatesBlock:
    """Class A, continued -- the second node's own refusals."""

    def test_a_fit_from_this_node_passes_and_a_foreign_handle_is_refused(self) -> None:
        """GATE 16. ``fit`` is a ``raw_handle``: whatever the registry holds, untouched.

        The registry stores the WHOLE return of ``ld_ordered_choice``, so a caller can put any
        stored object behind this argument -- another node's payload, a frame, a string. None of
        them carries the fitted model this test has to rebuild its binary logits from, and reading
        a missing key would reach the caller as a ``KeyError`` traceback.
        """
        y, x = mccullagh()
        assert wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )["brant_test"]["parameter"] == 1

        for foreign in ({"auc": 0.9}, "a handle", 42, {"fit": "not a model"}):
            with pytest.raises(GateError) as refused:
                wrapper.ld_proportional_odds_test(fit=foreign)
            assert refused.value.detail_code == "precondition-domain"
            # NOT "is not available" ALONE. That is the boilerplate prefix every
            # refuse_a_combination message carries, so it survives any rewrite of the authored
            # reason and proves only that SOME refusal happened. The class the handle was
            # holding, the reason and the remedy are what this gate has to say.
            assert type(foreign).__name__ in str(refused.value)
            assert "it needs the ordered outcome and the covariates" in str(refused.value)
            assert "the whole result of that node and not one field of it" in str(refused.value)

    def test_a_logit_fit_passes_and_a_probit_one_is_refused(self) -> None:
        """GATE 17. Brant's test is a test of PROPORTIONAL ODDS, and odds are logistic.

        Brant (1990) section 3 embeds the model in ``logit gamma_j(x) = theta_j - beta_j' x`` and
        tests the equality of the ``beta_j`` estimated by ``J-1`` binary LOGISTIC regressions. A
        probit or complementary log-log fit is a different link, its coefficients are not log odds
        ratios, and the augmented family the test compares against is not the one it was fitted
        under.
        """
        y, x = mccullagh()
        assert wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x, link="logit")
        )["brant_test"]["method"] == "Brant (1990) omnibus Wald test of proportional odds"

        for link in ("probit", "cloglog"):
            with pytest.raises(GateError) as refused:
                wrapper.ld_proportional_odds_test(
                    fit=wrapper.ld_ordered_choice(y=y, x=x, link=link)
                )
            assert refused.value.detail_code == "precondition-domain"
            assert link in str(refused.value)

    @pytest.mark.parametrize("alpha", [0.0, 1.0, -0.5, 2.0])
    def test_an_alpha_inside_the_unit_interval_passes_and_an_endpoint_is_refused(
        self, alpha: float
    ) -> None:
        """GATE 18. ``alpha`` decides ``reject``, so it is a real argument and is checked."""
        y, x = mccullagh()
        fit = wrapper.ld_ordered_choice(y=y, x=x)
        assert wrapper.ld_proportional_odds_test(fit=fit, alpha=0.5)["alpha"] == 0.5

        with pytest.raises(GateError) as refused:
            wrapper.ld_proportional_odds_test(fit=fit, alpha=alpha)
        assert refused.value.detail_code == "precondition-domain"
        assert "alpha" in str(refused.value)
        assert "open interval (0.0, 1.0)" in str(refused.value)

    def test_three_levels_pass_and_a_binary_outcome_leaves_no_degrees_of_freedom(self) -> None:
        """GATE 19. With two categories there is one dichotomy and nothing to compare it with.

        The omnibus statistic has ``(J - 2) p`` degrees of freedom, so a binary outcome gives zero
        -- there is only one binary logit and the restriction it would be tested against is
        vacuous. A chi-squared statistic on zero degrees of freedom has a p-value of 0 whatever the
        data, which is a number that would be reported and read.
        """
        y, x = mccullagh()
        assert wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )["brant_test"]["parameter"] == 1

        published_y, published_x = published()
        binary = pd.Series(
            np.where(published_y.to_numpy() > 3, 1, 0), index=published_y.index, name="rep77"
        )
        with pytest.raises(GateError) as refused:
            wrapper.ld_proportional_odds_test(
                fit=wrapper.ld_ordered_choice(y=binary, x=published_x)
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "lies outside [1.0, inf]" in str(refused.value)

    def test_a_separable_dichotomy_is_refused_and_the_published_table_is_the_one_that_separates(
        self,
    ) -> None:
        """GATE 20. THE ORACLE CASE'S OWN DATASET IS WHAT THIS REFUSES, WHICH IS THE POINT.

        MEASURED on Stata's cross-tabulation: no domestic car has an Excellent 1977 record, so the
        fourth dichotomy ``1{rep77 > 4}`` is 45 zeros against 0 ones for domestic cars and 16
        against 5 for foreign ones. That is quasi-complete separation: the maximum-likelihood
        estimate does not exist, and ``sm.Logit`` returns ``[-21.146504, 19.983354]`` behind a
        ``ConvergenceWarning`` alone. Every one of the other three dichotomies is admitted, and so
        are both of McCullagh's, so the rule is discriminating rather than blanket. MEASURED with
        the intercept, the two committed tables read ``['ok', 'ok', 'ok', 'SEPARATED']`` and
        ``['ok', 'ok']``.

        IT IS NOT THE QUESTION GATE 15 ASKS, AND THE LINE ABOVE IS THE PROOF. The very fit this
        node refuses is the ORACLE CASE, published to seven significant digits -- so a separated
        cumulative dichotomy does not put the ordered model's own estimate out of reach, and this
        rule cannot be reused for it. The ordered model has its own existence programme.

        THE QUESTION IS ASKED OF THE DESIGN INCLUDING THE INTERCEPT, and that is load-bearing
        rather than incidental. MEASURED: over the covariate alone the same fourth dichotomy scores
        an objective of zero and is ADMITTED -- the covariate is an indicator, so no direction in
        it alone orders the outcome, and it is the intercept that makes the separating hyperplane
        exist. The binary logits this test fits carry an intercept, so that is the design the
        existence question belongs to.
        """
        y, x = mccullagh()
        assert wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )["brant_test"]["statistic"] > 0.0

        published_y, published_x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_proportional_odds_test(
                fit=wrapper.ld_ordered_choice(y=published_y, x=published_x)
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the design separates the outcome" in str(refused.value)
        assert "rep77 > 4" in str(refused.value)

    def test_the_separation_refusal_is_this_gates_own_and_not_the_estimators(self) -> None:
        """GATE 20'S OTHER HALF: WHOSE REFUSAL THE CALLER IS ACTUALLY READING.

        ``require_no_separation`` raises a ``GateError``, ``GateError`` IS a ``ValueError``
        (``errors.py``), and :func:`~econflow_engine.gates.estimation.is_estimator_refusal` admits
        any ``ValueError`` -- so this gate, called from inside the ``try`` that translates the
        ESTIMATOR's exceptions, came back to the caller as the estimator objecting to their data.
        MEASURED on the oracle dataset before it was moved out: two stacked
        ``ld_proportional_odds_test:`` prefixes, the internal class name ``GateError`` quoted at the
        caller, a doubled full stop where the authored remedy ended, and the per-dichotomy remedy
        buried inside a sentence about a fit that could not be estimated.

        THE TEST ABOVE CANNOT SEE ANY OF THAT, which is why this one exists beside it: both the
        ``detail_code`` and the substring "the design separates the outcome" survive the wrap
        unchanged, so every assertion it makes stays green while the message is wrong.
        """
        published_y, published_x = published()
        with pytest.raises(GateError) as refused:
            wrapper.ld_proportional_odds_test(
                fit=wrapper.ld_ordered_choice(y=published_y, x=published_x)
            )
        message = str(refused.value)
        assert message.startswith(f"{TEST_FN}: the design separates the outcome")
        assert message.count(f"{TEST_FN}:") == 1
        assert "the estimator refused these inputs" not in message
        assert "GateError" not in message
        assert ".." not in message

    def test_a_readable_design_passes_and_one_this_engines_arithmetic_cannot_read_is_refused(
        self,
    ) -> None:
        """GATE 21. ``fit`` IS A ``raw_handle``, SO ITS DESIGN IS WHATEVER A CALLER PUT THERE.

        The sibling node gates its own ``x`` for missing values and for rank, but nothing carries
        those facts across a handle: ``_the_stored_sample`` checks the SHAPE of what arrived and a
        caller may register any mapping. MEASURED before these two rules, both reported to the
        caller as the estimator objecting to their data, and neither sentence was true --

        * a design carrying a ``nan``: "It reported ValueError: Invalid input for linprog: c must
          not contain values inf, nan, or None" -- scipy complaining from inside this engine's own
          separation programme;
        * a design that is collinear ONCE THE INTERCEPT IS ADDED, which is the design the binary
          regressions are actually fitted on: "It reported LinAlgError: Singular matrix" from
          ``np.linalg.inv``. A constant column is full rank beside one covariate and is rank
          deficient beside that covariate AND an intercept, so the sibling node's own rank rule
          does not answer this one.
        """
        y, x = mccullagh()
        handle = wrapper.ld_ordered_choice(y=y, x=x)
        assert wrapper.ld_proportional_odds_test(fit=handle)["brant_test"]["parameter"] == 1

        holed = x.copy()
        holed.iloc[3, 0] = float("nan")
        with pytest.raises(GateError) as missing:
            wrapper.ld_proportional_odds_test(fit={**handle, "design": holed})
        assert missing.value.detail_code == "precondition-missing"
        assert "contains 1 missing" in str(missing.value)
        assert "the estimator refused these inputs" not in str(missing.value)

        with pytest.raises(GateError) as deficient:
            wrapper.ld_proportional_odds_test(
                fit={**handle, "design": x.assign(constant=1.0)}
            )
        assert deficient.value.detail_code == "precondition-rank"
        assert "at least one column is a linear combination of the others" in str(
            deficient.value
        )
        assert "the estimator refused these inputs" not in str(deficient.value)

    def test_a_positive_statistic_passes_and_a_negative_one_is_refused(
        self, tmp_path: Path
    ) -> None:
        """GATE 22. THE RULE THE BODY'S OWN DOCSTRING CALLS THE INVISIBLE MISTAKE.

        ``_brant_blocks`` uses ``pi_max(j,l) - pi_j pi_l`` because for ``j <= l`` the joint event
        ``y > j`` and ``y > l`` IS ``y > l``. Using ``min`` there returns a NEGATIVE chi-squared
        with a p-value of exactly 1.0 -- and a p-value of 1 is what a reader of a proportional-odds
        diagnostic hopes to see, so nothing about that output looks wrong. A Wald statistic cannot
        be negative, which is why one is refused rather than reported.

        NO ADMISSIBLE INPUT REACHES THIS RULE, so the mistake is put back rather than mocked: the
        body's own source, with that one expression rewritten, run on McCullagh's table. MEASURED,
        it returns -0.13397014178700709 -- the same figure the body's docstring records -- and the
        rule refuses it by name.

        THE PER-COVARIATE HALF IS THE SAME LINE AND IS RECORDED RATHER THAN ASSERTED. With one
        covariate the two statistics coincide and the omnibus is checked first, so a second
        committed table would not reach it. It IS reachable: with the joint covariance indefinite,
        the full quadratic form can stay positive while a covariate's sub-form does not, and
        searching four hundred drawn designs under the same mutation found one -- 707 rows, four
        levels, two covariates -- refused at ``"the Brant chi-squared for x0" =
        -0.0015404009306487563``. No contingency table small enough to commit reproduced it, so
        what stands here is the omnibus half of the loop plus GATE 23, whose refusal names a
        per-covariate entry.
        """
        y, x = mccullagh()
        sound = wrapper.ld_proportional_odds_test(fit=wrapper.ld_ordered_choice(y=y, x=x))
        assert sound["brant_test"]["statistic"] > 0.0

        changed = with_one_expression_changed(tmp_path, JOINT_PROBABILITY, JOINT_WITH_MIN)
        with pytest.raises(GateError) as refused:
            changed.ld_proportional_odds_test(fit=changed.ld_ordered_choice(y=y, x=x))
        assert refused.value.detail_code == "precondition-domain"
        assert "the Brant chi-squared for the omnibus statistic" in str(refused.value)
        assert "-0.13397014178700709" in str(refused.value)
        assert "lies outside [0.0, inf]" in str(refused.value)

    def test_reportable_statistics_pass_and_ones_that_are_not_numbers_are_refused(
        self, tmp_path: Path
    ) -> None:
        """GATE 23. THE STATISTIC HAS NO VALUE WHERE THE JOINT COVARIANCE CANNOT BE INVERTED.

        That is what ``require_finite_estimates``' remedy on this call already says, and until the
        ``LinAlgError`` in ``_wald`` was translated it described a path nothing could take:
        ``np.linalg.solve`` raised, the raise sat outside every ``try``, and the gate ran after it,
        so a singular contrast covariance left through the gateway as a crash.

        THE MISTAKE THAT REACHES IT IS THE ONE BRANT'S PAPER EXISTS TO CORRECT. Building the joint
        covariance as though the ``J - 1`` binary fits were INDEPENDENT makes every block
        ``pi_j pi_l - pi_j pi_l``, so ``V`` is the zero matrix and ``D V D'`` cannot be inverted.
        MEASURED with that one expression rewritten: both the omnibus statistic and the covariate's
        own come back ``nan``, and the refusal names them both rather than reporting a null.
        """
        y, x = mccullagh()
        sound = wrapper.ld_proportional_odds_test(fit=wrapper.ld_ordered_choice(y=y, x=x))
        assert math.isfinite(sound["brant_test"]["statistic"])
        assert math.isfinite(sound["by_variable"]["carrier"]["statistic"])

        changed = with_one_expression_changed(
            tmp_path, JOINT_PROBABILITY, JOINT_AS_INDEPENDENT
        )
        with pytest.raises(GateError) as refused:
            changed.ld_proportional_odds_test(fit=changed.ld_ordered_choice(y=y, x=x))
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the chi-squared statistics this method reports are not numbers" in str(
            refused.value
        )
        assert "'carrier'" in str(refused.value)
        assert "'the omnibus statistic'" in str(refused.value)


class TestStructure:
    """Class B -- the shape of the result, and that the wire can carry it."""

    def test_both_nodes_carry_exactly_their_declared_output_keys(self) -> None:
        """EXACT in both directions, against each node's own declaration."""
        declared = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        records = {node["fn"]: node["output_keys"] for node in declared["nodes"]}
        assert records[FIT_FN]["status"] == "declared", records[FIT_FN]
        assert set(records[FIT_FN]["keys"]) == FIT_KEYS
        assert records[TEST_FN]["status"] == "declared", records[TEST_FN]
        assert set(records[TEST_FN]["keys"]) == TEST_KEYS

        result = fitted()
        assert isinstance(result, dict)
        assert set(result) == FIT_KEYS

        y, x = mccullagh()
        assert set(wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )) == TEST_KEYS

    def test_the_payload_carries_no_serialisation_stub_anywhere(self) -> None:
        """A REGISTERING NODE THAT RETURNS AN OBJECT IS A NODE THIS ENGINE CANNOT PROVE.

        Card #523 registers this node's result, and the second node's argument is a handle to it,
        so the temptation is to put the fitted ``OrderedResults`` in the mapping and let the
        registry keep it. MEASURED, that is closed: ``to_mcp`` renders it as
        ``{'@mcp_class': ['OrderedResultsWrapper'], '@mcp_serialized': False, ...}`` and
        ``tests/controls/double_run.py`` refuses such a payload outright -- "the digest is taken
        over a class name and this gate has not run the body". So what the handle carries is DATA:
        the ordered outcome and the design, which is what the proportional-odds test re-fits over.
        This asserts the absence, in both nodes, rather than leaving it to the gate.
        """
        result = fitted()
        wire = to_mcp(result)
        assert set(wire) == FIT_KEYS
        assert payload_stubs(wire) == []

        y, x = mccullagh()
        test_wire = to_mcp(wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        ))
        assert payload_stubs(test_wire) == []
        assert set(test_wire) == TEST_KEYS

    def test_the_handle_carries_the_sample_the_second_node_re_fits_over(self) -> None:
        """The two fields that exist for the sibling node, asserted as the sample they are."""
        result = fitted()
        outcome, design = result["outcome"], result["design"]
        assert isinstance(outcome, pd.Series)
        assert isinstance(outcome.dtype, pd.CategoricalDtype)
        assert outcome.cat.ordered is True
        assert list(outcome.cat.categories) == [1, 2, 3, 4, 5]
        assert outcome.name == "rep77"
        assert isinstance(design, pd.DataFrame)
        assert list(design.columns) == ["foreign"]
        assert outcome.index.equals(design.index)
        assert len(outcome) == PUBLISHED_NOBS == len(design)

    def test_the_wire_carries_the_declared_order_the_body_argues_it_publishes(self) -> None:
        """WHAT ``outcome`` CLAIMS TO CARRY, ASSERTED ON THE WIRE AND NOT ON THE OBJECT.

        ``_the_reported_outcome``'s own docstring argues that the outcome is published as an
        ORDERED ``Categorical`` because it carries three things a column of codes does not -- the
        level LABELS, their ORDER, and the fact that the order was DECLARED rather than inferred --
        and card #523 repeats it. MEASURED before this test, that was false of what travels:
        ``to_mcp(fit)["outcome"]`` was ``{'values': [...], 'name': 'tonsil_size'}`` and the string
        "ordered" appeared nowhere in the payload.

        THE MECHANISM, because it is not visible from either end. ``serialize.py`` registers a
        ``pd.Categorical`` handler that emits ``{"values", "levels"}``, but the body wraps its
        Categorical in a ``pd.Series`` -- it has to, for the index the sibling node aligns against
        -- and ``singledispatch`` then picks the ``pd.Series`` handler, which flattens the column
        through ``tolist()``. Nothing was lost in process, which is why no test saw it: the second
        node reads the registry object, where the order is intact.
        """
        y, x = mccullagh_labelled()
        wire = to_mcp(wrapper.ld_ordered_choice(y=y, x=x))["outcome"]
        assert wire["levels"] == ["present", "enlarged", "greatly enlarged"]
        assert wire["ordered"] is True
        assert wire["name"] == "tonsil_size"
        assert wire["values"][0] == "present" and wire["values"][-1] == "greatly enlarged"
        assert json.loads(to_json(wire)) == wire

    def test_the_payload_round_trips_through_to_json(self) -> None:
        """No NaN token, no Infinity token: what orjson writes, json.loads reads."""
        for payload in (fitted(), fitted(link="probit"), fitted(link="cloglog")):
            wire = to_mcp(payload)
            blob = to_json(wire)
            assert "NaN" not in blob and "Infinity" not in blob
            assert json.loads(blob) == wire

    def test_the_fit_registers_and_the_test_of_it_does_not(self) -> None:
        """Card #523 registers one of its two nodes, and only one."""
        assert wrapper.NODE_META[FIT_FN].register_field == "fit"
        assert wrapper.NODE_META[TEST_FN].register_field is None

    def test_the_reported_cut_points_are_not_the_parameters_the_library_stores(self) -> None:
        """THE REPRESENTATION TRAP, ON THE PUBLISHED TABLE, WHERE IT IS AT ITS WORST.

        ``OrderedModel.transform_threshold_params`` is
        ``concatenate((th[:1], exp(th[1:]))).cumsum()``
        -- the first stored parameter IS the first cut point and every later one is the LOG of the
        increment to the next. MEASURED on Stata's 66 cars, where five categories mean four of
        them: the stored vector is (-2.7655669, 0.5705317, 0.6621604, 0.7796616) and the cut points
        are (-2.7655669, -0.9963594, 0.9426174, 3.1233515). The second entry differs by 1.567 AND
        BY ITS SIGN, and the stored vector is still MONOTONE INCREASING, so nothing downstream --
        no ordering check, no plot, no reader -- would notice. The published /cut2 is -.9963603.
        """
        from statsmodels.miscmodels.ordinal_model import OrderedModel

        y, x = published()
        model = OrderedModel(y, x, distr="logit")
        stored = np.asarray(
            model.fit(method="lbfgs", disp=0, maxiter=2000).params[model.k_vars :], dtype=float
        )
        assert bool(np.all(np.diff(stored) > 0)), "the stored vector is not monotone"

        reported = fitted()["thresholds"]
        assert list(reported) == list(PUBLISHED_THRESHOLDS)
        for label, published_value in PUBLISHED_THRESHOLDS.items():
            assert reported[label] == pytest.approx(published_value, rel=1e-4)
        assert len(stored) == len(PUBLISHED_THRESHOLDS)
        assert stored[1] == pytest.approx(0.5705317, abs=1e-6)
        assert reported["2|3"] == pytest.approx(-0.9963594, abs=1e-6)
        assert stored[1] > 0.0 > reported["2|3"]

    def test_the_threshold_standard_errors_are_another_parameterisations(self) -> None:
        """WHY ``coeftable`` CARRIES THE COVARIATES AND NO THRESHOLD ROW.

        ``bse`` reports the standard errors of the parameters the library STORES, and the last
        ``J - 2`` of those are log increments rather than cut points. MEASURED against the same
        page, which prints a standard error for each: the coefficient agrees at 9.2315e-08 and the
        FIRST cut point at 6.1775e-08 -- both are stored as themselves -- while the other three are
        4.3718e-02, 4.5772e-01 and 6.0102e-01 away. Reporting them beside the transformed cut
        points would pair an estimate with another parameterisation's uncertainty.
        """
        from statsmodels.miscmodels.ordinal_model import OrderedModel

        y, x = published()
        model = OrderedModel(y, x, distr="logit")
        errors = np.asarray(
            model.fit(method="lbfgs", disp=0, maxiter=2000).bse, dtype=float
        )
        disagreements = [
            abs(errors[i] - published) / published
            for i, published in enumerate(PUBLISHED_STANDARD_ERRORS)
        ]
        assert disagreements[0] < 1e-6
        assert disagreements[1] < 1e-6
        assert min(disagreements[2:]) > 1e-2

        table = fitted()["coeftable"]
        assert list(table["term"]) == ["foreign"]
        assert list(table.columns) == [
            "term", "estimate", "std_error", "z_value", "p_value", "conf_low", "conf_high",
        ]
        assert float(table["std_error"].iloc[0]) == pytest.approx(
            PUBLISHED_STANDARD_ERRORS[0], rel=1e-6
        )

    @pytest.mark.parametrize("table", ["stata", "mccullagh"])
    @pytest.mark.parametrize("link", ["logit", "probit", "cloglog"])
    def test_the_marginal_effects_are_the_derivative_they_claim_to_be(
        self, link: Literal["logit", "probit", "cloglog"], table: str
    ) -> None:
        """THE ARITHMETIC THIS BODY OWNS, CHECKED AGAINST ITS OWN DEFINITION.

        ``OrderedResults`` has NO ``get_margeff`` on statsmodels 0.14.6 -- ``hasattr`` is False --
        so every number under ``marginal_effects`` is this engine's, from equation (ME):
        ``dP(y = j)/dx_k = [f(mu_j - x'b) - f(mu_{j+1} - x'b)] b_k`` with ``f(+-inf) = 0``, averaged
        over the sample. :func:`finite_difference_effects` computes the same quantity by a central
        difference of the fitted probabilities, which is the derivative's definition.

        THE SINGLE HOME FOR THIS AGREEMENT, and it had three. MEASURED over BOTH committed tables
        and all three links, with the witness fitted at the body's own stopping rule, the worst
        ``|analytic - numeric|`` anywhere is 6.4009e-12 -- Stata's table under the logit link. The
        remaining five are 5.2496e-12, 2.4719e-12, 5.3365e-12, 2.6358e-12 and 4.3622e-12. That one
        figure is asserted here and quoted nowhere else; the oracle case's notes point at this test
        rather than carrying a second copy of it.

        THE SECOND TABLE IS THE ONE THE INVOCATION PAYLOAD USES, which is why it is here. Run on
        Stata's alone, this witness passed while standing at a different optimum from the body --
        see :func:`finite_difference_effects` for what that cost on McCullagh's.
        """
        y, x = published() if table == "stata" else mccullagh()
        covariate = "foreign" if table == "stata" else "carrier"
        analytic = wrapper.ld_ordered_choice(y=y, x=x, link=link)["marginal_effects"]
        numeric = finite_difference_effects(y, x, link=link)
        assert set(analytic) == set(numeric) == {covariate}
        for level, value in analytic[covariate].items():
            assert value == pytest.approx(numeric[covariate][level], abs=1e-10)

    def test_the_effects_sum_to_zero_across_categories(self) -> None:
        """A row has to end up in some category, so the derivatives of the shares cancel."""
        for link in ("logit", "probit", "cloglog"):
            effects = fitted(link=link)["marginal_effects"]["foreign"]
            assert len(effects) == 5
            assert sum(effects.values()) == pytest.approx(0.0, abs=1e-12)

    def test_a_positive_coefficient_carries_negative_effects_in_the_middle(self) -> None:
        """CARD #523's SECOND TRAP, ON THE PUBLISHED DATA RATHER THAN ON A SAMPLE CHOSEN FOR IT.

        The coefficient on ``foreign`` is +1.455878, and the sign of a coefficient fixes the
        direction for the LOWEST and HIGHEST categories only. MEASURED on Stata's own table, the
        five average effects are -0.061901, -0.167404, -0.079478, +0.206836 and +0.101948: three of
        the five are NEGATIVE under a positive coefficient, and the middle of the scale --
        `Average`, the third of five repair records -- is one of them. A reader who took the sign of
        the coefficient as the sign of the effect would have it backwards for three categories out
        of five.
        """
        result = fitted()
        assert result["params"]["foreign"] > 0.0
        effects = result["marginal_effects"]["foreign"]
        assert [round(effects[str(level)], 6) for level in (1, 2, 3, 4, 5)] == [
            -0.061901, -0.167404, -0.079478, 0.206836, 0.101948,
        ]
        assert sum(1 for value in effects.values() if value < 0.0) == 3

    def test_the_complementary_log_log_link_is_the_distribution_the_name_promises(self) -> None:
        """MEASURED: ``distr='cloglog'`` is not a value statsmodels 0.14.6 accepts at all.

        ``OrderedModel.__init__`` maps only the strings ``'probit'`` and ``'logit'`` and assigns
        anything else straight to ``self.distr``, expecting a scipy-style distribution, so the
        contract's own third link raises ``AttributeError: 'str' object has no attribute 'name'``
        -- not a refusal about the caller's data but an attribute error from inside the library.
        This node supplies the distribution instead. ``scipy.stats.gumbel_l`` IS the complementary
        log-log link: its CDF is ``1 - exp(-exp(x))``, and the two are bit-identical here.
        """
        assert float(stats.gumbel_l.cdf(0.3)) == float(1.0 - math.exp(-math.exp(0.3)))
        assert float(stats.gumbel_l.cdf(0.3)) == 0.7407231340091724

        from statsmodels.miscmodels.ordinal_model import OrderedModel

        y, x = published()
        with pytest.raises(AttributeError, match="'str' object has no attribute 'name'"):
            OrderedModel(y, x, distr="cloglog").fit(method="lbfgs", disp=0, maxiter=2000)

        result = fitted(link="cloglog")
        assert result["link"] == "cloglog"
        assert result["llf"] == pytest.approx(-83.84775290215052, rel=1e-6)

    def test_each_link_returns_a_different_fit(self) -> None:
        """The argument reaches the likelihood rather than being recorded and ignored.

        MEASURED on the published table: ``llf`` is -85.90816143633305 under logit,
        -85.64704926392842 under probit and -83.84775290215052 under cloglog.
        """
        likelihoods = {link: fitted(link=link)["llf"] for link in ("logit", "probit", "cloglog")}
        assert likelihoods["logit"] == pytest.approx(-85.90816143633305, rel=1e-6)
        assert likelihoods["probit"] == pytest.approx(-85.64704926392842, rel=1e-6)
        assert likelihoods["cloglog"] == pytest.approx(-83.84775290215052, rel=1e-6)
        assert len(set(likelihoods.values())) == 3

    def test_a_wider_confidence_level_widens_the_interval_and_moves_nothing_else(self) -> None:
        """``conf_level`` reaches the interval and no other field."""
        narrow = fitted(conf_level=0.5)
        wide = fitted(conf_level=0.99)
        assert float(wide["coeftable"]["conf_high"].iloc[0]) > float(
            narrow["coeftable"]["conf_high"].iloc[0]
        )
        assert float(wide["coeftable"]["conf_low"].iloc[0]) < float(
            narrow["coeftable"]["conf_low"].iloc[0]
        )
        assert wide["params"] == narrow["params"]
        assert wide["thresholds"] == narrow["thresholds"]
        assert wide["llf"] == narrow["llf"]

    def test_the_declared_defaults_are_read_from_the_contract_and_not_invented(self) -> None:
        """An omitted optional takes the value ``node-specs.json`` publishes, and no other."""
        assert wrapper.NODE_META[FIT_FN].defaults["link"] == "logit"
        assert wrapper.NODE_META[FIT_FN].defaults["conf_level"] == 0.95
        assert wrapper.NODE_META[TEST_FN].defaults["alpha"] == 0.05

        y, x = published()
        implied = wrapper.ld_ordered_choice(y=y, x=x)
        named = wrapper.ld_ordered_choice(y=y, x=x, link="logit", conf_level=0.95)
        assert to_json(to_mcp(implied)) == to_json(to_mcp(named))

        ordered_y, ordered_x = mccullagh()
        fit = wrapper.ld_ordered_choice(y=ordered_y, x=ordered_x)
        assert wrapper.ld_proportional_odds_test(fit=fit)["alpha"] == 0.05

    def test_the_coefficient_table_is_a_chart_this_engine_can_emit(self) -> None:
        """What ``chart_spec`` returns for this frame, and it is a table's worth of bars.

        Card #523 declares ``chart_kind: table``; ``_frame_spec`` plots every NUMERIC column
        against the row number, so the ``term`` column is dropped and six series come back. This
        test asserts what the engine emits rather than what the card means.
        """
        spec = chart_spec(fitted()["coeftable"], title="ordered logit")
        assert spec is not None
        assert_pure(spec)
        assert [series["name"] for series in spec["series"]] == [
            "estimate", "std_error", "z_value", "p_value", "conf_low", "conf_high",
        ]

    def test_the_published_paper_of_this_card_reproduces_at_the_precision_it_prints(self) -> None:
        """McCULLAGH (1980) TABLE 1, AND THE THREE DECIMALS THAT KEEP IT OUT OF THE ORACLE.

        p. 112 prints ``Delta-hat = 0.603 +/- 0.225; theta-hat_1 = -0.810 +/- 0.116; theta-hat_2 =
        1.061 +/- 0.118`` and p. 113 ``G^2 = 0.302 on one degree of freedom``. MEASURED here:
        0.6026415259338052, -0.809828952110833, 1.0613983374271192 and 0.3021876724632646 -- which
        are 5.9448e-04, 2.1117e-04, 3.7544e-04 and 6.2143e-04 relative from the printed figures and
        round to every one of them. Half a unit in the third decimal of 0.603 is 8.3e-04 of it, so
        no tolerance class in _policy.json can hold this comparison: `estimate-1e-4` refuses it by
        arithmetic rather than by measurement. The claim is therefore made at the precision the page
        carries, which is what ``round`` says and a tolerance class cannot.

        THE DEVIANCE IS COMPUTED HERE AND NOT READ OFF THE FIT, because statsmodels reports none
        for this model. It is ``2 sum n_ij log(n_ij / m_ij)`` over the six cells of Table 1, with
        ``m_ij`` the fitted cell counts -- the likelihood ratio against the saturated model, on
        ``(2-1)(3-1) - 1 = 1`` degree of freedom, which is the number the page states. The cell
        probabilities behind it are rebuilt from THE PAYLOAD -- the reported coefficient and the
        reported cut points, through the logistic CDF -- rather than from the estimator, so this
        checks the numbers a caller receives and not the ones the library holds.
        """
        y, x = mccullagh()
        result = wrapper.ld_ordered_choice(y=y, x=x)
        delta = result["params"]["carrier"]
        theta = list(result["thresholds"].values())
        assert round(delta, 3) == MCCULLAGH_DELTA
        assert (round(theta[0], 3), round(theta[1], 3)) == MCCULLAGH_THETA
        assert abs(delta - MCCULLAGH_DELTA) / MCCULLAGH_DELTA == pytest.approx(
            5.9448e-04, rel=1e-3
        )

        cuts = np.array([-np.inf, *result["thresholds"].values(), np.inf])
        linear = np.array([0.5, -0.5]) * delta
        cumulative = stats.logistic.cdf(cuts[None, :] - linear[:, None])
        probabilities = np.diff(cumulative, axis=1)
        observed = np.array([[19.0, 29.0, 24.0], [497.0, 560.0, 269.0]])
        expected = observed.sum(axis=1, keepdims=True) * probabilities
        deviance = 2.0 * float(np.sum(observed * np.log(observed / expected)))
        assert round(deviance, 3) == MCCULLAGH_DEVIANCE

    def test_the_standard_error_this_paper_prints_is_not_the_one_this_method_reports(self) -> None:
        """AND THAT DISAGREEMENT IS NOT ROUNDING, WHICH IS WHY NO STANDARD ERROR IS CLAIMED.

        McCullagh prints ``0.225`` for the same quantity this fit gives 0.22741574250766616 --
        1.0737e-02 apart, an order of magnitude beyond what three printed decimals can explain. His
        p. 112 quotes the same 0.225 for the generalized-empirical-logit estimator Delta-tilde
        immediately above, whose asymptotic variance is his equation (2.6), an EXPECTED-information
        formula; statsmodels reports the observed-information standard error. Two estimators of one
        quantity, and the oracle case claims neither.
        """
        y, x = mccullagh()
        table = wrapper.ld_ordered_choice(y=y, x=x)["coeftable"]
        ours = float(table["std_error"].iloc[0])
        assert ours == pytest.approx(0.22741574250766616, rel=1e-6)
        assert abs(ours - 0.225) / 0.225 == pytest.approx(1.0737e-02, rel=1e-3)

    def test_the_test_statistic_is_the_wald_form_two_ways(self) -> None:
        """THE BRANT STATISTIC, CHECKED AGAINST AN IDENTITY THE PAPER'S OWN ALGEBRA GIVES.

        With three categories and one covariate the omnibus statistic
        ``(D b)' [D V D']^-1 (D b)`` has a single row in ``D``, so it collapses to
        ``(b_1 - b_2)^2 / Var(b_1 - b_2)``. The body builds the general form; this rebuilds the
        scalar one from the same two binary logits by a second route. MEASURED on McCullagh's
        table, they agree to 1.7e-16 and the value is 0.31557010523209517 on one degree of freedom,
        p = 0.5742820912402614 -- proportional odds is not rejected for these data, which is the
        conclusion the paper reaches by other means.
        """
        import statsmodels.api as sm

        y, x = mccullagh()
        reported = wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )
        assert reported["brant_test"]["statistic"] == pytest.approx(
            0.31557010523209517, rel=1e-9
        )
        assert reported["brant_test"]["parameter"] == 1
        assert reported["brant_test"]["p_value"] == pytest.approx(
            0.5742820912402614, rel=1e-9
        )
        assert reported["reject"] is False

        codes = np.asarray(reported_codes(y), dtype=float)
        design = np.column_stack([np.ones(len(x)), x.to_numpy(dtype=float)])
        slopes, weights, inverses = [], [], []
        for cut in range(2):
            fit = sm.Logit((codes > cut).astype(float), design).fit(disp=0)
            slopes.append(float(np.asarray(fit.params)[1]))
            probability = np.asarray(fit.predict(), dtype=float)
            weights.append(probability)
            inverses.append(
                np.linalg.inv(design.T @ (design * (probability * (1 - probability))[:, None]))
            )
        blocks = {}
        for first in range(2):
            for second in range(2):
                joint = weights[max(first, second)] - weights[first] * weights[second]
                blocks[first, second] = (
                    inverses[first] @ (design.T @ (design * joint[:, None])) @ inverses[second]
                )[1, 1]
        variance = blocks[0, 0] + blocks[1, 1] - 2.0 * blocks[0, 1]
        identity = (slopes[0] - slopes[1]) ** 2 / variance
        assert identity == pytest.approx(reported["brant_test"]["statistic"], abs=1e-12)

    def test_the_restriction_is_watched_saying_yes_and_saying_no(self) -> None:
        """A TEST NOBODY HAS SEEN REJECT IS NOT YET A TEST.

        :func:`proportional` satisfies the restriction exactly -- the odds ratio is 19 at both cut
        points -- and the statistic there is 2.09e-28, which is zero to the precision the linear
        algebra carries. :func:`crossed` violates it as hard as three categories allow: 15.545455 at
        the first cut point against 0.064327 at the second. MEASURED, the statistic is 72.81 on one
        degree of freedom, p = 1.43e-17 -- AND THE PROPORTIONAL-ODDS FIT ITSELF REPORTS A SLOPE OF
        EXACTLY ZERO for the same data, because the table is symmetric under reversing the levels
        and swapping the groups so the two opposite effects cancel. A reader of that coefficient
        alone would conclude the group does not matter; the test is what says otherwise, which is
        the card's first interpretation trap made visible.
        """
        holds_y, holds_x = proportional()
        holds = wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=holds_y, x=holds_x)
        )
        assert holds["brant_test"]["statistic"] == pytest.approx(0.0, abs=1e-20)
        assert holds["brant_test"]["p_value"] > 0.999
        assert holds["reject"] is False

        fails_y, fails_x = crossed()
        fit = wrapper.ld_ordered_choice(y=fails_y, x=fails_x)
        assert fit["params"]["group"] == pytest.approx(0.0, abs=1e-8)
        fails = wrapper.ld_proportional_odds_test(fit=fit)
        assert fails["brant_test"]["statistic"] == pytest.approx(72.80995505827819, rel=1e-6)
        assert fails["brant_test"]["p_value"] < 1e-15
        assert fails["reject"] is True
        assert fails["by_variable"]["group"]["statistic"] == pytest.approx(
            fails["brant_test"]["statistic"], rel=1e-9
        )

    def test_alpha_decides_the_verdict_and_nothing_else(self) -> None:
        """``alpha`` is not recorded and ignored: it is the threshold ``reject`` is taken at."""
        y, x = mccullagh()
        fit = wrapper.ld_ordered_choice(y=y, x=x)
        default = wrapper.ld_proportional_odds_test(fit=fit)
        generous = wrapper.ld_proportional_odds_test(fit=fit, alpha=0.6)
        assert default["reject"] is False
        assert generous["reject"] is True
        assert generous["brant_test"] == default["brant_test"]
        assert generous["alpha"] == 0.6


class TestOracleCase:
    """Class C -- a published number, its citation and its tolerance class."""

    def test_the_published_number_is_reproduced_within_its_tolerance(self) -> None:
        """The committed case, loaded and run through the conformance harness itself.

        NOT a second comparison written here: ``admissible_calls`` applies the load rules and
        ``disagreement`` is the harness's own two-step comparison, so this test cannot be greener
        than the corpus gate is.
        """
        from tests.conformance.test_conformance import (
            admissible_calls,
            disagreement,
            run_call,
        )

        cases = [case for case in admissible_calls() if case.fn == FIT_FN]
        assert len(cases) == 1, [case.id for case in cases]
        case = cases[0]
        assert case.tolerance_class == "estimate-1e-4"

        state, payload = run_call(case)
        assert state == "succeeded", payload
        assert (
            disagreement(payload, case.expected, case.unchecked_keys, case.rtol, case.atol)
            is None
        )

    def test_the_agreement_with_the_page_is_the_one_the_case_records(self) -> None:
        """WHAT THE CASE'S NOTES CLAIM, MEASURED HERE SO A REGRESSION IS VISIBLE.

        A tolerance class that a payload clears by three orders of magnitude says nothing about
        HOW well it clears it, and the margin is what a later change to the optimiser would eat
        first. The worst of the six agreements is the third cut point, at 2.1959e-06 -- forty-five
        times inside the class the case is claimed at.
        """
        result = fitted()
        agreements = [
            abs(result["params"]["foreign"] - PUBLISHED_COEFFICIENT) / abs(PUBLISHED_COEFFICIENT),
            *(
                abs(result["thresholds"][label] - value) / abs(value)
                for label, value in PUBLISHED_THRESHOLDS.items()
            ),
            abs(result["llf"] - PUBLISHED_LLF) / abs(PUBLISHED_LLF),
        ]
        assert result["nobs"] == PUBLISHED_NOBS
        assert max(agreements) < 1e-5, agreements
        assert max(agreements) == pytest.approx(2.1959e-06, rel=1e-2)

    def test_the_second_node_has_no_published_number_and_the_case_directory_says_so(self) -> None:
        """CLASS C's ABSENCE, ASSERTED RATHER THAN LEFT AS A GAP NOBODY NOTICED.

        Brant (1990), doi:10.2307/2532457, prints an omnibus X^2 of 11.2 on 6 degrees of freedom
        for 83 donated livers and never prints the 83 x 7 design behind it, so nothing can be
        rebuilt to compare against; McCullagh prints his data and no Brant statistic. There is
        therefore no oracle case for ``ld_proportional_odds_test``, and this asserts that state of
        affairs so that adding one is a deliberate change to this test rather than a silent
        addition. Its arithmetic is checked instead by the identity route and by the two
        constructed tables in :class:`TestStructure`.
        """
        from tests.conformance.test_conformance import admissible_calls

        assert [case.id for case in admissible_calls() if case.fn == TEST_FN] == []
        cases = sorted(
            path.name
            for path in (ENGINE_ROOT / "tests" / "oracle" / "c16_limited_dependent").glob(
                "ordered_choice/*.json"
            )
        )
        assert cases == ["stata_r_ologit_example_1_repair_records.json"]


class TestDeterminism:
    """Class D -- identical inputs, identical bytes."""

    def test_two_identical_calls_serialise_to_identical_bytes(self) -> None:
        """Neither node is in ``stochastic_unseeded_fns``; read that rather than assume it."""
        specs = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        unseeded = specs["vocabulary"]["stochastic_unseeded_fns"]
        assert FIT_FN not in unseeded
        assert TEST_FN not in unseeded

        first = to_json(to_mcp(fitted()))
        second = to_json(to_mcp(fitted()))
        assert first == second
        assert len(first) > 0

        y, x = mccullagh()
        before = to_json(to_mcp(wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )))
        after = to_json(to_mcp(wrapper.ld_proportional_odds_test(
            fit=wrapper.ld_ordered_choice(y=y, x=x)
        )))
        assert before == after


def test_the_module_exports_every_function_its_card_names() -> None:
    """The one assertion a scaffold can make truthfully before a body exists."""
    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]
    assert not missing, missing
