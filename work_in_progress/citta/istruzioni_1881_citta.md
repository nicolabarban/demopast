# Trascrizione COMUNE CAPOLUOGO — Tav. I, censimento 1881

File unico per tutte le città:
`1881/VOL2/popby_sex_agegroup_ms_edu_comune.pdf` (214 pagine)

Tav. I, «Popolazione per età, sesso, stato civile e istruzione nei Comuni capoluoghi
di provincia». **Una tabella dedicata per città**, intestata `COMUNE DI <NOME>`, in
ordine alfabetico, **3 pagine per città**. Le righe sono le età.

## Colonne
`STATO CIVILE` (Celibi M/F, Coniugati M/F, Vedovi M/F) | **`COMPLESSO` (M, F, Tot.)**
| `ISTRUZIONE` (Sanno leggere soltanto M/F, Sanno leggere e scrivere M/F,
Analfabeti M/F).
**Servono solo le colonne `COMPLESSO` M e F.** Stato civile e istruzione NON servono.
La colonna `COMPLESSO Tot.` serve come verifica: deve valere M+F su ogni riga.

## ⚠️ Cosa trascrivere — NON serve tutta la tavola
La tavola elenca gli **anni singoli** (`Dalla nascita a 1 anno`, `Da 1 anno compiuto
a 2`, … fino a `99 anni compiuti a 100`), ma **ogni 5 anni stampa anche una riga di
SUBTOTALE QUINQUENNALE** (0-4, 5-9, 10-14, …), di norma in grassetto. **Sono i
subtotali stampati che ci servono**: sommare a mano 100 celle introdurrebbe errori
che la tavola ci risparmia.

Trascrivi, per ciascun sesso:
1. I **primi 5 anni singoli**: età `0` (riga «Dalla nascita a 1 anno»), `1`, `2`, `3`,
   `4` → 5 valori.
2. **I subtotali quinquennali stampati**: `5-9`, `10-14`, `15-19`, `20-24`, `25-29`,
   `30-34`, `35-39`, `40-44`, `45-49`, `50-54`, `55-59`, `60-64`, `65-69`, `70-74`,
   `75-79`, `80-84`, `85-89`, `90-94`, `95-99` → 19 valori, **più il valore `0-4`
   costruito come spiegato qui sotto** → 20 in tutto.

   ⚠️ **ATTENZIONE — verificato su 7 città: il subtotale `0-4` NON è stampato.**
   La riga «Dalla nascita a 1 anno» è tipograficamente staccata e **esclusa** dal
   primo subtotale, che copre **solo 1-4**. Quindi:
   `0-4 = riga «Dalla nascita a 1 anno» + subtotale stampato 1-4` — la somma di **due
   sole celle stampate**, non di cinque. Metti QUESTO valore in `subtotali[0]`, non il
   subtotale 1-4 grezzo: lasciarci 1-4 sottostimerebbe silenziosamente la classe.
   Dal blocco `5-9` in poi i subtotali stampati sono regolarmente quinquennali.
   Riporta anche il valore grezzo del subtotale 1-4 stampato nel campo apposito.
3. `Centenari` → 1 valore.
4. `Età ignota` → 1 valore.

Totale **27 valori per sesso**, in quest'ordine: [0, 1, 2, 3, 4, poi i 20 subtotali
0-4…95-99, poi Centenari, poi Età ignota].

Più il **TOTALE GENERALE** stampato per la città (colonna COMPLESSO, per sesso).

**Se i subtotali quinquennali NON esistono o non coprono tutte le classi, FERMATI e
dillo**: non ricostruirli sommando gli anni singoli senza segnalarlo.

## Verifiche — LEGGI CON ATTENZIONE
Per il 1881 **non esiste un riferimento esterno indipendente**: l'ISTAT non pubblica
la popolazione *presente* ai confini dell'epoca per questo censimento (il *residente*
del volume di riferimento è un concetto diverso e NON è confrontabile — per Napoli
differisce del 2,7%). La verifica è quindi tutta **interna**, e va fatta tutta:

1. **Gli anni singoli 1..4 devono sommare al subtotale `1-4` stampato**, per sesso
   (NON 0..4: vedi l'avvertenza sopra). È il controllo che valida entrambe le letture.
2. **La somma dei 20 subtotali + Centenari + Età ignota = TOTALE GENERALE stampato**,
   per sesso.
3. **La colonna `COMPLESSO Tot.` = M+F** su ogni riga che trascrivi.
4. Il prompt ti dà un valore *indicativo* (residente, concetto diverso): serve solo a
   escludere di aver preso la città sbagliata. **Non è un checksum**: uno scarto di
   qualche punto percentuale è atteso e NON va corretto.

## Metodo
Leggi il PDF con Read (il parametro `pages` è obbligatorio: il file ha 214 pagine).
**Il layer di testo è inaffidabile**: `pdftotext` estrae molto testo ma con cifre
corrotte ricorrenti (`196!` per 1964, `i945` per 1945, `2<109`, `lO` per 10) e
allineamento delle colonne perso. Usalo per navigare, non per trascrivere.
Questi PDF sono stencil **JBIG2**, compressione lossy a dizionario di simboli che
**sostituisce cifre visivamente simili**: renderizzare oltre la risoluzione nativa
non aggiunge informazione, ingrandisce solo l'artefatto. Confusioni ricorrenti:
`8→3`, `6→5`, `0→9`, perdita del separatore delle migliaia.
**L'aritmetica è un arbitro migliore dell'occhio.**
Ritaglia con `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H <alt>`,
coordinate da `pdftotext -bbox`. **NON usare `sips --cropOffset`: ritaglia dal centro
dell'immagine e sbaglia riga.** Lavora nella scratchpad con nomi file univoci.

Se una cifra è illeggibile o la fonte si autocontraddice, **dillo**: non inventare un
valore per far quadrare la somma.

## Output
Restituisci SOLO questo JSON:
```
{"citta": "<nome>",
 "maschi": {"singoli_0_4": [5 int], "subtotale_1_4_stampato": int,
            "subtotali": [20 int], "centenari": int,
            "eta_ignota": int, "totale_stampato": int},
 "femmine": {"singoli_0_4": [5 int], "subtotale_1_4_stampato": int,
             "subtotali": [20 int], "centenari": int,
             "eta_ignota": int, "totale_stampato": int},
 "verifica_singoli_vs_subtotale_0_4": "<esito, per sesso>",
 "verifica_somma_vs_totale": "<esito, per sesso>",
 "totale_letto": int,
 "pagine": "<pagine PDF usate>"}
```
Non modificare nessun file del repo.
