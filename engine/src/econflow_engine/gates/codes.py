# SPDX-License-Identifier: AGPL-3.0-only
"""The closed detail-code vocabulary, and the one constructor that emits it.

WHY THIS MODULE SITS BELOW THE GATES. :mod:`~econflow_engine.gates.primitives`
imports :mod:`~econflow_engine.gates.cross_section` (``require_cross_section``
delegates to it), so the vocabulary cannot live in either without a cycle. It
lives here, and all three gate modules import it.

WHY ``reason_code`` STAYS ``"other"`` AND THE DIAGNOSIS MOVES TO ``detail_code``.
``ENGINE_REASON_CODES`` is the wire contract and it is CLOSED at eighteen names.
It is not a list this package may extend: ``artifacts/parity-fixtures.json``
carries the same eighteen under ``reason_codes``, that artifact is a frozen input
recording 4855 verdicts taken against the frozen adapter, and
``tests/parity/test_parity.py`` asserts membership against it. A nineteenth name
would mean re-sealing a corpus this box does not touch, and it would change what
a client sees on a wire that is already specified. So the wire answer is
``other`` -- as it already is for every ``kind: "path"`` refusal and for three of
the formula codes -- and the finer diagnosis rides in ``detail_code``, which is
this project's own extensible half. ``chart_spec.py`` established the pattern
before this module existed.

``GateDetailCode`` IS THE ENFORCEMENT, NOT THE TEST. Typing the parameter as a
``Literal`` means ``mypy --strict`` rejects an undeclared code at the call site,
statically, at every emitter -- which is stronger than any runtime assertion and
covers the two codes no primitive owns. ``GATE_DETAIL_CODES`` is DERIVED from the
same declaration with ``get_args``, so the runtime tuple and the static type can
never disagree; ``errors.py`` writes its two copies by hand and that is the
mistake not repeated here.

WHAT THIS DOES NOT REACH, STATED PLAINLY. ``mcp/make_tool.py`` maps a
``GateError`` to ``ToolResult(ok=False, reason_code=exc.reason_code, …)`` and
``ToolResult`` carries NO ``detail_code`` field, so the distinction below is
available in-process -- to a wrapper author, to a test, to anything that catches
the exception -- and is DROPPED before the response reaches a client. Carrying it
through means one new field on ``ToolResult`` and ``NodeResponse``; that is a
change to the response shape and is deliberately not made here.
"""

from __future__ import annotations

from typing import Final, Literal, get_args

from econflow_engine.errors import GateError

__all__ = ["GATE_DETAIL_CODES", "GateDetailCode", "refusal"]

#: TWO FAMILIES, AND THE LINE BETWEEN THEM IS WHO CAN FIX IT.
#:
#: ``precondition-*``
#:     the CALLER'S DATA violates a documented requirement of the method. The
#:     user can act on it -- supply more observations, drop a constant column,
#:     choose a method that admits an unbalanced panel.
#: ``gate-argument``
#:     the gate was called wrongly by the wrapper AUTHOR, and no change to the
#:     data fixes it. Kept separate so that a bug in a wrapper never reads to a
#:     wrapper author as a problem with the user's data.
GateDetailCode = Literal[
    "precondition-sample-size",
    "precondition-missing",
    "precondition-degenerate",
    "precondition-frequency",
    "precondition-domain",
    "precondition-rank",
    "precondition-panel",
    "precondition-cross-section",
    "precondition-shape",
    "gate-argument",
]

#: The same ten names as a runtime tuple, DERIVED so it cannot drift from the type.
GATE_DETAIL_CODES: Final[tuple[str, ...]] = get_args(GateDetailCode)


def refusal(message: str, code: GateDetailCode) -> GateError:
    """The ONE refusal shape. ``message`` is passed through verbatim.

    No prefixing happens here: the two normative gates build their own ``fn:``
    label (with an empty-``fn`` branch) and the primitives build theirs, and
    reshaping either would rewrite messages this change is only meant to give a
    code to.
    """
    return GateError("other", message, detail_code=code)
