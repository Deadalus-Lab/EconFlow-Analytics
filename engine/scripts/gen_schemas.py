#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""artifacts/node-specs.v1.json -> src/econflow_engine/generated/**.

Runs on the standard library alone. ONE input: the committed artifact. No
network, no ``eval`` -- building the engine never needs the
engine installed.

THREE TIERS, because the descriptions are roughly 80% of the artifact and a
worker executing a graph needs none of them:

    manifest.py          tier 1: 913 entries, NO descriptions, plus the
                         vocabulary block the allowlists read.
    args/<cat>.py  x30   tier 2: NodeMeta + the pydantic models + defaults.
    docs/<cat>.py  x30   tier 3: descriptions + input_example.

``contract_hash`` is COPIED VERBATIM from the artifact. It is computed over the
node's structural contract when the artifact is written, never here: this tier is
emitted FROM the contract and must not be able to restate it.

Modes:
    (default)   emit into src/econflow_engine/generated/
    --check     emit into a temporary directory and diff; exit 1 on any drift.
                Also re-asserts that every node's argument NAMES and ORDER still
                match the artifact.
"""

from __future__ import annotations

import argparse
import filecmp
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Any

ENGINE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE_ROOT / "src"))

from econflow_engine.naming import category_package  # noqa: E402  (after sys.path)

ARTIFACT_PATH = ENGINE_ROOT / "artifacts" / "node-specs.v1.json"
OUT_ROOT = ENGINE_ROOT / "src" / "econflow_engine" / "generated"

_IDENT_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def banner(source: str) -> str:
    return (
        "# SPDX-License-Identifier: AGPL-3.0-only\n"
        "# ============================================================\n"
        "# GENERATED FILE -- DO NOT EDIT.\n"
        f"# Source: artifacts/{source} (committed) via scripts/gen_schemas.py.\n"
        "# Rebuild with: python scripts/gen_schemas.py\n"
        "# ============================================================\n"
    )


def lit(value: Any) -> str:
    """Deterministic Python literal for a JSON-decoded value."""
    return repr(value)


def _tuple_lit(values: list[Any] | None) -> str:
    if values is None:
        return "None"
    if not values:
        return "()"
    return "(" + "".join(f"{lit(v)}, " for v in values) + ")"


def executability_lit(node: dict[str, Any]) -> str:
    e = node["executability"]
    return (
        "NodeExecutabilityMeta("
        f"status={lit(e['status'])}, "
        f"reason_code={lit(e['reason_code'])}, "
        f"reason={lit(e['reason'])}, "
        f"blocked_arg={lit(e['blocked_arg'])})"
    )


def register_field(node: dict[str, Any]) -> Any:
    reg = node.get("register")
    return None if reg is None else reg.get("field")


def arg_lit(arg: dict[str, Any]) -> str:
    parts = [
        f"name={lit(arg['name'])}",
        f"kind={lit(arg['kind'])}",
        f"required={lit(bool(arg['required']))}",
    ]
    if arg.get("enum") is not None:
        parts.append(f"enum={_tuple_lit(arg['enum'])}")
    if arg.get("allowed_vars") is not None:
        parts.append(f"allowed_vars={_tuple_lit(arg['allowed_vars'])}")
    return "NodeArgMeta(" + ", ".join(parts) + ")"


def defaults_lit(node: dict[str, Any]) -> str:
    entries = [
        f"{lit(a['name'])}: {lit(a['default'])}"
        for a in node["arguments"]
        if a.get("has_default")
    ]
    return "{}" if not entries else "{" + ", ".join(entries) + "}"


def node_description(node: dict[str, Any]) -> str:
    base = (
        f"{node['fn']} -- category {node['category']}, "
        f"METHOD-SELECTION card #{node['card_id']}."
    )
    reason = node["executability"]["reason"]
    if reason is None:
        return base
    return f"{base} [{node['executability']['status']}] {reason}"


def write(root: Path, relative: str, body: str) -> None:
    target = root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")


def emit_manifest(root: Path, artifact: dict[str, Any], artifact_sha256: str) -> None:
    lines = [
        banner("node-specs.v1.json"),
        '"""Tier 1: routing and palette data -- no descriptions, no imports.',
        "",
        "This module deliberately imports NOTHING. `econflow_engine.mcp.allowlists`",
        "reads the vocabulary from here, and `kinds` reads the allowlists, so any",
        "import of `kinds` from this file would close a cycle.",
        '"""',
        "",
        "from typing import Any",
        "",
        "#: Identity of the contract artifact this tier was emitted from.",
        "ENGINE_INFO: dict[str, Any] = {",
        f"    'n_nodes': {lit(artifact['engine']['n_nodes'])},",
        f"    'n_categories': {lit(artifact['engine']['n_categories'])},",
        f"    'artifact_sha256': {lit(artifact_sha256)},",
        "}",
        "",
        "#: The closed vocabularies, copied verbatim from the artifact.",
        f"VOCABULARY: dict[str, Any] = {lit(artifact['vocabulary'])}",
        "",
        "#: Tier 1 entries, keyed by node function name.",
        "MANIFEST: dict[str, dict[str, Any]] = {",
    ]
    for node in artifact["nodes"]:
        arg_names = [a["name"] for a in node["arguments"]]
        arg_kinds = [a["kind"] for a in node["arguments"]]
        lines.append(
            f"    {lit(node['fn'])}: {{"
            f"'fn': {lit(node['fn'])}, "
            f"'category': {lit(node['category'])}, "
            f"'card_id': {lit(node['card_id'])}, "
            f"'contract_hash': {lit(node['contract_hash'])}, "
            f"'register_field': {lit(register_field(node))}, "
            f"'executability': {lit(node['executability'])}, "
            f"'memory_class': {lit(node['memory_class'])}, "
            f"'cacheability': {lit(node['cacheability'])}, "
            f"'arg_names': {_tuple_lit(arg_names)}, "
            f"'arg_kinds': {_tuple_lit(arg_kinds)}}},"
        )
    lines.append("}")
    write(root, "manifest.py", "\n".join(lines))


