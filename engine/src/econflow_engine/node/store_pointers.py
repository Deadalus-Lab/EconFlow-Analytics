# SPDX-License-Identifier: AGPL-3.0-only
"""The store-pointer contract.

SOURCE OF TRUTH (read, not recalled):

``.node_is_pointer``
    a mapping carrying ``pointer_uri``, OR a scalar string beginning with
    ``store://``.
the pointer contract
    ``format`` is optional; when absent it is INFERRED from the suffix --
    ``.parquet`` -> ``parquet``, anything else -> ``native``.
the key parser
    ``store://bucket/key``; requires at least two segments and a non-empty key;
    rejects a ``..`` segment, a leading ``/``, a backslash, and control
    characters.
``.node_ptr_deserialize``
    parquet WITHOUT ``sidecar$class`` is a hard stop -- reconstruction is
    impossible because Parquet carries no ts index and no type information.
the handle registry
    ``sprintf("h_%06d_%s", counter, 8 chars of [a-z0-9])``.

Anything here that is STRICTER than the frozen corpus expects is deliberate
(P1 soundness: whatever this accepts, the corpus accepts). The enumeration of
those deliberate gaps lives in
``artifacts/intentional-divergences.json``, and the parity suite asserts SET
EQUALITY against it.
"""

from __future__ import annotations

import re
from typing import Any, Final

from econflow_engine.errors import GateError
from econflow_engine.mcp.allowlists import POINTER_FORMATS

__all__ = [
    "HANDLE_STRING_RE",
    "OBJECT_KEY_RE",
    "POINTER_SCHEME",
    "SYNTHETIC_HANDLE",
    "TICKET_MAX",
    "TICKET_PREFIX",
    "check_handle_input",
    "check_path_uri",
    "check_ticket_ref",
    "infer_pointer_format",
    "parse_store_uri",
]

POINTER_SCHEME: Final = "store://"
OBJECT_PREFIX: Final = "nodes"

#: The engine's own object space -- the ONLY keys it will deserialise as 'native'.
OBJECT_KEY_RE: Final = re.compile(rf"^{OBJECT_PREFIX}/[0-9a-f]{{64}}\.bin$")

#: The shape ``registry_put`` actually produces.
HANDLE_STRING_RE: Final = re.compile(r"^h_\d{6,}_[a-z0-9]{8}$")

#: ``[[:cntrl:]]`` in the C locale = U+0000..U+001F plus U+007F -- exactly what
#: the key parser strips out. Detecting control characters IS the
#: specification: they forge log lines, split headers, and survive visual review.
_CONTROL_CHAR_RE: Final = re.compile(r"[\x00-\x1f\x7f]")

_RDS_SUFFIX_RE: Final = re.compile(r"\.bin$", re.IGNORECASE)

#: A handle of the exact shape the registry emits, for synthetic examples.
SYNTHETIC_HANDLE: Final = "h_000001_abcdefgh"

TICKET_PREFIX: Final = "ticket:"
TICKET_MAX: Final = 64
_TICKET_RE: Final = re.compile(r"^[^\W_][\w.-]*$", re.UNICODE)

_POINTER_KEYS: Final = frozenset({"pointer_uri", "format", "sidecar"})


def _native_policy_message(key: str) -> str:
    return (
        f"node pointer: the key '{key}' does not belong to the engine's object space, "
        "so it is not deserialised as 'native'. Only node outputs (nodes/<sha256>.bin) are "
        "read back as objects; user data must be 'parquet'."
    )


def parse_store_uri(uri: str) -> tuple[str, str]:
    """Split ``store://bucket/key`` into ``(bucket, key)``, or raise :class:`GateError`."""
    if not uri.startswith(POINTER_SCHEME):
        raise GateError(
            "pointer-malformed", f"node pointer: the uri must start with '{POINTER_SCHEME}'."
        )
    rest = uri[len(POINTER_SCHEME) :]
    parts = rest.split("/")
    if len(parts) < 2:
        raise GateError(
            "pointer-malformed",
            f"node pointer: malformed uri '{uri}' (expected store://bucket/key).",
        )
    bucket = parts[0]
    key = "/".join(parts[1:])
    if not key:
        raise GateError(
            "pointer-malformed",
            f"node pointer: malformed uri '{uri}' (expected store://bucket/key).",
        )
    if ".." in key.split("/") or key.startswith("/") or "\\" in key:
        raise GateError("pointer-traversal", f"node pointer: unsafe key '{key}' (path traversal).")
    if _CONTROL_CHAR_RE.search(key):
        raise GateError("pointer-malformed", "node pointer: the key contains control characters.")
    return bucket, key


def infer_pointer_format(uri: str) -> str:
    """``.parquet`` -> ``parquet``, anything else -> ``native`` (the pointer contract)."""
    return "parquet" if uri.endswith(".parquet") else "native"


def _check_native_policy(key: str) -> None:
    if OBJECT_KEY_RE.match(key) is None:
        raise GateError("pointer-native-not-allowed", _native_policy_message(key))


