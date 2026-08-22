# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 21-systemic-risk: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'build_er_model': {
        'fn': 'build_er_model',
        'description': 'build_er_model -- category 21-systemic-risk, method card #223.',
        'args': {'l': 'Handle to a numeric vector of row sums (total LIABILITIES of each bank), length >= 2, non-negative, without NA/Inf; sum(l)==sum(a) is required.', 'a': 'Handle to a numeric vector of column sums (total ASSETS of each bank), same length as l, non-negative.', 'targetdensity': 'Target network density ∈ (0,1] (default 0.5).', 'seed': 'Reproducibility seed of the calibration (positive integer; default 1).', 'nsamples_calib': 'Number of matrices in the calibration (positive integer; default 100).', 'thin_calib': 'Thinning during the calibration (positive integer; default 100).', 'tol': 'Relative tolerance of the sum(l)==sum(a) balance check (default 1e-6).'},
        'input_example': {'l': '<matrix_handle>', 'a': '<matrix_handle>'},
    },
    'nrm_contagion': {
        'fn': 'nrm_contagion',
        'description': 'nrm_contagion -- category 21-systemic-risk, method card #222.',
        'args': {'exposures': 'Handle to a SQUARE (n x n) non-negative matrix of bilateral exposures (assets network: A->B => A has an asset in B); e.g. the exposure_matrix from nrm_reconstruct_matrix.', 'buffer': 'Handle to a numeric non-negative vector of capital buffer per node (length n).', 'weights': 'Handle to a non-negative vector of weights per node (e.g. total assets; length n, positive sum >0). Default: equal weights rep(1,n) — unweighted.', 'shock': '"all" (default; one default scenario per node) or a JSON array of n percentage shocks in [0,1] (a single scenario).', 'method': "'debtrank' (Bardoscia et al. 2015 continuous stress propagation) or 'threshold' (traditional Furfine default cascades). Default 'debtrank'.", 'exposure_type': "Matrix interpretation: 'assets' (A->B: A has an asset in B; default) or 'liabilities' (A->B: A owes B).", 'max_it': 'Maximum propagation iterations (default 1000).', 'single_hit': "Only for method='debtrank': True => old single-hit DebtRank (Battiston et al. 2012). Default False."},
        'input_example': {'exposures': '<matrix_handle>', 'buffer': '<matrix_handle>'},
    },
    'nrm_reconstruct_matrix': {
        'fn': 'nrm_reconstruct_matrix',
        'description': 'nrm_reconstruct_matrix -- category 21-systemic-risk, method card #222.',
        'args': {'rowsums': 'Handle to a numeric vector of ASSETS per node (row sums; length >= 2, non-negative); sum(rowsums) MUST == sum(colsums).', 'colsums': 'Handle to a numeric vector of LIABILITIES per node (column sums; same length as rowsums, non-negative, equal total sum).', 'method': "Reconstruction method: 'me' Maximum Entropy (Upper & Worm 2004; dense, deterministic); 'md' Minimum Density (Anand et al. 2015; sparse, STOCHASTIC -> seed). Default 'me'.", 'seed': "Positive integer seed for reproducibility of 'md' (default 1).", 'max_it': 'Maximum iterations (default 100000).', 'abs_tol': 'Convergence tolerance (default 0.001).', 'md_c': 'md: cost of an additional link (Anand et al.; default 1).', 'md_lambda': 'md: low-density fraction for the first md_k rounds, in [0,1] (default 1).', 'md_k': 'md: low-density allocation rounds (default 100).', 'md_theta': 'md: scaling parameter prior (default 1).', 'md_remove_prob': 'md: probability of randomly removing a link, in [0,1) (default 0.01).'},
        'input_example': {'rowsums': '<matrix_handle>', 'colsums': '<matrix_handle>'},
    },
    'sample_interbank_network': {
        'fn': 'sample_interbank_network',
        'description': 'sample_interbank_network -- category 21-systemic-risk, method card #223.',
        'args': {'l': 'Handle to row sums (liabilities); same as build_er_model.', 'a': 'Handle to col sums (assets); same length as l, sum(l)==sum(a).', 'model': 'Handle to a systemicrisk model (build_er_model.model).', 'nsamples': 'Number of posterior samples of matrix L (positive integer; default 100).', 'thin': 'Thinning: theta updates per sample (positive integer; default 100).', 'seed': 'Reproducibility seed of the MCMC (positive integer; default 1). REQUIRED determinism.', 'matrpertheta': 'Matrix updates per theta update (positive integer; default length(l)^2).', 'burnin': 'Number of burn-in iterations (positive integer; default auto).', 'probs': '2 increasing quantiles ∈ (0,1) for lower/upper matrices per cell (default [0.05, 0.95]).', 'tol': 'Relative tolerance of the sum(l)==sum(a) balance check (default 1e-6).'},
        'input_example': {'l': '<matrix_handle>', 'a': '<matrix_handle>', 'model': '<raw_handle>'},
    },
    'sys_correlation_network_measures': {
        'fn': 'sys_correlation_network_measures',
        'description': 'sys_correlation_network_measures -- category 21-systemic-risk, method card #221.',
        'args': {'returns': 'Handle to a numeric matrix of daily returns; >= 3 columns; >= 90 rows (coarse pre-gate) AND >= 3 full calendar months (~>= 100 rows; post-gate n_months>=3, otherwise blocked-by-gate: with < 3 months the monthly min-max degenerates to {0,1}); without NA/NaN/Inf. All columns become network nodes.', 'seed': 'Seed (default 123) — stabilizes the eigenvector-centrality routine (ARPACK) for determinism.'},
        'input_example': {'returns': '<matrix_handle>'},
    },
    'sys_covar_delta_covar': {
        'fn': 'sys_covar_delta_covar',
        'description': 'sys_covar_delta_covar -- category 21-systemic-risk, method card #221.',
        'args': {'returns': 'Handle to a numeric matrix of returns; column 1 = the system/market index, columns 2..p = institutions (>= 2 institutions, i.e. >= 3 columns); >= 30 rows; without NA/NaN/Inf. q=0.95 is hardcoded in the package.'},
        'input_example': {'returns': '<matrix_handle>'},
    },
    'sys_covar_delta_covar_t': {
        'fn': 'sys_covar_delta_covar_t',
        'description': 'sys_covar_delta_covar_t -- category 21-systemic-risk, method card #221.',
        'args': {'returns': 'Handle to a numeric matrix of returns; column 1 = the system, columns 2..p = institutions (>= 3 columns); >= 50 rows; without NA/NaN/Inf.', 'state_variables': 'Handle to a numeric matrix of state variables (e.g. VIX, spreads); >= 2 columns (NSV=1 breaks the package); same number of rows as returns; without NA/NaN/Inf.'},
        'input_example': {'returns': '<matrix_handle>', 'state_variables': '<matrix_handle>'},
    },
    'sys_scale': {
        'fn': 'sys_scale',
        'description': 'sys_scale -- category 21-systemic-risk, method card #221.',
        'args': {'x': 'Handle to a numeric vector (>= 2 elements, non-constant, without NA/NaN/Inf); min-max into [0,1].'},
        'input_example': {'x': '<matrix_handle>'},
    },
    'sr_mes_srisk': {
        'fn': 'sr_mes_srisk',
        'description': 'sr_mes_srisk -- category 21-systemic-risk, method card #553.',
        'args': {'returns': 'Institution return panel.', 'market': 'Market return.', 'liabilities': 'Book liabilities per institution.', 'market_cap': 'Market capitalisation per institution.', 'crisis_decline': 'Assumed market decline defining the crisis.', 'prudential_ratio': 'Required capital ratio.', 'horizon': 'Crisis horizon in days.', 'seed': 'Seed for the random number generator; required for reproducibility.'},
        'input_example': {'returns': '<df_handle>', 'market': '<series_handle>', 'crisis_decline': 0.4, 'prudential_ratio': 0.08, 'horizon': 126, 'seed': 1},
    },
    'sr_absorption_ratio': {
        'fn': 'sr_absorption_ratio',
        'description': 'sr_absorption_ratio -- category 21-systemic-risk, method card #554.',
        'args': {'returns': 'Asset or institution return panel.', 'n_components': 'Leading components counted; omitted = a fifth of the assets.', 'window': 'Rolling window in periods.', 'short_window': 'Short window for the standardised change.'},
        'input_example': {'returns': '<df_handle>', 'window': 500, 'short_window': 15},
    },
    'sr_granger_network': {
        'fn': 'sr_granger_network',
        'description': 'sr_granger_network -- category 21-systemic-risk, method card #555.',
        'args': {'returns': 'Institution return panel.', 'lags': 'Lag order for the pairwise tests.', 'adjust': 'Multiplicity adjustment.', 'window': 'Rolling window; omitted = full sample.', 'alpha': 'Significance level.'},
        'input_example': {'returns': '<df_handle>', 'lags': 1, 'adjust': 'fdr', 'alpha': 0.05},
    },
    'sr_network_topology': {
        'fn': 'sr_network_topology',
        'description': 'sr_network_topology -- category 21-systemic-risk, method card #555.',
        'args': {'adjacency': 'Directed adjacency matrix.', 'measures': 'Measures to compute; omitted = the standard set.'},
        'input_example': {'adjacency': '<matrix_handle>'},
    },
    'sr_stress_index': {
        'fn': 'sr_stress_index',
        'description': 'sr_stress_index -- category 21-systemic-risk, method card #556.',
        'args': {'indicators': 'Stress indicators, one column each.', 'segments': 'Segment label per indicator.', 'transform': 'Transformation to a common scale.', 'recursive': 'Use recursive rather than full-sample transformation.', 'correlation_window': 'Window for the time-varying correlation.'},
        'input_example': {'indicators': '<df_handle>', 'transform': 'empirical_cdf', 'recursive': True, 'correlation_window': 250},
    },
    'sr_correlation_filter': {
        'fn': 'sr_correlation_filter',
        'description': 'sr_correlation_filter -- category 21-systemic-risk, method card #557.',
        'args': {'correlation': 'Correlation matrix.', 'method': 'Filtering method.', 'threshold': 'Correlation threshold when thresholding.', 'metric': 'Correlation-to-distance transform.'},
        'input_example': {'correlation': '<matrix_handle>', 'method': 'mst', 'threshold': 0.5, 'metric': 'sqrt_2_1_minus_rho'},
    },
}
