#!/usr/bin/env python3
"""
Build data/mortality/*.csv for the test mortality section from the
dati_ISTAT extraction outputs.

Inputs (dati_ISTAT/data/processed/mortality_extraction/csv/):
  cdr_province_panel.csv        COD_PROV, DEN_PROV, year, deaths_total, total_pop, cdr
  imr_province_1863_1882.csv    COD_PROV, DEN_PROV, region, year, deaths_u1, births, imr
  imr_province_1931_1936.csv    COD_PROV, DEN_PROV, name_source, year, imr, neonatal_m1
  e0_province_1881.csv          COD_PROV, DEN_PROV, e0_T/M/F
  deaths_prov_agesex_TIDY.csv   region, DEN_PROV, COD_PROV, year, sex, age, age_order, deaths

Outputs (data/mortality/):
  mortality_panel.csv   COD_PROV, DEN_PROV, year, deaths, cdr, imr, e0
  imr_annual.csv        COD_PROV, DEN_PROV, year, imr      (1863-1882 + 1931 + 1936)
  deaths_agesex.csv     COD_PROV, year, sex, age_group, deaths  (grouped for pyramids)
  lifetables_1881.csv   copied as-is (download)
"""

import csv
import shutil
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SRC = Path("/Users/nicolabarban/Library/CloudStorage/Dropbox/dati_ISTAT"
           "/data/processed/mortality_extraction/csv")
OUT = HERE / "data/mortality"

# pyramid age groups: map TIDY detail rows -> census-style groups
PYR_GROUPS = (["0", "1_4"] + [f"{a}_{a+4}" for a in range(5, 85, 5)] + ["85plus"])


def fnum(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def load_imr() -> dict:
    """(COD_PROV, year) -> imr; also returns annual rows."""
    imr = {}
    annual = []
    for r in csv.DictReader((SRC / "imr_province_1863_1882.csv").open()):
        v = fnum(r["imr"])
        if v is None or not r["COD_PROV"]:
            continue
        key = (int(r["COD_PROV"]), int(r["year"]))
        imr[key] = v
        annual.append({"COD_PROV": key[0], "DEN_PROV": r["DEN_PROV"],
                       "year": key[1], "imr": v})
    for r in csv.DictReader((SRC / "imr_province_1931_1936.csv").open()):
        v = fnum(r["imr"])
        if v is None or not r["COD_PROV"]:
            continue
        key = (int(r["COD_PROV"]), int(r["year"]))
        imr[key] = v
        annual.append({"COD_PROV": key[0], "DEN_PROV": r["DEN_PROV"],
                       "year": key[1], "imr": v})
    # 1921 (TAVOLA X under-1 deaths / TAVOLA I births)
    f1921 = SRC / "imr_province_1921.csv"
    if f1921.exists():
        for r in csv.DictReader(f1921.open()):
            v = fnum(r["imr"])
            if v is None or not r["COD_PROV"]:
                continue
            key = (int(r["COD_PROV"]), int(r["year"]))
            imr[key] = v
            annual.append({"COD_PROV": key[0], "DEN_PROV": r["DEN_PROV"],
                           "year": key[1], "imr": v})
    return imr, annual


def tidy_age_group(age: str, order: float) -> str | None:
    """Map a TIDY detail row to a pyramid group; cumulative rows -> None."""
    a = age.lower()
    if "in su" in a or "ignot" in a:
        return None
    if "nascita" in a and ("anno" in a or "anni" in a or "mese" in a):
        return None  # cumulative
    if order is None:
        return None
    if order < 1:
        return "0"
    if order < 5:
        return "1_4"
    if order >= 85:
        return "85plus"
    lo = int(order // 5 * 5)
    return f"{lo}_{lo+4}"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    imr, imr_annual = load_imr()

    e0 = {}
    for r in csv.DictReader((SRC / "e0_province_1881.csv").open()):
        v = fnum(r["e0_T"])
        if v:
            e0[int(r["COD_PROV"])] = v

    # --- mortality_panel ---
    rows = []
    for r in csv.DictReader((SRC / "cdr_province_panel.csv").open()):
        cod, year = int(r["COD_PROV"]), int(r["year"])
        rows.append({
            "COD_PROV": cod, "DEN_PROV": r["DEN_PROV"], "year": year,
            "deaths": r["deaths_total"], "cdr": r["cdr"],
            "imr": imr.get((cod, year), ""),
            "e0": e0.get(cod, "") if year == 1881 else "",
        })
    with (OUT / "mortality_panel.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "DEN_PROV", "year",
                                           "deaths", "cdr", "imr", "e0"])
        w.writeheader(); w.writerows(rows)
    print(f"mortality_panel.csv: {len(rows)} rows")

    # --- imr_annual ---
    imr_annual.sort(key=lambda r: (r["COD_PROV"], r["year"]))
    with (OUT / "imr_annual.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "DEN_PROV", "year", "imr"])
        w.writeheader(); w.writerows(imr_annual)
    print(f"imr_annual.csv: {len(imr_annual)} rows")

    # --- deaths_agesex (grouped) ---
    acc = defaultdict(float)
    for r in csv.DictReader((SRC / "deaths_prov_agesex_TIDY.csv").open()):
        g = tidy_age_group(r["age"], fnum(r["age_order"]))
        if g is None or not r["COD_PROV"]:
            continue
        acc[(int(r["COD_PROV"]), int(r["year"]), r["sex"], g)] += float(r["deaths"])
    # 1921 TAVOLA X (age_lo/age_hi schema, checksum-validated detail rows)
    f1921 = SRC / "deaths_prov_agesex_1921.csv"
    if f1921.exists():
        for r in csv.DictReader(f1921.open()):
            lo = fnum(r["age_lo"])
            if lo is None or r["age"] == "TOTALE" or not r["COD_PROV"]:
                continue  # skip TOTALE and età ignota
            g = tidy_age_group(r["age"], lo)
            if g is None:
                continue
            acc[(int(r["COD_PROV"]), int(r["year"]), r["sex"], g)] += float(r["deaths"])
    ag_rows = [{"COD_PROV": c, "year": y, "sex": s, "age_group": g,
                "deaths": int(v)}
               for (c, y, s, g), v in sorted(acc.items())]
    with (OUT / "deaths_agesex.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "year", "sex",
                                           "age_group", "deaths"])
        w.writeheader(); w.writerows(ag_rows)
    years = sorted({r["year"] for r in ag_rows})
    print(f"deaths_agesex.csv: {len(ag_rows)} rows, years {years}")

    shutil.copy(SRC / "lifetables_1881.csv", OUT / "lifetables_1881.csv")
    print("lifetables_1881.csv copied")


if __name__ == "__main__":
    main()
