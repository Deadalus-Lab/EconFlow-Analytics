# SPDX-License-Identifier: AGPL-3.0-only
"""EconFlow Analytics platform integration layer.

Specified, not built. No integration code exists here yet, and none of the
Galaxy work this layer will carry has started.

This package exists now, empty, for one reason: the import-linter contract
"No statistic is ever computed outside engine/" needs a root package to resolve
against. An unresolvable contract does not fail — it is skipped, and a skipped
boundary check is indistinguishable from a passing one.
"""

__all__: list[str] = []
