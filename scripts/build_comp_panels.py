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

# (file panel, colonna conteggio, colonna tasso)
PANELS = {
    "fertility":  ("fertility_panel.csv",  "births",    "cbr"),
    "mortality":  ("mortality_panel.csv",  "deaths",    "cdr"),
    "marriages":  ("marriages_panel.csv",  "marriages", "nuptiality"),
    "migration":  ("migration_panel.csv",  "emigrants", "emig_rate"),
}


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
        if not a["has_count"]:
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


def main():
    for name, (fname, ccol, rcol) in PANELS.items():
        build_panel(name, fname, ccol, rcol)


if __name__ == "__main__":
    main()
