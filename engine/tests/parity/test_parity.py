# SPDX-License-Identifier: AGPL-3.0-only
"""THE P1/P2/P3 CONTRACT against 4855 frozen verdicts.

P1 -- SOUNDNESS      for every fixture, python.accept => frozen.accept. HARD FAIL, no
                     exceptions. This is what makes it safe to run the SAME
                     models in the editor, in the worker, and over LLM output.
P2 -- COMPLETENESS   frozen.reject (within the modelled class) => python.reject WITH
                     THE SAME reason code.
P3 -- ENUMERATED DIVERGENCE
                     {python.reject AND frozen.accept} == the contents of
                     artifacts/intentional-divergences.json, as SET EQUALITY:
                     both a NEW divergence and a DEAD entry fail the suite.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tests.parity.replay import Row, build_rows, divergence_key

ROWS, SPECS, FIXTURES, DIVERGENCES = build_rows()
DECLARED: set[str] = {m for d in DIVERGENCES["divergences"] for m in d["members"]}

# THE FIXTURES COVER A SUBSET, AND THE PER-NODE FAMILIES ARE SIZED BY IT.
# The frozen corpus was produced against the retired contract, which described 913
# of today's 1456 nodes. A node added since has no frozen verdict to be compared
# against, so it is not in any per-node family. Sizing these assertions from the
# LIVE catalogue instead would fail on the first node ever added -- and whoever hit
# that would edit the number rather than ask why it moved.
_ARTIFACTS = Path(__file__).resolve().parents[2] / "artifacts"
COVERED: frozenset[str] = frozenset(
    json.loads((_ARTIFACTS / "legacy-inventory.json").read_bytes().decode("utf-8"))[
        "contract_hashes"
    ]
)
N_NODES: int = len(COVERED)


def _family(name: str) -> list[Row]:
    return [r for r in ROWS if r.case["family"] == name]


def _report(rows: list[Row]) -> list[str]:
    return [r.show() for r in rows]


class TestCorpusHygiene:
    def test_every_fixture_was_replayed(self) -> None:
        assert len(ROWS) == FIXTURES["n_cases"]

    def test_family_sizes_are_the_expected_ones(self) -> None:
        sizes = {f: len(_family(f)) for f in FIXTURES["families"]}
        with_required = sum(
            1
            for n in SPECS["nodes"]
            if n["fn"] in COVERED and any(a["required"] for a in n["arguments"])
        )
        assert sizes["spec-accept"] == N_NODES
        assert sizes["optional-omitted"] == N_NODES
        assert sizes["unknown-key"] == N_NODES
        assert sizes["mutation"] == N_NODES
        assert sizes["kind-matrix"] == 240  # 20 kinds x 12 mutations
        assert sizes["formula"] == 40
        assert sizes["formula-allowed-vars"] == 2
        assert sizes["pointer"] == 21
        assert sizes["missing-required"] == with_required

    def test_every_reason_code_belongs_to_the_closed_set(self) -> None:
        closed = set(FIXTURES["reason_codes"])
        for row in ROWS:
            if row.frozen_reason is not None:
                assert row.frozen_reason in closed, row.case["id"]
            if row.py_reason is not None:
                assert row.py_reason in closed, f"{row.case['id']}: {row.py_reason}"

    def test_every_family_is_represented(self) -> None:
        assert sorted({r.case["family"] for r in ROWS}) == sorted(FIXTURES["families"])


class TestP1Soundness:
    VIOLATIONS = [r for r in ROWS if r.py_ok and not r.frozen_accepts]

    def test_no_python_accept_is_a_frozen_reject(self) -> None:
        assert _report(self.VIOLATIONS) == []

    def test_not_even_on_required_arguments(self) -> None:
        subset = [r for r in self.VIOLATIONS if r.frozen_reason == "missing-required"]
        assert _report(subset) == []

    def test_not_even_in_the_formula_allowlist(self) -> None:
        subset = [r for r in self.VIOLATIONS if (r.frozen_reason or "").startswith("formula-")]
        assert _report(subset) == []


class TestP2Completeness:
    REJECTS = [r for r in ROWS if not r.frozen_accepts]

    def test_every_r_reject_is_a_python_reject(self) -> None:
        assert _report([r for r in self.REJECTS if r.py_ok]) == []

    def test_with_the_same_reason_code(self) -> None:
        mismatched = [r for r in self.REJECTS if not r.py_ok and r.py_reason != r.frozen_reason]
        assert _report(mismatched) == []

    @pytest.mark.parametrize(
        "code", ["unknown-args", "missing-required", "handle-not-string"]
    )
    def test_reason_class_matches_one_for_one(self, code: str) -> None:
        subset = [r for r in self.REJECTS if r.frozen_reason == code]
        assert len(subset) > 0
        assert _report([r for r in subset if r.py_ok or r.py_reason != code]) == []

    def test_formula_pointer_and_forecastfn_reasons_match(self) -> None:
        subset = [
            r
            for r in self.REJECTS
            if (r.frozen_reason or "").startswith(("formula-", "pointer-"))
            or r.frozen_reason == "forecastfn-unknown"
        ]
        assert len(subset) > 0
        assert _report([r for r in subset if r.py_ok or r.py_reason != r.frozen_reason]) == []


class TestP3EnumeratedDivergence:
    DIVERGING = [r for r in ROWS if not r.py_ok and r.frozen_accepts]
    OBSERVED = {divergence_key(r.case) for r in DIVERGING}

    def test_the_divergence_file_is_well_formed(self) -> None:
        # ONE SPELLING ACROSS ALL SEVEN SEALED ARTIFACTS. This file declared its
        # version under `schema_version` while the other six used
        # `artifact_version`, so a reader looking for the version of a sealed
        # artifact had to know which of two names to ask for. Box 2.1.15.
        assert DIVERGENCES["artifact_version"] == 1
        entries = DIVERGENCES["divergences"]
        assert len(entries) > 0
        for entry in entries:
            assert entry["id"], entry
            assert entry["reason"], entry["id"]
            assert entry["rationale"], entry["id"]
            assert len(entry["since"]) == 10 and entry["since"][4] == "-", entry["id"]
            assert len(entry["members"]) > 0, entry["id"]
        members = [m for d in entries for m in d["members"]]
        assert len(members) == len(set(members)), "a member is declared twice"

    def test_no_new_divergence(self) -> None:
        extra = sorted(self.OBSERVED - DECLARED)
        examples = [
            f"{key}  e.g. {next(r for r in self.DIVERGING if divergence_key(r.case) == key).show()}"
            for key in extra
        ]
        assert examples == []

    def test_no_dead_entry(self) -> None:
        assert sorted(DECLARED - self.OBSERVED) == []

    def test_no_declared_class_hides_a_p1_violation(self) -> None:
        unsafe = [
            r
            for r in ROWS
            if r.py_ok and not r.frozen_accepts and divergence_key(r.case) in DECLARED
        ]
        assert _report(unsafe) == []

    def test_the_declared_classes_cover_every_diverging_fixture(self) -> None:
        assert len(self.DIVERGING) > 0
        assert len(self.OBSERVED) == len(DECLARED)


class TestThePositivePath:
    def test_every_input_example_passes_except_the_declared_one(self) -> None:
        accepts = _family("spec-accept")
        assert len(accepts) == N_NODES
        unexpected = [
            r for r in accepts if not r.py_ok and divergence_key(r.case) not in DECLARED
        ]
        assert _report(unexpected) == []
        # profoc_online's own generated example carries explicit nulls.
        assert len([r for r in accepts if not r.py_ok]) == 1

    def test_omitting_every_optional_passes(self) -> None:
        omitted = _family("optional-omitted")
        assert len(omitted) == N_NODES
        assert _report([r for r in omitted if not r.py_ok]) == []

    def test_every_unknown_key_and_every_missing_required_is_caught(self) -> None:
        unknown = _family("unknown-key")
        missing = _family("missing-required")
        assert len(unknown) == N_NODES
        assert len(missing) > 0
        assert _report([r for r in unknown if r.py_ok or r.py_reason != "unknown-args"]) == []
        assert (
            _report([r for r in missing if r.py_ok or r.py_reason != "missing-required"]) == []
        )
