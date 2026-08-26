# SPDX-License-Identifier: AGPL-3.0-only
"""Box 2.1.14 -- run it twice, compare the BYTES, and prove the comparison works.

WHAT THIS ASSERTS. A method handed the same inputs returns the same result. Not
an equal object -- the same BYTES, which is the standard the rest of this tree
already holds itself to: every committed artifact carries a ``.sha256`` sidecar
and ``assert-inventory`` re-hashes it. Object equality is a weaker claim and
would pass on differences that a consumer downstream can see, because ``==`` on a
DataFrame ignores column order in some paths, ``==`` on a float ignores nothing
but ``nan != nan`` makes it useless, and neither notices a set that iterated in a
different order. Serialising through :func:`econflow_engine.serialize.to_json`
and comparing the encoded bytes is the same question the sidecars ask.

WHY THE CONTROLS ARE THE PROOF TODAY. ``engine.n_implemented`` is 0: every
wrapper body is a typed stub that raises, so ZERO methods qualify for a double
run. A harness that iterated an empty set and printed "all match" would be
exactly the defect this box exists to prevent -- the sixth occurrence of it.
So the planted controls in :mod:`tests.controls.determinism` are double-run on
every invocation and their verdicts are asserted individually: three that MUST be
caught, two that MUST NOT be.

TWO COUNTS ARE PRINTED, NOT ONE, and both are checked:

  methods  double-run wrapper bodies. Compared EXACTLY against
           ``engine.n_implemented``, so it is 0 == 0 today and rises on its own
           with the first body written in 2.2 -- no second edit to this file.
  controls double-run planted controls. Compared EXACTLY against the size of the
           planted set. Non-zero, which is what makes a green run mean something.

WHAT HAPPENS WHEN THE FIRST BODY LANDS, stated plainly because it is deliberate.
A method cannot be run at all without an input payload, and this repository has
no committed source of wrapper invocation payloads today: ``parity-fixtures.json``
holds argument-adapter VERDICTS (accept/reject per argument), not call arguments.
Inventing one now would be speculative code for a caller that does not exist. So
the method leg enumerates the implemented set and REFUSES to go green while
skipping any member of it, naming each one. The first body written in 2.2 will
turn this red until it arrives with the means to run it twice -- which is the
correct outcome, and the opposite of a harness that silently skips it.

THE INVOCATION PAYLOAD, DEFINED BEFORE ANYTHING NEEDS IT (decision A4). The
paragraph above says what turns red. This says what makes it green again, so that
the first body author in 2.2 reads a contract instead of inventing one under the
pressure of a red gate -- an invented contract is the one that becomes permanent.
Until the first payload lands, ``engine.invocation_payloads`` in
.github/inventory.json reads "unmeasured", which assert-inventory prints as OWED.

SHAPE. One payload is one call, and it carries NO claim about the result::

    {"fn": "rs_multiple_testing",
     "inputs": {"p_values": [0.0001, 0.0004], "method": "bh", "alpha": 0.05},
     "notes": "why these arguments exercise this body rather than any others"}

``fn`` names a node function -- a key of :data:`econflow_engine.loader.MANIFEST`.
``inputs`` maps argument name to value and is bound exactly as the conformance
harness binds a case: ``run_method(fn, inputs)`` for a node, and
``signature(helper).bind(**inputs)`` for an engine helper. There is deliberately
no ``expected``, no ``tolerance_class`` and no ``citation``. Determinism asks
whether two runs agree with EACH OTHER, never whether either agrees with a
published number, and requiring a citation would make a method's determinism
depend on whether anybody happened to tabulate its output.

HANDLES ARE NOT EXPRESSIBLE, AND THIS SAYS SO RATHER THAN GUESSING. A series, a
frame or a pointer is produced by an earlier call, and a JSON literal cannot hold
one. ``oracle.literal_callable_nodes`` counts the nodes whose required arguments
are all literal kinds -- 103 of 1456 -- and that is exactly the set a payload can
reach today. A body outside those 103 needs a fixture form this definition
deliberately does not invent. It must not land until one is agreed: the honest
outcome is a red line naming the method, not a handle argument filled with a
plausible-looking zero.

WHERE IT LIVES. ``engine/tests/payloads/<package>/<module>/<name>.json``, mirroring
``engine/tests/oracle/`` so a payload is filed under the module it calls and a
misfiled one is visible. NOT ``engine/artifacts/``, sealed by
``artifacts.sidecars = 7`` under exact equality, where every payload would be a
re-seal across the corpus. NOT inside ``engine/tests/oracle/``, whose case key set
is CLOSED: a payload carries neither ``expected`` nor ``citation`` and would load
as Inadmissible, and hiding it behind the underscore that ``_case_files`` skips
would put a file in a directory whose own harness ignores it. NOT the repository
root, which is deny-by-default under ``.github/root-manifest.txt``. And nowhere
untracked: a payload this gate cannot read is not a payload it can run.

WHAT PRODUCES IT, AND WHAT WAS REJECTED. Hand-authored, one per implemented body,
landing in the SAME COMMIT as that body -- a payload is a choice of arguments that
exercise the method, and nobody but the body's author can make it. REJECTED:
deriving one from ``node-specs.json`` defaults, because a call assembled from
declared kinds is a degenerate call, a degenerate result is trivially
reproducible, and this gate would then go green having proved nothing -- the exact
vacuity it exists to refuse. REJECTED: emitting one from
``gen_wrappers.py --scaffold-tests``, because the generated tier is byte-compared
by ``gen_wrappers.py --check`` at step 1, so a hand-edited scaffold turns that
step red instead of this one.

AN ORACLE CASE ALREADY IS AN INVOCATION PAYLOAD, and it is reused rather than
copied. A case admitted by tests/conformance/test_conformance.py carries ``fn``
and ``inputs``, and that pair IS the call this harness needs -- the conformance
harness runs it as ``run_method(case.fn, case.inputs)``. So the source is a UNION:
every admissible oracle case contributes its (fn, inputs), and a file under
``tests/payloads/`` is written only for an implemented body that has none. WHAT
REUSE DOES NOT COVER, which is why it is not the whole answer: a case is refused
at load time unless it carries a real number AND a published locator, so a body
whose output nobody tabulated can never have one -- and most bodies are in that
position. Determinism must not wait on the literature.

HOW THIS HARNESS WILL CONSUME IT. ``check_methods`` resolves each implemented
method to a payload, preferring an oracle case, and double-runs it through the
same :func:`digest` comparison the controls already use. A method with no payload
stays a red line naming it. Step 10 of run_verifications.sh then prints a non-zero
method count beside the control count, and ``engine.invocation_payloads`` carries
the file count in place of the word.

    usage: python -m tests.controls.double_run   (run from engine/)
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from collections.abc import Callable, Iterator
from typing import Any

from econflow_engine.metrics import find_manifest, stub_ledger
from econflow_engine.serialize import to_json
from tests.controls.determinism import CONTROLS

ENGINE_ROOT = pathlib.Path(__file__).resolve().parents[2]
WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
MANIFEST = find_manifest(pathlib.Path(__file__))


def _say(message: str) -> None:
    """This module IS a gate; what it prints is its report."""
    print(message)  # noqa: T201


def digest(value: object) -> str:
    """The bytes a consumer would receive, hashed.

    ``to_json`` is the engine's own wire serialisation, so this compares what
    actually leaves the process rather than an in-memory object whose ``__eq__``
    may be looser than the wire is.
    """
    return hashlib.sha256(to_json(value).encode("utf-8")).hexdigest()


def is_nondeterministic(fn: Callable[[], Any]) -> tuple[bool, str, str]:
    """Call twice, hash both results, and report whether the bytes moved."""
    first, second = digest(fn()), digest(fn())
    return first != second, first, second


def implemented_methods() -> Iterator[str]:
    """Every wrapper function whose body is NOT the emitted raise.

    The walk is ``econflow_engine.metrics.stub_ledger``, which is also what the
    ``n_implemented`` figure in ``.github/actions/assert-inventory/assert.sh``
    is held to. Two walks answering "is this a stub?" differently would let a
    method be implemented by one measure and not by the other, and this harness
    compares its own count against that one.
    """
    for path, name in stub_ledger(WRAPPERS).implemented:
        yield f"{path.relative_to(ENGINE_ROOT)}::{name}"


def inventory(section: str, key: str) -> int:
    """Read one asserted constant. A manifest that cannot be read is a failure.

    NO except-and-return-zero. Swallowing the read is what made the collected
    floor vacuous inside the image for its whole existence.
    """
    try:
        return int(json.loads(MANIFEST.read_text(encoding="utf-8"))[section][key])
    except Exception as exc:  # noqa: BLE001 - re-raised immediately with the cause named
        sys.exit(f"FAIL: cannot read {section}.{key} from {MANIFEST}: {exc}")


def _fail(detail: list[str], message: str) -> int:
    """Print the offending rows, then the reason. Always returns 1."""
    for row in detail:
        _say(row)
    if detail:
        _say("")
    print(message, file=sys.stderr)  # noqa: T201
    return 1


def check_controls() -> int:
    """Double-run every planted control. Returns the count, or 0 on a bad verdict.

    A positive control that goes unflagged and a negative control that gets
    flagged are DIFFERENT defects and are reported separately: the first means
    this harness cannot detect nondeterminism at all, the second means it has
    decayed into a rule that refuses correct code.
    """
    holes: list[str] = []
    false_alarms: list[str] = []
    for name, fn, must_be_caught in CONTROLS:
        caught, first, second = is_nondeterministic(fn)
        if must_be_caught and not caught:
            holes.append(f"HOLE         {name}: both runs hashed {first}, so it never fires")
        elif not must_be_caught and caught:
            false_alarms.append(f"FALSE ALARM  {name}: {first} != {second}")

    if holes:
        _fail(
            holes,
            f"FAIL: {len(holes)} positive control(s) were NOT caught. This harness "
            "cannot detect a nondeterministic method, so a green run means nothing.",
        )
        return 0
    if false_alarms:
        _fail(
            false_alarms,
            f"FAIL: {len(false_alarms)} negative control(s) were flagged. A seeded "
            "draw and a constant are reproducible; a gate that refuses them is "
            "unusable and would be turned off.",
        )
        return 0
    return len(CONTROLS)


def check_methods() -> int:
    """Enumerate implemented methods and refuse to skip any. Returns -1 on failure."""
    methods = list(implemented_methods())
    floor = inventory("engine", "n_implemented")
    if len(methods) != floor:
        return -_fail(
            [],
            f"FAIL: found {len(methods)} implemented method(s), the manifest says "
            f"{floor}. Re-run the engine.n_implemented command in "
            ".github/inventory.json and move the number in its own diff.",
        )
    if methods:
        return -_fail(
            [f"UNRUN    {m}" for m in methods],
            f"FAIL: {len(methods)} implemented method(s) were enumerated and NONE was "
            "double-run: no invocation payload reaches them. parity-fixtures.json "
            "holds argument-adapter verdicts, not call arguments. THE CONTRACT IS "
            "ALREADY WRITTEN AND YOU ARE NOT MEANT TO INVENT ONE: the module "
            "docstring above gives the payload's shape, where the file goes, what "
            "produces it, and why an oracle case counts as one. The constant is "
            "engine.invocation_payloads in .github/inventory.json, which reads "
            "'unmeasured' until the first payload lands. A harness that skipped "
            "these and printed 'all match' is the defect box 2.1.14 exists to "
            "prevent.",
        )
    return len(methods)


def main() -> int:
    """Double-run the controls and the implemented methods; report both counts."""
    if not WRAPPERS.is_dir():
        sys.exit(f"FAIL: no wrapper tree at {WRAPPERS}; this gate cannot start.")

    controls_run = check_controls()
    if controls_run == 0:
        return 1

    methods_run = check_methods()
    if methods_run < 0:
        return 1

    floor = inventory("engine", "n_implemented")
    _say(
        f"ok: {methods_run} method(s) and {controls_run} control(s) double-run, "
        f"bytes compared (methods floor {floor}, "
        f"{sum(1 for *_, c in CONTROLS if c)} positive / "
        f"{sum(1 for *_, c in CONTROLS if not c)} negative controls all fired)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
