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

THE METHOD LEG HAS CONTROLS OF ITS OWN AND THEY LIVE ELSEWHERE, named here so
that a reader who does not find them above does not conclude there are none.
``engine/tests/test_double_run_methods.py`` plants a body into a hardlink mirror
of ``engine/`` and runs THIS module against it as a subprocess. Two must go
green: a body reached by its oracle case, and one reached by a payload file. The
rest must turn it red with the method named -- a body with no call at all, one
whose arguments the wire contract refuses, one that raises something that is not
a ``GateError``, one whose payload is a foreign-object stub, one that returns the
wall clock, one whose second run does not succeed, a public function that is not
a node, and a public function whose name collides with another module's node.
Those controls are what exercise the code below, which the committed tree, having
no bodies in it, cannot.

TWO COUNTS ARE PRINTED, NOT ONE, and both are checked:

  methods  double-run wrapper bodies. Compared EXACTLY against
           ``engine.n_implemented``, so it is 0 == 0 today and rises on its own
           with the first body written in 2.2 -- no second edit to this file.
  controls double-run planted controls. Compared EXACTLY against the size of the
           planted set. Non-zero, which is what makes a green run mean something.

WHAT HAPPENS WHEN THE FIRST BODY LANDS, stated plainly because it is deliberate.
A method cannot be run at all without an input payload. This paragraph was
written when nothing in the tree committed one -- ``parity-fixtures.json`` holds
argument-adapter VERDICTS (accept/reject per argument), not call arguments -- and
it concluded that the first body written in 2.2 would turn this gate red until it
arrived with the means to run itself twice. HALF OF THAT IS NO LONGER TRUE, and
the half that changed is recorded rather than erased: ``engine/tests/oracle/`` IS
a committed source of calls, so a body whose output somebody tabulated arrives
with its call already in the tree and goes green with no payload file written for
it at all -- see the UNION paragraph below. What has NOT changed is the refusal
this box exists for: the method leg enumerates the implemented set and REFUSES to
go green while skipping any member of it, naming each one. A body that arrives
with neither an oracle case nor a payload still turns this red, which is the
correct outcome and the opposite of a harness that silently skips it.

THE INVOCATION PAYLOAD, DEFINED BEFORE ANYTHING NEEDS IT (decision A4). The
paragraph above says what turns red. This says what makes it green again, so that
the first body author in 2.2 reads a contract instead of inventing one under the
pressure of a red gate -- an invented contract is the one that becomes permanent.
``engine.invocation_payloads`` in .github/inventory.json used to read
"unmeasured", which assert-inventory printed as OWED. It reads 0 now: the first
2.2 body arrived reached by its ORACLE CASE, so ``tests/payloads/`` was built --
which is what makes the constant measurable -- and holds no payload file yet.

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

HANDLES WERE NOT EXPRESSIBLE WHEN THIS WAS WRITTEN, AND NOW THEY ARE. A series, a
frame or a pointer is produced by an earlier call, and a JSON literal cannot hold
one. ``oracle.literal_callable_nodes`` counts the nodes whose required arguments
are all literal kinds -- 103 of 1456 -- and that was exactly the set a payload
could reach. This paragraph used to end by refusing to invent a fixture form and
requiring one to be agreed first; box 2.1.1.4 agreed it on 2026-08-27, so a
payload's ``inputs`` now take the same ``{"$fixture": name}`` and ``{"$produce":
...}`` forms an oracle case takes, resolved by the SAME code -- see the seam
below. The refusal stands where it still binds: the 19 nodes behind a required
``path`` remain out of reach, and the honest outcome there is a red line naming
the method, not a handle argument filled with a plausible-looking zero.

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
exercise the method, and nobody but the body's author can make it. That is also
why a payload naming a method with no body is refused here rather than ignored:
it runs nothing, and it would raise ``engine.invocation_payloads`` on behalf of a
call this gate never makes. REJECTED: deriving one from ``node-specs.json``
defaults, because a call assembled from declared kinds is a degenerate call, a
degenerate result is trivially reproducible, and this gate would then go green
having proved nothing -- the exact vacuity it exists to refuse. REJECTED:
emitting one from ``gen_wrappers.py --scaffold-tests``, because the generated tier
is byte-compared by ``gen_wrappers.py --check`` at step 1, so a hand-edited
scaffold turns that step red instead of this one.

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

