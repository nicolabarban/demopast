#!/usr/bin/env python3
"""
Rebuild downloads/1861/data_census_1861_adjusted_age.csv from Lorenzo
Lionello's digitised 1861 census database (OneDrive shared folder).

Background: the previous 1861 file had province data shifted/mislabeled
(e.g. "Torino" held Brescia's numbers, "Milano" held Basilicata's).
Sources, in order of preference per province:
  1861_correctionsMR/  (MR-corrected files, csv preferred over xls/xlsx)
  1861_full_database/  (one csv per province, single-year ages + Totale)

Milano (015) is kept from the already-published version, which was
re-extracted from the official TAVOLA SECONDA and matches the printed
marginals exactly.

Province names: codes already present keep their published DEN_PROV;
the 10 newly added codes take their census_1871 DEN_PROV.
"""

import csv
import re
from pathlib import Path

DB = Path.home() / ("Library/CloudStorage/OneDrive-AlmaMaterStudiorum"
                    "UniversitàdiBologna/Lorenzo Lionello's files - "
                    "Database Censimenti ISTAT/Censimento 1861")
FULL = DB / "1861_full_database"
CORR = DB / "1861_correctionsMR"
DEMO = Path(__file__).resolve().parent.parent
LONG = DEMO / "downloads/1861/data_census_1861_adjusted_age.csv"

# print-exact extractions in place (parse_prov_1861.py, validated against
# the printed TOTALE GENERALE): Milano, Como, Brescia, Siena,
# Abruzzo Ulteriore I, Capitanata
KEEP = {15, 13, 17, 52, 67, 71}

GROUPS = ([("0", 0, 0), ("1-4", 1, 4)] +
          [(f"{lo}-{lo + 4}", lo, lo + 4) for lo in range(5, 85, 5)] +
          [("85+", 85, 200)])


def parse_csv(path: Path) -> list[tuple[int, int, int]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    sep = ";" if text.splitlines()[0].count(";") > 1 else ","
    return clean(csv.DictReader(text.splitlines(), delimiter=sep))


def parse_xls(path: Path) -> list[tuple[int, int, int]]:
    import pandas as pd
    df = pd.read_excel(path)
    cols = {c.lower().split("_")[0]: c for c in df.columns}
    rows = ({"Age_column": str(r[cols["age"]]),
             "Male_column": r[cols["male"]],
             "Female_column": r[cols["female"]]} for _, r in df.iterrows())
    return clean(rows)


def clean(rows) -> list[tuple[int, int, int]]:
    """[(age, male, female)]; Centenari -> 100; Totale row dropped."""
    out = []
    for r in rows:
        a = str(r.get("Age_column") or "").strip()
        if not a or a == "nan" or a.lower().startswith("totale"):
            continue
        if re.match(r"^(Oltre\s+)?Centenari", a, re.I):
            age = 100
        else:
            m = re.match(r"^(?:Da\s+)?(\d+)", a)
            if not m:
                continue
            age = int(m.group(1))
        def num(v):
            try:
                return int(float(v))         # handles 10603.0 from pandas
            except (TypeError, ValueError):
                s = re.sub(r"[^\d]", "", str(v) if v is not None else "")
                return int(s) if s else 0
        out.append((age, num(r["Male_column"]), num(r["Female_column"])))
    return out


def load_db() -> dict[int, list[tuple[int, int, int]]]:
    src: dict[int, tuple[Path, str]] = {}
    for f in sorted(FULL.glob("*.csv")):
        src[int(f.name.split("_")[0])] = (f, "csv")
    for f in sorted(CORR.iterdir()):
        m = re.match(r"(\d+)_.+_1861\.(csv|xlsx?)$", f.name)
        if not m:
            continue
        code, ext = int(m.group(1)), m.group(2)
        # corrections override; csv preferred over excel within corrections
        if code not in src or src[code][0].parent == FULL or ext == "csv":
            src[code] = (f, "csv" if ext == "csv" else "xls")
    return {code: (parse_csv(p) if kind == "csv" else parse_xls(p))
            for code, (p, kind) in src.items()}


def main() -> None:
    db = load_db()

    name71 = {}
    for r in csv.DictReader((DEMO / "data/census/census_1871.csv").open()):
        name71[int(r["COD_PROV"])] = r["DEN_PROV"]
    old_rows = list(csv.DictReader(LONG.open()))
    name_old = {int(r["code"]): r["province"] for r in old_rows}

    out = []
    for code in sorted(set(db) | KEEP):
        if code in KEEP:
            out.extend({"code": f"{code:03d}", "province": r["province"],
                        "age_class": r["age_class"], "male": int(r["male"]),
                        "female": int(r["female"]), "total": int(r["total"])}
                       for r in old_rows if int(r["code"]) == code)
            continue
        ages = db[code]
        name = name_old.get(code) or name71.get(code) or f"COD{code}"
        for label, lo, hi in GROUPS:
            m = sum(x[1] for x in ages if lo <= x[0] <= hi)
            f = sum(x[2] for x in ages if lo <= x[0] <= hi)
            out.append({"code": f"{code:03d}", "province": name,
                        "age_class": label, "male": m, "female": f,
                        "total": m + f})

    with LONG.open("w", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(["code", "province", "age_class", "male", "female",
                    "total"])
        for r in out:
            w.writerow([r["code"], r["province"], r["age_class"],
                        r["male"], r["female"], r["total"]])

    by_prov = {}
    for r in out:
        by_prov.setdefault((r["code"], r["province"]), 0)
        by_prov[(r["code"], r["province"])] += r["total"]
    print(f"{LONG.name}: {len(by_prov)} provinces, "
          f"total {sum(by_prov.values()):,}")
    for (code, name), tot in sorted(by_prov.items()):
        print(f"  {code} {name:24s} {tot:>9,}")


if __name__ == "__main__":
    main()
