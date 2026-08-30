# SPDX-License-Identifier: AGPL-3.0-only
"""L2 serialisation: one total, JSON-safe conversion of any wrapper output.

ONE shared conversion, :func:`to_mcp`, that turns ANY wrapper output into a
JSON-safe structure, so that :func:`to_json` NEVER blows up and never leaks a
call, an environment, a file handle, or the heavy internals of a fitted model.

PRINCIPLES, unchanged:

* pure   -- does not mutate its input.
* total  -- an unknown or dangerous object becomes an EXPLICIT compact stub
            (``@mcp_class`` + ``@mcp_serialized: False``), NEVER silent garbage.
* single dispatch per type, with recursion into mappings and sequences.

WHY THIS SURFACE IS SMALL. The wire contract still names eight time-series
handle kinds, because the catalogue was selected against a language with eight
mutually incompatible time-series classes, each with its own index accessor.
pandas has ONE: a Series or DataFrame with a temporal index, so the whole
reconciliation problem collapses into two functions. What does NOT collapse is
the part that carries risk:

* THE STUB POLICY. An unknown or dangerous object is stubbed, never
  deep-serialised. The useful numbers already exist in the sibling fields the
  wrapper exports; walking a fitted model instead leaks its call, its data and
  its environment.
* THE HYPOTHESIS-TEST FLATTENING. A test result becomes atomic named fields.
* THE DISTANCE LOWER TRIANGLE. A condensed distance vector keeps its own length
  and size and NEVER borrows a square matrix's shape.
* THE RECORD-ORIENTED DataFrame. Row objects, not column arrays, so a consumer
  never has to zip parallel arrays back together.

THE CANONICAL JSON CONFIGURATION. These are the wire contract's settings, and
every consumer downstream is written against them:

* missing and non-finite values become ``null`` (there is no NaN in JSON, and
  emitting the non-standard token would break every strict parser downstream);
* dates and timestamps become ISO-8601 strings;
* full float precision is preserved -- Python's repr is already the shortest
  round-tripping form, which is what the contract's unrounded setting asks for;
* the contract's scalar-unboxing switch has no counterpart here and needs none:
  it existed because a scalar and a length-one vector were the same object. In
  Python they are not, so shapes are unambiguous without it.
"""

from __future__ import annotations

import datetime as dt
import math
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from functools import singledispatch
from typing import Any

import numpy as np
import orjson
import pandas as pd

__all__ = ["McpDistance", "stub", "to_json", "to_mcp"]

_ISO_DATE = "%Y-%m-%d"
_ISO_DATETIME = "%Y-%m-%dT%H:%M:%S%z"


@dataclass(frozen=True, slots=True)
class McpDistance:
    """A condensed distance vector, as the wire contract defines it.

    The condensed distance form is a lower-triangle vector of length n(n-1)/2 carrying ``Size``,
    ``Labels`` and ``method`` as attributes. scipy's condensed form is the same
    vector with the attributes lost, so wrappers wrap it here.

    THE TRAP THIS CLASS EXISTS FOR, measured: merely loading the
    ``proxy`` namespace registered a ``dim.dist`` method engine-wide, after which
    the generic branch reported ``dim = (n, n)`` for a vector of length n(n-1)/2,
    LOST the length, and filled the values with fabricated names -- wrong
    metadata in every node that registers a distance object. The rule that fixed
    it is the rule here: read the SIZE and LABELS that were declared, never infer
    a shape from the container.
    """

    condensed: Sequence[float]
    size: int
    labels: Sequence[str] | None = None
    method: str | None = None


def _iso_index_label(stamp: Any) -> str | None:
    """ISO-8601, never ``str(Timestamp)``: the latter uses a space separator."""
    if stamp is pd.NaT or stamp is None:
        return None
    moment = stamp.to_timestamp() if isinstance(stamp, pd.Period) else pd.Timestamp(stamp)
    # TWO PREDICATES, BECAUSE THE TWO CHECKERS MODEL THIS LINE DIFFERENTLY.
    # `pd.isna` states the intent -- `is pd.NaT` reads as provably false to mypy,
    # which types the constructor as always returning Timestamp, while at run time
    # `pd.Timestamp(pd.NaT)` really is NaT. pyright types the same call as
    # `Timestamp | NaTType` and only the isinstance form narrows it. Measured:
    # `isinstance(pd.NaT, pd.Timestamp)` is False, so the two agree on every input
    # this function can receive.
    if bool(pd.isna(moment)) or not isinstance(moment, pd.Timestamp):
        return None
    return moment.isoformat()


