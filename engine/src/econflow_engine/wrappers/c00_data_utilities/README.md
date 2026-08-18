<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 00-data-utilities

35 METHOD-SELECTION cards, 35 modules, 176 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #78 — Time series class unification + basic transformations (convert/diff/pc/index/scale/lag/aggregate/span/combine/summary)

**Module:** `time_series_class.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ts_convert` | `x` | `series_handle`, `enum` | — | `light` | — |
| `ts_transform` | `x` | `series_handle`, `enum` | — | `light` | — |
| `ts_rebase` | `x` | `series_handle`, `string` | — | `light` | — |
| `ts_standardize` | `x` | `series_handle`, `boolean`, `boolean` | `center=True`, `scale=True` | `light` | — |
| `ts_lag_series` | `x` | `series_handle`, `integer` | `by=1` | `light` | — |
| `ts_aggregate` | `x` | `series_handle`, `enum`, `enum`, `boolean` | `na_rm=False` | `light` | — |
| `ts_limit_span` | `x` | `series_handle`, `string`, `string`, `boolean` | `extend=False` | `light` | — |
| `ts_fill_regular` | `x` | `series_handle`, `number` | — | `light` | — |
| `ts_combine` | `series1`, `series2` | `series_handle`, `series_handle`, `enum` | — | `light` | — |
| `ts_stats` | `x` | `series_handle`, `boolean` | `spark=False` | `light` | — |

### Use when

after the fetch; unified class conversion (ts/xts/tsibble/df) + standard analyst transformations (diff/%/index/z/lag/aggregate/span)

### Do not use when

charts (frontend); INCREASING the frequency -> tempdisagg #79; filling NA -> imputeTS #80 (ts_fill_regular only inserts NA gaps)

### Alternatives

| instead use | when |
| --- | --- |
| #82 macro-arithmetic | you need explicit macro conventions + post-checks (annualize/deflate/contributions additivity) |
| ts_aggregate | consistency-preserving aggregation is not needed -> plain aggregate suffices |

### Output fields

- series: transformed object (ts->{values,start,frequency}, mts/matrix->nested rows, df->records)
- class/n/freq: compact metadata + applied arguments
- transform: pc=q/q%, pcy=YoY%, pca=annualized pc, diff=plain difference

### Pitfalls

- ts_rebase/ts_index: index=1 (NOT 100); base=A DATE (NOT a number); base=100 errors -> for base=100 see macro_rebase #82
- ts_aggregate: ONLY towards a lower frequency (hard gate)
- tsbox detects the time column from its CLASS (Date/POSIXct) — long-df (upload) as is

### References

- Sax, tsbox: Class-Agnostic Time Series (docs.ropensci.org/tsbox, tsbox)

## #79 — Temporal (dis)aggregation of series (Chow-Lin/Fernandez/Litterman/Denton disaggregation + aggregation)

**Module:** `temporal_aggregation_series.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `td_disaggregate` | `formula` | `formula`, `enum`, `string`, `enum`, `enum`, `integer` | `to='quarterly'`, `h=1` | `light` | — |
| `td_aggregate` | `x` | `series_handle`, `enum`, `string` | `to='annual'` | `light` | — |

### Use when

consistency-preserving frequency change; low->high (td, with/without an indicator) or high->low (ta, sum/average/first/last)

### Do not use when

plain aggregation without consistency -> ts_aggregate #78; scattered NA -> imputeTS #80; forecasting

### Alternatives

| instead use | when |
| --- | --- |
| method=chow-lin-maxlog (default) | with an indicator, broad range (recommended) |
| method=fernandez/litterman | underlying series I(1)/random-walk-like |
| method=denton-cholette/fast | WITHOUT an indicator, smooth interpolation |

### Output fields

- disaggregated: high-frequency ts (->{values,start,frequency}) — the main result
- low_span/high_span: requested vs realized spans (data-integrity)
- coefficients/se/rho/method/conversion/fr + r_squared/aic/bic/logl/rss (GLS regression stats)
- residuals/fitted_low/actual: LOW-frequency (input level, not output)

### Pitfalls

- SPAN GATE: the indicator MUST cover the low-freq series; otherwise silent truncation/extrapolation -> escalated to stop
- Denton methods leave regression stats NULL->NA — NOT a 'bad fit', there is no regression
- conversion must match: flow->sum, index/rate->average, stock->last/first (wrong = consistent but WRONG)

### References

- Sax & Steiner, Temporal Disaggregation of Time Series, 5(2):80-88, 2013 (doi:10.32614/RJ-2013-028)
- Chow & Lin 1971 (Rev. Econ. Stat. 372-375)
- Denton 1971 (JASA 66(333):99-102)
- Santos Silva & Cardoso 2001 (Economic Modelling 18:269, dynamic Chow-Lin)

## #80 — Replacement of missing values (NA) in time series (Kalman/interpolation/seadec + statsNA)

**Module:** `replacement_missing_values.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `imputets_kalman` | `x` | `series_handle`, `enum`, `boolean`, `number` | `smooth=True` | `light` | — |
| `imputets_interpolation` | `x` | `series_handle`, `enum`, `number` | — | `light` | — |
| `imputets_seadec` | `x` | `series_handle`, `enum`, `boolean`, `number`, `integer` | `find_frequency=False`, `seed=42` | `light` | — |
| `imputets_statsna` | `x` | `series_handle`, `integer` | `bins=4` | `light` | — |

### Use when

scattered/internal NA; pattern mapping (statsNA) + filling for methods that do not tolerate gaps (VAR/filters/ACF)

### Do not use when

frequency difference (not a gap) -> tempdisagg #79; missing tail (forecast) -> cat.02; NA gaps kept as NA without filling -> ts_fill_regular #78

### Alternatives

| instead use | when |
| --- | --- |
| na_kalman (default) | series with trend/seasonality, medium gaps |
| na_interpolation (linear/spline/stine) | fast, model-free, small gaps |
| na_seadec | strong seasonality to preserve (requires ts freq>1, >=2 periods) |

### Output fields

- imputed: ts/numeric (->{values,start,frequency}) + parameters
- n_imputed: NA positions that were filled; n_remaining_na: remaining ones (>maxgap)
- na_report: statsNA as data (length/number/percentage_NAs numeric/gaps/longest/most_weighty)

### Pitfalls

- n_remaining_na>0 is NOT an error — it is the deliberate maxgap cut-off (long NA runs stay NA)
- algorithm='random' is stochastic -> an enforced seed (default 42L) for reproducibility
- bins affects ONLY the print table; gap_distribution is UNBINNED (per exact gap length)
- imputed values carry no uncertainty — take care if they enter inference as observations

### References

- Moritz & Bartz-Beielstein, imputeTS, 9(1):207-218, 2017 (doi:10.32614/RJ-2017-009)
- Harvey 1990 (Forecasting, Structural TS Models and the Kalman Filter)
- Hyndman & Khandakar 2008 (JSS 26(3), auto.arima state-space)

## #81 — Descriptive statistics as data (ACF/PACF/CCF/rolling/correlation matrix + per-pair correlation inference)

**Module:** `descriptive_statistics.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `desc_acf` | `x` | `series_handle`, `integer`, `boolean` | `demean=True` | `light` | — |
| `desc_pacf` | `x` | `series_handle`, `integer` | — | `light` | — |
| `desc_ccf` | `x`, `y` | `series_handle`, `series_handle`, `integer` | — | `light` | — |
| `desc_rolling` | `x`, `width` | `series_handle`, `integer`, `enum`, `enum` | — | `light` | — |
| `desc_correlations` | `data` | `matrix_handle`, `enum`, `string` | `use='pairwise.complete.obs'` | `light` | — |
| `desc_cor_test` | `data` | `matrix_handle`, `enum`, `enum`, `enum`, `number`, `enum`, `boolean`, `boolean` | `conf_level=0.95`, `continuity=False` | `light` | — |

### Use when

pre-model exploration/diagnostics; ARMA order id (ACF/PACF), lead/lag (CCF), rolling stats, correlation matrix — all numeric data; desc_cor_test when you need INFERENCE (p-values/CI) per pair with multiplicity control

### Do not use when

formal stationarity (ACF is indicative -> ADF/KPSS cat.01); causality (CCF != Granger); partial/conditional correlation (conditioning on third variables -> regression cat.06/07); autocorrelated series without prewhitening (the i.i.d. null of cor_test is violated -> inflated Type I)

### Prerequisites

- c01_preparation_prechecks/unit_root_normality.run_adf_test (stationarity before interpreting ACF/PACF)
- c00_data_utilities/replacement_missing_values.imputets_kalman (fill NA first — the input gate rejects NA/Inf)

### Alternatives

| instead use | when |
| --- | --- |
| ACF cut-off -> MA(q), PACF cut-off -> AR(p) | Box-Jenkins order identification — use them together |
| method=spearman/kendall | rank-based, robust to non-linearity/outliers vs pearson (linear) |
| desc_rolling align=center | smoothing (non-causal) vs align=right (causal, default) |
| desc_correlations vs desc_cor_test | desc_correlations = POINT estimates (p×p matrix, no hypothesis, no p-value) -> exploration/heatmap. desc_cor_test = per-pair INFERENCE (statistic, df, p-value, conf.int) + MANDATORY multiplicity correction. The point estimates are IDENTICAL (test-covered) — the difference is ONLY the inference |
| p.adjust.method=BH (default) vs holm/bonferroni | BH controls the FDR (more powerful, for screening many pairs); holm/hochberg/hommel/bonferroni control the FWER (when EVERY false positive is costly). Bonferroni is dominated by holm — use holm. The alias 'fdr' is NOT exposed (identical to BH) |
| use=pairwise.complete.obs (default) vs complete.obs | pairwise = maximum n per pair but a DIFFERENT sample per pair (p-values are not strictly comparable); complete.obs = listwise drop, a COMMON sample across all pairs (comparable, smaller n); na.fail = hard stop on any NA |

### Output fields

- acf/pacf/ccf: numeric + lag + n_used; ci_upper/ci_lower = ±1.96/sqrt(n) white-noise band
- desc_rolling: rolled (index-aligned, fill=NA at the edges) + index
- desc_correlations: correlation (matrix->nested+dimnames), n=rows supplied, n_pairwise=per-pair complete
- desc_cor_test: pairs = tidy records PER PAIR (var1, var2, n, estimate, statistic, statistic_name, parameter, p_value, p_adjusted, conf_low, conf_high, ties, exact_used); ALWAYS read p_adjusted, NOT p_value
- desc_cor_test: pair_order = an EXPLICIT deterministic order (upper triangle by COLUMN INDEX (1,2),(1,3),..,(p-1,p) — NOT alphabetical), so that stored workflows reproduce (§5)
- desc_cor_test: n_rows_input / n_rows_used / n_missing_cells (n_missing_cells is measured BEFORE the listwise drop); any_ties / any_exact_fallback / warnings = degradation flags

### Pitfalls

- non-stationary series: the ACF decays slowly and linearly (an artefact, not structure) — test stationarity first
- CCF: with ccf(x, y) (as the wrapper calls it) lag k estimates cor(x[t+k], y[t]) -> NEGATIVE lags = x leads y (x leads, peak at lag<0), POSITIVE lags = x lags behind (y leads); confirm the lag sign in the raw object before concluding lead/lag
- desc_correlations: with pairwise.complete.obs & NA the scalar n OVERSTATES — read n_pairwise (a strong corr with a small n_pairwise is fragile)
- desc_cor_test: kendall/spearman define NEITHER conf.int NOR df — the wrapper returns an explicit NA in conf_low/conf_high/parameter (NEVER a silently omitted field). Source: the cor_test routine «conf.int.. Currently only given for Pearson's.. at least 4 complete pairs» (live-verified: is.null(conf.int)==TRUE for kendall & spearman)
- desc_cor_test: with ties cor_test silently DOWNGRADES the exact p-value to an asymptotic approximation and ONLY warns ('cannot compute exact p-value with ties'). The wrapper exposes this as DATA: ties / exact_used / any_exact_fallback / warnings (each warning carries its pair). Check exact_used before trusting small p-values
- desc_cor_test: for spearman with n>1290 AS 89 is abandoned silently (WITHOUT a warning) in favour of the t-approximation. the cor_test routine states 'n < 1290' while the stats code checks 'n <= 1290' — the wrapper encodes the CODE (live-verified), which is why exact_used is reliable
- desc_cor_test: on a constant (zero-variance) column cor_test does NOT error — it ONLY warns ('the standard deviation is zero') and returns an NA estimate/p-value (live-verified for all 3 methods). The wrapper makes this a HARD GATE, per column AND per pair (a column may have variance overall yet be constant on the common non-NA rows of a pair)
- desc_cor_test: for pearson cor_test SILENTLY ignores exact/continuity (live-verified: identical p-value, no warning) -> the wrapper makes them a hard gate so the user does not think they had an effect
- desc_cor_test: the i.i.d. null of cor_test is violated for autocorrelated macro series -> inflated Type I error. For lead/lag in time series use desc_ccf (with prewhitening) or Granger (cat.06), NOT desc_cor_test on raw levels
- desc_cor_test: the single n>=4 gate is DELIBERATELY stricter than the per-method minimum (pearson n>=3, kendall/spearman n>=2 — live-verified) so that the output schema does not change silently with the method; at n=2/3 kendall/spearman return a degenerate \|r\|=1 with p=1

### References

- base stats help (acf, pacf, ccf, cor) + zoo help (rollapply, zoo)
- Box, Jenkins & Reinsel, Time Series Analysis: Forecasting and Control (ACF/PACF order id)
- Enders 2015 Applied Econometric Time Series 4th ed. §2 (correlogram)
- the cor_test routine (the engine) — exact rules (kendall n<50; spearman AS 89), conf.int only for pearson with >=4 complete pairs; + stats:::cor_test.default source (TIES DEFINITION, cutoff n <= 1290)
- the p.adjust routine (the engine) — BH/BY/holm/hochberg/hommel/bonferroni; 'BH' (or its alias 'fdr')
- Benjamini & Hochberg (1995), JRSS-B 57(1):289-300, doi:10.1111/j.2517-6161.1995.tb02031.x (FDR — default BH)
- Holm (1979), Scand. J. Statist. 6:65-70 (step-down FWER; dominates Bonferroni)
- Benjamini & Yekutieli (2001), Ann. Statist. 29(4), doi:10.1214/aos/1013699998 (FDR under dependence — BY)

## #82 — Macro arithmetic (growth/annualize/deflate/rebase/per-capita/contributions)

**Module:** `macro_arithmetic.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `macro_growth` | `x` | `series_handle`, `integer`, `boolean`, `integer`, `boolean` | `periods=1`, `annualize=False`, `log=False` | `light` | — |
| `macro_deflate` | `nominal`, `deflator` | `series_handle`, `series_handle`, `number` | `base=100` | `light` | — |
| `macro_rebase` | `x`, `base_period` | `series_handle`, `integer`, `number` | `base_value=100` | `light` | — |
| `macro_per_capita` | `x`, `population` | `series_handle`, `series_handle`, `number` | `scale=1` | `light` | — |
| `macro_contributions` | `components`, `weights` | `matrix_handle`, `series_handle`, `series_handle`, `number` | `tol=1e-06` | `light` | — |

### Use when

deterministic macro identities with explicit conventions; rate/annualize, nominal->real, index rebase, per-capita, contributions + additivity check

### Do not use when

class-agnostic transformations on ts/xts (without macro semantics) -> tsbox #78; chain-linked data where contributions are non-additive (it exposes the residual)

### Prerequisites

- c00_data_utilities/replacement_missing_values.imputets_kalman (fill NA first — the finite gate rejects NA/NaN/Inf)

### Alternatives

| instead use | when |
| --- | --- |
| vs ts_transform #78 (ts_pc/pcy/pca) | macro_growth when you need an explicit annualization convention + div-by-zero flag |
| log=TRUE (log-growth) | additively decomposable, large changes/aggregation vs simple growth (direct %) |
| macro_rebase (base_value=100) | vs ts_rebase #78 (base=1, date-anchored) |

### Output fields

- macro_growth: growth (structurally leading-NA), annualized, annualize_convention, n_nonfinite_growth (div-by-zero flag)
- macro_deflate: real=nominal/deflator*base; macro_rebase: index+anchor; macro_per_capita: x/population*scale
- macro_contributions: contributions (matrix), contribution_total, additivity_checked/max_abs_residual/checks_passed

### Pitfalls

- compound annualization for simple growth: q/q 1% -> (1.01)^4-1 = 4.06% (NOT 4%); log: g*(freq/periods), linear
- n_nonfinite_growth/annualized>0 = a silent NaN (zero/negative base) which to_mcp turns into null; check it explicitly
- macro_contributions takes GROWTH RATES per component (column)/period (row), NOT levels; additivity fail -> hard stop

### References

- the standard library (arithmetic identities, no external dependency)
- annualization compound convention (live-verified in the wrapper)
- log-growth additivity (Tornqvist/log-diff decomposition, standard)

## #96 — Reading delimited / fixed-width flat files (CSV/TSV/delim/FWF) + parse-problem diagnostics