def emit_args(root: Path, category: str, nodes: list[dict[str, Any]]) -> None:
    module = category_package(category)
    lines = [
        banner("node-specs.v1.json"),
        f'"""Tier 2 for category {category} -- {len(nodes)} nodes. No descriptions."""',
        "",
        "from functools import cache",
        "",
        "from pydantic import BaseModel",
        "",
        "from econflow_engine.kinds import (",
        "    NodeArgMeta,",
        "    NodeExecutabilityMeta,",
        "    NodeMeta,",
        "    build_authoring_model,",
        "    build_wire_model,",
        ")",
        "",
        "NODE_META: dict[str, NodeMeta] = {",
    ]
    for node in nodes:
        args = "".join(f"        {arg_lit(a)},\n" for a in node["arguments"])
        lines.append(
            f"    {lit(node['fn'])}: NodeMeta(\n"
            f"        fn={lit(node['fn'])},\n"
            f"        category={lit(node['category'])},\n"
            f"        card_id={lit(node['card_id'])},\n"
            f"        contract_hash={lit(node['contract_hash'])},\n"
            f"        register_field={lit(register_field(node))},\n"
            f"        executability={executability_lit(node)},\n"
            f"        memory_class={lit(node['memory_class'])},\n"
            f"        args=(\n{args}        ),\n"
            f"        defaults={defaults_lit(node)},\n"
            "    ),"
        )
    lines += [
        "}",
        "",
        "#: Argument defaults, for FORM PREFILL ONLY. A default must never be sent",
        "#: explicitly on the wire: adapt_args assigns it RAW, bypassing coercion.",
        "DEFAULTS: dict[str, dict[str, object]] = {",
    ]
    for node in nodes:
        lines.append(f"    {lit(node['fn'])}: {defaults_lit(node)},")
    lines += [
        "}",
        "",
        "",
        "@cache",
        "def wire_model(fn: str) -> type[BaseModel]:",
        '    """The model the ENGINE validates. Built on first use and cached."""',
        "    return build_wire_model(NODE_META[fn])",
        "",
        "",
        "@cache",
        "def authoring_model(fn: str) -> type[BaseModel]:",
        '    """The model a GRAPH EDITOR edits. Built on first use and cached."""',
        "    return build_authoring_model(NODE_META[fn])",
    ]
    write(root, f"args/{module}.py", "\n".join(lines))


