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
from typing import Any

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

    def test_a_converged_fit_passes_and_a_separated_one_is_refused(self) -> None:
        """GATE 6. MEASURED: perfect separation returns coefficients of about +-57.

        The body runs the estimator under numpy's shipped error state, so this
        reaches ``require_convergence`` rather than an arithmetic exception whose
        occurrence depends on how the caller left ``np.seterr``. Nothing is
        relaxed here; that is the point of the scoping.
        """
        assert fitted()["coefficients"]

        separated = pd.DataFrame(
            {
                "x": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0],
                "y": [0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0],
            }
        )
        with pytest.raises(GateError) as refused:
            wrapper.run_binomial_fe_glm(formula="y ~ x", data=separated, link="logit")
        assert refused.value.detail_code == "precondition-degenerate"
        assert "did not converge" in str(refused.value)

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