HOW THIS HARNESS CONSUMES IT. ``check_methods`` resolves each implemented method
to a call, preferring a hand-authored payload where a body has both, and
double-runs it through the same :func:`digest` comparison the controls already
use. A method with no call at all stays a red line naming it, and so does one
whose call does not succeed: a refusal reproduces perfectly, so counting it as a
pass would let a body that refuses every input satisfy this gate. Step 10 of
run_verifications.sh then prints a non-zero method count beside the control count.
``engine.invocation_payloads`` does NOT follow from that count and must not be
read as though it does: it counts FILES under ``tests/payloads/``, and a body
reached by its oracle case turns this gate green having produced none. That is
exactly how the word WAS retired: the first call came from the oracle half, and
the constant measures only the other one.

THE CALL IS BOUND BY THE ORACLE HARNESS, NOT BY A SECOND COPY OF IT.
``tests.conformance.test_conformance`` exposes ``admissible_calls`` and
``run_call`` for exactly this, so fixture substitution through ``registry_put``,
``$produce`` at depth 1 and per-handle cleanup have ONE implementation. A second
one here would be free to disagree with it in silence, and a determinism gate that
binds arguments differently from the harness that proved them is comparing a call
no caller makes. A payload's ``$fixture`` and ``$produce`` references are resolved
by that same harness at LOAD time, so a payload naming a dataset that does not
exist is refused by name rather than raising out of the first run.

WHAT THIS GATE STILL DOES NOT PROVE, NAMED HERE RATHER THAN LEFT TO BE
DISCOVERED, in the spirit of the A4 paragraph above. 320 of the 1456 nodes carry
a ``register`` field: they hand the caller a HANDLE to a live object and a
payload beside it. ``_run_case`` returns ``response.payload`` and DISCARDS
``response.handle``, and ``to_mcp``'s default branch stubs any object it cannot
serialise into ``{"@mcp_class": [...], "@mcp_serialized": false, ...}`` -- a class
name and a length. The digest of such a payload is therefore a digest of a class
name, and two runs of a body returning a freshly fitted object hash equal
whatever the fit did. Measured: a body returning a new object on every call
passed this gate before the check below existed. WHAT IS DONE HERE is only to
name it: ``check_methods`` refuses such a payload outright and lists the method
as UNRUN with the classes it stubbed, so the gate says "not proven" where it used
to say "proven". WHAT IS OWED is the fix -- a seam exposing ``response.handle``
so this harness can ``registry_get`` the live object and digest THAT, before
``_run_case``'s ``finally`` clears the handle. It is a change to the shared oracle
seam rather than to this file, it belongs in its own box, and it is what would
turn a registering body from refused into proven. Until it lands, a body whose
result is not serialisable cannot satisfy this gate, and that is the honest state
rather than a gap.

BOTH RUNS SHARE ONE PROCESS, WHICH BOUNDS WHAT THIS CAN SEE. A body memoised with
``functools.cache`` returns the SAME object on its second call by construction, so
the two digests agree whatever the body computes. This gate cannot see
nondeterminism hiding behind a cache, and a 2.2 author reaching for one should
know that a green line here does not cover it.

    usage: python -m tests.controls.double_run   (run from engine/)
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from collections.abc import Callable
from typing import Any

from econflow_engine.metrics import find_manifest, stub_ledger
from econflow_engine.serialize import stub, to_json
from tests.conformance.test_conformance import (
    ENGINE_NAMESPACE,
    Case,
    Inadmissible,
    _resolve_target,
    _scan_inputs,
    admissible_calls,
    run_call,
)
from tests.controls.determinism import CONTROLS

ENGINE_ROOT = pathlib.Path(__file__).resolve().parents[2]
WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
MANIFEST = find_manifest(pathlib.Path(__file__))

