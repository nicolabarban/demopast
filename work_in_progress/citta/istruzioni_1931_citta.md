# Trascrizione COMUNE CAPOLUOGO — Tav. IX, censimento 1931

Il PDF `popby_sex_age_ms_comune/{Provincia}_1931.pdf` contiene la **Tavola IX**,
"Popolazione presente secondo l'età, il sesso e lo stato civile". Ogni comune è un
**blocco tabellare separato**, intestato `Comune di X`; le **righe sono le età**.
Il **comune capoluogo è sempre il primo blocco di pagina 1**.

Non ci sono tutti i comuni della provincia: solo i capoluoghi di ex circondario e i
comuni con un centro ≥10.000 abitanti (nota a piè di pagina). I blocchi successivi
sono comuni minori: non confonderli col capoluogo.

## Colonne
22 colonne: col. 1 = età, poi 7 blocchi da 3 (MF/M/F): `In complesso`, `Celibi e
nubili`, `Coniugati`, `Vedovi`, `Separati legalmente`, `Divorziati`, `Ignoto`.
**Servono solo le colonne 3 e 4** (`In complesso` M e F). Lo stato civile NON serve.
La colonna 2 (`In complesso` MF) serve come verifica: deve valere M+F su ogni riga.

## Righe da trascrivere (39 per sesso, in quest'ordine)
- **anni singoli**: `0`, `1`, `2`, … `14` (15 righe)
- **anni singoli**: `15`, `16`, `17`, `18`, `19`, `20` (6 righe)
- **classi**: `21-24`, `25-29`, `30-34`, `35-39`, `40-44`, `45-49`, `50-54`, `55-59`,
  `60-64` (9 righe)
- **classi**: `65-69`, `70-74`, `75-79`, `80-84`, `85-89`, `90-94`, `95-99`,
  `100 e oltre` (8 righe)
- `Età ignota` (1 riga)

Più il valore della riga `In complesso` (il totale della città).

**NON trascrivere i subtotali** — la tavola stampa `fino a 14 anni`, `da 15 a 64
anni` e `65 anni - ω` fra le righe: servono come verifica, non come dato.

## Verifiche (in ordine di forza)
1. **Somma delle 39 righe = `In complesso`**, per ciascun sesso.
2. **M+F = riferimento** fornito nel prompt.
3. **La colonna `MF` stampata deve valere M+F su ogni riga** — 39 controlli gratis.
4. **Subtotali stampati**: gli anni singoli 0-14 devono dare `fino a 14 anni`; le
   righe da 15 a 60-64 devono dare `da 15 a 64 anni`; le 8 classi da 65-69 a
   `100 e oltre` devono dare `65 anni - ω`. Sono controlli *indipendenti* dalla riga
   `In complesso` e localizzano l'errore in un terzo di tavola. Falli tutti e tre.

## Metodo
Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine).
**Il layer di testo è inaffidabile** (su questa tavola è tipicamente illeggibile:
`pdftotext` restituisce spazzatura tipo `~• . • ~J53·`). Questi PDF sono stencil
**JBIG2**, una compressione lossy a dizionario di simboli che **sostituisce cifre
visivamente simili**: renderizzare oltre la risoluzione nativa (300/600 dpi) non
aggiunge informazione, ingrandisce solo l'artefatto. Confusioni ricorrenti: `8→3`,
`6→5`, `0→9`, perdita del separatore delle migliaia.
**L'aritmetica è un arbitro migliore dell'occhio**: se una cifra è ambigua, il
residuo rispetto a `In complesso`, alla colonna `MF` o a un subtotale la determina
spesso in modo univoco.
Ritaglia con `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H <alt>`,
coordinate da `pdftotext -bbox`. **NON usare `sips --cropOffset`: ritaglia dal centro
dell'immagine e sbaglia riga.** Lavora nella scratchpad con nomi file univoci.

Se una cifra è davvero illeggibile o la fonte si autocontraddice, **dillo**: non
inventare un valore per far quadrare la somma. Distingui errore di lettura, glifo
danneggiato dalla compressione ed errore di stampa, e porta l'evidenza.

## Output
Restituisci SOLO questo JSON (39 valori per sesso, nell'ordine indicato sopra, con
`Età ignota` come ultimo elemento):
```
{"citta": "<nome>",
 "maschi": {"valori": [39 int], "in_complesso_stampato": int},
 "femmine": {"valori": [39 int], "in_complesso_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int,
 "check_subtotali": "<esito dei tre subtotali, per sesso>"}
```
Non modificare nessun file del repo.
