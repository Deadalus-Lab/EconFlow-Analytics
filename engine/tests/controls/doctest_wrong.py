# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.18 -- POSITIVE control: an example that is WRONG and MUST be failed.

THE OUTPUT BELOW IS DELIBERATELY FALSE. ``pytest --doctest-modules`` over this
file must COLLECT one item and FAIL it. If it ever passes, the doctest leaf is
not actually comparing anything and every "0 failures" it has ever printed was
worthless.

THIS FILE IS RUN IN ITS OWN PYTEST INVOCATION, by
``tests/controls/doctest_gate.py``, and never as part of the ordinary suite:
``--doctest-modules`` is not in ``addopts`` and this module is not named
``test_*.py``, so a plain ``pytest`` run neither imports nor examines it. Adding
``--doctest-modules`` to ``addopts`` in pyproject.toml would turn the suite red
here -- which is the correct outcome and not a reason to soften this file.
"""

from __future__ import annotations


def doubled(value: int) -> int:
    """Return twice ``value``.

    The example claims an answer this function does not give. That is the entire
    purpose of the module: the doctest runner must notice.

        >>> doubled(2)
        5
    """
    return value * 2
