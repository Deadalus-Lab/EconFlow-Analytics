# SPDX-License-Identifier: AGPL-3.0-only
"""THE HEART. Hand-written, explicit, non-collapsible.

A ``kind`` in the contract is the ONLY authentic type element of an argument.
``mcp_arg_schema()`` -- and therefore the ``json_type`` field of the artifact --
is DOCUMENTED LOSSY: the eight pointer-handle kinds plus ``formula`` and ``raw``
all collapse to ``"string"``. VALIDATE ON ``kind``, NEVER ON ``json_type``.
Ignoring that caused a real bug once; it is not a stylistic preference.

Here lives the kind -> pydantic mapping, one branch per kind, written against the
REAL coercion behaviour the wire contract specifies.

The ``arg_type_for_kind`` dispatch is DELIBERATELY explicit -- one branch per
kind, with the coercion it performs quoted in a comment. It does NOT collapse
into a lookup
table, and ``/simplify`` is not allowed to "simplify" intentional repetition.

THE THREE RULES PER NODE MODEL (each from verified behaviour):

1. ``ConfigDict(extra="forbid")`` ALWAYS -- ``adapt_args`` hard ``stop()``s on
   unknown keys ("Unknown arguments: ...").

2. ``required`` -> a plain field; ``not required`` -> ``| None = None``. NEVER
   Optional-as-nullable-INPUT: ``adapt_args`` reads an explicit ``null`` as
   ABSENT, so a nullable schema would send a null that the contract ignores -- and on a
   required argument that is a 422. The ``| None`` exists so that an ABSENT key
   has somewhere to land; an explicitly supplied ``None`` is rejected by the
   null guard that wraps every field.

3. NEVER a default in the wire model. the argument adapter assigns the
   default RAW (``out[[nm]] <- a$default``) while every EXPLICIT value goes
   through the contract's coercion rules
   is omitted; a materialised default would be sent explicitly and the node would
   answer 422. Defaults live in ``NodeMeta.defaults`` -- for form prefill only,
   and applied in the AUTHORING projection alone.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Annotated, Any, Literal, get_args

from annotated_types import MaxLen, MinLen
from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    ValidationError,
    create_model,
)

from econflow_engine.errors import ENGINE_REASON_CODES, EngineReasonCode, GateError
from econflow_engine.formula import validate_formula
from econflow_engine.mcp.allowlists import (
    FORECASTFN_NAMES,
    FORMULA_ALLOWED_CALLS,
    FORMULA_MAX_DEPTH,
    MAX_POINTER_ARRAY,
    NODE_ARG_KINDS,
    is_array_pointer_handle_kind,
    is_pointer_handle_kind,
    is_scalar_pointer_handle_kind,
)
from econflow_engine.node.store_pointers import (
    TICKET_PREFIX,
    check_handle_input,
    check_path_uri,
    check_ticket_ref,
)

__all__ = [
    "ENGINE_REASON_CODES",
    "FORMULA_CONSTRAINT_PROSE",
    "KIND_LLM_HINT",
    "NODE_ARG_KINDS",
    "EdgeRef",
    "NodeArgMeta",
    "NodeDocs",
    "NodeExecutabilityMeta",
    "NodeManifestEntry",
    "NodeMeta",
    "Projection",
    "arg_type_for_kind",
    "authoring_args_to_wire",
    "build_authoring_model",
    "build_wire_model",
    "reason_code_of",
    "reason_from_kind",
    "validate_wire",
]

Projection = Literal["wire", "authoring"]

_REASON_CODE_SET = frozenset(ENGINE_REASON_CODES)

FORMULA_CONSTRAINT_PROSE = (
    'the contract formula as text, e.g. "y ~ x1 + log(x2)". ONLY these calls are allowed: '
    f"{', '.join(FORMULA_ALLOWED_CALLS)} (maximum depth {FORMULA_MAX_DEPTH}). "
    "Everything else is rejected (default-deny)."
)

KIND_LLM_HINT: dict[str, str] = {
    "formula": FORMULA_CONSTRAINT_PROSE,
    "series_handle": "Connect an edge from a node that produces a univariate time series.",
    "multiseries_handle": "Connect an edge from a node that produces a multivariate time series.",
    "matrix_handle": "Connect an edge from a node that produces a numeric matrix.",
    "exog_handle": "Connect an edge from a node that produces a matrix of exogenous regressors.",
    "df_handle": "Connect an edge from a node that produces a data frame.",
    "raw_handle": "Connect an edge from a node that produces an object (e.g. a fitted model).",
    "raw_handle_array": (
        "Connect MULTIPLE edges (AT LEAST 2) -- one per asset, from nodes that produce an "
        "object (e.g. ga_spec). The ORDER of the edges IS the order of the assets: it must "
        "match the column order of the data supplied later."
    ),
    "irregular_series_handle": (
        "Connect an edge from a node that produces an irregularly indexed series."
    ),
    "raw": "Free value: passed to the engine UNTOUCHED (no coercion whatsoever).",
    "path": (
        f"File path. Give ONLY '{TICKET_PREFIX}<name>' -- the ticket name of a dataset the "
        "user has already uploaded. NEVER a local machine path, NEVER a store:// uri, NEVER "
        "a network address: the engine does not see your file system and every such value is "
        "refused by a gate. If the data has not been uploaded yet, ask the user for it "
        "instead of guessing a path."
    ),
}


# ---------------------------------------------------------------------------
# Field guards
# ---------------------------------------------------------------------------


def _reject_explicit_null(_value: object) -> object:
    raise GateError(
        "missing-required",
        "explicit null: the engine reads it as an ABSENT argument -- omit the key instead.",
    )


def _guard(inner: Any = None) -> Any:
    """Wrap a leaf validator with the explicit-null guard (rule 2).

    The guard MUST sit outside any ``| None`` union, otherwise an explicit null
    would slip through the ``None`` branch untouched.
    """

    def run(value: object) -> object:
        if value is None:
            return _reject_explicit_null(value)
        return value if inner is None else inner(value)

    return BeforeValidator(run)


def _formula_leaf(allowed_vars: tuple[str, ...] | None) -> Any:
    def run(value: object) -> object:
        result = validate_formula(value, allowed_vars)
        if result.ok:
            return value
        # REASON CODE, measured rather than assumed: the oracle's classifier
        # emits 'other' for the bad-head, parse and depth messages -- those three
        # codes appear ZERO times in parity-fixtures.v1.json, while
        # formula-not-string / -not-tilde / -multi-expr / -denied-call / -bad-var
        # all do. The precise diagnosis survives in GateError.detail_code.
        code = result.reason_code or "other"
        wire: EngineReasonCode = (
            "other" if code in ("formula-bad-head", "formula-parse", "formula-depth") else code
        )
        raise GateError(wire, result.message or "formula: rejected.", detail_code=code)

    return run


def _handle_array_leaf(value: object) -> object:
    if not isinstance(value, list):
        raise GateError(
            "handle-not-string",
            "this socket takes an ARRAY of handles -- one edge per asset, in order, "
            "not a single value.",
        )
    if not (2 <= len(value) <= MAX_POINTER_ARRAY):
        raise GateError(
            "handle-not-string",
            f"this socket takes between 2 and {MAX_POINTER_ARRAY} handles, got {len(value)}.",
        )
    for item in value:
        check_handle_input(item)
    return value


def _edge_ref_leaf(value: object) -> object:
    EdgeRef.model_validate(value)
    return value


def _edge_ref_array_leaf(value: object) -> object:
    if not isinstance(value, list):
        raise GateError(
            "handle-not-string",
            "this socket takes an ARRAY of edges -- one per asset, in order.",
        )
    if not (2 <= len(value) <= MAX_POINTER_ARRAY):
        raise GateError(
            "handle-not-string",
            f"this socket takes between 2 and {MAX_POINTER_ARRAY} edges, got {len(value)}.",
        )
    for item in value:
        EdgeRef.model_validate(item)
    return value


class EdgeRef(BaseModel):
    """An AUTHORING reference to another node's output. Never travels on the wire."""

    model_config = ConfigDict(extra="forbid", strict=True)

    # `from` is a Python keyword, so the wire name lives in an alias.
    from_: Annotated[str, MinLen(1)] = Field(alias="from")
    output: Annotated[str, MinLen(1)] | None = None


