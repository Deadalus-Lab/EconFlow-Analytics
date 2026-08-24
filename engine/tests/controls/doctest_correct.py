# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.18 -- NEGATIVE control: examples that are RIGHT and must be collected.

Two documented objects, each carrying a worked example whose printed output is
the output Python actually produces. ``pytest --doctest-modules`` over this file
must COLLECT two items and PASS both.

This is the half that proves the doctest leaf is running at all. Its sibling
``doctest_wrong.py`` proves the leaf can still fail.
"""

from __future__ import annotations


def observations(values: list[float | None]) -> int:
    """Count the observations that are actually present.

    A missing value is not an observation, and the length of the container is
    not the sample size -- the distinction every degrees-of-freedom calculation
    rests on.

        >>> observations([1.0, 2.0, 3.0])
        3
        >>> observations([1.0, None, 3.0])
        2
        >>> observations([])
        0
    """
    return sum(1 for v in values if v is not None)


def share(part: int, whole: int) -> float:
    """The share of ``whole`` accounted for by ``part``, as a proportion.

    An empty whole has no share; it is reported as 0.0 rather than raising,
    because the caller asked for a proportion of nothing and nothing is the
    honest answer.

        >>> share(1, 4)
        0.25
        >>> share(0, 4)
        0.0
        >>> share(3, 0)
        0.0
    """
    if whole == 0:
        return 0.0
    return part / whole
