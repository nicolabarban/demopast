# Stato digitalizzazione 1971 — checkpoint 2026-07-15

## Fatto (73/94 province trascritte e verificate al riferimento)
Tutte in `scratchpad/trascrizioni_1971.json`. Ogni provincia: somma 16 classi = totale
stampato, e M+F = riferimento ISTAT (`scratchpad/ref_1971.json`) all'unità — TRANNE i
casi a confini non ricomponibili, che tornano solo a coppia/tripla:
- Sardegna (Sassari/Nuoro/Cagliari): esatta come tripla (+0). Como/Bergamo esatta a coppia.

## MANCANTI (21) — da rilanciare dopo reset limiti (12:10 Europe/Rome)
La Spezia (file "Spezia_1971.pdf"), Pesaro e Urbino (file "Urbino_1971.pdf"),
Reggio di Calabria (file "ReggioCalabria_1971.pdf"), Siena, Siracusa, Sondrio,
Taranto, Teramo, Terni, Torino, Trapani, Trento, Treviso, Trieste, Udine, Varese,
Venezia, Vercelli, Verona, Vicenza, Viterbo.

## Pipeline pronta
- Istruzioni agente: `scratchpad/istruzioni_tav3_1971.md`
- Assemblaggio: `scratchpad/assembla_1971.py` (split <5 e 75+ con proporzioni 1961,
  largest-remainder). Da completare: mappa ALIAS nome→COD già in build_geojson names.
- Shapefile `province_1971.geojson` già generato (94 province, Pordenone/Isernia nuove).
- Riferimento `ref_1971.json` valido: somma 94 province = 54.136.547 = IT ufficiale.

## Dopo il completamento delle 94
1. python assembla_1971.py -> downloads/1971/data_census_1971_adjusted_age.csv
2. aggiungere 1971 a YEARS in build_census.py e CENSUS_YEARS in check_plausibility.py
3. build_census.py; aggiornare index/compare/series/about/download/CLAUDE.md
4. copiare i 94 PDF in downloads/sources/1971/provinces + build_scans_js.py
5. render, commit, push
