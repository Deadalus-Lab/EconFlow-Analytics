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
"""

from __future__ import annotations

import ast
import doctest
import json
import sys
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

import gen_wrappers as G  # noqa: E402  (after sys.path)

WRAPPERS = ENGINE_ROOT / "src" / "econflow_engine" / "wrappers"
WRAPPER_TESTS = ENGINE_ROOT / "tests" / "wrappers"
INVENTORY = ENGINE_ROOT.parent / ".github" / "inventory.json"

HEADER_BEGIN = "# --- gen_wrappers: header begin ---"
HEADER_END = "# --- gen_wrappers: header end ---"
DOCSTRING_END = ".. gen_wrappers: end of generated docstring"
SCAFFOLD_MARKER = "TODO(2.2)"

SECTIONS = ("Args:", "Returns:", "Gates:", "Examples:", "Note:")

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


def test_no_wrapper_docstring_offers_a_doctest_example(
    wrapper_functions: list[tuple[str, ast.FunctionDef]],
) -> None:
    """Zero examples in the tier, and the parser that box 2.1.18 will use says so.

    An example against a body that raises NotImplementedError is a failure, and
    1456 of them would arrive on the day ``--doctest-modules`` is switched on.
    The example is written with the body, which is the only point at which one
    can be true.
    """
    parser = doctest.DocTestParser()
    offenders = [
        f"{label}::{node.name}"
        for label, node in wrapper_functions
        if parser.get_examples(ast.get_docstring(node, clean=False) or "")
    ]
    modules = sorted(WRAPPERS.rglob("*.py"))
    offenders += [
        str(path.relative_to(WRAPPERS))
        for path in modules
        if parser.get_examples(ast.get_docstring(ast.parse(path.read_text("utf-8"))) or "")
    ]
    assert not offenders, offenders[:20]
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
