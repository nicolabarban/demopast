# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DEMOPAST (demopast.it) is an Italian historical demographic atlas, part of the GENPOP project. It displays interactive choropleth maps of Italian provinces with census data for 1861, 1871, 1881, 1901, 1911, 1921, 1931, 1936, 1951, 1961, and 1971.

## Tech Stack

- **Quarto** static website deployed to GitHub Pages via GitHub Actions
- **Leaflet.js** for choropleth maps (loaded from CDN)
- **Chart.js** for population pyramids (loaded from CDN)
- **PapaParse** for CSV loading in the browser

All rendering/logic is client-side JavaScript embedded in `.qmd` files — there is no backend.

## Build & Preview

```bash
quarto render          # Build site to _site/
quarto preview         # Local dev server with hot reload
```

`_quarto.yml` declares `data/**` and `downloads/**` as `resources`, so they must be listed there for Quarto to copy them into `_site/`. Anything added outside those trees will not be served.

## Data Processing (Python, offline only — not needed at runtime)

```bash
pip install geopandas pandas   # Dependencies for scripts/
python3 scripts/build_census.py    # downloads/*/data_census_*_adjusted_age.csv -> data/census/census_{year}.csv
python3 scripts/build_geojson.py   # raw/shapefiles/*                            -> data/geojson/province_{year}.geojson
```

- `scripts/build_census.py` reads the long-format adjusted-age CSVs **directly from `downloads/`** (`downloads/{year}/data_census_{year}_adjusted_age.csv`, columns `code, province, age_class, male, female, total`) and pivots them into the wide per-province schema the site consumes, recomputing `cwr` / `old_dep` / `struct_dep` / `mean_age`. The same files are what users download from the site, so `downloads/` is both the public artifact and the build input — there is no longer a separate `raw/census/` source. `DEN_PROV` is preserved from any pre-existing `data/census/census_{year}.csv` (join on `COD_PROV`) since province names in the long-format source are modern (e.g. "Imperia") while GeoJSONs use historical names (e.g. "Porto Maurizio").
- `scripts/build_geojson.py` reprojects shapefiles to WGS84 and simplifies with `tolerance=0.005` degrees (~500 m). Shapefiles must expose `COD_PROV` (int) and `DEN_PROV` (str) attributes. Shapefile sources live under `raw/shapefiles/` (gitignored) and are only needed when regenerating a GeoJSON.
- The 1881 adjusted-age source is missing `COD_PROV=92` (Cagliari); that province renders uncoloured with "N/A" in the panel — expected given the source gap. (Cagliari is present in 1861 and 1871.)
- The 1961 census covers all 92 provinces. Six of them (Latina 59, Cosenza 78, Catanzaro 79, Reggio di Calabria 80, Messina 83, Agrigento 84) were missing from the digitised source and were reconstructed from the printed Tav. 4 (Vol. III) province rows, redistributing the original age classes (0-6/6-14/14-21/…/75+) into the standard 19 groups using the age profile of clean neighbouring provinces as weights; each transcription matches the printed row totals and the official ISTAT provincial population to the unit (see `data/quality/audit_1951_1961.md`). It also contains 161 rows (mostly ages 70+) where `male+female != total` — digitisation errors in the source, kept as-is and flagged by `scripts/check_plausibility.py`. Province names in `downloads/1961/` come from the ISTAT shapefile DBF (decoded cp850 despite the .CPG claiming ANSI 1252; "Forlì" fixed via `DEN_PROV_FIXES` in `build_geojson.py`).
- The 1971 census covers 94 provinces — the 92 of 1961 plus Pordenone (93, split off Udine in 1968) and Isernia (94, split off Campobasso in 1970). `check_plausibility.py` flags the resulting drops in Udine and Campobasso; they are real boundary changes, not data errors. The source was digitised in-house from the printed Tav. 3 province rows (one PDF per province), which tabulate only 16 five-year classes: `<5`, `5-9`, …, `70-74`, `75+`. Transcriptions live in `work_in_progress/1971/trascrizioni_1971.json` and are assembled into the 19-group schema by `work_in_progress/1971/assembla_1971.py`, which splits the two open classes (`<5` → `0`/`1-4`, `75+` → `75-79`/`80-84`/`85+`) using the same province's 1961 proportions with largest-remainder rounding, so column totals stay exact. **The `0`, `1-4`, `75-79`, `80-84` and `85+` values for 1971 are therefore estimates, not printed figures** — every other class is transcribed. Borrowing the 1961 ratio imports 1961's rising-birth regime into a falling-birth decade, so `t_0` for 1971 is biased high by roughly 7% (~64k nationally) at the expense of `1-4`, and `85plus` is probably slightly low; the published indices are unaffected because `cwr`/`old_dep`/`struct_dep` consume the printed `0-4` and `75+` aggregates, and `mean_age` moves by ~0.003 years. Only the two youngest pyramid bars carry the bias. Recalibrating the age-0 split on provincial 1966-71 births would remove it. Pordenone and Isernia, absent in 1961, borrow the split proportions of their parent province (Udine 30, Campobasso 70). Each province was verified against its printed row total and the ISTAT reference `work_in_progress/1971/ref_1971.json` to the unit; the 94 provinces sum to 54,136,547, the official national count. Three provinces are only reconcilable against the reference in groups because of 1961→1971 boundary changes: Como+Bergamo as a pair, and Sassari+Nuoro+Cagliari as a triple.
- The 1871 sources contain a duplicate `COD_PROV=79` with two distinct `DEN_PROV` values ("Calabria Ulteriore II" and "Catanzaro"), reflecting a historical naming transition. Both shapefile and CSV preserve the duplicate; downstream code that joins on `COD_PROV` alone may pick either row.
- 1861 has 59 provinces (no Veneto, Lazio, Trentino, Friuli orientale); 1871 has 70 (Veneto and Lazio annexed). Historical province names like "Umbria", "Principato Ulteriore/Citeriore", "Terra del Lavoro", "Capitanata", "Terra di Bari", "Terra d'Otranto", "Calabria Citeriore/Ulteriore I/II", "Noto" appear only in these two years.

