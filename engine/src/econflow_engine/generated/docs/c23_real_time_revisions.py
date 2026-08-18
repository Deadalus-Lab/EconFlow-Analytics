# SPDX-License-Identifier: AGPL-3.0-only
# ============================================================
# GENERATED FILE -- DO NOT EDIT.
# Source: artifacts/node-specs.v1.json (committed) via scripts/gen_schemas.py.
# Rebuild with: python scripts/gen_schemas.py
# ============================================================

"""Tier 3 for category 23-real-time-revisions: descriptions and input examples.

A worker executing a graph must NOT import from here -- this tier is
roughly 80% of the artifact and none of it is needed to run a node.
"""

from typing import Any

NODE_DOCS: dict[str, dict[str, Any]] = {
    'analyze_revisions': {
        'fn': 'analyze_revisions',
        'description': 'analyze_revisions -- category 23-real-time-revisions, METHOD-SELECTION card #229.',
        'args': {'df': 'Handle to a long vintage DataFrame {time, pub_date, value}.', 'n_releases': 'Number of initial releases to analyze (0..n_releases; default 3).', 'final_release': 'Final release as benchmark: "latest" (default) or an integer-string (e.g. "10").', 'degree': 'Detail level 1..5 (default 5=all): 1 magnitude/bias; 2 correlation; 3 news/noise tests; 4 Theil/sign/seasonality; 5 full.'},
        'input_example': {'df': '<df_handle>', 'n_releases': 3, 'degree': 5},
    },
    'build_revision_triangle': {
        'fn': 'build_revision_triangle',
        'description': 'build_revision_triangle -- category 23-real-time-revisions, METHOD-SELECTION card #229.',
        'args': {'df': 'Handle to a long vintage DataFrame {time(Date), pub_date(Date), value(numeric)} of A SINGLE series; >= 2 vintages & >= 2 reference periods.'},
        'input_example': {'df': '<df_handle>'},
    },
    'compute_revisions': {
        'fn': 'compute_revisions',
        'description': 'compute_revisions -- category 23-real-time-revisions, METHOD-SELECTION card #229.',
        'args': {'df': 'Handle to a long vintage DataFrame {time, pub_date, value}.', 'mode': 'Revision-computation reference (default interval): interval=lag in vintages; nth_release=nth release; ref_date=fixed publication date.', 'interval': "mode='interval': positive integer lag in vintages (default 1).", 'nth_release': 'mode=\'nth_release\': "latest" or a non-negative integer (as a string, e.g. "0").', 'ref_date': "mode='ref_date': publication date 'YYYY-MM-DD' that EXISTS in the data."},
        'input_example': {'df': '<df_handle>', 'interval': 1},
    },
    'first_efficient_release': {
        'fn': 'first_efficient_release',
        'description': 'first_efficient_release -- category 23-real-time-revisions, METHOD-SELECTION card #229.',
        'args': {'df': 'Handle to a long vintage DataFrame {time, pub_date, value}.', 'n_releases': 'Number of releases to check (0..n_releases; default 5).', 'final_release': 'Final release benchmark: "latest" (default) or an integer-string.', 'significance': 'Significance level of the joint MZ test in (0,1) (default 0.05).', 'robust': 'HAC (Newey-West) robust standard errors (default True).', 'test_all': 'Check of ALL releases (default False = stop at the 1st efficient one).'},
        'input_example': {'df': '<df_handle>', 'n_releases': 5, 'significance': 0.05, 'robust': True, 'test_all': False},
    },
    'nowcast_revisions': {
        'fn': 'nowcast_revisions',
        'description': 'nowcast_revisions -- category 23-real-time-revisions, METHOD-SELECTION card #229.',
        'args': {'df': 'Handle to a long vintage DataFrame {time, pub_date, value}.', 'e': 'Index of the first efficient release (> 0; from first_efficient_release$e); e < n_releases is required.', 'n_releases': 'Number of releases for the state-space (0..n_releases; default 6).', 'method': 'Model (default jvn): jvn=Jacobs-van Norden news/noise; kk=Kishor-Koenig.', 'h': 'Forecast horizon (non-negative integer; default 0).', 'seed': 'Seed before the MLE (determinism; default 1).'},
        'input_example': {'df': '<df_handle>', 'e': 1, 'n_releases': 6, 'h': 0, 'seed': 1},
    },
}
