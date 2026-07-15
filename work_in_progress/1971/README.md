# Lavoro in corso: censimento 1971 (94 province)

Stato al 2026-07-15. Committato nel repo per poter riprendere da un altro computer.

## Cosa c'è qui
- `trascrizioni_1971.json` — righe PROVINCIA (Maschi/Femmine) trascritte dalle Tav. 3,
  16 classi quinquennali + totale stampato. **75/94 province fatte**, tutte verificate
  (somma = totale stampato E M+F = riferimento ISTAT all'unità; i casi a confini non
  ricomponibili — Sardegna, Como/Bergamo — tornano a coppia/tripla).
- `ref_1971.json` — riferimento ufficiale per COD_PROV (somma 94 = 54.136.547 = IT).
- `istruzioni_tav3_1971.md` — prompt per gli agenti di trascrizione.
- `assembla_1971.py` — genera `downloads/1971/data_census_1971_adjusted_age.csv`
  (split <5 e 75+ con proporzioni 1961, largest-remainder).
- `STATO_1971.md` — dettaglio pipeline.

## Province ANCORA DA TRASCRIVERE (19)
La Spezia (PDF "Spezia_1971.pdf"), Pesaro e Urbino (PDF "Urbino_1971.pdf"),
Reggio di Calabria, Siena, Siracusa, Taranto, Teramo, Terni, Torino, Trapani,
Trento, Treviso, Trieste, Udine, Varese, Venezia, Vercelli, Vicenza, Viterbo.

PDF sorgente (OneDrive UniBo, cartella condivisa L. Lionello):
`~/Library/CloudStorage/OneDrive-SharedLibraries-AlmaMaterStudiorumUniversitàdiBologna/Lorenzo Lionello - Popoulation by sex, age or age group and geography/Anno/1971/{Provincia}_1971.pdf`

## Come riprendere
1. Per ciascuna provincia mancante: lanciare un agente con `istruzioni_tav3_1971.md`,
   aggiungere il risultato a `trascrizioni_1971.json`, verificare somma=totale e
   M+F=ref_1971.
2. A 94/94: `python assembla_1971.py` (aggiornare il path del JSON se serve).
3. Aggiungere 1971 a YEARS in `scripts/build_census.py` e CENSUS_YEARS in
   `scripts/check_plausibility.py`; eseguire `build_census.py`.
4. `scripts/build_geojson.py` per il 1971 è già stato eseguito (province_1971.geojson,
   94 province — Pordenone/Isernia nuove). Shapefile in raw/shapefiles/Province_1971.
5. Aggiornare index.qmd (YEARS + slider max), compare.qmd, series.qmd, about.qmd,
   download.qmd, CLAUDE.md con l'anno 1971.
6. Copiare i 94 PDF in downloads/sources/1971/provinces (nomi {COD:03d}_{Nome}_1971.pdf)
   e rieseguire build_scans_js.py (aggiungere 1971 a YEARS e TAVOLE={...,1971:"TAV. 3"}).
7. quarto render, commit, push.
