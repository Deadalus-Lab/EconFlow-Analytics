# SPDX-License-Identifier: AGPL-3.0-only
"""Did the call OPEN a connection? Watched at run time, not parsed.

WHAT THIS ASSERTS, AND HOW IT DIFFERS FROM THE GATE BESIDE IT.
``.github/scripts/check-no-network.sh`` walks the abstract syntax tree of OUR
OWN wrapper source and reports ``0 of 598 wrapper modules reach the network``.
That claim is true and it is narrow: it is a claim about the text of 598 files.
It cannot see a transport reached through a dependency, because the dependency's
source is not in the walk. This module asks the other half of the question -- did
anything, at any depth, in any library, actually open a socket while a wrapper
body ran -- and it answers it by WATCHING the interpreter rather than by reading
anything.

THE HOLE THAT PRODUCED IT, MEASURED. ``textstat`` reaches
``nltk.download('cmudict')`` from ``textstat/backend/utils/_get_cmudict.py:24``
whenever the corpus is not already on disk, and that download resolves and
contacts ``raw.githubusercontent.com`` AT CALL TIME. A body calling
``textstat.flesch_reading_ease`` would therefore reach the network on every call
while ``engine.wrapper_network_calls`` stayed 0, because the wrapper's own source
names no transport. The import-linter contract in ``../pyproject.toml`` has the
same blind spot from the other direction: grimp squashes external packages, so
``wrappers -> textstat -> nltk -> urllib`` is one edge to an opaque node.
``import nltk`` alone pulls ``http.client``, ``socket`` and ``urllib.request``
through ``nltk/pathsec.py:12-20``. A category specified as "no network access" is
about to have bodies written against that guarantee, so the runtime half is
written before the bodies rather than after.

AN AUDIT HOOK, AND WHY NOT THE ALTERNATIVES. :func:`sys.addaudithook` (PEP 578)
receives every ``socket.*``, ``urllib.*``, ``ftplib.*`` ... event the interpreter
raises, from C, before the operation happens. It cannot be evaded by a library
importing differently, because there is no name to rebind. MEASURED, on this
tree, with ``socket.socket`` and ``socket.create_connection`` monkeypatched and a
spy installed on both: ``_socket.socket(AF_INET, SOCK_STREAM)`` -- the C
accelerator every patch of the Python name leaves untouched -- produced
``spy saw: []`` and ``audit hook saw: socket.__new__``; ``socket.getaddrinfo``
produced ``spy saw: []`` and ``audit hook saw: socket.getaddrinfo``. So
monkeypatching answers neither the C path nor DNS, and DNS is exactly how the
textstat case fires. ``socket.setdefaulttimeout`` was rejected outright: it bounds
how long a connection may take and detects nothing, so a fetch from a fast host
succeeds under it and is reported as a pass.

THE HOOK BLOCKS AS WELL AS RECORDS, AND THAT IS NOT BELT AND BRACES. Raising from
the hook aborts the operation, so this gate can never itself perform the fetch it
is looking for -- which matters because the investigation that found the hole had
its FIRST offline probe silently contaminated: textstat downloaded the corpus
over the real network mid-probe and the probe then reported a pass. Recording
BEFORE raising is what covers the other direction: ``nltk.download`` and its kin
catch broadly, so a library that swallows the refusal and returns a fallback
still leaves the event on the record. :class:`NetworkReached` derives from
``BaseException`` for the same reason -- a bare ``except Exception`` in a
dependency must not be able to hide it.

WHERE IT RUNS, AND WHY NOT IN THE SUITE. This is a step of
``run_verifications.sh`` in its own subprocess, the same shape as steps 10, 11
and 11b. PEP 578 provides no way to REMOVE an audit hook: a hook installed from
``tests/conftest.py`` is installed for the whole session -- collection, teardown
and every test after -- and nothing can undo it. A dedicated process is what
bounds that. Two figures were measured before choosing, so the reasoning is not
assumed. Cost is NOT the reason: 3x4 body calls took 0.057 s with no hook
installed and 0.049 s with one dispatching 81,578 events, which is noise. And
pytest does not trip the rule: the whole suite run under a recording hook
dispatched 647,395 audit events and 0 transport events.

IT NEEDS NO NETWORK OF ITS OWN, AND THAT WAS MEASURED RATHER THAN REASONED. The
hook raises before the interpreter makes the call, so every control fires whether
or not an egress exists. Run inside an empty network namespace --
``unshare -rn .venv/bin/python -m tests.controls.network_reach`` -- this gate is
green with all six controls firing. The engine suite is meant to be reproducible
offline and this step keeps it that way, which also means it behaves identically
on a runner with egress and on one without.

THE ANTI-VACUITY GUARDS, in the shape ``.github/scripts/check-no-network.sh``
established and ``tests/controls/__init__.py`` describes:

  1. A FLOOR from ``.github/inventory.json``. Every implemented body is
     enumerated by ``stub_ledger`` -- the same walk ``engine.n_implemented`` is
     held to -- every one of them is RUN, and a body this gate could not run is a
     red line naming it, never a skip. The count run is then compared against
     ``engine.n_implemented`` and against 1: a run that exercised no body must not
     report success, and today four bodies exist, so that can never be vacuous.
  2. POSITIVE controls, three, which MUST be caught. See :data:`CONTROLS`.
  3. NEGATIVE controls, two, which MUST NOT be. A gate that fired on ordinary
     work would be turned off, and the file-reading negative is the one that
     stops this decaying into "no I/O at all" -- ``open`` raises an audit event
     too, and a wrapper handed a path is entitled to read it.

A CONTROL ANOTHER RULE CAN SATISFY IS NOT A CONTROL FOR THE RULE IT WAS WRITTEN
FOR. So the three positives fire through three DIFFERENT mechanisms and no two
are interchangeable:
:func:`opens_a_socket` constructs a socket and connects it to a numeric address,
raising ``socket.connect`` with no name to resolve; :func:`resolves_a_host` raises
``socket.getaddrinfo`` and constructs no socket at all; and
:func:`a_dependency_that_fetches` reaches the network through a THIRD-PARTY
PACKAGE, from code this repository does not own and no static walk over this
repository can read. Only the third is the hole this module was written for.

WHAT THIS GATE CANNOT SEE, NAMED RATHER THAN LEFT TO BE DISCOVERED. An audit hook
watches THIS interpreter. A body that spawns a child process has moved the
question somewhere this hook cannot follow, so process creation is recorded as
``OPAQUE`` and turns this red -- "not proven", which is the honest verdict, and
distinct from ``REACHED``, which is a finding. It is not a network rule and is not
counted as one. What remains genuinely uncovered is a socket opened by a C
extension that bypasses the interpreter's own socket module entirely; nothing
short of a network namespace answers that, and a namespace is a property of the
runner rather than of this suite.

    usage: python -m tests.controls.network_reach   (run from engine/)
"""

