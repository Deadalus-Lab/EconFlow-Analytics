# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.14 -- the double-run determinism controls.

FIVE CALLABLES, and the harness in :mod:`tests.controls.double_run` must reach
the same verdict on all five on every run:

  POSITIVE (MUST be caught as nondeterministic)
    * :func:`wall_clock`      -- reads the wall clock
    * :func:`object_identity` -- reads an allocator address
    * :func:`unseeded_random` -- draws from the process-wide random state

  NEGATIVE (MUST NOT be caught)
    * :func:`fixed_mapping`   -- a constant
    * :func:`seeded_normal`   -- a draw from a generator seeded at every call

WHY THESE THREE POSITIVES AND NOT AN ARBITRARY ONE. They are the three real
mechanisms by which a numerical body stops reproducing, and they fail in
different places. The clock enters through a timestamp written into a result;
the allocator address enters through anything that hashes or sorts by ``id``, or
through a ``set`` iteration order derived from one; the process-wide random state
enters through any library call that draws without being handed a generator --
which is the default in numpy's legacy ``np.random`` API and in scipy's
``random_state=None``.

WHY ``seeded_normal`` IS THE NEGATIVE THAT MATTERS. It draws a pseudo-random
number, so a harness that merely looked for "does this touch a random API" would
flag it. It is nonetheless perfectly reproducible, because the generator is
constructed from a fixed seed inside the call. That is exactly the shape every
correct wrapper body will have, and a determinism gate that refused it would be
unusable -- so it is planted here to make sure this one never becomes that.
"""

from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import Any

import numpy as np


def wall_clock() -> float:
    """POSITIVE. The wall clock: a different float on every call."""
    return time.time()


#: Keeps each probe object alive, and that is LOAD-BEARING -- see below.
_ALIVE: list[object] = []


def object_identity() -> int:
    """POSITIVE. An allocator address, which is not a property of the input.

    THE OBJECT MUST OUTLIVE THE NEXT ALLOCATION, AND THE OBVIOUS FORM DOES NOT.
    Measured on CPython 3.12.13: ``id(object()) == id(object())`` is **True**.
    The temporary's refcount drops to zero at the end of the expression, the slot
    returns to the free list, and the next allocation is handed the identical
    address:

        >>> id(object()) == id(object())     # doctest: +SKIP
        True

    So the textbook nondeterminism control is, written that way, perfectly
    deterministic -- and a determinism harness planted with it would report that
    it had proved itself while its positive control never fired. Appending to
    ``_ALIVE`` keeps the first probe alive across the second call, which is also
    the realistic shape of the defect this models: a result that embeds the
    identity of an object the caller still holds.
    """
    probe = object()
    _ALIVE.append(probe)
    return id(probe)


def unseeded_random() -> float:
    """POSITIVE. The process-wide random state, drawn without a seed."""
    return random.random()  # noqa: S311 -- nondeterminism IS the point of this control.


def fixed_mapping() -> dict[str, Any]:
    """NEGATIVE. A constant: the same bytes on every call, forever."""
    return {"method": "control", "estimate": 0.5, "labels": ["a", "b"], "n": 3}


def seeded_normal() -> float:
    """NEGATIVE. Pseudo-random and fully reproducible: the seed is fixed here.

    The generator is constructed INSIDE the call, so each call starts from the
    same state. Hoisting it to module scope would make consecutive calls advance
    one shared stream and this control would -- correctly -- start failing.
    """
    return float(np.random.default_rng(7).normal())


#: The planted set, as ``(name, callable, must_be_caught)``.
#:
#: Read by :mod:`tests.controls.double_run`, which asserts the verdict on EVERY
#: entry rather than counting failures: a positive that goes unflagged and a
#: negative that gets flagged are different defects and are reported separately.
CONTROLS: tuple[tuple[str, Callable[[], Any], bool], ...] = (
    ("wall_clock", wall_clock, True),
    ("object_identity", object_identity, True),
    ("unseeded_random", unseeded_random, True),
    ("fixed_mapping", fixed_mapping, False),
    ("seeded_normal", seeded_normal, False),
)