def emit_docs(root: Path, category: str, nodes: list[dict[str, Any]]) -> None:
    module = category_package(category)
    lines = [
        banner("node-specs.v1.json"),
        f'"""Tier 3 for category {category}: descriptions and input examples.',
        "",
        "A worker executing a graph must NOT import from here -- this tier is",
        "roughly 80% of the artifact and none of it is needed to run a node.",
        '"""',
        "",
        "from typing import Any",
        "",
        "NODE_DOCS: dict[str, dict[str, Any]] = {",
    ]
    for node in nodes:
        arg_docs = ", ".join(
            f"{lit(a['name'])}: {lit(a.get('description') or '')}" for a in node["arguments"]
        )
        lines.append(
            f"    {lit(node['fn'])}: {{\n"
            f"        'fn': {lit(node['fn'])},\n"
            f"        'description': {lit(node_description(node))},\n"
            f"        'args': {{{arg_docs}}},\n"
            f"        'input_example': {lit(node['input_example'])},\n"
            "    },"
        )
    lines.append("}")
    write(root, f"docs/{module}.py", "\n".join(lines))


# The generated tier used to emit its own `.gitignore` containing `*`, on the
# reasoning that the reviewed diff is the JSON artifact. That was wrong here, and
# in two ways. The root `.gitignore` states the opposite in as many words -- the
# tier is committed deliberately, because the generated Python IS the reviewed
# form when the JSON input can no longer be regenerated. And the pattern ignored
# the whole directory, so the engine would have shipped without it and the SPDX
# gate would then have scanned a short tree against its floor and failed. One
# line, three failures. The tier is tracked; nothing writes an ignore rule here.


def emit_package_inits(root: Path, categories: list[str]) -> None:
    write(
        root,
        "__init__.py",
        banner("node-specs.v1.json")
        + '"""Machine-emitted node schemas. Gitignored: the reviewed diff is the JSON."""\n',
    )
    for tier, blurb in (("args", "Tier 2 modules, one per category."), ("docs", "Tier 3 modules.")):
        listing = "".join(f"    {lit(category_package(c))},\n" for c in categories)
        write(
            root,
            f"{tier}/__init__.py",
            banner("node-specs.v1.json")
            + f'"""{blurb}"""\n\nMODULES: tuple[str, ...] = (\n{listing})\n',
        )


def assert_argument_shape(artifact: dict[str, Any]) -> None:
    """Re-assert the invariants the emitted code silently depends on."""
    if artifact["artifact_version"] != 1:
        raise SystemExit(f"gen_schemas: unknown artifact_version {artifact['artifact_version']}.")
    nodes = artifact["nodes"]
    if len(nodes) != artifact["engine"]["n_nodes"]:
        raise SystemExit("gen_schemas: node count disagrees with engine.n_nodes.")
    kinds = set(artifact["vocabulary"]["kinds"])
    seen: set[str] = set()
    for node in nodes:
        fn = node["fn"]
        if not _IDENT_RE.match(fn):
            raise SystemExit(f"gen_schemas: fn {fn!r} is not a valid Python identifier.")
        if fn in seen:
            raise SystemExit(f"gen_schemas: duplicate fn {fn!r}.")
        seen.add(fn)
        names = [a["name"] for a in node["arguments"]]
        if len(names) != len(set(names)):
            raise SystemExit(f"gen_schemas: {fn} has duplicate argument names.")
        for a in node["arguments"]:
            if a["kind"] not in kinds:
                raise SystemExit(f"gen_schemas: {fn}.{a['name']} has kind {a['kind']!r}.")
            if a["kind"] == "enum":
                values = a.get("enum")
                if not values:
                    raise SystemExit(f"gen_schemas: {fn}.{a['name']} is an enum without values.")
                if any(not isinstance(v, str) for v in values):
                    raise SystemExit(
                        f"gen_schemas: {fn}.{a['name']} has non-string enum values. "
                        "The wire model builds a Literal of strings; teach it the new type "
                        "explicitly rather than letting it coerce."
                    )


