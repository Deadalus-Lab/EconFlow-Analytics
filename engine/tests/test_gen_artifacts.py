# SPDX-License-Identifier: AGPL-3.0-only
"""The authoring surface: corpus/** is the source, artifacts/*.json the output.

WHY THIS SUITE EXISTS. Between 2026-08-19 and 2026-08-20 the catalogue was
read-only: the three METHOD-SELECTION files had been deleted as duplicates of the
sealed artifacts, and the wrapper skill forbids editing ``artifacts/`` by hand.
``scripts/gen_artifacts.py`` restores the authoring surface, and two checks make
it trustworthy. ``--check`` rebuilds the committed artifacts from the corpus and
compares them byte for byte, so a corpus that silently dropped a field cannot look
like one that did not. ``--continuity`` asserts that nothing the retired contract
described has disappeared.

THE PROOF ALREADY EARNED ITS KEEP. On its first run the original round-trip
failed with one divergence, ``nodes[429].memory_class: "heavy" != "light"`` -- the
extractor had asked the mechanical rule about a spec that still carried its own
declared value, so the comparison answered itself and ``ga_sim``'s override was
dropped. A test that cannot fail proves nothing; that one did fail, on a real
defect, before it passed.

WHAT CHANGED ON 2026-08-21. The superseded v1 artifacts were retired, so the
round-trip lost the thing it compared against. Its unique property -- that nothing
ever disappears -- needs names, not artifacts, and now reads
``legacy-inventory.json``: the 913 function names, the 252 card ids, and the
contract hashes of the retired scheme, which nothing in this tree can recompute.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pytest

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

import gen_artifacts as G  # noqa: E402  (after sys.path)

ARTIFACTS = ENGINE_ROOT / "artifacts"


def read(name: str) -> Any:
    return json.loads((ARTIFACTS / name).read_bytes().decode("utf-8"))


@pytest.fixture(scope="module")
def corpus() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    return G.read_corpus()


# --------------------------------------------------------------------------
# The proof
# --------------------------------------------------------------------------

def test_the_legacy_inventory_is_self_consistent_and_covered() -> None:
    """The retired contract's membership, and the tokens nothing can recompute.

    This replaced two tests that rebuilt the superseded artifacts from the corpus
    and compared them field by field. Those artifacts are gone; what they uniquely
    held is here. The check is the same in substance -- the corpus must still
    describe everything the retired contract described -- and the two properties
    below are what make it more than a tautology: the file must agree with its own
    declared counts, and every hash it carries must be a token of the retired
    scheme rather than a recomputed modern one.
    """
    inv = read("legacy-inventory.json")
    assert inv["n_nodes"] == len(inv["contract_hashes"]) == 913
    assert inv["n_cards"] == len(inv["card_ids"]) == 252
    assert all(h.startswith("c-") for h in inv["contract_hashes"].values()), (
        "a legacy token was overwritten with a modern one; the retired scheme is "
        "'c-' and the current one is 'c2-'"
    )
    live = {n["fn"] for n in read("node-specs.json")["nodes"]}
    assert set(inv["contract_hashes"]) <= live
    assert {int(i) for i in inv["card_ids"]} <= {
        int(c["id"]) for c in read("method-cards.json")["cards"]
    }


def test_the_committed_artifacts_reproduce_from_the_corpus() -> None:
    """--check, as a test. A committed artifact that no longer matches its source
    is the exact failure this whole tier is built to make impossible."""
    assert G.run_check() == 0


def test_continuity_passes_on_the_committed_corpus() -> None:
    assert G.run_continuity() == 0


def test_continuity_permits_growth_but_refuses_a_deletion(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """THE PROPERTY THAT MAKES THE CHECK SURVIVABLE.

    The catalogue is going to keep growing. A check pinned to exactly 913 nodes
    and 252 cards would fail on the first new one, and whoever hit that would
    delete the check rather than the card -- so growth must pass. What must never
    pass is a retired entry going MISSING, because that is the regression this
    check exists to catch. Both directions are asserted here; asserting only the
    first would leave a check that cannot fail.
    """
    import shutil

    def corpus_copy() -> Path:
        target = tmp_path / f"corpus{len(list(tmp_path.iterdir()))}"
        shutil.copytree(G.CORPUS, target)
        return target

    template = json.loads((G.CORPUS / "23-real-time-revisions.json").read_text("utf-8"))

    grown = corpus_copy()
    block = json.loads((grown / "23-real-time-revisions.json").read_text("utf-8"))
    block["cards"].append({
        "id": 9001, "method": "PROBE", "wrapper_file": "c23_real_time_revisions/probe.py",
        "tool_fns": ["probe_fn"], "when": "w", "when_not": "wn", "alternatives": [],
        "output_key_fields": ["k"], "interpretation_traps": ["t"], "sources": ["s"],
        "precondition_tools": None, "precondition_gates": None})
    block["nodes"].append({
        "fn": "probe_fn", "card_id": 9001, "register": None, "input_example": {"x": 1},
        "arguments": [{"name": "x", "kind": "integer", "required": True, "description": "d",
                       "pointer_handle": False, "json_type": "integer", "enum": None,
                       "allowed_vars": None, "default": None, "has_default": False,
                       "default_json_type": None}]})
    (grown / "23-real-time-revisions.json").write_text(
        json.dumps(block, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(G, "CORPUS", grown)
    assert G.run_continuity() == 0, "a new card must not break continuity"

    shrunk = corpus_copy()
    block = json.loads(json.dumps(template))
    removed = block["nodes"].pop(0)["fn"]
    (shrunk / "23-real-time-revisions.json").write_text(
        json.dumps(block, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    monkeypatch.setattr(G, "CORPUS", shrunk)
    assert G.run_continuity() == 1, f"deleting {removed} must fail continuity"


# --------------------------------------------------------------------------
# The corpus stores no derived field -- one fact, one home
# --------------------------------------------------------------------------

@pytest.mark.parametrize(
    "field", ["route", "executability", "cacheability", "contract_hash", "category"]
)
def test_no_corpus_node_stores_a_derived_field(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]], field: str
) -> None:
    categories, _ = corpus
    offenders = [
        (block["category"], node["fn"])
        for block in categories
        for node in block["nodes"]
        if field in node
    ]
    assert offenders == [], offenders[:5]


@pytest.mark.parametrize("field", ["embed_text", "category"])
def test_no_corpus_card_stores_a_derived_field(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]], field: str
) -> None:
    categories, _ = corpus
    offenders = [
        (block["category"], card["id"])
        for block in categories
        for card in block["cards"]
        if field in card
    ]
    assert offenders == [], offenders[:5]


def test_every_memory_class_override_actually_overrides(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
) -> None:
    """An override that agrees with the rule is noise that will rot. And at least
    one must exist, or the escape hatch is untested and would break unnoticed."""
    from econflow_engine.node.memory_class import memory_class_of

    categories, _ = corpus
    overrides = [
        (block["category"], node["fn"], node["memory_class"], memory_class_of(
            {k: v for k, v in node.items() if k != "memory_class"}))
        for block in categories
        for node in block["nodes"]
        if "memory_class" in node
    ]
    assert overrides, "no override in the corpus: the escape hatch is never exercised"
    gratuitous = [o for o in overrides if o[2] == o[3]]
    assert gratuitous == [], gratuitous


# --------------------------------------------------------------------------
# Joins and identities
# --------------------------------------------------------------------------

def test_card_ids_are_unique_and_never_renumbered(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
) -> None:
    """Ids are identities, not positions: 252 cards over the range 1..257 with
    five gaps. A renumber would rewrite every card_id and every '-> #N' in the
    prose, silently."""
    categories, _ = corpus
    ids = [c["id"] for block in categories for c in block["cards"]]
    assert len(ids) == len(set(ids)), "duplicate card id"
    assert min(ids) >= 1
    assert sorted(ids) == sorted(c["id"] for c in read("method-cards.json")["cards"])
    # The retired contract's ids, read from the inventory that outlived it. Reading
    # them from the live catalogue instead would compare it against itself and the
    # assertion would hold no matter what happened.
    retired = {int(i) for i in read("legacy-inventory.json")["card_ids"]}
    assert retired <= set(ids), "a card id the retired contract described vanished"
    assert min(set(ids) - retired, default=258) >= 258, "new ids must start at 258"


def test_the_card_node_join_is_total(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
) -> None:
    categories, _ = corpus
    node_fns = {n["fn"] for block in categories for n in block["nodes"]}
    card_fns = {fn for block in categories for c in block["cards"] for fn in c["tool_fns"]}
    assert node_fns == card_fns
    card_ids = {c["id"] for block in categories for c in block["cards"]}
    dangling = sorted(
        n["fn"] for block in categories for n in block["nodes"]
        if n["card_id"] not in card_ids
    )
    assert dangling == [], dangling[:10]


def test_a_wrapper_file_never_spans_two_categories(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
) -> None:
    """gen_wrappers.py refuses this at generation time; catching it here names the
    card instead of the file."""
    categories, _ = corpus
    seen: dict[str, str] = {}
    clashes = []
    for block in categories:
        for card in block["cards"]:
            owner = seen.setdefault(card["wrapper_file"], block["category"])
            if owner != block["category"]:
                clashes.append((card["wrapper_file"], owner, block["category"]))
    assert clashes == [], clashes


# --------------------------------------------------------------------------
# The emitted v2
# --------------------------------------------------------------------------

def test_v2_nodes_carry_a_computed_contract_hash() -> None:
    import re

    nodes = read("node-specs.json")["nodes"]
    assert all(re.match(r"^c2-[0-9a-f]{64}$", n["contract_hash"]) for n in nodes)
    assert len({n["contract_hash"] for n in nodes}) == len(nodes)


def test_v2_declares_its_version_and_its_producer() -> None:
    for name in ("node-specs.json", "method-cards.json"):
        artifact = read(name)
        assert artifact["artifact_version"] == 2
        assert "gen_artifacts.py" in artifact["generated_by"]


def test_the_v2_sidecars_match_the_bytes() -> None:
    import hashlib

    for stem in ("node-specs", "method-cards"):
        digest = hashlib.sha256((ARTIFACTS / f"{stem}.json").read_bytes()).hexdigest()
        recorded = (ARTIFACTS / f"{stem}.sha256").read_text(encoding="utf-8").split()[0]
        assert digest == recorded, stem


def test_the_cards_pin_the_node_specs_they_were_built_against() -> None:
    """A card set describing nodes that no longer exist is worse than no card."""
    import hashlib

    digest = hashlib.sha256((ARTIFACTS / "node-specs.json").read_bytes()).hexdigest()
    assert read("method-cards.json")["source"]["node_specs_sha256"] == digest


def test_method_sources_covers_every_node_and_module(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
) -> None:
    """gen_wrappers.py REFUSES to run without a row per module, but nothing was
    checking the rows were CURRENT. A node appended to an existing card once left
    its row's node_fns stale, and the register disagreed with the artifact by
    exactly that node while every other gate stayed green."""
    register = json.loads(
        (ENGINE_ROOT / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))
    categories, _ = corpus

    modules = {c["wrapper_file"].removesuffix(".py")
               for block in categories for c in block["cards"]}
    assert set(register["modules"]) == modules
    assert register["n_modules"] == len(modules)

    listed = [fn for row in register["modules"].values() for fn in row["node_fns"]]
    spec = {n["fn"] for n in read("node-specs.json")["nodes"]}
    assert set(listed) == spec, sorted(spec.symmetric_difference(listed))[:10]
    assert register["n_node_fns"] == len(listed) == len(spec)


def test_method_sources_preserves_the_authored_columns() -> None:
    """category, package, cards, methods and node_fns are derived and rewritten;
    status, library and paper are the register's own content and must survive a
    rebuild, or every implementation decision is lost on the next --build."""
    register = json.loads(
        (ENGINE_ROOT / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))
    rows = register["modules"].values()
    assert any(r["library"] for r in rows), "no row names a library"
    for row in rows:
        assert row["status"] in {"planned", "selected"}, row
        assert not (row["library"] and row["paper"]), (
            "a row names a library AND a paper; the register permits one", row)
