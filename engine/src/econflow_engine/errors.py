# SPDX-License-Identifier: AGPL-3.0-only
"""The closed set of rejection reasons, and the gate exception that carries one.

A REASON CODE is the machine-readable half of a 422: the human message explains,
the code lets the caller branch. The set is CLOSED and is the same on both sides
of the wire -- it is asserted against ``artifacts/parity-fixtures.json``
(``reason_codes``) by the parity suite.

WHY THIS MODULE IS SEPARATE from :mod:`econflow_engine.kinds`: the pointer gates
in :mod:`econflow_engine.node.store_pointers` raise reason-carrying errors, and
``kinds`` imports those gates. Reason codes therefore have to sit below both.
"""

from __future__ import annotations

from typing import Final, Literal

__all__ = ["ENGINE_REASON_CODES", "EngineReasonCode", "GateError"]

EngineReasonCode = Literal[
    "unknown-args",
    "missing-required",
    "handle-not-string",
    "enum-invalid",
    "formula-not-string",
    "formula-parse",
    "formula-multi-expr",
    "formula-not-tilde",
    "formula-denied-call",
    "formula-bad-head",
    "formula-bad-var",
    "formula-depth",
    "forecastfn-unknown",
    "pointer-malformed",
    "pointer-traversal",
    "pointer-no-sidecar",
    "pointer-native-not-allowed",
    "other",
]

ENGINE_REASON_CODES: Final[tuple[str, ...]] = (
    "unknown-args",
    "missing-required",
    "handle-not-string",
    "enum-invalid",
    "formula-not-string",
    "formula-parse",
    "formula-multi-expr",
    "formula-not-tilde",
    "formula-denied-call",
    "formula-bad-head",
    "formula-bad-var",
    "formula-depth",
    "forecastfn-unknown",
    "pointer-malformed",
    "pointer-traversal",
    "pointer-no-sidecar",
    "pointer-native-not-allowed",
    "other",
)


class GateError(ValueError):
    """A hard gate refusal that carries the reason code the wire contract exposes.

    ``reason_code`` is what the client branches on; ``detail_code`` keeps the
    finer diagnosis when the two differ (see the formula and path notes in
    :mod:`econflow_engine.kinds`).
    """

    __slots__ = ("detail_code", "reason_code")

    def __init__(
        self, reason_code: EngineReasonCode, message: str, detail_code: str | None = None
    ) -> None:
        super().__init__(message)
        self.reason_code: EngineReasonCode = reason_code
        self.detail_code: str = detail_code if detail_code is not None else reason_code
