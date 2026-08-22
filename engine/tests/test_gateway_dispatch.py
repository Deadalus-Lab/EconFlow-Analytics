# SPDX-License-Identifier: AGPL-3.0-only
"""Every node the manifest declares must be dispatchable by the gateway.

WHY THIS FILE EXISTS. ``gateway._wrapper_module_for`` resolves a node to its
wrapper module in two hops: the manifest gives it a ``card_id``, and a card index
turns that id into a ``wrapper_file``. The two sides came from different
artifacts -- the manifest from the live catalogue, the card index from a hard-coded
read of the older, smaller card set -- so 543 of 1456 nodes resolved to a
``KeyError`` on the card id. Every node added after the catalogue grew was
undispatchable, and nothing said so: the only file that touches the gateway is
the conformance suite, whose tests are skipped.

THAT IS THE HAZARD THIS FILE GUARDS. The failure is invisible from either side on
its own -- the manifest is complete, the card index is internally consistent, and
only the join between them is short. This test walks the whole manifest, so a
future artifact split cannot quietly strand a subset of the engine again.
"""

from __future__ import annotations

import pytest

from econflow_engine.generated.manifest import MANIFEST
from econflow_engine.mcp import gateway


def test_every_manifest_node_resolves_to_a_wrapper_module() -> None:
    """No node in the catalogue may fail to resolve. A KeyError here is a short join."""
    index = gateway._card_index()
    unresolvable = sorted(
        {int(entry["card_id"]) for entry in MANIFEST.values()} - set(index)
    )
    assert not unresolvable, (
        f"{len(unresolvable)} card id(s) in the manifest are absent from the card "
        f"index, so every node carrying one is undispatchable: {unresolvable[:10]}"
    )


def test_the_card_index_covers_the_whole_catalogue() -> None:
    """The index must describe at least as many cards as the catalogue declares."""
    declared = {int(e["card_id"]) for e in MANIFEST.values()}
    assert len(gateway._card_index()) >= len(declared), (
        "the card index is smaller than the set of card ids the manifest uses; "
        "it is being read from a narrower artifact than the manifest was built from"
    )


@pytest.mark.parametrize("fn", sorted(MANIFEST)[::97])
def test_a_sample_of_nodes_import_their_wrapper_module(fn: str) -> None:
    """A spread across the catalogue actually imports, not merely resolves."""
    assert gateway._wrapper_module_for(fn) is not None