**Module:** `reading_delimited_fixed.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `read_csv_data` | `path` | `path`, `string`, `series_codes` | — | `light` | `data` |
| `read_tsv_data` | `path` | `path`, `string`, `series_codes` | — | `light` | `data` |
| `read_delimited` | `path`, `delim` | `path`, `string`, `string`, `series_codes` | — | `light` | `data` |
| `read_fwf_data` | `path` | `path`, `string`, `series_codes` | — | `light` | `data` |
| `read_parse_problems` | `path` | `path`, `enum`, `string`, `string` | — | `light` | — |

### Use when

the first step of the DAG; ingest a user-uploaded flat file -> a long/records data_frame (register data -> Parquet); parse problems as data

### Do not use when

Excel -> readxl #97; Parquet/Feather -> arrow #98; JSON -> jsonlite #99; Stata/SPSS/SAS -> haven #100; charts (frontend); a custom locale/fwf spec -> the L1 wrapper

### Prerequisites

- path: a non-empty string, NOT a directory, existing, size>0 bytes
- POST-gate ncol>0 (a whitespace-only file -> a silent 0x0 tibble)
- col_types NULL\|compact string\|col_spec; na a non-empty character without NA; read_delimited delim EXACTLY 1 character

### Alternatives

| instead use | when |
| --- | --- |
| #98 arw_read_csv | a large/columnar CSV or Arrow type inference; no fine-grained parse diagnostics |
| read_fwf_data | columnar fixed width with no delimiter |

### Output fields

- data: plain data_frame -> records (registered producer -> Parquet)
- col_names/column_types/n_rows/n_cols: the detected structure
- problems/n_problems/has_problems: parse diagnostics (the file column is dropped)

### Pitfalls

- lazy=FALSE internally so that the problems materialise IMMEDIATELY (the readr lazy default would leave them empty)
- a whitespace-only file -> readr silently returns a 0x0 tibble -> blocked (no column)
- col_types is a compact string (e.g. 'Dd'), NOT a per-column vector; locale/col_positions are not exposed on the node

### References

- Wickham & Hester, readr 2.2.0 (live args introspection), readr.tidyverse.org

## #97 — Reading/writing Excel workbooks (.xls/.xlsx read + sheet discovery +.xlsx write)

**Module:** `reading_writing_excel.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `xl_read_excel` | `path` | `path`, `string`, `string`, `boolean`, `integer` | `col_names=True`, `skip=0` | `light` | `data` |
| `xl_excel_sheets` | `path` | `path` | — | `light` | — |
| `xl_read_openxlsx` | `path` | `path`, `string`, `integer`, `boolean`, `boolean`, `boolean` | `startRow=1`, `colNames=True`, `rowNames=False`, `detectDates=False` | `light` | `data` |
| `xl_write_xlsx` | `x` | `df_handle`, `boolean`, `boolean` | `overwrite=True`, `as_table=False` | `light` | — |

### Use when

ingest an Excel upload -> a rectangular data_frame (register data -> Parquet); sheet/range selection; xl_write_xlsx is a terminal export

### Do not use when

CSV/TSV -> readr #96; Parquet/Feather -> arrow #98; Stata/SPSS/SAS -> haven #100; styling/plotting (frontend)

### Prerequisites

- path a non-empty string + file.exists; sheet validated against the real list of sheets
- range pre-validated with as.cell_limits; col_types in {skip,guess,logical,numeric,date,text,list}
- xl_read_openxlsx/.xls gate; xl_write_xlsx.xlsx extension + overwrite gate

### Alternatives

| instead use | when |
| --- | --- |
| xl_read_openxlsx | .xlsx only + row names/startRow/detectDates; NOT legacy.xls or an A1 range |
| xl_read_excel | legacy.xls or an A1 range subset (readxl) |

### Output fields

- data: tibble/data_frame -> records (registered producer -> Parquet) + nrow/ncol/columns/sheet
- xl_excel_sheets: sheets (character) + n_sheets
- xl_write_xlsx: file/sheets_written/n_sheets/bytes

### Pitfalls

- CRITICAL: write.xlsx(non-df/list-of-non-df) does NOT error -> a silently empty workbook -> hard gate
- openxlsx read.xlsx on an empty sheet -> NULL -> normalised to a 0-row df
- openxlsx does NOT read.xls (only.xlsx); sheet=position, 1-indexed

### References

- cellranger as.cell_limits (range pre-validation); live args/docs introspection

## #98 — Canonical on-disk data-format layer: Parquet/Feather/CSV readers + a Parquet writer + a lazy (hive-)partitioned Dataset

**Module:** `canonical_disk_format.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `arw_read_parquet` | `file` | `path`, `series_codes` | — | `light` | `data` |
| `arw_read_feather` | `file` | `path`, `series_codes` | — | `light` | `data` |
| `arw_read_csv` | `file` | `path`, `series_codes` | — | `light` | `data` |
| `arw_write_parquet` | `x` | `df_handle`, `enum` | — | `light` | — |
| `arw_open_dataset` | `sources` | `path`, `series_codes`, `enum`, `integer` | `n_preview=10` | `light` | — |

### Use when

Parquet/Feather/CSV, the lingua franca of the object store; the readers register data -> Parquet; the writer df->Parquet; open_dataset is lazy and partitioned

### Do not use when

parse diagnostics/col-spec -> readr #96; Excel -> readxl #97; JSON -> jsonlite #99; NEVER an opaque Arrow Table (as_data_frame=FALSE)

### Prerequisites

- read_*: file = an existing FILE (not a directory); a cryptic IOError otherwise
- write_parquet: x a data_frame with >=1 column; the parent dir of sink exists; codec_is_available; POST-gate the file was created
- open_dataset: sources = an existing DIRECTORY; n_preview >= 0 integer

### Alternatives

| instead use | when |
| --- | --- |
| #96 read_csv_data | a CSV with parse-problem diagnostics; not a large columnar file/type inference |
| arw_open_dataset | hive-partitioned multiple files in a directory (lazy); not a single eager file |

### Output fields

- data: plain data_frame (registered producer -> Parquet) + schema/n_rows/n_cols/columns/format
- writer: path/bytes/schema/compression (NOT a producer)
- open_dataset: a lazy dataset stub + JSON-safe schema/partitioning/files/preview

### Pitfalls

- CRITICAL: arrow tidyselect col_select with a NULL variable -> ZERO columns silently -> read all + subset in the standard library
- the codec (zstd/gzip) is compile-time optional -> gated with codec_is_available
- the readers ALWAYS materialise a plain data_frame (never an opaque Arrow Table)

### References

- live args/probe introspection; arrow.apache.org/docs/r

## #99 — JSON interchange: parse (fromJSON) / serialise (toJSON) / validate / NDJSON stream in-out

**Module:** `json_interchange_parse.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `json_parse` | `txt` | `string`, `boolean`, `boolean`, `boolean`, `boolean` | `flatten=False`, `simplify_vector=True`, `simplify_dataframe=True`, `simplify_matrix=True` | `light` | `parsed` |
| `json_write` | `x` | `raw_handle`, `boolean`, `boolean`, `enum`, `enum`, `enum`, `integer` | `auto_unbox=True`, `pretty=False` | `light` | — |
| `json_validate` | `txt` | `string` | — | `light` | — |
| `json_stream_parse` | `txt` | `string`, `boolean` | `flatten=False` | `light` | `data` |
| `json_stream_write` | `x` | `df_handle`, `integer` | `pagesize=500` | `light` | — |

### Use when

the JSON/NDJSON data layer; json_parse/json_stream_parse are producers (register); json_write/stream_write are serializers; json_validate is a diagnostic

### Do not use when

CSV -> readr #96; Excel -> readxl #97; Parquet -> arrow #98; for tabular data prefer arrow/readr; file IO belongs to the reader/writer nodes

### Prerequisites

- json_parse: txt a single non-NA non-empty string; validate FIRST (it blocks both malformed input AND SSRF/file fetching)
- json_write: digits defaults to NA (full precision); force=FALSE (a non-mappable class = a hard error)
- json_stream_parse: character without NA; EVERY line is validated before the stream; json_stream_write nrow>=1

### Alternatives

| instead use | when |
| --- | --- |
| json_stream_parse | NDJSON newline-delimited records -> a data_frame; not a single JSON document |
| #98 arrow / #96 readr | purely tabular data (Parquet/CSV) instead of nested/semi-structured JSON |

### Output fields

- json_parse: parsed (vector/list/data_frame, registered; df->Parquet otherwise RDS) + type/n
- json_stream_parse: data (data_frame -> Parquet) + n/ncol
- json_write/json_stream_write: json/ndjson/text strings; json_validate valid/error/offset

### Pitfalls

- CRITICAL: toJSON defaults to digits=4 and rounds SILENTLY (pi->3.1416) -> override with NA
- auto_unbox=TRUE (default): length-1 vectors -> JSON scalars
- fromJSON auto-fetching a URL/path is blocked by the validate-first rule (no SSRF)

### References

- Ooms, The jsonlite Package (arXiv:1403.2805); live r-btw introspection

## #100 — Import/export Stata/SPSS/SAS (.dta/.sav/.sas7bdat) with labelled metadata + labelled->factor materialisation

**Module:** `import_export_stata.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hvn_read_stata` | `path` | `path`, `string`, `series_codes`, `integer`, `integer`, `enum` | `skip=0` | `light` | `data` |
| `hvn_read_spss` | `path` | `path`, `boolean`, `string`, `series_codes`, `integer`, `integer`, `enum` | `user_na=False`, `skip=0` | `light` | `data` |
| `hvn_read_sas` | `path` | `path`, `path`, `string`, `series_codes`, `integer`, `integer`, `enum` | `skip=0` | `light` | `data` |
| `hvn_write_stata` | `data` | `df_handle`, `integer`, `string` | `version=14` | `light` | — |
| `hvn_as_factor` | `x` | `raw_handle`, `enum`, `boolean`, `boolean` | `ordered=False`, `only_labelled=True` | `light` | `data` |

### Use when

ingest a.dta/.sav/.sas7bdat upload -> a tidy data_frame (register data -> Parquet) + variable/value labels; hvn_write_stata exports; hvn_as_factor turns labelled into factor

### Do not use when

CSV -> readr #96; Excel -> readxl #97; Parquet -> arrow #98; JSON -> jsonlite #99; secondary formats (.por/.xpt/write_sav); URL/connection inputs (local path only)

### Prerequisites

- read path: a string of length 1, NOT a directory, existing; write path: the parent dir exists + a POST-gate that it was written
- write data must be a df with >=1 column; version a length-1 integer in 8-15; label NULL or <=80 bytes
- hvn_as_factor: a non-df input MUST be labelled (otherwise forcats silently turns every vector into a factor)

### Alternatives

| instead use | when |
| --- | --- |
| hvn_read_stata/spss/sas | choose by file format (.dta/.sav/.sas7bdat) |
| hvn_as_factor | categorical analysis/plots on haven_labelled columns before the downstream step |

### Output fields

- data: tibble (registered producer -> Parquet; labelled -> numeric codes)
- var_labels/value_labels/labelled_cols/col_types/dataset_label: JSON-safe metadata
- writer: path/written/version/n_rows/n_cols/bytes; as_factor: data/input_type/levels/n

### Pitfalls

- attr(col,'label') PARTIAL-matches 'labels' (the value labels) when the variable label is missing -> exact=TRUE everywhere
- write_dta version=14.5 is accepted SILENTLY; version=c(14,15) gives a cryptic length error -> a whole-number length-1 gate
- as_factor on a plain numeric -> forcats silently produces a factor (silently wrong) -> a labelled-only gate

### References

- Wickham/Miller/Smith, haven 2.5.5 (live args introspection + system.file iris examples)

## #101 — CLOSED-vocabulary tabular manipulation (filter/select/mutate/arrange/summarise/group_by/join/distinct/rename/relocate/slice)

**Module:** `closed_vocabulary_tabular.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dpl_filter` | `df`, `column` | `df_handle`, `string`, `enum`, `raw` | — | `light` | — |
| `dpl_select` | `df`, `columns` | `df_handle`, `series_codes`, `enum` | — | `light` | — |
| `dpl_mutate` | `df`, `new_column`, `columns` | `df_handle`, `string`, `enum`, `series_codes`, `number` | — | `light` | — |
| `dpl_arrange` | `df`, `columns` | `df_handle`, `series_codes`, `boolean` | `desc=False` | `light` | — |
| `dpl_summarise` | `df` | `df_handle`, `enum`, `string`, `series_codes` | — | `light` | — |
| `dpl_group_by` | `df`, `columns` | `df_handle`, `series_codes` | — | `light` | — |
| `dpl_join` | `x`, `y`, `by` | `df_handle`, `df_handle`, `enum`, `series_codes` | — | `light` | — |
| `dpl_distinct` | `df` | `df_handle`, `series_codes`, `boolean` | `keep_all=True` | `light` | — |
| `dpl_rename` | `df`, `old_names`, `new_names` | `df_handle`, `series_codes`, `series_codes` | — | `light` | — |
| `dpl_relocate` | `df`, `columns` | `df_handle`, `series_codes`, `series_codes`, `series_codes` | — | `light` | — |
| `dpl_slice` | `df` | `df_handle`, `enum`, `integer`, `string`, `integer`, `integer` | `n=1` | `light` | — |

### Use when

the relational/wrangling layer; filtering/selecting/transforming columns + per-group summarise (.by) + joins by column names; a CLOSED enum, not a tidy-eval string

### Do not use when

free tidy-eval expressions (structurally excluded); long<->wide reshaping/NA -> tidyr #102; grouped/panel series transformations -> collapse #103; random sampling (slice_sample was excluded)

### Alternatives

| instead use | when |
| --- | --- |
| #103 collapse | grouped/panel numeric series transformation (lags/diffs/growth/within/scale) — faster, g/t panel-aware |
| #102 tidyr | reshaping/completion instead of relational operations |

### Output fields

- data: the transformed data_frame (records) + n_rows/n_cols/columns
- dpl_group_by: group_keys/group_sizes/n_groups (a terminal info node — it does NOT chain a grouped_df)
- dpl_summarise: <stat>_<column> or n; dpl_join: r.type/by

### Pitfalls

- dpl_group_by is an INFO node; the grouped_df attribute is lost at the Parquet boundary -> use dpl_summarise(by=) for per-group aggregation
- dpl_mutate div/log/sqrt -> NaN/Inf cells; the warning is muffled into a message; the numerical validity is your responsibility
- dpl_filter: a silently-wrong gate — a numeric column vs a non-numeric value (1=='a' -> 0 rows) is blocked

### References

- dplyr 1.2.1 reference — A Grammar of Data Manipulation (Wickham et al.)
- dplyr.tidyverse.org / dplyr; vignettes dplyr/grouping/two-table

## #102 — Tidy-data reshaping & missing-value handling (pivot_longer/pivot_wider/separate_wider/unite/drop_na/replace_na/fill/complete/nest/unnest)

**Module:** `tidy_reshaping_missing.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tidyr_pivot_longer` | `data`, `cols` | `df_handle`, `series_codes`, `series_codes`, `string`, `string`, `string`, `string`, `boolean` | `values_drop_na=False` | `light` | — |
| `tidyr_pivot_wider` | `data`, `names_from`, `values_from` | `df_handle`, `series_codes`, `series_codes`, `series_codes`, `raw`, `enum`, `string`, `string`, `boolean` | `names_prefix=''`, `names_sep='_'`, `names_sort=False` | `light` | — |
| `tidyr_separate_wider` | `data`, `col` | `df_handle`, `string`, `enum`, `string`, `series_codes`, `raw`, `raw`, `string`, `string`, `string`, `boolean` | `too_few='error'`, `too_many='error'`, `cols_remove=True` | `light` | — |
| `tidyr_unite` | `data`, `col`, `cols` | `df_handle`, `string`, `series_codes`, `string`, `boolean`, `boolean` | `sep='_'`, `remove=True`, `na_rm=False` | `light` | — |
| `tidyr_drop_na` | `data` | `df_handle`, `series_codes` | — | `light` | — |
| `tidyr_replace_na` | `data`, `replace` | `df_handle`, `raw` | — | `light` | — |
| `tidyr_fill` | `data`, `cols` | `df_handle`, `series_codes`, `enum`, `series_codes` | — | `light` | — |
| `tidyr_complete` | `data`, `cols` | `df_handle`, `series_codes`, `raw` | — | `light` | — |
| `tidyr_nest` | `data`, `by` | `df_handle`, `series_codes`, `string` | `key='data'` | `light` | — |
| `tidyr_unnest` | `data`, `cols` | `df_handle`, `series_codes`, `boolean`, `string` | `keep_empty=False` | `light` | — |

### Use when

table shaping; long<->wide, splitting/uniting columns, completing combinations, cleaning/filling NA (drop/replace/fill LOCF-NOCB); CLOSED vocabulary (columns BY NAME, not tidy-eval)

### Do not use when

relational operations -> dplyr #101; deep rectangling/grid builders (omitted); statistical imputation -> imputeTS #80; class/frequency conversion -> tsbox #78

### Alternatives

| instead use | when |
| --- | --- |
| #101 dplyr | relational operations (filter/mutate/join/summarise) instead of reshaping |
| #103 collapse (qsu/collap) | fast summary/aggregation instead of completion |

### Output fields

- data: the reshaped tibble (records; nested list-columns recursively) + class/nrow/ncol/colnames
- n_dropped (drop_na) / n_added (complete)
- pivot_wider: values_fn applied; separate_wider: mode/col

### Pitfalls

- pivot_wider with an empty id_cols -> tidyr infers it from the remaining columns (a literal-NULL sentinel; the wrapper does NOT pass the argument; a non-literal NULL -> 1-row list-cols; fixed)
- values_fn: with a unique key -> do not supply an aggregator; with a non-unique key -> you MUST (SILENT list-col gate)
- separate_wider_regex: it has NO too_many; too_few='debug' -> a warning (muffled) + debug columns

### References

- tidyr 1.3.2 reference — Tidy Messy Data (Wickham et al.)
- tidyr.tidyverse.org / tidyr; vignettes pivot/nest/rectangle

## #103 — Fast (grouped/panel) data transformation (fgrowth/fdiff/flag/fcumsum/fscale/fwithin/collap/qsu/TRA)

