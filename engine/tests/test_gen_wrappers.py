# SPDX-License-Identifier: AGPL-3.0-only
"""The wrapper generator: the anatomy it emits, the regions it owns, its scaffold.

THREE PROPERTIES, AND EACH ONE IS ASSERTED OVER THE WHOLE TIER RATHER THAN OVER A
SAMPLE. A wrapper docstring carries five sections and a sentinel; no stub offers a
doctest example; and everything after a sentinel belongs to whoever writes the
body and survives a regeneration byte for byte.

WHY THE COUNTS APPEAR IN THE ASSERTIONS. The sweeps below read the tree and would
pass just as cheerfully over an empty one, so each states how many objects it
examined and compares that with .github/inventory.json. A walk that collapses to
zero then turns this red instead of green, which is the one failure this
repository has met most often.

THE MARKERS ARE KEPT HERE A SECOND TIME, DELIBERATELY. scripts/gen_wrappers.py
holds the only other copy. A marker changed on one side is then caught by
disagreement between two homes rather than believed on the word of one.

WHERE A SINGLE HAND-BUILT MODULE IS NOT ENOUGH. Three of the sweeps below run
``--write`` and ``--check`` over a writable COPY OF THE WHOLE TIER, because two
of the defects they refuse are invisible on one file: a splice that takes one
line too many trims every module by the same amount and leaves each one
internally consistent, and a section emitted on the wrong side of a sentinel
reads perfectly well until the next regeneration deletes somebody's work. Both
show up only as bytes, and only in aggregate.
"""

from __future__ import annotations

import ast
import doctest
import json
import shutil
import sys
from pathlib import Path
from typing import Any

import pytest

from econflow_engine.metrics import find_manifest, stub_ledger
from econflow_engine.naming import category_package, wrapper_module_name

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

import gen_wrappers as G  # noqa: E402  (after sys.path)

WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
WRAPPER_TESTS = ENGINE_ROOT / "tests" / "wrappers"
INVENTORY = find_manifest(Path(__file__))

HEADER_BEGIN = "# --- gen_wrappers: header begin ---"
HEADER_END = "# --- gen_wrappers: header end ---"
DOCSTRING_END = ".. gen_wrappers: end of generated docstring"
SCAFFOLD_MARKER = "TODO(2.2)"

SECTIONS = ("Args:", "Returns:", "Gates:", "Examples:", "Note:")

# THE SAME SECTIONS, IN THE ORDER THE EMITTER FIXES, WITH THE SENTINEL WHERE IT
# BELONGS. Presence says a section exists; only this says which SIDE of the
# sentinel it landed on, which is the whole contract of the splice.
ORDERED_SECTIONS = (
    "\n    Args:",
    "\n    Returns:",
    "\n    Gates:",
    f"\n    {DOCSTRING_END}",
    "\n    Examples:",
    "\n    Note:",
)

# One module, two tool functions, a written body in the second: small enough to
# read in a failure message and still a real wrapper with real markers.
SPLICED_MODULE = "c19_business_cycle_dating/bry_boschan.py"

AUTHOR_PART = [
    "",
    "    Examples:",
    "        A worked example lands with the body.",
    "",
    "    Note:",
    "        Hand-written for this test; nothing upstream is called.",
    '    """',
    '    return {"peaks": [0], "troughs": [1]}',
]


def inventory(section: str, key: str) -> int:
    """One asserted constant, from the one file that holds them all."""
    return int(json.loads(INVENTORY.read_text(encoding="utf-8"))[section][key])


def is_stub(fn: ast.FunctionDef) -> bool:
    """A docstring and a single ``raise NotImplementedError``, and nothing else."""
    return G.holds_only_generated_stubs(ast.Module(body=[fn], type_ignores=[]), [fn.name]) is None


def in_order(doc: str) -> bool:
    """True when all six landmarks are present, each after the one before it."""
    at = [doc.find(mark) for mark in ORDERED_SECTIONS]
    return all(i >= 0 for i in at) and at == sorted(at)


def module_fns(source: str) -> list[str]:
    """The names a scaffold's ``MODULE_FNS`` tuple holds, read off its syntax tree."""
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "MODULE_FNS" for target in node.targets
        ):
            assert isinstance(node.value, ast.Tuple), "MODULE_FNS is not a tuple"
            return [str(ast.literal_eval(element)) for element in node.value.elts]
    raise AssertionError("the scaffold emitted no MODULE_FNS")


