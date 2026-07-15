# Trascrizione COMUNE CAPOLUOGO — Tav. X, censimento 1936

Il PDF `Popby_sex_agegroup_provincia/{Provincia}_1936.pdf` contiene la **TAVOLA X**,
"Popolazione residente secondo l'età, il sesso e lo stato civile", articolata in
sezioni:
- **A) Provincia** (di norma p. 1)
- **B) Comune di {capoluogo}** (di norma p. 2) ← **è questa che serve**
- **C) Comune di …** eventuali altri comuni grandi

Attenzione: qui le **righe sono le classi di età**, non i comuni. Ogni comune ha una
tavola propria. Prendi la sezione **B**, non la **A**.

## Colonne
`IN COMPLESSO` (MF / M / F) + stato civile (Celibi e nubili, Coniugati, Vedovi,
Divorziati, Ignoto) × MF/M/F, per 19 colonne totali. **Servono solo le colonne 2 e 3
di `IN COMPLESSO`: M e F.** Lo stato civile NON serve.

## Righe da trascrivere (82 per sesso, in quest'ordine)
- **anni singoli**: `0`, `1`, `2`, … `74` (75 righe)
- **classi terminali**: `75-79`, `80-84`, `85-89`, `90-94`, `95-99`, `100-ω` (6 righe)
- `Ignota` (1 riga)
- Più il valore della riga `Complesso` (il totale).

In coda alla tavola ci sono i **«Gruppi speciali»** (fino a 5, fino a 9, 6-13, fino a
14, 15-64, 65-ω, 14-17, 18-20, 21-ω): **non trascriverli**, ma **usali come verifica
indipendente** (vedi sotto).

## Verifiche (in ordine di forza)
1. **Somma delle 82 righe = `Complesso`**, per ciascun sesso.
2. **M+F = riferimento** fornito nel prompt (popolazione residente ufficiale del
   comune al 1936).
3. **La colonna `MF` stampata deve valere M+F su ogni riga** — 82 controlli gratis.
4. **Gruppi speciali**: la somma degli anni singoli 15-64 deve dare il gruppo
   speciale `15-64` stampato; la somma di 65-74 + tutte le classi terminali (comprese
   `100-ω` e **escludendo** `Ignota`) deve dare `65-ω`. Sono controlli *indipendenti*
   dalla riga `Complesso` e intercettano errori che la sola somma non prende. Fanne
   almeno due; farli tutti e 9 costa poco e chiude la riga da ogni lato.
   **ATTENZIONE:** `fino a 5` è **inclusivo dell'anno 5** (= anni 0-5), non 0-4. Idem
   `fino a 9` (0-9) e `fino a 14` (0-14). Usare 0-4 produce un falso allarme.

## I CSV di `csv_in_complesso/` sono INUTILIZZABILI — non aprirli
In `1936/csv_in_complesso/` esistono trascrizioni OCR parziali marcate `_INCOMPL`.
**Verificate su 7 città e scartate su tutte e 7: trascrivi dal PDF, ignorali.**
Non sono semplicemente "imprecisi": oltre a valori errati a decine per città, in
alcuni casi **saltano righe**, quindi da una certa età in poi sono disallineati di
una posizione e i valori finiscono sull'età sbagliata. Un incolonnamento per
posizione produrrebbe errori silenziosi e plausibili — il tipo peggiore. Hanno anche
righe rimescolate, colonne M/F invertite, e la prima riga è l'intestazione numerica
letta come dato.

## Metodo
Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine).
**Il layer di testo è inaffidabile.** Questi PDF sono stencil **JBIG2**, una
compressione lossy a dizionario di simboli che **sostituisce cifre visivamente
simili**: renderizzare oltre la risoluzione nativa (300/600 dpi) non aggiunge
informazione, ingrandisce solo l'artefatto. Confusioni ricorrenti: `8→3`, `6→5`,
`0→9`, perdita del separatore delle migliaia (1.152 → 152).
**L'aritmetica è un arbitro migliore dell'occhio**: se una cifra è ambigua, il
residuo rispetto a `Complesso` o a un gruppo speciale la determina spesso in modo
univoco.
Ritaglia con `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H <alt>`,
coordinate da `pdftotext -bbox`. **NON usare `sips --cropOffset`: ritaglia dal centro
dell'immagine e sbaglia riga.** Lavora nella scratchpad con nomi file univoci.

Se una cifra è davvero illeggibile o la fonte si autocontraddice, **dillo**: non
inventare un valore per far quadrare la somma. Distingui errore di lettura, glifo
danneggiato dalla compressione ed errore di stampa, e porta l'evidenza.

## Output
Restituisci SOLO questo JSON (**82** valori per sesso, nell'ordine indicato sopra:
75 anni singoli 0-74, poi le 6 classi terminali, poi `Ignota` come ultimo elemento):
```
{"citta": "<nome>",
 "maschi": {"valori": [82 int], "complesso_stampato": int},
 "femmine": {"valori": [82 int], "complesso_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int,
 "check_gruppi_speciali": "<quali hai verificato e con quale esito>"}
```
Non modificare nessun file del repo.