from __future__ import annotations

import functools
import pathlib
import socket
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from typing import Any

import nltk  # type: ignore[import-untyped]
import textstat  # type: ignore[import-untyped]

from tests.conformance.test_conformance import run_call
from tests.controls.double_run import (
    _label,
    _node_of,
    calls_by_node,
    implemented_methods,
    inventory,
)

#: Audit-event namespaces that mean a connection was opened, a host resolved or a
#: request sent. MATCHED BY PREFIX, not against a list of event names, so an event
#: a future CPython adds to one of these modules is caught without an edit here --
#: the namespace IS the rule. ``socket.gethostname`` and its kin are inside it
#: deliberately: a wrapper computes from what it was handed and has no business
#: calling any of them.
TRANSPORT = (
    "socket.", "urllib.", "ftplib.", "smtplib.", "imaplib.", "poplib.",
    "nntplib.", "telnetlib.", "http.client.",
)

#: Events that move the question into a process this hook cannot watch. Not a
#: network finding -- see the docstring above.
PROCESS = ("subprocess.", "os.exec", "os.posix_spawn", "os.spawn", "os.fork", "os.system")

#: Verdicts, and the whole vocabulary of them.
REACHED, OPAQUE, CLEAN = "reached", "opaque", "clean"


class NetworkReached(BaseException):
    """Raised from the audit hook, so the operation never happens.

    ``BaseException`` and not ``Exception``: ``nltk.download`` and libraries like
    it catch broadly, and a refusal a dependency can swallow would let this gate
    report a pass on a call it had just interrupted.
    """


