"""Build the web panel for the Gentili (2026) 1876-1913 provincial emigration dataset.

Input : data/migration/gentili/Italian_Migration_1876_1913_English_Panel.csv
        (Zenodo, https://doi.org/10.5281/zenodo.23478963, CC-BY 4.0, unmodified)
        data/census/census_{1871,1881,1901,1911,1921}.csv (province population = sum of t_* columns)
Output: data/migration/gentili/gentili_panel.csv  (adds COD_PROV from province_1901.geojson,
        emigrants = Male_Total + Female_Total where available, else Total_Emigration (see below),
        pop_interp = population linearly interpolated between flanking censuses, and
        emig_rate = emigrants / pop_interp * 1000)
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data/migration/gentili/Italian_Migration_1876_1913_English_Panel.csv"
OUT = ROOT / "data/migration/gentili/gentili_panel.csv"
GEO = ROOT / "data/geojson/province_1901.geojson"
CENSUS_YEARS = (1871, 1881, 1901, 1911, 1921)

# panel name -> DEN_PROV in province_1901.geojson
NAME_FIXES = {
    "Aquila": "Aquila degli Abruzzi",
    "Bari": "Bari delle Puglie",
    "Massa Carrara": "Massa e Carrara",
    "Reggio Calabria": "Reggio di Calabria",
    "Reggio Emilia": "Reggio nell'Emilia",
}


def census_population() -> pd.DataFrame:
    """Wide table: index COD_PROV, one column per census year (NaN where province absent)."""
    cols = {}
    for year in CENSUS_YEARS:
        census = pd.read_csv(ROOT / f"data/census/census_{year}.csv")
        totals = census.filter(regex=r"^t_").sum(axis=1)
        cols[year] = pd.Series(totals.to_numpy(), index=census["COD_PROV"])
    return pd.DataFrame(cols)


def interpolate_population(census: pd.DataFrame, years: range) -> pd.DataFrame:
    """Long table (COD_PROV, year, pop_interp); linear in time, missing census years skipped."""
    grid = pd.DataFrame(index=pd.Index(years, name="year"), columns=census.index, dtype=float)
    for cod, series in census.iterrows():
        known = series.dropna()
        grid[cod] = pd.Series(known.to_numpy(), index=known.index.astype(int)).reindex(
            grid.index.union(known.index.astype(int))
        ).interpolate(method="index").reindex(grid.index)
    return grid.stack().rename("pop_interp").rename_axis(["year", "COD_PROV"]).reset_index()


def main() -> None:
    df = pd.read_csv(SRC)
    features = json.loads(GEO.read_text())["features"]
    codes = {f["properties"]["DEN_PROV"]: f["properties"]["COD_PROV"] for f in features}
    mapped = df["Province"].replace(NAME_FIXES)
    unmatched = sorted(set(mapped) - set(codes))
    if unmatched:
        raise SystemExit(f"Provinces without COD_PROV: {unmatched}")
    # In the source, Total_Emigration is the full total up to 1903 but holds only a small partial
    # figure from 1904 on (e.g. Alessandria 1906: 296). Male_Total + Female_Total equals
    # Total_Emigration exactly in every province-year before 1904 where both exist, and its
    # national sum matches the official totals afterwards (1913: 872,596 vs 872,598).
    by_sex = df["Male_Total"] + df["Female_Total"]
    out = df.assign(
        COD_PROV=mapped.map(codes).astype(int),
        emigrants=by_sex.fillna(df["Total_Emigration"]),
    ).rename(columns={"Year": "year"})
    pop = interpolate_population(census_population(), range(out["year"].min(), out["year"].max() + 1))
    out = out.merge(pop, on=["year", "COD_PROV"], how="left")
    if out["pop_interp"].isna().any():
        raise SystemExit("Missing interpolated population for some province-years")
    out = out.assign(
        pop_interp=out["pop_interp"].round(0).astype(int),
        emig_rate=(out["emigrants"] / out["pop_interp"] * 1000).round(2),
    )
    out.to_csv(OUT, index=False)
    print(f"{len(out)} rows, {out.COD_PROV.nunique()} provinces -> {OUT}")


if __name__ == "__main__":
    main()