# ---------------------------------------------------------------------------
# kind -> type. ONE BRANCH PER KIND. Do not collapse into a table.
# ---------------------------------------------------------------------------


def arg_type_for_kind(  # noqa: C901 - the explicitness IS the specification
    kind: str,
    projection: Projection,
    *,
    enum_values: tuple[str, ...] | None = None,
    allowed_vars: tuple[str, ...] | None = None,
) -> Any:
    """Return the pydantic annotation for one argument ``kind``.

    ``projection`` distinguishes the WIRE shape (what the engine receives) from
    the AUTHORING shape (what a graph editor edits): handle sockets carry a
    resolved pointer on the wire but an edge reference while authoring, and a
    path carries a store uri on the wire but a ticket while authoring.
    """
    # .mcp_coerce_one: `as.integer(val)`
    if kind == "integer":
        return int
    # .mcp_coerce_one: `as.numeric(val)`
    if kind == "number":
        return float
    # .mcp_coerce_one: `as.logical(val)`
    if kind == "boolean":
        return bool
    # .mcp_coerce_one: `as.character(val)`
    if kind == "string":
        return str
    # .mcp_coerce_one: `if (is.numeric(argspec$values)) as.numeric(val) else as.character(val)`
    # -- the TYPE only. Membership is checked by match.arg INSIDE the wrapper, which
    # is why the contract never produces 'enum-invalid'; we check membership up front.
    if kind == "enum":
        if not enum_values:
            raise ValueError("arg_type_for_kind: kind='enum' without values -- the spec is broken.")
        return Literal[tuple(enum_values)]
    # .mcp_coerce_one: `adapt_forecastfn(val)` -- a CLOSED allowlist; the alternative
    # would be eval(parse(text = ...)), i.e. remote code execution.
    if kind == "forecastfn_enum":
        return Literal[tuple(FORECASTFN_NAMES)]
    # .mcp_coerce_one: `as.character(unlist(val, use.names = FALSE))`
    if kind == "series_codes":
        return Annotated[list[str], MinLen(1)]
    # .mcp_coerce_one: `as.integer(unlist(val, use.names = FALSE))`
    if kind == "int_array":
        return Annotated[list[int], MinLen(1)]
    # .mcp_coerce_one: `as.numeric(unlist(val, use.names = FALSE))`
    if kind == "num_array":
        return Annotated[list[float], MinLen(1)]
    # .mcp_coerce_one: `adapt_formula(val, allowed_vars = argspec$allowed_vars)`
    if kind == "formula":
        return Annotated[Any, BeforeValidator(_formula_leaf(allowed_vars))]
    # .mcp_coerce_one: falls through to `val` -- passed to the wrapper UNTOUCHED.
    if kind == "raw":
        return Any
    # .mcp_coerce_one: `.mcp_path_gate(val, argname)`
    if kind == "path":
        leaf = check_path_uri if projection == "wire" else check_ticket_ref
        return Annotated[str, BeforeValidator(leaf)]
    # .mcp_coerce_one: `resolve_handle(val, "ts")`
    if kind == "series_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "mts")`
    if kind == "multiseries_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "matrix")`
    if kind == "matrix_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "exog_handle")`
    if kind == "exog_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "df")`
    if kind == "df_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "raw")`
    if kind == "raw_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `resolve_handle(val, "zoo")`
    if kind == "irregular_series_handle":
        return _handle_annotation(projection)
    # .mcp_coerce_one: `lapply(val, function(h) resolve_handle(h, "raw"))`
    if kind == "raw_handle_array":
        array_leaf = _handle_array_leaf if projection == "wire" else _edge_ref_array_leaf
        return Annotated[Any, BeforeValidator(array_leaf), MaxLen(MAX_POINTER_ARRAY)]
    raise ValueError(f"arg_type_for_kind: unknown kind {kind!r} (not in the artifact vocabulary).")


