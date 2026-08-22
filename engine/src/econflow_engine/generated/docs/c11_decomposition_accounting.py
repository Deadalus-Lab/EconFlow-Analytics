# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
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
        'description': 'ox_decompose -- category 11-decomposition-accounting, method card #63.',
        'args': {'formula': "Formula 'y ~ x1 + x2 +... | group'· group binary 0/1.", 'data': 'Handle to a cross-section DataFrame.', 'n_bootstrap': 'Bootstrap replications for SE (positive integer· default 100).', 'seed': 'Reproducibility seed of the bootstrap (default 42).'},
        'input_example': {'formula': 'y ~ x', 'data': '<df_handle>', 'n_bootstrap': 100, 'seed': 42},
    },
    'pi_bilateral': {
        'fn': 'pi_bilateral',
        'description': 'pi_bilateral -- category 11-decomposition-accounting, method card #190.',
        'args': {'data': 'Handle to long-format micro-data (columns time,prices,quantities,prodID).', 'start': "Period start 'YYYY-MM' (base = start = 1).", 'end': "Period end 'YYYY-MM' (must be start <= end).", 'formula': 'Bilateral index formula (default jevons· fisher/tornqvist = superlative baseline).', 'interval': 'True -> full monthly series with dates· False -> a single end-vs-start index (default).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'interval': False},
    },
    'pi_contributions': {
        'fn': 'pi_contributions',
        'description': 'pi_contributions -- category 11-decomposition-accounting, method card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Value-change decomposition indicator (default bennet· identity value=price+quantity).', 'matched': 'True -> only products matched in both periods (default False).', 'interval': 'True -> per-month contributions· False -> cumulative end-vs-start (default).', 'prec': 'Rounding decimal digits of the contributions (>=0· default 2).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'matched': False, 'interval': False, 'prec': 2},
    },
    'pi_multilateral': {
        'fn': 'pi_multilateral',
        'description': 'pi_multilateral -- category 11-decomposition-accounting, method card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Multilateral method (default geks· gk = rolling Geary-Khamis).', 'window': 'Rolling window length in months (>=2· default 13· <= available months).', 'wstart': "Estimation window start 'YYYY-MM' (default None = start of the data)."},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'window': 13},
    },
    'pi_splice': {
        'fn': 'pi_splice',
        'description': 'pi_splice -- category 11-decomposition-accounting, method card #190.',
        'args': {'data': 'Handle to long-format micro-data (time,prices,quantities,prodID).', 'start': "Start 'YYYY-MM'.", 'end': "End 'YYYY-MM' (start <= end).", 'method': 'Multilateral base for splicing (default geks).', 'window': 'Rolling window length in months (>=2· default 13).', 'splice': 'Splicing method of the multilateral series (default movement).', 'interval': 'True -> full spliced series with dates· False -> a single index (default).'},
        'input_example': {'data': '<df_handle>', 'start': '...', 'end': '...', 'window': 13, 'interval': False},
    },
    'prod_fare_primont': {
        'fn': 'prod_fare_primont',
        'description': 'prod_fare_primont -- category 11-decomposition-accounting, method card #62.',
        'args': {'data': 'Handle to a balanced panel DataFrame (DMU × period).', 'id_var': 'DMU identifier column name.', 'time_var': 'Period column name (NOT factor).', 'x_vars': 'Input column names· ALL > 0.', 'y_vars': 'Output column names· ALL > 0.', 'w_vars': 'Input price column names (both-or-neither with p.vars· 1 per input).', 'p_vars': 'Output price column names (both-or-neither with w.vars· 1 per output).', 'tech_change': 'Technological change over time is allowed (default True).', 'tech_reg': 'Technological regress is allowed (default True).', 'rts': 'Returns-to-scale (default vrs).', 'orientation': 'Orientation (default out).', 'scaled': 'Data scaling (default True).', 'shadow': 'Return shadow prices (default False).'},
        'input_example': {'data': '<df_handle>', 'id_var': '...', 'time_var': '...', 'x_vars': ['PROVIDER/DATASET/SERIES'], 'y_vars': ['PROVIDER/DATASET/SERIES'], 'tech_change': True, 'tech_reg': True, 'scaled': True, 'shadow': False},
    },
    'prod_malmquist': {
        'fn': 'prod_malmquist',
        'description': 'prod_malmquist -- category 11-decomposition-accounting, method card #62.',
        'args': {'data': 'Handle to a balanced panel DataFrame (DMU × period).', 'id_var': 'DMU identifier column name (e.g. country/region).', 'time_var': 'Period column name (NOT factor· integer/numeric/Date/character).', 'x_vars': 'Input column names (K, L,...)· ALL > 0.', 'y_vars': 'Output column names (GDP/value added,...)· ALL > 0.', 'rts': 'Returns-to-scale (default vrs).', 'orientation': 'Efficiency orientation (default out).', 'tech_reg': 'Technological regress of the frontier is allowed (default True).', 'scaled': 'Data scaling for numerical stability (default True).'},
        'input_example': {'data': '<df_handle>', 'id_var': '...', 'time_var': '...', 'x_vars': ['PROVIDER/DATASET/SERIES'], 'y_vars': ['PROVIDER/DATASET/SERIES'], 'tech_reg': True, 'scaled': True},
    },
    'da_growth_accounting': {
        'fn': 'da_growth_accounting',
        'description': 'da_growth_accounting -- category 11-decomposition-accounting, method card #484.',
        'args': {'output': 'Output series.', 'inputs': 'Input series, one column each.', 'shares': 'Factor shares; omitted = estimated from cost data.', 'index': 'Index form.'},
        'input_example': {'output': '<series_handle>', 'inputs': '<multiseries_handle>', 'index': 'tornqvist'},
    },
    'da_stochastic_frontier': {
        'fn': 'da_stochastic_frontier',
        'description': 'da_stochastic_frontier -- category 11-decomposition-accounting, method card #485.',
        'args': {'y': 'Output or cost.', 'x': 'Input table.', 'frontier': 'Frontier type.', 'distribution': 'Inefficiency distribution.', 'inefficiency_covariates': 'Covariates explaining inefficiency.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'y': '<series_handle>', 'x': '<df_handle>', 'frontier': 'production', 'distribution': 'half_normal', 'conf_level': 0.95},
    },
    'da_dea': {
        'fn': 'da_dea',
        'description': 'da_dea -- category 11-decomposition-accounting, method card #486.',
        'args': {'inputs': 'Input table.', 'outputs': 'Output table.', 'returns': 'Returns to scale.', 'orientation': 'Orientation.', 'decompose': 'Separate technical and scale efficiency.'},
        'input_example': {'inputs': '<df_handle>', 'outputs': '<df_handle>', 'returns': 'vrs', 'orientation': 'input', 'decompose': True},
    },
    'da_multilateral_index': {
        'fn': 'da_multilateral_index',
        'description': 'da_multilateral_index -- category 11-decomposition-accounting, method card #487.',
        'args': {'data': 'Transaction data: product, period, price and quantity.', 'product': 'Product identifier.', 'period': 'Period identifier.', 'price': 'Price column.', 'quantity': 'Quantity column.', 'method': 'Index method.', 'window': 'Estimation window in periods.', 'splice': 'Splicing method.'},
        'input_example': {'data': '<df_handle>', 'product': '...', 'period': '...', 'price': '...', 'method': 'geks', 'window': 13, 'splice': 'movement'},
    },
    'da_shift_share': {
        'fn': 'da_shift_share',
        'description': 'da_shift_share -- category 11-decomposition-accounting, method card #488.',
        'args': {'data': 'Region-by-industry employment or output.', 'region': 'Region identifier.', 'industry': 'Industry identifier.', 'value': 'Value column.', 'time': 'Period identifier.', 'dynamic': 'Update weights over time.'},
        'input_example': {'data': '<df_handle>', 'region': '...', 'industry': '...', 'value': '...', 'time': '...', 'dynamic': False},
    },
    'da_reweighting_decomposition': {
        'fn': 'da_reweighting_decomposition',
        'description': 'da_reweighting_decomposition -- category 11-decomposition-accounting, method card #489.',
        'args': {'data': 'Pooled data for both groups.', 'outcome': 'Outcome column.', 'group': 'Group indicator.', 'covariates': 'Covariate columns.', 'method': 'Decomposition method.', 'quantiles': 'Quantiles to decompose.', 'nboot': 'Number of bootstrap replications.', 'seed': 'Seed for the random number generator; required for reproducibility.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'outcome': '...', 'group': '...', 'method': 'dfl', 'quantiles': [0.1, 0.5, 0.9], 'nboot': 999, 'seed': 1, 'conf_level': 0.95},
    },
    'da_structural_decomposition': {
        'fn': 'da_structural_decomposition',
        'description': 'da_structural_decomposition -- category 11-decomposition-accounting, method card #490.',
        'args': {'table_start': 'Handle to the earlier table.', 'table_end': 'Handle to the later table.', 'extension': 'Environmental extension to decompose.', 'form': 'Decomposition form.'},
        'input_example': {'table_start': '<raw_handle>', 'table_end': '<raw_handle>', 'form': 'average_polar'},
    },
}
