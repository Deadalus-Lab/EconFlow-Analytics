# SPDX-License-Identifier: AGPL-3.0-only
"""Idempotency and the ``hash(inputs + params + node_version)`` cache hook.


THE DETERMINISM INVARIANT: identical inputs, params and node version means REUSE
the cached result, never recompute. Node inputs arrive as CONTENT-ADDRESSED
pointers (sha256 of the blob) and the gates are deterministic, so a node call is
a pure function of its request body. The key is therefore computed over the RAW
body -- with the ``pointer_uri`` values still in place, BEFORE pointers are
swapped for per-request registry handles, which are random and would poison it.

THE NON-CACHEABLE CARVE-OUT: a stochastic node whose randomness is not pinned by
a ``seed`` argument is refused caching, so a non-reproducible result is never
silently served from a cache.

THE CACHE LIVES HERE AND NOWHERE ELSE. The orchestrator does NOT implement its
own memoisation -- it calls the engine unconditionally and merely RECORDS the
verdict (``hit | miss | bypass``). Two caches with two key derivations would be
two answers to the same question.
"""

from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Callable
from typing import Any, Protocol

from econflow_engine.mcp.allowlists import STOCHASTIC_UNSEEDED_FNS

__all__ = [
    "CacheStore",
    "cache_key",
    "canonical",
    "compute_identity",
    "is_cacheable",
    "node_version_of",
    "stable_hash",
]


class CacheStore(Protocol):
    """The minimum a blob store must offer. Deliberately tiny and swappable."""

    def exists(self, key: str) -> bool: ...
    def read_bytes(self, key: str) -> bytes: ...
    def write_bytes(self, key: str, payload: bytes) -> None: ...


def canonical(value: Any) -> Any:
    """Make semantically equal bodies hash identically.

    For a MAPPING: drop nulls and sort by key -- key order must not matter. For a
    SEQUENCE: preserve order AND null placeholders, so ``[1, null, 3]`` never
    collides with ``[1, 3]`` and ``[a, b]`` differs from ``[b, a]``.
    """
    if isinstance(value, dict):
        kept = {k: canonical(v) for k, v in value.items() if v is not None}
        return {k: kept[k] for k in sorted(kept)}
    if isinstance(value, list | tuple):
        return [canonical(v) for v in value]
    return value


