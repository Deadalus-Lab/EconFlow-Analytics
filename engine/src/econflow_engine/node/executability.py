# SPDX-License-Identifier: AGPL-3.0-only
"""Executability tags.

WHY IT EXISTS: a frozen spec can declare an argument whose ``kind`` the adapter
converts into the WRONG type for the wrapper's own gate. The result is not an
infrastructure error but a GUARANTEED blocked-by-gate -- and the user would find
out only after paying for a store fetch and a full node execution, reading a
message that does not say the SCHEMA is at fault rather than their data.

THE REGISTRY IS EMPTY BY PROOF, not by omission. All five tags this mechanism
once carried were fixed AT THEIR SOURCE, not deleted as invalid; today all 913
nodes are executable, and the artifact says so. The mechanism stays INTACT: the
next kind-versus-gate mismatch already has its path -- one entry here becomes a
greyed-out node on the canvas and a preflight 422 before any computation.

    "non-executable"  every call is blocked; the fault is in a REQUIRED
                      argument and cannot be worked around.
    "degraded"        the node runs, but ONE argument is inert: passing it
                      explicitly hits a gate, omitting it works.

KEEP IT COMPLETE: a new spec with such a mismatch MUST be entered here, or the
node is advertised as executable when it is not.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Final

__all__ = ["EXECUTABILITY", "Executability", "executability_of", "is_non_executable"]


@dataclass(frozen=True, slots=True)
class Executability:
    status: str
    reason_code: str | None = None
    #: Human-readable and EDUCATIONAL: it says what the rule requires, why it
    #: blocks, and what the fix is. It reaches the user verbatim.
    reason: str | None = None
    blocked_arg: str | None = None


_EXECUTABLE: Final = Executability(status="executable")

#: fn -> tag. Empty by proof; see the module docstring.
EXECUTABILITY: Final[dict[str, Executability]] = {}


def executability_of(spec: Any) -> Executability:
    """Pure and total: an untagged node is executable with empty fields."""
    fn = spec.get("fn") if isinstance(spec, dict) else getattr(spec, "fn", None)
    if fn is None:
        return _EXECUTABLE
    return EXECUTABILITY.get(str(fn), _EXECUTABLE)


def is_non_executable(spec: Any) -> bool:
    """The preflight predicate. ONLY ``non-executable`` blocks.

    ``degraded`` runs normally: whether it fails depends on whether the caller
    supplied the inert argument, and that is for the wrapper's real gate to
    judge, not for us.
    """
    return executability_of(spec).status == "non-executable"