**Module:** `fast_transformation.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cll_growth` | `x` | `series_handle`, `integer`, `integer`, `boolean`, `number`, `number`, `series_codes`, `num_array`, `number` | `n=1`, `diff=1`, `logdiff=False`, `scale=100`, `power=1` | `light` | — |
| `cll_diff` | `x` | `series_handle`, `integer`, `integer`, `boolean`, `number`, `series_codes`, `num_array`, `number` | `n=1`, `diff=1`, `log=False`, `rho=1` | `light` | — |
| `cll_lag` | `x` | `series_handle`, `integer`, `series_codes`, `num_array`, `number` | `n=1` | `light` | — |
| `cll_cumsum` | `x` | `series_handle`, `series_codes`, `boolean`, `boolean` | `na_rm=True`, `fill=False` | `light` | — |
| `cll_scale` | `x` | `series_handle`, `series_codes`, `num_array`, `boolean`, `number`, `number` | `na_rm=True`, `mean=0`, `sd=1` | `light` | — |
| `cll_within` | `x` | `series_handle`, `series_codes`, `num_array`, `boolean`, `number`, `number` | `na_rm=True`, `mean=0`, `theta=1` | `light` | — |
| `cll_collap` | `X`, `by` | `df_handle`, `series_codes`, `enum`, `series_codes`, `num_array` | — | `light` | — |
| `cll_qsu` | `x` | `df_handle`, `series_codes`, `num_array`, `boolean` | `higher=False` | `light` | — |
| `cll_transform` | `x`, `STATS` | `series_handle`, `num_array`, `enum`, `series_codes` | — | `light` | — |

### Use when

a high-performance transform layer for series & PANELS; lags/diffs/growth/cumsum/scale/within + multi-column aggregation + a qsu summary + a generic TRA; panel support through g+t, C/C++-fast, NA-skipping

### Do not use when

relational operations -> dplyr #101; long<->wide -> tidyr #102; macro-semantic transforms (index base=100/deflate/contributions) -> tsbox #78 / macro-arithmetic #82; rolling windows -> slider #105

### Alternatives

| instead use | when |
| --- | --- |
| #78 tsbox / #82 macro-arithmetic | you need macro semantics (annualize/deflate/base=100 index/contributions) rather than a mechanical fast transform |
| #101 dplyr summarise | small non-panel aggregations; collap wins on speed/multi-column work |

### Output fields

- series: the transformed object (ts/matrix/df); stubs=FALSE -> clean column names
- cll_collap: result (aggregated df); cll_qsu: summary (a plain df via as_data.frame(qsu))
- class/n + the applied arguments

### Pitfalls

- fscale/fwithin on a constant series -> a NaN z-score (honest, not silent)
- cll_collap weights: only the weighted fast-stat functions (mean/sum/median/sd/prod) use them; first/last/min/max/nobs ignore them (the warning is muffled)
- cll_qsu on a data_frame: supply g (routed to by); qsu_default ignores g SILENTLY

### References

- collapse 2.1.7 reference — Advanced and Fast Data Transformation (Krantz); JSS 116(1) doi:10.18637/jss.v116.i01
- fastverse.org/collapse / collapse; vignettes collapse_intro/collapse_and_plm

## #104 — Deterministic invertible preprocessing transforms (diff/standardize/normalize/box_cox/auto_lambda + tk_augment_lags/differences + pad_by_time)

**Module:** `deterministic_invertible_preprocessing.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ttk_diff` | `x` | `series_handle`, `integer`, `integer`, `boolean` | `lag=1`, `difference=1`, `log=False` | `light` | — |
| `ttk_diff_inv` | `x` | `series_handle`, `num_array`, `integer`, `integer`, `boolean` | `lag=1`, `difference=1`, `log=False` | `light` | — |
| `ttk_standardize` | `x` | `series_handle` | — | `light` | — |
| `ttk_normalize` | `x` | `series_handle` | — | `light` | — |
| `ttk_box_cox` | `x` | `series_handle`, `number`, `enum`, `number`, `number` | `lambda_lower=-1`, `lambda_upper=2` | `light` | — |
| `ttk_auto_lambda` | `x` | `series_handle`, `enum`, `number`, `number` | `lambda_lower=-1`, `lambda_upper=2` | `light` | — |
| `ttk_augment_lags` | `data`, `value_col` | `df_handle`, `series_codes`, `int_array`, `series_codes` | `lags=1`, `new_names='auto'` | `light` | — |
| `ttk_augment_differences` | `data`, `value_col` | `df_handle`, `series_codes`, `int_array`, `integer`, `boolean`, `series_codes` | `lags=1`, `differences=1`, `log=False`, `new_names='auto'` | `light` | — |
| `ttk_pad_by_time` | `data`, `date_col` | `df_handle`, `string`, `string`, `number`, `enum`, `string`, `string` | `by='auto'` | `light` | — |

### Use when

the feature-engineering layer; EXACTLY invertible preprocessing for a forecasting/ML node (differencing/standardize/normalize/Box-Cox + lag/diff augmentation + regular-timestamp padding)

### Do not use when

charts (plot_*); grouped/panel fast transforms -> collapse #103; macro-semantic growth/index -> macro-arithmetic #82; rolling smoothing -> slider #105; imputation -> imputeTS #80

### Alternatives

| instead use | when |
| --- | --- |
| #103 collapse | panel-aware (g/t) fast differencing/scaling without inversion parameters |
| #82 macro-arithmetic | a macro convention (annualize/deflate) rather than reversible ML preprocessing |

### Output fields

- result: the transformed vector + the INVERSION PARAMETERS (initial_values/mean/sd/min/max/lambda)
- augmenters: result (tibble) + new_columns + dimensions
- ttk_box_cox: lambda ('auto' -> selected & reported)

### Pitfalls

- Box-Cox/auto_lambda require x>0; log=TRUE requires x>0 (otherwise SILENT NaN); lambda_lower<upper (an inverted interval is accepted silently -> gate)
- ttk_diff_inv needs EXACTLY the initial_values & lag/difference of ttk_diff for a full inversion
- a constant series -> standardize/normalize give NaN (gated); auto_lambda is deterministic (an identical lambda, no seed)

### References

- timetk 2.9.1 reference — A Tool Kit for Working with Time Series (Dancho/Vaughan)
- business-science.github.io/timetk / timetk; vignettes TK04/TK07

## #105 — Deterministic rolling-window aggregations (slide_dbl/slide_index_dbl/slide_period_dbl/hop_index_vec)

**Module:** `deterministic_rolling_window.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `sld_slide` | `x` | `series_handle`, `enum`, `number`, `number`, `integer`, `boolean`, `boolean` | `before=0`, `after=0`, `step=1`, `complete=False`, `na_rm=False` | `light` | — |
| `sld_slide_index` | `x`, `i` | `series_handle`, `num_array`, `enum`, `number`, `number`, `boolean`, `boolean` | `before=0`, `after=0`, `complete=False`, `na_rm=False` | `light` | — |
| `sld_slide_period` | `x`, `i` | `series_handle`, `num_array`, `enum`, `enum`, `integer`, `number`, `number`, `boolean`, `boolean` | `every=1`, `before=0`, `after=0`, `complete=False`, `na_rm=False` | `light` | — |
| `sld_hop_index` | `x`, `i`, `starts`, `stops` | `series_handle`, `num_array`, `num_array`, `num_array`, `enum`, `boolean` | `na_rm=False` | `light` | — |

### Use when

the rolling-aggregate layer; rolling mean/sum/sd/min/max/median in 4 regimes (positional/index-relative/calendar-period/arbitrary pairs); vctrs-native, type-stable

### Do not use when

charts (frontend); diff/growth/lags -> collapse #103 / timetk #104; a free custom reducer (structurally excluded); weighted/EMA rolling -> roll/TTR

### Alternatives

| instead use | when |
| --- | --- |
| #103 collapse / #104 timetk | point transforms (diff/growth/scale) rather than window reduction |
| roll / TTR | specialised weighted/EMA rolling |

### Output fields

- values: double vector = chart-data (length=length(x) for slide*, =length(starts) for hop)
- n/n_na/reducer/na_rm + the applied arguments
- empty windows -> NaN/Inf, reported in n_na (they are not hidden)

### Pitfalls

- .f is NEVER exposed — a closed reducer enum {mean,sum,sd,min,max,median} (a security boundary)
- hop_index output length = length(starts) (NOT length(x)); slide_period.before/.after count BLOCKS, not observations
- .before/.after: an integer or Inf; negatives = look-forward; a non-empty window requires before+after>=0

### References

- slider 0.3.3 reference — Sliding Window Functions (Vaughan)
- slider; vignettes slider/rowwise

## #106 — Indexed (time-stamped) time-series toolbox (periodicity->OHLC, calendar-period aggregation, index merge/join, intraday alignment)

**Module:** `indexed_time_series.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `xts_to_period` | `x` | `irregular_series_handle`, `enum`, `integer`, `boolean` | `k=1`, `OHLC=True` | `light` | — |
| `xts_period_apply` | `x` | `irregular_series_handle`, `enum`, `integer`, `enum`, `boolean` | `k=1`, `na_rm=False` | `light` | — |
| `xts_apply_monthly` | `x` | `irregular_series_handle`, `enum`, `boolean` | `na_rm=False` | `light` | — |
| `xts_merge` | `x`, `y` | `irregular_series_handle`, `irregular_series_handle`, `enum`, `number` | — | `light` | — |
| `xts_align_time` | `x` | `irregular_series_handle`, `number` | `n=60` | `light` | — |

### Use when

the time/calendar index ITSELF is the subject: OHLC periodicity conversion, calendar aggregation (endpoints/period.apply/apply.monthly), index join, intraday alignment

### Do not use when

plain rolling transforms -> TTR #107/roll #109/data.table #108; charts (frontend); INCREASING the frequency -> tempdisagg #79; class plumbing with no index -> tsbox #78

### Alternatives

| instead use | when |
| --- | --- |
| #78 ts_aggregate | class-agnostic aggregation without OHLC/calendar-endpoint control |
| #107 TTR / #109 roll | a rolling-window statistic rather than a calendar bucket |

### Output fields

- series: the xts result (to_mcp.xts -> {index, values}); classed -> an RDS bucket in the node round trip
- class/n/ncol/periodicity + the applied arguments
- xts_to_period: ncol=4 OHLC or ncol=1 close; the index is the end of the period

### Pitfalls

- to.period on an arbitrary multi-column input SILENTLY builds a misleading OHLC -> hard gate requiring univariate OR a genuine 4-column OHLC
- align.time on a Date/yearmon index is a SILENT no-op -> hard gate requiring a POSIXct index
- the OHLC column prefix is the caller's series name (fallback 'V.' for non-symbols); align: n_seconds is separate from the count n

### References

- Ryan & Ulrich, xts: eXtensible Time Series ( xts)

## #107 — Rolling / windowed series transforms (rate-of-change, momentum, moving-average smoothers, single-series rolling stats, rolling cor/cov)

**Module:** `rolling_windowed_series.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ttr_roc` | `x` | `series_handle`, `integer`, `enum` | `n=1` | `light` | — |
| `ttr_momentum` | `x` | `series_handle`, `integer` | `n=1` | `light` | — |
| `ttr_ma` | `x` | `series_handle`, `integer`, `enum`, `boolean`, `number`, `num_array`, `number`, `number`, `number` | `n=10`, `wilder=False`, `v=1`, `offset=0.85`, `sigma=6` | `light` | — |
| `ttr_run` | `x` | `series_handle`, `integer`, `enum` | `n=10` | `light` | — |
| `ttr_run_cor` | `x`, `y` | `series_handle`, `series_handle`, `integer`, `enum` | `n=10` | `light` | — |

### Use when

deterministic rolling & rate-of-change transforms on a univariate series: ROC(log/discrete), momentum, MA smoothers, rolling moments, rolling cor/cov

### Do not use when

OHLC/price technicals (out of scope); calendar/intraday -> xts #106; matrix/panel or rolling regression -> roll #109; fast lead/lag & frollapply -> data.table #108; charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #109 roll | online/weighted rolling, panel/matrix, or rolling regression |
| #108 data.table frollapply | C speed on a long series + robust reducers (IQR/mad/prod) |
| #106 xts period.apply/apply.monthly | calendar buckets rather than a fixed rolling window |

### Output fields

- values: plain numeric chart-data (an ALMA 1-column matrix -> as_numeric)
- n_obs, n_na: an explicit NA count (never a silent drop) + the applied arguments
- type: continuous=log return, discrete=simple % return (ROC)

### Pitfalls

- ROC/momentum with n>length return an all-NA result of the wrong length SILENTLY -> gate n to [1,length]
- runCor/runCov do NOT check length(x)==length(y) -> silent garbage -> a hard equal-length gate
- runQuantile does not exist in TTR 0.24.4; for a quantile intent -> ttr_run(fun='median'/'mad'); the cumulative expanding mode is not exposed

### References

- Ulrich, TTR: Technical Trading Rules ( TTR)

## #108 — Fast (C) lead/lag + rolling-window aggregates + rolling robust reducers (shift, froll family, frollapply closed reducer set)

**Module:** `fast_lead_lag.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dt_shift` | `x` | `series_handle`, `int_array`, `enum`, `number` | `n=1` | `light` | — |
| `dt_roll` | `x`, `n` | `series_handle`, `int_array`, `enum`, `number`, `enum`, `boolean`, `boolean` | `na_rm=False`, `adaptive=False` | `light` | — |
| `dt_roll_apply` | `x`, `n` | `series_handle`, `integer`, `enum`, `number`, `enum`, `boolean` | `na_rm=False` | `light` | — |

### Use when

C-speed feature engineering on ONE series: lead/lag/shift/cyclic (multi-offset), rolling moments (right/left/center, adaptive), rolling robust reducers (median/mad/IQR/var/prod)

### Do not use when

online/weighted/panel/rolling regression -> roll #109; ROC/momentum/MA smoothers -> TTR #107; calendar/OHLC/intraday -> xts #106; charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #107 TTR runSum/runMean/runSD | the same rolling moments with macro enums on a short series |
| #109 roll | weighted/online rolling, a panel matrix, or roll_lm |

### Output fields

- result: a plain numeric vector; or a list of equal-length vectors for a multi-offset dt_shift (to_mcp handles both)
- n_obs, class + the applied arguments
- leading/trailing NA per align; padding from fill

### Pitfalls

- shift(x,1.5)/frollmean(x,2.5) SILENTLY truncate the fraction -> an integer-n gate (round-based)
- a multi-offset dt_shift (n=c(1,2)) -> result is a list, not a flat vector
- adaptive=TRUE requires n to be a vector of length(x) & align!=center; has.nf=FALSE/algo='exact' are not exposed (silently wrong max/min)

### References

- Barrett/Dowle/Srinivasan, data.table: Extension of data_frame ( data.table)

## #109 — Fast rolling & expanding window statistics on vector/matrix (mean/sd/var, cor/cov, z-score, quantile, rolling regression)

**Module:** `fast_rolling_expanding.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `rll_mean` | `x`, `width` | `matrix_handle`, `integer`, `num_array`, `integer`, `boolean` | `online=True` | `light` | — |
| `rll_sd` | `x`, `width` | `matrix_handle`, `integer`, `num_array`, `boolean`, `integer`, `boolean` | `center=True`, `online=True` | `light` | — |
| `rll_var` | `x`, `width` | `matrix_handle`, `integer`, `num_array`, `boolean`, `integer`, `boolean` | `center=True`, `online=True` | `light` | — |
| `rll_cor` | `x`, `width` | `matrix_handle`, `matrix_handle`, `integer`, `num_array`, `boolean`, `boolean`, `integer`, `boolean` | `center=True`, `scale=True`, `online=True` | `light` | — |
| `rll_cov` | `x`, `width` | `matrix_handle`, `matrix_handle`, `integer`, `num_array`, `boolean`, `boolean`, `integer`, `boolean` | `center=True`, `scale=False`, `online=True` | `light` | — |
| `rll_lm` | `x`, `y`, `width` | `matrix_handle`, `matrix_handle`, `integer`, `num_array`, `boolean`, `integer`, `boolean` | `intercept=True`, `online=True` | `light` | — |
| `rll_scale` | `x`, `width` | `matrix_handle`, `integer`, `num_array`, `boolean`, `boolean`, `integer`, `boolean` | `center=True`, `scale=True`, `online=True` | `light` | — |
| `rll_quantile` | `x`, `width` | `matrix_handle`, `integer`, `num_array`, `number`, `integer`, `boolean` | `p=0.5`, `online=True` | `light` | — |

### Use when

fast (Rcpp/online) rolling/expanding statistics on a vector or a matrix panel: moments, co-moments (pairwise/k×k×n), z-scores, quantiles, rolling regression; weighted & min_obs warm-up

### Do not use when

single-series ROC/momentum/MA -> TTR #107; fast lead/lag & frollapply reducers -> data.table #108; calendar/OHLC/intraday -> xts #106; charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #108 data.table frollmean/frollapply | ONE series, C speed & robust reducers, without weighted/online/panel support |
| #107 TTR runSD/runCor | classic rolling moments/cor on a short univariate series |

### Output fields

- result: numeric vector / matrix / k×k×n array (rll_cor/cov with y=NULL on a matrix -> a 3D array of matrices)
- rll_lm: coefficients/r_squared/std_error (matrices, 1 row per observation) + n/width/min_obs/online — NOT a chainable producer
- class/shape (n or dim) + width/min_obs/online (+center/scale/p)

### Pitfalls

- width>nobs or min_obs>width => SILENTLY all-NA; width=4.5/'5' => silent truncation/coercion -> hard gates
- weights of a mismatched length are accepted silently -> a gate on length==width
- the first width-1 (or min_obs-1) rows are an NA warm-up; online=TRUE is incremental (negligible differences vs online=FALSE)

### References

- Foster, roll: Rolling and Expanding Statistics ( roll, jjf234.github.io/roll)

## #110 — Rolling O(n) statistics (mean/sd/min/max/quantile/mad) on a numeric vector/matrix

**Module:** `rolling_statistics_numeric.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `run_mean` | `x`, `k` | `matrix_handle`, `integer`, `enum`, `enum` | — | `light` | — |
| `run_sd` | `x`, `k` | `matrix_handle`, `integer`, `num_array`, `enum`, `enum` | — | `light` | — |
| `run_min` | `x`, `k` | `matrix_handle`, `integer`, `enum`, `enum` | — | `light` | — |
| `run_max` | `x`, `k` | `matrix_handle`, `integer`, `enum`, `enum` | — | `light` | — |
| `run_quantile` | `x`, `k`, `probs` | `matrix_handle`, `integer`, `num_array`, `integer`, `enum`, `enum` | `type=7` | `light` | — |
| `run_mad` | `x`, `k` | `matrix_handle`, `integer`, `num_array`, `number`, `enum`, `enum` | `constant=1.4826` | `light` | — |

