# SPDX-License-Identifier: AGPL-3.0-only
"""Tests for the wrapper module ``roc_auc_binary`` -- method card #84.

FOUR CLASSES, IN THIS ORDER. A is the gates block, B the shape of the result, C the oracle case and
D determinism.

THE DATA. Hanley and McNeil's Table I lives in ``tests/fixtures/hanley_mcneil_1982_ct_image_*`` and
is reached through ``build_fixture``, which is the code path the oracle case takes -- so a change to
the transcription moves this file's inputs with it. It is a 5 x 2 count table of 109 images, which
makes it a heavily tied score: 109 observations over five distinct ratings. That is the property
most of the assertions below need, because ties are where an area, a placement value and an
operating point each stop being obvious.

EVERYTHING ELSE HERE IS EIGHT ROWS BUILT IN THE TEST, and small on purpose: four controls scoring
1, 2, 3, 4 and four cases scoring 3, 4, 5, 6, whose area is 14/16 by hand and whose Youden point is
a THREE-WAY TIE. A published table cannot be relied on to carry a tie at its own maximum, and the
tie is what the card's "several rows on ties" promises.
"""

from __future__ import annotations

import json
import math
import os
import subprocess
import sys
import textwrap
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest

from econflow_engine.chart_spec import assert_pure, chart_spec
from econflow_engine.errors import GateError
from econflow_engine.serialize import to_json, to_mcp
from econflow_engine.wrappers.c16_limited_dependent import (
    roc_auc_binary as wrapper,
)

MODULE_FNS = ("run_roc",)

FN = "run_roc"
ENGINE_ROOT = Path(__file__).resolve().parents[3]

#: The payload this node promises, read off card #84's rewritten ``output_key_fields``.
#: :class:`TestStructure` asserts that ``node-specs.json`` declares the same set rather
#: than trusting either copy.
CARD_KEYS = frozenset(
    {
        "auc",
        "auc_ci",
        "roc_curve",
        "best_threshold",
        "n_cases",
        "n_controls",
        "controls_level",
        "cases_level",
        "direction",
        "percent",
    }
)

#: The area Hanley and McNeil print as ``2,642/(58 x 51)`` on p. 31, at the precision that
#: ratio of two published integers actually carries. The oracle case is where it is compared
#: against the page; this file uses it wherever a passing call has to assert a value.
PUBLISHED_AREA = 0.8931710615280595

#: The environment variable the payload writes, and the payload that writes it. Both are the
#: ones that RAN against the first 2.2 body before its formula gate, kept verbatim so the
#: control asks the question the attacker asked.
INJECTION_MARKER = "EF_RCE"
INJECTION_PAYLOAD = (
    f'__import__("os").environ.__setitem__("{INJECTION_MARKER}","pwned") or w'
)


def published() -> tuple[pd.Series, pd.Series]:
    """Hanley and McNeil's 109 CT images, through the real fixture loader.

    NOT a second transcription: ``build_fixture`` is the code path the oracle case takes,
    so a change to the dataset moves this file's inputs with it.
    """
    from tests.conformance.fixtures import build_fixture

    truth: pd.Series = build_fixture("hanley_mcneil_1982_ct_image_truth")
    rating: pd.Series = build_fixture("hanley_mcneil_1982_ct_image_rating")
    return truth, rating


def scored(**overrides: Any) -> dict[str, Any]:
    """One passing call on the published table, used by many assertions."""
    truth, rating = published()
    call: dict[str, Any] = {"response": truth, "predictor": rating, "direction": "<"}
    call.update(overrides)
    return wrapper.run_roc(**call)


def eight_rows() -> tuple[list[int], list[float]]:
    """Four controls at 1, 2, 3, 4 and four cases at 3, 4, 5, 6.

    THE AREA IS 14/16 BY HAND. Summing the tie-aware kernel of Hanley and McNeil's
    section IV over the sixteen pairs gives 2.5 + 3.5 + 4 + 4 = 14, and the two
    half-credits come from the two ties at 3 and at 4 -- so a body that scored a tie
    as a win or as a loss returns 0.90625 or 0.84375 instead.
    """
    return [0, 0, 0, 0, 1, 1, 1, 1], [1.0, 2.0, 3.0, 4.0, 3.0, 4.0, 5.0, 6.0]


def small(**overrides: Any) -> dict[str, Any]:
    """One passing call on those eight rows."""
    response, predictor = eight_rows()
    call: dict[str, Any] = {
        "response": response,
        "predictor": predictor,
        "direction": "<",
    }
    call.update(overrides)
    return wrapper.run_roc(**call)


