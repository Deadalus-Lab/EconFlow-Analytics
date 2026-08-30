# SPDX-License-Identifier: AGPL-3.0-only
"""Every wrapper signature resolves at CALL time, not only for a type checker.

THE DEFECT THIS EXISTS FOR IS INVISIBLE TO EVERY STATIC GATE IN THIS REPOSITORY.
``tests/conftest.py`` installs ``beartype.claw`` over ``econflow_engine``, and
beartype resolves a signature's annotations on EVERY CALL. While the wrapper
generator emitted ``import pandas as pd`` under ``if TYPE_CHECKING:``, the name
existed for mypy, pyright, ruff and ``gen_wrappers.py --check`` and did not exist
for the interpreter, so the first real call into such a module raised

    BeartypeCallHintForwardRefException: Forward reference "pd.Series"
    unimportable from unimportable module "pd".

MEASURED before the emitter was changed: 536 of the 598 wrapper modules name
``pd`` or ``np`` in a signature, and every one of them carried the
``TYPE_CHECKING`` block. The failure appears only when a body exists to be
called, which is why it survived the whole stub tier and why the proof below has
to be a real call rather than a comparison of text.

FOUR TESTS: TWO SWEEPS, AND TWO CONTROLS THAT ARE WHAT KEEP THE SWEEPS HONEST,
BECAUSE NEITHER CONTROL CAN DO THE OTHER'S JOB.

The first control plants a module in each header shape and calls both in ONE
SUBPROCESS: the pre-fix shape MUST be stopped at the annotation and the post-fix
shape MUST reach the body. That pins what beartype does with each shape, and
nothing more -- the subprocess installs its OWN hook over its OWN planted
package, so it is structurally blind to this session's. Comment out
``beartype_package("econflow_engine")`` in ``tests/conftest.py`` and it stays
green while the sweeps below have stopped reaching beartype at all.

The second control closes exactly that hole, IN THIS SESSION: it calls a real
wrapper with a deliberately wrong argument type and requires beartype's
parameter violation. Nothing else in this module can tell a live hook from a
dead one, because a stub raises ``NotImplementedError`` either way.
"""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from collections.abc import Iterator
from importlib import import_module
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import pytest
from beartype.roar import BeartypeCallHintParamViolation

from econflow_engine.metrics import find_manifest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
INVENTORY = find_manifest(Path(__file__))

#: The two names a wrapper signature carries that Python does not supply itself.
#: They are the only ones ``gen_wrappers.py`` emits an import for.
SIGNATURE_NAMES = ("pd", "np")

#: One value per handle annotation the generator emits. A call is attempted only
#: where EVERY required parameter is in this table: beartype checks the argument
#: as well as the annotation, and a wrong value would raise its parameter
#: violation instead of reaching the body -- a different verdict wearing the same
#: red.
#:
#: EVERY ONE OF THEM IS EMPTY, AND THAT IS THE SWEEP'S SAFETY ARGUMENT RATHER THAN
#: A DETAIL OF THE FIXTURE. ``test_every_stub_callable_from_handles_alone_reaches_
#: its_body`` requires a written body to REFUSE, and the only reason every body
#: must is that no method is defined over no observations. These carried three
#: rows until 2026-08-29, while the docstring below claimed they were empty: the
#: assertion held for ``ld_count_model`` only because it estimates four parameters
#: and 4 > 3, so a future body needing two parameters would have RETURNED a result
#: over three rows and turned the sweep red for being correct.
HANDLE_VALUES: dict[str, Any] = {
    "pd.Series": pd.Series([], dtype=float),
    "pd.DataFrame": pd.DataFrame({"a": pd.Series([], dtype=float)}),
    "np.ndarray": np.zeros(0),
}

# REUSE-IgnoreStart -- the SPDX lines below are written into a temporary file and
# declare nothing about this one. tests/test_stub_definition.py carries the same
# bracket and the measurement behind it.

#: The header the emitter used to write, and the defect itself.
_TYPE_CHECKING_ONLY = '''# SPDX-License-Identifier: AGPL-3.0-only
"""A planted wrapper module. Not part of the engine."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import pandas as pd


def planted_stub(*, y: pd.Series) -> dict[str, Any]:
    """A stub, in the shape gen_wrappers.py emits."""
    raise NotImplementedError("planted_stub: not implemented.")
'''

