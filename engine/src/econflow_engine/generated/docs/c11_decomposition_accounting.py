# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 11-decomposition-accounting: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'ox_decompose': {
        'fn': 'ox_decompose',
        'description': 'ox_decompose -- category 11-decomposition-accounting, METHOD-SELECTION card #63.',
        'args': {'formula': "Formula 'y ~ x1 + x2 +... | group'· group binary 0/1.", 'data': 'Handle to a cross-section DataFrame.', 'n_bootstrap': 'Bootstrap replications for SE (positive integer· default 100).', 'seed': 'Reproducibility seed of the bootstrap (default 42).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'n_bootstrap': 100, 'seed': 42},
    },
    'pi_bilateral': {
        'fn': 'pi_bilateral',
        'description': 'pi_bilateral -- category 11-decomposition-accounting, METHOD-SELECTION card #190.',
        'args': {'data': 'Handle to long-format micro-data (columns time,prices,quantities,prodID).', 'start': "Period start 'YYYY-MM' (base = start = 1).", 'end': "Period end 'YYYY-MM' (must be start <= end).", 'formula': 'Bilateral index formula (default jevons· fisher/tornqvist = superlative baseline).', 'interval': 'True -> full monthly series with dates· False -> a single end-vs-start index (default).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'interval': False},
    },
    'pi_contributions': {
        'fn': 'pi_contributions',
        'description': 'pi_contributions -- category 11-decomposition-accounting, METHOD-SELECTION card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Value-change decomposition indicator (default bennet· identity value=price+quantity).', 'matched': 'True -> only products matched in both periods (default False).', 'interval': 'True -> per-month contributions· False -> cumulative end-vs-start (default).', 'prec': 'Rounding decimal digits of the contributions (>=0· default 2).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'matched': False, 'interval': False, 'prec': 2},
    },
    'pi_multilateral': {
        'fn': 'pi_multilateral',
        'description': 'pi_multilateral -- category 11-decomposition-accounting, METHOD-SELECTION card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Multilateral method (default geks· gk = rolling Geary-Khamis).', 'window': 'Rolling window length in months (>=2· default 13· <= available months).', 'wstart': "Estimation window start 'YYYY-MM' (default None = start of the data)."},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'window': 13},
    },
    'pi_splice': {
        'fn': 'pi_splice',
        'description': 'pi_splice -- category 11-decomposition-accounting, METHOD-SELECTION card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Multilateral base for splicing (default geks).', 'window': 'Rolling window length in months (>=2· default 13).', 'splice': 'Splicing method of the multilateral series (default movement).', 'interval': 'True -> full spliced series with dates· False -> a single index (default).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'window': 13, 'interval': False},
    },
    'prod_fareprim': {
        'fn': 'prod_fareprim',
        'description': 'prod_fareprim -- category 11-decomposition-accounting, METHOD-SELECTION card #62.',
        'args': {'data': 'Handle to a balanced panel DataFrame (DMU × period).', 'id_var': 'DMU identifier column name.', 'time_var': 'Period column name (NOT factor).', 'x_vars': 'Input column names· ALL > 0.', 'y_vars': 'Output column names· ALL > 0.', 'w_vars': 'Input price column names (both-or-neither with p.vars· 1 per input).', 'p_vars': 'Output price column names (both-or-neither with w.vars· 1 per output).', 'tech_change': 'Technological change over time is allowed (default True).', 'tech_reg': 'Technological regress is allowed (default True).', 'rts': 'Returns-to-scale (default vrs).', 'orientation': 'Orientation (default out).', 'scaled': 'Data scaling (default True).', 'shadow': 'Return shadow prices (default False).'},
        'input_example': {'data': '<df_handle>', 'id_var': '...', 'time_var': '...', 'x_vars': ['PROVIDER/DATASET/SERIES'], 'y_vars': ['PROVIDER/DATASET/SERIES'], 'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    },
    'prod_malmquist': {
        'fn': 'prod_malmquist',
        'description': 'prod_malmquist -- category 11-decomposition-accounting, METHOD-SELECTION card #62.',
        'args': {'data': 'Handle to a balanced panel DataFrame (DMU × period).', 'id_var': 'DMU identifier column name (e.g. country/region).', 'time_var': 'Period column name (NOT factor· integer/numeric/Date/character).', 'x_vars': 'Input column names (K, L,...)· ALL > 0.', 'y_vars': 'Output column names (GDP/value added,...)· ALL > 0.', 'rts': 'Returns-to-scale (default vrs).', 'orientation': 'Efficiency orientation (default out).', 'tech_reg': 'Technological regress of the frontier is allowed (default True).', 'scaled': 'Data scaling for numerical stability (default True).'},
        'input_example': {'data': '<df_handle>', 'id_var': '...', 'time_var': '...', 'x_vars': ['PROVIDER/DATASET/SERIES'], 'y_vars': ['PROVIDER/DATASET/SERIES'], 'tech_reg': True, 'scaled': True},
    },
}
