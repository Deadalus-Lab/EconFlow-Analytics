# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.1.4 -- does a fixture actually REACH the body, or merely sit beside it?

WHAT THIS ASSERTS. A dataset named by a ``$fixture`` value form is built, put in
the real session registry, and delivered through the real argument adapter, and
the value the body receives is the one the published table holds. Not that a
frame can be built -- that a frame BUILT HERE arrives THERE.

WHY THE CONTROLS ARE THE PROOF TODAY, and it is the same reason
:mod:`tests.controls.double_run` gives. ``engine.n_implemented`` is 0: every
wrapper body is a typed stub that raises, so no real body can be watched reading
a dataset. A harness that iterated the implemented set and printed "all reached"
would have examined NOTHING -- the exact defect every gate in this tree is
written to refuse. So four node-shaped callables are planted and driven down the
real path, and their verdicts are asserted individually.

THE PATH IS THE REAL ONE, NOT A REBUILT ONE. Each control is delivered by
``build`` -> ``registry_put`` -> ``adapt_args`` -> ``resolve_handle`` ->
``_AS_KIND``, against the CONTRACT OF A REAL NODE read from node-specs.json
through ``node_meta``. A control fed a hand-made DataFrame would prove that this
module can make a DataFrame. Borrowing a real node's argument metadata is what
makes it prove that the delivery path a caller uses carries the data.

THE DETECTOR, in one sentence: build the dataset twice, once as published and
once with every leaf moved, run the callable on both, and compare the BYTES of
the two payloads through the engine's own ``to_json``. If they are the same, the
payload does not depend on the data.

  POSITIVE (MUST be flagged)
    * :func:`ignores_its_handle`  -- never touches the argument at all
    * :func:`reads_only_the_shape` -- touches it, but reads only its length

  NEGATIVE (MUST NOT be flagged)
    * :func:`reads_the_data`       -- a sum over the values
    * :func:`names_its_columns`    -- a payload that legitimately does not depend
                                      on the values, and DECLARES that it does not

WHY TWO POSITIVES THAT FAIL THE SAME TEST. They are the two real mechanisms by
which a body stops reading its input, and they look completely different in
source. The first is a body written before its data was wired up -- a constant
returned from a stub somebody forgot to finish. The second is subtler and is the
one that survives review: a body that genuinely uses its argument, and uses only
its shape, while the payload claims to describe its contents. A detector that
caught the first and missed the second would pass every code review and catch
nothing that a code review would not.

WHY ``names_its_columns`` IS THE NEGATIVE THAT MATTERS. Its payload does not move
when the data moves, exactly like both positives, and the ONLY thing separating
it from them is that it says so. That is deliberate and it is the same doctrine
as ``unchecked_keys`` in the oracle harness: an exemption is admissible when it
NAMES ITSELF, and inadmissible when it is inferred. A detector without this
control would have no way to express a correct value-independent payload, and
would be turned off the first time somebody wrote one.

    usage: python -m tests.controls.fixture_reach   (run from engine/)