#: The header the emitter writes now.
_IMPORTED_AT_RUN_TIME = '''# SPDX-License-Identifier: AGPL-3.0-only
"""A planted wrapper module. Not part of the engine."""

from __future__ import annotations

from typing import Any

import pandas as pd


def planted_stub(*, y: pd.Series) -> dict[str, Any]:
    """A stub, in the shape gen_wrappers.py emits."""
    raise NotImplementedError("planted_stub: not implemented.")
'''
# REUSE-IgnoreEnd

#: Each planted shape, with the exception its call must raise.
PLANTED: dict[str, tuple[str, str]] = {
    "type_checking_only": (_TYPE_CHECKING_ONLY, "BeartypeCallHintForwardRefException"),
    "imported_at_run_time": (_IMPORTED_AT_RUN_TIME, "NotImplementedError"),
}

#: Run in a subprocess against the planted package; prints one line per shape.
_PLANTED_RUNNER = """
import importlib
import sys

import pandas as pd
from beartype.claw import beartype_package

sys.path.insert(0, sys.argv[1])
beartype_package("planted_wrappers")

for name in sys.argv[2:]:
    module = importlib.import_module(f"planted_wrappers.{name}")
    try:
        module.planted_stub(y=pd.Series([1.0]))
    except BaseException as exc:
        print(f"{name} {type(exc).__name__}")
    else:
        print(f"{name} RETURNED")
"""


def inventory(section: str, key: str) -> int:
    """One asserted constant, from the one file that holds them all."""
    return int(json.loads(INVENTORY.read_text(encoding="utf-8"))[section][key])


def wrapper_modules() -> list[Path]:
    return sorted(path for path in WRAPPERS.rglob("*.py") if path.name != "__init__.py")


def module_path(path: Path) -> str:
    """``.../wrappers/c00_x/y.py`` -> ``econflow_engine.wrappers.c00_x.y``."""
    return "econflow_engine.wrappers." + ".".join(path.relative_to(WRAPPERS).with_suffix("").parts)


def signature_annotations(path: Path) -> set[str]:
    """Every ``pd.X``/``np.X`` a signature names, over EVERY parameter.

    OVER EVERY PARAMETER, REQUIRED OR OPTIONAL, and that is the whole point.
    beartype resolves an annotation when the argument it guards is checked, so an
    optional handle is the same wall one call later: omit the argument and the
    stub is reached, PASS it and ``pd`` has to exist. Fifteen modules import
    pandas or numpy for an optional parameter alone, and a sweep restricted to
    required parameters never opens one of them.

    Walked as an AST rather than split out of ``ast.unparse``: an optional
    parameter is annotated ``pd.DataFrame | None``, whose text has no attribute
    ``getattr`` could find. Measured over the tier -- every wrapper parameter is
    keyword-only, no return annotation names either module, so this is the whole
    signature surface and not a sample of it.
    """
    named: set[str] = set()
    for fn in ast.parse(path.read_text(encoding="utf-8")).body:
        if not isinstance(fn, ast.FunctionDef) or fn.name.startswith("_"):
            continue
        for arg in fn.args.kwonlyargs:
            if arg.annotation is None:
                continue
            named.update(
                f"{node.value.id}.{node.attr}"
                for node in ast.walk(arg.annotation)
                if isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id in SIGNATURE_NAMES
            )
    return named


def required_annotations(path: Path) -> dict[str, dict[str, str]]:
    """fn -> {parameter: annotation}, over the REQUIRED parameters only.

    Required is spelled as "the generator gave it no ``= None``", which is the
    same rule ``render_param`` emits by.

    THE FILTER IS HERE BECAUSE A CALLER HAS TO BUILD A VALUE, and for no other
    reason. ``handle_only_calls`` below supplies an argument for every parameter
    it names, so it can only name the ones ``HANDLE_VALUES`` can construct; an
    optional parameter is omitted from the call and needs no value. The namespace
    sweep passes no arguments at all and therefore uses ``signature_annotations``
    instead -- restricting IT to required parameters is what left fifteen modules
    unexamined.
    """
    out: dict[str, dict[str, str]] = {}
    for fn in ast.parse(path.read_text(encoding="utf-8")).body:
        if not isinstance(fn, ast.FunctionDef) or fn.name.startswith("_"):
            continue
        out[fn.name] = {
            arg.arg: ast.unparse(arg.annotation) if arg.annotation else ""
            for arg, default in zip(fn.args.kwonlyargs, fn.args.kw_defaults, strict=True)
            if default is None
        }
    return out


