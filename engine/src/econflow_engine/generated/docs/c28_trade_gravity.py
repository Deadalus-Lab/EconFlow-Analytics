# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 28-trade-gravity: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'ec_balassa': {
        'fn': 'ec_balassa',
        'description': 'ec_balassa -- category 28-trade-gravity, method card #239.',
        'args': {'df': 'Handle to a long trade DataFrame {country, product, value(>=0)}· >= 2 countries & >= 2 products.', 'discrete': 'discrete=True => 0/1 specialization (Balassa >= cutoff)· False => continuous RCA (default True).', 'cutoff': 'Balassa discretization threshold (positive· default 1).', 'country': "Country column name (default 'country').", 'product': "Product column name (default 'product').", 'value': "Export value column name (default 'value'· NON-negative)."},
        'input_example': {'df': '<df_handle>', 'discrete': True, 'cutoff': 1},
    },
    'ec_complexity': {
        'fn': 'ec_complexity',
        'description': 'ec_complexity -- category 28-trade-gravity, method card #239.',
        'args': {'df': 'Handle to a long trade DataFrame {country, product, value(>=0)}.', 'method': 'Complexity method (default fitness): fitness (non-linear iterative)· reflections (Hidalgo-Hausmann iterated averaging)· eigenvalues (2nd eigenvector).', 'iterations': 'Number of iterations for fitness/reflections (positive· default 20).', 'extremality': "Extremality parameter ONLY for method='fitness' (positive· default 1).", 'discrete': 'discrete=True => 0/1 specialization (Balassa >= cutoff)· False => continuous RCA (default True).', 'cutoff': 'Balassa discretization threshold (positive· default 1).', 'country': "Country column name (default 'country').", 'product': "Product column name (default 'product').", 'value': "Export value column name (default 'value'· NON-negative)."},
        'input_example': {'df': '<df_handle>', 'iterations': 20, 'extremality': 1, 'discrete': True, 'cutoff': 1},
    },
    'ec_proximity': {
        'fn': 'ec_proximity',
        'description': 'ec_proximity -- category 28-trade-gravity, method card #239.',
        'args': {'df': 'Handle to a long trade DataFrame {country, product, value(>=0)}.', 'compute': 'Which proximity matrices (default both): both / country (country×country) / product (product×product, product space).', 'discrete': 'discrete=True => 0/1 specialization (Balassa >= cutoff)· False => continuous RCA (default True).', 'cutoff': 'Balassa discretization threshold (positive· default 1).', 'country': "Country column name (default 'country').", 'product': "Product column name (default 'product').", 'value': "Export value column name (default 'value'· NON-negative)."},
        'input_example': {'df': '<df_handle>', 'discrete': True, 'cutoff': 1},
    },
    'gr_bvu': {
        'fn': 'gr_bvu',
        'description': 'gr_bvu -- category 28-trade-gravity, method card #237.',
        'args': {'df': 'Handle to a bilateral trade DataFrame {origin, destination, flow, distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline — only column names.', 'dependent_variable': 'Column name of the trade flow (dependent). Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).', 'distance': 'Distance column name (distance). Log-transformed automatically => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).', 'income_origin': 'Origin income column name (exporter GDP)· log-transformed => >0.', 'income_destination': 'Destination income column name (importer GDP)· log-transformed => >0.', 'code_origin': 'Origin country code column name (exporter id, e.g. iso_o).', 'code_destination': 'Destination country code column name (importer id, e.g. iso_d).', 'additional_regressors': 'Array of names of ADDITIONAL dyadic regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY log-transformed here. Optional.', 'robust': 'robust=True => a robust linear fit robust SEs (without p-value)· False => lm/glm (default False).'},
        'input_example': {'df': '<df_handle>', 'dependent_variable': '...', 'distance': '...', 'income_origin': '...', 'income_destination': '...', 'code_origin': '...', 'code_destination': '...', 'robust': False},
    },
    'gr_fixed_effects': {
        'fn': 'gr_fixed_effects',
        'description': 'gr_fixed_effects -- category 28-trade-gravity, method card #237.',
        'args': {'df': 'Handle to a bilateral trade DataFrame {origin, destination, flow, distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline — only column names.', 'dependent_variable': 'Column name of the trade flow (dependent). Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).', 'distance': 'Distance column name (distance). Log-transformed automatically => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).', 'code_origin': 'Origin country code column name (exporter id, e.g. iso_o).', 'code_destination': 'Destination country code column name (importer id, e.g. iso_d).', 'additional_regressors': 'Array of names of ADDITIONAL dyadic regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY log-transformed here. Optional.', 'robust': 'robust=True => a robust linear fit robust SEs (without p-value)· False => lm/glm (default False).'},
        'input_example': {'df': '<df_handle>', 'dependent_variable': '...', 'distance': '...', 'code_origin': '...', 'code_destination': '...', 'robust': False},
    },
    'gr_ols': {
        'fn': 'gr_ols',
        'description': 'gr_ols -- category 28-trade-gravity, method card #237.',
        'args': {'df': 'Handle to a bilateral trade DataFrame {origin, destination, flow, distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline — only column names.', 'dependent_variable': 'Column name of the trade flow (dependent). Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).', 'distance': 'Distance column name (distance). Log-transformed automatically => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).', 'income_origin': 'Origin income column name (exporter GDP)· log-transformed => >0.', 'income_destination': 'Destination income column name (importer GDP)· log-transformed => >0.', 'code_origin': 'Origin country code column name (exporter id, e.g. iso_o).', 'code_destination': 'Destination country code column name (importer id, e.g. iso_d).', 'additional_regressors': 'Array of names of ADDITIONAL dyadic regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY log-transformed here. Optional.', 'uie': 'uie=True => unitary income elasticities (dependent/(inc_o*inc_d) before the log)· False => incomes explicit regressors (default False).', 'robust': 'robust=True => a robust linear fit robust SEs (without p-value)· False => lm/glm (default False).'},
        'input_example': {'df': '<df_handle>', 'dependent_variable': '...', 'distance': '...', 'income_origin': '...', 'income_destination': '...', 'code_origin': '...', 'code_destination': '...', 'uie': False, 'robust': False},
    },
    'gr_ppml': {
        'fn': 'gr_ppml',
        'description': 'gr_ppml -- category 28-trade-gravity, method card #237.',
        'args': {'df': 'Handle to a bilateral trade DataFrame {origin, destination, flow, distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline — only column names.', 'dependent_variable': 'Column name of the trade flow (dependent). Poisson PML => NON-NEGATIVE (>=0· accepts zeros).', 'distance': 'Distance column name (distance). Log-transformed automatically => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).', 'additional_regressors': 'Array of names of ADDITIONAL dyadic regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY log-transformed here. Optional.', 'robust': 'robust=True => a robust linear fit robust SEs (without p-value)· False => lm/glm (default False).'},
        'input_example': {'df': '<df_handle>', 'dependent_variable': '...', 'distance': '...', 'robust': False},
    },
    'gr_tetrads': {
        'fn': 'gr_tetrads',
        'description': 'gr_tetrads -- category 28-trade-gravity, method card #237.',
        'args': {'df': 'Handle to a bilateral trade DataFrame {origin, destination, flow, distance, (incomes), (dummies)}· >= 3 rows (bilateral pairs). The data NEVER inline — only column names.', 'dependent_variable': 'Column name of the trade flow (dependent). Log-transformed => STRICTLY POSITIVE (>0· zeros/negatives are dropped silently => gate).', 'distance': 'Distance column name (distance). Log-transformed automatically => STRICTLY POSITIVE (>0· non-positive => silent row-drop => gate).', 'code_origin': 'Origin country code column name (exporter id, e.g. iso_o).', 'code_destination': 'Destination country code column name (importer id, e.g. iso_d).', 'filter_origin': 'Reference exporter code (must EXIST in the column code_origin)· eliminates monadic exporter effects.', 'filter_destination': 'Reference importer code (must EXIST in the column code_destination)· eliminates monadic importer effects.', 'additional_regressors': 'Array of names of ADDITIONAL dyadic regressors (e.g. rta, contig, comlang)· for PPML pass the incomes ALREADY log-transformed here. REQUIRED for tetrads (>=1).', 'multiway': 'multiway=True => multi-way clustered SEs (Cameron-Gelbach-Miller 2011· returns a coeftest matrix)· False => plain lm (default False).'},
        'input_example': {'df': '<df_handle>', 'dependent_variable': '...', 'distance': '...', 'code_origin': '...', 'code_destination': '...', 'filter_origin': '...', 'filter_destination': '...', 'additional_regressors': ['PROVIDER/DATASET/SERIES'], 'multiway': False},
    },
    'pp_hdfe': {
        'fn': 'pp_hdfe',
        'description': 'pp_hdfe -- category 28-trade-gravity, method card #238.',
        'args': {'data': 'Handle to ONE long gravity DataFrame: one row per (exporter, importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect factor columns.', 'dep': 'Column name of the dependent flow/count (bilateral trade flow, non-negative)· PPML models E[y]=exp(xbeta).', 'indep': 'Names of numeric regressor columns (>= 1): e.g. dummies of trade provisions / policies· ALL numeric, WITHOUT NA.', 'fixed': 'High-dimensional fixed effects: either a character vector of simple FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g. [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).', 'cluster': 'Column names for cluster-robust SE / penalty loadings (optional)· REQUIRED when plugin=True.', 'tol': 'Convergence tolerance of the IRLS (positive· default 1e-8).', 'hdfetol': 'Convergence tolerance of the HDFE partialling-out (positive· default 1e-4).'},
        'input_example': {'data': '<df_handle>', 'dep': '...', 'indep': ['PROVIDER/DATASET/SERIES'], 'fixed': '...', 'tol': 1e-08, 'hdfetol': 0.0001},
    },
    'pp_ml_fit': {
        'fn': 'pp_ml_fit',
        'description': 'pp_ml_fit -- category 28-trade-gravity, method card #238.',
        'args': {'data': 'Handle to ONE long gravity DataFrame: one row per (exporter, importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect factor columns.', 'dep': 'Column name of the dependent flow/count (bilateral trade flow, non-negative)· PPML models E[y]=exp(xbeta).', 'indep': 'Names of numeric regressor columns (>= 1): e.g. dummies of trade provisions / policies· ALL numeric, WITHOUT NA.', 'fixed': 'High-dimensional fixed effects: either a character vector of simple FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g. [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).', 'lambdas': 'Vector of non-negative lambda of the penalization path (REQUIRED when plugin=False)· the lambda that MINIMIZES the BIC is selected.', 'penalty': 'Penalty type (default lasso): lasso=L1 selection· ridge=L2.', 'plugin': 'plugin lasso (default False): ignores lambdas & uses data-driven penalty loadings· REQUIRES cluster.', 'post': 'post-lasso: re-estimation (unpenalized PPML) on the selected regressors for de-biased coefficients (default False).', 'cluster': 'Column names for cluster-robust SE / penalty loadings (optional)· REQUIRED when plugin=True.', 'seed': 'Seed before the fit (determinism· default 1).', 'hdfetol': 'Convergence tolerance of the HDFE partialling-out (positive· default 1e-4).'},
        'input_example': {'data': '<df_handle>', 'dep': '...', 'indep': ['PROVIDER/DATASET/SERIES'], 'fixed': '...', 'plugin': False, 'post': False, 'seed': 1, 'hdfetol': 0.0001},
    },
    'pp_penalized_hdfe': {
        'fn': 'pp_penalized_hdfe',
        'description': 'pp_penalized_hdfe -- category 28-trade-gravity, method card #238.',
        'args': {'data': 'Handle to ONE long gravity DataFrame: one row per (exporter, importer, [time]) with a flow column (dep >= 0), regressors (indep) and fixed-effect factor columns.', 'dep': 'Column name of the dependent flow/count (bilateral trade flow, non-negative)· PPML models E[y]=exp(xbeta).', 'indep': 'Names of numeric regressor columns (>= 1): e.g. dummies of trade provisions / policies· ALL numeric, WITHOUT NA.', 'fixed': 'High-dimensional fixed effects: either a character vector of simple FE (e.g. ["exp","imp"]) or array-of-arrays for interaction FE (e.g. [["exp","time"],["imp","time"],["exp","imp"]] = exporter-time, importer-time, pair FE).', 'lambda': 'Non-negative penalization parameter (lambda=0 => unpenalized)· larger lambda => stronger shrinkage (lasso: more zeros).', 'penalty': 'Penalty type (default lasso): lasso=L1 (variable selection, zeroes coefficients)· ridge=L2 (shrinkage without zeroing).', 'plugin': 'plugin lasso (Breinlich et al. 2021): coefficient-specific data-driven penalty loadings (default False)· REQUIRES cluster.', 'cluster': 'Column names for cluster-robust SE / penalty loadings (optional)· REQUIRED when plugin=True.', 'hdfetol': 'Convergence tolerance of the HDFE partialling-out (positive· default 1e-4).'},
        'input_example': {'data': '<df_handle>', 'dep': '...', 'indep': ['PROVIDER/DATASET/SERIES'], 'fixed': '...', 'lambda': 0.5, 'plugin': False, 'hdfetol': 0.0001},
    },
    'tg_ge_gravity': {
        'fn': 'tg_ge_gravity',
        'description': 'tg_ge_gravity -- category 28-trade-gravity, method card #593.',
        'args': {'data': 'Bilateral trade panel with expenditure and production.', 'exporter': 'Exporter identifier.', 'importer': 'Importer identifier.', 'trade': 'Trade flow column.', 'counterfactual': 'Counterfactual policy variables.', 'elasticity': 'Trade elasticity.', 'tol': 'Equilibrium tolerance.'},
        'input_example': {'data': '<df_handle>', 'exporter': '...', 'importer': '...', 'trade': '...', 'counterfactual': '<df_handle>', 'elasticity': 1.0, 'tol': 1e-10},
    },
    'tg_gravity_panel': {
        'fn': 'tg_gravity_panel',
        'description': 'tg_gravity_panel -- category 28-trade-gravity, method card #594.',
        'args': {'trade': 'Bilateral trade flows.', 'covariates': 'Bilateral covariates such as distance and borders.', 'exporter': 'Exporter identifier.', 'importer': 'Importer identifier.', 'time': 'Time identifier.', 'estimator': 'Estimator.', 'fixed_effects': 'Fixed-effect structure.', 'include_intranational': 'Include intra-national trade.', 'cluster': 'Clustering.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'trade': '<df_handle>', 'exporter': '...', 'importer': '...', 'time': '...', 'estimator': 'ppml', 'fixed_effects': 'three_way', 'include_intranational': False, 'cluster': 'pair', 'conf_level': 0.95},
    },
    'tg_trade_value_added': {
        'fn': 'tg_trade_value_added',
        'description': 'tg_trade_value_added -- category 28-trade-gravity, method card #595.',
        'args': {'io_table': 'Handle to a multi-regional input-output system.', 'decomposition': 'Decomposition.', 'country': 'Country to report for; omitted = all.'},
        'input_example': {'io_table': '<raw_handle>', 'decomposition': 'koopman_wang_wei'},
    },
    'tg_gvc_participation': {
        'fn': 'tg_gvc_participation',
        'description': 'tg_gvc_participation -- category 28-trade-gravity, method card #595.',
        'args': {'io_table': 'Handle to a multi-regional input-output system.', 'measures': 'Measures to compute.'},
        'input_example': {'io_table': '<raw_handle>'},
    },
    'tg_trade_indices': {
        'fn': 'tg_trade_indices',
        'description': 'tg_trade_indices -- category 28-trade-gravity, method card #596.',
        'args': {'trade': 'Trade flows by country and product.', 'country': 'Country identifier.', 'product': 'Product identifier.', 'exports': 'Export value column.', 'imports': 'Import value column.', 'indices': 'Indices to compute; omitted = the standard set.'},
        'input_example': {'trade': '<df_handle>', 'country': '...', 'product': '...', 'exports': '...'},
    },
    'tg_ppml_hdfe': {
        'fn': 'tg_ppml_hdfe',
        'description': 'tg_ppml_hdfe -- category 28-trade-gravity, method card #597.',
        'args': {'data': 'Bilateral panel.', 'formula': 'Model formula.', 'absorb': 'Columns whose fixed effects are absorbed.', 'cluster': 'Clustering variables.', 'check_separation': 'Detect and report perfect separation.', 'conf_level': 'Confidence level for intervals.'},
        'input_example': {'data': '<df_handle>', 'formula': 'y ~ x', 'absorb': ['a', 'b'], 'check_separation': True, 'conf_level': 0.95},
    },
}
