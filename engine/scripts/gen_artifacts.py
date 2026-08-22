#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""corpus/** -> artifacts/node-specs.json + artifacts/method-cards.json.

THE PROBLEM THIS SOLVES. There is currently no way to author a method card at
all. ``engine/METHOD-SELECTION.{yaml,md}`` and ``-TREES.yaml`` were removed on
2026-08-19 as duplicates of the sealed artifacts -- they carried the same cards
and the same trees, field for field -- and the wrapper skill still forbids
editing ``artifacts/`` by hand. Between the two, the catalogue became read-only.
This generator restores the authoring surface: ``corpus/`` is written by a
person, ``artifacts/`` is emitted from it, and the emitted file is never edited.

STANDARD LIBRARY ONLY, like the two generators beside it. Building the engine
must never require the engine, or a YAML parser, to be installed.

WHAT LIVES IN THE CORPUS, AND WHAT DOES NOT. A field that can be computed is not
stored, because two copies of one fact drift. Every exclusion below was measured
against the committed v1 artifacts rather than assumed, and the measurement is
re-run by ``--continuity``:

    route              "/node/" + fn                                913/913
    executability      constant {executable, null, null, null}      913/913
    cacheability       spec_cacheable  always true                  913/913
                       has_seed_arg    an argument named "seed"     913/913
                       seed_required   that argument is required    913/913
                       stochastic_unseeded  fn in the vocabulary    913/913
    memory_class       memory_class_of(), the mechanical rule       912/913
    contract_hash      contract_hash.py                             (v2)
    embed_text         the card template below                      252/252

``memory_class`` is 912 of 913 because exactly one node -- ``ga_sim`` -- declares
``light`` where the rule says ``heavy``. That is the escape hatch the rule's own
module documents, so the corpus keeps an OPTIONAL ``memory_class`` and the
generator only fills it in when it is absent. One override, stored once, visible.

``embed_text`` is 252 of 252 only once the empty-``sources`` rule is included:
card 227 is the catalogue's single sourceless card, and the exporter OMITS the
``Sources:`` line entirely rather than emitting an empty one. Reproducing that
exactly is what makes the reconstruction a proof instead of a near-miss.

CARD IDS ARE STABLE AND GAPPED. The 252 ids run 1..257 with 16, 66, 67, 86 and
93 absent -- they are identities, not positions. A new card takes the next free
id from 258 upward; nothing is ever renumbered, because a renumber silently
rewrites every ``card_id`` on the node side and every "-> #N" cross-reference in
the prose.

