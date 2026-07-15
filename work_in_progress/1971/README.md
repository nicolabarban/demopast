# Censimento 1971 — digitalizzazione completata (94/94 province)

Completato il 2026-07-15. Questa cartella conserva la trascrizione grezza e la
pipeline che la trasforma nel formato del sito, per riproducibilità e audit.
Il pannello 1971 è pubblicato: `downloads/1971/data_census_1971_adjusted_age.csv`,
`data/census/census_1971.csv`, `data/geojson/province_1971.geojson`.

## Cosa c'è qui
- `trascrizioni_1971.json` — righe PROVINCIA (Maschi/Femmine) trascritte dalle Tav. 3,
  16 classi quinquennali + totale stampato. **94/94 province.**
- `ref_1971.json` — riferimento ufficiale per COD_PROV (somma 94 = 54.136.547 = IT).
- `istruzioni_tav3_1971.md` — prompt usato dagli agenti di trascrizione.
- `assembla_1971.py` — rigenera `downloads/1971/data_census_1971_adjusted_age.csv`
  dalle trascrizioni (split <5 e 75+ con proporzioni 1961, largest-remainder).
- `estrai_righe_totale.py` — utility per ritagliare le strisce delle righe TOTALE
  PROVINCIA dai PDF, usata per rileggere le cifre dubbie ad alta risoluzione.
- `STATO_1971.md` — storico del lavoro.

## Verifiche superate
Per ogni provincia: somma delle 16 classi = totale stampato per sesso, e M+F =
`ref_1971.json` all'unità. Fanno eccezione, per cambi di confine 1961→1971 non
ricomponibili a livello di singola provincia, Como+Bergamo (esatta a coppia) e
Sassari+Nuoro+Cagliari (esatta a tripla). Somma delle 94 province = 54.136.547,
identica al totale nazionale ufficiale.

## Limite noto del dato
La Tav. 3 stampa solo 16 classi: `<5` e `75+` sono aperte. Le classi `0`, `1-4`,
`75-79`, `80-84`, `85+` del 1971 sono quindi **stimate** (proporzioni 1961 della
stessa provincia, largest-remainder così che i totali di colonna restino esatti),
non trascritte. Pordenone (93) e Isernia (94), che nel 1961 non esistevano, usano
le proporzioni della provincia madre (Udine 30, Campobasso 70).

## Rigenerare
```bash
python3 work_in_progress/1971/assembla_1971.py   # -> downloads/1971/...csv
python3 scripts/build_census.py                  # -> data/census/census_1971.csv
python3 scripts/check_plausibility.py            # -> data/quality/plausibility_report.md
```

PDF sorgente (94 Tav. 3 provinciali) archiviati nel repo in
`downloads/sources/1971/provinces/` e linkati dall'atlante. Originali su OneDrive
UniBo, cartella condivisa L. Lionello:
`~/Library/CloudStorage/OneDrive-AlmaMaterStudiorumUniversitàdiBologna/Lorenzo Lionello's files - Censimenti/1971/popby_sex_agegroup_provincia/`