def stable_hash(value: Any) -> str:
    """Canonical sha256 over stable JSON. Full float precision, nulls preserved."""
    payload = json.dumps(
        canonical(value), sort_keys=False, separators=(",", ":"), ensure_ascii=False,
        allow_nan=False, default=str,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


_COMPUTE_IDENTITY: list[str] = []


def compute_identity() -> str:
    """A stable per-process string identifying the compute build.

    ``NODE_COMPUTE_VERSION`` (a git sha or image digest, baked at image build)
    plus the Python version plus a hash of the resolved lock file. Computed once
    and memoised.

    THE TRAP THIS FIELD EXISTS FOR: the same source on two CPU architectures can
    differ in the last floating-point digit. If the architecture is not part of
    the compute identity, the cache key LIES -- it claims two results are the
    same computation when they are not. Bake the target architecture into
    ``NODE_COMPUTE_VERSION`` when building multi-arch images.
    """
    if _COMPUTE_IDENTITY:
        return _COMPUTE_IDENTITY[0]
    import platform
    from pathlib import Path

    version = os.environ.get("NODE_COMPUTE_VERSION", "")
    lock = Path(os.environ.get("ECONFLOW_ROOT", ".")) / "uv.lock"
    lock_hash = (
        hashlib.sha256(lock.read_bytes()).hexdigest()[:16] if lock.is_file() else ""
    )
    identity = "|".join((version, platform.python_version(), lock_hash))
    _COMPUTE_IDENTITY.append(identity)
    return identity


def node_version_of(spec: Any) -> str:
    """Per-node version string; stored workflows pin it.

    Derived from the node's exposed surface plus the compute identity, so any
    change to what the node accepts, returns or runs on invalidates old entries
    automatically. This is deliberately NOT the contract hash: a contract-hash
    change affects a stored GRAPH (its arguments may no longer be valid), a
    node-version change affects only the CACHE.
    """
    declared = _get(spec, "node_version")
    if declared is not None:
        return str(declared)
    contract = {
        "fn": _get(spec, "fn"),
        "arguments": _get(spec, "arguments"),
        "register": _get(spec, "register"),
        "export": _get(spec, "export"),
        "compute": compute_identity(),
    }
    return f"v-{stable_hash(contract)}"


def cache_key(spec: Any, raw_body: dict[str, Any] | None) -> str:
    """``hash(inputs + params + node_version)``, over the RAW body."""
    payload = {
        "fn": _get(spec, "fn"),
        "node_version": node_version_of(spec),
        "body": canonical(raw_body or {}),
    }
    return f"{_get(spec, 'fn')}/{stable_hash(payload)}"


def _has_seed(spec: Any, raw_body: dict[str, Any] | None) -> bool:
    seed_spec = _argument(spec, "seed")
    if seed_spec is None:
        return False
    if (raw_body or {}).get("seed") is not None:
        return True
    default = seed_spec.get("default") if isinstance(seed_spec, dict) else None
    return default is not None


def is_cacheable(spec: Any, raw_body: dict[str, Any] | None) -> bool:
    """A node is cacheable only when its result is REPRODUCIBLE.

    Not cacheable when either the node EXPOSES a ``seed`` knob that this call did
    not pin, or it is a known stochastic node carrying no seed argument at all
    and this call is unseeded. Deterministic specs are cacheable by default;
    ``cacheable = False`` on the spec opts a node out entirely.
    """
    if _get(spec, "cacheable") is False:
        return False
    if _argument(spec, "seed") is not None and not _has_seed(spec, raw_body):
        return False
    fn = str(_get(spec, "fn") or "")
    stochastic = _get(spec, "stochastic") is True or fn in STOCHASTIC_UNSEEDED_FNS
    return not (stochastic and not _has_seed(spec, raw_body))


def store_key(key: str) -> str:
    """Where a cache entry lives inside the blob store."""
    return f"cache/{hashlib.sha256(key.encode('utf-8')).hexdigest()}.json"


def cache_get(key: str, store: CacheStore) -> Any | None:
    """Read a cache entry. A corrupt entry is a MISS, never an error.

    JSON, not a pickle: a cache blob is data that crosses process and version
    boundaries, and unpickling it would be arbitrary code execution on whatever
    the store happens to hold.
    """
    blob_key = store_key(key)
    if not store.exists(blob_key):
        return None
    try:
        return json.loads(store.read_bytes(blob_key).decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        return None


def cache_put(key: str, result: Any, store: CacheStore) -> None:
    store.write_bytes(
        store_key(key), json.dumps(result, ensure_ascii=False, allow_nan=False).encode("utf-8")
    )


def with_node_cache(
    spec: Any, raw_body: dict[str, Any] | None, store: CacheStore, compute: Callable[[], Any]
) -> tuple[Any, str]:
    """Run ``compute`` behind the cache. Returns ``(result, "hit"|"miss"|"bypass")``."""
    if not is_cacheable(spec, raw_body):
        return compute(), "bypass"
    key = cache_key(spec, raw_body)
    cached = cache_get(key, store)
    if cached is not None:
        return cached, "hit"
    result = compute()
    cache_put(key, result, store)
    return result, "miss"


def _get(spec: Any, key: str) -> Any:
    if isinstance(spec, dict):
        return spec.get(key)
    return getattr(spec, key, None)


def _argument(spec: Any, name: str) -> Any:
    arguments = _get(spec, "arguments") or _get(spec, "args") or ()
    if isinstance(arguments, dict):
        return arguments.get(name)
    for arg in arguments:
        arg_name = arg.get("name") if isinstance(arg, dict) else getattr(arg, "name", None)
        if arg_name == name:
            return arg
    return None