def _check_store_pointer(value: dict[str, Any]) -> None:
    """Validate a pointer OBJECT: ``{pointer_uri, format?, sidecar?}``, strictly."""
    uri = value.get("pointer_uri")
    if not isinstance(uri, str):
        raise GateError(
            "handle-not-string",
            "node pointer: the object carries no string 'pointer_uri' -- there is nothing "
            "to read from the store.",
        )
    extra = sorted(set(value) - _POINTER_KEYS)
    if extra:
        # Strict on purpose: a typo ('sidcar') must be an error rather than a
        # silently dropped sidecar, which the engine would ignore.
        raise GateError(
            "handle-not-string",
            f"node pointer: unknown key(s) {', '.join(extra)} (expected only "
            "pointer_uri, format, sidecar).",
        )
    fmt = value.get("format")
    if fmt is not None and fmt not in POINTER_FORMATS:
        raise GateError(
            "pointer-malformed",
            f"node pointer: unknown format {fmt!r} (expected one of {', '.join(POINTER_FORMATS)}).",
        )
    sidecar = value.get("sidecar")
    if sidecar is not None and not isinstance(sidecar, dict | list):
        raise GateError(
            "pointer-malformed", "node pointer: 'sidecar' must be an object (or an empty array)."
        )

    _, key = parse_store_uri(uri)
    if (fmt if fmt is not None else infer_pointer_format(uri)) == "native":
        _check_native_policy(key)
        return
    cls = sidecar.get("class") if isinstance(sidecar, dict) else None
    if not isinstance(cls, str) or not cls:
        raise GateError(
            "pointer-no-sidecar",
            "node pointer: parquet without a sidecar -- reconstruction is impossible "
            "(the ts index and the class would be lost); the producer must send the sidecar.",
        )


def _check_bare_store_uri(uri: str) -> None:
    """Validate a BARE ``store://`` uri, which by definition carries no sidecar."""
    _, key = parse_store_uri(uri)
    if infer_pointer_format(uri) == "native":
        _check_native_policy(key)
        return
    raise GateError(
        "pointer-no-sidecar",
        "node pointer: parquet without a sidecar -- reconstruction is impossible "
        "(the ts index and the class would be lost); the producer must send the sidecar.",
    )


def check_handle_input(value: object) -> object:
    """Accept a store pointer object, a bare ``store://`` uri, or a registry handle."""
    if isinstance(value, dict):
        _check_store_pointer(value)
        return value
    if isinstance(value, str):
        if HANDLE_STRING_RE.match(value) is not None:
            return value
        _check_bare_store_uri(value)
        return value
    raise GateError(
        "handle-not-string",
        "registry: the handle must be a store pointer, a bare store:// uri, or a handle of "
        "the shape 'h_<counter>_<8 chars>' (as registry_put produces it).",
    )


def check_path_uri(value: object) -> str:
    """Gate a ``kind: "path"`` argument -- a mirror of ``.mcp_path_gate``.

    REASON CODE: every refusal here reports ``other``. That is not a shortcut, it
    is what the engine does: the parity oracle classifies EVERY ``node path:``
    message as ``other`` (measured -- all ten shape mutations of
    ``kind/path/*`` in ``parity-fixtures.v1.json`` carry ``reason_code: "other"``,
    and no ``pointer-*`` code appears for any path argument). The precise
    diagnosis is preserved in ``GateError.detail_code``.
    """
    if not isinstance(value, str) or not value:
        shape = "empty string" if isinstance(value, str) else type(value).__name__
        n = len(value) if isinstance(value, list | dict | str) else 1
        raise GateError(
            "other",
            "node path: invalid value -- expected ONE non-empty string with the path of a "
            f"file inside the object store (store://<bucket>/<key>), got {shape} of length {n}.",
            detail_code="path-not-string",
        )
    if not value.startswith(POINTER_SCHEME):
        raise GateError(
            "other",
            f"node path: only an object store path ({POINTER_SCHEME}<bucket>/<key>) is "
            f"accepted -- the value '{value}' is a local file system path. Upload the file "
            "and pass its ticket: the engine does not see your file system.",
            detail_code="path-not-store-uri",
        )
    try:
        _, key = parse_store_uri(value)
    except GateError as exc:
        raise GateError("other", f"node path: {exc}", detail_code=exc.reason_code) from exc
    if _RDS_SUFFIX_RE.search(key) is not None:
        # A path argument names a DATA FILE, never a serialised engine object.
        # This is stricter than the read policy, which allowlists nodes/<hash>.bin.
        raise GateError(
            "other",
            f"node path: the key '{key}' ends in '.bin' -- a path argument names a "
            "DATA FILE, never a serialised engine object. Pass the ticket of an "
            "uploaded dataset.",
            detail_code="path-native-not-allowed",
        )
    return value


def check_ticket_ref(value: object) -> str:
    """Gate the AUTHORING projection of a path argument: ``ticket:<name>``.

    Tickets are resolved to a pointer BEFORE the authoring -> wire projection
    (an asynchronous database lookup), so they never travel on the wire.
    """
    if not isinstance(value, str) or not value.startswith(TICKET_PREFIX):
        raise GateError(
            "other",
            f"path argument: expected '{TICKET_PREFIX}<name>' -- the name of a dataset you "
            "have uploaded. Local paths and store:// uris are not accepted here.",
            detail_code="ticket-malformed",
        )
    ticket = value[len(TICKET_PREFIX) :]
    if len(ticket) > TICKET_MAX:
        raise GateError(
            "other",
            f"path argument: the ticket name exceeds {TICKET_MAX} characters.",
            detail_code="ticket-too-long",
        )
    if _TICKET_RE.match(ticket) is None:
        raise GateError(
            "other",
            "path argument: a ticket name allows letters (any alphabet), digits and "
            "'.' '_' '-', and starts with a letter or a digit. No spaces and no '/'.",
            detail_code="ticket-charset",
        )
    return value