def assert_generated_matches(artifact: dict[str, Any], root: Path) -> None:
    """Assert that the EMITTED argument names and order still match the artifact.

    Read back from the emitted TEXT rather than by importing it: a --check run
    must not depend on the package being importable, and a reordered tuple is
    exactly the drift this catches.
    """
    manifest_text = (root / "manifest.py").read_text(encoding="utf-8")
    for node in artifact["nodes"]:
        expected = _tuple_lit([a["name"] for a in node["arguments"]])
        needle = f"{lit(node['fn'])}: {{'fn': {lit(node['fn'])}"
        if needle not in manifest_text:
            raise SystemExit(f"gen_schemas --check: {node['fn']} is absent from the manifest.")
        if f"'arg_names': {expected}" not in manifest_text:
            raise SystemExit(
                f"gen_schemas --check: argument names/order drifted for {node['fn']}."
            )


def generate(root: Path, artifact: dict[str, Any], artifact_sha256: str) -> list[str]:
    by_category: dict[str, list[dict[str, Any]]] = {}
    for node in artifact["nodes"]:
        by_category.setdefault(node["category"], []).append(node)
    categories = list(by_category)
    if len(categories) != artifact["engine"]["n_categories"]:
        raise SystemExit("gen_schemas: category count disagrees with engine.n_categories.")

    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    emit_manifest(root, artifact, artifact_sha256)
    emit_package_inits(root, categories)
    for category in categories:
        emit_args(root, category, by_category[category])
        emit_docs(root, category, by_category[category])
    return categories


def _emitted_files(root: Path) -> set[str]:
    """Every file the generator OWNS, ignoring interpreter bytecode.

    Importing the generated package leaves __pycache__ behind; it is a runtime
    side effect, not an emitted artifact, and counting it as drift makes --check
    fail on any machine that has run the tests.
    """
    return {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
    }


def diff_trees(expected: Path, actual: Path) -> list[str]:
    drift: list[str] = []
    left = _emitted_files(expected)
    right = _emitted_files(actual)
    drift += [f"only in the regenerated tree: {p}" for p in sorted(left - right)]
    drift += [f"only on disk (stale): {p}" for p in sorted(right - left)]
    for rel in sorted(left & right):
        if not filecmp.cmp(expected / rel, actual / rel, shallow=False):
            drift.append(f"content differs: {rel}")
    return drift


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="regenerate into a temporary directory and fail on any drift",
    )
    args = parser.parse_args()

    raw = ARTIFACT_PATH.read_bytes()
    artifact_sha256 = hashlib.sha256(raw).hexdigest()
    artifact = json.loads(raw.decode("utf-8"))
    assert_argument_shape(artifact)

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / "generated"
            categories = generate(fresh, artifact, artifact_sha256)
            assert_generated_matches(artifact, fresh)
            if not OUT_ROOT.exists():
                print("gen_schemas --check: generated/ is missing; run the generator.")
                return 1
            drift = diff_trees(fresh, OUT_ROOT)
        if drift:
            print("gen_schemas --check: DRIFT")
            for line in drift:
                print(f"  {line}")
            return 1
        print(
            f"gen_schemas --check: OK -- {len(artifact['nodes'])} nodes / "
            f"{len(categories)} categories, artifact sha256 {artifact_sha256[:12]}"
        )
        return 0

    categories = generate(OUT_ROOT, artifact, artifact_sha256)
    assert_generated_matches(artifact, OUT_ROOT)
    print(
        f"gen_schemas: {len(artifact['nodes'])} nodes / {len(categories)} categories "
        f"-> src/econflow_engine/generated (artifact sha256 {artifact_sha256[:12]})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