#: ``None`` when disarmed. A list when armed, and the list IS the record.
_WATCH: list[tuple[str, str]] | None = None


def _observe(event: str, args: tuple[Any, ...]) -> None:
    """The audit hook. Disarmed, it returns before doing anything at all.

    Re-entrant by construction: rendering ``args`` re-enters this hook for the
    events that rendering raises, and every one of those falls through the two
    prefix tests and returns. Only a transport event raised while rendering a
    transport event could recurse, and rendering opens no sockets.
    """
    if _WATCH is None:
        return
    if event.startswith(TRANSPORT):
        kind = REACHED
    elif event.startswith(PROCESS):
        kind = OPAQUE
    else:
        return
    _WATCH.append((kind, f"{event}{args!r:.120}"))
    raise NetworkReached(event)


sys.addaudithook(_observe)


@contextmanager
def watching() -> Iterator[list[tuple[str, str]]]:
    """Arm the hook for the duration, and yield the record it writes."""
    global _WATCH
    if _WATCH is not None:
        raise RuntimeError("watching() is already armed; a nested record would be lost.")
    record: list[tuple[str, str]] = []
    _WATCH = record
    try:
        yield record
    finally:
        _WATCH = None


def verdict(record: list[tuple[str, str]]) -> str:
    """What a watched call amounts to. A transport event outranks an opaque one."""
    kinds = {kind for kind, _ in record}
    if REACHED in kinds:
        return REACHED
    if OPAQUE in kinds:
        return OPAQUE
    return CLEAN


def _say(message: str) -> None:
    """This module IS a gate; what it prints is its report."""
    print(message)  # noqa: T201


