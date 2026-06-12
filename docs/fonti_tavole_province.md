# Inventario fonti — Popolazione per età e sesso a livello provinciale

Materiale disponibile nel database di Lorenzo Lionello (OneDrive, *Database
Censimenti ISTAT*) e tavole originali ISTAT/MAIC da cui proviene ogni
censimento. Le intestazioni delle tavole sono lette dalle scansioni stesse;
le voci segnate ⚠ (volume/edizione) sono attribuzioni da confermare sul
frontespizio del volume.

| Censimento (data) | Tavola originale (dall'intestazione della scansione) | Volume / pubblicazione | Dettaglio età nella fonte | Materiale per provincia (bypage) | Altre cartelle nel DB | Su demopast |
|---|---|---|---|---|---|---|
| **1861** (31 dic 1861) | TAVOLA II (Seconda) — *Popolazione accentrata e sparsa per età, sesso e stato civile* | MAIC, Censimento generale (31 dicembre 1861), **Vol. II, ed. 1864** (confermato: volume intero in `downloads/sources/1861/`) | Anni singoli 0→100, Centenari / Oltre centenari | 59 province: PDF scansione (~6 pp.) + CSV | `1861_full_database`, `1861_correctionsMR`, `Limiti_1861` | ✔ dati + scan link |
| **1871** (31 dic 1871) | Tavola II — *Popolazione classificata per età* | MAIC, Censimento 31 dicembre 1871, Vol. II (Roma, ~1875) ⚠ | Anni singoli 0→100, Centenari | 69 province: PDF + CSV | `1871_full_database`, `Limiti_1871` | ✔ dati + scan link |
| **1881** (31 dic 1881) | TAVOLA II — *Popolazione per gruppi di età, per sesso, stato civile e istruzione nei circondari (o distretti) e nelle provincie* (p. ~502) | MAIC, Censimento della popolazione del Regno d'Italia al 31 dicembre 1881 ⚠ vol. | Anni singoli 0–4, poi gruppi quinquennali fino a 95-100, Centenari, Ignota | 68 province: PDF + CSV | `1881_full_database`, `Limiti_1881` | ✔ dati + scan link |
| **1901** (10 feb 1901) | TAV. XX — *Classificazione della popolazione per sesso ed età. A. In ciascuna provincia* (p. ~90; tavola riassuntiva nazionale, più province per pagina) | MAIC, Censimento della popolazione del Regno d'Italia al 10 febbraio 1901, volume riassuntivo ⚠ | Anni singoli 0→15, poi 15-18 / 18-21 / 21-25, quinquennali 25→100, 100 e oltre, Ignota | 69 province: PDF (1 pagina) + CSV + XLSX | `1901_full_database`, `1901_clean`, `Limiti_1901` | ✔ dati (**ricostruiti print-exact giu 2026**: doppia digitalizzazione Datalab + Lionello riconciliata sulle Somme stampate) + scan link |
| **1911** (10 giu 1911) | TAVOLA IV — *Popolazione presente classificata per sesso, età, stato civile ed istruzione* (p. ~614) | MAIC/DGS, Censimento della popolazione del Regno al 10 giugno 1911 ⚠ vol. | Anni singoli (0-1, 1-2, …) | 65 province: PDF + XLSX | `1911_full_database`, `Limiti_1911` | ✔ dati + scan link |
| **1921** (1 dic 1921) | TAVOLA XIV — *Popolazione presente classificata per sesso, età e stato civile* (p. ~302) | ISTAT (Ufficio del censimento), Censimento della popolazione del Regno al 1° dicembre 1921 — volumi regionali ⚠ | Anni singoli 0→~20, poi quinquennali fino a 95-100, oltre 100 | 69 province: PDF + CSV (cartella `1921_bypage`) | `1921_full_database`, `1921_full_database_clean`, `Limiti_1921` | ✔ dati + scan link |
| **1931** (21 apr 1931) | TAVOLA IX — *Popolazione presente secondo l'età, il sesso e lo stato civile* ⚠ titolo (OCR illeggibile) | ISTAT, VII Censimento generale della popolazione — fascicoli provinciali ⚠ | Anni singoli; più pagine per provincia (dettaglio anche per comuni capoluogo) | 91 cartelle (89 province con codice + `000_Noprovincia`: Littoria, Pola…); PDF per pagina + XLSX per comune — **uniti in un PDF unico per provincia** sul sito | `1931_full_database`, `Limiti_1931` | ✔ dati + scan link (merge) |
| **1936** (21 apr 1936) | TAVOLA X — *Popolazione residente secondo l'età, il sesso e lo stato civile. A) Provincia* | ISTAT, VIII Censimento generale della popolazione, 21 aprile 1936-XIV — fascicoli provinciali ⚠ | Anni singoli (CSV campione: 0→74; coda da verificare) | 94 province: PDF + CSV | `1936_full_database`, `Limiti_1936` | ✔ dati + scan link |
| **1951** (4 nov 1951) | TAV. 4 — *Popolazione residente [per sesso ed età]* | ISTAT, IX Censimento generale della popolazione, **Vol. I — Dati sommari per comune** (confermato dall'intestazione) | Gruppi: fino a 6, 6-10, 10-14, 14-18, 18-21, 21-25, 25-35, …, 65 e oltre — **dati per comune** | 90 province: PDF provincia + un CSV per comune | `1951_full_database`, `Limiti_1951` | ✘ non ancora sul sito |
| **1961** (15 ott 1961) | (intestazione non leggibile) ⚠ | ISTAT, X Censimento generale della popolazione ⚠ vol. | Anni singoli (file nominati `*_1960`) | 86 province: PDF + CSV (`1961_single_age_database/1961_database_bypage_single_age`) | `1961_problems` (province problematiche: Brindisi, Caltanissetta, Enna, Ferrara, Foggia, …) | ✘ non ancora sul sito |

## Note

- **Censimenti mancanti**: 1891 e 1941 non furono effettuati; il DB non li contiene.
- **bypage** = una cartella per provincia con il ritaglio PDF della tavola
  originale e la digitalizzazione (CSV/XLSX). È il materiale usato per i link
  "original scan" su demopast (`downloads/sources/{anno}/provinces/`).
- **Qualità digitalizzazione**: 1861 — età 70+ gonfiate ×10 in 5 province,
  ricostruite print-exact (commit `901962c`); Palermo 1861 incompleto nel DB
  (~385k vs ~584k attesi). 1901 — il file originariamente pubblicato aveva i
  gruppi 15-19/20-24 mal allocati in tutte le 69 province + doppi conteggi
  (es. Arezzo +38k); **ricostruito print-exact (giu 2026)** riconciliando due
  digitalizzazioni indipendenti (Datalab OCR + CSV Lionello) cella per cella
  contro le Somme stampate. Errori di stampa documentati nell'originale:
  Siena 40-45 F «3 271» → 6 271; Reggio Emilia 11 F = 2 833 (entrambe le
  digitalizzazioni l'avevano travisato); Catanzaro 21-25 M = 13 386;
  Venezia Somma M «199 115» → 199 715 (refuso nella Somma, righe corrette).
  21 province conservano residui non allocabili ≤±50 rispetto alla Somma
  stampata (incoerenze interne della tavola originale).
- **Correzioni giu 2026** (verifica incrociata file lunghi ↔ file sito):
  - 1871 — il CSV scaricabile (`downloads/1871/data_census_1871_adjusted_age.csv`)
    conteneva due volte la provincia cod 079 («Calabria Ulteriore II» +
    «Catanzaro», blocchi identici → totale doppio 824 472). Rimosso il blocco
    duplicato (1330 → 1311 righe); il file wide del sito era già corretto.
  - 1931 — `data/census/census_1931.csv`: corretti tre `DEN_PROV` ereditati da
    versioni precedenti: cod 32 «Fiume» → **Trieste** (i dati, 348 405 ab.,
    sono di Trieste: lo confermano file lungo e geojson), cod 70 «Capobasso» →
    Campobasso, cod 35 «ReggioE» → ReggioEmilia. Lo scan
    `032_Fiume_1931.pdf` è numerato male (il cod 32 è Trieste); resta accanto
    al corretto `032_Trieste_1931.pdf`, che è quello linkato dal sito.
- **QC sistematico** (skill census-consistency, giu 2026): tutti gli 8 anni
  passati al controllo automatico — report in `docs/qc_flags_census.csv`
  (566 flag: 58 ERROR, 508 WARN). Gli ERROR sono incoerenze M+F ≠ Totale
  **ereditate dalle tavole originali / trascrizioni** (1881: 10, 1911: 3,
  1921: 13, 1931: 10, 1936: 21, 1871: 1); i WARN sono per lo più profili
  d'età o sex ratio anomali spiegabili (emigrazione maschile, coorti di
  guerra). Correggerli richiede verifica cella per cella sullo scan.
- **Verifica sullo scan dei cluster peggiori (giu 2026)** — Nuoro 1936,
  Imperia 1936, Napoli 1936, Messina 1871 ricontrollati cella per cella
  sulle tavole originali, riconciliando con i totali di controllo stampati
  (Complesso, «fino a N», 15-64, 65-ω / Totale provincia), che tornano
  **esattamente** dopo le correzioni:
  - *Nuoro 1936*: 13 celle corrette (per lo più Totali di gruppo errati,
    es. 65-69 «7 445» → 6 940); incluse 2 righe non flaggate perché
    internamente coerenti ma sbagliate vs scan (55-59, 60-64 M).
  - *Imperia 1936*: la trascrizione proveniva dalla **tavola sbagliata**
    (somma 154 163 = popolazione presente, non Tav. X residente 158 565);
    ritrascritti tutti i 19 gruppi dagli anni singoli dello scan.
  - *Napoli 1936*: 4 celle (tra cui 70-74 F «69 128» → 23 763 e
    85+ M «1 295» → 1 895, da 85-89 M = 1 615 letto «1 015»).
  - *Messina 1871*: 13 celle; il 40-44 T «15 414» → 27 914; colonna M
    provinciale ora riconcilia esattamente col Totale stampato (208 288).
    Restano 3 righe internamente incoerenti nell'originale (residui ≤ ±30,
    es. mesi 3-4 dell'età 0: T 849 vs M+F 819).
  - *Bergamo 1936*: 7 celle (5-9 M «34 108» → 35 008; 4 Totali di gruppo;
    incluse 2 righe ±1 non flaggate); Complesso esatto 605 797 / 294 107 /
    311 690.
  - *Genova 1936*: 5 celle, tutte −60/−600 sul T (30-34 anche M, riga non
    flaggata perché internamente coerente); Complesso, 15-64 e 65-ω esatti
    (867 066 / 420 873 / 446 193).
  - *Pisa 1921* (Tav. XIV, blocco TOTALE provincia a p. 162): 6 celle
    (60-64 T «13 921» → 13 291, trasposizione; 80-84 M/F 971/993 →
    975/989, riga non flaggata); Complesso esatto al netto dell'età
    ignota (360 787 − 2 045 = 358 742 / 181 473 / 179 314).
  - *Roma 1931*: lo scan bypage contiene solo i comuni; verificata invece
    sulla **Tavola VIII (Provincia)** del fascicolo eBiblio
    (`IST0005915Fasc60_ROMA`, pp. 24-28): 4 celle (5-9 F «70 073» →
    78 073; 65-69 T «39 051» → 39 851, entrambe confusioni 0↔8; 85+ F
    via 90-94 F «104» → 194). Controlli «fino a 14», «15-64», «65-ω» e
    In complesso (1 577 115 / 795 545 / 781 570) tornano esattamente.
    Nota: i file 1931 (database Riccardo) escludono sistematicamente la
    riga «100 e oltre» (Roma: 5 / 1 / 4) oltre all'età ignota.
- **Date riferimento**: popolazione *presente* fino al 1921 e nel 1931;
  *residente* nel 1936 (Tav. X) e 1951.
