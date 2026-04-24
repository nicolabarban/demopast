"""Convert province shapefiles in raw/shapefiles/ into simplified WGS84
GeoJSON under data/geojson/ for the Quarto site's Leaflet map.

Input:  raw/shapefiles/Province_{year}/Province_{year}.shp
Output: data/geojson/province_{year}.geojson

Each feature must expose integer COD_PROV and string DEN_PROV properties —
those are the keys used by the site's JS to join with census CSVs and to
label the info panel.
"""

from __future__ import annotations

from pathlib import Path

import geopandas as gpd

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw" / "shapefiles"
OUT_DIR = ROOT / "data" / "geojson"

SIMPLIFY_TOLERANCE_DEG = 0.005  # ~500 m at Italian latitudes


def build(year: int) -> Path:
    src = RAW_DIR / f"Province_{year}" / f"Province_{year}.shp"
    gdf = gpd.read_file(src).to_crs(epsg=4326)

    missing = {"COD_PROV", "DEN_PROV"} - set(gdf.columns)
    if missing:
        raise ValueError(f"{src} missing required columns: {missing}")

    gdf["COD_PROV"] = gdf["COD_PROV"].astype(int)
    gdf["DEN_PROV"] = gdf["DEN_PROV"].astype(str)
    gdf["geometry"] = gdf["geometry"].simplify(
        SIMPLIFY_TOLERANCE_DEG, preserve_topology=True
    )
    gdf = gdf[["COD_PROV", "DEN_PROV", "geometry"]]

    dst = OUT_DIR / f"province_{year}.geojson"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    gdf.to_file(dst, driver="GeoJSON")
    return dst


def main() -> None:
    for d in sorted(RAW_DIR.glob("Province_*")):
        year = int(d.name.split("_")[1])
        dst = build(year)
        size_kb = dst.stat().st_size / 1024
        print(f"{year}: {dst.relative_to(ROOT)} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
