#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
"""The v2 contract hash — the one definition, used by the artifact generator.

WHY THIS IS DEFINED AND NOT RECOVERED. The v1 artifacts carry ``contract_hash``
as ``c-<64 hex>``, written by an exporter that is not in this tree. Nothing in
this repository can regenerate those values, and no future version of this engine
will be able to either. A v1 value is therefore an opaque identity token, the
same class of thing as ``engine.spec_source_sha256``: recorded, never recomputed.
A search over roughly 7.3 million candidate serialisations did not reproduce one.
It was never going to: the input is gone. The tokens survive in
``artifacts/legacy-inventory.json``, which keeps them for exactly that reason.

An algorithm nobody can run is a serial number, not a contract. So v2 computes
its own, here, from a canonical form that is written down and tested.

THE PREFIX CARRIES THE VERSION, AND THAT IS THE SAFETY PROPERTY. A v2 hash is
``c2-``; a v1 token is ``c-``. The two schemas' patterns are mutually exclusive,
so a v1 token cannot validate as v2, a v2 hash cannot validate as v1, and no
comparison between the two can silently succeed. That is the only real hazard in
replacing an opaque value with a computed one, and it is closed by construction
rather than by a convention someone has to remember.

WHAT THE HASH COVERS — the node's callable contract, and nothing else:

    fn          the node's name. Proved to matter: friedman_test, kw_test and
                qs_test carry byte-identical arguments and metadata, and v1 gave
                them three different tokens.
    arguments   in order, every field except ``description``. Order is part of
                the signature, so the list is never sorted.
    register    the field a result is registered under. Part of what the caller
                gets back, so a change to it is a change to the contract.
    export      the sink argument, format and extension of the three nodes that
                write a file. Changing what a node writes is a break for every
                caller, so it is contract rather than metadata.

THIS COVERAGE IS NOT INVENTED. It is the retired contract's own semantics,
carried over: the v1 token covered a node's function name, arguments, register
field and export field, and explicitly NOT its memory class, so that a
resource-allocation change could not invalidate a stored graph. v2 keeps that
meaning and changes only the function that computes it. Each element of the
coverage, and each exclusion, is asserted in ``tests/test_contract_hash.py``, so
the claim is checked in this tree rather than taken on trust.

The v1 digest was taken over a BINARY serialisation of that object, which is why
no amount of searching over JSON forms was ever going to reproduce it, and why
this module does not try.

WHAT IT DELIBERATELY IGNORES: ``description`` and every node-level annotation --
``route`` (derived from ``fn``), ``category``, ``card_id``, ``register``,
``memory_class``, ``executability``, ``cacheability``, ``input_example``. If
prose moved the hash, every wording fix would read as a breaking change, and a
signal that cries wolf is one reviewers stop reading.

CANONICAL FORM. Keys sorted, no whitespace, Unicode kept as Unicode, UTF-8, then
SHA-256. Sorting the keys is what makes the hash independent of the order fields
happen to sit in the corpus; not sorting the argument LIST is what keeps the
signature contractual. An absent optional field and an explicit null are the
same input, so the artifact's formatting never becomes part of the contract --
``materialize`` is present on 1 argument of 4698 and absent on the rest.

Usage::

    contract_hash.py <artifact.json>            print one `fn  hash` per line
    contract_hash.py <artifact.json> --check    recompute and compare in place
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any, Final

__all__ = ["CONTRACT_FIELDS", "PREFIX", "canonical_contract", "contract_hash"]

#: Every argument field except ``description``. Read with a default, so a field
#: the corpus omits hashes exactly as one it writes as null.
CONTRACT_FIELDS: Final[tuple[str, ...]] = (
    "name",
    "kind",
    "required",
    "json_type",
    "enum",
    "allowed_vars",
    "default",
    "has_default",
    "default_json_type",
    "pointer_handle",
    "materialize",
)

PREFIX: Final = "c2-"


def canonical_contract(node: Mapping[str, Any]) -> str:
    """The exact bytes that are hashed, as text.

    Exposed because a hash whose input cannot be inspected is not reviewable: a
    disagreement about two hashes is settled by diffing this, not by guessing.
    """
    payload = {
        "fn": node["fn"],
        "arguments": [
            {field: argument.get(field) for field in CONTRACT_FIELDS}
            for argument in node["arguments"]
        ],
        "register": node.get("register"),
        "export": node.get("export"),
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def contract_hash(node: Mapping[str, Any]) -> str:
    """``c2-`` followed by the SHA-256 of :func:`canonical_contract`."""
    digest = hashlib.sha256(canonical_contract(node).encode("utf-8")).hexdigest()
    return PREFIX + digest


def _load(path: Path) -> list[dict[str, Any]]:
    artifact = json.loads(path.read_bytes().decode("utf-8"))
    nodes: list[dict[str, Any]] = artifact["nodes"]
    if not nodes:
        raise SystemExit(f"contract_hash: {path} declares no nodes; nothing to hash.")
    return nodes


def run_check(path: Path, nodes: list[dict[str, Any]]) -> int:
    """Recompute every stored hash in place and report the first divergences.

    Refuses a retired v1 artifact outright, before comparing anything. Recomputing
    a v2 hash for every node of such a file would report a mismatch on all of
    them, and a wall of mismatches reads as a broken algorithm rather than as the
    category error it is.
    """
    stored = [n.get("contract_hash", "") for n in nodes]
    if any(s.startswith("c-") for s in stored):
        raise SystemExit(
            f"contract_hash: {path} carries retired v1 tokens. This check recomputes "
            "v2 hashes only, and it requires every stored contract_hash to begin "
            "'c2-'. A 'c-' token came from an exporter that is not in this tree and "
            "that nothing here can rerun, so it can be read but never recomputed. "
            "Run this against artifacts/node-specs.json, which is the artifact that "
            "carries v2 hashes."
        )

    mismatched = [
        (node["fn"], node.get("contract_hash", "<missing>"), contract_hash(node))
        for node in nodes
        if node.get("contract_hash") != contract_hash(node)
    ]
    if mismatched:
        print(f"contract_hash: {len(mismatched)} of {len(nodes)} node(s) diverged", file=sys.stderr)
        for fn, was, now in mismatched[:25]:
            print(f"  {fn}\n    stored     {was}\n    recomputed {now}", file=sys.stderr)
        if len(mismatched) > 25:
            print(f"  ... and {len(mismatched) - 25} more", file=sys.stderr)
        return 1

    distinct = len({contract_hash(n) for n in nodes})
    if distinct != len(nodes):
        print(
            f"contract_hash: {len(nodes) - distinct} collision(s) among {len(nodes)} nodes",
            file=sys.stderr,
        )
        return 1
    print(f"contract_hash: {len(nodes)} node(s) reproduce, all distinct.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="a node-specs artifact")
    parser.add_argument(
        "--check",
        action="store_true",
        help="recompute every stored hash and exit non-zero on any divergence",
    )
    args = parser.parse_args()

    nodes = _load(args.artifact)
    if args.check:
        return run_check(args.artifact, nodes)
    try:
        for node in nodes:
            print(f"{node['fn']}\t{contract_hash(node)}")
    except BrokenPipeError:
        # `| head` closing the pipe is the reader leaving, not a failure here.
        # Redirecting the fd stops the interpreter reporting it again at exit.
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
