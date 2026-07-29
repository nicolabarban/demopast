# Errori e incongruenze residue nei dati — stato al 2026-07-29

Inventario di ciò che resta dopo la campagna di correzioni del 2026-07-29
(25 celle corrette dalla stampa: Firenze/Catania/Cosenza/Terni/Enna 1936 +
20 celle 1871/1911/1921/1961, registro in `correzioni_2026-07-29.json`).
Da riprendere quando si deciderà di proseguire la bonifica.

## 1. Incoerenze aritmetiche residue (61 celle m+f ≠ totale)

| Anno | Celle | Delta max | Dettaglio |
|------|-------|-----------|-----------|
| 1881 | 10 | −45 | Aquila età 0 (−45); Como 10-14 e Grosseto 35-39 (±30); Bergamo, Ravenna, Forlì, Ancona, Macerata, Salerno (±2-20) |
| 1911 | 2 | +7 | Siena 10-14 (+5), Napoli 70-74 (+7) |
| 1921 | 5 | +24 | Sassari 50-54 (+24), Piacenza 35-39 e Parma 65-69 (+10), Reggio Emilia 85+ e Trapani 15-19 (−2) |
| 1931 | 10 | ±180 | **Cuneo 0/1-4 (±30) e Ascoli 0/1-4 (±180): coppie speculari = ARTEFATTO nostro** (split età 0 vs 1-4 calcolato diversamente per T e per M/F nel passaggio adjusted-age — correggibile in pipeline, senza fonti). Altre: Cuneo 80-84/85+, Ravenna ×3, Grosseto 85+ (±1-2) |
| 1936 | 17 | ±9 | tutte piccole, spesso a coppie speculari (Foggia 10-14/45-49 ∓9; Chieti 45-49/85+ +6; Benevento; Latina +9; …) |
| 1961 | 17 | −42 | cluster Valle d'Aosta (6 celle) e Treviso (6 celle): appartengono alle 161 righe in cui è il VOLUME STAMPATO a non quadrare (verificato per Treviso: M/F stampati giusti, totali stampati che ballano). Parma 70-74, Ravenna 15-19, Macerata ×2 (−10) |

**Azionabili:**
1. Artefatto 0/1-4 di Cuneo e Ascoli 1931 → fix di pipeline, nessuna fonte
   necessaria (~mezz'ora).
2. Le ~30 celle piccole non diagnosticate di 1881/1921/1931/1936 → stesso
   metodo del 2026-07-29: localizzare l'età singola dal delta nell'archivio
   OneDrive, verificare il ritaglio stampato con un agente, correggere via
   `scripts/apply_corrections.py`. Priorità bassa: |delta|≤45 su classi di
   decine di migliaia, effetto invisibile su indici e piramidi.
3. I cluster 1961 VdA/Treviso NON sono recuperabili: incoerenza della stampa.

## 2. Errori silenziosi (non rilevabili con m+f≠t)

Celle sbagliate in modo internamente coerente. Un caso trovato per
combinazione: **Parma 1961, classe 45-49 — CSV M=15.501/T=31.162, stampato
15.511/31.172** (da correggere alla prossima campagna). Tasso complessivo
ignoto; quantificabile solo con ri-verifica a campione contro le tavole.

## 3. Flag ERROR di plausibilità residui (18) — quasi tutti fenomeni reali

- 4 salti intercensuari da CAMBI DI CONFINE, non errori: Gorizia e Trieste
  1936→1951 (cessioni 1947), Valle d'Aosta 1936→1951 (riassetto provincia di
  Aosta), Palermo 1861→1871. Candidati a una whitelist in
  `check_plausibility.py`.
- 4 aritmetici = celle Ascoli/Cuneo/VdA del punto 1.
- 6 su nuzialità/natalità 1865-72 (Mantova, Ferrara, Girgenti, Pesaro, Roma):
  sotto-registrazione dei primi anni dello stato civile.
- 4 su emigrazione Belluno 1911-14 (82-94‰): emigrazione di massa reale;
  soglia del flag troppo severa.

## 4. Limiti strutturali documentati (stime dichiarate, non correggibili)

- 1881: manca Cagliari (COD_PROV 92).
- 1961: 6 province ricostruite; 1971: classi 0/1-4/75-79/80-84/85+ stimate
  (bias ~+7% su t_0).
- Città: classi stimate 1951/61/71 e confine 15-19/20-24 del 1901; Torino
  1911 senza riparto M/F dell'ignota (594); Catania 1931 rilevata il 22 nov;
  salto presente→residente tra 1931 e 1936; annessioni comunali anni '20-'30.
- 1871: COD_PROV 79 duplicato.
- Imperia 1961: fonte digitalizzata a età singole troncata all'età 73.
- Resto provincia: 3 celle ereditate (1911 Napoli 70-74 +7; 1921 Venezia
  10-14 −360 → ora ridotta?; cfr. output di `genera_resto_provincia.py`).

## Metodo per la prossima campagna

Collaudato il 2026-07-29: (1) delta della classe → localizza l'età singola
nell'archivio OneDrive (`Database Censimenti ISTAT/Censimento {anno}`);
(2) agente con il PDF di `downloads/sources/{anno}/provinces/` che legge il
ritaglio stampato a 300-1200 dpi e chiude i conti (M+F=MF, somme di colonna,
circondari); (3) correzione nel registro JSON + `scripts/apply_corrections.py`;
(4) rigenerare `build_census.py`, `check_plausibility.py`,
`genera_resto_provincia.py`; (5) commit e push.