### Use when

after the fetch; fast deterministic rolling statistics over one buffer (smoothing, rolling volatility, envelopes, rolling quantiles/MAD); trailing align='right' with no look-ahead

### Do not use when

weights/multivariate rolling (cor/cov/lm/scale) -> roll #109; an irregular index/custom function -> slider #105 / data.table #108; NA imputation -> imputeTS #80; charts -> frontend

### Alternatives

| instead use | when |
| --- | --- |
| #109 roll | you need weights/min_obs/online or multivariate rolling (cor/cov/lm/scale) |
| #105 slider | rolling by index/period or with an arbitrary function |

### Output fields

- series: the rolling vector (a matrix input -> nested rows)
- n: output length (endrule='trim' -> shorter); k/endrule/align + the applied arguments
- probs/type/constant/center_supplied: per-method metadata

### Pitfalls

- k: a finite integer in [1, nobs] (hard gate); k<=0 => x unchanged, fractional => truncated, k>n => over-run
- align='center' requires an ODD k (an even k => a silently asymmetric window); 'right'=trailing (no look-ahead)
- endrule='trim' SHORTENS the series; the default endrule fills the edges with the statistic itself

### References

- Tukey — running median / MAD robust smoothing

## #111 — Date parsing/rounding/components + safe month arithmetic (ymd/ym/parse_date_time, floor/ceiling/round_date, quarter/semester/year/month/wday, %m+%/%m-%)

**Module:** `date_parsing_rounding.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `lub_parse_date` | `x` | `series_codes`, `enum` | — | `light` | `dates` |
| `lub_parse_datetime` | `x`, `orders` | `series_codes`, `series_codes`, `string` | `tz='UTC'` | `light` | `dates` |
| `lub_round_date` | `x` | `raw_handle`, `enum`, `enum` | — | `light` | `dates` |
| `lub_component` | `x` | `raw_handle`, `enum` | — | `light` | — |
| `lub_month_arith` | `x`, `months` | `raw_handle`, `integer`, `enum` | — | `light` | `dates` |

### Use when

date cleaning BEFORE tsbox/the other nodes; parsing raw strings->Date/POSIXct, calendar rounding, extraction of numeric fields, safe month arithmetic with rollback

### Do not use when

class/frequency plumbing of an already-timed series -> tsbox #78; simple day arithmetic -> the standard library; charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #78 tsbox | the series is ALREADY in a time-aware class -> class/frequency plumbing; lubridate comes first, to build the Date column |
| base as.Date/format/+ | homogeneous ISO input with no need for month rollback -> base suffices; lubridate for heterogeneous parsing + %m+% rollback |

### Output fields

- dates: parsed/rounded/shifted Date\|POSIXct -> ISO-8601 strings (+ n, n_na, class)
- values: the numeric calendar field (quarter 1-4, wday 1-7,..) from lub_component
- applied args: order/orders/tz \| unit/boundary \| component \| months/op

### Pitfalls

- silent NA: ymd/ym/parse_date_time return NA with ONLY a warning on unparsable input -> the wrapper hard-stops on every non-blank failure (blocked-by-gate)
- %m+%/%m-% rollback: 31 Jan %m+% 1 month = 28/29 Feb (NOT an overflow) — the reason it exists; months is built with period(month=n) because months is NOT exported
- wday defaults to week_start=7 (Sunday=1); unit is a closed enum {month,quarter,year,week,day}, otherwise a cryptic 'Invalid unit specification'

### References

- Grolemund & Wickham, Dates and Times Made Easy with lubridate, JSS 40(3) 2011 ( lubridate)

## #112 — Business-day calendar + working-day arithmetic (create.calendar/bizdays/offset/adjust/bizseq) from a closed specification (holidays + weekdays)

**Module:** `business_day_calendar.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bizc_create_calendar` | — | `series_codes`, `series_codes`, `boolean`, `enum`, `enum`, `string`, `string` | `financial=True`, `adjust_from='none'`, `adjust_to='none'` | `light` | — |
| `bizc_bizdays` | `from`, `to` | `series_codes`, `series_codes`, `series_codes`, `series_codes`, `boolean`, `enum`, `enum`, `string`, `string` | `financial=True`, `adjust_from='none'`, `adjust_to='none'` | `light` | — |
| `bizc_offset` | `dates`, `n` | `series_codes`, `int_array`, `series_codes`, `series_codes`, `boolean`, `enum`, `enum`, `string`, `string` | `financial=True`, `adjust_from='none'`, `adjust_to='none'` | `light` | — |
| `bizc_adjust` | `dates` | `series_codes`, `enum`, `series_codes`, `series_codes`, `boolean`, `enum`, `enum`, `string`, `string` | `direction='next'`, `financial=True`, `adjust_from='none'`, `adjust_to='none'` | `light` | — |
| `bizc_bizseq` | `from`, `to` | `string`, `string`, `series_codes`, `series_codes`, `boolean`, `enum`, `enum`, `string`, `string` | `financial=True`, `adjust_from='none'`, `adjust_to='none'` | `light` | — |

### Use when

BUSINESS-day arithmetic on a calendar built from a closed specification; T+n settlement, NETWORKDAYS counting, rolling to a business day, enumerating business days; fixed income/derivatives

### Do not use when

time-series class/frequency conversions -> tsbox #78; fractional business days (bizdayse); built-in market catalogues (ANBIMA/QuantLib/Rmetrics); imputation/aggregation

### Alternatives

| instead use | when |
| --- | --- |
| adjust_from=previous + adjust_to=next | Excel NETWORKDAYS: the count must start/end on a business day |
| financial=FALSE | inclusive counting (it also counts the final business day; +1 vs financial=TRUE) |
| direction=next vs previous | the market roll convention (following vs preceding) |
| #78 tsbox | you need a time-series transformation, not calendar arithmetic |

### Output fields

- bizc_create_calendar: weekdays/financial/adjust_from/adjust_to + n_holidays/holidays + start_date/end_date + n_bizdays (a validation summary; NOT the raw Calendar object)
- bizc_bizdays: count (integer vector, NETWORKDAYS-style) + from/to (Date->ISO) + n + financial
- bizc_offset: result (shifted Date->ISO) + dates + n + n_out
- bizc_adjust: result (rolled Date->ISO) + dates + direction + n_out
- bizc_bizseq: sequence (business days, Date->ISO) + n + from/to

### Pitfalls

- weekdays: only the 7 LOWER-CASE English tokens; 'Saturday'/'funday' SILENTLY become business days (silently wrong) -> hard gate
- offset n: a fractional n returns NA SILENTLY -> a gate on integers
- financial=TRUE (default) does NOT count the final business day; it gives -1 vs financial=FALSE
- the default range = [min,max] of the holidays; dates outside it error with 'Given date out of range' -> widen start_date/end_date
- from>to: bizdays returns a NEGATIVE value, bizseq gives a cryptic error -> a gate on from<=to

### References

- Wilson Freitas, bizdays: Business Days Calculations and Utilities v1.0.17
- 2006 ISDA Definitions — business-day/day-count conventions (following/preceding/modified following, NETWORKDAYS)

## #113 — Tidy temporal data frames — an explicit key/index contract + structural gap handling (has/scan/count/fill) + CLOSED-vocabulary calendar aggregation (index_by+summarise)

**Module:** `tidy_temporal_frames.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `tsib_as_tsibble` | `data`, `index` | `df_handle`, `string`, `series_codes`, `boolean` | `regular=True` | `light` | `series` |
| `tsib_gaps` | `x` | `df_handle`, `enum`, `boolean` | `full=False` | `light` | — |
| `tsib_fill_gaps` | `x` | `df_handle`, `boolean` | `full=False` | `light` | `series` |
| `tsib_index_agg` | `x`, `value_cols` | `df_handle`, `series_codes`, `enum`, `enum`, `boolean` | `by_key=True` | `light` | `series` |

### Use when

a long df -> a contract-checked temporal table with an explicit index (+optional key); detecting/materialising implicit gaps; calendar aggregation to a lower frequency; it feeds tidyverts (fable/feasts)

### Do not use when

free tidy-eval (excluded); class-agnostic conversions/transforms -> tsbox #78; statistical NA imputation -> imputeTS #80 (fill_gaps only inserts NA); INCREASING the frequency -> tempdisagg #79; charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #78 tsbox | class-agnostic conversion/transformation without the key/index contract (lighter) |
| tsib_index_agg vs ts_aggregate | calendar buckets per key (tsibble) vs plain class-agnostic aggregation (tsbox) |

### Output fields

- series: tbl_ts (to_mcp -> records; a calendar index -> strings 'YYYY QN'/'YYYY Mon') — the main PRODUCER result
- class/n/index/key/measured/interval: compact metadata + the applied arguments
- tsib_gaps: result + any_gaps + n_missing (has=keys with gaps; scan=the missing rows; count=the sum of n)
- tsib_fill_gaps: n_filled (rows added as NA)

### Pitfalls

- a raw Date index on monthly/quarterly data -> interval=1D (the GCD of the days) -> SPURIOUS gaps; supply yearmonth/yearquarter; the interval is returned explicitly
- index_by+summarise with a key: it SILENTLY collapses the keys together; by_key=TRUE (default) => group_by_key => per key
- coarsening to a HIGHER resolution than the index (finer than the source) => a clean error (caught), not a silent one
- the reducers apply only to NUMERIC measured columns (gated before the cryptic summarise error)

### References

- tsibble 1.2.0 reference/vignettes (intro-tsibble, implicit-na): as_tsibble, has_gaps/scan_gaps/count_gaps, fill_gaps, index_by (r-btw docs_help_page + live introspection)
- Wang, Cook & Hyndman (2020), A New Tidy Data Structure to Support Exploration and Modeling of Temporal Data, JCGS 29(3):466-478, doi:10.1080/10618600.2019.1695624

## #114 — Robust outlier handling + robust measures of location/scale (winsorize/trim/robust-z/Huber-M)

**Module:** `robust_outlier_handling.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dt_winsorize` | `x` | `series_handle`, `num_array`, `num_array`, `boolean` | `na_rm=False` | `light` | — |
| `dt_trim` | `x` | `series_handle`, `number`, `boolean` | `trim=0.1`, `na_rm=False` | `light` | — |
| `dt_robscale` | `x` | `series_handle`, `boolean`, `boolean` | `center=True`, `scale=True` | `light` | — |
| `dt_huber` | `x` | `series_handle`, `number`, `boolean`, `number` | `k=1.345`, `na_rm=False` | `light` | — |

### Use when

cleaning the tails BEFORE an econometric method; capping/trimming extreme values, robust median/MAD z-scores, Huber-M location (+ a Wald CI); macro series with spikes/crises

### Do not use when

rolling/time-varying cleaning -> caTools #110 / roll #109; NA imputation -> imputeTS #80; robust/quantile regression -> rlm/quantreg #64; matrix/df input (vector only)

### Alternatives

| instead use | when |
| --- | --- |
| #104 ttk_standardize (classic scale) | without outliers -> mean/sd is more efficient; with outliers -> dt_robscale (median/MAD) |
| dt_trim vs dt_winsorize | winsorize keeps n (capping); trim reduces n (dropping) |

### Output fields

- dt_winsorize: values/lower/upper/probs/n_changed
- dt_trim: values/trimmed_indices/n_trimmed/trimmed_mean; dt_robscale: values/center(median)/scale(MAD)
- dt_huber: location/lower/upper/conf_level (NA if no CI)

### Pitfalls

- Winsorize has no probs argument — the wrapper computes val=quantile(x,probs) first (a convenience layer)
- RobScale has no na.rm => an NA input => silently all NA (hard gate); scaling with MAD=0 => all NaN (hard gate)
- trim∈[0,0.5); >=0.5 => silently NA; NA with na_rm=FALSE => silently NA (all gated)

### References

- Huber (1964), Robust Estimation of a Location Parameter

## #115 — Benchmarking a high-frequency indicator to a low-frequency total (two-step Prais-Winsten regression + additive Denton smoothing)

**Module:** `benchmarking_high_frequency.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dsg_two_steps_benchmark` | `hfserie`, `lfserie` | `series_handle`, `series_handle`, `boolean`, `boolean`, `number` | `include_differenciation=False`, `include_rho=False` | `light` | `model` |
| `dsg_annual_benchmark` | `hfserie`, `lfserie` | `series_handle`, `series_handle`, `boolean`, `boolean`, `number` | `include_differenciation=False`, `include_rho=False` | `light` | `model` |
| `dsg_in_sample` | `object` | `raw_handle`, `enum` | — | `light` | — |

### Use when

a high-frequency indicator is bent so that it sums EXACTLY to a low-frequency target total (the INSEE two-step: Prais-Winsten GLS + additive Denton); annualBenchmark = the default QNA windows

### Do not use when

a broad menu of disaggregation methods (Chow-Lin/Fernandez/Litterman/Denton-Cholette) -> tempdisagg #79; plain aggregation without consistency -> ts_aggregate #78; proportional 3-rule smoothing -> threeRuleSmooth (omitted); charts (frontend)

### Alternatives

| instead use | when |
| --- | --- |
| #79 tempdisagg | you want an explicit choice of disaggregation model (chow-lin/fernandez/litterman/denton) or high->low aggregation (ta) |
| dsg_annual_benchmark | annual->sub-annual with the usual default windows of quarterly national accounts |

### Output fields

- benchmarked: the high-frequency ts (->{values,start,frequency}) — the MAIN result; = fitted_values + smoothed_part; it sums exactly to lfserie within the window
- coefficients/std_errors/rho: the Prais-Winsten regression (constant + the loading on the indicator); rho=0 = no AR term (not a failure)
- fitted_values/smoothed_part: the two additive components (ts); n_high/freq_high/freq_low/freq_ratio metadata
- model: the fitted twoStepsBenchmark handle (RDS bucket) -> dsg_in_sample / coef / se / rho
- dsg_in_sample.comparison: a 2-column mts (Benchmark vs Predicted value), type changes\|levels

### Pitfalls

- FREQ GATE: freq(hf) must be STRICTLY > freq(lf) & an integer ratio; an equal frequency (ratio 1) is accepted SILENTLY by the package (degenerate) -> hard-blocked
- NA in lfserie: silently all-NA coefficients + an all-NA benchmark (silently wrong) -> hard-blocked
- include.differenciation=1 (numeric) is accepted silently as TRUE -> a strict logical gate
- consistency holds ONLY inside the benchmark window; the extrapolation tail (hf beyond lf) is a projection, not a benchmarked value

### References

- Denton 1971, Adjustment of Series to Annual Totals (JASA 66(333):99-102); Prais & Winsten 1954; INSEE/Banque de France two-step benchmarking

## #116 — Fast row/column panel statistics (median/var/sd/quantiles) + a diffusion index (breadth) over a numeric wide panel matrix