def opens_a_socket() -> None:
    """POSITIVE. Constructs a socket and connects it. No name is resolved.

    MEASURED: the hook aborts this at ``socket.__new__``, the first event the
    sequence raises, so ``socket.connect`` is never reached and no packet could
    leave. The address is in TEST-NET-1 (RFC 5737), which is never routed, so the
    call is harmless even with the hook removed -- which is how the HOLE branch
    can be exercised without touching a real host.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(0.05)
        sock.connect(("192.0.2.1", 9))


def resolves_a_host() -> None:
    """POSITIVE. DNS alone: no socket object is ever constructed.

    This is the shape a monkeypatch of ``socket.socket`` cannot see, and the shape
    the textstat case actually fires in -- the first event that fetch raises is
    ``socket.getaddrinfo``, not ``socket.connect``. ``.invalid`` is reserved by
    RFC 2606.
    """
    socket.getaddrinfo("econflow.invalid", 80)


def a_dependency_that_fetches() -> None:
    """POSITIVE. THE REAL CASE: a third-party call that fetches at call time.

    ``textstat.flesch_reading_ease`` asks nltk for the cmudict corpus and, on a
    cache miss, downloads it from ``raw.githubusercontent.com``. Nothing in this
    repository's source names a transport, so the static gate beside this one
    reports the module clean; this control is the demonstration that the runtime
    gate does not.

    ASSERTED BY CONSTRUCTION, AND SAID PLAINLY: no wrapper body imports textstat
    today, so this is a planted caller and not an existing one. textstat is named
    because it is the MEASURED instance of the hole rather than an illustration of
    it. If the dependency is ever dropped, replace this control with the next
    dependency that fetches at call time -- do not delete it.

    THE CACHE IS FORCED ABSENT, which is what makes this fire on EVERY machine
    rather than only on one that has never run textstat. ``nltk.data.path`` is
    pointed at an empty directory for the duration and the miss is asserted rather
    than assumed. MEASURED with a decoy corpus planted at
    ``~/nltk_data/corpora/cmudict``: the forced path misses it, and
    ``nltk.download`` then reaches for its remote index before consulting anything
    local, so the control still fired on ``socket.getaddrinfo
    ('raw.githubusercontent.com', None, 0, 0, 6)``. A poisoned home directory
    therefore cannot silently disarm it.

    WHAT FORCING THE PATH DOES NOT DO, MEASURED, because the obvious reading is
    wrong. It redirects the LOOKUP and not the WRITE:
    ``nltk.downloader._downloader`` is a module singleton whose ``download_dir``
    is resolved when ``nltk`` is imported, so it still reads ``~/nltk_data`` after
    the path is replaced, while a freshly computed ``default_download_dir()``
    returns the temp directory. A first version of this control asserted the temp
    directory was empty afterwards and would have passed over a real download into
    the home directory -- which happened, once, while this was being written.

    WHAT ACTUALLY GUARANTEES THIS GATE FETCHES NOTHING is structural and is not an
    assertion here: the hook raises at ``socket.getaddrinfo``, the first event the
    attempt makes, before a connection exists. If the hook ever stops blocking,
    the download succeeds, no transport event is recorded, and this control is
    reported as a HOLE -- so the gate turns red on the run that contaminated it.

    ONCE PER PROCESS, AND :func:`check_controls` CALLS IT ONCE. textstat memoises
    ``get_cmudict`` with an ``lru_cache``, which does not cache the refusal -- so a
    blocked call still fires on the next attempt. What the cache DOES hide is a
    corpus that was fetched successfully earlier in the same interpreter, and that
    is how the probe which found this hole silently disarmed itself: an earlier
    unblocked call downloaded cmudict, and every later call in that process read
    the cache and reported clean.
    """
    with tempfile.TemporaryDirectory(prefix="econflow-nltk-empty-") as empty:
        nltk.data.path[:] = [empty]
        try:
            found = nltk.data.find("corpora/cmudict")
        except LookupError:
            pass
        else:
            raise AssertionError(
                f"the cmudict corpus is reachable at {found} despite nltk.data.path "
                f"being forced to the empty {empty}; this control cannot fire and is "
                "therefore not a control."
            )
        textstat.flesch_reading_ease("The quick brown fox jumps over the lazy dog.")


def computes_from_its_inputs() -> None:
    """NEGATIVE. What every correct body does, and it must not be flagged.

    THE WEAKER OF THE TWO NEGATIVES, AND SAID SO. Measured with the rule widened
    to match EVERY audit event: this control was still reported clean, because
    arithmetic over a tuple of floats raises no audit event at all, while
    :func:`reads_a_committed_file` was correctly flagged. So the decay guard is
    carried by that one; this is the shape of an ordinary body, kept because that
    is the thing the rule must never refuse.
    """
    values = (0.31, 0.47, 0.12, 0.88, 0.55)
    mean = sum(values) / len(values)
    spread = sum((v - mean) ** 2 for v in values) / (len(values) - 1)
    if not spread > 0:
        raise AssertionError("the negative control computed nothing.")


def reads_a_committed_file() -> None:
    """NEGATIVE. Local file access, which raises audit events of its own.

    ``open`` is an audited event, so a rule written as "any audit event" or as "no
    I/O" would flag this. A wrapper handed a path is entitled to read it, and 19
    nodes take a required ``path``; a gate that refused them would be turned off.
    """
    manifest = pathlib.Path(__file__).resolve().parents[2] / "pyproject.toml"
    if not manifest.read_bytes():
        raise AssertionError(f"{manifest} is empty; the negative control read nothing.")


def spawns_a_process() -> None:
    """OPAQUE. A child's sockets are outside this interpreter, so this hook is blind.

    Recorded as unproven rather than as a finding. The hook aborts at
    ``subprocess.Popen``, so no child is created -- measured: the child's only job
    was to create a file, and the file does not exist afterwards.
    """
    subprocess.run([sys.executable, "-c", "pass"], check=True)


#: The planted set, as ``(name, callable, expected_verdict)``.
#:
#: Every entry's verdict is asserted individually rather than counted: a positive
#: that goes unflagged means this harness cannot detect a fetch at all, and a
#: negative that gets flagged means it has decayed into a rule that refuses
#: correct code. Those are different defects and are reported separately.
CONTROLS: tuple[tuple[str, Callable[[], None], str], ...] = (
    ("opens_a_socket", opens_a_socket, REACHED),
    ("resolves_a_host", resolves_a_host, REACHED),
    ("a_dependency_that_fetches", a_dependency_that_fetches, REACHED),
    ("computes_from_its_inputs", computes_from_its_inputs, CLEAN),
    ("reads_a_committed_file", reads_a_committed_file, CLEAN),
    ("spawns_a_process", spawns_a_process, OPAQUE),
)


def _watch(call: Callable[[], object]) -> tuple[str, list[tuple[str, str]], str, object]:
    """Run one callable under the armed hook. Verdict, record, note and result.

    A call the hook aborted is expected and is not an error. Any OTHER exception
    is reported in the note, because a control or a body that fell over before it
    could reach anything has not been observed doing nothing -- it has not been
    observed at all.
    """
    result: object = None
    with watching() as record:
        try:
            result = call()
        except NetworkReached:
            note = ""
        except Exception as exc:  # noqa: BLE001 - reported as a red line, never swallowed
            note = f"{type(exc).__name__}: {exc}"
        else:
            note = ""
    return verdict(record), record, note, result


def check_controls() -> int:
    """Run every planted control and assert its verdict. Returns the count, or 0.

    THE THREE FAILURES ARE DIFFERENT DEFECTS and are reported separately and in
    full, never one short-circuiting the next: a control that must be caught and
    was not means this harness cannot see a fetch at all; a control that must not
    be caught and was means the rule has decayed into one that refuses correct
    code; and a control that raised means its verdict was never taken.

    A CONTROL THAT MUST BE CAUGHT AND RAISED INSTEAD IS A HOLE, NOT A BREAKAGE.
    Measured with the hook's prefix list emptied: :func:`opens_a_socket` reached a
    real ``TimeoutError`` and :func:`resolves_a_host` a real ``gaierror``, because
    with nothing blocking them the calls simply proceed. Filing those as "the
    control did not run" would report the gate's own hole as a broken control.
    """
    holes: list[str] = []
    false_alarms: list[str] = []
    broken: list[str] = []
    for name, call, expected in CONTROLS:
        seen, record, note, _ = _watch(call)
        events = ", ".join(detail for _, detail in record) or "no audited event"
        because = f" -- the call itself raised {note}" if note else ""
        if seen == expected:
            if note:
                broken.append(f"BROKEN       {name}: {note}")
        elif expected == CLEAN:
            false_alarms.append(f"FALSE ALARM  {name}: flagged {seen} on {events}")
        else:
            holes.append(
                f"HOLE         {name}: expected {expected}, saw {seen} on "
                f"{events}{because}"
            )

    if holes:
        _report(
            holes,
            f"FAIL: {len(holes)} control(s) that MUST be caught were not. This harness "
            "cannot see a body reach the network, so a green run means nothing -- and "
            "if a_dependency_that_fetches is among them, the corpus was DOWNLOADED "
            "rather than refused and this run reached the network itself.",
        )
    if false_alarms:
        _report(
            false_alarms,
            f"FAIL: {len(false_alarms)} control(s) that must NOT be caught were flagged. "
            "Arithmetic and reading a committed file are not network access; a gate "
            "that refuses them is unusable and would be turned off.",
        )
    if broken:
        _report(broken, "FAIL: a planted control raised, so its verdict was never taken.")
    if holes or false_alarms or broken:
        return 0
    return len(CONTROLS)


def _report(detail: list[str], message: str) -> None:
    """Print the offending rows, then the reason."""
    for row in detail:
        _say(row)
    if detail:
        _say("")
    print(message, file=sys.stderr)  # noqa: T201


def check_methods() -> int:
    """Run every implemented body under the hook and refuse to skip any. -1 on failure.

    A CALL THAT DID NOT SUCCEED IS UNRUN, NOT CLEAN, and that distinction is the
    difference between this gate proving something and proving nothing.
    ``run_call`` turns a stub's ``NotImplementedError`` and a body's ``GateError``
    into a STATE rather than an exception, so a body whose arguments the wire
    contract refuses returns quietly, raises no audit event, and would otherwise
    be counted as a body observed reaching nothing. It was never entered.
    ``tests/controls/double_run.py`` refuses the same shape for its own reason.
    """
    methods = list(implemented_methods())
    calls, _ = calls_by_node()
    reached: list[str] = []
    opaque: list[str] = []
    unrun: list[str] = []
    for path, name in methods:
        label = _label(path, name)
        case = calls.get(_node_of(path, name))
        if case is None:
            unrun.append(
                f"UNRUN    {label}: no oracle case and no payload file, so this gate "
                "never ran it; tests/controls/double_run.py names the reason"
            )
            continue
        seen, record, note, result = _watch(functools.partial(run_call, case))
        events = "; ".join(detail for _, detail in record)
        state = result[0] if isinstance(result, tuple) and result else "returned nothing"
        if seen == REACHED:
            reached.append(f"REACHED  {label}: {events}")
        elif seen == OPAQUE:
            opaque.append(f"OPAQUE   {label}: {events}")
        elif note:
            unrun.append(f"UNRUN    {label}: its call raised -- {note}")
        elif state != "succeeded":
            unrun.append(f"UNRUN    {label}: its call {state}, so the body was not entered")

    if reached:
        _report(
            reached,
            f"FAIL: {len(reached)} wrapper body/bodies opened a connection while "
            "running. The source may name no transport -- a dependency reaching the "
            "network at call time is exactly the case this gate exists for. Fetching "
            "belongs to the external-data node, which lives outside the wrapper set "
            "so that the rule can stay absolute here.",
        )
        return -1
    if opaque:
        _report(
            opaque,
            f"FAIL: {len(opaque)} wrapper body/bodies created a child process. This "
            "hook watches THIS interpreter, so the child's sockets are unobservable "
            "and the gate reports 'not proven' rather than 'proven'.",
        )
        return -1
    if unrun:
        _report(
            unrun,
            f"FAIL: {len(unrun)} implemented method(s) were enumerated and NOT run "
            "under the hook. A harness that skipped them and printed 'no connection "
            "opened' would have examined nothing, which is the defect this whole "
            "package exists to refuse.",
        )
        return -1
    return len(methods)


def main() -> int:
    """Run the controls and every implemented body; assert both counts."""
    controls_run = check_controls()
    if controls_run == 0:
        return 1

    methods_run = check_methods()
    if methods_run < 0:
        return 1

    floor = inventory("engine", "n_implemented")
    if methods_run < max(floor, 1):
        _report(
            [],
            f"FAIL: ran {methods_run} wrapper body/bodies under the hook, below the "
            f"floor {max(floor, 1)} (engine.n_implemented is {floor}). The walk is "
            "wrong, not the tree -- and a run that exercised no body has not passed.",
        )
        return 1

    expected = {name: kind for name, _, kind in CONTROLS}
    _say(
        f"ok: {methods_run} wrapper body/bodies and {controls_run} planted control(s) "
        f"run under a PEP 578 audit hook; no transport event observed "
        f"(floor {floor}, "
        f"{sum(1 for k in expected.values() if k == REACHED)} must be caught / "
        f"{sum(1 for k in expected.values() if k == CLEAN)} must not / "
        f"{sum(1 for k in expected.values() if k == OPAQUE)} opaque, all fired)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
