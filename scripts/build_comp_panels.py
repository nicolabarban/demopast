#!/usr/bin/env python3
"""Aggrega i pannelli provinciali (fertility/mortality/marriages/migration)
a livello COMPARTIMENTO, per la vista a doppio livello del sito.

Per ogni pannello produce:
  data/<panel>/<panel>_comp.csv         compartimento, year, count, rate
  data/<panel>/<panel>_comp_byprov.csv  COD_PROV, year, count, rate
                                        (valore del compartimento ribaltato su
                                         ogni provincia, per colorare la mappa)

Metodo:
  count_comp = somma dei conteggi provinciali del compartimento (checksum).
  Per il tasso: si recupera la popolazione provinciale implicita
  pop = count / rate * SCALE (dove rate e count esistono entrambi), si somma,
  e rate_comp = sum(count) / sum(pop) * SCALE. Così il tasso compartimentale
  e' coerente con quelli provinciali senza bisogno di una fonte pop separata.
  Una (comp, anno) e' inclusa solo se ha almeno una provincia con dati.
"""
import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data"

# COD_PROV -> compartimento (full 1936 extent; i file storici hanno meno codici)
COMP_PROVS = {
    "PIEMONTE": [1, 2, 3, 4, 5, 6, 7],
    "LIGURIA": [8, 9, 10, 11],
    "LOMBARDIA": list(range(12, 21)),
    "VENEZIA TRIDENTINA": [21, 22],
    "VENETO": list(range(23, 31)),
    "VENEZIA GIULIA E ZARA": [31, 32],
    "EMILIA": list(range(33, 41)),
    "MARCHE": [41, 42, 43, 44],
    "TOSCANA": list(range(45, 54)),
    "UMBRIA": [54, 55],
    "LAZIO": [56, 57, 58, 59, 60],
    "CAMPANIA": [61, 62, 63, 64, 65],
    "ABRUZZI E MOLISE": [66, 67, 68, 69, 70],
    "PUGLIE": [71, 72, 73, 74, 75],
    "BASILICATA": [76, 77],
    "CALABRIE": [78, 79, 80],
    "SICILIA": list(range(81, 90)),
    "SARDEGNA": [90, 91, 92],
}
PROV_COMP = {p: c for c, ps in COMP_PROVS.items() for p in ps}
SCALE = 1000.0

# Venezia Giulia e Zara: dati demopast internamente incoerenti per il 1931
# (codice provincia 32 = Trieste nel census ma = Fiume nei panel; census ha
# solo 2 delle 5 province) -> esclusa da tutti i pannelli comp, come nelle
# life tables. Resta grigia in mappa.
EXCLUDE_COMP = {"VENEZIA GIULIA E ZARA"}

# fertility/marriages/migration: i panel provinciali del sito sono completi
# (verificato in audit) -> aggregazione diretta per COD_PROV.
PANELS = {
    "fertility":  ("fertility_panel.csv",  "births",    "cbr"),
    "marriages":  ("marriages_panel.csv",  "marriages", "nuptiality"),
    "migration":  ("migration_panel.csv",  "emigrants", "emig_rate"),
}

# mortalita': ricostruita da fonti AUTOREVOLI (il mortality_panel del sito e'
# incompleto: perde le province con nome storico variante).
DATI = Path("/Users/nicolabarban/Library/CloudStorage/Dropbox/dati_ISTAT"
            "/data/processed/mortality_extraction/csv")
CENSUS = DATA / "census"
CROSSWALK = DATI / "province_crosswalk_demopast.csv"
DEATHS_PROV = DATI / "deaths_province_panel.csv"          # 1863-1881 + 1901
DEATHS_COMP_AGESEX = {1911: DATI / "deaths_comp_agesex_1911.csv",
                      1931: DATI / "deaths_comp_agesex_1931_full.csv"}
MORT_YEARS = [1871, 1881, 1901, 1911, 1931]


def fnum(v):
    if v is None:
        return None
    v = v.strip()
    if v == "" or v.lower() == "nan":
        return None
    try:
        return float(v)
    except ValueError:
        return None


