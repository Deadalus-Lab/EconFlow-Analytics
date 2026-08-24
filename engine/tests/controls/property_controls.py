# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.16 -- planted methods that prove the properties can fail.

FOUR CALLABLES AND TWO PROPERTIES. The properties here are the SAME functions
the real properties in ``tests/test_properties.py`` are built from, applied to
planted methods instead of to library code. That is what makes them evidence: a
property that is only ever run against code that satisfies it is
indistinguishable from a property that cannot fail.

  POSITIVE (the property MUST be falsified)
    * :func:`adds_a_constant` -- violates scale equivariance by adding a shift
    * :func:`drops_nan`       -- silently discards missing observations

  NEGATIVE (the property MUST hold)
    * :func:`scaled_mean`     -- genuinely scale-equivariant
    * :func:`needs_two`       -- refuses n = 1 by RAISING, which is a legitimate
                                 answer and must not read as a violation

WHY ``needs_two`` IS A NEGATIVE AND NOT A POSITIVE. An estimator whose variance
denominator is (n - 1) cannot answer for a single observation, and the correct
behaviour is a refusal the caller can catch -- ``GateError`` in this engine,
which subclasses ``ValueError``. A property written as "returns a finite number
for every input" would call that a bug and push whoever wrote it toward returning
nan instead, which is the silent failure this repository exists to refuse. The
property is therefore "answers or refuses, never fabricates", and this control
pins that distinction.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

__all__ = [
    "adds_a_constant",
    "assert_nan_preserving",
    "assert_scale_equivariant",
    "drops_nan",
    "needs_two",
    "observed",
    "scaled_mean",
]

# --------------------------------------------------------------------------
# The properties. Shared with the real property tests.
# --------------------------------------------------------------------------


def assert_scale_equivariant(
    method: object, values: pd.Series, factor: float
) -> None:
    """f(c * x) == c * f(x).

    The defining property of a location-free statistic: doubling the units of a
    series doubles the answer and changes nothing else. A method that adds a
    constant anywhere in its body breaks it, which is why this is the property
    the shift control is planted against.

    Compared with a RELATIVE tolerance, because the alternative -- an absolute
    epsilon -- is a different assertion at 1e-6 than at 1e6 and would pass or
    fail on the magnitude the search happened to draw rather than on the method.
    """
    assert callable(method)
    base = method(values)
    scaled = method(values * factor)
    if base is None or scaled is None:
        return
    if not (np.isfinite(base) and np.isfinite(scaled)):
        return
    expected = base * factor
    tolerance = 1e-9 * max(1.0, abs(expected))
    assert abs(scaled - expected) <= tolerance, (
        f"scale equivariance violated: f(x * {factor}) = {scaled}, "
        f"but {factor} * f(x) = {expected}"
    )


def assert_nan_preserving(method: object, values: pd.Series) -> None:
    """A missing observation stays missing; it is never quietly dropped.

    Dropping NaN changes the sample the answer describes without saying so, and
    every downstream degrees-of-freedom, standard error and confidence interval
    is then computed against a different n than the caller believes. The engine's
    rule is that a method either handles the missing value explicitly or refuses.
    """
    assert callable(method)
    out = method(values)
    if out is None:
        return
    assert len(out) == len(values), (
        f"a missing observation was dropped: input had {len(values)} "
        f"observation(s), output has {len(out)}"
    )


# --------------------------------------------------------------------------
# POSITIVE controls -- these MUST falsify the property above.
# --------------------------------------------------------------------------


def adds_a_constant(values: pd.Series) -> float:
    """POSITIVE. Scale equivariance broken by a shift the caller cannot see.

    ``mean(c * x) + 1`` is not ``c * (mean(x) + 1)`` for any c other than 1, so
    the property is falsified by every draw with a factor away from unity. This
    is the shape of the real defect: an offset, a bias correction or a
    continuity term applied unconditionally inside a body that is documented as
    scale-free.
    """
    return float(np.nanmean(values.to_numpy())) + 1.0


def drops_nan(values: pd.Series) -> pd.Series:
    """POSITIVE. Missing observations discarded, silently, with no refusal."""
    return values.dropna()


# --------------------------------------------------------------------------
# NEGATIVE controls -- these MUST satisfy the property above.
# --------------------------------------------------------------------------


def scaled_mean(values: pd.Series) -> float | None:
    """NEGATIVE. Genuinely scale-equivariant: mean(c * x) == c * mean(x).

    ``None`` rather than nan when every observation is missing: an empty mean has
    no value, and this repository's serialiser writes a missing number as JSON
    ``null``. Returning nan here would make the property assert on a value that
    is not one.
    """
    array = values.to_numpy()
    if not np.isfinite(array).any():
        return None
    return float(np.nanmean(array))


def observed(values: pd.Series) -> int:
    """The SAMPLE SIZE, which is not the same number as the length.

    A series of length 2 carrying one NaN describes ONE observation. Every
    degrees-of-freedom calculation in econometrics is stated over this count and
    not over the container's length, and conflating the two is the same mistake
    :func:`assert_nan_preserving` exists to catch, wearing different clothes.
    """
    return int(np.isfinite(values.to_numpy()).sum())


def needs_two(values: pd.Series) -> float:
    """NEGATIVE. Refuses fewer than two OBSERVATIONS by raising.

    The sample variance has an (n - 1) denominator, so one observation is not a
    sample it can describe. It says so rather than fabricating a number.

    THE GUARD COUNTS OBSERVATIONS, NOT LENGTH, AND THE FIRST VERSION DID NOT.
    Guarding on ``len(values) < 2`` let ``[0.0, nan]`` through: length 2, one
    observation, so ``np.nanvar(..., ddof=1)`` computed dof = 1 - 1 = 0 and numpy
    raised ``RuntimeWarning: Degrees of freedom <= 0 for slice``, which this
    suite turns into an error. Found by the property, on the second run, on a
    case nobody would have typed by hand -- which is what these tests are for.
    """
    n = observed(values)
    if n < 2:
        raise ValueError(
            f"needs_two: a sample variance needs at least 2 observations, {n} given."
        )
    return float(np.nanvar(values.to_numpy(), ddof=1))