#: Where a hand-authored payload lives, mirroring ``tests/oracle/``. The tree now
#: exists and holds no payload yet: the one implemented body is reached by its
#: oracle case, so ``engine.invocation_payloads`` is a measured 0 rather than the
#: OWED marker it carried while the directory was absent.
PAYLOADS = ENGINE_ROOT / "tests" / "payloads"

#: The closed key set of a payload file. A payload carries no ``expected``, no
#: ``tolerance_class`` and no ``citation``: determinism asks whether two runs
#: agree with EACH OTHER, never whether either agrees with a published number.
PAYLOAD_KEYS = frozenset({"fn", "inputs", "notes"})

#: A wrapper function as this gate identifies it: ``(namespace, module, fn)``.
#: NOT the bare ``fn``. A public function beside a body whose name happens to
#: match another module's node would, keyed on the bare name, resolve to that
#: node's call, run that node twice and be counted as a double-run while its own
#: code never executed.
Node = tuple[str, str, str]

#: The two fields of ``econflow_engine.serialize.stub``'s refusal record that
#: :func:`foreign_stubs` reads. Their presence is PROBED in :func:`main` rather
#: than assumed, because a renamed key would leave that check reading a field
#: that no longer exists and passing every stubbed payload in silence.
SERIALISED_FIELD = "@mcp_serialized"
CLASS_FIELD = "@mcp_class"


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


def implemented_methods() -> tuple[tuple[pathlib.Path, str], ...]:
    """Every wrapper function whose body is NOT the emitted raise, with its file.

    The walk is ``econflow_engine.metrics.stub_ledger``, which is also what the
    ``n_implemented`` figure in ``.github/actions/assert-inventory/assert.sh``
    is held to. Two walks answering "is this a stub?" differently would let a
    method be implemented by one measure and not by the other, and this harness
    compares its own count against that one.

    THE PATH IS YIELDED BESIDE THE NAME because it is what makes the name
    unambiguous. ``stub_ledger`` yields every PUBLIC function, which is a wider
    set than the node manifest, and :func:`check_methods` narrows it with the
    path in hand.
    """
    return stub_ledger(WRAPPERS).implemented


def _label(path: pathlib.Path, name: str) -> str:
    """How one method is named in this gate's report: its file, then its function."""
    return f"{path.relative_to(ENGINE_ROOT)}::{name}"


def _node_of(path: pathlib.Path, name: str) -> Node:
    """The triple a wrapper function is filed under, read from its PATH.

    ``src/econflow_engine/wrappers/<package>/<module>.py`` is the same
    ``<package>/<module>`` an oracle case and a payload are filed under, which is
    what lets the three be compared without a fourth spelling of the mapping.
    """
    return path.parent.name, path.stem, name


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


def payload_files() -> list[pathlib.Path]:
    """Every committed payload file, or none where the tree does not exist yet.

    The underscore skip mirrors ``tests/oracle``: a file whose name begins with
    one is apparatus beside the corpus, not a member of it, and
    ``assert-inventory`` counts this same set with the same exclusion.
    """
    if not PAYLOADS.is_dir():
        return []
    return sorted(p for p in PAYLOADS.rglob("*.json") if not p.name.startswith("_"))


