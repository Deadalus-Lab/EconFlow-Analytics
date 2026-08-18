<!-- SPDX-License-Identifier: AGPL-3.0-only -->
# 11-decomposition-accounting

3 METHOD-SELECTION cards, 3 modules, 7 nodes.

Every card below governs one wrapper module in this package. The cards are the
reason a method exists here at all: they record when it applies, what to reach
for instead, and the traps that make its output easy to misread.

## #62 — productivity (TFP / Malmquist / DEA)

**Module:** `productivity.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `prod_malmquist` | `data`, `id_var`, `time_var`, `x_vars`, `y_vars` | `df_handle`, `string`, `string`, `series_codes`, `series_codes`, `enum`, `enum`, `boolean`, `boolean` | `tech_reg=True`, `scaled=True` | `light` | — |
| `prod_fareprim` | `data`, `id_var`, `time_var`, `x_vars`, `y_vars` | `df_handle`, `string`, `string`, `series_codes`, `series_codes`, `series_codes`, `series_codes`, `boolean`, `boolean`, `enum`, `enum`, `boolean`, `boolean` | `tech_change=True`, `tech_reg=True`, `scaled=True`, `shadow=False` | `light` | — |

### Use when

a balanced DMU×period panel with inputs (K,L,materials) & outputs (GDP); non-parametric TFP: malm=change, fareprim=levels (multilateral transitive)

### Do not use when

a single time series for one DMU; an unbalanced panel; parametric/SFA with noise; decomposition of forecast variance (→ FEVD, cat. 04)

### Alternatives

| instead use | when |
| --- | --- |
| prod_fareprim (transitive levels) | you want comparable TFP LEVELS across many DMU/years at once (multilateral); the only transitive+complete index (O'Donnell 2012) |
| prod_malmquist (change) | you want the CHANGE in TFP between adjacent periods (Solow-style, quantity-only, effch×tech) |
| SFA (stochastic frontier) | you want to separate inefficiency from random noise (DEA attributes everything to inefficiency) and you accept a functional form |
| hicksmoorsteen/lowe/fisher/laspeyres/paasche | excluded (charter §4): non-transitive or price-based, redundant next to malm+fareprim |

### Output fields

- Changes.malmquist: the TFP change index; >1=improvement, <1=deterioration (the same under both orientations)
- Changes.effch: efficiency change (catching up to the frontier); malmquist=effch×tech
- Changes.tech: technological change (a shift of the frontier); obtech/ibtech/matech are its components
- Levels$TFP (fareprim): the TFP level, transitive → directly comparable cross-DMU/period
- Levels$TFPE=TFP/MP ∈(0,1]; OTE/OSE/OME: technical/scale/mix efficiency (out-oriented)
- Levels$REV/COST/PROF: profitability, ONLY with prices (w.vars/p.vars)
- Changes (fareprim): changes prefixed with 'd' (dTFP,dOTE,dPROF); Shadowp only with shadow=TRUE

### Pitfalls

- efficiency scores ∈(0,1]; a value=1 = best-in-sample frontier, NOT absolutely perfect (DEA is relative/deterministic)
- zero/negative inputs/outputs → SILENT garbage (a zero output → malmquist ~1e30); the gate requires strictly >0
- a factor time.var → DEA sorts by the order of the LEVELS, not chronologically → a SILENTLY sign-flipped TFP change
- the accessors Levels/Changes/Shadowp are BROKEN on a modern the reference (is with a length-1 class2); read $Levels/$Changes directly
- DEA has no noise term: outliers/measurement error shift the frontier & distort every score
- an unbalanced panel → the package does not work; malm needs >=2 periods, fareprim >=1

### References

- productivity (help malm/fareprim, live-verified 1.1.0)
- Färe & Grosskopf 1996 Intertemporal Production Frontiers (Malmquist decomposition)
- O'Donnell 2011/2012 AJAE 94(4):873-890 (Färe-Primont transitivity & complete decomposition)
- Caves-Christensen-Diewert 1982 (Malmquist index)

## #63 — oaxaca (Blinder-Oaxaca decomposition)

**Module:** `oaxaca.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `ox_decompose` | `formula`, `data` | `formula`, `df_handle`, `integer`, `integer` | `n_bootstrap=100`, `seed=42` | `light` | — |

### Use when

cross-section; decomposing the MEAN gap of a continuous outcome between TWO groups (0/1) into explained/endowments vs unexplained/coefficients (+interaction, three-fold)

### Do not use when

>2 groups; a causal claim (unexplained ≠ discrimination); a non-linear/binary outcome; a time-series/panel gap

### Alternatives

| instead use | when |
| --- | --- |
| three-fold decomposition | you want an explicit interaction term + a complete accounting split with no reference choice (Jann 2008) |
| two-fold (reference-coefficient scheme) | you want 'how much of the gap closes if we equalised X'; choose group_weight (pooled or A/B) |
| quantile / RIF decomposition (Firpo-Fortin-Lemieux) | the gap varies across the DISTRIBUTION (glass ceiling/sticky floor), not only at the mean |
| non-linear Oaxaca (Fairlie/Yun) | a binary/count outcome; outside the wrapper (reg.fun is locked to lm) |

### Output fields

- twofold: overall per reference weight (group_weight); coef_explained/se_explained (endowments), coef_unexplained/se_unexplained (+_A/_B)
- twofold_variables: the decomposition per regressor (column variable)
- threefold: coef_endowments, coef_coefficients, coef_interaction (+SEs)
- threefold_variables: three-fold per regressor
- x_means: mean_A/mean_B/mean_diff per regressor (the raw material of the endowments effect)
- y: y_A/y_B/y_diff — mean outcomes & the total gap (= the sum of the components)
- n: n_A/n_B/n_pooled; n_dropped: silent NA-drop reporting

