"""Transform long-format adjusted-age census CSVs in raw/census/ into the
wide-format per-province CSVs consumed by the Quarto site (data/census/).

Input  (long):  raw/census/{year}/data_census_{year}_adjusted_age.csv
                columns: code, province, age_class, male, female, total
Output (wide):  data/census/census_{year}.csv
                columns: COD_PROV, DEN_PROV, total_pop, male_pop, female_pop,
                         m_{age}, f_{age}, t_{age} for 19 age groups,
                         cwr, old_dep, struct_dep, mean_age

DEN_PROV is preserved from any pre-existing data/census/census_{year}.csv
(joined on COD_PROV) so that download-link filenames in downloads/{year}/
continue to resolve. New province codes fall back to the raw name with
spaces stripped.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "raw" / "census"
OUT_DIR = ROOT / "data" / "census"

YEARS = (1881, 1901, 1911, 1921)

AGE_CLASS_TO_SUFFIX = {
    "0": "0",
    "1-4": "1_4",
    "5-9": "5_9",
    "10-14": "10_14",
    "15-19": "15_19",
    "20-24": "20_24",
    "25-29": "25_29",
    "30-34": "30_34",
    "35-39": "35_39",
    "40-44": "40_44",
    "45-49": "45_49",
    "50-54": "50_54",
    "55-59": "55_59",
    "60-64": "60_64",
    "65-69": "65_69",
    "70-74": "70_74",
    "75-79": "75_79",
    "80-84": "80_84",
    "85+": "85plus",
}

AGE_SUFFIXES = list(AGE_CLASS_TO_SUFFIX.values())

AGE_MIDPOINTS = {
    "0": 0.5, "1_4": 2.5, "5_9": 7, "10_14": 12, "15_19": 17,
    "20_24": 22, "25_29": 27, "30_34": 32, "35_39": 37, "40_44": 42,
    "45_49": 47, "50_54": 52, "55_59": 57, "60_64": 62, "65_69": 67,
    "70_74": 72, "75_79": 77, "80_84": 82, "85plus": 87.5,
}

CHILD_AGES = ("0", "1_4")
FERTILE_F_AGES = ("15_19", "20_24", "25_29", "30_34", "35_39", "40_44")
YOUNG_AGES = ("0", "1_4", "5_9", "10_14")
WORKING_AGES = (
    "15_19", "20_24", "25_29", "30_34", "35_39",
    "40_44", "45_49", "50_54", "55_59", "60_64",
)
OLD_AGES = ("65_69", "70_74", "75_79", "80_84", "85plus")


def load_name_map(year: int) -> dict[int, str]:
    """Return {COD_PROV: DEN_PROV} from an existing processed CSV, if any."""
    path = OUT_DIR / f"census_{year}.csv"
    if not path.exists():
        return {}
    with path.open() as f:
        return {int(r["COD_PROV"]): r["DEN_PROV"] for r in csv.DictReader(f)}


def sanitize_name(name: str) -> str:
    """Fallback DEN_PROV: strip whitespace so it survives in URLs."""
    return "".join(name.split())


def build_year(year: int) -> pd.DataFrame:
    src = RAW_DIR / str(year) / f"data_census_{year}_adjusted_age.csv"
    df = pd.read_csv(src, dtype={"code": int, "age_class": str})
    unknown = set(df["age_class"]) - set(AGE_CLASS_TO_SUFFIX)
    if unknown:
        raise ValueError(f"{year}: unexpected age_class values {unknown}")
    df["age"] = df["age_class"].map(AGE_CLASS_TO_SUFFIX)

    wide = df.pivot_table(
        index=["code", "province"],
        columns="age",
        values=["male", "female", "total"],
        aggfunc="sum",
        fill_value=0,
    )
    prefix = {"male": "m", "female": "f", "total": "t"}
    wide.columns = [f"{prefix[metric]}_{age}" for metric, age in wide.columns]
    wide = wide.reset_index().rename(columns={"code": "COD_PROV"})

    name_map = load_name_map(year)
    wide["DEN_PROV"] = [
        name_map.get(c, sanitize_name(p))
        for c, p in zip(wide["COD_PROV"], wide["province"])
    ]
    wide = wide.drop(columns=["province"])

    wide["total_pop"] = sum(wide[f"t_{a}"] for a in AGE_SUFFIXES)
    wide["male_pop"] = sum(wide[f"m_{a}"] for a in AGE_SUFFIXES)
    wide["female_pop"] = sum(wide[f"f_{a}"] for a in AGE_SUFFIXES)

    children = sum(wide[f"t_{a}"] for a in CHILD_AGES)
    women_fertile = sum(wide[f"f_{a}"] for a in FERTILE_F_AGES)
    young = sum(wide[f"t_{a}"] for a in YOUNG_AGES)
    working = sum(wide[f"t_{a}"] for a in WORKING_AGES)
    old = sum(wide[f"t_{a}"] for a in OLD_AGES)

    wide["cwr"] = ((children / women_fertile) * 1000).round(1).where(women_fertile > 0, 0)
    wide["old_dep"] = ((old / working) * 100).round(1).where(working > 0, 0)
    wide["struct_dep"] = (((young + old) / working) * 100).round(1).where(working > 0, 0)
    weighted = sum(wide[f"t_{a}"] * AGE_MIDPOINTS[a] for a in AGE_SUFFIXES)
    wide["mean_age"] = (weighted / wide["total_pop"]).round(1).where(wide["total_pop"] > 0, 0)

    ordered = ["COD_PROV", "DEN_PROV", "total_pop", "male_pop", "female_pop"]
    for a in AGE_SUFFIXES:
        ordered.extend([f"m_{a}", f"f_{a}", f"t_{a}"])
    ordered.extend(["cwr", "old_dep", "struct_dep", "mean_age"])
    return wide[ordered].sort_values("COD_PROV").reset_index(drop=True)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for year in YEARS:
        out = build_year(year)
        path = OUT_DIR / f"census_{year}.csv"
        out.to_csv(path, index=False)
        print(f"{year}: {len(out)} provinces -> {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