def handle_only_calls() -> Iterator[tuple[Path, str, dict[str, str]]]:
    """Every ``(module, function, required)`` this suite can call from handles alone."""
    for path in wrapper_modules():
        for fn, required in required_annotations(path).items():
            if required and set(required.values()) <= set(HANDLE_VALUES):
                yield path, fn, required


@pytest.fixture(scope="module")
def planted_verdicts(tmp_path_factory: pytest.TempPathFactory) -> dict[str, str]:
    """Both planted shapes called under ``beartype.claw``, in one subprocess.

    A SUBPROCESS AND NOT THIS ONE. ``beartype_package`` installs a process-wide
    import hook; this session already carries the one conftest.py installed over
    ``econflow_engine``, and a second one planted mid-run would outlive the test
    that asked for it. Both shapes share the one interpreter, so the difference
    between the two verdicts is the header and nothing else.

    The cost of that isolation is that these verdicts say NOTHING about this
    session's hook, which is what
    ``test_the_session_hook_is_live_over_the_wrapper_tier`` is for.
    """
    root = tmp_path_factory.mktemp("planted_annotations")
    package = root / "planted_wrappers"
    package.mkdir()
    (package / "__init__.py").write_text('"""Planted."""\n', encoding="utf-8")
    for name, (source, _) in PLANTED.items():
        (package / f"{name}.py").write_text(source, encoding="utf-8")

    done = subprocess.run(
        [sys.executable, "-c", _PLANTED_RUNNER, str(root), *PLANTED],
        capture_output=True,
        text=True,
        check=False,
    )
    if done.returncode != 0:
        raise AssertionError(f"the planted runner failed:\n{done.stdout}\n{done.stderr}")
    return dict(line.split(" ", 1) for line in done.stdout.strip().splitlines())


@pytest.mark.parametrize("shape", sorted(PLANTED))
def test_the_planted_header_shapes_reach_the_verdicts_written_down(
    planted_verdicts: dict[str, str], shape: str
) -> None:
    """CONTROL ONE: what beartype does with each header shape.

    ``type_checking_only`` is the shape the emitter used to write, and calling it
    IS the defect; ``imported_at_run_time`` is the shape it writes now. This is
    the whole of what a child interpreter can answer for -- that the two shapes
    are distinguishable at all. Whether THIS session still has a hook is control
    two's question.
    """
    expected = PLANTED[shape][1]
    assert planted_verdicts[shape] == expected, (
        f"the planted {shape} header produced {planted_verdicts[shape]}, not {expected}; "
        "beartype no longer resolves annotations the way the wrapper tier depends on, "
        "and the sweeps below have stopped proving anything"
    )


def test_the_session_hook_is_live_over_the_wrapper_tier() -> None:
    """CONTROL TWO: ``beartype.claw`` really is installed over this session's imports.

    WITHOUT THIS THE TWO SWEEPS BELOW CAN BE GREEN FOR HAVING RUN WITH RUN-TIME
    TYPE CHECKING SWITCHED OFF. A stub raises ``NotImplementedError`` with or
    without the hook, so the call sweep's verdict is identical in both worlds and
    the subprocess control cannot see this session at all. Measured by commenting
    out ``beartype_package("econflow_engine")`` in ``tests/conftest.py``: every
    other test in this module stayed green.

    A WRONG ARGUMENT TYPE, WHICH ONLY THE HOOK CAN OBJECT TO. beartype checks
    parameters BEFORE the body runs, so an installed hook answers
    ``BeartypeCallHintParamViolation`` and an absent one falls through to the
    stub's ``NotImplementedError``. Per ``tests/support.py::as_shipped`` beartype
    is a ``dev`` dependency and this hook is installed by conftest.py alone, so
    what is asserted here is a property of the TEST SESSION and never of a
    deployed engine -- and ``BeartypeCallHintParamViolation`` subclasses neither
    ``ValueError`` nor ``TypeError``, so no gate's own refusal can be mistaken
    for it.
    """
    target = next(handle_only_calls(), None)
    assert target is not None, (
        "no wrapper is callable from handles alone, so this control has no target; "
        "it cannot report that the hook is live by examining nothing"
    )
    path, fn, required = target
    wrapper = getattr(import_module(module_path(path)), fn)
    with pytest.raises(BeartypeCallHintParamViolation):
        wrapper(**dict.fromkeys(required, object()))


