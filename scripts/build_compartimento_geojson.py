#!/usr/bin/env python3
"""Genera data/geojson/compartimento_{year}.geojson dai confini storici ISTAT.

Fonte: Limiti_{year}.zip (ISTAT, confini statistico-amministrativi storici,
CC-BY). 1871-1921 contengono lo shapefile Compartimenti diretto; 1931 e 1936
solo Province -> si dissolvono in compartimenti via COMP_PROVS (COD_PROV).

Output: poligoni regione in EPSG:4326 (Leaflet), semplificati, con proprieta'
COMP = nome canonico maiuscolo che combacia con e0_comp / <panel>_comp.

Prerequisito: gli ZIP scaricati ed estratti in SRC_DIR (vedi sotto).
"""
import glob
from pathlib import Path

import geopandas as gpd
from shapely import set_precision

SRC = Path("/tmp/istat_confini")
OUT = Path(__file__).resolve().parent.parent / "data/geojson"
YEARS_COMP = [1871, 1881, 1901, 1911, 1921]   # hanno Compartimenti_*.shp
YEARS_PROV = [1931, 1936]                       # solo Province -> dissolvi
SIMPLIFY_M = 200.0   # tolleranza semplificazione in metri (CRS metrico)

COMP_PROVS = {
    "PIEMONTE": [1, 2, 3, 4, 5, 6, 7], "LIGURIA": [8, 9, 10, 11],
    "LOMBARDIA": list(range(12, 21)), "VENEZIA TRIDENTINA": [21, 22],
    "VENETO": list(range(23, 31)), "VENEZIA GIULIA E ZARA": [31, 32],
    "EMILIA": list(range(33, 41)), "MARCHE": [41, 42, 43, 44],
    "TOSCANA": list(range(45, 54)), "UMBRIA": [54, 55],
    "LAZIO": [56, 57, 58, 59, 60], "CAMPANIA": [61, 62, 63, 64, 65],
    "ABRUZZI E MOLISE": [66, 67, 68, 69, 70], "PUGLIE": [71, 72, 73, 74, 75],
    "BASILICATA": [76, 77], "CALABRIE": [78, 79, 80],
    "SICILIA": list(range(81, 90)), "SARDEGNA": [90, 91, 92],
}
PROV_COMP = {p: c for c, ps in COMP_PROVS.items() for p in ps}

# DEN_COMP ISTAT -> nome canonico (per lo piu' solo maiuscolo)
def canon_comp(den):
    special = {"VENEZIA GIULIA": "VENEZIA GIULIA E ZARA"}
    u = str(den).strip().upper()
    return special.get(u, u)


def find_shp(patterns):
    for pat in patterns:
        fs = glob.glob(str(SRC / "**" / pat), recursive=True)
        if fs:
            return fs[0]
    return None


def write_geojson(gdf, year):
    gdf = gdf.to_crs(4326)
    out = OUT / f"compartimento_{year}.geojson"
    gdf.to_file(out, driver="GeoJSON")
    kb = out.stat().st_size // 1024
    print(f"[ok] {year}: {len(gdf)} compartimenti -> {out.name} ({kb} KB) "
          f"[{', '.join(sorted(gdf['COMP']))[:60]}...]")


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    for y in YEARS_COMP:
        shp = find_shp([f"Compartimenti_{y}.shp", f"Compartimenti_ {y}.shp"])
        if not shp:
            print(f"[skip] {y}: Compartimenti shapefile non trovato")
            continue
        g = gpd.read_file(shp)
        g["COMP"] = g["DEN_COMP"].map(canon_comp)
        g["geometry"] = g.geometry.simplify(SIMPLIFY_M)
        write_geojson(g[["COMP", "geometry"]].dissolve("COMP",
                                                        as_index=False), y)

    for y in YEARS_PROV:
        shp = find_shp([f"Province_{y}.shp", f"Province{y}.shp"])
        if not shp:
            print(f"[skip] {y}: Province shapefile non trovato")
            continue
        g = gpd.read_file(shp)
        g["COD_PROV"] = g["COD_PROV"].astype(float).astype(int)
        g["COMP"] = g["COD_PROV"].map(PROV_COMP)
        missing = g[g["COMP"].isna()]["COD_PROV"].tolist()
        if missing:
            print(f"[warn] {y}: COD_PROV senza compartimento (saltati): {missing}")
        g = g.dropna(subset=["COMP"])
        g["geometry"] = g.geometry.simplify(SIMPLIFY_M)
        write_geojson(g[["COMP", "geometry"]].dissolve("COMP",
                                                       as_index=False), y)


if __name__ == "__main__":
    main()
