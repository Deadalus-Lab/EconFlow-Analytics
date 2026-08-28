# SPDX-License-Identifier: AGPL-3.0-only
"""The method leg of box 2.1.14, proven on planted bodies rather than on none.

WHY THIS SUITE EXISTS. ``tests/controls/double_run.py`` grew the code that
resolves an implemented method to a call and double-runs it. With zero bodies in
the tree that code runs ZERO times, so the gate prints "0 method(s) ... ok" and
every line of the new path is unexercised -- a harness that examined nothing
reporting success, which is the one shape ARCHITECTURE.md 11.1 refuses and which
this tree has hit six times. The controls below are what make the method leg mean
something before the first real body arrives to use it.

HOW A BODY IS PLANTED. A HARDLINK MIRROR of ``engine/``, the same device
``tests/test_payload_sentinel.py`` uses and for the same reasons: hardlinks make
the copy cheap and leave every count identical, where a symlinked tree would not
be walked by ``rglob`` at all. EVERY write into the mirror goes through
``_write``, which UNLINKS its target first: ``write_text`` truncates IN PLACE, so
writing through a hardlink would edit the repository itself. One helper holds
that invariant rather than each call site restating it, so a write added here
later cannot reintroduce the defect. The mirror carries its own
``.github/inventory.json`` beside an ``engine/`` directory, which is what
``find_repo_root`` requires and what makes the gate read the planted manifest
instead of the real one.

WHY THE PLANTED NODES TAKE NO HANDLE. These controls answer for the PAYLOAD
mechanism -- does a committed call reach an implemented body, and are its two runs
compared -- not for the fixture mechanism, which ``tests/conformance`` already
proves on its own controls. A node whose required arguments are all literal kinds
isolates the first question from the second, so a failure here names the payload
path rather than something three layers down.

WHAT THE NEGATIVE CONTROLS COVER, AND WHY EACH ONE EXISTS SEPARATELY. Every one
of them was watched failing against the gate with the guard it names removed,
which is the only evidence that it guards anything. A body with no call at all; a
body whose arguments the wire contract refuses, which reproduces its own refusal
byte for byte and would otherwise be counted as a double run; a body whose second
run does not succeed, where the digests agree and only the message says so; a
body whose payload is a ``to_mcp`` refusal record, where the digest is a class
name; a body that raises something the gateway does not convert into a state,
which used to end the process and hide every later method; a public function that
is not a node, and one whose name collides with another module's node; a payload
naming a dataset the tree does not hold; two payloads naming one node; and a
payload for a body nobody wrote.

THIS SUITE IS NAMED FOR THE LEG IT TESTS, NOT FOR PAYLOAD FILES. It was
``test_invocation_payloads.py`` first, which read as though it covered the file
format alone; half of what it covers has no payload file in it at all, because an
admissible oracle case reaches a body just as well. No inventory constant names
the file -- ``engine.test_files`` counts ``test_*.py`` and does not move.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from econflow_engine.metrics import find_repo_root
from tests.support import ENGINE_ROOT, INVENTORY

REPO_ROOT = find_repo_root(Path(__file__))

#: A node with an admissible oracle case, so the ORACLE half of the union is
#: exercised by a body alone, with no payload file written for it.
FN_WITH_AN_ORACLE_CASE = "rs_multiple_testing"

#: A node whose required argument set is empty and which has no oracle case, so a
#: payload FILE is the only thing that can reach it.
FN_WITHOUT_AN_ORACLE_CASE = "hd_list"


def _write(path: Path, text: str) -> None:
    """The ONLY way this suite writes into the mirror: unlink first, then write.

    Every pre-existing file in the mirror is a hardlink to the repository's own
    inode, and ``write_text`` opens with ``O_TRUNC`` and writes in place rather
    than replacing the file, so a write that skipped the unlink would edit the
    repository.
    """
    path.unlink(missing_ok=True)
    path.write_text(text, encoding="utf-8")


def _mirror(tmp_path: Path) -> Path:
    """A writable hardlink mirror of engine/, under a root the gate can resolve.

    The manifest is written UNCHANGED here rather than only where a test moves a
    constant: ``find_repo_root`` needs it beside an ``engine/`` directory to
    resolve the root at all, so a mirror without one cannot start the gate, and
    the resting control below would then be measuring the absence of a file.
    """
    root = tmp_path / "root"
    (root / ".github").mkdir(parents=True)
    engine = root / "engine"
    shutil.copytree(
        ENGINE_ROOT,
        engine,
        copy_function=os.link,
        ignore=shutil.ignore_patterns("__pycache__", "mutants", ".venv", ".omc"),
    )
    _manifest(engine)
    return engine


def _manifest(engine: Path, **engine_overrides: object) -> None:
    """Write the real manifest into the mirror with named constants moved."""
    data = json.loads(INVENTORY.read_text(encoding="utf-8"))
    data["engine"].update(engine_overrides)
    _write(engine.parent / ".github" / "inventory.json", json.dumps(data, indent=2))


def _implemented(planted: int = 0) -> int:
    """The COMMITTED tree's body count plus the bodies a test plants on top of it.

    READ, NEVER WRITTEN DOWN. The mirror is a hardlink copy of the real tree, so
    every plant below is the committed figure plus its own plants. The literal
    ``1`` that used to stand at each of these call sites was the committed 0 plus
    one plant, and it stopped being right the moment phase 2.2 landed its first
    body -- a re-edit of this file that ``double_run.py``'s own docstring says
    should not be needed ("it is 0 == 0 today and rises on its own with the first
    body written in 2.2 -- no second edit to this file"). It is read here so that
    the second body, and the six-hundredth, need none either.
    """
    manifest = json.loads(INVENTORY.read_text(encoding="utf-8"))
    return int(manifest["engine"]["n_implemented"]) + planted


def _module_of(engine: Path, fn: str) -> Path:
    """The wrapper module declaring ``fn``, found by its DEFINITION.

    Matched on ``def <fn>(`` rather than on the emitted stub raise, because
    ``_plant`` removes that raise: a helper keyed on it would find the module
    before planting and fail to find it afterwards.
    """
    needle = f"\ndef {fn}("
    for path in sorted((engine / "src" / "econflow_engine" / "wrappers").rglob("*.py")):
        if path.name != "__init__.py" and needle in path.read_text(encoding="utf-8"):
            return path
    raise AssertionError(f"no wrapper module defines {fn}")


def _plant(engine: Path, fn: str, body: str) -> None:
    """Give exactly one function a body, replacing the emitted raise with ``body``.

    The catalogue size does not move: one function stops being a stub and no
    function is added or removed, so the implemented count rises by one and the
    stub count falls by one.
    """
    path = _module_of(engine, fn)
    text = path.read_text(encoding="utf-8")
    stub = f'    raise NotImplementedError(\n        "{fn}: not implemented."\n    )'
    assert stub in text, f"{fn} does not carry the emitted stub raise verbatim"
    _write(path, text.replace(stub, body, 1))


def _append_public_function(engine: Path, beside: str, name: str) -> None:
    """Add a PUBLIC function to the wrapper module declaring ``beside``.

    This is the move the gate has to survive and cannot survive today by luck:
    ``stub_ledger`` counts every public function in a wrapper module, so an
    author who writes a helper without the leading underscore adds one to the
    implemented count while adding nothing the manifest knows about.
    """
    path = _module_of(engine, beside)
    body = (
        f'\n\ndef {name}(value: int) -> int:\n'
        f'    """A public helper an author wrote beside a body."""\n'
        f"    return value\n"
    )
    _write(path, path.read_text(encoding="utf-8") + body)


def _payload(
    engine: Path,
    fn: str,
    inputs: dict[str, object],
    stem: str = "",
    extra: dict[str, object] | None = None,
) -> Path:
    """Write one payload file under the module the node belongs to.

    ``stem`` names the FILE rather than the node, so the duplicate control below
    can file two payloads for one ``fn`` -- which is the state the gate has to
    refuse and which a filename derived from ``fn`` alone cannot produce.
    ``extra`` is a mapping rather than ``**kwargs`` because a caller splatting a
    mapping into ``**kwargs`` can silently bind ``stem`` instead of adding a key.
    """
    module = _module_of(engine, fn)
    directory = engine / "tests" / "payloads" / module.parent.name / module.stem
    directory.mkdir(parents=True, exist_ok=True)
    record: dict[str, object] = {
        "fn": fn,
        "inputs": inputs,
        "notes": "planted control: the arguments are the point, not the result.",
    }
    record.update(extra or {})
    path = directory / f"{stem or fn}.json"
    _write(path, json.dumps(record, indent=2))
    return path


def _run(engine: Path) -> subprocess.CompletedProcess[str]:
    """Run the real gate against the mirror, never a second copy of its logic."""
    env = dict(os.environ)
    env["PYTHONPATH"] = str(engine / "src")
    env.pop("VIRTUAL_ENV", None)
    return subprocess.run(
        [sys.executable, "-m", "tests.controls.double_run"],
        cwd=engine,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


CONSTANT_BODY = '    return {"value": 1}'
NONDETERMINISTIC_BODY = "    import time\n\n    return {'clock': time.time()}"

#: Returns an object ``to_mcp`` cannot serialise. A NEW object on every call, so
#: the two runs share nothing but the stub record -- which is exactly why they
#: hash equal, and why the gate must refuse the payload rather than compare it.
FOREIGN_OBJECT_BODY = "    return object()"

def _raising_body(message: str) -> str:
    """A body that raises what the gateway does NOT convert into a state.

    ``run_method`` catches ``NotImplementedError`` and ``make_tool`` catches
    ``GateError``; a bare ``ValueError`` reaches the gate's own loop, which is
    where it was measured ending the process.
    """
    return f'    raise ValueError("{message}")'


#: Succeeds once, then refuses. ``GateError`` is what ``make_tool`` converts into
#: a refusal, so the second run reports state ``refused`` through the production
#: path rather than as an exception. The flag lives on the function object
#: because both runs share one process.
SECOND_RUN_REFUSED_BODY = (
    "    from econflow_engine.errors import GateError\n"
    "\n"
    '    if getattr(hd_list, "_already_ran", False):\n'
    '        raise GateError("other", "hd_list: refused on the second call.")\n'
    '    hd_list._already_ran = True\n'
    '    return {"value": 1}'
)


def test_the_resting_mirror_reproduces_the_real_green_run(tmp_path: Path) -> None:
    """POSITIVE. The mirror itself is not the variable: untouched, it is green.

    Without this, every red below could be the mirror rather than the plant.
    """
    engine = _mirror(tmp_path)

    result = _run(engine)

    assert result.returncode == 0, result.stdout + result.stderr
    assert f"{_implemented()} method(s)" in result.stdout, result.stdout


def test_a_write_into_the_mirror_leaves_the_file_it_is_linked_to_alone(tmp_path: Path) -> None:
    """CONTROL over the apparatus. An invariant nothing measures is a comment.

    ``engine/tests/payloads/`` does not exist yet, so the condition is BUILT here
    rather than waited for: a file outside the mirror, linked in at the path
    ``_payload`` writes to, is what ``_mirror`` produces of its own accord the day
    a payload for this node is committed.
    """
    engine = _mirror(tmp_path)
    committed = tmp_path / "committed.json"
    original = '{"fn": "the committed payload this suite must never edit"}\n'
    committed.write_text(original, encoding="utf-8")
    linked = _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    linked.unlink()
    os.link(committed, linked)

    written = _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})

    assert committed.read_text(encoding="utf-8") == original
    assert json.loads(written.read_text(encoding="utf-8"))["fn"] == FN_WITHOUT_AN_ORACLE_CASE


def test_a_body_reached_by_its_oracle_case_is_double_run(tmp_path: Path) -> None:
    """POSITIVE. An oracle case IS a payload: a body with one needs no second file."""
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITH_AN_ORACLE_CASE, CONSTANT_BODY)
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 0, result.stdout + result.stderr
    assert f"{_implemented(1)} method(s)" in result.stdout, result.stdout


def test_a_body_reached_by_a_payload_file_is_double_run(tmp_path: Path) -> None:
    """POSITIVE. A body nobody tabulated is reached by its hand-authored payload."""
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 0, result.stdout + result.stderr
    assert f"{_implemented(1)} method(s)" in result.stdout, result.stdout


def test_a_body_with_no_call_at_all_is_named_and_refused(tmp_path: Path) -> None:
    """NEGATIVE. The skip this gate exists to prevent, and the method is NAMED.

    A harness that enumerated this body, found nothing to run it with and printed
    "all match" is the defect box 2.1.14 was written against.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "UNRUN" in result.stdout, result.stdout
    assert FN_WITHOUT_AN_ORACLE_CASE in result.stdout, result.stdout


def test_a_nondeterministic_body_is_caught(tmp_path: Path) -> None:
    """NEGATIVE. Two runs of one call must be compared, not merely performed.

    This is the assertion that makes the positive controls mean something: a
    harness that ran a body twice and never compared the bytes would pass every
    test above and fail this one.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, NONDETERMINISTIC_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "MOVED" in result.stdout, result.stdout


def test_a_payload_filed_under_the_wrong_module_is_refused(tmp_path: Path) -> None:
    """NEGATIVE. The directory names the node, so a payload cannot certify itself.

    ``load_payload`` reads ``namespace`` and ``module`` from the PATH; without a
    check against the node ``fn`` names, a misfiled payload simply runs and the
    directory means nothing.
    """
    engine = _mirror(tmp_path)
    path = _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    misfiled = path.parent.parent / "not_the_owning_module" / path.name
    misfiled.parent.mkdir()
    _write(misfiled, path.read_text(encoding="utf-8"))
    path.unlink()

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "not_the_owning_module" in result.stderr, result.stdout + result.stderr


def test_a_payload_filed_under_the_engine_namespace_is_refused(tmp_path: Path) -> None:
    """NEGATIVE. That namespace binds by ``getattr``, which is not a wrapper call.

    A payload under ``engine/`` takes the engine-helper branch of ``_run_case``:
    it reaches ``econflow_engine.<module>.<fn>`` past the gateway, the MANIFEST
    membership check and the ``__all__`` restriction the oracle loader applies.
    """
    engine = _mirror(tmp_path)
    path = _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    misfiled = engine / "tests" / "payloads" / "engine" / "metrics" / path.name
    misfiled.parent.mkdir(parents=True)
    _write(misfiled, path.read_text(encoding="utf-8"))
    path.unlink()

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "filed under 'engine/'" in result.stderr, result.stdout + result.stderr


@pytest.mark.parametrize(
    ("extra", "dropped"),
    [({"expected": 1.0}, None), ({}, "notes")],
    ids=["an-extra-key", "a-missing-key"],
)
def test_a_payload_that_is_not_one_is_refused(
    tmp_path: Path, extra: dict[str, object], dropped: str | None
) -> None:
    """NEGATIVE. The key set is closed in BOTH directions.

    An ``expected`` would be an oracle case filed where nothing checks its
    citation; a missing ``notes`` would be a choice of arguments with no record of
    why those arguments exercise this body, which is the whole content of the
    choice.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    path = _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {}, extra=extra)
    if dropped is not None:
        record = json.loads(path.read_text(encoding="utf-8"))
        del record[dropped]
        _write(path, json.dumps(record, indent=2))
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode != 0, result.stdout + result.stderr
    assert "expected exactly" in result.stdout + result.stderr, result.stdout + result.stderr


def test_a_body_whose_call_the_wire_contract_refuses_is_named_and_refused(
    tmp_path: Path,
) -> None:
    """NEGATIVE. A REFUSAL REPRODUCES PERFECTLY, and that is the whole danger.

    The body never executes: the wire contract rejects the arguments before it is
    reached, both runs return the same refusal message, and their digests agree.
    Without the guard this pins, the gate reports the method as double-run and
    exits 0 -- a body that refuses every input would satisfy box 2.1.14.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {"bogus": 1})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "UNRUN" in result.stdout, result.stdout
    assert FN_WITHOUT_AN_ORACLE_CASE in result.stdout, result.stdout
    assert "refused" in result.stdout, result.stdout


def test_a_body_whose_second_run_does_not_succeed_says_so(tmp_path: Path) -> None:
    """NEGATIVE, AND IT PINS THE MESSAGE RATHER THAN THE EXIT CODE.

    Run 1 succeeds and run 2 is refused, so the two digests differ and the gate
    exits 1 either way. What the guard buys is a line that says WHICH run failed:
    fold the second state into the digest comparison and the report becomes two
    unequal hashes with nothing to act on, and where a refusal happens to encode
    to the same bytes as the payload it would read "MOVED x != x".
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, SECOND_RUN_REFUSED_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "MOVED" in result.stdout, result.stdout
    assert "run 2 refused" in result.stdout, result.stdout
    assert FN_WITHOUT_AN_ORACLE_CASE in result.stdout, result.stdout


def test_a_body_whose_payload_cannot_be_serialised_is_not_counted_as_proven(
    tmp_path: Path,
) -> None:
    """NEGATIVE. A DIGEST OVER A CLASS NAME IS NOT A DIGEST OVER A RESULT.

    ``to_mcp`` stubs any object it cannot serialise into a record carrying the
    class name and a length, so a body returning a NEW object on every call hashes
    identically on both runs. 320 of the 1456 nodes register an object, and
    ``_run_case`` discards the handle, so this is the shape most registering
    bodies will arrive in. The gate must say "not proven", not "proven".
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, FOREIGN_OBJECT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "UNRUN" in result.stdout, result.stdout
    assert "['object']" in result.stdout, result.stdout
    assert FN_WITHOUT_AN_ORACLE_CASE in result.stdout, result.stdout


def test_a_raising_body_is_reported_and_the_loop_reaches_the_next_method(
    tmp_path: Path,
) -> None:
    """NEGATIVE. ONE CRASHING BODY MUST NOT HIDE EVERY METHOD BEHIND IT.

    Measured before the fix: a planted ``raise ValueError`` produced a raw
    traceback, no red line naming the method, and a loop that never reached the
    remaining ones. Two bodies are planted here for exactly that reason -- if the
    first still ends the process, the second is never named, which is the
    assertion below rather than a description of it.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, _raising_body("boom-one"))
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _plant(engine, FN_WITH_AN_ORACLE_CASE, _raising_body("boom-two"))
    _manifest(engine, n_implemented=_implemented(2))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "Traceback" not in result.stderr, result.stderr
    assert "boom-one" in result.stdout, result.stdout
    assert "boom-two" in result.stdout, result.stdout
    assert result.stdout.count("UNRUN") == 2, result.stdout