@pytest.fixture(scope="module")
def wrapper_functions() -> list[tuple[str, ast.FunctionDef]]:
    """Every public tool function under wrappers/, labelled by its module."""
    out: list[tuple[str, ast.FunctionDef]] = []
    for path in sorted(WRAPPERS.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        label = str(path.relative_to(WRAPPERS))
        out += [
            (label, node)
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")
        ]
    return out


@pytest.fixture(scope="module")
def plan_and_context() -> tuple[dict[Path, str], dict[str, Any]]:
    return G.build_plan()


@pytest.fixture
def sandbox(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """A writable copy of the whole wrapper tier, with the generator pointed at it.

    ``OUT_ROOT`` and ``ENGINE_ROOT`` are module globals read at CALL time -- the
    first to plan where a module belongs, the second to label one in a report --
    so redirecting the pair is what lets ``--write`` and ``--check`` be exercised
    for real, over 598 files that can be edited and destroyed, rather than
    against a mock of themselves.

    ``ARTIFACTS`` and ``INVENTORY`` are module globals of exactly the same kind
    and are just as patchable; this fixture DELIBERATELY LEAVES THEM ALONE, so
    they go on pointing at the committed tree. Rebinding ``ENGINE_ROOT`` does not
    reach them -- each was derived from it once, at import, and holds a Path of
    its own -- so leaving them out is the whole of what it takes. The asymmetry
    is the point: a sandboxed run has to be planned from the real artifacts and
    counted against the real manifest, or it proves nothing about the tier it
    copied.

    A test that takes this fixture must call ``build_plan`` itself. The
    module-scoped plan above is built against the committed tree, and one built
    inside a sandbox would be cached and handed to every later test in the file.
    """
    root = tmp_path / "wrappers"
    shutil.copytree(WRAPPERS, root, ignore=shutil.ignore_patterns("__pycache__"))
    monkeypatch.setattr(G, "OUT_ROOT", root)
    monkeypatch.setattr(G, "ENGINE_ROOT", tmp_path)
    return root


# ---------------------------------------------------------------------------
# 2.1.6 -- the anatomy
# ---------------------------------------------------------------------------


def test_every_generated_docstring_carries_the_whole_anatomy(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
) -> None:
    """Args, Returns, Gates, Examples, Note and the sentinel, on all of them.

    ASSERTED OVER ALL 1456, NOT OVER THE IMPLEMENTED ONES. There are no
    implemented ones today, so a rule scoped to them would examine nothing and
    report success -- which is the shape of a gate that has never run.
    """
    problems: list[str] = []
    for label, node in wrapper_functions:
        doc = ast.get_docstring(node, clean=False)
        if doc is None:
            problems.append(f"{label}::{node.name}: no docstring at all")
            continue
        problems += [
            f"{label}::{node.name}: no '{section}' section"
            for section in SECTIONS
            if f"\n    {section}" not in doc
        ]
        if f"\n    {DOCSTRING_END}" not in doc:
            problems.append(f"{label}::{node.name}: no generated-docstring sentinel")
    assert not problems, problems[:20]
    assert len(wrapper_functions) == inventory("engine", "methods")


def test_the_generated_sections_keep_their_order(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
) -> None:
    """Args, Returns, Gates, the sentinel, then Examples and Note. In that order.

    THE SENTINEL'S POSITION IS THE CONTRACT, and the test above cannot state it:
    an emitter that put Examples and Note ABOVE the sentinel satisfies every
    presence assertion in this file and reproduces exactly under ``--check``,
    having moved the two author-owned sections inside the span ``--write``
    re-derives. Every worked example and implementation note written in 2.2
    would then be destroyed by the next regeneration, silently, tier-wide.

    ASSERTED ON THE PLANNED TEXT AS WELL AS ON THE TREE. The committed files
    record the last write, so an emitter changed today looks correct there until
    somebody runs ``--write`` -- and that run is the one that does the damage.
    """
    problems = [
        f"{label}::{node.name}"
        for label, node in wrapper_functions
        if not in_order(ast.get_docstring(node, clean=False) or "")
    ]
    assert not problems, problems[:20]
    assert len(wrapper_functions) == inventory("engine", "methods")

    plan, _ = plan_and_context
    planned: list[str] = []
    for path, source in sorted(plan.items()):
        if path.name == "__init__.py":
            continue
        for node in ast.parse(source).body:
            if not isinstance(node, ast.FunctionDef) or node.name.startswith("_"):
                continue
            if not in_order(ast.get_docstring(node, clean=False) or ""):
                problems.append(f"{path.name}::{node.name} (as planned)")
            planned.append(node.name)
    assert not problems, problems[:20]
    assert len(planned) == inventory("engine", "methods")


def test_the_validation_section_is_rendered_from_the_card_and_not_from_a_constant(
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
) -> None:
    """The twenty-five authored sentences, followed from their cards into docstrings.

    THE OTHER HALF OF A PIN THAT ALREADY EXISTS. tests/test_gates_registry.py
    holds these sentences to their cards by count and by digest, so a reword or a
    deletion on the CARD side is loud. Nothing there says they reach a wrapper
    docstring: ``validation_section`` returning ``[]`` empties the section from
    every one of those modules and every count in this file goes on passing.

    THEY ARE THE STRONGEST POSITIVE CONTROL THE SECTION PAIR HAS. The Gates
    section renders the same sentence on every card whose ``precondition_gates``
    is empty, which is nearly all of them, so it is close to indistinguishable
    from a constant; these twenty-five sentences are prose that can have arrived
    only by being read off a card.
    """
    plan, _ = plan_and_context
    cards = [
        card
        for card in G.read_artifact("method-cards.json")["cards"]
        if card.get("validation_notes")
    ]
    assert len(cards) == 9, "the corpus moved; re-measure before editing this test"

    seen = 0
    for card in cards:
        path = (
            G.OUT_ROOT
            / category_package(card["category"])
            / f"{wrapper_module_name(card['wrapper_file'])}.py"
        )
        # The emitter wraps a sentence across lines, so both homes are compared
        # with their whitespace runs collapsed -- which is what makes the whole
        # sentence, rather than a word of it, the thing asserted.
        homes = {
            "the planned text": " ".join(plan[path].split()),
            "the committed module": " ".join(path.read_text(encoding="utf-8").split()),
        }
        for note in card["validation_notes"]:
            # THE EXPECTED SIDE SHARES NO TRANSFORM WITH THE EMITTER, and routing
            # it through ``docsafe`` is exactly the mistake: with ``docsafe``
            # returning "" both sides collapse to "", every bullet renders as a
            # bare "- ", and ``"" in home`` passes on all twenty-five. Measured over
            # the corpus: no note carries a backslash or a triple quote, so
            # ``docsafe`` is a no-op on every one of them and dropping it here
            # compares the same bytes -- while a regression in it now shows. The
            # two 2026-08-28 cards were re-measured against this and carry none
            # either.
            want = " ".join(str(note).split())
            assert want, "an empty note asserts nothing"
            for where, home in homes.items():
                assert want in home, f"card #{card['id']}: {note!r} is absent from {where}"
            seen += 1
    assert seen == 25
    carrying = [
        path for path, source in plan.items() if "\n    Validation:\n" in source
    ]
    assert len(carrying) == 9, sorted(p.name for p in carrying)


def _implemented_pairs() -> set[tuple[str, str]]:
    """The written bodies, keyed on THE MODULE AND THE NAME rather than the name.

    ``stub_ledger`` yields ``(path, name)`` and this used to throw the path away.
    A public function in module B whose name equals an implemented node in module
    A was then classified as a body: excluded from the rule that no stub may carry
    an example, and required by the other direction to carry one it has no way to
    make true. ``tests/test_double_run_methods.py`` calls that same collision "the
    dangerous half" and refuses it in the double-run gate; the pair key is what
    refuses it here.
    """
    return {
        (str(path.relative_to(WRAPPERS)), name)
        for path, name in stub_ledger(WRAPPERS).implemented
    }


def _split_stubs_from_bodies(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
    implemented: set[tuple[str, str]],
) -> tuple[list[tuple[str, ast.FunctionDef]], list[tuple[str, ast.FunctionDef]]]:
    """Split the walked functions on the pair key. Shared with the control below."""
    stubs = [
        (label, node) for label, node in wrapper_functions if (label, node.name) not in implemented
    ]
    bodies = [
        (label, node) for label, node in wrapper_functions if (label, node.name) in implemented
    ]
    return stubs, bodies


def test_a_helper_colliding_with_another_module_s_body_is_read_as_a_stub(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
) -> None:
    """THE CONTROL FOR THE PAIR KEY, and the collision is planted rather than hoped for.

    Keyed on the bare name, an author's public helper in module B that happens to
    share a name with module A's written body is classified as a BODY. It is then
    dropped from the no-example-on-a-stub check and added to the every-body-
    carries-an-example check -- a helper that can never satisfy the second and is
    no longer watched by the first. Both halves are asserted here, and the
    collision is asserted to be real under the old key so this cannot pass by
    finding no collision at all.
    """
    implemented = _implemented_pairs()
    assert implemented, "no body is written; this control would compare nothing"
    body_label, body_name = sorted(implemented)[0]
    impostor_label = next(label for label, _ in wrapper_functions if label != body_label)
    impostor = ast.parse(f'def {body_name}() -> None:\n    """A helper, no example."""\n').body[0]
    assert isinstance(impostor, ast.FunctionDef)

    assert body_name in {name for _, name in implemented}, "the collision is not real"

    stubs, bodies = _split_stubs_from_bodies(
        [*wrapper_functions, (impostor_label, impostor)], implemented
    )
    assert (impostor_label, impostor) in stubs
    assert (impostor_label, impostor) not in bodies
    assert (body_label, body_name) in {(label, node.name) for label, node in bodies}


def test_no_stub_docstring_offers_a_doctest_example(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
) -> None:
    """No example on a body that RAISES, and the parser box 2.1.18 uses says so.

    An example against a body that raises NotImplementedError is a failure, and
    1456 of them would arrive on the day ``--doctest-modules`` is switched on.
    The example is written with the body, which is the only point at which one
    can be true.

    THE RULE IS ABOUT STUBS AND USED TO BE WORDED AS "ZERO IN THE TIER", which
    was the same statement while every body was a stub and stopped being one with
    the first body written in phase 2.2. That body arrives with the example this
    docstring has always asked for, and reading the old wording as a ceiling
    would have made writing one a failure. The set that must carry none is
    therefore narrowed to the stubs, by the SAME walk
    ``.github/actions/assert-inventory/assert.sh`` counts ``n_implemented`` with,
    and the count of examined functions is asserted below so that a narrowing to
    nothing cannot pass.

    THE OTHER DIRECTION IS ASSERTED TOO: an implemented body that carries NO
    example is refused here, because ``tests/controls/doctest_gate.py`` floors
    the collected count at ``engine.n_implemented`` and a body without one turns
    that gate red with nothing naming the cause.
    """
    parser = doctest.DocTestParser()
    stubs, bodies = _split_stubs_from_bodies(wrapper_functions, _implemented_pairs())
    assert len(bodies) == inventory("engine", "n_implemented")
    assert len(stubs) + len(bodies) == len(wrapper_functions)

    offenders = [
        f"{label}::{node.name}"
        for label, node in stubs
        if parser.get_examples(ast.get_docstring(node, clean=False) or "")
    ]
    modules = sorted(WRAPPERS.rglob("*.py"))
    offenders += [
        str(path.relative_to(WRAPPERS))
        for path in modules
        if parser.get_examples(ast.get_docstring(ast.parse(path.read_text("utf-8"))) or "")
    ]
    assert not offenders, offenders[:20]
    exampleless = [
        f"{label}::{node.name}"
        for label, node in bodies
        if not parser.get_examples(ast.get_docstring(node, clean=False) or "")
    ]
    assert not exampleless, exampleless[:20]
    # THE POSITIVE CONTROL, AND THE CEILING ABOVE RESTS ENTIRELY ON IT. "zero
    # examples found" and "the parser was never looking" print the same result,
    # and the doctest floor in tests/controls/doctest_gate.py sits at 0, so it
    # cannot notice examples appearing either. One example the parser must see.
    assert len(parser.get_examples("Examples:\n    >>> 1 + 1\n    2\n")) == 1
    assert len(wrapper_functions) == inventory("engine", "methods")
    # One __init__.py per category, plus the wrapper tier's own package.
    packages = [path for path in modules if path.name == "__init__.py"]
    assert len(packages) == inventory("engine", "categories") + 1
    assert len(modules) - len(packages) == inventory("engine", "wrappers")


def test_every_implemented_body_still_carries_its_generated_docstring(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
) -> None:
    """The implemented-only rule, and it cross-checks the manifest rather than the tree.

    ``engine.n_implemented`` is 0 today, so the loop below runs zero times. What
    keeps this from being vacuous is the equality: the count of written bodies
    this walk found has to be the count the manifest declares, so the first body
    that lands without moving that constant turns this red.
    """
    implemented = [(label, node) for label, node in wrapper_functions if not is_stub(node)]
    assert len(implemented) == inventory("engine", "n_implemented")
    for label, node in implemented:
        doc = ast.get_docstring(node, clean=False) or ""
        assert f"\n    {DOCSTRING_END}" in doc, f"{label}::{node.name} lost its sentinel"
        assert "\n    Note:" in doc, f"{label}::{node.name} lost its implementation note"


# ---------------------------------------------------------------------------
# The emission guard
# ---------------------------------------------------------------------------


def test_the_emission_guard_refuses_python_that_does_not_parse() -> None:
    """A generator that can emit unparsable source and not notice is a broken gate.

    THE PLANT IS THE DEFECT THIS EXISTS FOR, not an invented one: routing a
    ``pytest.fail`` call through the prose wrapper split its string literal
    across two lines and emitted exactly this.
    """
    G.emitted('def fine() -> None:\n    """A control that parses."""\n', "a control")
    plant = 'pytest.fail("one half\n    "and the other")\n'
    with pytest.raises(SystemExit) as raised:
        G.emitted(plant, "a deliberate plant")
    assert "a deliberate plant" in str(raised.value)


def test_the_check_denominators_have_no_default() -> None:
    """A denominator that cannot be read means the gate has not started."""
    G.inventory_constant("engine", "wrappers")
    with pytest.raises(SystemExit) as raised:
        G.inventory_constant("engine", "no_such_constant")
    assert "no_such_constant" in str(raised.value)


def test_check_reports_the_denominators_it_reached(
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """What a green ``--check`` says it examined, against what the manifest declares.

    The figures below are read from the manifest rather than typed here, so this
    states the relationship and not a copy of three numbers.
    """
    plan, context = plan_and_context
    assert G.run_check(plan, context) == 0
    out = capsys.readouterr().out
    assert f"{inventory('engine', 'categories')} package header(s)" in out
    assert f"{inventory('engine', 'wrappers')} module header region(s)" in out
    assert f"{inventory('engine', 'methods')} generated docstring region(s)" in out


def test_check_refuses_a_denominator_that_disagrees_with_the_manifest(
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    """The anti-vacuity guard of ``--check``, WATCHED FAILING.

    ``_check_counts`` is what stops a marker-parsing bug from comparing nothing
    and printing OK, and a guard nobody has seen fail is not yet a guard:
    appending to a list the caller discards, or comparing ``>=`` where the
    manifest says exactly, leaves ``--check`` green forever over a tree it has
    stopped reading. The disagreement is planted in the denominator rather than
    in the tree, because that is the direction a real bug arrives from -- the
    count collapses, the manifest does not.
    """
    plan, context = plan_and_context
    monkeypatch.setattr(G, "inventory_constant", lambda *_: 999999)
    assert G.run_check(plan, context) == 1
    out = capsys.readouterr().out
    assert "DRIFT" in out
    assert "999999" in out


# ---------------------------------------------------------------------------
# 2.1.5 -- the regions
# ---------------------------------------------------------------------------


STUB_MODULE = '''# SPDX-License-Identifier: AGPL-3.0-only
"""A control."""


def f() -> dict[str, int]:
    """Node ``f``.

    .. gen_wrappers: end of generated docstring
    """
    raise NotImplementedError(
        "f: not implemented."
    )
'''

WRITTEN_MODULE = STUB_MODULE.replace(
    '    raise NotImplementedError(\n        "f: not implemented."\n    )\n',
    '    return {"n": 1}\n',
)


def test_holds_only_generated_stubs_names_the_function_that_holds_a_body() -> None:
    """The write guard, demoted to an assertion, watched refusing a real body."""
    assert G.holds_only_generated_stubs(ast.parse(STUB_MODULE), ["f"]) is None
    assert G.holds_only_generated_stubs(ast.parse(WRITTEN_MODULE), ["f"]) == "f"


def _hand_fill(planned: str, fn: str) -> str:
    """One stub of ``planned`` given a body and author-owned Examples and Note."""
    lines = planned.split("\n")
    start = next(i for i, line in enumerate(lines) if line.startswith(f"def {fn}("))
    sentinel = next(i for i in range(start, len(lines)) if lines[i].strip() == DOCSTRING_END)
    close = next(i for i in range(sentinel, len(lines)) if lines[i] == '    """')
    after = next(
        (i for i in range(close + 1, len(lines)) if lines[i].startswith("def ")), len(lines)
    )
    return "\n".join([*lines[: sentinel + 1], *AUTHOR_PART, "", "", *lines[after:]])


def test_write_re_derives_the_generated_regions_and_preserves_everything_else(
    tmp_path: Path,
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The proof the whole marker design rests on, run through ``--write`` itself.

    The file on disk carries a written body, author-owned sections AND a
    deliberately wrong generated docstring. A splice that copied the file through
    untouched would preserve the body and fail to re-derive the region; one that
    rewrote the file whole would re-derive the region and destroy the body.
    Only a correct splice satisfies both halves.
    """
    plan, context = plan_and_context
    source = next(path for path in plan if str(path).endswith(SPLICED_MODULE))
    planned = plan[source]
    fns = context["fns_by_module"][source]

    written = _hand_fill(planned, fns[0])
    perturbed = written.replace(
        "        A JSON-safe mapping", "        Something else entirely", 1
    )
    assert perturbed != written, "the perturbation did not apply; the test proves nothing"

    target = tmp_path / "bry_boschan.py"
    target.write_text(perturbed, encoding="utf-8")
    monkeypatch.setattr(G, "ENGINE_ROOT", tmp_path)

    assert G.run_write({target: planned}, {**context, "fns_by_module": {target: fns}}) == 0

    result = target.read_text(encoding="utf-8")
    assert "Something else entirely" not in result, "the generated region was not re-derived"
    assert "A JSON-safe mapping" in result
    assert "\n".join(AUTHOR_PART) in result, "the author's bytes did not survive"
    assert result.count(HEADER_BEGIN) == 1
    assert result.count(HEADER_END) == 1
    assert result.count(DOCSTRING_END) == len(fns)
    G.emitted(result, "the spliced module")


def test_write_refuses_a_written_body_it_cannot_splice(
    tmp_path: Path,
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """No markers and a real body: the one file a whole rewrite would destroy."""
    plan, context = plan_and_context
    source = next(path for path in plan if str(path).endswith(SPLICED_MODULE))
    planned = plan[source]
    fns = context["fns_by_module"][source]

    stripped = _hand_fill(planned, fns[0]).replace(HEADER_BEGIN + "\n", "")
    target = tmp_path / "bry_boschan.py"
    target.write_text(stripped, encoding="utf-8")
    monkeypatch.setattr(G, "ENGINE_ROOT", tmp_path)

    assert G.run_write({target: planned}, {**context, "fns_by_module": {target: fns}}) == 1
    assert target.read_text(encoding="utf-8") == stripped, "a refusal wrote something"


def test_write_refuses_a_module_whose_functions_it_could_not_name(
    tmp_path: Path,
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """THE HOLE THE DEMOTION OPENED, and the guard that closes it.

    ``holds_only_generated_stubs`` loops over the function names it is given, so
    with an empty list the loop never runs and it answers None -- "still a stub,
    safe to rewrite whole". That is correct for a package __init__.py and wrong
    for anything else: a module missing from fns_by_module would be classified
    safe and overwritten, body and all. The old write path could not reach this
    because it iterated the card-derived mapping itself.
    """
    plan, context = plan_and_context
    source = next(path for path in plan if str(path).endswith(SPLICED_MODULE))
    fns = context["fns_by_module"][source]

    assert G.holds_only_generated_stubs(ast.parse(WRITTEN_MODULE), []) is None, (
        "the premise of this test no longer holds"
    )

    target = tmp_path / "bry_boschan.py"
    target.write_text(_hand_fill(plan[source], fns[0]), encoding="utf-8")
    monkeypatch.setattr(G, "ENGINE_ROOT", tmp_path)

    assert G.run_write({target: plan[source]}, {**context, "fns_by_module": {}}) == 1
    assert "bry_boschan" in target.read_text(encoding="utf-8")


def test_the_committed_tree_carries_one_marker_region_per_module() -> None:
    """598 header regions and 1456 sentinels, counted off the committed files."""
    headers = 0
    sentinels = 0
    for path in sorted(WRAPPERS.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        text = path.read_text(encoding="utf-8")
        assert text.count(HEADER_BEGIN) == 1, path
        assert text.count(HEADER_END) == 1, path
        headers += 1
        sentinels += text.count(f"    {DOCSTRING_END}")
    assert headers == inventory("engine", "wrappers")
    assert sentinels == inventory("engine", "methods")


def test_check_reads_above_a_sentinel_and_ignores_what_is_written_below_it(
    sandbox: Path,
) -> None:
    """The boundary, from both sides, on one file.

    ``run_verifications.sh`` runs ``--check`` over the COMMITTED tree, where
    ``engine.n_implemented`` is 0: no byte below any sentinel belongs to an
    author yet, so the permitting direction is never exercised there. The first
    body written in 2.2 arrives with an example and an implementation note, and
    a region drawn one line too wide would turn the drift gate red with nothing
    in the suite naming the boundary as the cause.

    THE SECOND HALF IS WHAT MAKES THE FIRST MEAN ANYTHING. A ``--check`` that
    had stopped comparing would satisfy the permissive assertion as cheerfully
    as a correct one, so the same file is then edited ABOVE its sentinel and the
    gate has to notice.
    """
    target = next(
        path for path in sorted(sandbox.rglob("*.py")) if str(path).endswith(SPLICED_MODULE)
    )
    lines = target.read_text(encoding="utf-8").splitlines(keepends=True)
    at = next(i for i, line in enumerate(lines) if line.strip() == DOCSTRING_END)
    lines.insert(at + 1, "\n        An example the author wrote by hand.\n")
    target.write_text("".join(lines), encoding="utf-8")

    plan, context = G.build_plan()
    assert G.run_check(plan, context) == 0, "an edit below a sentinel turned the drift gate red"

    above = target.read_text(encoding="utf-8").replace("    Returns:\n", "    Yields:\n", 1)
    target.write_text(above, encoding="utf-8")
    assert G.run_check(plan, context) == 1, "an edit inside a generated region went unnoticed"


def test_write_over_a_clean_tree_changes_not_one_byte(
    sandbox: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """All 598 modules, byte for byte, across a ``--write`` that had nothing to do.

    THE PROPERTY A HAND-BUILT MODULE IN tmp_path CANNOT STATE. A splice taking
    one line too many trims the same three lines from every module in the tier
    and leaves each one internally consistent: the tests built on a single
    module all pass, and ``--check`` afterwards reports OK, because the regions
    it compares still agree on both sides. The damage exists only in aggregate
    and only as bytes, which is what this compares.

    The count of files is asserted first, so a sandbox that copied a handful of
    them cannot report success for having compared a handful of them.
    """
    before = {path: path.read_bytes() for path in sorted(sandbox.rglob("*.py"))}
    expected = inventory("engine", "wrappers") + inventory("engine", "categories") + 1
    assert len(before) == expected, "the sandbox does not hold the tier it claims to"

    plan, context = G.build_plan()
    assert G.run_write(plan, context) == 0
    report = capsys.readouterr().out

    # The bytes are read before the report is, so a failure here names the
    # damage rather than the sentence the generator printed about it. WHAT IT
    # NAMES IS THE POINT: 598 files against 598 files is an unreadable diff, so
    # each entry carries the module and the line delta -- which is what says
    # whether a splice took one line too many or a header was rewritten whole.
    after = {path: path.read_bytes() for path in sorted(sandbox.rglob("*.py"))}
    assert before.keys() == after.keys(), "a no-op write added or removed a file"
    changed = [
        f"{path.name}: {before[path].count(b'\n')} -> {after[path].count(b'\n')} lines"
        for path in before
        if before[path] != after[path]
    ]
    assert not changed, (
        f"{len(changed)} of {len(before)} module(s) moved under a no-op write: {changed[:10]}"
    )
    assert "0 file(s) rewritten" in report


# ---------------------------------------------------------------------------
# 2.1.7 -- the scaffold
# ---------------------------------------------------------------------------


def test_the_scaffold_emits_the_four_mandatory_classes() -> None:
    """Gates block, structure, oracle case, determinism -- in that order."""
    tree = ast.parse(G.scaffold_tests("bry_boschan"))
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef)]
    assert [node.name for node in classes] == [
        "TestGatesBlock",
        "TestStructure",
        "TestOracleCase",
        "TestDeterminism",
    ]
    for cls in classes:
        tests = [node for node in cls.body if isinstance(node, ast.FunctionDef)]
        assert tests, f"{cls.name} emitted no test"
        for test in tests:
            assert SCAFFOLD_MARKER in ast.unparse(test), f"{cls.name}.{test.name}"


def test_every_scaffolded_test_is_red_until_it_is_written() -> None:
    """A scaffold whose tests pass is 598 files that raise the floor and assert nothing.

    ``SCAFFOLD_MARKER in ast.unparse(test)`` is satisfied by the marker string
    sitting inside ANY call -- ``pytest.skip`` included. Six skipping tests
    across 598 scaffolds is some 3,600 collected items that state nothing about
    any method, and ``suite.min_tests`` would rise to meet them. What makes a
    scaffold a scaffold is that every test in it fails until somebody writes it.
    """
    tree = ast.parse(G.scaffold_tests("bry_boschan"))
    tests = [
        node
        for cls in tree.body
        if isinstance(cls, ast.ClassDef)
        for node in cls.body
        if isinstance(node, ast.FunctionDef)
    ]
    # Two in the gates block, two in the structure class, one each in the oracle
    # and determinism classes. Measured, not a floor: a fifth class or a sixth
    # test is then a deliberate one-line edit here.
    assert len(tests) == 6
    for test in tests:
        assert len(test.body) == 1, f"{test.name} does something besides fail"
        statement = test.body[0]
        assert isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Call)
        called = statement.value.func
        assert isinstance(called, ast.Attribute) and isinstance(called.value, ast.Name)
        assert (called.value.id, called.attr) == ("pytest", "fail"), (
            f"{test.name} calls {ast.unparse(called)}; a scaffold that does not fail passes"
        )


def test_every_scaffold_names_every_function_of_the_module_it_scaffolds(
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
) -> None:
    """MODULE_FNS over all 598, against the mapping the plan derives separately.

    THE SCAFFOLD'S ONE TRUE STATEMENT DEPENDS ON THIS TUPLE. The generator
    describes ``test_the_module_exports_every_function_its_cards_name`` as the
    one assertion a scaffold can make truthfully before a body exists, and it
    iterates MODULE_FNS. Emitted empty, the tuple renders as ``MODULE_FNS = (\\n)``,
    the loop runs zero times, and that assertion becomes ``assert not []``.

    THE TWO DERIVATIONS ARE INDEPENDENT, which is what makes the comparison
    worth making: ``_resolve_module`` filters the cards itself, and the mapping
    it is compared against is the one ``build_plan`` hands the splice.
    """
    _, context = plan_and_context
    fns_by_module: dict[Path, list[str]] = context["fns_by_module"]
    problems: list[str] = []
    named = 0
    for path, fns in sorted(fns_by_module.items()):
        source = G.scaffold_tests(path.stem)
        declared = module_fns(source)
        if declared != fns:
            problems.append(f"{path.name}: names {declared}, its cards name {fns}")
        named += len(declared)
        home = f"tests/wrappers/{path.parent.name}/test_{path.stem}.py"
        if home not in source:
            problems.append(f"{path.name}: does not name {home} as its home")
    assert not problems, problems[:10]
    assert len(fns_by_module) == inventory("engine", "wrappers")
    assert named == inventory("engine", "methods")


def test_every_scaffold_the_generator_can_emit_parses_and_fits_the_line_limit(
    plan_and_context: tuple[dict[Path, str], dict[str, Any]],
) -> None:
    """All 598 of them, because a limit checked on one module is checked on none."""
    plan, _ = plan_and_context
    modules = sorted(
        path.stem for path in plan if path.suffix == ".py" and path.name != "__init__.py"
    )
    over: list[str] = []
    for module in modules:
        source = G.emitted(G.scaffold_tests(module), f"the scaffold for {module}")
        over += [
            f"{module}: {line}"
            for line in source.split("\n")
            if len(line) > G.LINE_LIMIT
        ]
    assert not over, over[:10]
    assert len(modules) == inventory("engine", "wrappers")


def test_no_committed_wrapper_test_still_carries_the_scaffold_marker() -> None:
    """A scaffold is a starting point, and a committed one asserts nothing.

    598 unfilled scaffolds would raise ``suite.min_tests`` by several thousand
    while proving nothing about any method, so the marker is what a filled test
    removes and what a committed one may not keep.
    """
    carrying = [
        str(path.relative_to(ENGINE_ROOT))
        for path in sorted(WRAPPER_TESTS.rglob("test_*.py"))
        if SCAFFOLD_MARKER in path.read_text(encoding="utf-8")
    ]
    assert not carrying, carrying


def test_the_scaffold_names_a_module_it_cannot_find() -> None:
    """A typo is a refusal, never an empty file written to the convention path."""
    with pytest.raises(SystemExit) as raised:
        G.scaffold_tests("no_such_wrapper_module")
    assert "no_such_wrapper_module" in str(raised.value)
