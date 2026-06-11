#!/usr/bin/env python3
"""
Build data/fertility/fertility_panel.csv for the test fertility section.

Input:
  dati_ISTAT/.../csv/births_province_panel.csv
      province, year, births, COD_PROV, DEN_PROV, source, validated

Population denominators: demopasta census files (1861-1936), linearly
interpolated between flanking censuses per COD_PROV; nearest census when a
year falls outside a province's census range. 1931 rows without a
historical COD_PROV (post-1927 split-off provinces) are matched by name
against census_1931 so they still get a code, name and rate.

Output: data/fertility/fertility_panel.csv
  COD_PROV, DEN_PROV, year, births, cbr   (crude birth rate per 1000)
"""

import csv
import re
import shutil
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SRC = Path("/Users/nicolabarban/Library/CloudStorage/Dropbox/dati_ISTAT"
           "/data/processed/mortality_extraction/csv/births_province_panel.csv")
CENSUS_DIR = HERE / "data/census"
OUT = HERE / "data/fertility"

CENSUS_YEARS = [1861, 1871, 1881, 1901, 1911, 1921, 1931, 1936]


def normname(s: str) -> str:
    s = unicodedata.normalize("NFD", s.lower())
    return re.sub(r"[^a-z]", "", s)


def load_census() -> tuple[dict, dict]:
    """pop[(COD_PROV, census_year)] -> total_pop; name1931[norm] -> (cod, den)."""
    pop, name1931 = {}, {}
    for cy in CENSUS_YEARS:
        f = CENSUS_DIR / f"census_{cy}.csv"
        if not f.exists():
            continue
        for r in csv.DictReader(f.open()):
            try:
                cod, tp = int(r["COD_PROV"]), int(r["total_pop"])
            except (KeyError, ValueError):
                continue
            pop[(cod, cy)] = tp
            if cy == 1931:
                name1931[normname(r["DEN_PROV"])] = (cod, r["DEN_PROV"])
    return pop, name1931


def interp_pop(pop: dict, cod: int, year: int) -> float | None:
    """Linear interpolation between flanking censuses; nearest outside range."""
    avail = sorted(cy for cy in CENSUS_YEARS if (cod, cy) in pop)
    if not avail:
        return None
    if year <= avail[0]:
        return pop[(cod, avail[0])]
    if year >= avail[-1]:
        return pop[(cod, avail[-1])]
    lo = max(cy for cy in avail if cy <= year)
    hi = min(cy for cy in avail if cy >= year)
    if lo == hi:
        return pop[(cod, lo)]
    w = (year - lo) / (hi - lo)
    return pop[(cod, lo)] * (1 - w) + pop[(cod, hi)] * w


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    pop, name1931 = load_census()

    rows, no_pop = [], set()
    for r in csv.DictReader(SRC.open()):
        if not r["births"]:
            continue
        year, births = int(r["year"]), int(r["births"])
        cod = int(r["COD_PROV"]) if r["COD_PROV"] else None
        den = r["DEN_PROV"]
        if cod is None and year == 1931:
            # post-1927 provinces: match by name against census_1931
            hit = name1931.get(normname(r["province"]))
            if hit:
                cod, den = hit
        if cod is None:
            no_pop.add(f"{r['province']} ({year})")
            continue
        p = interp_pop(pop, cod, year)
        cbr = round(births / p * 1000, 2) if p else ""
        rows.append({"COD_PROV": cod, "DEN_PROV": den or r["province"],
                     "year": year, "births": births, "cbr": cbr})

    rows.sort(key=lambda r: (r["year"], r["COD_PROV"]))
    with (OUT / "fertility_panel.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "DEN_PROV", "year",
                                           "births", "cbr"])
        w.writeheader(); w.writerows(rows)

    years = sorted({r["year"] for r in rows})
    print(f"fertility_panel.csv: {len(rows)} rows, {len(years)} years "
          f"({years[0]}-{years[-1]})")
    for y in years:
        yr = [r for r in rows if r["year"] == y]
        rates = sorted(r["cbr"] for r in yr if r["cbr"] != "")
        med = rates[len(rates) // 2] if rates else "-"
        print(f"  {y}: {len(yr):3d} prov, total {sum(r['births'] for r in yr):9,d},"
              f" median CBR {med}")
    if no_pop:
        print("dropped (no COD_PROV/census match):", ", ".join(sorted(no_pop)))

    # full extraction (incl. provinces without census denominators) as download
    shutil.copy(SRC, OUT / "births_full_extraction.csv")
    print("births_full_extraction.csv copied")


if __name__ == "__main__":
    main()
