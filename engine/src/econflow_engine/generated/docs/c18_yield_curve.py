# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 18-yield-curve: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'atsm_estimate': {
        'fn': 'atsm_estimate',
        'description': 'atsm_estimate -- category 18-yield-curve, METHOD-SELECTION card #211.',
        'args': {'model_type': "Type of single-country JPS ATSM (default 'JPS original'; GVAR/JLL/multi out of scope for this node).", 'economy': "A single economy; must exist in yields ('Y<mat>M_<economy>') and dom_macro.", 'n_factors': 'Number of country-specific spanned factors N (>=1, < #maturities).', 'global_var': "Names of global variables (rownames of global_macro; default 'Gl_Eco_Act').", 'dom_var': "Names of domestic variables ('<dom_var> <economy>' in dom_macro; default 'Eco_Act').", 'init_date': "Sample start 'dd-mm-yyyy' (within the data range, < final_date).", 'final_date': "Sample end 'dd-mm-yyyy' (within the data range, > init_date).", 'data_freq': "Data frequency (default 'Monthly'; determines the dt annualization).", 'stationary_Q': 'StatQ: enforcement of maximum eigenvalue under Q < 1 (default False).', 'horizon': 'Analysis horizon of the term-premia decomposition (default 25).', 'compute_term_premia': 'True -> model-implied yields + term premia + expected component; False -> estimation only (default True).', 'yields': "Handle to a numeric matrix of yields (rows 'Y<mat>M_<economy>' × dates 'dd-mm-yyyy', with rownames/colnames); None -> built-in 'CM_2024'.", 'global_macro': 'Handle to a numeric matrix of global macro (variables × dates); None -> built-in; ALL-or-NONE with yields/dom_macro.', 'dom_macro': "Handle to a numeric matrix of domestic macro ('<var> <economy>' × dates); None -> built-in."},
        'input_example': {'n_factors': 1, 'stationary_Q': False, 'horizon': 25, 'compute_term_premia': True},
    },
    'fit_nelson_siegel': {
        'fn': 'fit_nelson_siegel',
        'description': 'fit_nelson_siegel -- category 18-yield-curve, METHOD-SELECTION card #87.',
        'args': {'rates': 'Handle to a yield matrix [n_obs x n_maturities] (rows = dates, columns = maturities).', 'maturities': 'Handle to a strictly increasing numeric vector of maturities (>= 4 pillars; same count as the columns of rates).'},
        'input_example': {'rates': '<matrix_handle>', 'maturities': '<matrix_handle>'},
    },
    'fit_svensson': {
        'fn': 'fit_svensson',
        'description': 'fit_svensson -- category 18-yield-curve, METHOD-SELECTION card #87.',
        'args': {'rates': 'Handle to a yield matrix [n_obs x n_maturities] (rows = dates, columns = maturities).', 'maturities': 'Handle to a strictly increasing numeric vector of maturities (>= 6 pillars; same count as the columns of rates).', 'which_rate': "Curve type for fitted/residuals; default 'Spot' = the quantity comparable to the observed yields."},
        'input_example': {'rates': '<matrix_handle>', 'maturities': '<matrix_handle>'},
    },
    'yc_fit': {
        'fn': 'yc_fit',
        'description': 'yc_fit -- category 18-yield-curve, METHOD-SELECTION card #210.',
        'args': {'maturities': 'Maturities in years; positive & STRICTLY INCREASING (same count as the columns of the yields).', 'rates': 'Yields of ONE curve (decimals, same length as maturities); give rates OR panel, NOT both.', 'panel': 'Handle to a yield matrix [n_obs × n_maturities] (time series of curves; nelson_siegel+panel = Diebold-Li factor dynamics).', 'method': 'Fit method (default nelson_siegel; min pillars: NS 4 / svensson 6 / cubic 3).', 'type': 'Type of yields (default zero).', 'tau_init': 'Initial decay value tau (nelson_siegel; > 0; default 1).', 'tau1_init': 'Initial value of the 1st decay tau1 (svensson; > 0; default 1).', 'tau2_init': 'Initial value of the 2nd decay tau2 (svensson; > 0; default 5).', 'weights': 'Positive weights per maturity (nelson_siegel/svensson; NOT cubic_spline); emphasis on liquid tenors.', 'dates': 'Date labels per row of the panel (count = panel rows); labels only, not model input.'},
        'input_example': {'maturities': [0.5, 0.5], 'tau_init': 1, 'tau1_init': 1, 'tau2_init': 5},
    },
    'yc_transform': {
        'fn': 'yc_transform',
        'description': 'yc_transform -- category 18-yield-curve, METHOD-SELECTION card #210.',
        'args': {'object': 'Handle to yc_fit$object: fitted yc_curve (spot/forward/discount) or panel matrix (pca).', 'transform': 'Transformation (default spot); spot/forward/discount require yc_curve; pca requires a panel matrix.', 'grid': "Maturity grid (positive maturities) for spot/forward/discount; None -> the curve's maturities.", 'horizon': "Forward-forward horizon (> 0) for transform='forward'; None -> instantaneous forward.", 'compounding': "Compounding convention for transform='discount' (default continuous).", 'n_components': "Number of principal components for transform='pca' (∈ [1, min(n_obs-1, n_maturities)]; default 3).", 'scale': 'Scaling of variables before the PCA (default False = covariance, standard in yield-curve PCA).'},
        'input_example': {'object': '<raw_handle>', 'n_components': 3, 'scale': False},
    },
    'ycevo_estimate': {
        'fn': 'ycevo_estimate',
        'description': 'ycevo_estimate -- category 18-yield-curve, METHOD-SELECTION card #212.',
        'args': {'data': 'Handle to a bond cash-flow panel with columns qdate(Date), id, price, tupq(>0, days), pdint.', 'x': "Estimation time points as dates 'YYYY-MM-DD' (same class/range as qdate).", 'tau': "Maturity grid in years (>0); default None = the package's automatic grid.", 'span_x': 'Half-width of the kernel time window (default 60; ignored if hx is given).', 'hx': 'Bandwidths per point x (positive; length = length(x)); overrides span_x.', 'ht': 'Bandwidths per maturity tau (positive; length = length(tau); requires explicit tau).', 'smooth': 'loess smoothing of the curve with respect to tau (default False = raw estimator points).'},
        'input_example': {'data': '<df_handle>', 'x': ['PROVIDER/DATASET/SERIES'], 'span_x': 60, 'smooth': False},
    },
}
