# SPDX-License-Identifier: AGPL-3.0-only
"""Method wrapper ``economic_complexity_rca`` -- METHOD-SELECTION card #239.

#239 Economic complexity: RCA (the Balassa index), ECI/PCI (fitness/reflections/eigenvalues),
    product-space proximity

Category 28-trade-gravity; module ``economic_complexity_rca``.

Reference implementation: not yet selected; see engine/METHOD-SOURCES.json.

See ``./README.md`` for when this method applies, what to reach for instead, and the interpretation
traps recorded against it.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

from econflow_engine.generated.args.c28_trade_gravity import NODE_META, wire_model

if TYPE_CHECKING:
    import pandas as pd

# Re-exported so a body can re-validate its own inputs with ``wire_model(fn)`` and
# read kinds and defaults from ``NODE_META[fn]`` without another import.
__all__ = [
    "ec_balassa",
    "ec_complexity",
    "ec_proximity",
    "NODE_META",
    "wire_model",
]


def ec_balassa(
    *,
    df: pd.DataFrame,
    discrete: bool | None = None,
    cutoff: float | None = None,
    country: str | None = None,
    product: str | None = None,
    value: str | None = None,
) -> dict[str, Any]:
    """Node ``ec_balassa`` -- METHOD-SELECTION card #239.

    Economic complexity: RCA (the Balassa index), ECI/PCI (fitness/reflections/eigenvalues),
    product-space proximity.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long trade DataFrame {country, product, value(>=0)}·
            >= 2 countries & >= 2 products.
        discrete: [boolean, optional] discrete=True => 0/1 specialization (Balassa >= cutoff)· False
            => continuous RCA (default True). Default ``True``.
        cutoff: [number, optional] Balassa discretization threshold (positive· default 1). Default
            ``1``.
        country: [string, optional] Country column name (default 'country').
        product: [string, optional] Product column name (default 'product').
        value: [string, optional] Export value column name (default 'value'· NON-negative).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ec_balassa: not implemented. The method card is in ./README.md."
    )


def ec_complexity(
    *,
    df: pd.DataFrame,
    method: Literal["fitness", "reflections", "eigenvalues"] | None = None,
    iterations: int | None = None,
    extremality: float | None = None,
    discrete: bool | None = None,
    cutoff: float | None = None,
    country: str | None = None,
    product: str | None = None,
    value: str | None = None,
) -> dict[str, Any]:
    """Node ``ec_complexity`` -- METHOD-SELECTION card #239.

    Economic complexity: RCA (the Balassa index), ECI/PCI (fitness/reflections/eigenvalues),
    product-space proximity.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long trade DataFrame {country, product, value(>=0)}.
        method: [enum, optional] Complexity method (default fitness): fitness (non-linear
            iterative)· reflections (Hidalgo-Hausmann iterated averaging)· eigenvalues (2nd
            eigenvector).
        iterations: [integer, optional] Number of iterations for fitness/reflections (positive·
            default 20). Default ``20``.
        extremality: [number, optional] Extremality parameter ONLY for method='fitness' (positive·
            default 1). Default ``1``.
        discrete: [boolean, optional] discrete=True => 0/1 specialization (Balassa >= cutoff)· False
            => continuous RCA (default True). Default ``True``.
        cutoff: [number, optional] Balassa discretization threshold (positive· default 1). Default
            ``1``.
        country: [string, optional] Country column name (default 'country').
        product: [string, optional] Product column name (default 'product').
        value: [string, optional] Export value column name (default 'value'· NON-negative).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ec_complexity: not implemented. The method card is in ./README.md."
    )


def ec_proximity(
    *,
    df: pd.DataFrame,
    compute: Literal["both", "country", "product"] | None = None,
    discrete: bool | None = None,
    cutoff: float | None = None,
    country: str | None = None,
    product: str | None = None,
    value: str | None = None,
) -> dict[str, Any]:
    """Node ``ec_proximity`` -- METHOD-SELECTION card #239.

    Economic complexity: RCA (the Balassa index), ECI/PCI (fitness/reflections/eigenvalues),
    product-space proximity.

    Category 28-trade-gravity; memory class ``light``.

    Args:
        df: [df_handle, required] Handle to a long trade DataFrame {country, product, value(>=0)}.
        compute: [enum, optional] Which proximity matrices (default both): both / country
            (country×country) / product (product×product, product space).
        discrete: [boolean, optional] discrete=True => 0/1 specialization (Balassa >= cutoff)· False
            => continuous RCA (default True). Default ``True``.
        cutoff: [number, optional] Balassa discretization threshold (positive· default 1). Default
            ``1``.
        country: [string, optional] Country column name (default 'country').
        product: [string, optional] Product column name (default 'product').
        value: [string, optional] Export value column name (default 'value'· NON-negative).

    Returns:
        A JSON-safe mapping, ready for ``econflow_engine.serialize.to_mcp``.
    """
    raise NotImplementedError(
        "ec_proximity: not implemented. The method card is in ./README.md."
    )