## File Structure

- `index.qmd` — Atlas page: map (1/3) + info panel (2/3) with indices, pyramid, age table
- `compare.qmd` — Side-by-side province comparison
- `series.qmd` — Time-series chart. Loads all census CSVs at init, lets the user pick a geographic level (Italy / Macro-area / Region / Provinces, multi-select) and an indicator, and plots a Chart.js line per selection across 1861/1871/1881/1901/1911/1921/1931/1936/1951/1961/1971. Province→region→macro-area is mapped in a `REGION_MAP` object inside `series.qmd` keyed by `COD_PROV`; if you add new provinces or split a region, update that object. Ratio indicators (CWR / dependencies / mean age) are recomputed from aggregated counts the same way as `showNationalData` in `index.qmd`.
- `about.qmd` — Project info, team
- `_quarto.yml` — site config; output to `_site/`
- `scripts/build_census.py`, `scripts/build_geojson.py` — offline data pipeline (see above)
- `data/geojson/province_{year}.geojson` — Province boundaries (WGS84) for 1861/1871/1881/1901/1911/1921/1931/1936/1951/1961/1971. Source shapefiles: ISTAT "Confini statistico-amministrativi: analisi storica" (https://www.istat.it/storage/cartografia/confini-amministrativi-storici/Limiti_{year}.zip).
- `data/census/census_{year}.csv` — Aggregated data: 19 age groups × M/F/T + 4 demographic indices. Rebuilt from `downloads/{year}/data_census_{year}_adjusted_age.csv` by `scripts/build_census.py`.
- `downloads/{year}/data_census_{year}_adjusted_age.csv` — Long-format adjusted-age source CSVs for 1861/1871/1881/1901/1911/1921/1931/1936/1951/1961/1971. These are both the public download (linked from the atlas page per year) and the input to `scripts/build_census.py`. The previous per-province `{COD_PROV:03d}_{DEN_PROV}_{year}.csv` files have been retired. The 1931 file was originally in Mac Roman encoding — `build_census.py` expects UTF-8, so re-converting any future updated source (e.g. `iconv -f MAC -t UTF-8`) is required before running the build.
- `raw/shapefiles/` — Shapefile sources for `build_geojson.py` (gitignored, optional — only needed to regenerate GeoJSONs).

## Key Conventions

- `COD_PROV` (integer) is the join key between GeoJSON features and census CSV rows.
- Age-group columns use prefix `m_`, `f_`, `t_` + suffix like `0`, `1_4`, `5_9`, ..., `85plus` (19 groups total).
- Demographic indices columns: `cwr` (child/woman ratio, ‰), `old_dep` (%), `struct_dep` (%), `mean_age` (years).
- National-level aggregates shown on initial load are computed **client-side** by summing per-province rows and recomputing ratios (see `showNationalData` in `index.qmd`). If you change index formulas in Python, mirror them here.
- Chart.js is loaded via `include-in-header` in the YAML frontmatter. Loading it in the HTML body does not work — Quarto strips inline `<script>` tags from body content.
- `index.qmd` intentionally disables map interaction (drag, zoom, scroll-wheel) — it is a static choropleth, not a pan/zoom map. Don't re-enable without reason.
- The atlas year set is the JS array `YEARS` near the top of `index.qmd` and the `<option>` list in `compare.qmd`. Both must be kept in sync, and a matching `data/census/census_{year}.csv` + `data/geojson/province_{year}.geojson` + `downloads/{year}/data_census_{year}_adjusted_age.csv` triple is required for any year listed.
- The "Download province data" link is per-year, not per-province: it points at the consolidated `downloads/{year}/data_census_{year}_adjusted_age.csv` for whichever year the slider is on. It is hidden in the national (initial) view by `showNationalData`.

## Deploy

Push to `main` triggers `.github/workflows/publish.yml`, which runs `quarto render` and publishes `_site/` to GitHub Pages. The GitHub Pages source must be set to "GitHub Actions" in repo settings. The custom domain `demopast.it` is configured via `CNAME`.
