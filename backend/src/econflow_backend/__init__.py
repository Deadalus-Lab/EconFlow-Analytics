# SPDX-License-Identifier: AGPL-3.0-only
"""EconFlow Analytics platform integration layer.

Specified, not built. See docs/ROADMAP.md; the Galaxy work lands in Phases 9-10.

This package exists now, empty, for one reason: the import-linter contract
"No statistic is ever computed outside engine/" needs a root package to resolve
against. An unresolvable contract does not fail — it is skipped, and a skipped
boundary check is indistinguishable from a passing one.
"""

__all__: list[str] = []
