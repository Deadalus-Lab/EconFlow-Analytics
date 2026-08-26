# --- gen_wrappers: header begin ---
# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``canonical_disk_format`` -- method card #98.

#98 Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset

Category 00-data-utilities; module ``canonical_disk_format``.

Reference implementation: pyarrow.

See ``engine/corpus/`` for when this method applies, what to reach for instead, and the
interpretation traps recorded against it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c00_data_utilities import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "arw_open_dataset",
    "arw_read_csv",
    "arw_read_feather",
    "arw_read_parquet",
    "arw_write_parquet",
    "NODE_META",
    "wire_model",
]

# --- gen_wrappers: header end ---


def arw_read_parquet(
    *,
    file: str,
    col_select: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``arw_read_parquet`` -- method card #98.

    Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        file: [path, required] Object-store path to a single Parquet file.
        col_select: [series_codes, optional] Column names to select (empty = all).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
        - write_parquet: x a data_frame with >=1 column; the parent dir of sink exists;
          codec_is_available; POST-gate the file was created
        - open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "arw_read_parquet: not implemented."
    )


def arw_read_feather(
    *,
    file: str,
    col_select: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``arw_read_feather`` -- method card #98.

    Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        file: [path, required] Object-store path to a Feather/Arrow-IPC file.
        col_select: [series_codes, optional] Column names to select; empty = all.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
        - write_parquet: x a data_frame with >=1 column; the parent dir of sink exists;
          codec_is_available; POST-gate the file was created
        - open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "arw_read_feather: not implemented."
    )


def arw_read_csv(
    *,
    file: str,
    col_select: Sequence[str] | None = None,
) -> dict[str, Any]:
    """Node ``arw_read_csv`` -- method card #98.

    Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset.

    Category 00-data-utilities; memory class ``light``.

    Registers its result under ``data``, so a later node can consume it as a handle.

    Args:
        file: [path, required] Object-store path to a CSV file (Arrow reader).
        col_select: [series_codes, optional] Column names to select; empty = all.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
        - write_parquet: x a data_frame with >=1 column; the parent dir of sink exists;
          codec_is_available; POST-gate the file was created
        - open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "arw_read_csv: not implemented."
    )


def arw_write_parquet(
    *,
    x: pd.DataFrame,
    compression: Literal["snappy", "gzip", "zstd", "uncompressed"] | None = None,
) -> dict[str, Any]:
    """Node ``arw_write_parquet`` -- method card #98.

    Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset.

    Category 00-data-utilities; memory class ``light``.

    Args:
        x: [df_handle, required] Handle to a DataFrame (>=1 column) to write as Parquet.
        compression: [enum, optional] Compression codec (default snappy; gated with
            codec_is_available).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
        - write_parquet: x a data_frame with >=1 column; the parent dir of sink exists;
          codec_is_available; POST-gate the file was created
        - open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "arw_write_parquet: not implemented."
    )


def arw_open_dataset(
    *,
    sources: str,
    partitioning: Sequence[str] | None = None,
    format: Literal["parquet", "arrow", "feather", "csv", "tsv", "text", "json"] | None = None,
    n_preview: int | None = None,
) -> dict[str, Any]:
    """Node ``arw_open_dataset`` -- method card #98.

    Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy
    (hive-)partitioned Dataset.

    Category 00-data-utilities; memory class ``light``.

    Args:
        sources: [path, required] Object-store path to a DIRECTORY holding a (hive-)partitioned
            dataset.
        partitioning: [series_codes, optional] Partition column names (directory order); empty =
            auto hive.
        format: [enum, optional] Dataset file format (default parquet).
        n_preview: [integer, optional] Number of head preview rows (default 10; 0 = none). Default
            ``10``.

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.

    Gates:
        None declared. The ``precondition_gates`` field of this method card is empty; the checks a
        body must run are named here once the field carries them.

    Validation:
        Documented on the method card:

        - read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
        - write_parquet: x a data_frame with >=1 column; the parent dir of sink exists;
          codec_is_available; POST-gate the file was created
        - open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

    .. gen_wrappers: end of generated docstring

    Examples:
        None yet. This node raises ``NotImplementedError``; its example is written with its body and
        belongs to whoever writes it.

    Note:
        The implementation note is written with the body: the library functions it calls and their
        versions, what the method leaves out, and every gate added with the source that requires it.
    """
    raise NotImplementedError(
        "arw_open_dataset: not implemented."
    )
