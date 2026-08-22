# SPDX-License-Identifier: AGPL-3.0-only
"""The two index-label predicates, pinned against the checkers that shaped them.

WHY THIS FILE EXISTS. ``serialize._iso_index_label`` and ``chart_spec._iso_label``
both have to decide one thing: whether the stamp they were handed is a real
moment or a missing one. Both were written with a ``pd.isna`` guard, and both had
to be rewritten because pandas-stubs models ``pd.Timestamp(...)`` as returning
``Timestamp`` to mypy and ``Timestamp | NaTType`` to pyright -- so the narrowing
each checker accepts is not the same narrowing.

THAT IS THE HAZARD THIS FILE GUARDS. A predicate swapped to satisfy a type
checker is a behaviour change wearing the clothes of a lint fix, and neither
module had a single test when the swap was made. The values below are the
measured behaviour of the ``pd.isna`` form, recorded so that the next person who
rewrites either guard to please a checker finds out immediately if the answer
moved.

``NaT`` is the whole point of the two cases that name it. ``NaT.isoformat()``
returns the string ``'NaT'`` at run time, which is exactly what ``str(NaT)``
returns -- which is why the axis-label fallback is not a behaviour change, and
why asserting it is the only way to keep it from becoming one.
"""

from __future__ import annotations

import pandas as pd
import pytest

from econflow_engine.chart_spec import _axis_labels, _iso_label
from econflow_engine.serialize import _iso_index_label


@pytest.mark.parametrize(
    ("stamp", "expected"),
    [
        (pd.NaT, None),
        (None, None),
        (pd.Timestamp("2026-08-20T13:45:00"), "2026-08-20T13:45:00"),
        (pd.Period("2026-08", freq="M"), "2026-08-01T00:00:00"),
        ("2026-01-02", "2026-01-02T00:00:00"),
    ],
)
def test_a_missing_stamp_serialises_to_null(stamp: object, expected: str | None) -> None:
    """Missing becomes ``None``; present becomes ISO-8601 with a ``T`` separator."""
    assert _iso_index_label(stamp) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (pd.NaT, "NaT"),
        (pd.Timestamp("2026-08-20"), "2026-08-20T00:00:00"),
        ("2026-01-02", "2026-01-02T00:00:00"),
    ],
)
def test_an_axis_label_never_returns_none(value: object, expected: str) -> None:
    """An axis label is always a string: a missing stamp labels itself ``NaT``."""
    assert _iso_label(value) == expected


def test_a_gap_in_a_datetime_index_keeps_its_position() -> None:
    """The label list stays aligned with the index; a gap is not dropped."""
    index = pd.DatetimeIndex([pd.Timestamp("2026-01-01"), pd.NaT, pd.Timestamp("2026-01-03")])
    assert _axis_labels(index) == ["2026-01-01T00:00:00", "NaT", "2026-01-03T00:00:00"]


def test_a_period_index_is_labelled_at_its_start() -> None:
    labels = _axis_labels(pd.PeriodIndex(["2026-01", "2026-02"], freq="M"))
    assert labels == ["2026-01-01T00:00:00", "2026-02-01T00:00:00"]


def test_a_non_temporal_index_is_labelled_verbatim() -> None:
    """Only a datetime or period index is reformatted; everything else is ``str``."""
    assert _axis_labels(pd.Index(["a", "b"])) == ["a", "b"]
