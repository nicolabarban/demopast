# Tabella per città — popolazione per età e sesso, 13 grandi città

Completata il 2026-07-15 (8 anni); estesa il 2026-07-29 con 1901 e 1911.
**13 città × 10 anni di censimento = 130 tavole trascritte**, tutte verificate.
Prodotto finale: `downloads/citta/data_census_citta.csv`
(2.470 righe = 130 × 19 gruppi di età).

Città: Torino, Milano, Venezia, Genova, Bologna, Firenze, Livorno, Roma, Napoli,
Bari, Palermo, Messina, Catania. Il `code` è il COD_PROV della provincia di cui la
città è capoluogo, così la tabella si unisce a quella provinciale.

## Anni: 10 su 11
1871, 1881, 1901, 1911, 1921, 1931, 1936, 1951, 1961, 1971. Escluso solo il
**1861**: non esiste — l'ISTAT dell'epoca pubblica l'età solo per provincia.
(La ricognizione iniziale aveva scartato anche 1901 e 1911 per errore: il 1901
è per coorte di nascita e si converte in età quasi esattamente, e il Vol. II
del 1911 ha le sezioni comunali con anni singoli — vedi
`docs/fonti_tavole_citta.md`, aggiornato.)

## Qualità del dato, anno per anno

| Anno | Concetto | Armonizzazione sui 19 gruppi | Riferimento esterno |
|------|----------|------------------------------|---------------------|
| 1871 | presente | **esatta** (anni singoli) | ✓ ufficiale, delta 0 su 13/13 |
| 1881 | presente | **esatta** (subtotali stampati) | ✗ assente |
| 1901 | presente | **quasi esatta** (coorti; stimato solo il confine 15-19/20-24) | ✓ totali M/F/M+F stampati, delta 0 su 13/13 |
| 1911 | presente | **esatta** (anni singoli 0-21 + quinquenni) | ✓ totali stampati, delta 0 su 13/13; Torino via totale comune 427.106 |
| 1921 | presente | **esatta** (anni singoli 0-20 + quinquenni) | ✗ solo Torino |
| 1931 | presente | **esatta** (anni singoli 0-20 + classi) | ✓ ufficiale, delta 0 su 13/13 |
| 1936 | residente | **esatta** (anni singoli 0-74) | ✓ ufficiale, delta 0 su 13/13 |
| 1951 | residente | **stimata** (12 classi irregolari) | ✓ ufficiale, delta 0 su 13/13 |
| 1961 | residente | **stimata** (15 classi irregolari) | ✓ ufficiale, delta 0 su 13/13 |
| 1971 | residente | **stimata** (`<5` e `75+` aperte) | ✓ ufficiale, delta 0 su 13/13 |

**Attenzione al cambio di concetto**: 1871-1931 è popolazione *presente* (de facto),
1936-1971 *residente*. Non sono la stessa cosa — per Roma 1921 il presente supera il
residente del 4,2%. Confrontare 1931 e 1936 significa confrontare due concetti diversi.

**Le classi stimate**: per 1951, 1961 e 1971 le classi originali non si allineano ai
19 gruppi. `assembla_citta.py` le redistribuisce sugli anni singoli usando come forma
il profilo per età della **provincia della città nello stesso anno** (che i 19 gruppi
li ha), con largest-remainder. Nessun individuo entra o esce da una classe originale:
la redistribuzione avviene solo *dentro* ciascuna classe stampata. Per il 1971 sono
stimate solo `0`, `1-4`, `75-79`, `80-84`, `85+`; per 1951 e 1961 l'effetto è più
diffuso perché i tagli originali (6, 14, 18, 21) attraversano i quinquenni.

**Età ignota**: le persone senza età dichiarata non appartengono ad alcuna classe e
restano fuori dai 19 gruppi. Sono poche ovunque tranne il 1921 (25.238 sulle 13
città, per lo più Roma e Napoli) e, in misura minore, il 1911 (8.807, di cui
4.946 a Napoli e 1.748 a Roma). Il totale della città dai 19 gruppi è quindi
leggermente sotto il totale stampato dove la riga esiste.

## Insidie della fonte, tutte verificate

- **1921, centro ≠ comune**: la Tav. XIV affianca *centri*, *comuni capoluoghi*,
  *circondari*, *province*. Su Firenze la colonna CENTRI (247.791) era **più vicina**
  al valore atteso del comune (253.565): fidarsi dell'ordine di grandezza avrebbe
  fatto prendere la colonna sbagliata con un numero plausibile.
- **1871, running header ingannevole**: le tabelle scorrono e l'intestazione anticipa
  o ritarda. Il totale di 50.657 letto per Roma in ricognizione era **Reggio Emilia**.
  Ogni città è stata ancorata a «COMUNE DI \<nome\>» e alla propria riga «Totale..».
- **1881, il subtotale 0-4 non esiste**: la riga «Dalla nascita a 1 anno» è staccata
  ed esclusa dal primo subtotale, che copre solo 1-4. Assumerlo 0-4 perderebbe l'intera
  coorte dei lattanti (5.427 maschi a Napoli).
- **1931, Catania fuori data**: nota a stampa — «I dati del Comune di Catània si
  riferiscono al 22 novembre 1931-X», sette mesi dopo il censimento generale del 21
  aprile. **Non è perfettamente comparabile con le altre 12.**
