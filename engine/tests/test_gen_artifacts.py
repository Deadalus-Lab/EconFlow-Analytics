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

from econflow_engine.metrics import find_manifest

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


#: THE DIGESTS THIS RE-SEAL SUPERSEDED, recorded here as a second, independent
#: home. Read from the committed tree on 2026-08-26 with
#: ``git show HEAD:engine/artifacts/node-specs.sha256`` and
#: ``git show HEAD:engine/artifacts/method-cards.sha256``. They cannot be read
#: that way from the suite: ``.dockerignore`` excludes ``.git/`` and
#: run_verifications.sh runs this suite inside the image build, so a git-reading
#: test would fail the build rather than check anything. Keeping the pair here as
#: well as in ``corpus/_provenance.json`` is what makes the provenance block
#: checkable at all -- a block edited to name a digest that never existed is
#: worse than no block, and with one home nothing would notice.
#:
#: MOVED ON 2026-08-26 BY BOX 2.1.1.12, and the pair here moved with the corpus
#: record in the same commit -- that is the whole point of two homes.
#:
#: THE TWO MOVE BY VERY DIFFERENT AMOUNTS, AND A REVIEWER MUST READ THE PAIR
#: KNOWING IT. ``sources`` is a CARD field, so method-cards.json moves by 93
#: lines -- 46 entries and the 46 ``embed_text`` blobs that carry them into
#: retrieval -- while nothing in node-specs.json's catalogue changes at all: it
#: moves by exactly the two lines of the provenance block, which is emitted onto
#: both artifacts. Both digests are still the committed bytes each file
#: superseded, read with ``git show HEAD:engine/artifacts/<stem>.sha256``.
#:
#: NO ``contract_hash`` MOVES: the projection is fn, arguments, register and
#: export, and ``sources`` is none of them and lives in the other artifact.
SUPERSEDED = {
    "node_specs_sha256": "758ce29823b3cb5bb2eff5dc304969412f31c4ce079fbeab801377005f8bd39a",
    "method_cards_sha256": "49223d87e845f0423d9f1033daa131f649e8520659dd7b7cc4c8f9ebb0062dcc",
}


def test_both_artifacts_record_the_digests_this_reseal_superseded() -> None:
    """Box 2.1.1.12. The re-seal happens IN PLACE, so the only trace it leaves is
    this block: same filenames, same sidecar count, ``wrapper_file`` untouched.
    Both artifacts carry the same record, because one re-seal produced both."""
    import hashlib
    import re

    blocks = {name: read(name)["previous"] for name in ("node-specs.json", "method-cards.json")}
    assert blocks["node-specs.json"] == blocks["method-cards.json"], (
        "one re-seal, one record: the two artifacts disagree about what they superseded"
    )
    previous = blocks["node-specs.json"]
    assert previous["reason"] == (
        "box 2.1.1.12 -- 46 cards stop naming a distribution the register measured "
        "as not implementing their method"
    )
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", previous["resealed"]), previous["resealed"]
    for key, digest in SUPERSEDED.items():
        assert previous[key] == digest

    # A block naming the file it sits in records nothing. Both digests must be
    # the ones the re-seal REPLACED, so neither may equal what is on disk now.
    for stem, key in (("node-specs", "node_specs_sha256"),
                      ("method-cards", "method_cards_sha256")):
        current = hashlib.sha256((ARTIFACTS / f"{stem}.json").read_bytes()).hexdigest()
        assert previous[key] != current, (
            f"{stem}: the provenance block names the current bytes, so it records no "
            "prior state at all"
        )


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


def test_a_rebuild_carries_every_authored_column_across(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]], tmp_path: Path,
) -> None:
    """THE RULE, NOT THE COLUMN LIST -- because the list is what keeps growing.

    ``category``, ``package``, ``cards``, ``methods`` and ``node_fns`` are derived
    from the corpus and rewritten on every build. Everything else in a row is the
    register's own content, and a column absent from the carry-over is a column
    ``--build`` DELETES from all 598 rows at once -- after which ``--check``
    compares the emptied register against an equally empty rebuild and reports
    that everything reproduces. The data is gone and both gates are green.

    NAMING THE COLUMNS HERE WOULD REPRODUCE THE DEFECT IT CHECKS FOR. This suite
    named ``status``, ``library``, ``paper`` and ``wave`` while ``dataset`` was
    being added, and a test listing the columns it knows about cannot fail for
    the one it does not. So this rebuilds into a temporary tree and asserts the
    rebuilt rows are IDENTICAL to the committed ones outside the derived set --
    which is the rule, and holds for the next authored column without being
    edited.
    """
    categories, _ = corpus
    committed = json.loads(
        (ENGINE_ROOT / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))["modules"]

    G.sync_method_sources(categories, tmp_path)
    rebuilt = json.loads(
        (tmp_path / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))["modules"]

    assert set(rebuilt) == set(committed)
    for key, row in committed.items():
        assert set(rebuilt[key]) == set(row), (
            "a rebuild changed which columns a row carries; an authored column "
            "missing from sync_method_sources' carry-over is deleted here",
            key, sorted(set(row) ^ set(rebuilt[key])),
        )
        for column in set(row) - G.DERIVED_COLUMNS:
            assert rebuilt[key][column] == row[column], (key, column)