def load_payload(path: pathlib.Path) -> Case:
    """One payload file, as a call. A file that is not one is a failure, never a skip.

    The key set is CLOSED and checked in both directions. A payload carrying an
    ``expected`` would be an oracle case filed where nothing checks its citation,
    and a payload missing ``notes`` would be a choice of arguments with no record
    of why those arguments exercise this body -- which is the whole content of the
    choice.

    ``namespace`` and ``module`` come from the PATH rather than from the file, and
    ``_resolve_target`` -- the oracle loader's own check rather than a second copy
    of it -- is what makes a payload filed under the wrong module a mismatch
    instead of a self-certifying one. The ``engine`` namespace is refused outright
    here: it binds ``fn`` by ``getattr`` on a module, reaching past the gateway,
    the MANIFEST and ``__all__``, and this leg answers for WRAPPER bodies.

    ``_scan_inputs`` IS CALLED HERE AND NOT LEFT TO THE FIRST RUN, for the same
    reason ``_load_case`` calls it: it is what turns a ``{"$fixture": ...}``
    naming no dataset into a refusal that names the file and the dataset, where
    the run would raise ``FixtureError`` out of the loop as a traceback. It also
    fills ``fixtures`` and ``produce_chain``, which a payload built without it
    would leave empty while claiming to reach a dataset.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        sys.exit(f"FAIL: {path} is not a JSON object.")
    keys = frozenset(raw)
    if keys != PAYLOAD_KEYS:
        sys.exit(
            f"FAIL: {path} carries keys {sorted(keys)}, expected exactly "
            f"{sorted(PAYLOAD_KEYS)}. Extra: {sorted(keys - PAYLOAD_KEYS)}; "
            f"missing: {sorted(PAYLOAD_KEYS - keys)}."
        )
    if not isinstance(raw["inputs"], dict):
        sys.exit(f"FAIL: {path} has a non-object 'inputs'.")
    namespace, module, fn = path.parent.parent.name, path.parent.name, str(raw["fn"])
    if namespace == ENGINE_NAMESPACE:
        sys.exit(
            f"FAIL: {path} is filed under '{ENGINE_NAMESPACE}/', which names a PUBLIC "
            "helper rather than a node. This leg double-runs wrapper bodies, and a "
            "helper reached by getattr is not a call any caller makes."
        )
    inputs = dict(raw["inputs"])
    try:
        _resolve_target(namespace, module, fn)
    except Inadmissible as refusal:
        sys.exit(f"FAIL: {path} does not name the node it is filed under: {refusal}")
    try:
        datasets, chain = _scan_inputs(inputs)
    except Inadmissible as refusal:
        sys.exit(f"FAIL: {path} names something the tree does not hold: {refusal}")
    return Case(
        id=f"{namespace}/{module}/{path.stem}",
        fn=fn,
        module=module,
        namespace=namespace,
        inputs=inputs,
        expected=None,
        unchecked_keys=(),
        tolerance_class="",
        rtol=0.0,
        atol=0.0,
        fixtures=tuple(datasets),
        produce_chain=tuple(chain),
    )


def payload_calls() -> dict[Node, tuple[Case, pathlib.Path]]:
    """Every committed payload, as a call, keyed by the node it runs.

    TWO FILES NAMING ONE NODE ARE REFUSED rather than resolved. Written into a
    mapping in sorted order, the second would simply replace the first, so one of
    the two calls a reviewer approved would never be made and nothing would say
    so. Both file names are printed, because the choice of which to keep is the
    author's.
    """
    found: dict[Node, tuple[Case, pathlib.Path]] = {}
    for path in payload_files():
        case = load_payload(path)
        key = (case.namespace, case.module, case.fn)
        if key in found:
            sys.exit(
                f"FAIL: {found[key][1]} and {path} both name '{case.fn}'. One node "
                "takes one payload here: a second would silently replace the first "
                "and the call it carries would never be made."
            )
        found[key] = (case, path)
    return found


def calls_by_node() -> tuple[dict[Node, Case], dict[Node, pathlib.Path]]:
    """Every call this gate can make, and where each payload file came from.

    THE SOURCE IS A UNION. An admissible oracle case already carries ``fn`` and
    ``inputs``, so a body that has one needs no second file; a payload file is
    written only for a body whose output nobody tabulated, which is most of them.
    A hand-authored payload wins where a body has both, because it was written
    for this gate while the case was written for the literature. Engine-helper
    cases are excluded: they call a helper rather than a wrapper body, and this
    leg answers for wrapper bodies.
    """
    calls: dict[Node, Case] = {
        (case.namespace, case.module, case.fn): case
        for case in admissible_calls()
        if case.namespace != ENGINE_NAMESPACE
    }
    payloads = payload_calls()
    for key, (case, _) in payloads.items():
        calls[key] = case
    return calls, {key: path for key, (_, path) in payloads.items()}


def foreign_stubs(payload: object) -> list[str]:
    """Every refusal-to-serialise record inside a payload, by the class it names.

    ``to_mcp``'s default branch STUBS a foreign object -- a fitted model, a
    closure, an open connection -- into a record whose only fields are a class
    NAME and a length. Hashing that record answers whether the stub reproduces,
    which it always does, and says nothing about the body that produced the
    object. Walked RECURSIVELY because ``to_mcp`` recurses through mappings and
    sequences: a stub nested beside real numbers is the same defect one level
    down, and the seam that would fix it (see the module docstring) fixes both.
    """
    if isinstance(payload, dict):
        if payload.get(SERIALISED_FIELD) is False:
            return [str(name) for name in payload.get(CLASS_FIELD, ["?"])]
        return [found for value in payload.values() for found in foreign_stubs(value)]
    if isinstance(payload, list):
        return [found for value in payload for found in foreign_stubs(value)]
    return []


def _run_once(case: Case) -> tuple[str, Any]:
    """One run of one call, with a raising body REPORTED rather than propagated.

    ``run_method`` turns a stub's ``NotImplementedError`` and a body's
    ``GateError`` into states; every other exception reaches this loop as a
    traceback. Measured: a planted ``raise ValueError`` ended the process on the
    first method, printed no red line for it, and left every later method
    unexamined. The catch belongs here and not in ``make_tool``, whose callers
    have their own error handling and are entitled to see the exception -- but a
    gate that reports one method by hiding the rest is worse than the crash it
    replaced.
    """
    try:
        return run_call(case)
    except Exception as exc:  # noqa: BLE001 - reported as a red line, never swallowed
        return "raised", f"{type(exc).__name__}: {exc}"


def _double_run(case: Case) -> tuple[str, str]:
    """Run one call twice and judge it. ``("", "")`` when the two runs agree.

    The other verdicts are ``unrun`` -- the call did not reach the body, or
    reached it and returned something this gate cannot hash meaningfully -- and
    ``moved``, the bytes differing between two runs of the same call.

    A SECOND RUN THAT DID NOT SUCCEED IS NOT FOLDED INTO THE DIGEST COMPARISON.
    It usually leaves the two digests EQUAL, so the shared message would report
    "MOVED x != x" -- a line whose own numbers contradict its verdict, handed to
    whoever has to act on it.
    """
    first_state, first = _run_once(case)
    if first_state != "succeeded":
        return "unrun", f"its call {first_state} -- {first}"
    stubbed = foreign_stubs(first)
    if stubbed:
        return "unrun", (
            f"its payload is a to_mcp refusal record for {sorted(set(stubbed))}, so "
            "the digest is taken over a class name and this gate has not run the body"
        )
    second_state, second = _run_once(case)
    if second_state != "succeeded":
        return "moved", f"run 1 succeeded, run 2 {second_state} -- {second}"
    before, after = digest(first), digest(second)
    if before != after:
        return "moved", f"{before} != {after}"
    return "", ""


def _report(
    not_a_node: list[str], orphans: list[str], unrun: list[str], moved: list[str]
) -> int:
    """The four ways this leg goes red, each with the message its rows call for.

    Reported in the order a reader can act on them: what is not a method at all,
    then a payload with nothing to run, then a method that was not run, then one
    that did not reproduce.
    """
    if not_a_node:
        return -_fail(
            not_a_node,
            f"FAIL: {len(not_a_node)} public function(s) in the wrapper tree are "
            "counted as implemented methods and are NOT nodes. RENAME EACH ONE WITH "
            "A LEADING UNDERSCORE; do not write a payload for it. `stub_ledger` "
            "counts every public function in a wrapper module, the manifest knows "
            "only the 1456 node functions, and a public helper beside a body has no "
            "wire contract to be called through. A helper whose name collides with "
            "ANOTHER module's node is listed here too and is the more dangerous "
            "case: it has a call in the tree that is not its own.",
        )
    if orphans:
        return -_fail(
            orphans,
            f"FAIL: {len(orphans)} payload file(s) name a method with no body. A "
            "payload lands in the same commit as the body it runs; one that arrives "
            "without a body runs nothing here and raises the file count that "
            "engine.invocation_payloads reports.",
        )
    if unrun:
        return -_fail(
            unrun,
            f"FAIL: {len(unrun)} implemented method(s) were enumerated and NOT "
            "double-run. THE CONTRACT IS ALREADY WRITTEN AND YOU ARE NOT MEANT TO "
            "INVENT ONE: the module docstring above gives the payload's shape, "
            "where the file goes, what produces it, and why an oracle case counts "
            "as one. A method whose call does not succeed is listed here too -- a "
            "refusal reproduces, but it exercises the gate rather than the body -- "
            "and so is one whose payload is a foreign-object stub, whose digest is "
            "a class name rather than a result. A harness that skipped these and "
            "printed 'all match' is the defect box 2.1.14 exists to prevent.",
        )
    if moved:
        return -_fail(
            moved,
            f"FAIL: {len(moved)} method(s) returned different BYTES on two runs of "
            "the same call. A method handed the same inputs must return the same "
            "result; find the unseeded draw, the wall clock or the set iteration "
            "before this lands.",
        )
    return 0


def check_methods() -> int:
    """Double-run every implemented method and refuse to skip any. -1 on failure.

    THE IMPLEMENTED SET IS INTERSECTED WITH THE NODE MANIFEST, and that is not a
    tidying step. ``stub_ledger`` yields every PUBLIC function in a wrapper
    module, which is 1:1 with the manifest today only because no author has yet
    written a public helper beside a body. The first one who does would otherwise
    be told to "land its payload" -- advice that cannot be followed, since a
    helper has no wire contract -- when the fix is to rename it with a leading
    underscore. ``_resolve_target`` is the check, reused rather than restated: it
    refuses a name the manifest does not hold AND a name filed under a module
    that is not the node's own, which is the collision case.
    """
    methods = list(implemented_methods())
    floor = inventory("engine", "n_implemented")
    if len(methods) != floor:
        return -_fail(
            [],
            f"FAIL: found {len(methods)} implemented method(s), the manifest says "
            f"{floor}. Re-run the engine.n_implemented command in "
            ".github/inventory.json and move the number in its own diff.",
        )

    calls, payload_paths = calls_by_node()
    not_a_node: list[str] = []
    unrun: list[str] = []
    moved: list[str] = []
    for path, name in methods:
        label, node = _label(path, name), _node_of(path, name)
        try:
            _resolve_target(*node)
        except Inadmissible as refusal:
            not_a_node.append(f"NOT A NODE  {label}: {refusal}")
            continue
        case = calls.get(node)
        if case is None:
            unrun.append(f"UNRUN    {label}: no oracle case and no payload file")
            continue
        verdict, detail = _double_run(case)
        if verdict == "unrun":
            unrun.append(f"UNRUN    {label}: {detail}")
        elif verdict == "moved":
            moved.append(f"MOVED    {label}: {detail}")

    implemented = {_node_of(path, name) for path, name in methods}
    orphans = sorted(
        f"ORPHAN   {path.relative_to(ENGINE_ROOT)}: '{node[2]}' has no body"
        for node, path in payload_paths.items()
        if node not in implemented
    )
    failed = _report(not_a_node, orphans, unrun, moved)
    return failed if failed else len(methods)


def main() -> int:
    """Double-run the controls and the implemented methods; report both counts."""
    if not WRAPPERS.is_dir():
        sys.exit(f"FAIL: no wrapper tree at {WRAPPERS}; this gate cannot start.")
    probe = stub(object())
    if probe.get(SERIALISED_FIELD) is not False or CLASS_FIELD not in probe:
        sys.exit(
            f"FAIL: econflow_engine.serialize.stub emits {sorted(probe)}, which does "
            f"not carry {SERIALISED_FIELD} and {CLASS_FIELD}. foreign_stubs would "
            "then read a field that does not exist and pass every stubbed payload."
        )

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