def _handle_annotation(projection: Projection) -> Any:
    leaf = check_handle_input if projection == "wire" else _edge_ref_leaf
    return Annotated[Any, BeforeValidator(leaf)]


def reason_from_kind(kind: str | None) -> EngineReasonCode:
    """The reason code a plain type failure of this kind reports."""
    if kind is None:
        return "other"
    if kind == "formula":
        return "formula-not-string"
    if kind == "forecastfn_enum":
        return "forecastfn-unknown"
    if kind == "enum":
        return "enum-invalid"
    if is_pointer_handle_kind(kind):
        return "handle-not-string"
    return "other"


# ---------------------------------------------------------------------------
# Node metadata
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class NodeExecutabilityMeta:
    status: str
    reason_code: str | None = None
    reason: str | None = None
    blocked_arg: str | None = None


@dataclass(frozen=True, slots=True)
class NodeArgMeta:
    name: str
    kind: str
    required: bool
    enum: tuple[str, ...] | None = None
    allowed_vars: tuple[str, ...] | None = None


@dataclass(frozen=True, slots=True)
class NodeMeta:
    fn: str
    category: str
    card_id: int
    contract_hash: str
    register_field: str | None
    executability: NodeExecutabilityMeta
    memory_class: str
    args: tuple[NodeArgMeta, ...]
    defaults: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class NodeManifestEntry:
    fn: str
    category: str
    card_id: int
    contract_hash: str
    register_field: str | None
    executability: NodeExecutabilityMeta
    memory_class: str
    arg_names: tuple[str, ...]
    arg_kinds: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class NodeDocs:
    fn: str
    description: str
    args: dict[str, str]
    input_example: dict[str, Any]


