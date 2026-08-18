# SPDX-License-Identifier: AGPL-3.0-only
"""EconFlow Analytics computation engine.

Layering:

* ``kinds`` -- the hand-written argument-kind contract (the heart).
* ``formula`` -- the default-deny formula allowlist (security).
* ``node`` -- store pointers, cache identity, executability, memory class.
* ``mcp`` -- the tool surface: registry, adapters, gateway, server.
* ``generated`` -- machine-emitted node schemas; committed, and regenerated
 by ``scripts/gen_schemas.py --write``.
* ``wrappers`` -- one module per method wrapper, one stub per node.
"""

__all__ = ["__version__"]

__version__ = "0.1.0"