def mann_whitney_variance(response: Any, predictor: Any) -> float:
    """DeLong's variance computed the SLOW way, from the kernel itself.

    THE INDEPENDENT WITNESS FOR THE BODY'S OWN ARITHMETIC, and it is written here
    rather than imported because importing the body's helper would compare that
    helper with itself. This is Hanley and McNeil's S(x_A, x_N) evaluated over every
    one of the n_A x n_N pairs -- the definition -- while the body computes the same
    placement values from midranks, which is Sun and Xu's (2014) O(n log n) form of
    it. Two routes to one quantity, and the test is that they agree.
    """
    labels = np.asarray(response)
    scores = np.asarray(predictor, dtype=float)
    cases = scores[labels == max(np.unique(labels))]
    controls = scores[labels == min(np.unique(labels))]
    difference = cases[:, None] - controls[None, :]
    kernel = np.where(difference > 0, 1.0, np.where(difference == 0, 0.5, 0.0))
    v10 = kernel.mean(axis=1)
    v01 = kernel.mean(axis=0)
    return float(np.var(v10, ddof=1)) / len(v10) + float(np.var(v01, ddof=1)) / len(v01)


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

    def test_a_supplied_direction_passes_and_an_absent_one_is_refused(self) -> None:
        """GATE 1. The contract publishes NO default for ``direction``.

        ``node-specs.json`` gives the argument ``has_default: false`` while its own
        description claims "default auto", so an omitted value reaches the body as
        ``None`` and stays ``None``. The two orientations return an area and one
        minus it, so there is no neutral answer to fall back on.
        """
        assert scored()["direction"] == "<"

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=truth, predictor=rating)
        assert refused.value.reason_code == "other"
        assert refused.value.detail_code == "precondition-domain"
        assert "was not supplied" in str(refused.value)
        assert "direction" in str(refused.value)

    def test_a_direction_outside_the_declared_enum_is_refused_in_the_shipped_package(
        self,
    ) -> None:
        """GATE 1b. THE SUITE CANNOT SEE THIS DEFECT FROM INSIDE ITSELF.

        ``tests/conftest.py`` installs ``beartype.claw`` over ``econflow_engine``,
        so under pytest a direct call with an undeclared ``direction`` is stopped
        by the annotation before any gate runs. beartype is a DEV dependency and
        that comment says the hook must never move into the package, so the
        SHIPPED package has no such check -- and the body resolved anything that
        was not ``'auto'`` with a bare ``str(direction)``, then oriented on
        ``resolved == '<'``. MEASURED without the hook: ``direction='X'`` returned
        an area of 0.0 where ``'<'`` returns 1.0, and reported ``'X'`` back under
        ``direction``. An inverted area under an orientation outside the enum,
        with no refusal.

        SO THE CALL IS MADE IN A SUBPROCESS, which loads no ``conftest`` and
        therefore installs no hook. That is the only configuration in which this
        assertion is about the package a user installs rather than about beartype.
        """
        program = textwrap.dedent(
            """
            import json
            import numpy as np
            from econflow_engine.errors import GateError
            from econflow_engine.wrappers.c16_limited_dependent import roc_auc_binary

            out_tree = roc_auc_binary.__file__
            truth = np.array([0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0])
            score = np.array([0.1, 0.9, 0.2, 0.8, 0.7, 0.3, 0.6, 0.55, 0.4, 0.45])
            out = {"module": out_tree}
            # The hook really is absent, or this proves nothing.
            out["beartyped"] = hasattr(roc_auc_binary.run_roc, "__beartype_wrapper__")
            passing = roc_auc_binary.run_roc(
                response=truth, predictor=score, direction="<", ci=False
            )
            out["area_for_lt"] = passing["auc"]
            for bad in ("X", "less", "", "ascending"):
                try:
                    got = roc_auc_binary.run_roc(
                        response=truth, predictor=score, direction=bad, ci=False
                    )
                    out[bad] = {"auc": got["auc"], "direction": got["direction"]}
                except GateError as exc:
                    out[bad] = {"refused": str(exc), "code": exc.detail_code}
            print(json.dumps(out))
            """
        )
        # PYTHONPATH IS PINNED TO THIS TREE'S OWN src/, AND THAT IS THE ASSERTION
        # BEHIND THE ASSERTION. pyproject.toml sets `pythonpath = ["src"]`, which
        # pytest applies to ITSELF and cannot pass to a child; a bare
        # `python -c` from engine/ therefore imports whatever econflow_engine is
        # installed. MEASURED: under this repository's own `uv run --project ..`
        # that resolves to this worktree, but under another checkout's virtualenv
        # it resolved to THAT tree instead -- where run_roc is still a stub. A
        # green run against the wrong source is the one outcome this file must
        # never produce, so the path is pinned and the module the child actually
        # imported is asserted below.
        finished = subprocess.run(  # noqa: S603 - fixed argv, no shell
            [sys.executable, "-c", program],
            capture_output=True,
            text=True,
            check=False,
            timeout=120,
            cwd=ENGINE_ROOT,
            env={**os.environ, "PYTHONPATH": str(ENGINE_ROOT / "src")},
        )
        assert finished.returncode == 0, (
            f"the child exited {finished.returncode}; stderr:\n{finished.stderr}"
        )
        answered = json.loads(finished.stdout)
        assert answered["module"] == str(
            ENGINE_ROOT / "src/econflow_engine/wrappers/c16_limited_dependent/roc_auc_binary.py"
        ), f"the child imported {answered['module']}, which is not the tree under test"
        assert answered["beartyped"] is False
        assert answered["area_for_lt"] == 1.0
        for bad in ("X", "less", "", "ascending"):
            assert "refused" in answered[bad], f"{bad!r} was accepted: {answered[bad]}"
            assert answered[bad]["code"] == "precondition-domain"
            assert "is not one of the values this argument declares" in answered[bad][
                "refused"
            ]
            assert repr(bad) in answered[bad]["refused"]

    @pytest.mark.parametrize("level", [0.0, 1.0, 1.5, -0.1])
    def test_a_level_inside_the_unit_interval_passes_and_an_endpoint_is_refused(
        self, level: float
    ) -> None:
        """GATE 2. MEASURED: at ``conf_level`` 1 the normal quantile is ``inf``.

        ``scipy.stats.norm.ppf(1.0)`` is ``inf`` and ``norm.ppf(0.5)`` -- which is
        where ``conf_level = 0`` lands -- is ``0.0``, so one endpoint gives an
        interval of infinite width and the other an interval of no width at all.
        Neither is refused by anything in scipy.
        """
        assert scored(conf_level=0.9)["auc_ci"]["conf_level"] == 0.9

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth, predictor=rating, direction="<", conf_level=level
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "conf_level" in str(refused.value)
        assert "open interval (0.0, 1.0)" in str(refused.value)

    def test_a_complete_predictor_passes_and_a_missing_one_is_refused(self) -> None:
        """GATE 3. MEASURED: one NaN in the score raises ``ValueError: Input contains NaN``.

        The message names no argument, so a caller cannot tell whether the response
        or the predictor carried it. THE HOLE IS PUT IN THE MIDDLE OF THE TABLE and
        not at either end: the first and last rows are the two positions an off-by-one
        in a scan would still reach.
        """
        assert scored()["n_cases"] == 51

        truth, rating = published()
        holed = rating.astype(float)
        holed.iloc[54] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=truth, predictor=holed, direction="<")
        assert refused.value.detail_code == "precondition-missing"
        assert '"predictor" contains 1 missing' in str(refused.value)

    def test_a_finite_predictor_passes_and_an_infinite_one_is_refused(self) -> None:
        """GATE 3, the other half. MEASURED: an infinity raises out of sklearn's check.

        ``ValueError: Input contains infinity or a value too large for
        dtype('float64')`` -- again naming no argument. An infinite score is also the
        one value that would survive as a THRESHOLD into the reported curve.
        """
        assert scored()["n_controls"] == 58

        truth, rating = published()
        holed = rating.astype(float)
        holed.iloc[17] = float("inf")
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=truth, predictor=holed, direction="<")
        assert refused.value.detail_code == "precondition-missing"
        assert "0 missing and 1 non-finite" in str(refused.value)

    def test_a_numeric_predictor_passes_and_a_text_one_is_refused(self) -> None:
        """GATE 3, the dtype half. MEASURED: a column of digit strings raises.

        ``ValueError: dtype='numeric' is not compatible with arrays of
        bytes/strings.`` A score is a number and a value that merely looks like one
        is not silently converted here either.
        """
        assert scored()["auc"] == pytest.approx(PUBLISHED_AREA, rel=1e-12)

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth, predictor=rating.astype(str), direction="<"
            )
        assert refused.value.detail_code == "precondition-shape"
        assert '"predictor" is not numeric' in str(refused.value)

    def test_a_vector_predictor_passes_and_a_frame_is_refused(self) -> None:
        """GATE 3, the shape half. MEASURED: sklearn answers a 2-D score with

        ``ValueError: y should be a 1d array, got an array of shape (109, 2)``,
        which is true and says nothing about which argument this node calls it.
        """
        assert scored()["roc_curve"].shape == (5, 3)

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth,
                predictor=pd.DataFrame({"a": rating, "b": rating}),
                direction="<",
            )
        assert refused.value.detail_code == "precondition-shape"
        assert '"predictor" is a DataFrame' in str(refused.value)

    def test_a_complete_response_passes_and_a_missing_one_is_refused(self) -> None:
        """GATE 4. MEASURED: a missing label is not one refusal but two.

        A float response carrying a ``nan`` raises ``ValueError: Input y_true
        contains NaN`` behind ``RuntimeWarning: invalid value encountered in cast``
        -- and under this suite's ``-W error`` the warning arrives first. An OBJECT
        response carrying ``None`` raises ``ValueError: unknown format is not
        supported`` instead. The rule is asked of a missingness MASK of the response
        rather than of the response itself, so that one question covers both, and
        covers a response of strings, which no numeric rule can read at all.
        """
        assert scored()["n_cases"] + scored()["n_controls"] == 109

        truth, rating = published()
        holed = truth.astype(float)
        holed.iloc[61] = float("nan")
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=holed, predictor=rating, direction="<")
        assert refused.value.detail_code == "precondition-missing"
        assert '"response" contains 1 missing' in str(refused.value)

    def test_a_missing_label_is_refused_when_the_response_is_text(self) -> None:
        """GATE 4, on the dtype the numeric rules cannot see at all.

        A response of the words the table prints, with one label absent. Nothing in
        ``gates.primitives`` reads a column of strings, which is why the question is
        put to a mask.
        """
        truth, rating = published()
        words = truth.map({0: "normal", 1: "abnormal"}).astype(object)
        assert wrapper.run_roc(
            response=words, predictor=rating, direction=">"
        )["cases_level"] == "normal"

        words.iloc[3] = None
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=words, predictor=rating, direction=">")
        assert refused.value.detail_code == "precondition-missing"
        assert '"response" contains 1 missing' in str(refused.value)

    def test_a_vector_response_passes_and_a_frame_is_refused(self) -> None:
        """GATE 4, the shape half, asked through the same mask."""
        assert scored()["percent"] is False

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=pd.DataFrame({"a": truth, "b": truth}),
                predictor=rating,
                direction="<",
            )
        assert refused.value.detail_code == "precondition-shape"
        assert '"response" has 2 dimension(s)' in str(refused.value)

    def test_an_aligned_predictor_passes_and_a_shifted_index_is_refused(self) -> None:
        """GATE 5. MEASURED: scikit-learn pairs the two arguments POSITIONALLY.

        Two Series whose indexes do not overlap at all -- labels 1..109 against
        110..218 -- return the SAME area, 0.8931710615280595, with no warning of any
        kind. pandas aligns on labels and this library does not; nothing in the
        result records which of the two happened.
        """
        assert scored()["auc"] == pytest.approx(PUBLISHED_AREA, rel=1e-12)

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth,
                predictor=rating.set_axis(rating.index + 109),
                direction="<",
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "is not aligned with the response" in str(refused.value)

    def test_equal_lengths_pass_and_a_short_predictor_is_refused(self) -> None:
        """GATE 5, the length half. MEASURED: sklearn reports only the two numbers.

        ``ValueError: Found input variables with inconsistent numbers of samples:
        [109, 108]`` names neither argument.
        """
        assert scored()["roc_curve"].shape[0] == 5

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth, predictor=rating.iloc[:-1], direction="<"
            )
        assert refused.value.detail_code == "precondition-shape"
        assert "108 label(s) against the response's 109" in str(refused.value)

    def test_two_levels_pass_and_a_third_one_is_refused(self) -> None:
        """GATE 6. MEASURED: a third level raises a message about an argument this node

        does not carry -- ``ValueError: multi_class must be in ('ovo', 'ovr')`` --
        because ``roc_auc_score`` reads a three-level target as a multiclass request.
        THE THIRD LEVEL IS ONE ROW IN THE MIDDLE OF THE TABLE, which is the hardest
        place for it to survive: a body that read only the first and last labels, or
        that counted levels from a sample of the column, would miss it.
        """
        assert scored()["n_cases"] == 51

        truth, rating = published()
        third = truth.astype(object)
        third.iloc[54] = "questionable"
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=third, predictor=rating, direction="<")
        assert refused.value.detail_code == "precondition-domain"
        assert "lies outside [2.0, 2.0]" in str(refused.value)
        assert "'questionable'" in str(refused.value)

    def test_the_refusal_names_the_levels_it_found_and_stops_naming_them(self) -> None:
        """GATE 6's MESSAGE, and the reason it is capped.

        A response is DATA rather than a schema: a column handed to this node by
        mistake carries as many distinct values as it has rows, and the rating
        column is exactly that mistake -- five levels here, and a continuous score
        would be 109. The message names what a caller needs to see and then says
        how many it did not name, rather than putting the input on the wire.
        """
        _, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=rating, predictor=rating, direction="<")
        assert refused.value.detail_code == "precondition-domain"
        assert "= 5.0 lies outside [2.0, 2.0]" in str(refused.value)
        assert "of which [1, 2, 3, 4, 5]" in str(refused.value)
        assert "more" not in str(refused.value)

        many = pd.Series(range(20))
        with pytest.raises(GateError) as capped:
            wrapper.run_roc(response=many, predictor=many.astype(float), direction="<")
        assert "of which [0, 1, 10, 11, 12, 13, 14, 15] and 12 more" in str(capped.value)

    def test_two_levels_pass_and_a_single_class_response_is_refused(self) -> None:
        """GATE 6, the other side. MEASURED: one class returns ``nan``, not an error.

        ``roc_auc_score`` over a response of all ones returns ``nan`` behind
        ``UndefinedMetricWarning: Only one class is present in y_true``, and
        ``roc_curve`` returns a false-positive rate that is ``nan`` in every row
        behind a warning of its own. ``sklearn.exceptions`` is not one of the
        packages ``is_estimator_refusal`` reads as an estimator, so under this
        suite's ``-W error`` that warning is a CRASH, and with warnings left as
        warnings the area reaches the wire as ``null``.
        """
        assert scored()["n_controls"] == 58

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth * 0 + 1, predictor=rating, direction="<"
            )
        assert refused.value.detail_code == "precondition-domain"
        assert "lies outside [2.0, 2.0]" in str(refused.value)

    def test_orderable_levels_pass_and_an_unorderable_pair_is_refused(self) -> None:
        """GATE 7. Which level is the case is decided by ORDER, so it needs one.

        A column of zeros whose missing values were written as the string ``NA`` has
        exactly two levels and no order between them: Python answers ``0 < 'NA'``
        with a ``TypeError``, which is not a ``GateError`` and would leave this node
        as a crash. THE STRING SITS IN THE MIDDLE OF THE COLUMN for the reason the
        third-level test gives.
        """
        assert scored()["cases_level"] == 1

        truth, rating = published()
        mixed = truth.astype(object)
        mixed.iloc[:] = 0
        mixed.iloc[40:60] = "NA"
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=mixed, predictor=rating, direction="<")
        assert refused.value.detail_code == "precondition-domain"
        assert "ranking the two levels of the response" in str(refused.value)

    def test_two_of_each_pass_and_a_single_case_is_refused_only_when_the_ci_is_asked_for(
        self,
    ) -> None:
        """GATE 8. MEASURED: one case makes the DeLong variance undefined, loudly or quietly.

        ``np.var(x, ddof=1)`` over one observation raises ``RuntimeWarning: Degrees
        of freedom <= 0 for slice`` -- a crash under this suite's ``-W error`` -- and
        returns ``nan`` with warnings left as warnings, which reaches the wire as an
        interval of two nulls. The area itself is perfectly well defined over one
        case, so the rule is asked only where the variance is: with ``ci=False`` the
        same data returns.
        """
        response = [0, 0, 0, 1]
        predictor = [1.0, 2.0, 3.0, 4.0]
        assert wrapper.run_roc(
            response=response, predictor=predictor, direction="<", ci=False
        )["auc"] == 1.0

        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=response, predictor=predictor, direction="<")
        assert refused.value.detail_code == "precondition-sample-size"
        assert "carries 1 observation(s); this method requires at least 2" in str(
            refused.value
        )

    def test_a_score_that_discriminates_passes_and_a_constant_one_is_refused(self) -> None:
        """GATE 9. MEASURED: a constant score returns an area of 0.5 with NO warning,

        and a DeLong variance of exactly 0.0 beside it -- so the interval is
        ``(0.5, 0.5)``, a 95 % interval of no width at all, reported as though it
        were one. The area is an honest answer and is returned when no interval is
        asked for; the interval is not.
        """
        assert scored()["auc_ci"]["low"] < scored()["auc"] < scored()["auc_ci"]["high"]

        truth, rating = published()
        flat = pd.Series(np.full(len(rating), 3.0), index=rating.index)
        assert wrapper.run_roc(
            response=truth, predictor=flat, direction="<", ci=False
        )["auc"] == 0.5

        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=truth, predictor=flat, direction="<")
        assert refused.value.detail_code == "precondition-domain"
        assert "the DeLong variance of the AUC" in str(refused.value)
        assert "open interval (0.0, inf)" in str(refused.value)

    def test_the_same_rule_refuses_a_perfectly_separated_score(self) -> None:
        """GATE 9, ON THE CASE AN INPUT RULE COULD NEVER SEE.

        The score below is not constant, not missing, not tied and not degenerate by
        any question asked of an argument: four controls at 0.1, 0.2 and four cases
        at 0.8, 0.9. Every case outranks every control, so every placement value is
        1 and every co-placement value is 0, both variances are exactly zero, and
        the reported interval would be ``(1.0, 1.0)``. This is why the rule is asked
        of the variance the body COMPUTED rather than of the score it was given.
        """
        response = [0, 0, 1, 1]
        predictor = [0.1, 0.2, 0.8, 0.9]
        assert wrapper.run_roc(
            response=response, predictor=predictor, direction="<", ci=False
        )["auc"] == 1.0

        with pytest.raises(GateError) as refused:
            wrapper.run_roc(response=response, predictor=predictor, direction="<")
        assert refused.value.detail_code == "precondition-domain"
        assert "the DeLong variance of the AUC" in str(refused.value)

    def test_a_reportable_interval_passes_and_one_of_infinities_is_refused(self) -> None:
        """GATE 10. THE OUTPUT RULE, AND THE INPUT THAT REACHES IT IS NARROW.

        ``conf_level`` is refused at 1.0 by GATE 2, but 0.9999999999999999 is
        strictly less than 1.0 as a double and passes it. MEASURED: ``1 - (1 -
        0.9999999999999999) / 2`` evaluates to exactly ``1.0``, so
        ``scipy.stats.norm.ppf`` returns ``inf`` and the interval is
        ``(-inf, inf)``. ``to_mcp`` renders both bounds as ``null`` and ``to_json``
        writes no ``Infinity`` token, so what a caller would receive is well-formed
        JSON whose interval is simply empty -- which is also how this payload
        reports ``auc_ci`` when no interval was asked for. The two must not be
        indistinguishable.
        """
        assert math.isfinite(scored(conf_level=0.999999)["auc_ci"]["high"])

        truth, rating = published()
        with pytest.raises(GateError) as refused:
            wrapper.run_roc(
                response=truth,
                predictor=rating,
                direction="<",
                conf_level=0.9999999999999999,
            )
        assert refused.value.detail_code == "precondition-degenerate"
        assert "the lower bound of the interval" in str(refused.value)
        # THE WHOLE PHRASE, NOT ITS TAIL. Asserting "are not numbers" alone passed
        # over a doubled clause: the gate writes "the {quantity} this method
        # reports", and the caller sent "area and interval this method reports",
        # so the message read "the area and interval this method reports this
        # method reports are not numbers".
        assert "the area and interval this method reports are not numbers" in str(
            refused.value
        )
        assert "reports this method reports" not in str(refused.value)

    def test_a_response_label_carrying_a_payload_is_reported_and_never_evaluated(
        self, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """THE CONTROL FOR THE ONLY CALLER-CHOSEN TEXT THIS NODE CARRIES ONWARD.

        This node declares no argument of kind ``string``: ``direction`` is an enum
        the wire model checks against the contract's own list, and ``ci`` and
        ``conf_level`` are a boolean and a number. What IS caller-chosen text is the
        CONTENT of ``response``, which is kind ``raw_handle`` -- the stored object,
        untouched -- and whose two level labels are echoed into the payload under
        ``controls_level`` and ``cases_level`` and into this module's own refusal
        messages. The first 2.2 body shipped a live remote code execution through an
        argument spliced into a formula, so the question is asked here rather than
        assumed: the payload below is the one that ran in that body, and a level
        label must merely be COMPARED and REPORTED. The marker is asserted in a
        ``finally`` so that it, and not the exception type, is what turns this red.
        """
        monkeypatch.delenv(INJECTION_MARKER, raising=False)
        truth, rating = published()
        labelled = truth.map({0: INJECTION_PAYLOAD, 1: "zzz_case"}).astype(object)
        try:
            result = wrapper.run_roc(
                response=labelled, predictor=rating, direction="<"
            )
        finally:
            assert os.environ.get(INJECTION_MARKER) is None, (
                "THE PAYLOAD EXECUTED. A response label reached something that "
                "evaluates it, and this node's contract says nothing here does."
            )
        assert result["controls_level"] == INJECTION_PAYLOAD
        assert result["cases_level"] == "zzz_case"
        assert result["auc"] == pytest.approx(PUBLISHED_AREA, rel=1e-12)
        assert to_json(to_mcp(result))

    def test_an_undeclared_argument_is_refused_before_the_body_runs(self) -> None:
        """The wire contract, not the body: ``extra="forbid"`` on the model."""
        model = wrapper.wire_model(FN)
        with pytest.raises(ValueError, match="unknown_argument") as refused:
            model.model_validate(
                {"response": "handle", "predictor": "handle", "unknown_argument": 1}
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

        result = scored()
        assert isinstance(result, dict)
        assert set(result) == CARD_KEYS

    def test_the_payload_walks_to_mcp_with_no_serialisation_stub(self) -> None:
        """A stub in the payload is a value the wire cannot carry.

        THE RESPONSE HERE IS BOOLEAN, WHICH IS THE DTYPE THAT BREAKS IT. MEASURED:
        ``to_mcp(np.bool_(True))`` returns ``{'@mcp_class': ['bool'],
        '@mcp_serialized': False, ...}`` -- a refusal record -- while every other
        numpy scalar this node could report as a level converts cleanly. A body that
        read its levels out of a numpy array without reducing them to Python objects
        would ship that stub under ``cases_level`` for every logical response, and
        the published table, whose labels are integers, could never show it.
        """
        truth, rating = published()
        logical = wrapper.run_roc(
            response=truth.astype(bool), predictor=rating, direction="<"
        )
        assert logical["cases_level"] is True
        assert logical["controls_level"] is False
        assert type(logical["cases_level"]) is bool

        for result in (scored(), logical, small()):
            payload = to_mcp(result)
            assert stubs_free(payload), payload
            assert set(payload) == CARD_KEYS

    def test_the_payload_round_trips_through_to_json(self) -> None:
        """No NaN token, no Infinity token: what orjson writes, json.loads reads."""
        payload = to_mcp(scored())
        blob = to_json(payload)
        assert "NaN" not in blob and "Infinity" not in blob
        assert json.loads(blob) == payload

    def test_this_node_registers_nothing(self) -> None:
        """Card #84 registers no result: every field it reports is data, not a fit."""
        assert wrapper.NODE_META[FN].register_field is None

    def test_the_area_is_the_mann_whitney_statistic_the_paper_defines(self) -> None:
        """The tie rule, on eight rows where a wrong one is visible by hand.

        Two of the sixteen pairs are ties. Scoring a tie as a win gives 0.90625 and
        scoring it as a loss gives 0.84375; the half-credit Hanley and McNeil's
        section IV specifies gives 14/16.
        """
        assert small()["auc"] == 0.875
        assert small()["n_cases"] == 4
        assert small()["n_controls"] == 4

    def test_the_reported_curve_keeps_the_operating_point_the_library_drops(self) -> None:
        """THE DEFAULT THAT DELETES A ROW OF THE CARD'S OWN PROMISE.

        MEASURED on the published table: ``roc_curve`` with its shipped
        ``drop_intermediate=True`` returns five thresholds ``[inf, 5, 4, 2, 1]`` and
        with ``drop_intermediate=False`` returns six, ``[inf, 5, 4, 3, 2, 1]``. The
        rating-3 operating point -- `questionable`, the middle of the paper's own
        scale -- is the one that disappears, and nothing warns. The card promises the
        full curve, so the default is not taken.
        """
        # The ignore's home is `[[tool.mypy.overrides]]` in engine/pyproject.toml,
        # beside scipy and statsmodels; see the note at the wrapper module's import.
        from sklearn.metrics import roc_curve  # type: ignore[import-untyped]

        truth, rating = published()
        dropped = roc_curve(truth, rating)[2]
        kept = roc_curve(truth, rating, drop_intermediate=False)[2]
        assert list(dropped) == [math.inf, 5.0, 4.0, 2.0, 1.0]
        assert list(kept) == [math.inf, 5.0, 4.0, 3.0, 2.0, 1.0]

        reported = scored()["roc_curve"]
        assert list(reported["threshold"]) == [5.0, 4.0, 3.0, 2.0, 1.0]

    def test_the_infinite_sentinel_is_removed_from_the_reported_curve(self) -> None:
        """Card #84: "the +/-Inf sentinels are removed". MEASURED: sklearn emits one.

        ``thresholds[0]`` is ``inf`` on every call -- it is the operating point at
        which nothing is called positive -- and ``to_mcp`` renders an infinity as
        ``null``, so leaving it in would put a null threshold on the wire beside a
        sensitivity of 0.
        """
        for result in (scored(), small(), scored(direction=">")):
            thresholds = np.asarray(result["roc_curve"]["threshold"], dtype=float)
            assert np.isfinite(thresholds).all(), thresholds
            assert len(thresholds) == len(set(thresholds.tolist()))

    def test_every_reported_field_describes_the_same_sample(self) -> None:
        """Alignment, asserted rather than documented."""
        result = scored()
        assert result["n_cases"] == 51
        assert result["n_controls"] == 58
        assert result["n_cases"] + result["n_controls"] == 109
        assert list(result["roc_curve"].columns) == [
            "threshold", "sensitivity", "specificity",
        ]
        assert list(result["best_threshold"].columns) == list(result["roc_curve"].columns)
        assert result["percent"] is False
        assert result["auc_ci"]["method"] == "delong"
        assert result["auc_ci"]["conf_level"] == 0.95

    def test_the_best_threshold_is_a_row_of_the_curve_at_the_youden_maximum(self) -> None:
        """Youden's J = sensitivity + specificity - 1, and the ties are all kept.

        THE EIGHT ROWS ARE CHOSEN SO THAT THREE ROWS TIE at J = 0.5 -- thresholds 5,
        4 and 3 -- which is what the card's "several rows on ties" promises and what
        the published table, whose maximum is a single row at rating 4, cannot show.
        """
        curve = small()["roc_curve"]
        best = small()["best_threshold"]
        assert list(best["threshold"]) == [5.0, 4.0, 3.0]
        assert list(best["sensitivity"]) == [0.5, 0.75, 1.0]
        assert list(best["specificity"]) == [1.0, 0.75, 0.5]

        youden = curve["sensitivity"] + curve["specificity"] - 1.0
        assert float(youden.max()) == 0.5
        merged = curve.merge(best, how="inner")
        assert len(merged) == len(best)

        published_best = scored()["best_threshold"]
        assert len(published_best) == 1
        assert float(published_best["threshold"].iloc[0]) == 4.0

    def test_the_orientation_is_reported_and_never_left_as_auto(self) -> None:
        """Card #84's second trap: ``auto`` hides an inversion unless it is reported.

        The payload therefore carries the orientation the body RESOLVED, never the
        word the caller sent. On these eight rows the higher score belongs to the
        cases, so ``auto`` resolves to ``'<'``; negating the score inverts that and
        ``auto`` resolves to ``'>'``, returning the SAME area from a score that reads
        the other way round.
        """
        response, predictor = eight_rows()
        negated = [-value for value in predictor]

        assert small(direction="auto")["direction"] == "<"
        assert small(direction="auto")["auc"] == 0.875

        flipped = wrapper.run_roc(
            response=response, predictor=negated, direction="auto"
        )
        assert flipped["direction"] == ">"
        assert flipped["auc"] == 0.875

        strict = wrapper.run_roc(
            response=response, predictor=negated, direction="<"
        )
        assert strict["direction"] == "<"
        assert strict["auc"] == 0.125

    def test_the_two_orientations_report_thresholds_on_the_callers_own_scale(self) -> None:
        """``direction='>'`` is computed on the negated score and reported on the caller's.

        The thresholds a reader sees are values the predictor actually took, in both
        orientations, and the sensitivity beside them changes meaning with the
        orientation: at ``'<'`` it is the share of cases scoring AT OR ABOVE the
        threshold, at ``'>'`` the share scoring at or below it.
        """
        ascending = small(direction="<")["roc_curve"]
        descending = small(direction=">")["roc_curve"]
        assert list(ascending["threshold"]) == [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        assert list(descending["threshold"]) == [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        assert list(descending["sensitivity"]) == [0.0, 0.0, 0.25, 0.5, 0.75, 1.0]

    def test_which_label_is_the_case_is_decided_by_order_and_always_reported(self) -> None:
        """Card #84's CRITICAL trap, made observable.

        MEASURED: ``roc_auc_score`` handed the words the table prints returns
        0.10682893847194047 -- it binarises against ``np.unique``, so `normal` is the
        LATER label and becomes the case, and the area comes back inverted with no
        warning. ``roc_curve`` handed the same column REFUSES it outright
        (``ValueError: y_true takes value in {'abnormal', 'normal'} and pos_label is
        not specified``), so the two halves of this method disagree about the same
        input. This node applies one rule -- the lower level is the control, the
        higher is the case -- to both halves, and REPORTS it.
        """
        from sklearn.metrics import roc_auc_score

        truth, rating = published()
        words = truth.map({0: "normal", 1: "abnormal"}).astype(object)
        assert roc_auc_score(words, rating) == pytest.approx(
            0.10682893847194047, rel=1e-12
        )

        result = wrapper.run_roc(response=words, predictor=rating, direction="<")
        assert result["controls_level"] == "abnormal"
        assert result["cases_level"] == "normal"
        assert result["auc"] == pytest.approx(0.10682893847194047, rel=1e-12)

        corrected = wrapper.run_roc(response=words, predictor=rating, direction=">")
        assert corrected["controls_level"] == "abnormal"
        assert corrected["cases_level"] == "normal"
        assert corrected["auc"] == pytest.approx(PUBLISHED_AREA, rel=1e-12)

    def test_the_interval_is_the_delong_variance_and_not_the_papers_own_estimator(
        self,
    ) -> None:
        """THE ARITHMETIC THIS BODY OWNS, CHECKED AGAINST ITS OWN DEFINITION.

        The body computes the placement values from midranks, which is Sun and Xu's
        (2014) form of DeLong's variance and the one pROC documents itself as using.
        :func:`mann_whitney_variance` computes the same quantity the slow way, from
        the n_A x n_N kernel Hanley and McNeil define in their section IV. The two
        must agree.

        AND THE PAPER'S OWN 0.032 IS NOT THIS NUMBER, which is why the oracle case
        claims no interval. MEASURED on the committed fixtures: Hanley and McNeil's
        Formula (1) with the Q1 = 0.8182 and Q2 = 0.8313 of their Table II returns
        0.03200416314832256, reproducing the 3.2 % the page prints, while the DeLong
        standard error is 0.030724408379381122 -- 4.0 % apart, and 400 times outside
        the tolerance class the area is claimed at.
        """
        truth, rating = published()
        result = scored()
        half = result["auc_ci"]["high"] - result["auc"]
        variance = (half / 1.959963984540054) ** 2
        assert variance == pytest.approx(
            mann_whitney_variance(truth, rating), rel=1e-12
        )
        assert math.sqrt(variance) == pytest.approx(0.030724408379381122, rel=1e-12)

        theta = PUBLISHED_AREA
        n_cases, n_controls = 51, 58
        hanley_mcneil = math.sqrt(
            (
                theta * (1.0 - theta)
                + (n_cases - 1) * (0.8182 - theta**2)
                + (n_controls - 1) * (0.8313 - theta**2)
            )
            / (n_cases * n_controls)
        )
        assert hanley_mcneil == pytest.approx(0.03200416314832256, rel=1e-12)
        assert round(hanley_mcneil, 3) == 0.032
        assert abs(hanley_mcneil - math.sqrt(variance)) / hanley_mcneil > 0.03

    def test_the_interval_is_not_clipped_to_the_unit_interval(self) -> None:
        """The normal approximation runs past 1 on a small sample, and is reported so.

        MEASURED on the eight rows: the area is 0.875 and the DeLong standard error
        is 0.125, so the 95 % interval reaches 1.1199954980675066. Clipping it to 1
        would report a bound the arithmetic did not produce and would hide exactly
        the case in which the normal approximation should not be trusted.
        """
        interval = small()["auc_ci"]
        assert interval["low"] == pytest.approx(0.6300045019324932, rel=1e-12)
        assert interval["high"] == pytest.approx(1.1199954980675066, rel=1e-12)
        assert interval["high"] > 1.0

    def test_a_wider_confidence_level_widens_the_interval(self) -> None:
        """``conf_level`` reaches the interval and nothing else."""
        narrow = scored(conf_level=0.5)
        wide = scored(conf_level=0.99)
        assert wide["auc_ci"]["high"] > narrow["auc_ci"]["high"]
        assert wide["auc_ci"]["low"] < narrow["auc_ci"]["low"]
        assert wide["auc"] == narrow["auc"]
        assert wide["roc_curve"].equals(narrow["roc_curve"])

    def test_no_interval_is_reported_when_none_is_asked_for(self) -> None:
        """``ci=False`` empties the field rather than filling it with a wide one."""
        without = scored(ci=False)
        assert without["auc_ci"] is None
        assert without["auc"] == pytest.approx(PUBLISHED_AREA, rel=1e-12)
        assert set(without) == CARD_KEYS
        assert stubs_free(to_mcp(without))

    def test_the_curve_is_a_chart_this_engine_can_emit(self) -> None:
        """What ``chart_spec`` returns for this frame, and it is NOT a ROC curve.

        MEASURED against chart_spec as it stands. Card #84 declares
        ``chart_kind: line``, and the emitter DOES reach its line branch -- but
        ``_frame_spec`` plots every numeric column against the ROW NUMBER, so what
        comes back is three lines (threshold, sensitivity, specificity) over the
        index rather than sensitivity against one minus specificity, which is what a
        ROC curve is. This test asserts what the engine emits rather than what the
        card means, and records the difference instead of hiding it. It is a defect
        in the emitter's frame branch (box 2.1.12) rather than in this payload, and
        it is the same one the sibling count-model body records against its
        coefficient table.
        """
        spec = chart_spec(scored()["roc_curve"], title="roc")
        assert spec is not None
        assert_pure(spec)
        assert [series["name"] for series in spec["series"]] == [
            "threshold", "sensitivity", "specificity",
        ]
        assert len(spec["series"][0]["data"]) == 5

    def test_the_declared_defaults_are_read_from_the_contract_and_not_invented(
        self,
    ) -> None:
        """An omitted optional takes the value ``node-specs.json`` publishes, and no other.

        ``direction`` is deliberately absent from this check: the contract declares
        NO default for it, which is why it is a refusal rather than a fallback.
        """
        defaults = wrapper.NODE_META[FN].defaults
        assert defaults["ci"] is True
        assert defaults["conf_level"] == 0.95
        assert "direction" not in defaults

        truth, rating = published()
        implied = wrapper.run_roc(response=truth, predictor=rating, direction="<")
        named = wrapper.run_roc(
            response=truth, predictor=rating, direction="<", ci=True, conf_level=0.95
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
        assert case.tolerance_class == "statistic-1e-6"

        state, payload = run_call(case)
        assert state == "succeeded", payload
        assert (
            disagreement(payload, case.expected, case.unchecked_keys, case.rtol, case.atol)
            is None
        )

    def test_the_published_ratio_is_what_the_case_claims(self) -> None:
        """2,642/(58 x 51) is the page's own arithmetic, and it is where the digits come from.

        Table II prints ``0.893``, which is 1.9156e-04 relative from what this body
        returns and would be refused by ``estimate-1e-4``. The same line prints the
        ratio, and the ratio is exact.
        """
        assert PUBLISHED_AREA == 2642.0 / (58.0 * 51.0)
        assert scored()["auc"] == PUBLISHED_AREA
        assert round(PUBLISHED_AREA, 3) == 0.893
        assert abs(PUBLISHED_AREA - 0.893) / 0.893 == pytest.approx(1.9156e-04, rel=1e-3)


class TestDeterminism:
    """Class D -- identical inputs, identical bytes."""

    def test_two_identical_calls_serialise_to_identical_bytes(self) -> None:
        """``run_roc`` is not in ``stochastic_unseeded_fns``; read that."""
        specs = json.loads(
            (ENGINE_ROOT / "artifacts" / "node-specs.json").read_bytes().decode("utf-8")
        )
        assert FN not in specs["vocabulary"]["stochastic_unseeded_fns"]

        first = to_json(to_mcp(scored()))
        second = to_json(to_mcp(scored()))
        assert first == second
        assert len(first) > 0


def test_the_module_exports_every_function_its_card_names() -> None:
    """The one assertion a scaffold can make truthfully before a body exists."""
    missing = [fn for fn in MODULE_FNS if not hasattr(wrapper, fn)]
    assert not missing, missing
