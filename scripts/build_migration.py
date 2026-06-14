#!/usr/bin/env python3
"""
Build data/migration/migration_panel.csv for the test migration section.

Input:
  dati_ISTAT/.../csv/emigration_province_panel.csv
      province, year, emigrants, emig_eur, emig_trans, COD_PROV, DEN_PROV,
      source, validated

Population denominators: demopasta census files, linearly interpolated
between flanking censuses per COD_PROV (same approach as build_marriages.py).

Output: data/migration/migration_panel.csv
  COD_PROV, DEN_PROV, year, emigrants, emig_rate   (per 1000 inhabitants)
plus emigration_full_extraction.csv (source copy, incl. Europe/transoceanic
split and validation flags).
"""

import csv
import re
import shutil
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SRC = Path("/Users/nicolabarban/Library/CloudStorage/Dropbox/dati_ISTAT"
           "/processed/mortality_extraction/csv/emigration_province_panel.csv")
CENSUS_DIR = HERE / "data/census"
OUT = HERE / "data/migration"

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
        if not r["emigrants"]:
            continue
        year, emig = int(r["year"]), int(r["emigrants"])
        cod = int(r["COD_PROV"]) if r["COD_PROV"] else None
        den = r["DEN_PROV"]
        if cod is None and year >= 1927:
            hit = name1931.get(normname(r["province"]))
            if hit:
                cod, den = hit
        if cod is None:
            no_pop.add(f"{r['province']} ({year})")
            continue
        p = interp_pop(pop, cod, year)
        rate = round(emig / p * 1000, 2) if p else ""
        rows.append({"COD_PROV": cod, "DEN_PROV": den or r["province"],
                     "year": year, "emigrants": emig, "emig_rate": rate})

    rows.sort(key=lambda r: (r["year"], r["COD_PROV"]))
    with (OUT / "migration_panel.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "DEN_PROV", "year",
                                           "emigrants", "emig_rate"])
        w.writeheader(); w.writerows(rows)

    years = sorted({r["year"] for r in rows})
    print(f"migration_panel.csv: {len(rows)} rows, years {years}")
    for y in years:
        yr = [r for r in rows if r["year"] == y]
        rates = sorted(r["emig_rate"] for r in yr if r["emig_rate"] != "")
        med = rates[len(rates) // 2] if rates else "-"
        print(f"  {y}: {len(yr):3d} prov, total {sum(r['emigrants'] for r in yr):8,d},"
              f" median rate {med}")
    if no_pop:
        print("dropped (no COD_PROV/census match):", ", ".join(sorted(no_pop)))

    shutil.copy(SRC, OUT / "emigration_full_extraction.csv")
    print("emigration_full_extraction.csv copied")


if __name__ == "__main__":
    main()
