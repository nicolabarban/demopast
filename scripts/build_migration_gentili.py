"""Build the web panel for the Gentili (2026) 1876-1913 provincial emigration dataset.

Input : data/migration/gentili/Italian_Migration_1876_1913_English_Panel.csv
        (Zenodo, https://doi.org/10.5281/zenodo.23478963, CC-BY 4.0, unmodified)
Output: data/migration/gentili/gentili_panel.csv  (adds COD_PROV from province_1901.geojson,
        and emig_rate = Total_Emigration / Population_1881 * 1000)
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data/migration/gentili/Italian_Migration_1876_1913_English_Panel.csv"
OUT = ROOT / "data/migration/gentili/gentili_panel.csv"
GEO = ROOT / "data/geojson/province_1901.geojson"

# panel name -> DEN_PROV in province_1901.geojson
NAME_FIXES = {
    "Aquila": "Aquila degli Abruzzi",
    "Bari": "Bari delle Puglie",
    "Massa Carrara": "Massa e Carrara",
    "Reggio Calabria": "Reggio di Calabria",
    "Reggio Emilia": "Reggio nell'Emilia",
}


def main() -> None:
    df = pd.read_csv(SRC)
    features = json.loads(GEO.read_text())["features"]
    codes = {f["properties"]["DEN_PROV"]: f["properties"]["COD_PROV"] for f in features}
    mapped = df["Province"].replace(NAME_FIXES)
    unmatched = sorted(set(mapped) - set(codes))
    if unmatched:
        raise SystemExit(f"Provinces without COD_PROV: {unmatched}")
    out = df.assign(
        COD_PROV=mapped.map(codes).astype(int),
        emig_rate=(df["Total_Emigration"] / df["Population_1881"] * 1000).round(2),
    )
    out = out.rename(columns={"Year": "year", "Total_Emigration": "emigrants"})
    out.to_csv(OUT, index=False)
    print(f"{len(out)} rows, {out.COD_PROV.nunique()} provinces -> {OUT}")


if __name__ == "__main__":
    main()