# ---------------------------------------------------------------------------
# Model builders
# ---------------------------------------------------------------------------

# `protected_namespaces=()` is REQUIRED, not cosmetic: eleven real node arguments
# are named `model_code`, `model_name`, `model_names`, `model_type`. Pydantic's
# default protects the `model_` prefix and would only WARN -- and an argument name
# is part of the contract contract, so renaming it is not an option.
_MODEL_CONFIG = ConfigDict(extra="forbid", strict=True, protected_namespaces=())


def _leaf_inner(arg: NodeArgMeta, projection: Projection) -> Any:
    return arg_type_for_kind(
        arg.kind, projection, enum_values=arg.enum, allowed_vars=arg.allowed_vars
    )


def _field_spec(arg: NodeArgMeta, projection: Projection, default: Any) -> tuple[Any, Any]:
    base = _leaf_inner(arg, projection)
    inner: Any = None
    if getattr(base, "__metadata__", None):
        # The kind supplied its own leaf validator; the null guard must wrap it.
        for meta in base.__metadata__:
            if isinstance(meta, BeforeValidator):
                inner = meta.func
        base = _strip_before_validators(base)
    annotated = base if default is Ellipsis else (base | None)
    return Annotated[annotated, _guard(inner)], default


def _strip_before_validators(annotated: Any) -> Any:
    origin = get_args(annotated)[0]
    keep = [m for m in annotated.__metadata__ if not isinstance(m, BeforeValidator)]
    return Annotated[tuple([origin, *keep])] if keep else origin


def build_wire_model(meta: NodeMeta) -> type[BaseModel]:
    """The model the ENGINE validates: no defaults, no nullable inputs, no extras."""
    fields: dict[str, Any] = {
        arg.name: _field_spec(arg, "wire", ... if arg.required else None) for arg in meta.args
    }
    return create_model(f"{meta.fn}_wire", __config__=_MODEL_CONFIG, **fields)


def build_authoring_model(meta: NodeMeta) -> type[BaseModel]:
    """The model a GRAPH EDITOR edits: handles are edges, paths are tickets.

    This is the ONLY projection that materialises defaults, and only for form
    prefill -- ``authoring_args_to_wire`` drops any value equal to its default
    before the payload reaches the engine.
    """
    fields: dict[str, Any] = {}
    for arg in meta.args:
        if arg.required:
            fields[arg.name] = _field_spec(arg, "authoring", ...)
            continue
        default = meta.defaults.get(arg.name)
        fields[arg.name] = _field_spec(arg, "authoring", default)
    return create_model(f"{meta.fn}_authoring", __config__=_MODEL_CONFIG, **fields)