**Module:** `fast_row_column.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `panel_row_stats` | `x` | `matrix_handle`, `enum`, `boolean` | `stat='median'`, `na_rm=False` | `light` | — |
| `panel_col_stats` | `x` | `matrix_handle`, `enum`, `boolean` | `stat='median'`, `na_rm=False` | `light` | — |
| `panel_quantiles` | `x` | `matrix_handle`, `num_array`, `integer`, `boolean` | `probs=[0, 0.25, 0.5, 0.75, 1]`, `type=7`, `na_rm=False` | `light` | — |
| `panel_diffusion_index` | `x` | `matrix_handle`, `boolean` | `na_rm=False` | `light` | — |

### Use when

a wide numeric panel (matrix rows=time, cols=series); fast cross-sectional (per-period) & over-time (per-series) location/spread, quantiles per period (fan chart), and a diffusion index (the share of series that rise)

### Do not use when

a single series / ts-class handling -> tsbox #78; rolling windows -> slider #105; ACF/PACF/corr -> descriptives #81; grouped/panel-aware work with ids -> collapse #103; it accepts ONLY a plain numeric matrix (NOT ts/mts/df)

### Alternatives

| instead use | when |
| --- | --- |
| #103 collapse (fmedian/fsd/fquantile, g=) | grouped/panel-aware aggregation with ids, or speed on very large data |
| #78 tsbox | class/frequency plumbing of one or a few series rather than cross-sectional panel statistics |

### Output fields

- values: a numeric vector (row->n_time cross-sectional, col->n_series over time) + margin/stat/na.rm
- quantiles: matrix n_time x length(probs), with columns named by prob (drop=FALSE keeps a matrix for a single prob)
- index: the diffusion index of length n_time-1 in [0,1] (0.5=balance, >0.5=broad expansion)

### Pitfalls

- na.rm=FALSE => an NA PROPAGATES as NA (visible, NOT a silent drop); set TRUE to ignore NA
- row = per-period cross-sectional; col = per-series over time — do not confuse the axis
- a ts/mts passes is_matrix==TRUE and would be accepted silently -> a hard gate blocks it; supply a plain numeric matrix
- rowVars/rowSds on a 1-element margin -> NA (the variance of a single value), not an error

### References

- matrixStats 1.5.0 reference — rowMedians/colMedians, rowVars/colVars, rowSds/colSds, rowQuantiles (signatures checked live via args); Bengtsson H., matrixStats <
- diffusion index / breadth as a leading indicator: Stock & Watson 'Diffusion Indexes'; Conference Board business-cycle diffusion methodology

## #117 — Composite index / dimensionality reduction with PCA (PC1 composite index + loadings + variance decomposition + biplot coordinates + newdata projection + rules for the number of components + KPSS precheck)

**Module:** `composite_index_dimensionality.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pca_composite` | `x` | `matrix_handle`, `boolean`, `boolean` | `center=True`, `scale=True` | `light` | — |
| `pca_biplot_coords` | `x` | `matrix_handle`, `boolean`, `boolean`, `int_array`, `number`, `boolean` | `center=True`, `scale=True`, `biplot_scale=1`, `pc_biplot=False` | `light` | — |
| `pca_predict` | `x`, `newdata` | `matrix_handle`, `matrix_handle`, `boolean`, `boolean` | `center=True`, `scale=True` | `light` | — |
| `pca_n_components` | `x` | `matrix_handle`, `boolean`, `boolean`, `number` | `center=True`, `scale=True`, `cum_var_threshold=0.9` | `light` | — |
| `pca_stationarity_precheck` | `x` | `matrix_handle`, `enum`, `boolean`, `number` | `lshort=True`, `alpha=0.05` | `light` | — |

### Use when

many correlated indicators -> ONE composite index = PC1 (data-driven loadings); dimensionality reduction; cum_var for the number of components; scale=TRUE (default) for heterogeneous units; biplot chart-data (observation scores + variable arrows in the SAME scaled space) -> pca_biplot_coords; out-of-sample apply: fit on train, project NEW rows with the SAME center/scale -> pca_predict; how many components to keep BY A RULE (Kaiser-Guttman / cum-var / broken-stick) -> pca_n_components; BEFORE PCA on TIME SERIES: KPSS per column -> pca_stationarity_precheck

### Do not use when

charts as DRAWING (frontend; we supply ONLY coordinates); a latent factor with dynamics/mixed frequency/missing data -> dfms DFM #03; explicit/equal weights -> matrixStats panel_row_stats #116 / macro-arithmetic #82; NON-STATIONARY series in LEVELS -> #256 pca-nonstationary (pn_pca_nonstationary); elbow/scree as a rule (Cattell 1966: it requires VISUAL judgement, not a rule)

### Prerequisites

- pca_stationarity_precheck # ONLY when the input is TIME SERIES (in a cross-section stationarity is undefined)

### Alternatives

| instead use | when |
| --- | --- |
| #03 dfms (DFM) | a common latent factor with dynamics/mixed frequency/gaps (state space) rather than a static cross-section |
| #116 panel_row_stats / #82 macro-arithmetic | you want explicit/audited (equal/expert) weights instead of data-driven loadings |
| factanal | a measurement model with error terms (factor analysis), not maximisation of explained variance |
| #256 pca-nonstationary (pn_pca_nonstationary) | the columns are NON-STATIONARY time series (KPSS rejects) — the standardization of classical PCA is MATHEMATICALLY UNDEFINED there (Hamilton, Ma & Xi, NBER WP 32068) |

### Output fields

- composite: PC1 scores = the composite index (numeric of length n, names from rownames)
- loadings/scores: matrices (p x k / n x k) -> nested rows + dimnames
- var_explained/cum_var: the share & cumulative share per PC1/PC2/..; pc1_var = the share of the composite
- sdev, n_obs/n_vars/n_comp, center/scale (the applied arguments)
- pca_biplot_coords: obs_coords (n x 2) / var_coords (p x 2) / lambda (the COMMON scale factor) / components / var_explained — NUMBERS ONLY, no drawing (charter §5)
- pca_predict: scores_new / composite_new / rotation / center_used / scale_used (fit/apply externalization — a reproducible apply OUTSIDE the node: scale(new, center_used, scale_used) %*% rotation) / scores_train
- pca_n_components: k_kaiser + kaiser_threshold + kaiser_basis · k_cum_var + cum_var_threshold · k_broken_stick (sequential) + k_broken_stick_any + broken_stick_expected · k_min/k_max
- pca_stationarity_precheck: statistic/p_value/p_at_bound/trunc_lag/nonstationary PER COLUMN · columns_flagged/n_nonstationary/any_nonstationary/small_sample · warning_code/warning_message/recommended_node/recommended_fn/source (a STRUCTURED field, NOT message, NOT stop)

### Pitfalls

- PC signs are arbitrary (help Note, they differ by build/BLAS) -> an explicit sign normalization: each PC is flipped so that the max-\|loading\| is positive; interpret the direction from the loadings
- scale=TRUE is a hard gate against a constant/zero-variance column (otherwise 'cannot rescale a constant/zero column'); NA/Inf -> a cryptic svd error
- PC1 is z-score-like (mean~0), with no natural units -> for a base-100 index do a separate rebase; scale=FALSE lets the highest-variance column dominate
- the input must be a numeric matrix (NOT a data_frame -> silent character coercion), >=2 columns, >=3 rows
- predict.prcomp: it matches columns BY NAME ONLY if rownames(rotation) != NULL (that is, if the training matrix had colnames). WITHOUT colnames it checks ONLY the number of columns and projects SILENTLY WRONG results for reordered columns (live-verified: the same input, completely different scores) ⇒ pca_predict requires colnames on BOTH AND an identical ORDER
- biplot_scale is NOT the prcomp scale.: it is the lambda exponent of biplot.prcomp. stats only WARNS outside [0,1]; here it is a hard stop (charter §5)
- a biplot on a rank-deficient matrix (a duplicate/collinear column): sdev ~ 1.18e-16 (NOT exactly 0) -> lam ~ 0 -> silently enormous observation coordinates. Gated with the documented tol of the prcomp routine: sqrt(.Machine.double.eps) * sdev[1]
- the Kaiser-Guttman «eigenvalue > 1» rule HOLDS ONLY on a CORRELATION matrix (scale=TRUE, mean eigenvalue == 1). On a COVARIANCE matrix (scale=FALSE) the threshold is mean(eigenvalues) (Jolliffe 2002 §6.1.2) — which is why kaiser_threshold + kaiser_basis are returned explicitly
- broken-stick: «ALL of them pass» is MATHEMATICALLY IMPOSSIBLE (sum(var_explained) == sum(b_j) == 1); k_broken_stick (which stops at the FIRST failure) and k_broken_stick_any DIFFER (e.g. on ~independent columns: k=0 but k_any=2)
- kpss_test gives a p-value ONLY within [0.01, 0.10] (interpolation in KPSS 1992 Table 1) and warns at the bounds ⇒ alpha is gated to [0.01, 0.10] + p_at_bound per column
- non-stationarity is NOT a stop: the node must stay fully usable on CROSS-SECTION data (countries/firms), where stationarity is not even defined — hence a STRUCTURED warning is returned

### References

- Venables & Ripley, Modern Applied Statistics with S (2002); Jolliffe, Principal Component Analysis (2002) §6.1.1/§6.1.2
- OECD/JRC Nardo et al., Handbook on Constructing Composite Indicators (2008) — PCA weighting
- the biplot.princomp routine (lam = (sdev*sqrt(n))^scale; obs /lam, vars *lam; pc.biplot) · Gabriel KR (1971), Biometrika 58(3):453-467
- Kaiser HF (1960), Educ. Psychol. Meas. 20:141-151 · Guttman L (1954) — eigenvalue>1 on a correlation matrix
- Frontier S (1976) · Jackson DA (1993), Ecology 74(8):2204-2214 — broken-stick b_j = (1/p) sum_{i=j.p} 1/i
- Cattell RB (1966) — elbow/scree is REJECTED as a rule (it requires visual judgement, not a rule)
- Hamilton, Ma & Xi, NBER WP 32068 — for a non-stationary variable the population mean is undefined and the sample sd diverges ⇒ PCA standardization is invalid
- Kwiatkowski, Phillips, Schmidt & Shin (1992), J. Econometrics 54:159-178 · the kpss_test routine (lshort=TRUE ⇒ trunc lag floor(4*(n/100)^0.25); Table 1 ⇒ small_sample = n<30; a p-value only within [0.01,0.10])

## #118 — Parametric distributions (normal/student_t) as a numeric grid: quantile bands / cdf / density / moments (fan-chart data)

**Module:** `parametric_distributions_numeric.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `dist_fan_quantiles` | `mu`, `sigma` | `enum`, `num_array`, `num_array`, `num_array`, `num_array` | — | `light` | — |
| `dist_prob_cdf` | `mu`, `sigma`, `at` | `enum`, `num_array`, `num_array`, `num_array`, `num_array` | — | `light` | — |
| `dist_density_grid` | `mu`, `sigma`, `at` | `enum`, `num_array`, `num_array`, `num_array`, `num_array` | — | `light` | — |
| `dist_moments` | `mu`, `sigma` | `enum`, `num_array`, `num_array`, `num_array` | — | `light` | — |

### Use when

a forecast/scenario from PARAMETERS (mean/sd, df) -> numeric data for the frontend: fan bands per horizon, CDF/tail probability, a density curve, moments

### Do not use when

density-forecast scoring (CRPS/LogS/PIT) -> scoringRules #94; empirical quantiles from a sample -> quantile/caTools #110; FITTING a distribution to data -> #12 (this takes parameters, it does not fit); charts -> frontend

### Alternatives

| instead use | when |
| --- | --- |
| #94 scoringRules | density-forecast EVALUATION (CRPS/LogS/PIT) rather than grid generation |
| student_t vs normal | fat tails in the scenario -> student_t (a small df); otherwise normal (df->inf) |

### Output fields

- dist_fan_quantiles: quantiles (matrix n_dist x n_probs) + probs/family/params + mean/sd
- dist_prob_cdf: cdf (n_dist x n_at) in [0,1]; dist_density_grid: density (n_dist x n_at) >=0
- dist_moments: mean/variance/sd per distribution

### Pitfalls

- probs must be strictly in (0,1): probs>1 => a silent WARN 'NaNs produced' (silently wrong); 0/1 => ±Inf (hard gate)
- Student-t: the variance is infinite for df<=2, the mean is undefined for df<=1 => to_mcp null (NOT 0)
- sigma is a scale, NOT the sd for a t: sd = sigma*sqrt(df/(df-2)) for df>2; recycling of length 1 or L (otherwise a clean stop)

### References

- distributional reference/pkgdown (dist_normal/dist_student_t/cdf/variance; generics quantile/density) v0.8.1
- O'Hara-Wild et al., distributional: Vectorised Probability Distributions

## #119 — US NBER recession chronology — recession-shading intervals + a per-date 0/1 recession dummy (nberDates)

**Module:** `nber_recession_chronology.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `nber_recessions` | — | `string`, `string`, `boolean` | `as_date=False` | `light` | — |
| `nber_recession_flag` | `dates` | `series_codes`, `boolean` | `as_date=False` | `light` | — |

### Use when

the official NBER peak->trough recession intervals as numeric data -> recession-shading bands (frontend) or a 0/1 recession-dummy regressor aligned to a series

### Do not use when

DRAWING the bands (nberShade/ymdShade/romerLines — frontend); non-US or data-driven turning-point dating (the NBER chronology is fixed); Romer dates (not exposed)

### Alternatives

| instead use | when |
| --- | --- |
| reader/data nodes + tsbox #78 | you need the series itself/transformations, not a recession reference |
| nber_recession_flag | you want a 0/1 dummy per date rather than intervals for shading |

### Output fields

- recessions: records df start/end = peak->trough (yyyymmdd int by default, or Date); overlap-clipped to [from,to]
- flags: records df date/in_recession 0/1 + n_recession_periods
- metadata: n_recessions/n, from/to (yyyymmdd), as_date

### Pitfalls

- the window is INCLUSIVE at both ends (Start=peak & End=trough are inside the recession); the day after the trough => 0
- a recession-free [from,to] => 0 rows (valid, NOT an error)
- 20200101 is a yyyymmdd INTEGER, NOT a year; from=2020 errors (not an 8-digit date)

### References

- Hallman, tis: Time Indexes and Time Indexed Series ( tis); NBER Business Cycle Dating Committee (nber.org)

## #120 — Numeric rescaling (min-max / around-mid) + axis break positions (extended/log) + label strings (number/percent)

**Module:** `numeric_rescaling_axis.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `scale_rescale` | `x` | `series_handle`, `num_array`, `num_array` | `to=[0, 1]` | `light` | — |
| `scale_rescale_mid` | `x` | `series_handle`, `number`, `num_array`, `num_array` | `mid=0`, `to=[0, 1]` | `light` | — |
| `scale_breaks` | `x` | `series_handle`, `integer`, `enum`, `number` | `n=5`, `base=10` | `light` | — |
| `scale_labels` | `x` | `series_handle`, `enum`, `number`, `string` | `big_mark=''` | `light` | — |

### Use when

a DATA helper: linear rescaling of a series to a target range, computing axis-break positions as DATA (Wilkinson/log), formatting numbers into number/percent label strings

### Do not use when

macro-semantic rebase/deflate/per-capita -> macro-arithmetic #82 / ts_rebase #78; chart/colour palettes/ggplot scale objects -> frontend; z-score standardization -> ts_standardize #78

### Alternatives

| instead use | when |
| --- | --- |
| #78 ts_standardize | you want a z-score (mean/sd) rather than a min-max range rescale |
| #82 macro_rebase | you want a date-anchored base=100 index with economic meaning rather than a mechanical [0,1] |

### Output fields

- values: the rescaled numeric (the same length as x, NA preserved) + to/from/mid/n
- breaks: numeric axis positions (round numbers, n_breaks~n, NOT exactly n) + n_breaks/type/base
- labels: character label strings (percent = x100 + '%') + type/n

### Pitfalls

- to/from MUST be numeric of length 2; length 1 => zero_range => mean(to) for EVERY element (silently wrong, gated)
- n>=1 integer (n<=0 => extended loops forever); base>1 (base<=1 => breaks_log loops forever); type='log' requires positive values
- scale_rescale is a min-max range rescale (NOT a z-score, NOT a base=100 index); a constant series => mean(to)

### References

- scales reference: rescale/rescale_mid (to=c(0,1), from=range(x,na.rm,finite), mid=0), breaks_extended/breaks_log(n,base), label_number/label_percent(accuracy,big.mark)
- Wickham & Seidel, scales: Scale Functions for Visualization (, scales); Talbot/Lin/Hanrahan 2010 extended breaks

## #121 — Analytic OLS on a CLOSED formula: a deterministic time trend (linear/quadratic) + the detrended series, or response ~ named numeric predictor columns (lm + broom tidy/glance)

**Module:** `analytic_ols_closed.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ols_trend` | `y` | `series_handle`, `enum` | — | `light` | `model` |
| `ols_regress` | `data`, `response`, `predictors` | `df_handle`, `string`, `series_codes` | — | `light` | `model` |

### Use when

a fast deterministic (analytic QR, no seed) linear model in the data layer: removing a deterministic trend (ols_trend->detrended) or a simple regression on explicitly named numeric columns (ols_regress); the formula is ALWAYS closed (an enum or bare names) through reformulate

### Do not use when

charts (frontend); a stochastic trend/unit root -> differencing & unit-root tests #2 (not a deterministic detrend, which is spurious); factors/interactions/WLS/offset (a numeric-only closed design); residual diagnostics -> pass the model handle to lmtest/FinTS #76

### Alternatives

| instead use | when |
| --- | --- |
| #82 macro-arithmetic | explicit macro conventions (growth/deflate/rebase) rather than a model |
| #56 mFilter/HP trend-cycle | a flexible/non-parametric trend rather than a low-order polynomial |
| #2 unit-root tests (urca) | the question is detrending vs differencing (trend- vs difference-stationary) |

### Output fields

- coefficients: tidy -> term/estimate/std_error/statistic(t)/p_value (records)
- glance: glance -> r_squared/adj_r_squared/sigma/AIC/BIC/log_lik/df_residual/nobs
- fitted/residuals: numeric vectors; ols_trend adds detrended (=the trend residuals); n/k observations/parameters
- model: the fitted lm — a producer handle (RDS bucket) for diagnostics/prediction nodes

### Pitfalls

