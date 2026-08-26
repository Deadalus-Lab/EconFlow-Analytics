# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.18 -- NEGATIVE control: prose-only documentation, ZERO examples.

WHY THIS SHAPE HAS ITS OWN CONTROL. The 1456 wrapper docstrings carry prose
``Examples`` sections with no ``>>>`` in them, deliberately: a prose section
describes what a method is for without asserting an answer, and 1456 executable
examples over typed stubs that raise ``NotImplementedError`` would be 1456
guaranteed failures.

So the doctest leaf has to distinguish THREE outcomes, not two:

    collected and passed   -- a real, correct example        (doctest_correct.py)
    collected and failed   -- a real, wrong example          (doctest_wrong.py)
    collected ZERO, no error -- prose with no example        (THIS FILE)

The third is the one a careless implementation gets wrong, in either direction:
by treating an indented prose block as an example and failing it, or by treating
"no examples here" as an import error. Neither may happen. ``pytest
--doctest-modules`` over this file must collect exactly 0 items and exit
cleanly.
"""

from __future__ import annotations


def augmented_dickey_fuller(series_name: str) -> str:
    """Describe the augmented Dickey-Fuller test, without running one.

    Note:
        The null hypothesis is that the series contains a unit root. Rejecting
        it is evidence of stationarity, not proof of it, and the test's power is
        low against a near-unit-root alternative.

    Examples:
        A researcher checks a quarterly GDP series for a unit root before
        differencing it, then reports the lag order chosen by the information
        criterion alongside the statistic. Nothing here is executable, and
        nothing here should be collected.
    """
    return f"augmented Dickey-Fuller on {series_name}"


class Specification:
    """A model specification, documented in prose alone.

    Note:
        Deliberately carries no worked example. A docstring may reasonably have
        none, and the leaf must not mistake that for a missing test.
    """

    def __init__(self, lags: int) -> None:
        """Record the lag order this specification was built with."""
        self.lags = lags