# ---------------------------------------------------------------------------
# Validation outcome
# ---------------------------------------------------------------------------


def reason_code_of(error: Mapping[str, Any]) -> str | None:
    """Recover the reason code a gate attached to one pydantic error, if any."""
    ctx = error.get("ctx")
    if isinstance(ctx, dict):
        cause = ctx.get("error")
        if isinstance(cause, GateError):
            return cause.reason_code
    err_type = error.get("type")
    return err_type if isinstance(err_type, str) and err_type in _REASON_CODE_SET else None


def validate_wire(
    model: type[BaseModel], body: dict[str, Any], kinds: dict[str, str]
) -> tuple[bool, str | None]:
    """Validate a wire body and, on failure, report the SINGLE reason code.

    The ordering mirrors ``adapt_args``: unknown keys are reported before
    anything else, because that is the first thing the contract function checks.
    """
    try:
        model.model_validate(body)
    except ValidationError as exc:
        errors = exc.errors()
        if any(e["type"] == "extra_forbidden" for e in errors):
            return False, "unknown-args"
        first = errors[0]
        carried = reason_code_of(first)
        if carried is not None:
            return False, carried
        if first["type"] == "missing":
            return False, "missing-required"
        loc = first["loc"]
        arg_name = str(loc[0]) if loc else ""
        return False, reason_from_kind(kinds.get(arg_name))
    return True, None


# ---------------------------------------------------------------------------
# Authoring -> wire
# ---------------------------------------------------------------------------

EdgeResolver = Any


def authoring_args_to_wire(
    meta: NodeMeta, args: dict[str, Any], resolve_edge: EdgeResolver
) -> dict[str, Any]:
    """Project authoring arguments onto the wire.

    The scalar-versus-array decision belongs to the socket's KIND, never to the
    number of connected edges: ``dcc_multispec`` is the single ``raw_handle_array``
    node in the vocabulary, and with ONE edge an edge-count heuristic would send a
    bare pointer object that the engine would iterate field-by-field -- numerically
    plausible, silently wrong, and caught by no gate.
    """
    by_name = {a.name: a for a in meta.args}
    out: dict[str, Any] = {}
    for name, value in args.items():
        arg = by_name.get(name)
        if arg is None:
            raise ValueError(
                f"authoring_args_to_wire({meta.fn}): unknown argument '{name}' "
                "(it does not belong to this method)."
            )
        if value is None:
            raise ValueError(
                f"authoring_args_to_wire({meta.fn}): explicit null in '{name}' -- the engine "
                "reads it as ABSENT; omit the key."
            )
        if is_array_pointer_handle_kind(arg.kind):
            if not isinstance(value, list):
                raise ValueError(
                    f"authoring_args_to_wire({meta.fn}): '{name}' is an ARRAY-of-handles "
                    "socket -- expected a list of edge references, one per asset, in order."
                )
            out[name] = [resolve_edge(EdgeRef.model_validate(item), name) for item in value]
            continue
        if is_scalar_pointer_handle_kind(arg.kind):
            out[name] = resolve_edge(EdgeRef.model_validate(value), name)
            continue
        if arg.kind == "path" and isinstance(value, str) and value.startswith(TICKET_PREFIX):
            raise ValueError(
                f"authoring_args_to_wire({meta.fn}): '{name}' is a path socket and the value "
                f"is still a ticket ('{TICKET_PREFIX}...'). Tickets are resolved to a pointer "
                "BEFORE this projection (an asynchronous database lookup); this function is "
                "synchronous and does not do it."
            )
        if not arg.required and name in meta.defaults and value == meta.defaults[name]:
            continue
        out[name] = value
    for arg in meta.args:
        if arg.required and arg.name not in out:
            raise ValueError(
                f"authoring_args_to_wire({meta.fn}): missing required argument '{arg.name}'."
            )
    return out
