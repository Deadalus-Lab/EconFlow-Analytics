<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 26-text-as-data

1 METHOD-SELECTION card, 1 module, 4 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #234 — Textual sentiment pipeline (corpus -> lexicon sentiment -> time aggregation -> elastic-net sparse-regression forecasting)

**Module:** `textual_sentiment_pipeline.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `snt_corpus` | `df` | `df_handle`, `boolean` | `do_clean=False` | `light` | `corpus` |
| `snt_sentiment` | `corpus` | `raw_handle`, `series_codes`, `enum` | — | `light` | `sentiment` |
| `snt_measures` | `sentiment` | `raw_handle`, `enum`, `integer`, `series_codes`, `enum`, `enum`, `boolean` | `lag=1`, `do_ignore_zeros=True` | `light` | `measures` |
| `snt_model` | `measures`, `y` | `raw_handle`, `num_array`, `enum`, `enum`, `num_array`, `integer`, `boolean`, `integer`, `integer`, `integer` | `h=0`, `do_intercept=True`, `seed=1` | `light` | — |

### Use when

you have time-stamped TEXT (news/reports/tweets) {id,date,texts,+features} and you want to turn it into numeric sentiment indicators and forecast a macro variable: (a) build the corpus, (b) compute the lexicon-based document sentiment, (c) aggregate it over time into several measures (lexicon×feature×time scheme), (d) run a sparse elastic-net (glmnet) regression y~measures

### Do not use when

you have no text (only numeric series -> #219/#220 shrinkage/ML); you want a general sparse regression with no textual sentiment (glmnet/BMS directly); word embeddings/transformer NLP (outside the surface); data ingestion (a file upload — a frontend route, not a node)

### Alternatives

| instead use | when |
| --- | --- |
| snt_corpus | the first step: a df {id,date,texts,+numeric features} -> a sento_corpus (a register handle for the chain) |
| snt_sentiment (how ∈ counts/proportional/TFIDF/UShaped/..) | lexicon-based document sentiment with >=1 built-in lexicons (LM_en/HENRY_en/GI_en/FEEL/..) and a within-document weighting |
| snt_measures (by/lag/how_time/how_docs/fill) | the temporal aggregation of the document sentiment into measure time series; how_time (equal_weight/linear/almon/beta/exponential) — ALL of them are tried -> nmeasures=lexicons×features×time |
| snt_model (model=gaussian/binomial/multinomial, type=BIC/AIC/Cp/cv) | a sparse elastic-net (glmnet) regression of y on the measures; the (alpha,lambda) pair is selected by an information criterion (gaussian only) or by out-of-sample cross-validation (also for classification) |

### Output fields

- snt_corpus: corpus (a register raw_handle) + n_documents/date_min/date_max/features/n_features
- snt_sentiment: sentiment (a register raw_handle; the data.table -> per-document records = chart-data) + sentiment_columns (lexicon--feature)/lexicons/how
- snt_measures: measures (a register raw_handle) + measures_table (date + the measure columns = chart-data) + measure_names/n_measures/n_dates/dates/dimensions(features,lexicons,time)
- snt_model: a coefficients df {term,coefficient} (multinomial: + class) + alpha/lambda (as selected)/n_predictors/n_selected (the non-zero ones excluding the intercept)/a discarded df/ic_criterion (NA under cv)/fit_dates + the raw fit (to_mcp -> a stub)

### Pitfalls

- a 4-stage CHAIN: each stage REGISTERS the raw object as a handle (a raw_handle) that feeds the next one; snt_model is TERMINAL
- the information criteria (type=BIC/AIC/Cp) apply ONLY to model='gaussian'; binomial/multinomial REQUIRE type='cv' (with train_window/test_window)
- y MUST be aligned with the measure dates (length == n_dates); gaussian numeric; binomial 2 values; multinomial >=3 values
- how_time & alphas are vectors that are tried (ALL of them, NOT match.arg); howTime='own' is not supported (a custom weight matrix)
- alpha=0=ridge, alpha=1=lasso (the elastic-net mixing); n_selected = the sparse (non-zero) coefficients; a higher lambda => a sparser model
- the seed pins the caret cv fold RNG (defence in depth; the IC path is deterministic anyway)
- MASKING: type='cv' triggers a runtime require(caret) (=> ggplot2/lattice are attached); the wrapper calls no bare generic (everything is sentometrics::/stats::); library(sentometrics) does not attach data.table/quanteda

### References

- sentometrics v1.0.1 ref manual (the sento_corpus/sento_lexicons/compute_sentiment/ctr_agg/aggregate.sentiment/ctr_model/sento_model help pages)
- Ardia, Bluteau, Boudt, Borms & Vrontos 2021 'The the reference Package sentometrics to Compute, Aggregate, and Predict with Textual Sentiment' Journal of Statistical Software 99(2) https://doi.org/10.18637/jss.v099.i02
- Ardia, Bluteau & Boudt 2019 'Questioning the news about economic growth: Sparse forecasting using thousands of news-based sentiment values' International Journal of Forecasting 35(4) 1370-1386
- Loughran & McDonald 2011 'When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks' Journal of Finance 66(1) 35-65 (the LM lexicon); Henry 2008 (the HENRY lexicon); Stone et al. General Inquirer (the GI lexicon)
- Zou & Hastie 2005 'Regularization and variable selection via the elastic net' JRSS-B 67(2) 301-320; Friedman, Hastie & Tibshirani 2010 'Regularization Paths for Generalized Linear Models via Coordinate Descent' JSS 33(1) (glmnet)
- wrapper footer IMPLEMENTATION NOTE (c26_text_as_data/textual_sentiment_pipeline)