- **1871, Livorno**: il totale stampato esclude 49 maschi «dei quali non si conoscono
  l'età, nè lo stato civile, nè l'istruzione», dichiarati in nota.
- **1951, Messina**: il suo PDF manca dagli estratti; letta dal fascicolo completo.

## Errata: due valori divergono deliberatamente dalla carta
Entrambi su Roma, entrambi errori del tipografo provati da riscontri multipli
indipendenti, entrambi registrati col valore **corretto**:
- **1961, femmine 60-65**: stampato 46.753, vero **47.753** (quattro chiusure).
- **1881, femmine «Età ignota»**: stampato 325, vero **326** (tre riscontri).

## Anomalia reale, non un errore
**Catania -9,1% e Palermo -0,8% fra 1921 e 1931.** Non è un problema di trascrizione:
lo stesso calo compare nel volume ufficiale ISTAT, fonte indipendente (residente:
Catania 251.618 → 225.169, -10,5%; Palermo 393.519 → 379.905, -3,5%). È il noto
**sovraconteggio del censimento 1921 nelle province meridionali e insulari**, che fu
rettificato in seguito: le tavole riportano il dato *rilevato*, non quello rettificato.
Vale per Bari, Napoli, Palermo, Messina e Catania.

## Metodo — la lezione che conta
**L'aritmetica batte l'occhio.** Questi PDF sono stencil **JBIG2**, una compressione
lossy a *dizionario di simboli* che **sostituisce cifre visivamente simili**: per
questo rileggere a 1200 o 2400 dpi non serve — ingrandisce l'artefatto. Su Torino 1951
il totale maschile si legge `333.227` a qualsiasi risoluzione, ma vale **338.227**.
Le tavole però stampano ridondanza (totali di riga, colonna MF, subtotali, riga
PROVINCIA), e quella ridondanza determina la cifra vera in modo univoco.
Confusioni ricorrenti: `8→3`, `6→5`, `0→9`, `4→1`, e la perdita del separatore delle
migliaia.

Il controllo più potente si è rivelato il **test di chiusura per colonna**: dove è
stampata la riga PROVINCIA, vale `città = PROVINCIA − somma degli altri comuni`, che
ricostruisce il valore **senza leggere la riga**. Su Firenze 1961 ha rivelato che gli
errori erano *due*, non uno — la rilettura visiva da sola aveva concluso, sbagliando,
che fosse un errore di stampa in una cella sola.

## Rigenerare
```bash
python3 work_in_progress/citta/assembla_citta.py   # -> downloads/citta/data_census_citta.csv
```
Richiede `data/census/census_{1951,1961,1971}.csv` come donatori di forma.
Lo script scrive gli 8 anni originali e poi richiama `assembla_1901_1911.py`,
che aggiunge 1901 e 1911 dalle rispettive trascrizioni (può anche essere
lanciato da solo: fa il merge sul CSV esistente).

Nota 1901: la tavola è per anno di nascita; la conversione in età al 10 feb
1901 assegna i nati 1901+1900 all'età 0, 1899-1896 a 1-4, ecc. L'unico gruppo
a cavallo dei quinquenni è 1882-80 (età 18-19-20), splittato tra 15-19 e 20-24
con le proporzioni per anno singolo della stessa città al 1911.
Nota 1911: la scansione di Torino è tagliata dopo «Oltre 100»; le righe Ignota
e Totale sono ricostruite dal totale presente del comune (427.106).

## Resto provincia
`genera_resto_provincia.py` produce
`downloads/citta/data_census_resto_provincia.csv`: provincia − comune
capoluogo, cella per cella sui 19 gruppi, per i 10 anni del pannello
(colonne: `year, code, province, city_excluded, age_class, male, female,
total`). Nessuna cella negativa. Tre celle ereditano un'incoerenza
m+f ≠ total già presente nella fonte provinciale (1911 Napoli 70-74 delta +7;
1921 Venezia 10-14 −360; 1921 Firenze 5-9 −200). Una quarta — 1936 Catania
1-4, delta +8.202 — è stata **corretta alla fonte** il 2026-07-29: nel CSV
d'archivio l'età 1 M era scritta «8,202» con la virgola e il parser l'aveva
scartata (stesso difetto per Cosenza età 38, totale «6,130»); entrambe
verificate sulla tavola stampata e corrette in `downloads/1936/`. Le
annessioni comunali degli
anni '20-'30 (Grande Milano, Napoli, Roma…) creano discontinuità nel resto:
sono cambi di confine, non errori.

## Cosa c'è qui
- `trascrizioni_{anno}_citta.json` — trascrizioni grezze, con le classi originali
  della fonte e le note/errata per anno.
- `ref_citta.json` — riferimento di verifica (ISTAT ed. 1977 **tomo 2**, «confini
  dell'epoca»; il tomo 1 è ricalcolato ai confini 1971 e come checksum sarebbe
  fuorviante — Genova 1921: 304.108 contro 541.562).
- `istruzioni_{anno}_citta.md` — prompt usati dagli agenti di trascrizione.
- `assembla_citta.py` — armonizzazione sui 19 gruppi.