def test_a_public_function_that_is_not_a_node_is_named_and_refused(
    tmp_path: Path,
) -> None:
    """NEGATIVE. THE ADVICE HAS TO BE FOLLOWABLE, AND "land its payload" IS NOT.

    ``stub_ledger`` counts every public function in a wrapper module, so the first
    2.2 author who writes a helper without a leading underscore turns this gate
    permanently red. A helper has no wire contract and no manifest entry: no
    payload can ever reach it, and the fix is the rename.
    """
    engine = _mirror(tmp_path)
    _append_public_function(engine, FN_WITHOUT_AN_ORACLE_CASE, "helper_beside_a_body")
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "NOT A NODE" in result.stdout, result.stdout
    assert "helper_beside_a_body" in result.stdout, result.stdout
    assert "leading underscore" in result.stderr.lower(), result.stderr


def test_a_public_function_colliding_with_another_module_s_node_is_refused(
    tmp_path: Path,
) -> None:
    """NEGATIVE, AND THE DANGEROUS HALF OF THE ONE ABOVE.

    A helper whose name matches another module's node HAS a call in the tree --
    just not its own. Keyed on the bare function name, the gate resolves the
    impostor to that node's payload, runs THAT node twice and reports two
    double-run methods while the helper's own code never executes: measured, the
    exact tree planted here goes GREEN with the intersection removed. The real
    node is implemented too, because that is what makes the impostor's borrowed
    call succeed and the vacuous green possible.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _append_public_function(engine, FN_WITH_AN_ORACLE_CASE, FN_WITHOUT_AN_ORACLE_CASE)
    _manifest(engine, n_implemented=_implemented(2))

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "NOT A NODE" in result.stdout, result.stdout
    assert "belongs to c00_data_utilities" in result.stdout, result.stdout


def test_a_payload_naming_a_dataset_the_tree_does_not_hold_is_refused(
    tmp_path: Path,
) -> None:
    """NEGATIVE. A MISSING FIXTURE IS A REFUSAL AT LOAD TIME, NOT A RUN THAT DIED.

    ``_load_case`` resolves every value form when a case is loaded, which is what
    turns a ``FixtureError`` into a refusal naming the FILE that carries the bad
    reference. A payload that skipped that step raised the error out of the first
    run: originally as a bare traceback, and -- once the loop learned to catch a
    raising body -- as a red line naming the wrapper module and the dataset but
    never the payload file the author has to open. The file name is what this
    pins, because it is the part only the load-time check can supply.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {"pattern": {"$fixture": "no_such_dataset"}})
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)
    reported = result.stdout + result.stderr

    assert result.returncode != 0, reported
    assert "Traceback" not in result.stderr, result.stderr
    assert "no_such_dataset" in reported, reported
    assert f"{FN_WITHOUT_AN_ORACLE_CASE}.json" in reported, reported