def _clean_float(value: float) -> float | None:
    """Non-finite becomes ``null``: JSON has no NaN and no Infinity."""
    return None if not math.isfinite(value) else float(value)


def stub(
    value: object, note: str | None = None, extra: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    """The compact refusal-to-serialise record. The contract other layers read."""
    out: dict[str, Any] = {
        "@mcp_class": [type(value).__name__],
        "@mcp_serialized": False,
    }
    shape = getattr(value, "shape", None)
    if isinstance(shape, tuple) and all(isinstance(d, int | np.integer) for d in shape):
        out["dim"] = [int(d) for d in shape]
    else:
        try:
            out["length"] = len(value)  # type: ignore[arg-type]
        except TypeError:
            out["length"] = None
    if note is not None:
        out["@mcp_note"] = note
    if extra:
        out.update(extra)
    return out


@singledispatch
def to_mcp(value: object) -> Any:
    """Convert any wrapper output into a JSON-safe structure.

    THE DEFAULT BRANCH IS THE TOTAL CATCH-ALL and it STUBS. Anything that reaches
    here is a foreign fitted object, a module, a closure, a file handle or an
    open connection. Recursing into it would leak internals; refusing is the
    designed answer, and the numbers the caller wants are in the sibling fields
    the wrapper already exported.
    """
    if callable(value):
        return stub(value, note="callable -- not serialised.")
    return stub(
        value,
        note=(
            "foreign / non-serialisable object -- see the sibling fields for the "
            "extracted values."
        ),
    )


@to_mcp.register(type(None))
def _(value: None) -> None:
    return None


@to_mcp.register(bool)
def _(value: bool) -> bool:
    return value


@to_mcp.register(int)
@to_mcp.register(np.integer)
def _(value: int) -> int:
    return int(value)


@to_mcp.register(float)
@to_mcp.register(np.floating)
def _(value: float) -> float | None:
    return _clean_float(float(value))


@to_mcp.register(str)
def _(value: str) -> str:
    return value


@to_mcp.register(complex)
@to_mcp.register(np.complexfloating)
def _(value: complex) -> dict[str, Any]:
    return {"re": _clean_float(value.real), "im": _clean_float(value.imag)}


@to_mcp.register(dt.datetime)
def _(value: dt.datetime) -> str:
    return value.strftime(_ISO_DATETIME) if value.tzinfo else value.isoformat()


@to_mcp.register(dt.date)
def _(value: dt.date) -> str:
    return value.strftime(_ISO_DATE)


@to_mcp.register(Mapping)
def _(value: Mapping[Any, Any]) -> dict[str, Any]:
    return {str(k): to_mcp(v) for k, v in value.items()}


@to_mcp.register(list)
@to_mcp.register(tuple)
@to_mcp.register(set)
@to_mcp.register(frozenset)
def _(value: Sequence[Any]) -> list[Any]:
    return [to_mcp(v) for v in value]


@to_mcp.register(np.ndarray)
def _(value: np.ndarray) -> Any:
    if np.iscomplexobj(value):
        return {
            "re": to_mcp(np.real(value)),
            "im": to_mcp(np.imag(value)),
            "dim": list(value.shape),
        }
    if value.ndim == 0:
        return to_mcp(value.item())
    if value.ndim == 1:
        return [to_mcp(v) for v in value.tolist()]
    if value.ndim == 2:
        # Rows, not columns: a consumer must never have to transpose to read one
        # observation, and `dim` travels alongside so the shape stays explicit.
        return {"values": [[to_mcp(v) for v in row] for row in value.tolist()],
                "dim": list(value.shape)}
    return {"values": [to_mcp(v) for v in value.ravel(order="F").tolist()],
            "dim": list(value.shape)}


@to_mcp.register(pd.Timestamp)
def _(value: pd.Timestamp) -> str | None:
    return None if pd.isna(value) else value.isoformat()


@to_mcp.register(pd.Categorical)
def _(value: pd.Categorical) -> dict[str, Any]:
    return {
        "values": [None if pd.isna(v) else str(v) for v in value],
        "levels": [str(c) for c in value.categories],
        "ordered": bool(value.ordered),
        # `ordered` IS PART OF THE ANSWER AND NOT A DETAIL. `levels` is a LIST, so it
        # reads as an order whether or not the column declares one -- and an
        # unordered Categorical's categories are pandas' lexicographic sort, which is
        # an order nobody chose. A consumer cannot tell the two apart without this.
    }


@to_mcp.register(pd.Series)
def _(value: pd.Series) -> dict[str, Any]:
    """Every time-series representation collapses to this: values plus an index."""
    out: dict[str, Any] = {"values": [to_mcp(v) for v in value.tolist()]}
    if isinstance(value.dtype, pd.CategoricalDtype):
        # THE CATEGORICAL HANDLER ABOVE NEVER SEES A CATEGORICAL COLUMN. `to_mcp` is a
        # `singledispatch` over the argument's CLASS, and a Categorical inside a Series
        # is a Series -- so `tolist()` flattened it to its labels and the levels and
        # their order were dropped on the wire while surviving in process. Measured on
        # `ld_ordered_choice`, whose `outcome` is published as an ordered Categorical
        # precisely for the order it carries: what travelled was `{"values": [...],
        # "name": "tonsil_size"}` and nothing else.
        out["levels"] = [str(c) for c in value.cat.categories]
        out["ordered"] = bool(value.cat.ordered)
    if isinstance(value.index, pd.DatetimeIndex | pd.PeriodIndex):
        out["index"] = [_iso_index_label(t) for t in value.index]
        freq = getattr(value.index, "freqstr", None)
        if freq is not None:
            out["frequency"] = freq
    elif not isinstance(value.index, pd.RangeIndex):
        out["index"] = [to_mcp(i) for i in value.index.tolist()]
    if value.name is not None:
        out["name"] = str(value.name)
    return out


@to_mcp.register(pd.DataFrame)
def _(value: pd.DataFrame) -> list[dict[str, Any]]:
    """Record-oriented: one JSON object per row, columns as keys."""
    if value.empty:
        return []
    columns = [str(c) for c in value.columns]
    cells = [[to_mcp(v) for v in value[c].tolist()] for c in value.columns]
    return [
        dict(zip(columns, (column[i] for column in cells), strict=True))
        for i in range(len(value))
    ]


@to_mcp.register(McpDistance)
def _(value: McpDistance) -> dict[str, Any]:
    condensed = [to_mcp(v) for v in value.condensed]
    return {
        "lower_tri": condensed,
        "length": len(condensed),
        "size": int(value.size),
        "labels": None if value.labels is None else [str(x) for x in value.labels],
        "method": value.method,
    }


_HTEST_FIELDS = (
    "statistic",
    "parameter",
    "pvalue",
    "p_value",
    "estimate",
    "null_value",
    "confidence_interval",
    "conf_int",
    "standard_error",
    "stderr",
    "alternative",
    "method",
    "data_name",
)


def flatten_htest(result: object) -> dict[str, Any] | None:
    """Flatten a hypothesis-test result into atomic named fields.

    Recognises the shape rather than a class, because there is no single one:
    scipy returns a different named tuple per test and statsmodels returns plain
    tuples and result objects. Anything carrying a statistic AND a p-value is
    treated as a test result; anything else returns ``None`` so the caller falls
    through to the normal dispatch.
    """
    has_statistic = hasattr(result, "statistic")
    has_p = hasattr(result, "pvalue") or hasattr(result, "p_value")
    if not (has_statistic and has_p):
        return None
    out: dict[str, Any] = {}
    for name in _HTEST_FIELDS:
        if not hasattr(result, name):
            continue
        value = getattr(result, name)
        if value is None or callable(value):
            continue
        out[name] = to_mcp(value)
    return out


def _json_default(value: object) -> Any:
    converted = to_mcp(value)
    if type(converted) is type(value) and not isinstance(converted, dict | list):
        raise TypeError(f"to_json: cannot serialise {type(value).__name__}.")
    return converted


def to_json(value: object, *, indent: bool = False) -> str:
    """Serialise a payload with the canonical configuration.

    orjson rather than the standard library, for one substantive reason and one
    incidental one. THE SUBSTANTIVE ONE: orjson writes a non-finite float as
    ``null`` natively, which is exactly what the contract requires. The standard
    library instead emits the non-standard ``NaN`` token, which breaks strict
    parsers downstream, or raises -- and raising would be a behaviour change from
    the contract, not a safety improvement, since the contract says null. THE
    INCIDENTAL ONE: it is faster on the large numeric payloads a node returns.

    Float precision is the shortest round-tripping form, which is what the
    contract's unrounded setting asks for.
    """
    option = orjson.OPT_INDENT_2 if indent else 0
    return orjson.dumps(to_mcp(value), default=_json_default, option=option).decode("utf-8")
