# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DEMOPAST (demopast.it) is an Italian historical demographic atlas, part of the GENPOP project. It displays interactive choropleth maps of Italian provinces with census data for 1881, 1901, 1911, and 1921.

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
- The 1881 adjusted-age source is missing `COD_PROV=92` (Cagliari); that province renders uncoloured with "N/A" in the panel — expected given the source gap.

## File Structure

- `index.qmd` — Atlas page: map (1/3) + info panel (2/3) with indices, pyramid, age table
- `compare.qmd` — Side-by-side province comparison
- `about.qmd` — Project info, team
- `_quarto.yml` — site config; output to `_site/`
- `scripts/build_census.py`, `scripts/build_geojson.py` — offline data pipeline (see above)
- `data/geojson/province_{year}.geojson` — Province boundaries (WGS84) for 1881/1901/1911/1921. `province_1931.geojson` still exists on disk but is unreferenced by the site (1931 was retired from the atlas).
- `data/census/census_{year}.csv` — Aggregated data: 19 age groups × M/F/T + 4 demographic indices. Rebuilt from `downloads/{year}/data_census_{year}_adjusted_age.csv` by `scripts/build_census.py`. `census_1931.csv` is an orphan from the previous pipeline and is not referenced by the site.
- `downloads/{year}/data_census_{year}_adjusted_age.csv` — Long-format adjusted-age source CSVs for 1881/1901/1911/1921. These are both the public download (linked from the atlas page per year) and the input to `scripts/build_census.py`. The previous per-province `{COD_PROV:03d}_{DEN_PROV}_{year}.csv` files have been retired.
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