def test_a_rebuild_carries_a_column_no_committed_row_exercises_yet(
    corpus: tuple[list[dict[str, Any]], dict[str, Any]],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """THE POSITIVE CONTROL, because the register above cannot supply one.

    The test before this compares rebuilt rows against committed ones, and for a
    column no row has filled in that comparison is ``None == None`` -- which
    holds just as well with the carry-over deleted. ``dataset`` is exactly such a
    column today: the kind is defined and the row it was defined for is still
    planned, so nothing in the live register would notice it being dropped.

    So this plants a register in which EVERY authored column carries a
    distinctive value and drives the real ``sync_method_sources`` over it. No
    mock and no stub: the function reads a register and writes a register, and
    this hands it a different one. It names no column, so it covers the next
    authored column as it stands.
    """
    categories, _ = corpus
    key = sorted(G.read_corpus()[0][0]["cards"], key=lambda c: c["id"])[0]["wrapper_file"]
    key = key.removesuffix(".py")

    # THE PLANTED COLUMNS COME FROM THE COMMITTED REGISTER, NOT FROM
    # AUTHORED_COLUMNS. Reading the constant would make this control blind to the
    # one failure it exists for: a column deleted from that constant would vanish
    # from the planted record in the same edit, and the control would pass while
    # --build dropped the column from all 598 rows. Measured -- written the other
    # way first, it stayed green for `dataset`, `wave` and `paper` alike.
    committed = json.loads(
        (ENGINE_ROOT / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))["modules"]
    authored = sorted(set(next(iter(committed.values()))) - G.DERIVED_COLUMNS)
    assert authored, "the register carries no authored column; this control is empty"

    planted = {column: f"planted-{column}" for column in authored}
    # The planted register keeps the real FILENAME: sync_method_sources derives
    # what it writes under `out` from the same constant it reads, so a register
    # named anything else lands under a name the assertions below would miss.
    source = tmp_path / "in"
    source.mkdir()
    register = source / "METHOD-SOURCES.json"
    register.write_text(json.dumps({"modules": {key: planted}}), encoding="utf-8")
    monkeypatch.setattr(G, "METHOD_SOURCES", register)

    out = tmp_path / "out"
    out.mkdir()
    G.sync_method_sources(categories, out)
    rebuilt = json.loads(
        (out / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))["modules"][key]

    for column, value in planted.items():
        assert rebuilt[column] == value, (
            f"{column} did not survive a rebuild; it is missing from "
            "gen_artifacts.AUTHORED_COLUMNS and --build deletes it from every row",
            column,
        )

    # And a row the planted register says nothing about reads as UNDECIDED,
    # rather than inheriting the value from the row beside it.
    rest = json.loads((out / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))["modules"]
    other = next(k for k in rest if k != key)
    assert {c: rest[other][c] for c in authored} == {c: G.AUTHORED_COLUMNS[c] for c in authored}


def test_the_register_admits_exactly_one_source_kind_per_row() -> None:
    """The register's own domain, asserted where the generator reads it.

    tests/test_method_sources.py answers for the CONTENT of the register against
    the lockfile and the tree; this answers for the shape the generator and
    gen_wrappers.py both depend on -- a status from the closed pair, and never
    two source kinds on one row, which stops gen_wrappers mid-generation.
    """
    register = json.loads(
        (ENGINE_ROOT / "METHOD-SOURCES.json").read_bytes().decode("utf-8"))
    kinds = ("library", "paper", "dataset")
    for row in register["modules"].values():
        assert row["status"] in {"planned", "selected"}, row
        assert sum(bool(row[k]) for k in kinds) <= 1, (
            "a row names more than one of a library, a paper and a dataset; "
            "the register permits one", row)


# --------------------------------------------------------------------------
# output_keys: what a node's payload contains, and the debt of not saying
# --------------------------------------------------------------------------

INVENTORY = find_manifest(Path(__file__))


def _inventory(section: str, key: str) -> int:
    manifest = json.loads(INVENTORY.read_bytes().decode("utf-8"))
    return int(manifest[section][key])


def test_every_node_declares_an_output_keys_record() -> None:
    """``status`` has NO DEFAULT, and ``keys`` agrees with it.

    An absent record would read to every consumer as "nothing to declare", which
    is the same silence as "declared, and the payload is empty" -- two different
    claims sharing one text. The generator subscripts the corpus rather than
    calling ``.get``, so a node authored without one is a KeyError at build time;
    this asserts the property on the EMITTED artifact, where a consumer reads it.
    """
    nodes = read("node-specs.json")["nodes"]
    assert len(nodes) == _inventory("artifacts", "n_nodes")
    for node in nodes:
        record = node["output_keys"]
        assert set(record) == {"status", "keys"}, node["fn"]
        if record["status"] == "declared":
            assert isinstance(record["keys"], list) and record["keys"], node["fn"]
            assert len(set(record["keys"])) == len(record["keys"]), node["fn"]
        else:
            assert record["status"] == "undeclared", node["fn"]
            assert record["keys"] is None, node["fn"]


def test_the_undeclared_output_key_debt_is_the_measured_one() -> None:
    """A DEBT COUNTER THAT MUST REACH ZERO, and not an allowlist.

    Exact equality in both directions is what separates the two. An allowlist
    would only refuse a NEW undeclared node; exact equality also refuses a node
    that quietly stops being declared, and it forces the number down in a reviewed
    one-line diff as the payloads are written. Same shape and same reasoning as
    ``engine.unresolved_sources``.
    """
    nodes = read("node-specs.json")["nodes"]
    undeclared = [n["fn"] for n in nodes if n["output_keys"]["status"] == "undeclared"]
    declared = [n["fn"] for n in nodes if n["output_keys"]["status"] == "declared"]
    owed = _inventory("engine", "undeclared_output_keys")
    assert len(undeclared) + len(declared) == len(nodes)
    assert declared, "no node declares its payload; the containment gate compares nothing"
    assert len(undeclared) == owed, (
        f"{len(undeclared)} node(s) have not written down what their payload "
        f"contains, and engine.undeclared_output_keys says {owed}. Re-run the "
        f"command in the 'commands' block and move the number in its own diff -- "
        f"DOWNWARD, which is the only direction this constant is meant to travel."
    )


def test_the_containment_check_compares_the_cards_it_can() -> None:
    """The denominator is a MEASUREMENT, so the gate cannot pass over an empty set.

    ``check_output_key_containment`` returns how many cards it actually compared
    -- those with at least one declared function -- and refuses zero. Asserting
    that count against the committed catalogue is what stops the gate decaying
    into a loop that skips every card and reports success.
    """
    cards = read("method-cards.json")["cards"]
    nodes = read("node-specs.json")["nodes"]
    assert len(cards) == _inventory("artifacts", "n_cards")
    compared = G.check_output_key_containment(cards, nodes)
    declared = sum(1 for n in nodes if n["output_keys"]["status"] == "declared")
    assert 0 < compared <= len(cards)
    assert compared <= declared, (
        "more cards were compared than there are declared nodes to compare them "
        "against; the two counts describe the same declarations"
    )


def test_a_card_naming_a_field_its_declared_node_lacks_is_refused() -> None:
    """THE POSITIVE CONTROL. Planted, because a gate nobody watched fail is a hope.

    The containment direction is one-way on purpose -- a declared key the card
    never mentioned is fine -- so the only thing this can catch is a card naming a
    field its own declared node does not carry. That contradiction is planted here
    rather than argued about.
    """
    nodes = read("node-specs.json")["nodes"]
    declared = next(n for n in nodes if n["output_keys"]["status"] == "declared")
    card = {
        "id": 9999,
        "tool_fns": [declared["fn"]],
        "output_key_fields": ["a_field_no_node_carries: and its description"],
    }
    with pytest.raises(SystemExit, match="a_field_no_node_carries"):
        G.check_output_key_containment([card], nodes)


def test_the_containment_check_never_parses_a_prose_entry() -> None:
    """THE NEGATIVE CONTROL. 627 of the 2627 entries are sentences, not names.

    A sentence turned into a field name by a regular expression is a payload key
    nobody wrote down, so an entry that does not open with ``name: value`` is
    passed over rather than guessed at. Without this the gate would invent a field
    and then demand that a node declare it.
    """
    nodes = read("node-specs.json")["nodes"]
    declared = next(n for n in nodes if n["output_keys"]["status"] == "declared")
    card = {
        "id": 9999,
        "tool_fns": [declared["fn"]],
        "output_key_fields": [
            "The frame carries one row per observation and one column per series.",
            "Whether the test rejected at the requested level.",
        ],
    }
    assert G.check_output_key_containment([card], nodes) == 1


def test_the_prose_share_of_the_card_entries_is_the_measured_one() -> None:
    """The split the seeding rule rests on, asserted rather than remembered.

    ``FIELD_ENTRY`` reads 2000 of the 2627 committed entries and never the other
    627, and the decision to seed 142 nodes rather than 543 rests on that split. A
    catalogue edit that turned most of the prose into parseable names would make
    the debt mechanically closable, and this says so loudly instead of leaving the
    seeding rule looking arbitrary for ever.
    """
    cards = read("method-cards.json")["cards"]
    entries = [e for c in cards for e in (c["output_key_fields"] or [])]
    parseable = [e for e in entries if G.FIELD_ENTRY.match(e)]
    assert len(entries) == 2627, len(entries)
    assert len(parseable) == 2000, len(parseable)