### Pitfalls

- an invalid group/the reference/formula → oaxaca emits a message AND returns NULL (not stop; tryCatch does not catch it); pre-gate + post-gate result!=NULL
- degenerate fit: a per-group lm that is rank-deficient/df_residual<=0 → non-NULL with NA/misleading coefficients and NO error; post-gate per .reg
- 'unexplained' ≠ discrimination: it absorbs omitted variables & functional-form error (Jann 2008); NOT causal
- sign: y_diff=y_A−y_B (group=0 → A); check which group is 0/1 before interpreting; the components sum to y_diff
- the two-fold split depends on the reference group_weight; a different weight → a different explained/unexplained split
- the bootstrap SE are stochastic → set.seed before the call (the same seed → an identical two-fold split)
- silent NA-drop: rows with NA are ignored silently → report n_dropped

### References

- oaxaca (help oaxaca, live-verified 0.1.5)
- Blinder 1973 J. Human Resources; Oaxaca 1973 Int. Economic Review (the original decompositions)
- Jann 2008 Stata Journal 8(4):453-479 (two-fold reference schemes, three-fold, unexplained≠discrimination)

## #190 — Price index numbers (bilateral/multilateral/spliced) + CPI-subindex contribution decompositions

**Module:** `price_index_numbers.py` · **Reference:** not yet selected; see engine/METHOD-SOURCES.json

### Nodes

| fn | required args | kinds | defaults | memory | register.field |
| --- | --- | --- | --- | --- | --- |
| `pi_bilateral` | `data`, `start`, `end` | `df_handle`, `string`, `string`, `enum`, `boolean` | `interval=False` | `light` | — |
| `pi_multilateral` | `data`, `start`, `end` | `df_handle`, `string`, `string`, `enum`, `integer`, `string` | `window=13` | `light` | — |
| `pi_splice` | `data`, `start`, `end` | `df_handle`, `string`, `string`, `enum`, `integer`, `enum`, `boolean` | `window=13`, `interval=False` | `light` | — |
| `pi_contributions` | `data`, `start`, `end` | `df_handle`, `string`, `string`, `enum`, `boolean`, `boolean`, `integer` | `matched=False`, `interval=False`, `prec=2` | `light` | — |

### Use when

long-format scanner/CPI micro data (time,prices,quantities,prodID); you want a price index (bilateral or multilateral) or a decomposition of the change in the value of a CPI subindex into price/quantity contributions per product

### Do not use when

you already have a finished index-level series (an index level ts) — that is a transform/growth-rate task, not index-number construction; a macro aggregate without product-level micro data; a need for SPQ/model-based or chained bilateral batch indices (outside the curated surface)

### Prerequisites

- pi_bilateral (the bilateral baseline; check the Laspeyres vs Paasche drift before choosing multilateral)
- pi_multilateral (GEKS/CCDI/GK/TPD; a transitive base for splicing)
- c00_data_utilities/reading_delimited_fixed.read_delimited (loading the long-format CSV micro data)

### Alternatives

| instead use | when |
| --- | --- |
| pi_multilateral (GEKS/CCDI/GK/TPD) | high product turnover / new-goods bias — the bilateral indices (Laspeyres/Paasche) suffer chain drift; you want a transitive multilateral index |
| pi_splice | you want a non-revisable extending multilateral series beyond a fixed window (a rolling-window splice) |
| #62 prod_fareprim (productivity) | you want a TFP/quantity index (Färe-Primont) rather than a price index |

### Output fields

- pi_bilateral: index (a scalar, or a vector if interval=TRUE); formula; dates (month labels when interval is used)
- pi_multilateral: index (a scalar, end vs start over the window); method; window; wstart
- pi_splice: index (a scalar, or the full series if interval=TRUE); method; splice; dates
- pi_contributions.aggregate: 1 row {Value_difference, Price_indicator, Quantity_indicator} (the identity: value = price + quantity)
- pi_contributions.contributions: a per-product data_frame {prodID, value_differences, price_contributions, quantity_contributions}; n_products

### Pitfalls

- start > end: PriceIndices SILENTLY returns a wrong (inverted) index — the wrapper blocks it (gate); always keep start <= end
- bilateral Laspeyres/Paasche over/understate because of substitution bias; Fisher/Törnqvist (superlative) is the correct baseline; a large Laspeyres–Paasche gap => move to multilateral
- gk = Geary-Khamis rolling window (the default here); it differs from geary_khamis (fixed base, not exposed); do not confuse them
- window (multilateral/splice): an integer >= 2 months; too small a window => noise, too large => the composition becomes out of date
- pi_contributions: the price_contributions of a product can be 0 when its price did not change — the quantity is a contribution to the value DIFFERENCE (an indicator, not an index ratio)
- interval=FALSE => a single index, end vs start (base=start=1); interval=TRUE => a series with dates for a chart

### References

- ILO/IMF/OECD/Eurostat/UNECE/World Bank (2004, 2020) Consumer Price Index Manual: Theory and Practice
- Diewert (1976) Exact and superlative index numbers, J. Econometrics 4:115
- Bennet (1920) The theory of measurement of changes in cost of living, JRSS 83:455; Montgomery (1937)
- Krsinich (2016) The FEWS index: Fixed Effects with a Window Splice (UNECE-ILO); de Haan & Krsinich (2014) multilateral GEKS
