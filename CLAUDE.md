# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DEMOPAST (demopast.it) is an Italian historical demographic atlas, part of the GENPOP project. It displays interactive choropleth maps of Italian provinces with census data for 1881, 1911, 1921, and 1931.

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
python3 scripts/build_census.py    # raw/census/*.csv   -> data/census/census_{year}.csv
python3 scripts/build_geojson.py   # raw/shapefiles/*  -> data/geojson/province_{year}.geojson
```

- `scripts/build_census.py` pivots long-format adjusted-age CSVs (`raw/census/{year}/data_census_{year}_adjusted_age.csv`, columns `code, province, age_class, male, female, total`) into the wide per-province schema the site consumes, and recomputes `cwr` / `old_dep` / `struct_dep` / `mean_age`. It preserves `DEN_PROV` from any pre-existing `data/census/census_{year}.csv` (join on `COD_PROV`) so `downloads/{year}/` filenames keep resolving — province names in the raw source are modern (e.g. "Imperia") while existing download files and GeoJSONs use historical names (e.g. "Porto Maurizio").
- `scripts/build_geojson.py` reprojects shapefiles to WGS84 and simplifies with `tolerance=0.005` degrees (~500 m). Shapefiles must expose `COD_PROV` (int) and `DEN_PROV` (str) attributes.
- Raw source data lives under `raw/` (gitignored):
  - `raw/census/{year}/data_census_{year}_adjusted_age.csv` for 1881, 1901, 1911, 1921
  - `raw/shapefiles/Province_{year}/` for 1901 (other years' GeoJSONs are already committed under `data/geojson/`)
- The 1881 adjusted-age source is missing `COD_PROV=92` (Cagliari); that province renders uncoloured with "N/A" in the panel — expected given the source gap. 1911 code 29 (Rovigo), previously absent, is now populated.

## File Structure

- `index.qmd` — Atlas page: map (1/3) + info panel (2/3) with indices, pyramid, age table
- `compare.qmd` — Side-by-side province comparison
- `about.qmd` — Project info, team
- `_quarto.yml` — site config; output to `_site/`
- `scripts/build_census.py`, `scripts/build_geojson.py` — offline data pipeline (see above)
- `data/geojson/province_{year}.geojson` — Province boundaries (WGS84). 1881/1911/1921/1931 serve the atlas; 1901 is generated and ready but not yet wired into the site.
- `data/census/census_{year}.csv` — Aggregated data: 19 age groups × M/F/T + 4 demographic indices. 1881/1911/1921 are rebuilt from `raw/census/` adjusted-age sources; 1931 is an earlier build from a now-removed source (untouched by current scripts); 1901 is ready but not yet on the site.
- `downloads/{year}/{COD_PROV:03d}_{DEN_PROV}_{year}.csv` — Per-province CSV files for user download (granular per-year-of-age data, distinct from the aggregated `data/census/` format; 1931 has no downloads)
- `raw/` — Source data for the pipeline (gitignored)

## Key Conventions

- `COD_PROV` (integer) is the join key between GeoJSON features and census CSV rows; download filenames zero-pad it to 3 digits
- Age-group columns use prefix `m_`, `f_`, `t_` + suffix like `0`, `1_4`, `5_9`, ..., `85plus` (19 groups total)
- Demographic indices columns: `cwr` (child/woman ratio, ‰), `old_dep` (%), `struct_dep` (%), `mean_age` (years)
- National-level aggregates shown on initial load are computed **client-side** by summing per-province rows and recomputing ratios (see `showNationalData` in `index.qmd`). If you change index formulas in Python, mirror them here.
- Chart.js is loaded via `include-in-header` in the YAML frontmatter. Loading it in the HTML body does not work — Quarto strips inline `<script>` tags from body content.
- `index.qmd` intentionally disables map interaction (drag, zoom, scroll-wheel) — it is a static choropleth, not a pan/zoom map. Don't re-enable without reason.
- `downloads/1931/` is not populated; the download link is hidden when `year === 1931` in `index.qmd`.

## Deploy

Push to `main` triggers `.github/workflows/publish.yml`, which runs `quarto render` and publishes `_site/` to GitHub Pages. The GitHub Pages source must be set to "GitHub Actions" in repo settings. The custom domain `demopast.it` is configured via `CNAME`.