- NA/Inf: the gates reject them up front — there is NO silent na.omit that would change the sample (do imputation #80 first)
- detrend vs difference: ols_trend removes a DETERMINISTIC trend; on a unit-root series the residuals stay non-stationary -> difference instead
- collinearity: perfectly collinear predictors -> lm gives an NA coefficient SILENTLY; here a rank-deficient stop; n==k (saturated) -> sigma=NaN, gated as n is not > k

### References

- stats lm/reformulate (the reference base docs, r-btw docs_help_page)
- broom tidy.lm/glance.lm ( broom 1.0.x, docs.ropensci.org/broom)
- Wooldridge Introductory Econometrics (deterministic trend/detrending); Hamilton Time Series Analysis ch.3 (the trend- vs difference-stationary caveat)

## #252 — CORRELATION FILTER: greedy removal of highly correlated variables (findCorrelation over a VALIDATED correlation matrix) + an out-of-sample APPLY with the fitted column names

**Module:** `correlation_filter_greedy.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `cf_cor_matrix` | `x` | `matrix_handle`, `enum` | — | `light` | — |
| `cf_find_correlation` | `cor_matrix` | `matrix_handle`, `number`, `boolean` | `cutoff=0.9`, `exact=True` | `light` | — |
| `cf_filter` | `x` | `matrix_handle`, `number`, `boolean`, `enum`, `series_codes` | `cutoff=0.9`, `exact=True` | `light` | `data` |

### Use when

PRE-PROCESSING before a high-dimensional/collinearity-sensitive model (regression, PCA, ML): on an observations x variables matrix (countries x indicators, periods x variables) you drop AS MANY COLUMNS as needed so that NO remaining pairwise \|r\| exceeds the cutoff; the rule: for every pair above the threshold, the variable with the LARGEST MEAN \|correlation\| with ALL the others (= the most redundant overall) is deleted; the flow: cf_cor_matrix (a VALIDATED p x p matrix) -> cf_find_correlation (WHICH ones go) -> cf_filter (fit + apply)

### Do not use when

TIME SERIES IN I(1) LEVELS (spurious correlation — supply DIFFERENCES EXPLICITLY; NEVER an implicit differencing here); a SIGNIFICANCE test for a correlation (p-values/CI/multiplicity) -> #81 desc_cor_test; DISTANCES/clustering/MDS (a dist object, as.dist(1-r)) -> #240 dm_cor_dist (cat 29); dimension COMPRESSION instead of SELECTION (you keep all the information in a few axes) -> #117 prcomp; exact LINEAR COMBINATIONS of dependence (QR-based) -> findLinearCombos (NOT exposed); stateful preProcess/recipes pipelines (EXPLICITLY REJECTED, the normative gate spec §3b); charts/heatmaps (the frontend, §5); p = 1 (>= 2 variables are required)

### Prerequisites

- cf_cor_matrix # FIRST the VALIDATED matrix: max_abs_offdiag/mean_abs_cor/n_pairs show WHETHER filtering is needed and at which cutoff
- c00_data_utilities/replacement_missing_values.imputets_kalman # NA are a hard gate here (they would become NA in the correlation matrix)
- c01_preparation_prechecks/unit_root_normality.run_adf_test # IF the columns are time series: confirm stationarity FIRST, otherwise the sample correlation is spurious (§3b gate 3)

### Alternatives

| instead use | when |
| --- | --- |
| cf_find_correlation(exact = TRUE) [DEFAULT] | ALWAYS, unless p is very large: it recomputes the mean correlations at EVERY step and removes FEWER variables («The exact calculations will remove a smaller number of predictors but can be much slower», the findCorrelation routine Details) |
| cf_find_correlation(exact = FALSE) | ONLY when p is so large that the exact path is prohibitively slow; an EXPLICIT choice — the two paths give DIFFERENT sets (live on the help-page R1, cutoff 0.6: exact -> {x1,x4,x5}; fast -> {x1,x3,x4,x5}) |
| method = 'spearman' / 'kendall' | the relation is MONOTONE but not linear, or outliers are present (rank-based, robust); kendall is O(n^2) and is slow at large n; the default pearson = a LINEAR relation |
| cf_filter(keep = <keep_names of a previous fit>) | NEW data (test/out-of-sample): it applies THE SAME filter WITHOUT re-estimation (§3b gate 6); CRITICAL — a re-fit on the test set changes the COLUMN SET and the model breaks (live-verified in the tests: a different sample -> a different filter) |
| #117 pca_composite (prcomp) | you want COMPRESSION (all the variables contribute to a few orthogonal axes) rather than the SELECTION of a subset of columns; the filter keeps INTERPRETABLE original variables, PCA does not |
| cutoff 0.75 (aggressive) vs 0.9 (default) vs 0.95 (conservative) | the smaller the cutoff, the more columns leave; read max_abs_offdiag/n_pairs_above_before from cf_cor_matrix first — if max\|r\| < cutoff NOTHING leaves |

### Output fields

- cf_cor_matrix: cor (a p x p VALIDATED matrix — heatmap chart-data) + method/use('everything', PINNED) + n/p/variables + mean_abs_cor (THE greedy criterion, per variable) + max_abs_offdiag/max_abs_pair/max_abs_index + min_cor/max_cor/n_pairs + eigen_min/is_psd (a PSD DIAGNOSTIC, NOT a gate)
- cf_find_correlation: remove_index/remove_names AND keep_index/keep_names (= the FITTED PARAMS, §3b gate 6; ALWAYS sorted ascending) + n_variables/n_removed/n_kept/share_removed
- cf_find_correlation: max_abs_before vs max_abs_after (+ max_abs_pair_before/after) and n_pairs_above_before vs n_pairs_above_after (ALWAYS 0 — the algorithm's invariant) — the main «before/after» chart-data
- cf_filter: data (THE FILTERED DATA, n x n_variables_out — it becomes a handle: the card's SOLE producer/register) + mode ('fit' \| 'apply') + keep_names/remove_names + n_variables_in/out + n/cutoff/exact/method/variables
- cf_filter in mode='apply': cor/mean_abs_cor = NULL and max_abs_before/after = NA — DOCUMENTED, it means «NO re-estimation» (a pure column subselection)

### Pitfalls

- DETERMINISM #1 (§5): the documented caret default is exact = ncol(x) < 100 — THE ALGORITHM CHANGES AT 100 COLUMNS. A node that changed path because the user added the 100th variable would be NON-REPRODUCIBLE => 'exact' is an EXPLICIT argument with OUR OWN constant default TRUE, NEVER the package default
- DETERMINISM #2: the ORDER of the indices caret returns depends on the column order (live: the same SET, a different ORDER when they are reversed) => CANONICALIZATION, ALWAYS ascending sorted indices/names are returned. No randomness anywhere (no RNG/seed); identical over 2 runs is pinned in the tests (the wrapper AND the node path)
- SILENTLY WRONG (the main reason the wrapper exists): findCorrelation REQUIRES A CORRELATION MATRIX, but with exact=FALSE it SILENTLY accepts RAW DATA (live: a 10x5 random matrix -> «2 3 1» as if these were correlations); ONLY the exact path checks symmetry («correlation matrix is not symmetric») => OUR OWN symmetry/diagonal/range checks ALWAYS, on both paths
- SILENTLY WRONG: a non-square 3x4 matrix + exact=FALSE -> numeric(0) SILENTLY; p=1 + exact=FALSE -> numeric(0) SILENTLY (exact: «only one variable given»); diag != 1 (e.g. 5) AND \|r\| > 1 (e.g. 3) pass SILENTLY on BOTH paths — that is, ANYTHING symmetric is accepted as a «correlation» (did you supply a COVARIANCE matrix? -> cov2cor)
- SILENTLY WRONG: a CONSTANT (zero-variance) column => cor emits ONLY the warning «the standard deviation is zero» and fills the WHOLE row/column with NA (live-verified, the engine); findCorrelation then fails cryptically («The correlation matrix has some missing values.» or, on the exact path, «missing value where TRUE/FALSE needed») => a hard gate that NAMES the constant columns
- SILENTLY WRONG: cor with n = 1 -> an ENTIRELY NA matrix WITHOUT even a warning; with n = 2 -> every \|r\| is 1 BY DEFINITION (two points define a line) => a hard gate n >= 3 in the FIT (in the APPLY n >= 1 suffices: the names are GIVEN, not estimated)
- SILENTLY WRONG: cutoff = 1.5 -> integer(0) SILENTLY (nothing is filtered); cutoff <= 0 -> it removes almost EVERYTHING. caret does NOT check => a hard gate 0 < cutoff < 1
- §3b GATE 6 (fit/apply externalization): keep_names/remove_names ARE the fitted params and are ALWAYS returned; cf_filter(keep=..) applies them to NEW data WITHOUT re-estimation. If the filter is re-estimated on the test set, the COLUMN SET CHANGES (different correlations) and the trained model's coefficients are applied to the WRONG columns (the KNIME «Normalize Model» pattern). That is also why duplicate colnames are a hard gate: the apply would be ambiguous
- §3b GATE 3 (non-stationarity): the node is CROSS-SECTION/PANEL. In I(1) LEVELS the sample correlation does NOT converge to a population parameter (spurious correlation, Granger-Newbold 1974; Hamilton-Ma-Xi for why the standardization is undefined) => supply DIFFERENCES EXPLICITLY upstream; NEVER an implicit differencing here
- §3b GATE 2 (no implicit standardization): correlation is INVARIANT to linear transformations => there is NO scale/center argument (it would be a no-op implying a non-existent option)
- PSD: A DOCUMENTED DEVIATION — a non-positive-semidefinite matrix is exposed as eigen_min/is_psd but does NOT block: the greedy algorithm stays well defined (it compares \|r\| per pair) and it is LIVE-VERIFIED that EVEN the R1 matrix of the help page itself has a minimum eigenvalue of -0.2634288 (the same holds for published matrices rounded to 2 decimals)
- PINNED ARGUMENTS: verbose=FALSE (findCorrelation(verbose=TRUE) PRINTS with cat — «Compare row 1 and column 5 with corr 0.85..» — a violation of §5) and names=FALSE (the help page's Value is INVERTED: «A vector of indices.. when names = TRUE», whereas LIVE it returns NAMES; we supply BOTH indices AND names, produced by us); cor(use='everything') PINNED — pairwise.complete.obs computes EVERY pair on a DIFFERENT sample and can yield a non-PSD, inconsistent filter
- MASKING: library(caret) is NOT called — requireNamespace + findCorrelation. caret drags in ggplot2 (Depends), which MASKS Position in the SHARED source env (live conflicts(detail=TRUE)); the S3 registration at namespace load (131 methods) is ALL on generics OF caret ITSELF (train./rfe./varImp./predictors. etc.) — NO predict.*/plot.*/update.* on a base/stats generic (compare quanteda `$.dfm`, proxy on `dist`)
- THE BOUNDARY vs #240 (dm_cor_dist, cat 29): there a DISTANCE object dist = as.dist(1-r) is produced for clustering — a DIFFERENT object, a DIFFERENT semantics (1-r reverses the direction and loses the sign) and it does NOT feed findCorrelation. cf_cor_matrix exists ONLY so that the node is usable end-to-end

### References

- caret 7.0.1 the findCorrelation routine (live-verified the engine): Usage «findCorrelation(x, cutoff = 0.9, verbose = FALSE, names = FALSE, exact = ncol(x) < 100)»; Details «If two variables have a high correlation, the function looks at the mean absolute correlation of each variable and removes the variable with the largest mean absolute correlation» + «Using exact = TRUE will cause the function to re-evaluate the average correlations at each step.. will remove a smaller number of predictors but can be much slower»; Value INVERTED («A vector of indices.. when names = TRUE»); the R1 example (5x5)
- Kuhn, M. & Johnson, K. (2013) Applied Predictive Modeling, Springer, ch. 3 «Data Pre-Processing» (the Removing Predictors / between-predictor correlations section) — the textbook source of the greedy procedure, as cited in the wrapper's header
- the cor routine's documentation / the sd routine — «the standard deviation is zero» warning-only on a constant column (live-verified: cor(cbind(a=1:4,b=rep(1,4))) -> NA + only a warning); use='everything'; cov2cor
- Granger, C.W.J. & Newbold, P. (1974) «Spurious regressions in econometrics», Journal of Econometrics 2(2) 111-120 — why the node is cross-section/panel and not for I(1) levels
- Hamilton, J.D., Ma, X. & Xi, J., «Principal Component Analysis for a Mix of Stationary and Nonstationary Variables», NBER WP 32068 — §3b normative gate 3 (non-stationarity ⇒ standardization/sample moments undefined); see #256
- the normative gate spec §3b normative gate 6 (fit/apply externalization; the KNIME Normalizer -> «Normalize Model» pattern) + gate 2 (no implicit standardization) + REJECTED: recipes/preProcess as a stateful pipeline
- wrapper footer IMPLEMENTATION NOTE (c00_data_utilities/correlation_filter_greedy) — 7 live-verified silently-wrong behaviours, the conflicts(detail=TRUE) of caret/ggplot2, and the invariant «no remaining \|r\| > cutoff» (600 random cases, exact AND fast, 0 violations)

## #253 — DESIGN MATRIX (feature engineering): ORTHOGONAL/RAW polynomials (poly + returning attr 'coefs'), INTERACTIONS without a formula surface (model_matrix), an allowlisted formula path, a COMBINATORIAL factor (interaction)

**Module:** `design_matrix_orthogonal.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ply_poly` | `x` | `matrix_handle`, `integer`, `boolean`, `num_array`, `num_array`, `string` | `degree=2`, `raw=False`, `name='x'` | `light` | — |
| `ply_interactions` | `data` | `df_handle`, `series_codes`, `integer`, `boolean`, `boolean`, `enum`, `raw`, `series_codes`, `enum`, `integer`, `integer` | `order=2`, `include_main=True`, `intercept=True`, `max_levels=30`, `max_columns=200` | `light` | — |
| `ply_model_matrix` | `data`, `formula` | `df_handle`, `formula`, `enum`, `raw`, `series_codes`, `enum`, `integer`, `integer` | `max_levels=30`, `max_columns=200` | `light` | — |
| `ply_interaction_factor` | `data`, `vars` | `df_handle`, `series_codes`, `boolean`, `string`, `boolean`, `boolean`, `integer` | `drop=False`, `sep='.'`, `lex_order=False`, `indicator=False`, `max_levels=200` | `light` | — |

### Use when

IMMEDIATELY BEFORE any regression/ML node, when you need NON-LINEARITY (polynomials: the Phillips curve, threshold-like relations) or INTERACTIONS (a*b, regime x variable, country x sector): the node builds the DESIGN MATRIX EXPLICITLY, GATED and — most critically — REPRODUCIBLY OUT OF SAMPLE (it returns AND accepts back the fitted params: coefs_alpha/coefs_norm2 · xlev + contrasts + column_names)

### Do not use when

model ESTIMATION (the node does NOT run a regression — it supplies ONLY the matrix X; the dependent variable does NOT belong here: the formula is ONE-SIDED); splines/semi-parametric bases (ns/bs — ANOTHER family, its own card); DISCRETISATION of a continuous variable into categories -> #255 binning; calendar dummies -> #254 hd_dummies; filtering of collinear columns -> #252 cf_filter; sparse matrices (sparse.model_matrix — a new dependency); stateful pipelines (recipes prep/bake — REJECTED, the normative gate spec §3b); charts (the frontend, §5)

### Prerequisites

- c00_data_utilities/replacement_missing_values.imputets_kalman # NA are a hard gate: model_frame DROPS ROWS SILENTLY (live 6 -> 5) and breaks the alignment with y
- ply_interactions # with order = 1: see FIRST how many columns the MAIN terms produce (column_bound/n_columns) before you raise the order — interactions multiply
- c00_data_utilities/discretisation_numeric_column.bn_quantile_bins # IF you want a CATEGORICAL interaction from a CONTINUOUS variable: discretise FIRST (interaction on a numeric column creates ONE LEVEL PER VALUE)

### Alternatives

| instead use | when |
| --- | --- |
| ply_interactions [THE RECOMMENDED ROUTE] | you want main terms + all interactions up to 'order' from VALIDATED COLUMN NAMES: NO formula comes from the user — the RCE surface DOES NOT EVEN EXIST (the formula is built internally from language objects; ZERO parse/eval) |
| ply_model_matrix (the formula path) | you GENUINELY need an expression that cannot be stated with names+order: I(x^2), log(x), nested factors, an explicit removal of terms; it passes TWICE through a default-deny allowlist (adapt_formula at L3 + an independent walk in the wrapper) and NEVER accepts a string |
| raw = TRUE (ply_poly) | you want INTERPRETABLE coefficients on the original scale (x, x^2, x^3); the price: SEVERE collinearity, and the p-values of the lower degrees CHANGE when a higher one is added. The default FALSE = an ORTHOGONAL basis (numerically stable, uncorrelated columns) |
| ply_poly(coefs_alpha, coefs_norm2) [APPLY] | NEW data: MANDATORY in order to produce THE SAME basis — a re-fit poly on the new data gives A DIFFERENT BASIS and the trained model's coefficients mean nothing (§3b gate 6) |
| xlev + expect_columns [the design matrix APPLY] | NEW data with factors: MANDATORY — with FEWER levels in newdata model_matrix produces SILENTLY FEWER COLUMNS (live-verified) and the coefficients land in the WRONG POSITIONS |
| contrasts = 'contr.sum' instead of 'contr.treatment' | you want interactions interpretable as DEVIATIONS FROM THE MEAN (the main term stops being «relative to the first level»); 'contr.helmert' = successive contrasts; 'contr.poly' = orthogonal polynomials for ORDERED factors |
| ply_interaction_factor | you want ONE COMBINATORIAL FACTOR (e.g. country x regime as A SINGLE categorical column for fixed effects/grouping) instead of column products in a design matrix |
| rank_check = 'report' (instead of 'auto') | the DOWNSTREAM node is regularized (ridge/lasso, cat 20) and rank deficiency is not an error; 'auto' (the default) is STRICT ('stop') in the FIT and TOLERANT ('report') in the APPLY, where an absent level is NORMAL |

### Output fields

- ply_poly: basis (n x degree — chart-data) + column_names (name_poly1.d) + degree/raw + coefs_alpha (length degree) / coefs_norm2 (length degree+2) / coefs_source ('fitted'\|'supplied'\|'raw') = THE FITTED PARAMS (§3b gate 6) + orthonormality_error/centering_error (ONLY on the fit path) + n/n_unique/x_min/x_max/name
- ply_interactions & ply_model_matrix: design (an n x k BARE numeric matrix) + column_names/n_columns/n_rows + column_term & assign (COLUMN -> TERM; 0 = intercept) + term_labels/n_terms/intercept + formula (deparsed)
- ply_interactions & ply_model_matrix: xlev (THE LEVELS PER FACTOR) + xlev_source ('fitted'\|'supplied') + contrasts/contrasts_arg + variables/factor_vars/numeric_vars = THE design matrix's FITTED PARAMS (§3b gate 6)
- ply_interactions & ply_model_matrix: rank + rank_deficient + rank_check/rank_check_arg + column_bound (THE UPPER BOUND checked BEFORE construction) + max_columns/max_levels; ply_interactions additionally order/include_main/built_formula
- ply_interaction_factor: levels + codes (1.n_levels per row) + counts (chart-data) + n_levels/n_used_levels + empty_levels/n_empty_levels/has_empty_levels + indicator (n x n_levels 0/1 or NULL) + input_levels (fit/apply) + combinations/drop/sep/lex_order/n

### Pitfalls

- §3b GATE 6 — THE NODE'S REASON FOR EXISTING: an ORTHOGONAL polynomial is NOT a function of x alone — it depends on the CENTRES/NORMS (alpha, norm2) computed ON THE TRAINING SAMPLE. A re-fit poly on new data => A DIFFERENT BASIS => the model's coefficients mean nothing. That is why the coefs are returned AS NUMBERS and accepted back (the KNIME Normalizer -> «Normalize Model» pattern); poly(simple=TRUE) DISCARDS the coefs (live: attributes = only dim/dimnames), which is why it is NOT exposed
- §3b GATE 6 (b) — A SILENTLY WRONG BEHAVIOUR OF model_matrix: newdata with FEWER factor levels produces FEWER COLUMNS WITHOUT ANY ERROR (live-verified: ~a*g with 3 levels -> (Intercept),a,gy,gz,a:gy,a:gz; the same newdata with 2 levels -> (Intercept),a,gy,a:gy) => the coefficients are applied at the WRONG POSITIONS. That is why xlev + expect_columns are returned/accepted, with a hard gate on an UNKNOWN level («factor a has new level..») AND on a different column set
- SECURITY (.claude/rules/security.md — NEVER eval(parse)): ply_interactions EXPOSES NO formula surface; it builds the RHS with call/as.symbol over names that (a) really exist in data and (b) pass the strict identifier regex ^[A-Za-z.][A-Za-z0-9._]*$, and implants it into a TEMPLATE formula (f <- ~0; f[[2]] <- rhs; environment(f) <- baseenv) => ZERO parse/str2lang/as.formula(text)/eval
- SECURITY (ply_model_matrix, THREE LAYERS OF DEFENCE): (1) at L3 the string passes ONLY through adapt_formula (the reference/mcp/formula_allowlist — a default-deny allowlist walk WITHOUT eval + a sealed enclosure); (2) the wrapper does NOT accept a string AT ALL, only an object of class formula; (3) an INDEPENDENT default-deny allowlist walk (.ply_validate_lang) that works EVEN under a bare source and ADDITIONALLY restricts EVERY symbol to the data's column names. ONLY these are allowed: ~ + - * : ^ ( I log log1p log2 log10 exp sqrt abs poly factor as.factor ordered interaction; the '.' shorthand is explicitly rejected; expression depth <= 64; the call head MUST be a plain symbol (NOT fn or (fn))
- SILENTLY WRONG (poly): a FRACTIONAL degree does NOT error — it is SILENTLY truncated downwards (live: poly(x, degree=1.5) -> 1 column); WRONG coefs LENGTHS -> a column FULL OF NA WITHOUT an error (hence the gate length(alpha)==degree AND length(norm2)==degree+2, live-verified: degree 3 -> 3 and 5); coefs TOGETHER WITH raw=TRUE -> SILENTLY ignored; degree >= the number of unique values: the ORTHOGONAL poly errors («'degree' must be less than number of unique points») but the RAW one does NOT — it produces LINEARLY DEPENDENT columns => THE SAME gate on both paths
- SILENTLY WRONG (NA): model_frame SILENTLY DROPS the incomplete rows (live 6 -> 5) and the design matrix CEASES to be aligned with y => PINNED na.action = na.fail + OUR OWN explicit NA/Inf gate BEFORE the call, ONLY on the columns actually used; PINNED drop.unused.levels = FALSE (TRUE would NULLIFY the xlev)
- SILENTLY WRONG (RANK DEFICIENCY): empty level combinations produce aliased columns — live-verified qr(mm).rank = 2 over 4 columns WITHOUT any error; lm on such a matrix returns SILENTLY NA coefficients. The node ALWAYS computes the rank and blocks according to rank_check ('auto' = stop in the FIT, report in the APPLY)
- SILENTLY WRONG (interaction): interaction accepts a NUMERIC column WITHOUT COMPLAINT and creates ONE LEVEL PER UNIQUE VALUE (live: levels «1.5.a»..) => a hard gate, discretise first (#255); with drop=FALSE (the documented default) the EMPTY levels REMAIN and are reported explicitly (empty_levels), but indicator=TRUE IS BLOCKED under empty levels: each empty level gives a column FULL OF ZEROS -> rank deficiency -> silent NA in lm
- DIMENSION EXPLOSION: an UPPER BOUND on columns is checked BEFORE the matrix is built (prod(nlevels) per term; numeric = 1) => a giant matrix is NEVER constructed; max_levels defaults to 30 per factor, max_columns to 200 (in ply_interaction_factor max_levels defaults to 200 and the PRODUCT of the levels is checked BEFORE the call when drop=FALSE); a factor with ONLY 1 level -> the cryptic «contrasts can be applied only to factors with 2 or more levels» is caught BEFOREHAND
- ORTHONORMALITY: it is checked (max\|X'X - I\| and max\|colSums\|) ONLY on the FIT path — OUT OF SAMPLE IT DOES NOT HOLD BY DESIGN (the basis is orthogonal WITH RESPECT TO THE TRAINING SAMPLE, not with respect to every new x); on the apply path the two fields are NA — EXPECTED, not an error
- MASKING: ZERO — the file does NOT call library on any package (only stats/base/utils, ALWAYS attached); the live conflicts(detail=TRUE) is IDENTICAL to the baseline before/after the source. CONVERSELY, because OTHER wrappers in the shared env mask core generics, ALL the calls are stats::/base::/utils:: qualified
- DETERMINISM (§5): NO RNG path (poly = QR/a three-term recursion; model_matrix/interaction = combinatorial) => NO seed argument; identical over 2 runs is pinned in the tests (the wrapper AND the node path). TERMINAL nodes: no register — the fit/apply is EXPLICIT (the user hands back coefs/xlev/expect_columns)

### References

- the poly routine's documentation (live-verified): «poly(x,.., degree = 1, coefs = NULL, raw = FALSE, simple = FALSE)»; class c('poly','matrix'); attr 'coefs' = list(alpha, norm2) ONLY when raw = FALSE (degree 3 -> length(alpha)=3, length(norm2)=5 = degree+2; simple=TRUE -> attributes ONLY dim/dimnames); «'degree' must be less than number of unique points»; predict.poly ≡ poly(new, degree, coefs=) (all.equal)
- the model_matrix routine's documentation / the terms routine / the model_frame routine — attr 'assign' (column -> term, 0 = intercept), attr 'contrasts', contrasts.arg, na.action, drop.unused.levels; «contrasts can be applied only to factors with 2 or more levels»; live-verified silent column loss in newdata with fewer levels AND silent dropping of rows with NA (6 -> 5)
- the interaction routine's documentation (drop = FALSE, sep = '.', lex.order = FALSE) — the documented default drop=FALSE keeps ALL the combinations; the qr routine (rank) for the rank-deficiency check
- the contr.treatment routine's documentation / contr.sum / contr.helmert / contr.poly — the four exposed factor codings (the reference default = contr.treatment, relative to the FIRST level)
- .claude/rules/security.md — «Never use eval(parse(text = user_input)) with untrusted input»; the reference/mcp/adapt_formula (a default-deny allowlist walk + a sealed enclosure) = THE ONLY point where a string becomes a formula
- the normative gate spec §3b normative gate 6 (fit/apply externalization: «every scaling/discretisation/poly node must return the fitted params.. attr(poly,'coefs').. otherwise the out-of-sample apply is not reproducible»; the KNIME Normalizer -> «Normalize Model» pattern) + the live-verified gate «poly: 'degree' must be less than number of unique points» + REJECTED recipes (stateful prep/bake)
- wrapper footer IMPLEMENTATION NOTE (c00_data_utilities/design_matrix_orthogonal) — the omissions (simple=TRUE, multivariate poly, predict.poly, na.omit/na.pass, drop.unused.levels, sparse.model_matrix, ns/bs), the ZERO masking (live conflicts), the formula's three layers of defence, and every live-verified silently-wrong behaviour

## #254 — CALENDAR EFFECTS: holidays for G7+CH & financial centres (NYSE/LONDON/ZURICH/TSX) -> NAMED 0/1 columns aligned to a given vector of dates + isWeekday/isBizday

**Module:** `calendar_effects_holidays.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `hd_list` | — | `string` | `pattern='.*'` | `light` | — |
| `hd_holidays` | `year` | `int_array`, `series_codes`, `enum`, `enum` | `calendar='none'`, `nyse_type='all'` | `light` | — |
| `hd_dummies` | `dates` | `series_codes`, `series_codes`, `enum`, `enum`, `raw`, `enum`, `int_array` | `calendar='none'`, `nyse_type='all'`, `dummy_type='per_holiday'`, `wday=[1, 2, 3, 4, 5]` | `light` | — |

### Use when

DAILY/WEEKLY macro or financial series with DETERMINISTIC calendar disturbances (national holidays, exchange closures, the MOVING Easter): you produce EXPLICIT exogenous 0/1 dummies (exog_handle) for ARIMA/regression/GARCH; without them the calendar contaminates the residuals and shows up FALSELY as seasonality or ARCH. The flow: hd_list (WHICH names exist — 120 in total) -> hd_holidays (THE DATES per holiday/year) -> hd_dummies (aligned 0/1 columns + weekday/bizday flags)

### Do not use when

COUNTING business days / date rolling / offsets under a custom calendar -> #112 bizdays (create.calendar/bizdays/add.bizdays/adjust.next); general date & frequency algebra -> #111 lubridate / #113 tsibble / #78 tsbox; SEASONAL ADJUSTMENT (X-13/SEATS trading-day & Easter regressors INSIDE the model) -> #4 Seasonal-wrapper (cat 01); MONTHLY/QUARTERLY data where a holiday is not a discrete event (there you want trading-day/leap-year regressors, not day dummies); NON-calendar regime dummies -> #255 binning or #253 ply_interaction_factor; charts (the frontend, §5); NON-G7 countries outside the timeDate catalogue (see hd_list — the catalogue is CLOSED)

### Prerequisites

- hd_list # A MANDATORY FIRST STEP: the VALID holiday names (an unknown name = a hard gate); 120 in total, US 18 · CA 6 · GB 4 · DE 5 · FR 6 · IT 6 · JP 33 · CH 5 (live-verified, timeDate 4052.112)
- hd_holidays # THE DATES before the dummies: empty_sources/n_on_weekend show whether the holiday really exists in the requested years and how many fall on Sat/Sun

### Alternatives

| instead use | when |
| --- | --- |
| hd_dummies(dummy_type = 'per_holiday') [DEFAULT] | you want a DIFFERENT coefficient per holiday (e.g. Christmas vs Thanksgiving have a different effect size); it costs one degree of freedom per holiday |
| dummy_type = 'aggregate' | few observations or few events per holiday -> ONE column 'holiday_any' (1 = any holiday); fewer degrees of freedom, a single common effect. The is_holiday vector is returned ALWAYS, whatever the choice |
| dummy_type = 'both' | you want BOTH the per-holiday columns AND the aggregate (e.g. per-holiday in the model, aggregate in the chart) |
| calendar = 'NYSE' \| 'LONDON' \| 'ZURICH' \| 'TSX' | FINANCIAL daily data: a CLOSED MARKET is a STRUCTURAL GAP (not a missing value); it gives ONE column named after the centre, IN ADDITION to the named holidays |
| nyse_type = 'special' (only with calendar = 'NYSE') | you want ONLY the EXTRAORDINARY closures (e.g. 2001-09-11.14) — shock events, not institutional holidays; 'standard' = only the institutional ones; 'all' (the default) = ALL |
| hd_dummies(holiday_dates = <holiday_dates of a previous node>) [APPLY] | a NEW sample (out-of-sample/the next wave): IDENTICAL columns IN THE SAME ORDER, even if some holiday does not fall inside it, INDEPENDENTLY of the timeDate version (§3b gate 6). MUTUALLY EXCLUSIVE with holidays/calendar/nyse_type |
| #112 bizdays (create.calendar/bizdays) | you do not want dummies but a COUNT of business days between dates, date shifting (adjust.next/previous) or the generation of a bizseq under a custom calendar |

### Output fields

- hd_list: holidays (the NAMES matching the pattern) + n + all_holidays/n_all (120) + countries + count_by_country (bar chart-data; US 18 · CA 6 · GB 4 · DE 5 · FR 6 · IT 6 · JP 33 · CH 5) + n_matched_by_country + calendars (NYSE/LONDON/ZURICH/TSX) + year_min/year_max (1583/2200) + empty
- hd_holidays: dates (SORTED, UNIQUE, 'YYYY-MM-DD') + n_dates + date_table (records {source, year, date} — chart-data) + count_by_source + years/n_years
- hd_holidays/hd_dummies: holiday_dates = THE FITTED PARAM (§3b gate 6; a named list holiday -> dates); it is passed VERBATIM to hd_dummies(holiday_dates=) for an out-of-sample apply
- hd_holidays: empty_sources/n_empty_sources (A SILENT GAP: a holiday that DID NOT YET EXIST -> 0 dates WITHOUT an error) + n_on_weekend/share_on_weekend + dates_per_year
- hd_dummies: dummies (n x k 0/1 — chart-data; ROWS = the GIVEN dates in the GIVEN order, COLUMNS = the sources in the GIVEN order) + dummy_levels (column NAMES+ORDER = a fitted param) + n_columns + count_by_column
- hd_dummies: is_holiday/n_holiday/share_holiday + is_weekday/n_weekday + is_bizday/n_bizday + n_holiday_on_weekday + wday + mode ('fit'\|'apply') + dummy_type + empty_holiday_set/n_holiday_dates
- hd_dummies: constant_columns/n_constant_columns = THE ALL-ZERO COLUMNS (the holiday does not fall inside the sample) — they are NOT removed (that would break the fit/apply) but are FLAGGED: a rank-deficient design, on which lm returns SILENTLY an NA coefficient

### Pitfalls

- TRAP #1 (NAMES VIA get): holiday calls match.fun(Holiday) on a CHARACTER STRING => get(name, mode='function', envir=<caller>); WITHOUT an attach the name is NOT found (live: «object 'USNewYearsDay' of mode 'function' was not found»). THE FIX: we pass the FUNCTION OBJECT via getExportedValue('timeDate', nm) — the help page itself documents this («a list of the unquoted function names») => requireNamespace SUFFICES and masking is avoided entirely. AN ADDITIONAL hard gate: EVERY name is checked against listHolidays BEFORE the call, with an explicit message + «nearby» names
- MASKING (WHY library(timeDate) IS NOT CALLED) — live conflicts(detail=TRUE), the engine: the attach adds abline · lines · plot · points · getDataPart · initialize · Ops · show · sample. plot/lines/abline/points ARE HARMLESS (§5: we NEVER draw) — THE CRITICAL ONE IS `sample`: timeDate promotes it to an S4 standardGeneric (live: isGeneric('sample') -> TRUE) and `sample` is used by bootstrap/simulation wrappers in the SHARED source env (boot/MCS/tsDyn/BVAR); likewise Ops/show/initialize/getDataPart are S4 generics of other packages. WITH requireNamespace the conflicts output is IDENTICAL to the baseline (zero new entries); the S3 registration at namespace load (as.timeDate.*/timeCeiling.*/skewness.*/kurtosis.*) is ALL on generics OF timeDate ITSELF
- TRAP #2 (S4 -> to_mcp): holiday/holidayNYSE returns an S4 'timeDate' and to_mcp STUBS IT OUT (`@mcp_serialized`=FALSE) => THE DATES WOULD BE LOST. EVERY timeDate is converted HERE into character 'YYYY-MM-DD' before being returned (pinned in the tests: no S4 leaks)
- DETERMINISM (§5): 'year' is MANDATORY — the timeDate default is getRmetricsOptions('currentYear') = THE CURRENT YEAR FROM THE CLOCK => not reproducible. TIMEZONE: FinCenter PINNED to 'GMT' (live-verified: THE SAME dates under TZ=Pacific/Auckland AND TZ=America/Los_Angeles); zone/FinCenter are NOT exposed. No randomness (purely calendrical computations); the output is ALWAYS sorted (sort+unique) and the column order = the GIVEN argument order; identical over 2 runs is pinned in the tests
- SILENTLY WRONG (years): outside [1000, 9999] timeDate does NOT error — it returns NA with ONLY the warning «character string is not in a standard unambiguous format» (year 0 -> NA, 10000 -> NA); the same for a NON-INTEGER year (2024.5 -> NA) and NA. OUR OWN HARD gate is [1583, 2200]: the lower bound = the 1st FULL year of the GREGORIAN calendar (the reform of 1582-10-15), because the timeDate Easter algorithm is GREGORIAN => before 1583 the results are ANACHRONISTIC
- SILENTLY WRONG (dates): timeDate('not-a-date') -> NA with only a warning; timeDate('2024-02-30') -> NA => any invalid date would SILENTLY become a row of ALL ZEROS. A hard gate: Date or STRICTLY 'YYYY-MM-DD', UNIQUE (the alignment index must be unique), NOT POSIXt (the POSIXt->Date conversion depends on the TIME ZONE and would shift days)
- SILENTLY WRONG (wday): isWeekday(x, wday = 99) does NOT error — it returns ALL FALSE («no day is a business day») => silently wrong bizday flags. A hard gate wday ∈ [0, 6] (0 = Sunday.. 6 = Saturday; the default 1:5 = Mon-Fri)
- §3b GATE 6 (fit/apply externalization): holiday_dates (a named list) + dummy_levels (the column NAMES AND ORDER) are returned as plain character/numeric fields AND accepted back (hd_dummies(holiday_dates=)) => an out-of-sample apply with IDENTICAL columns, INDEPENDENTLY of the timeDate version (the help page states explicitly that the catalogue «is changed from time to time»). The two paths are MUTUALLY EXCLUSIVE — otherwise the train/test columns could differ silently
- THE ZERO COLUMNS ARE NOT DROPPED: a holiday that does not fall inside the sample gives an all-zero column; SILENTLY removing it would BREAK the fit/apply (different train vs test columns). ALL of them are returned and the problem is flagged in constant_columns (a rank-deficient design; lm returns SILENTLY an NA coefficient — the same pattern as #253)
- SILENT GAPS THAT ARE NOT ERRORS: a holiday that DID NOT YET EXIST returns 0 dates WITHOUT an error (live: USJuneteenthNationalIndependenceDay before 2021 · CAFamilyDay in 2000 · JPMountainDay/GBEarlyMayBankHoliday in old years · specialHolidayGB in 2024) => the fields empty_sources/n_empty_sources; an EMPTY holiday set => isBizday DEGENERATES into isWeekday (live, without an error) => the fields empty_holiday_set/n_holiday_dates
- listHolidays: it applies the regex ANYWHERE inside the name, NOT as a prefix — which is why 'GB' gives 4 while the names that BEGIN with GB are 3 (the 4th is 'specialHolidayGB'); live-verified. An invalid regex -> a labelled stop («invalid regular expression '[', reason 'Missing ]''»)
- holidayNYSE(type=''): the DOCUMENTED default '' CANNOT be passed EXPLICITLY — the match.arg inside holidayNYSE errors («'arg' should be one of “standard”, “special”») => for nyse_type='all' we OMIT the argument entirely; also nyse_type applies ONLY with calendar='NYSE' (otherwise a hard stop rather than a silent no-op)
- holiday(names=TRUE) WAS OMITTED: the names are produced via substitute/all.names on the UNQUOTED argument; with function objects the help page says that «as a last resort.. generated names are used» (H1, H2,..) AND it PRINTS with cat (live-verified in the body; a violation of §5) => we call ONE holiday at a time and build the holiday->dates mapping OURSELVES
- THE INTERNAL PREFIX.hdum_ (NOT.hd_):.hd_call ALREADY EXISTS in c07_causality_policy/honest_robust_inference and ALL the wrappers are loaded into THE SAME source env => it would be a SILENT overwrite; the EXPORTED hd_* names were checked and are free

### References

- timeDate 4052.112 ref manual (live-verified the engine): the holiday routine «holiday(year = getRmetricsOptions('currentYear'), Holiday = 'Easter',.., names = FALSE)» + «Holiday: one or more names of holidays as a character vector OR a list of the UNQUOTED FUNCTION NAMES» + the cat fallback for generated names; the listHolidays routine (pattern = '.*'; «the list is changed from time to time»); the holidayNYSE routine (type = c('', 'standard', 'special')); holidayLONDON/holidayZURICH/holidayTSX; the isWeekday routine / the isBizday routine (wday = 1:5); the timeDate routine (FinCenter)
- LIVE-VERIFIED catalogue counts (timeDate 4052.112, listHolidays('.*') = 120): US 18 · CA 6 · GB 4 (3 with the GB prefix + specialHolidayGB) · DE 5 · FR 6 · IT 6 · JP 33 · CH 5
- LIVE-VERIFIED conflicts(detail = TRUE) after library(timeDate): abline lines plot points getDataPart initialize Ops show sample; isGeneric('sample') -> TRUE (an S4 promotion); with requireNamespace: ZERO new entries
- The Gregorian reform: the papal bull «Inter gravissimas», in force from 1582-10-15 => 1583 = the 1st FULL Gregorian year; the timeDate Easter algorithm is Gregorian (the gate's lower bound)
- the normative gate spec §3b: the live-verified gate «holiday: object 'X' of mode 'function' was not found» + the masking table («timeDate: plot, lines, abline, points, initialize, getDataPart, … (10) — harmless (we never draw — §5) but document it in the footer; holiday resolves names via get ⇒ it requires an attach or getExportedValue») + normative gate 6 (fit/apply externalization; KNIME «Normalize Model»)
- docs/catalog/merge-wrapper.md — the catalog row «Calendar effects / holiday dummies (national holidays G7+CH + financial centers -> named 0/1 columns)», timeDate already installed (ZERO new dependency), with the same verified per-country counts
- wrapper footer IMPLEMENTATION NOTE (c00_data_utilities/calendar_effects_holidays) — traps #1/#2, the live-verified silent NA of timeDate, the TZ-invariance test, the silent gaps (empty_sources/constant_columns/empty_holiday_set) and the reasons for the omissions (names=TRUE, holidayNERC, Sys.timeDate, timeSequence/align, skewness/kurtosis, plots)

## #255 — DISCRETISATION (binning) of ONE numeric column: EQUAL-POPULATION bins (sample quantiles, quantile type 7 PINNED) or EQUAL-WIDTH bins (an explicit seq over the range or over a GIVEN fixed domain) + an out-of-sample APPLY of the STORED breaks

**Module:** `discretisation_numeric_column.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `bn_quantile_bins` | `x` | `matrix_handle`, `integer`, `num_array`, `series_codes`, `boolean`, `boolean`, `enum`, `boolean` | `right=True`, `dedupe_breaks=False`, `dummies=False` | `light` | — |
| `bn_equal_width` | `x` | `matrix_handle`, `integer`, `number`, `number`, `series_codes`, `boolean`, `enum`, `boolean` | `n_bins=4`, `right=True`, `dummies=False` | `light` | — |
| `bn_apply` | `x`, `breaks` | `matrix_handle`, `num_array`, `series_codes`, `boolean`, `boolean`, `enum`, `enum`, `boolean` | `right=True`, `include_lowest=True`, `dummies=False` | `light` | — |

### Use when

converting ONE continuous macro variable into DISCRETE REGIMES (regime dummies): «high vs low inflation», «growth quartile», «spread zone», or INTEGER CODES as the input to a categorical node; ONE node PER variable (fan-out from the frontend). BINNING IS FIT + APPLY: the fit LEARNS the boundaries from the sample, bn_apply REUSES them verbatim on a new sample

### Do not use when

NON-STATIONARY I(1) LEVELS with SAMPLE quantiles (the «quartiles» reflect the POSITION IN TIME, not an economic regime — supply DIFFERENCES/rates or use bn_equal_width with EXOGENOUS boundaries); ENDOGENOUS regime detection from the data themselves -> Markov-switching / threshold (cat 06) or #244 mclust (cat 29); STRUCTURAL CHANGE POINTS in time -> #3 strucchange (cat 01); MANY columns at once (one node per variable); NON-LINEARITY WITHOUT information loss -> #253 ply_poly (polynomials discard nothing, binning DOES); ALREADY categorical variables (no binning needed); charts/histograms (the frontend, §5)

### Prerequisites

- bn_quantile_bins # run it FIRST and look at n_distinct/counts/n_breaks_dropped: many TIES => the quantiles coincide and the node BLOCKS (by design)
- c00_data_utilities/replacement_missing_values.imputets_kalman # NA/Inf are a hard gate with na_action='fail' (the default); alternatively na_action='keep' PRESERVES the POSITION with an NA code
- c01_preparation_prechecks/unit_root_normality.run_adf_test # IF the column is a time series: non-stationarity => the SAMPLE quantiles do NOT converge (§3b gate 3)

### Alternatives

| instead use | when |
| --- | --- |
| bn_quantile_bins(n_bins = 4) [DEFAULT] | you want EQUAL-POPULATION bins (each regime has the same number of observations => the same statistical power per dummy): 3 = terciles, 4 = quartiles, 5 = quintiles, 10 = deciles |
| bn_quantile_bins(probs = c(0, 0.1, 0.9, 1)) | you want UNEQUAL bins with an economic meaning («lower tail / centre / upper tail»); it MUST be strictly increasing with the endpoints EXACTLY 0 and 1; it does NOT combine with n_bins |
| bn_equal_width(n_bins) | you want EQUAL-WIDTH bins (interpretable value ranges instead of equal population); under a skewed distribution the extreme bins may end up EMPTY — they are reported explicitly in empty_bins |
| bn_equal_width(range_min, range_max) | you want COMPARABLE bins across COUNTRIES/SAMPLES or on a NON-STATIONARY series: you supply THEORETICAL, EXOGENOUS boundaries (e.g. around a 2% inflation target) instead of sample ones — THE CORRECT ROUTE when §3b gate 3 forbids sample quantiles |
| bn_apply(breaks = <breaks of a previous fit>) [§3b gate 6] | NEW data (test/out-of-sample/another country): THE SAME boundaries => COMPARABLE regime dummies; a re-fit gives DIFFERENT boundaries and the out-of-sample result is NOT reproduced. Supply the fit's labels/right/include_lowest as well |
| out_of_range = 'na' or 'clamp' (bn_apply) | 'na' = an EXPLICIT NA code + a record (n_out_of_range/out_of_range_labels) when you want to KNOW which new values fell outside; 'clamp' = assignment to the EXTREME bin, when the regimes are defined as «below/above X» — but it DISTORTS the extreme-value information. The default is 'fail' (blocked-by-gate) |
| dedupe_breaks = TRUE (bn_quantile_bins) | EXPLICIT consent when the column has many TIES and two quantiles coincide: the UNIQUE boundaries are kept, the bins become FEWER than requested (n_breaks_dropped) and they no longer have equal population; the default FALSE = a hard stop |
| dummies = TRUE | you want the 0/1 indicator matrix (n x n_bins) DIRECTLY as regressors; the missing/out-of-range rows get NA (NOT 0 — a 0 would mean «definitely not in this bin») |
| #253 ply_poly | you want NON-LINEARITY WITHOUT information loss — binning discards the WITHIN-BIN variance, polynomials do not |

### Output fields

- bin (INTEGER codes 1.n_bins per observation, named) + bin_label (character per observation) + labels (the bin NAMES) — NEVER a factor (JSON-safe)
- breaks (NUMERIC, n_bins+1 boundaries) = THE FITTED PARAM (§3b gate 6); it is handed back verbatim to bn_apply together with labels/right/include_lowest
- counts + share (histogram chart-data) + bin_lower/bin_upper/bin_width (THE BOUNDARIES) + bin_min/bin_max/bin_mean/bin_median (the OBSERVED range INSIDE each bin) + empty_bins/n_empty_bins
- dummies (n x n_bins 0/1 or NULL; NA on the unassignable rows) + method ('quantile'\|'equal_width'\|'apply') + right/include_lowest
- out_of_range + n_out_of_range/out_of_range_index/out_of_range_labels + n_clamped + n_assigned + n/n_valid/n_missing/missing_index/n_distinct + column/observations
- bn_quantile_bins ADDITIONALLY: probs + quantile_type (ALWAYS 7 — so that two fits are comparable ONLY if they come from the SAME estimator) + n_bins_requested + n_breaks_dropped + dedupe_breaks + data_min/data_max
- bn_equal_width ADDITIONALLY: width + range_min/range_max + range_supplied (WHETHER the boundaries are EXOGENOUS or sample-based) + data_min/data_max

### Pitfalls

- §3b GATE 6 (fit/apply externalization) — WHY THERE ARE THREE FUNCTIONS: the fit LEARNS the breaks from the sample; a re-fit on new data gives DIFFERENT boundaries => the regime dummies are NOT comparable and the out-of-sample result is «reproducible ONLY BY LUCK». That is why the breaks are returned AS A NUMERIC FIELD and bn_apply accepts them BACK (the KNIME «Auto-Binner» -> PMML model / Normalizer -> «Normalize Model» pattern)
- §3b GATE 3 (NON-STATIONARITY, Hamilton-Ma-Xi NBER WP 32068): on an I(1) series the SAMPLE quantiles do NOT converge to a population parameter => the «quartiles» reflect the POSITION IN TIME (the early period = a low bin) and NOT an economic regime. A documented PRECONDITION: discretise DIFFERENCES/rates, or use bn_equal_width with THEORETICAL exogenous boundaries. NEVER a silent correction here (§3b gate 2: no hidden conversion)
- DETERMINISM #1 (§5): THE QUANTILE TYPE IS PINNED TO 7 (the reference/S default) and is NOT exposed as an argument: the NINE types of Hyndman & Fan (1996) give DIFFERENT breaks on the SAME data, so a switchable 'type' would break the reproducibility of STORED workflows («stored workflows pin node versions», §5). The type is ALWAYS returned in quantile_type
- DETERMINISM #2: the equal-width boundaries are computed with an EXPLICIT seq(from, to, length.out = n_bins+1) — NEVER with cut(x, breaks = <A NUMBER>), which SILENTLY MOVES the outer limits by 0.1% of the range (documented) AND does NOT return the boundaries it used => a non-externalizable fit (it would break gate 6). No RNG/sampling/parallelism; identical over 2 runs is pinned in the tests (the wrapper AND the node)
- NOTE: `cut` lives in **base**, NOT in stats (`quantile` lives in stats) — all the calls are fully qualified base::/stats
- SILENTLY WRONG (cut a): VALUES OUTSIDE the breaks -> SILENTLY NA («Values which fall outside the range of breaks are coded as NA»); in an out-of-sample apply this means LOST OBSERVATIONS WITHOUT ANY INDICATION => an explicit out_of_range policy with the default 'fail'
- SILENTLY WRONG (cut b): UNSORTED breaks are sorted SILENTLY («The default method will sort a numeric vector of breaks») AND the labels are matched AFTER the sorting => the REGIME NAMES land on the WRONG BINS. A hard gate: STRICTLY INCREASING breaks
- SILENTLY WRONG (cut c-f): an NA INSIDE the breaks is ignored SILENTLY (cut(1:10, c(0,NA,10)) -> ONE bin instead of two); DUPLICATE labels are MERGED SILENTLY into ONE level (cut(1:10, c(0,5,10), labels=c('a','a')) -> ONE 'a' for ALL the values); breaks given as a factor -> the LEVEL CODES are used SILENTLY; include.lowest=FALSE -> the MINIMUM value becomes SILENTLY NA; an Inf in the data -> SILENTLY an NA bin. ALL are hard gates
- SILENTLY WRONG (number of bins): n_bins = 1 is not a discretisation — cut with 2 breaks returns ONE level WITHOUT an error => a gate n_bins >= 2 AND STRICTLY < the number of UNIQUE values (otherwise the boundaries coincide)
- TIES (the most frequent real cause of failure): on a column with many repetitions the quantiles COINCIDE and cut throws «'breaks' are not unique». The node catches it BEFORE the call, with the column's NAME and the number of duplicates; the ways out: lower n_bins OR an explicit dedupe_breaks=TRUE (then FEWER bins, NOT of equal population). In bn_apply duplicates are ALWAYS A HARD STOP — deduping there would change the number of bins relative to the fit
- NA POLICY: na_action='fail' (the default) \| 'keep' — NOT 'omit'. The regime dummies MUST stay ALIGNED with the series/the panel; removing rows would break the alignment with y (exactly the error model_frame makes silently, see #253). With 'keep' the missing POSITIONS are preserved with an NA code and recorded in n_missing/missing_index
- right/include_lowest MUST be THE SAME in the apply as in the fit (the fits here are ALWAYS include_lowest=TRUE), otherwise the BOUNDARY observations change bin; out_of_range='clamp' REQUIRES include_lowest=TRUE (otherwise the value «clamped» onto the extreme boundary would become NA AGAIN)
- THE OUTPUT IS NEVER a factor: we keep the factor INTERNALLY and DECOMPOSE it into INTEGER codes + character labels (JSON-safe, §5); the ORDERING lives in the order of 'labels' (which is why ordered_result is omitted); dig.lab is PINNED to 3 (the reference default) with a post-check of UNIQUENESS/level count — cut itself raises the digits up to 12 and falls back to 'Range_k' labels when the boundaries differ at the 14th digit (live-verified)
- MASKING: ZERO — no library (only base/stats, ALWAYS attached); the live conflicts(detail=TRUE) is IDENTICAL before/after the source. CONVERSELY, because OTHER wrappers in the shared source env mask core generics (proxy -> dist/as_matrix; sn -> sd; ARIMA -> ARIMA), ALL the calls here are base::/stats:: qualified
- A TERMINAL node (no register/chaining): it returns chart-ready numbers (codes/labels per observation, breaks, per-bin counts/share/boundaries/observed min-max-mean-median, an optional 0/1 matrix). The fit/apply is EXPLICIT: the user hands the breaks back

### References

- the cut routine's documentation / cut_default (live-verified): «cut(x, breaks, labels = NULL, include.lowest = FALSE, right = TRUE, dig.lab = 3, ordered_result = FALSE,..)»; «Values which fall outside the range of breaks are coded as NA»; «The default method will sort a numeric vector of breaks»; «'breaks' are not unique»; «number of intervals and length of 'labels' differ»; «when breaks is a single number the outer limits are moved away by 0.1% of the range»; ⚠️ cut lives in base, NOT in stats
- the quantile routine's documentation / quantile_default (live-verified default type = 7): «quantile(x, probs = seq(0,1,0.25), na.rm = FALSE, names = TRUE, type = 7, digits = 7, fuzz =..)»; «missing values and NaN's not allowed if 'na.rm' is FALSE»; the endpoints coincide with min/max for EVERY type
- Hyndman, R.J. & Fan, Y. (1996) «Sample Quantiles in Statistical Packages», The American Statistician 50(4) 361-365 — the nine types of sample quantiles; type 7 (p_k = (k-1)/(n-1)) is the reference/S default. THE PINNING IS A §5 REQUIREMENT (reproducibility of stored workflows)
- Hamilton, J.D., Ma, X. & Xi, J., «Principal Component Analysis for a Mix of Stationary and Nonstationary Variables», NBER WP 32068 — §3b normative gate 3: on a non-stationary series the SAMPLE moments/quantiles do not converge to a population parameter (see #256, the correct route for mixed I(0)/I(1) panels)
- the normative gate spec §3b normative gate 6 (fit/apply externalization — explicitly «breaks»; the KNIME Normalizer -> «Normalize Model» pattern; KNIME Auto-Binner -> a PMML model) + gate 2 (no implicit conversion) + the live-verified gate «cut: 'breaks' are not unique on a constant/dense column ⇒ dedupe or stop (⚠️ cut is in base, NOT stats)»
- docs/catalog/merge-wrapper.md — the catalog row «Binning / discretization (equal-width or quantile; terciles/quartiles for regime dummies)», stats+base, ZERO new dependency, «returning the breaks (fit/apply)», «type=7 = the reference/S/Excel default»
- wrapper footer IMPLEMENTATION NOTE (c00_data_utilities/discretisation_numeric_column) — the 8 live-verified silently-wrong behaviours of cut (a through h), the reasons for the omissions (quantile type/na.rm/names/digits/fuzz; cut breaks=<a number>/ordered_result/dig.lab/labels=FALSE; hist/.bincode/findInterval), the ZERO masking (live conflicts) and the post-checks of.bn_build
