# SPDX-License-Identifier: AGPL-3.0-only
"""The dataset mover, column by column, and the case that made it column-aware.

WHY THIS SUITE EXISTS. ``test_a_case_that_ran_moves_when_its_fixture_moves``
re-runs every oracle case on a moved dataset and requires the payload to move; it
is the only evidence that a fixture reaches the body rather than sitting beside
it. That control asserts FIRST that the moved dataset still RUNS, on the stated
premise that "the control moves values, never shapes".

THE PREMISE WAS FALSE FOR ONE COLUMN SHAPE and the first wrapper body written in
phase 2.2 is what found it. :func:`move_leaf` sees one number at a time. Scaling
0 leaves it at 0, so its fallback adds one -- landing it exactly on the other
level of an indicator column, while the 1s scale off it. A response of {0, 1}
came back as {1, 1.001}, and ``run_binomial_fe_glm`` refused the moved dataset
with the estimator's own "The dependent variable must be binary (0 or 1)". Every
binary-response, ordered and count method in the catalogue would have met the
same wall.

WHAT THE FIX IS NOT. The indicator column is still moved, and moved TOTALLY: it
is negated, so every value changes and a response with 9 ones in 138 rows becomes
one with 129. Nothing here lets a body that ignores its data pass the control it
serves; the assertions below pin both halves of that.
"""

from __future__ import annotations

from typing import Any

import pytest

from tests.conformance.fixtures import (
    build,
    fixture,
    is_indicator,
    move_values,
)

RTOL = 1e-4
ATOL = 1e-10

#: The published dataset the first body is proved against: a float frame whose
#: second column is the 0/1 response and whose first is a real measurement.
ORING = "dalal_fowlkes_hoadley_1989_oring_field_joint"


def _column(record: dict[str, Any], index: int) -> list[Any]:
    return [row[index] for row in record["values"]]


class TestIsIndicator:
    """What counts as an indicator column, and what does not."""

    @pytest.mark.parametrize(
        "column", [[0.0, 1.0, 0.0], [0, 1], [1, 0, 1, 1], [0.0, 1.0]]
    )
    def test_a_column_of_zeros_and_ones_is_one(self, column: list[Any]) -> None:
        assert is_indicator(column)

    @pytest.mark.parametrize(
        "column",
        [
            [0.0, 0.0],
            [1.0, 1.0],
            [0.0, 1.0, 2.0],
            [0.5, 1.0],
            [-1.0, 0.0],
            [True, False],
            ["0", "1"],
            [],
        ],
        ids=[
            "constant-zero",
            "constant-one",
            "three-levels",
            "a-fraction",
            "coded-minus-one",
            "booleans-move-already",
            "strings",
            "empty",
        ],
    )
    def test_everything_else_is_not(self, column: list[Any]) -> None:
        assert not is_indicator(column)


class TestMoveValues:
    """The mover over a real published frame."""

    def test_the_indicator_column_is_negated_and_stays_an_indicator(self) -> None:
        record = fixture(ORING)
        moved = move_values(record, RTOL, ATOL)
        before, after = _column(record, 1), _column(moved, 1)

        assert is_indicator(after), "the moved response is no longer 0/1"
        assert after == [1 - value for value in before]
        assert sum(before) == 9.0
        assert sum(after) == 129.0

    def test_the_measured_column_is_scaled_and_every_value_moves(self) -> None:
        record = fixture(ORING)
        moved = move_values(record, RTOL, ATOL)
        before, after = _column(record, 0), _column(moved, 0)

        assert all(a != b for a, b in zip(after, before, strict=True))
        assert after[0] == pytest.approx(before[0] * (1.0 + 10.0 * RTOL))

    def test_the_shape_the_columns_and_the_row_count_are_untouched(self) -> None:
        record = fixture(ORING)
        moved = move_values(record, RTOL, ATOL)

        assert moved["shape"] == record["shape"]
        assert moved["columns"] == record["columns"]
        assert moved["index"] == record["index"]
        assert len(moved["values"]) == len(record["values"])
        assert build(moved).shape == build(record).shape

    def test_a_frame_with_no_indicator_column_is_scaled_exactly_as_before(self) -> None:
        """THE REGRESSION HALF. The change must not alter any other dataset."""
        record = fixture("anscombe_1973_data_set_i")
        moved = move_values(record, RTOL, ATOL)

        for index in (0, 1):
            before, after = _column(record, index), _column(moved, index)
            assert after == [value * (1.0 + 10.0 * RTOL) for value in before]

    def test_a_series_shaped_dataset_moves_as_one_column(self) -> None:
        record = dict(fixture(ORING))
        record["shape"] = "series"
        record["columns"] = ["incident"]
        record["values"] = [0.0, 1.0, 1.0, 0.0]

        assert move_values(record, RTOL, ATOL)["values"] == [1.0, 0.0, 0.0, 1.0]

    def test_a_mapping_shaped_dataset_keeps_the_leaf_walk(self) -> None:
        record = dict(fixture(ORING))
        record["shape"] = "object"
        record["columns"] = None
        record["index"] = None
        record["dtype"] = None
        record["values"] = {"alpha": 2.0, "nested": [3.0, 4.0]}

        moved = move_values(record, RTOL, ATOL)["values"]
        assert moved["alpha"] == pytest.approx(2.0 * (1.0 + 10.0 * RTOL))
        assert moved["nested"] == [
            pytest.approx(3.0 * (1.0 + 10.0 * RTOL)),
            pytest.approx(4.0 * (1.0 + 10.0 * RTOL)),
        ]