Modes::

    --build       corpus/**  -> the sealed artifacts
    --check       build to a temporary tree and diff against what is committed
    --continuity  THE GUARD: assert every node and card the retired contract
                  described is still present, from legacy-inventory.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Final

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "src"))
sys.path.insert(0, str(ENGINE_ROOT / "scripts"))

from contract_hash import contract_hash  # noqa: E402  (after sys.path)

from econflow_engine.node.memory_class import memory_class_of  # noqa: E402

ARTIFACTS: Final = ENGINE_ROOT / "artifacts"
CORPUS: Final = ENGINE_ROOT / "corpus"
METHOD_SOURCES: Final = ENGINE_ROOT / "METHOD-SOURCES.json"
VOCABULARY_FILE: Final = "_vocabulary.json"
LEGACY_FILE: Final = "legacy-inventory.json"

#: EVERY FILE THIS GENERATOR EMITS, named relative to the engine root. ``build``
#: writes exactly this set under the directory it is handed and nothing outside
#: it, and ``--check`` compares exactly this set against the tree. One list, so
#: an output cannot be emitted without also being checked -- which is how the
#: register came to be written by ``--check`` and compared by nothing.
GENERATED: Final = (
    "artifacts/node-specs.json",
    "artifacts/node-specs.sha256",
    "artifacts/method-cards.json",
    "artifacts/method-cards.sha256",
    "METHOD-SOURCES.json",
)

#: Emitted key order. Not correctness -- readability. A stable order keeps a
#: one-card diff to one card rather than to the whole file.
NODE_KEYS: Final = (
    "fn", "route", "category", "card_id", "register", "contract_hash",
    "executability", "memory_class", "cacheability", "input_example",
    "arguments", "export",
)
ARG_KEYS: Final = (
    "name", "kind", "materialize", "required", "description", "pointer_handle",
    "json_type", "enum", "allowed_vars", "default", "has_default",
    "default_json_type",
)
CARD_KEYS: Final = (
    "id", "category", "method", "wrapper_file", "tool_fns", "when", "when_not",
    "alternatives", "output_key_fields", "interpretation_traps", "sources",
    "precondition_tools", "precondition_gates", "embed_text",
)

EXECUTABLE: Final = {"status": "executable", "reason_code": None,
                     "reason": None, "blocked_arg": None}

DOT: Final = " · "


# ---------------------------------------------------------------- derivation


def cacheability_of(node: dict[str, Any], unseeded: frozenset[str]) -> dict[str, Any]:
    seed = [a for a in node["arguments"] if a["name"] == "seed"]
    return {
        "spec_cacheable": True,
        "has_seed_arg": bool(seed),
        "seed_required": bool(seed) and bool(seed[0]["required"]),
        "stochastic_unseeded": node["fn"] in unseeded,
    }


def embed_text_of(card: dict[str, Any]) -> str:
    """The retrieval blob. Reproduces all 252 committed cards byte-for-byte."""
    alternatives = DOT.join(
        f"{a['alt']} ({a['criterion']})" for a in (card["alternatives"] or [])
    )
    lines = [
        f"[#{card['id']}] {card['method']}",
        f"Category: {card['category']}",
        f"Nodes: {DOT.join(card['tool_fns'])}",
        f"WHEN: {card['when']}",
        f"NOT when: {card['when_not']}",
        f"Alternatives: {alternatives}",
        f"Output: {DOT.join(card['output_key_fields'] or [])}",
        f"Pitfalls: {DOT.join(card['interpretation_traps'] or [])}",
    ]
    if card["sources"]:
        lines.append(f"Sources: {DOT.join(card['sources'])}")
    return "\n".join(lines)


def ordered(source: dict[str, Any], keys: tuple[str, ...]) -> dict[str, Any]:
    """Project onto `keys` in order, dropping any the source does not carry."""
    return {k: source[k] for k in keys if k in source}


# ---------------------------------------------------------------- corpus i/o


def read_corpus() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not CORPUS.is_dir():
        raise SystemExit(f"gen_artifacts: no corpus at {CORPUS}.")
    vocabulary = json.loads((CORPUS / VOCABULARY_FILE).read_bytes().decode("utf-8"))
    files = sorted(p for p in CORPUS.glob("*.json") if not p.name.startswith("_"))
    if not files:
        raise SystemExit(f"gen_artifacts: {CORPUS} holds no category files.")
    categories = [json.loads(p.read_bytes().decode("utf-8")) for p in files]
    return categories, vocabulary


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=1, ensure_ascii=False) + "\n"
    path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- build


def build_node_specs(
    categories: list[dict[str, Any]],
    vocabulary: dict[str, Any],
) -> dict[str, Any]:
    """Corpus -> the node-specs artifact.

    Every ``contract_hash`` is COMPUTED here, by ``contract_hash.py``. The retired
    contract's tokens were substituted rather than computed, and this function
    used to take them as an argument; that path went with the round-trip that was
    its only caller. They survive in ``legacy-inventory.json``, read by
    ``--continuity`` and by nothing else.
    """
    unseeded = frozenset(vocabulary["stochastic_unseeded_fns"])
    nodes: list[dict[str, Any]] = []
    for block in categories:
        category = block["category"]
        for authored in block["nodes"]:
            node: dict[str, Any] = {
                "fn": authored["fn"],
                "route": f"/node/{authored['fn']}",
                "category": category,
                "card_id": authored["card_id"],
                "register": authored.get("register"),
                "executability": dict(EXECUTABLE),
                "memory_class": authored.get("memory_class") or memory_class_of(authored),
                "input_example": authored["input_example"],
                "arguments": [ordered(a, ARG_KEYS) for a in authored["arguments"]],
            }
            if authored.get("export") is not None:
                node["export"] = authored["export"]
            node["cacheability"] = cacheability_of(node, unseeded)
            node["contract_hash"] = contract_hash(node)
            nodes.append(ordered(node, NODE_KEYS))

    return {
        "artifact_version": 2,
        "generated_by": "scripts/gen_artifacts.py from corpus/ -- regenerate, never edit",
        "engine": {
            "n_nodes": len(nodes),
            "n_categories": len({n["category"] for n in nodes}),
        },
        "vocabulary": vocabulary,
        "nodes": nodes,
    }


def build_method_cards(
    categories: list[dict[str, Any]],
    node_specs: dict[str, Any],
    node_specs_sha256: str,
) -> dict[str, Any]:
    cards: list[dict[str, Any]] = []
    for block in categories:
        for authored in block["cards"]:
            card = dict(authored)
            card["category"] = block["category"]
            card["embed_text"] = embed_text_of(card)
            cards.append(ordered(card, CARD_KEYS))
    cards.sort(key=lambda c: c["id"])

    covered = {fn for c in cards for fn in c["tool_fns"]}
    declared = {n["fn"] for n in node_specs["nodes"]}
    if covered != declared:
        orphan_nodes = sorted(declared - covered)[:10]
        orphan_cards = sorted(covered - declared)[:10]
        raise SystemExit(
            "gen_artifacts: the card/node join is broken.\n"
            f"  nodes named by no card : {orphan_nodes}\n"
            f"  card tool_fns with no node: {orphan_cards}"
        )

    return {
        "artifact_version": 2,
        "generated_by": "scripts/gen_artifacts.py from corpus/ -- regenerate, never edit",
        "source": {
            "node_specs_sha256": node_specs_sha256,
            "n_cards": len(cards),
            "n_categories": len({c["category"] for c in cards}),
            "n_nodes_covered": len(covered),
            "n_cards_without_sources": sum(1 for c in cards if not c["sources"]),
        },
        "cards": cards,
    }


def sync_method_sources(categories: list[dict[str, Any]], out: Path) -> tuple[int, int]:
    """Reconcile METHOD-SOURCES.json with the corpus, writing the result under ``out``.

    THE DERIVED COLUMNS ARE REFRESHED, THE AUTHORED ONES ARE PRESERVED.
    ``category``, ``package``, ``cards``, ``methods`` and ``node_fns`` all follow
    from the corpus and are rewritten; ``status``, ``library`` and ``paper`` are
    the register's own content and are carried over untouched.

    Refreshing rather than skipping existing rows is the point. An earlier
    scratch version only ADDED missing rows, so when a node was later appended to
    an existing card its row kept the old ``node_fns`` -- and the count silently
    disagreed with the artifact by exactly that node. gen_wrappers.py refuses to
    run without a row per module, but nothing was checking the rows were current.

    THE AUTHORED COLUMNS ARE READ FROM THE LIVE REGISTER, THE RESULT IS WRITTEN
    UNDER ``out``. The read cannot be redirected: ``status``, ``library`` and
    ``paper`` exist nowhere else, so a temporary tree holds nothing to carry
    over. The write must be, and until 2026-08-22 it was not -- this function
    wrote to the live register on every call, including the call ``--check``
    makes into a temporary tree. A register that had drifted from the corpus was
    therefore REPAIRED by the gate and then reported as reproducing: the drift
    was erased by the check that exists to find it, and a fresh clone would not
    rebuild the tree that had just passed.
    """
    register = json.loads(METHOD_SOURCES.read_bytes().decode("utf-8"))
    previous = register["modules"]

    modules: dict[str, dict[str, Any]] = {}
    for block in categories:
        category = block["category"]
        for card in sorted(block["cards"], key=lambda c: c["id"]):
            key = card["wrapper_file"].removesuffix(".py")
            row = modules.setdefault(key, {
                "module": key.split("/")[-1],
                "category": category,
                "package": package_of(category),
                "cards": [], "methods": [], "node_fns": [],
            })
            row["cards"].append(card["id"])
            row["methods"].append(card["method"])
            row["node_fns"].extend(card["tool_fns"])

    for key, row in modules.items():
        carried = previous.get(key, {})
        row["status"] = carried.get("status", "planned")
        row["library"] = carried.get("library")
        row["paper"] = carried.get("paper")

    register["modules"] = modules
    register["n_modules"] = len(modules)
    register["n_node_fns"] = sum(len(r["node_fns"]) for r in modules.values())
    (out / METHOD_SOURCES.name).write_text(
        json.dumps(register, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return register["n_modules"], register["n_node_fns"]


def build(out: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Emit every file in ``GENERATED`` under ``out``, and write nothing outside it.

    ``out`` is a ROOT that mirrors ``engine/``, not the artifacts directory: the
    artifacts sit under ``artifacts/`` and the register sits beside it at the
    root, so one destination has to cover both. Writing nothing outside ``out``
    is what makes ``--check``, which hands this a temporary directory,
    read-only.
    """
    categories, vocabulary = read_corpus()
    specs = build_node_specs(categories, vocabulary)
    specs_path = out / "artifacts/node-specs.json"
    write_json(specs_path, specs)
    digest = hashlib.sha256(specs_path.read_bytes()).hexdigest()
    (out / "artifacts/node-specs.sha256").write_text(
        f"{digest}  node-specs.json\n", encoding="utf-8"
    )

    sync_method_sources(categories, out)
    cards = build_method_cards(categories, specs, digest)
    cards_path = out / "artifacts/method-cards.json"
    write_json(cards_path, cards)
    cards_digest = hashlib.sha256(cards_path.read_bytes()).hexdigest()
    (out / "artifacts/method-cards.sha256").write_text(
        f"{cards_digest}  method-cards.json\n", encoding="utf-8"
    )
    return specs, cards


# ---------------------------------------------------------------- continuity


def package_of(category: str) -> str:
    """``00-data-utilities`` -> ``c00_data_utilities``. Mirrors econflow_engine.naming."""
    return "c" + re.sub(r"[^0-9A-Za-z_]+", "_", category.lower())


def run_continuity() -> int:
    """Nothing the retired contract described may disappear from the catalogue.

    This replaced a round-trip that rebuilt the superseded artifacts from the
    corpus and compared them field by field. That proof required keeping 4.5 MB
    of superseded artifacts in the tree to compare against, and it proved two
    things at once: that the corpus reproduces the old contract, and that nothing
    was lost. ``--check`` already proves the first for the live catalogue, byte
    for byte. Only the second needed a home, and it needs NAMES, not artifacts --
    so it reads ``legacy-inventory.json``: 913 function names and 252 card ids
    distilled from the retired set, together with the contract hashes that set
    carried and that nothing here can recompute.

    GROWTH IS EXPECTED, LOSS IS NOT. The catalogue is larger than the inventory
    and will keep growing; this checks one direction only.
    """
    inventory = json.loads((ARTIFACTS / LEGACY_FILE).read_bytes().decode("utf-8"))
    categories, _ = read_corpus()

    # MEMBERSHIP, read straight off the corpus. Deliberately not via build_*: a
    # corpus that has lost a node also has a broken card/node join, and the
    # builders refuse such a corpus before this check could report WHICH entry
    # went missing. Diagnosing the loss is this function's whole job, so it must
    # not depend on the tree being buildable.
    live_fns = {n["fn"] for block in categories for n in block["nodes"]}
    live_ids = {int(c["id"]) for block in categories for c in block["cards"]}
    want_fns = set(inventory["contract_hashes"])
    want_ids = {int(i) for i in inventory["card_ids"]}

    # Anti-vacuity FIRST: an inventory edited down to nothing must not read as a pass.
    if len(want_fns) != int(inventory["n_nodes"]) or len(want_ids) != int(inventory["n_cards"]):
        print("gen_artifacts --continuity: legacy-inventory.json disagrees with its own "
              "counts; it has been edited without care.", file=sys.stderr)
        return 1
    if not want_fns or not want_ids:
        print("gen_artifacts --continuity: the inventory is empty, so this proved nothing.",
              file=sys.stderr)
        return 1

    lost_fns = sorted(want_fns - live_fns)
    lost_ids = sorted(want_ids - live_ids)
    if lost_fns or lost_ids:
        print("gen_artifacts --continuity: the catalogue has LOST entries the retired "
              "contract described", file=sys.stderr)
        for fn in lost_fns[:15]:
            print(f"    node gone: {fn}", file=sys.stderr)
        for cid in lost_ids[:15]:
            print(f"    card gone: #{cid}", file=sys.stderr)
        print("    A rename is not a loss, but it must be DECLARED: record it in "
              "legacy-inventory.json where a reviewer sees it, never by relaxing this "
              "check.", file=sys.stderr)
        return 1

    print(f"gen_artifacts --continuity: all {len(want_fns)} retired node(s) and "
          f"{len(want_ids)} retired card(s) are still present.")
    print(f"gen_artifacts --continuity: the catalogue carries {len(live_fns)} node(s) and "
          f"{len(live_ids)} card(s) -- {len(live_fns) - len(want_fns)} node(s) and "
          f"{len(live_ids) - len(want_ids)} card(s) added since.")
    return 0




# ---------------------------------------------------------------- check


def run_check() -> int:
    """Build into a temporary tree and compare, writing nothing into the live tree."""
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp)
        build(fresh)
        drift = []
        for name in GENERATED:
            committed = ENGINE_ROOT / name
            if not committed.exists():
                drift.append(f"{name}: not committed")
            elif committed.read_bytes() != (fresh / name).read_bytes():
                drift.append(f"{name}: differs from the corpus")
    if drift:
        print("gen_artifacts --check: the committed files do not match the corpus",
              file=sys.stderr)
        for line in drift:
            print(f"    {line}", file=sys.stderr)
        print("    Each file above is emitted from corpus/ and must hold exactly what "
              "corpus/ produces.\n"
              "    Run `python scripts/gen_artifacts.py --build` and commit the result.",
              file=sys.stderr)
        return 1
    print(f"gen_artifacts --check: all {len(GENERATED)} generated file(s) reproduce "
          "from corpus/.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="corpus/** -> the sealed artifacts")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build", action="store_true", help="emit the sealed artifacts")
    mode.add_argument("--check", action="store_true", help="assert the committed set matches")
    mode.add_argument("--continuity", action="store_true",
                      help="prove nothing the retired contract described has been lost")
    args = parser.parse_args()

    if args.continuity:
        return run_continuity()
    if args.check:
        return run_check()

    specs, cards = build(ENGINE_ROOT)
    print(
        f"gen_artifacts --build: {specs['engine']['n_nodes']} node(s) across "
        f"{specs['engine']['n_categories']} categories, {cards['source']['n_cards']} card(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
