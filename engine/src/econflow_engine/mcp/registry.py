# SPDX-License-Identifier: AGPL-3.0-only
"""The session handle registry.

IT IMPLEMENTS ONE INVARIANT: the data stays in the engine, the handles go to the
model. Numeric objects and heavy fitted models stay in the server process; a
caller receives ONLY an opaque string handle plus value-free metadata, and passes
that handle back for the next step.

Handles are ``h_<counter>_<8 chars>`` -- the shape the wire contract validates.
The suffix comes from :mod:`secrets`, not a plain RNG: a handle is a capability,
and a guessable capability is no capability at all.

BOUNDED, NEVER SESSION-DEATH: the store evicts the oldest entry when it fills,
rather than growing until the process dies.

VALUE-FREE LISTING: :func:`registry_list` returns class, length, shape and the
caller's own metadata -- NEVER the values. The same leak guard as every
value-free summary in the engine.
"""

from __future__ import annotations

import secrets
import threading
from collections import OrderedDict
from dataclasses import dataclass
from typing import Any, Final

__all__ = [
    "HandleError",
    "MAX_ENTRIES",
    "registry_clear",
    "registry_get",
    "registry_list",
    "registry_meta",
    "registry_put",
]

MAX_ENTRIES: Final = 512
_ALPHABET: Final = "abcdefghijklmnopqrstuvwxyz0123456789"


class HandleError(KeyError):
    """An unknown, expired or malformed handle."""


@dataclass(slots=True)
class _Entry:
    value: Any
    meta: Any


class _Registry:
    """Thread-safe by construction: the FastAPI app serves concurrent requests."""

    __slots__ = ("_counter", "_entries", "_lock")

    def __init__(self) -> None:
        self._entries: OrderedDict[str, _Entry] = OrderedDict()
        self._counter = 0
        self._lock = threading.Lock()

    def new_handle(self) -> str:
        self._counter += 1
        suffix = "".join(secrets.choice(_ALPHABET) for _ in range(8))
        return f"h_{self._counter:06d}_{suffix}"

    def put(self, value: Any, meta: Any = None) -> str:
        with self._lock:
            while len(self._entries) >= MAX_ENTRIES:
                self._entries.popitem(last=False)
            handle = self.new_handle()
            self._entries[handle] = _Entry(value=value, meta=meta)
            return handle

    def entry(self, handle: object) -> _Entry:
        if not isinstance(handle, str) or not handle:
            raise HandleError("registry: the handle must be a non-empty string.")
        with self._lock:
            found = self._entries.get(handle)
        if found is None:
            raise HandleError(
                f"registry: unknown handle '{handle}' (it has expired or never existed)."
            )
        return found

    def listing(self) -> dict[str, dict[str, Any]]:
        with self._lock:
            items = list(self._entries.items())
        out: dict[str, dict[str, Any]] = {}
        for handle, entry in sorted(items):
            value = entry.value
            shape = getattr(value, "shape", None)
            out[handle] = {
                "handle": handle,
                "class": type(value).__name__,
                "length": _safe_len(value),
                "dim": list(shape) if isinstance(shape, tuple) else None,
                "meta": entry.meta,
            }
        return out

    def clear(self, handle: str | None = None) -> None:
        with self._lock:
            if handle is None:
                self._entries.clear()
                self._counter = 0
                return
        self.entry(handle)
        with self._lock:
            self._entries.pop(handle, None)


def _safe_len(value: object) -> int | None:
    try:
        return len(value)  # type: ignore[arg-type]
    except TypeError:
        return None


_REGISTRY = _Registry()


def registry_put(value: Any, meta: Any = None) -> str:
    """Store a value and return its opaque handle."""
    return _REGISTRY.put(value, meta)


def registry_get(handle: object) -> Any:
    """Retrieve a stored value. An unknown handle raises :class:`HandleError`."""
    return _REGISTRY.entry(handle).value


def registry_meta(handle: object) -> Any:
    return _REGISTRY.entry(handle).meta


def registry_list() -> dict[str, dict[str, Any]]:
    """Value-free metadata for every live handle."""
    return _REGISTRY.listing()


def registry_clear(handle: str | None = None) -> None:
    """Drop one handle, or the whole store when ``handle`` is ``None``."""
    _REGISTRY.clear(handle)