"""

from __future__ import annotations

import sys
from collections.abc import Callable
from typing import Any

from tests.conformance.fixtures import build_fixture, moved_builder
from tests.controls.double_run import digest

#: The node whose CONTRACT the controls are delivered against. Chosen because its
#: single required argument is one ``df_handle``, which is the shortest real path
#: from a published table to a body, and because it registers no result -- so a
#: run of this module leaves nothing in the store to evict a later handle.
NODE = "fast_summary"

#: The published table. Anscombe's eleven (x, y) pairs: small enough to read in
#: full, and already carried by two committed oracle cases.
DATASET = "anscombe_1973_data_set_i"

#: THE MOVE IS NOT A TOLERANCE QUESTION. The oracle harness perturbs by ten times
#: a class's own rtol because it is asking whether a COMPARISON can fail. This
#: module asks whether the data arrived at all, and a move that a floating-point
#: sum could swallow would make a reaching body look like an ignoring one. So the
#: move is unmistakable -- ten times 1e-6 relative on every leaf -- and the two
#: questions stay separate.
REACH_RTOL = 1e-6
REACH_ATOL = 1e-12


def ignores_its_handle(**_: Any) -> dict[str, float]:
    """POSITIVE. A constant: the argument is never read, so no data can reach it."""
    return {"value": 42.0}


def reads_only_the_shape(**kwargs: Any) -> dict[str, float]:
    """POSITIVE. Reads the frame's LENGTH and calls the answer a total.

    The dangerous shape, because it survives review: the argument is genuinely
    used, so nothing about the source says "this body ignores its input", and the
    payload nonetheless describes contents it never looked at.
    """
    return {"total": float(len(kwargs["x"]))}


def reads_the_data(**kwargs: Any) -> dict[str, float]:
    """NEGATIVE. A sum over the values, which is what a reaching body looks like."""
    return {"total": float(kwargs["x"].to_numpy().sum())}


def names_its_columns(**kwargs: Any) -> dict[str, Any]:
    """NEGATIVE. A payload that legitimately does not depend on the values.

    Naming a frame's columns is a real thing for a body to return, and the answer
    is the same whatever the numbers are. It is admissible for one reason: the
    control DECLARES that it does not depend on the values, and the detector
    reads that declaration rather than inferring it.
    """
    return {"columns": list(kwargs["x"].columns)}


#: ``(name, callable, depends_on_values, must_be_flagged)``. The third field is
#: the declaration described above; the fourth is the verdict this module must
#: reach, and it is asserted for every control on every run.
CONTROLS: tuple[tuple[str, Callable[..., Any], bool, bool], ...] = (
    ("ignores_its_handle", ignores_its_handle, True, True),
    ("reads_only_the_shape", reads_only_the_shape, True, True),
    ("reads_the_data", reads_the_data, True, False),
    ("names_its_columns", names_its_columns, False, False),
)


def _say(message: str) -> None:
    """This module IS a gate; what it prints is its report."""
    print(message)  # noqa: T201


def deliver(builder: Callable[[str], Any]) -> dict[str, Any]:
    """A dataset -> the keyword arguments a body receives, by the production path.

    Every step here is the one a caller's request goes through. The handle is
    dropped again immediately: ``adapt_args`` has already resolved it by the time
    this returns, and a control run that left handles behind would eat into the
    512-entry bound the store evicts against.
    """
    from econflow_engine.loader import node_meta
    from econflow_engine.mcp.adapters import adapt_args
    from econflow_engine.mcp.registry import registry_clear, registry_put

    meta = node_meta(NODE)
    required = [a.name for a in meta.args if a.required]
    if len(required) != 1:
        sys.exit(
            f"FAIL: {NODE} declares {len(required)} required argument(s) {required}; "
            f"this module drives a single-argument contract. Choose another node "
            f"and say why in NODE above."
        )
    handle = registry_put(builder(DATASET), meta={"fixture": DATASET})
    try:
        return adapt_args(meta, {required[0]: handle})
    finally:
        registry_clear(handle)


def payload_ignores_the_data(body: Callable[..., Any]) -> tuple[bool, str, str]:
    """Run the body on the published table and on a moved one; compare the bytes."""
    first = digest(body(**deliver(build_fixture)))
    second = digest(body(**deliver(moved_builder(REACH_RTOL, REACH_ATOL))))
    return first == second, first, second


def _fail(detail: list[str], message: str) -> int:
    """Print the offending rows, then the reason. Always returns 1."""
    for row in detail:
        _say(row)
    if detail:
        _say("")
    print(message, file=sys.stderr)  # noqa: T201
    return 1


def check_controls() -> int:
    """Drive every planted control. Returns the count, or 0 on a bad verdict.

    A positive control that goes unflagged and a negative control that gets
    flagged are DIFFERENT defects and are reported separately, exactly as
    ``double_run.check_controls`` reports them: the first means this module
    cannot detect a body ignoring its input at all, so a green run means nothing;
    the second means it has decayed into a rule that refuses correct code.
    """
    holes: list[str] = []
    false_alarms: list[str] = []
    for name, body, depends_on_values, must_be_flagged in CONTROLS:
        unmoved, first, second = payload_ignores_the_data(body)
        flagged = unmoved and depends_on_values
        if must_be_flagged and not flagged:
            holes.append(
                f"HOLE         {name}: the payload was expected to be unchanged by "
                f"moved data and was not ({first} != {second})"
            )
        elif not must_be_flagged and flagged:
            false_alarms.append(
                f"FALSE ALARM  {name}: both runs hashed {first}, and this control "
                f"reads the data or declares that it does not depend on it"
            )

    if holes:
        _fail(
            holes,
            f"FAIL: {len(holes)} positive control(s) were NOT flagged. This module "
            "cannot detect a body that ignores the dataset delivered to it, so a "
            "fixture case could be green having compared nothing.",
        )
        return 0
    if false_alarms:
        _fail(
            false_alarms,
            f"FAIL: {len(false_alarms)} negative control(s) were flagged. A body "
            "that reads its data, and one whose payload declares no dependence on "
            "the values, are both correct; a gate that refuses them is unusable "
            "and would be turned off.",
        )
        return 0
    return len(CONTROLS)


def main() -> int:
    """Drive the controls and report the count, with the path they travelled."""
    controls_run = check_controls()
    if controls_run == 0:
        return 1
    _say(
        f"ok: {controls_run} control(s) driven from tests/fixtures/{DATASET}.json "
        f"through registry_put -> adapt_args -> resolve_handle against the "
        f"contract of {NODE} "
        f"({sum(1 for *_, c in CONTROLS if c)} positive / "
        f"{sum(1 for *_, c in CONTROLS if not c)} negative controls all fired)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