def test_two_payloads_naming_one_node_are_refused(tmp_path: Path) -> None:
    """NEGATIVE. THE SECOND WOULD REPLACE THE FIRST AND NOTHING WOULD SAY SO.

    Both files are read, both are valid, and the mapping keeps whichever sorts
    last -- so one of two reviewed calls is silently never made. Both names are
    printed, because choosing which to keep is the author's decision.
    """
    engine = _mirror(tmp_path)
    _plant(engine, FN_WITHOUT_AN_ORACLE_CASE, CONSTANT_BODY)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {}, stem="a_second_file")
    _manifest(engine, n_implemented=_implemented(1))

    result = _run(engine)

    assert result.returncode != 0, result.stdout + result.stderr
    assert "both name" in result.stderr, result.stderr
    assert "a_second_file.json" in result.stderr, result.stderr
    assert f"{FN_WITHOUT_AN_ORACLE_CASE}.json" in result.stderr, result.stderr


def test_a_payload_for_a_body_nobody_wrote_is_refused(tmp_path: Path) -> None:
    """NEGATIVE. A PAYLOAD THAT RUNS NOTHING STILL RAISES THE COUNT.

    The contract is that a payload lands in the same commit as the body it runs.
    An orphan is loaded, validated and never called, while
    ``engine.invocation_payloads`` counts it -- a constant reporting a call this
    gate does not make.
    """
    engine = _mirror(tmp_path)
    _payload(engine, FN_WITHOUT_AN_ORACLE_CASE, {})

    result = _run(engine)

    assert result.returncode == 1, result.stdout + result.stderr
    assert "ORPHAN" in result.stdout, result.stdout
    assert FN_WITHOUT_AN_ORACLE_CASE in result.stdout, result.stdout