def test_every_signature_name_is_bound_in_its_module_at_run_time() -> None:
    """The denominator: every module imported and read, not grepped.

    ``pd`` and ``np`` are looked up in the imported module's own namespace and
    the annotated attribute is fetched from them, which is what beartype does
    with the forward reference. No argument is constructed, so this sweep is
    under no obligation to skip an optional parameter -- it covers every module
    the call sweep below cannot reach, whether because its required parameters
    are not handles alone or because its only handle is optional.
    """
    parsed = 0
    named = 0
    unbound: list[str] = []
    for path in wrapper_modules():
        parsed += 1
        annotations = signature_annotations(path)
        if not annotations:
            continue
        named += 1
        namespace = vars(import_module(module_path(path)))
        for annotation in sorted(annotations):
            root, attribute = annotation.split(".", 1)
            bound = namespace.get(root)
            if bound is None or not hasattr(bound, attribute):
                unbound.append(f"{path.relative_to(WRAPPERS)}: {annotation}")

    floor = inventory("engine", "wrappers")
    assert parsed >= floor, f"walked {parsed} module(s), below the floor {floor}"
    named_floor = inventory("suite", "min_signature_name_modules")
    assert named >= named_floor, (
        f"{named} module(s) name pandas or numpy in a signature, below the floor "
        f"{named_floor} in .github/inventory.json; the sweep has shrunk, and what it "
        "examines must never fall without a reviewed diff saying so"
    )
    assert not unbound, unbound[:10]


def test_every_stub_callable_from_handles_alone_reaches_its_body() -> None:
    """The proof: real calls, under the hook this session already installed.

    A stub raises ``NotImplementedError``, and beartype resolves the annotations
    BEFORE the body runs -- so ``NotImplementedError`` is the evidence that
    resolution succeeded. Anything else means the annotation stopped the call.

    A WRITTEN BODY ANSWERS ``GateError`` INSTEAD, and the sweep is told which
    functions those are rather than admitting the class everywhere. The arguments
    below are EMPTY handles -- a Series, a frame and an array with no rows at all,
    which is what ``HANDLE_VALUES`` holds and what the note there is about -- so a
    body that reached them must refuse: it has no observations, and every such
    method has a length rule. Accepting ``GateError`` from a stub would let a body land
    unnoticed in the stub set, and accepting anything but a refusal from a body
    would let it return a result over no data, so the two sets are asserted
    separately and neither can cover for the other. ``stub_ledger`` is the walk
    ``engine.n_implemented`` is measured with, so the split cannot drift from the
    manifest.
    """
    from econflow_engine.errors import GateError
    from econflow_engine.metrics import stub_ledger

    implemented = {name for _, name in stub_ledger(WRAPPERS).implemented}
    called = 0
    wrong: list[str] = []
    for path, fn, required in handle_only_calls():
        called += 1
        arguments = {name: HANDLE_VALUES[ann] for name, ann in required.items()}
        expected: type[Exception] = GateError if fn in implemented else NotImplementedError
        try:
            getattr(import_module(module_path(path)), fn)(**arguments)
        except expected:
            continue
        except Exception as exc:
            wrong.append(
                f"{path.relative_to(WRAPPERS)}::{fn}: {type(exc).__name__}: {exc} "
                f"(expected {expected.__name__})"
            )
        else:
            wrong.append(f"{path.relative_to(WRAPPERS)}::{fn}: returned without raising")

    called_floor = inventory("suite", "min_handle_only_calls")
    assert called >= called_floor, (
        f"{called} wrapper call(s) were reachable from handles alone, below the floor "
        f"{called_floor} in .github/inventory.json; give the handle parameters defaults "
        "and this sweep shrinks to nothing without a word"
    )
    assert not wrong, wrong[:10]