def build_panel(name, fname, ccol, rcol):
    src = DATA / name / fname
    if not src.exists():
        print(f"[skip] {name}: {src} assente")
        return
    rows = list(csv.DictReader(src.open()))

    # accumula per (compartimento, anno)
    agg = defaultdict(lambda: {"count": 0.0, "pop": 0.0,
                               "has_count": False, "has_pop": False})
    for r in rows:
        try:
            cod = int(r["COD_PROV"])
        except (ValueError, KeyError):
            continue
        comp = PROV_COMP.get(cod)
        if comp is None:
            continue
        year = r["year"]
        cnt = fnum(r.get(ccol))
        rate = fnum(r.get(rcol))
        a = agg[(comp, year)]
        if cnt is not None:
            a["count"] += cnt
            a["has_count"] = True
            if rate is not None and rate > 0:
                a["pop"] += cnt / rate * SCALE
                a["has_pop"] = True

    comp_rows, byprov_rows = [], []
    for (comp, year), a in sorted(agg.items()):
        if not a["has_count"] or comp in EXCLUDE_COMP:
            continue
        count = round(a["count"])
        rate = (round(a["count"] / a["pop"] * SCALE, 2)
                if a["has_pop"] and a["pop"] > 0 else "")
        comp_rows.append({"compartimento": comp, "year": year,
                          ccol: count, rcol: rate})
        for cod in COMP_PROVS[comp]:
            byprov_rows.append({"COD_PROV": cod, "year": year,
                                ccol: count, rcol: rate})

    out_comp = DATA / name / f"{name}_comp.csv"
    with out_comp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["compartimento", "year", ccol, rcol])
        w.writeheader()
        w.writerows(comp_rows)

    out_bp = DATA / name / f"{name}_comp_byprov.csv"
    with out_bp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "year", ccol, rcol])
        w.writeheader()
        w.writerows(byprov_rows)

    yrs = sorted({r["year"] for r in comp_rows})
    print(f"[ok] {name}: {len(comp_rows)} righe comp ({len(yrs)} anni "
          f"{yrs[0]}-{yrs[-1]}), {len(byprov_rows)} righe byprov")


def census_pop_by_comp(year):
    """Popolazione compartimentale = somma province dal census dell'anno."""
    f = CENSUS / f"census_{year}.csv"
    if not f.exists():
        return {}
    pop = defaultdict(float)
    for x in csv.DictReader(f.open()):
        try:
            comp = PROV_COMP.get(int(x["COD_PROV"]))
        except (ValueError, KeyError):
            continue
        v = fnum(x.get("total_pop"))
        if comp and v:
            pop[comp] += v
    return pop


def build_mortality():
    """Ricostruisce mortality_comp da fonti autorevoli (non dal panel sito).
    deaths: 1871/1881/1901 da deaths_province_panel via crosswalk;
            1911/1931 da deaths_comp_agesex (somma eta', esclusa riga TOTALE).
    cdr:    deaths / popolazione censuaria * 1000."""
    name2cod = {r["province_istat"]: int(r["COD_PROV"])
                for r in csv.DictReader(CROSSWALK.open())}
    # deaths_province_panel usa nomi moderni/corti assenti dal crosswalk
    # (che ha i nomi storici): mappa esplicita -> COD_PROV
    name2cod.update({
        "Agrigento": 84, "Bari": 72, "Imperia": 8, "L'Aquila": 66,
        "Massa-Carrara": 45, "Reggio Calabria": 80, "Reggio Emilia": 35,
    })
    deaths = defaultdict(lambda: defaultdict(float))   # year -> comp -> deaths

    # 1871/1881/1901 dal panel provinciale pieno
    for r in csv.DictReader(DEATHS_PROV.open()):
        y = int(r["year"])
        if y not in (1871, 1881, 1901):
            continue
        cod = name2cod.get(r["province"])
        comp = PROV_COMP.get(cod) if cod else None
        v = fnum(r.get("deaths_total"))
        if comp and v:
            deaths[y][comp] += v

    # 1911/1931 dalle tavole compartimentali eta'xsesso (nomi d'epoca -> canonici)
    comp_alias = {"LUCANIA": "BASILICATA"}
    for y, f in DEATHS_COMP_AGESEX.items():
        for r in csv.DictReader(f.open()):
            comp = comp_alias.get(r["compartimento"], r["compartimento"])
            if comp == "REGNO" or r["age"] == "TOTALE":
                continue
            v = fnum(r.get("deaths"))
            if v:
                deaths[y][comp] += v

    comp_rows, byprov_rows = [], []
    for y in MORT_YEARS:
        pop = census_pop_by_comp(y)
        for comp in sorted(deaths[y]):
            if comp in EXCLUDE_COMP:
                continue
            d = round(deaths[y][comp])
            p = pop.get(comp, 0)
            cdr = round(d / p * SCALE, 2) if p > 0 else ""
            comp_rows.append({"compartimento": comp, "year": y,
                              "deaths": d, "cdr": cdr})
            for cod in COMP_PROVS[comp]:
                byprov_rows.append({"COD_PROV": cod, "year": y,
                                    "deaths": d, "cdr": cdr})

    out = DATA / "mortality" / "mortality_comp.csv"
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["compartimento", "year",
                                           "deaths", "cdr"])
        w.writeheader()
        w.writerows(comp_rows)
    out_bp = DATA / "mortality" / "mortality_comp_byprov.csv"
    with out_bp.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["COD_PROV", "year", "deaths", "cdr"])
        w.writeheader()
        w.writerows(byprov_rows)

    yrs = sorted({r["year"] for r in comp_rows})
    print(f"[ok] mortality (ricostruita): {len(comp_rows)} righe comp "
          f"({yrs}), {len(byprov_rows)} righe byprov")


def main():
    for name, (fname, ccol, rcol) in PANELS.items():
        build_panel(name, fname, ccol, rcol)
    build_mortality()


if __name__ == "__main__":
    main()
