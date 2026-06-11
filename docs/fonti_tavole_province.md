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
- **Date riferimento**: popolazione *presente* fino al 1921 e nel 1931;
  *residente* nel 1936 (Tav. X) e 1951.
