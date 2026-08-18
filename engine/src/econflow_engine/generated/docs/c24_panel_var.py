# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 24-panel-var: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'pv_bootstrap': {
        'fn': 'pv_bootstrap',
        'description': 'pv_bootstrap -- category 24-panel-var, METHOD-SELECTION card #230.',
        'args': {'fit': 'Handle to an IDENTIFIED panel SVAR (pv_identify$fit).', 'method': 'Bands (default pmb): pmb=panel moving-block bootstrap· mg=mean-group inference (spread of N individuals); mb=individual moving-block bootstrap of one individual.', 'n_ahead': 'IRF horizon (positive integer; default 20).', 'n_boot': 'Bootstrap iterations for pmb/mb (positive integer; default 100).', 'b_length': "method='mb': residual block length (positive integer; default 1; ~T/10).", 'b_dim': "method='pmb': block dimensions (temporal, cross-sectional); default [1,1] i.i.d.", 'individual': "method='mb': individual to bootstrap (name or position 1..N).", 'level': 'Confidence level of the bands ∈ (0,1) (default 0.90).', 'seed': 'Seed for pmb/mb (determinism; default 1).'},
        'input_example': {'fit': '<raw_handle>', 'n_ahead': 20, 'n_boot': 100, 'b_length': 1, 'b_dim': [1, 1], 'level': 0.9, 'seed': 1},
    },
    'pv_cointegration': {
        'fn': 'pv_cointegration',
        'description': 'pv_cointegration -- category 24-panel-var, METHOD-SELECTION card #230.',
        'args': {'df': 'Handle to a long panel DataFrame {id_col + K variables}, as in pv_estimate.', 'variables': 'Names of the K (>=2) endogenous columns in system order.', 'lags': 'Common lag order p (positive integer) of the VAR in levels.', 'test': 'Procedure (default JO): JO=Johansen trace (panel); BR=Breitung two-step pooled· SL=Saikkonen-Luetkepohl· CAIN=Arsova-Oersal.', 'id_col': "Individual identity column name (default 'id').", 'det_case': "Deterministic term for JO/BR (default Case1); SL/CAIN ignore it and use 'SL_trend'.", 'n_factors': 'PANIC common factors (Arsova-Oersal) for JO/SL (default inactive).'},
        'input_example': {'df': '<df_handle>', 'variables': ['PROVIDER/DATASET/SERIES'], 'lags': 1, 'id_col': 'id'},
    },
    'pv_estimate': {
        'fn': 'pv_estimate',
        'description': 'pv_estimate -- category 24-panel-var, METHOD-SELECTION card #230.',
        'args': {'df': 'Handle to a long panel DataFrame: identity column `id_col` + K numeric variable columns (same order k=1..K in each individual); >= 2 individuals, without NA.', 'variables': 'Names of the K (>=2) endogenous columns in system order.', 'lags': 'Common lag order p (positive integer) of the VAR in levels.', 'id_col': "Individual identity column name (default 'id').", 'model': 'VAR = mean-group VAR in levels (default); VEC = (pooled) mean-group rank-restricted VECM.', 'type': 'Deterministic term. VAR: const/trend/both/none (default const)· VEC: Case1..Case5 (default Case4).', 'dim_r': "model='VEC': common cointegration rank r (1..K-1); required for VEC.", 'n_factors': 'Number of common factors for SUR (default inactive).', 'n_iterations': 'Maximum iterations of SUR/pooled cointegrating vectors (default inactive).'},
        'input_example': {'df': '<df_handle>', 'variables': ['PROVIDER/DATASET/SERIES'], 'lags': 1, 'id_col': 'id'},
    },
    'pv_identify': {
        'fn': 'pv_identify',
        'description': 'pv_identify -- category 24-panel-var, METHOD-SELECTION card #230.',
        'args': {'fit': 'Handle to an UNIDENTIFIED panel VAR/VEC (pv_estimate$fit).', 'method': 'Identification (default chol): chol=recursive/Cholesky; cvm=Cramer-von Mises ICA· dc=distance-covariance ICA· iv=proxy/IV; grt=SVEC long/short-run (REQUIRES a VEC fit).', 'n_ahead': 'IRF horizon (positive integer; default 20).', 'fevd_ahead': 'FEVD horizon (positive integer; default 10).', 'order_k': "method='chol': causal ordering (variable names or integer positions).", 'combine': 'cvm/dc: group/pool/indiv (default indiv)· iv: pool/indiv (default pool); combination of individuals.', 'iv': "method='iv': handle to a proxy DataFrame (L columns, T-lags rows).", 'S2': "method='iv' with multiple proxies: MR/JL/NQ (default MR; pool=>NQ).", 'cov_u': "method='iv': residual covariance OMEGA (÷T) or SIGMA (÷T-n) (default OMEGA).", 'LR': "method='grt': K×K long-run restriction matrix (NA=free, 0=zero).", 'SR': "method='grt': K×K short-run restriction matrix (NA=free).", 'n_factors': "cvm/dc combine='group': number of common structural shocks (default inactive).", 'seed': 'Seed for cvm/dc (DEoptim/steadyICA; determinism; default 1).'},
        'input_example': {'fit': '<raw_handle>', 'n_ahead': 20, 'fevd_ahead': 10, 'seed': 1},
    },
}
