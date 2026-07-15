# Trascrizione COMUNE CAPOLUOGO — Tav. XIV, censimento 1921

I PDF stanno in `1921/Popby_sex_agegroup_circondiari/{Regione}_1921.pdf`, **uno per
regione**. Il nome della cartella inganna: la **Tavola XIV** affianca più livelli
geografici, non solo il circondario. Titolo completo:

> «Popolazione presente classificata secondo il sesso e l'età **nei Centri di almeno
> 15 000 abitanti, nei Comuni capiluoghi di Circondario, nei Circondari, nelle
> Provincie e nella Regione**.»

**Devi prendere la colonna sotto l'intestazione `COMUNI CAPILUOGHI DI CIRCONDARIO`.**

## ⚠️ Il tranello principale: CENTRO ≠ COMUNE
La tavola ha anche una colonna `CENTRI` (nuclei urbani di almeno 15.000 abitanti),
che per le grandi città è **diversa e più piccola** del comune. Esempio verificato:
Roma **centro** 656.266, Roma **comune** 691.661. Se prendi la colonna sbagliata il
numero è plausibile ma sbagliato. Verifica l'intestazione, non l'ordine di grandezza.
Non prendere nemmeno le colonne `CIRCONDARI`, `PROVINCIE`, `REGIONE`.

## Righe (39 per sesso, in quest'ordine)
- **anni singoli**: `fino a 1`, `1-2`, `2-3`, … `19-20`, `20-21` (21 righe)
- **quinquenni**: `21-25`, `25-30`, `30-35`, `35-40`, `40-45`, `45-50`, `50-55`,
  `55-60`, `60-65`, `65-70`, `70-75`, `75-80`, `80-85`, `85-90`, `90-95`, `95-100`
  (16 righe)
- `oltre 100` (1 riga)
- `ignota` (1 riga)

Più il valore della riga `In complesso` (il totale della città).

Ogni classe è ripartita in **MF / M / F**: servono **M** e **F**; `MF` serve come
verifica (deve valere M+F su ogni riga).

Il dato è **popolazione PRESENTE** (de facto), non residente.

## Verifiche — LEGGI CON ATTENZIONE
Per il 1921 **non esiste un riferimento esterno indipendente**: l'ISTAT non pubblica
la popolazione *presente* ai confini dell'epoca per questo censimento. La verifica si
appoggia quindi ai soli controlli **interni** alla tavola, che vanno fatti TUTTI:

1. **Somma delle 39 righe = `In complesso`**, per ciascun sesso.
2. **La colonna `MF` stampata = M+F su ogni riga** — 39 controlli.
3. **`In complesso` MF = `In complesso` M + `In complesso` F.**
4. Il prompt ti dà un valore *atteso indicativo*: è un ordine di grandezza o una
   lettura preliminare non verificata, **non** un checksum ufficiale. Se il tuo
   totale diverge, non forzare nulla: riporta quello che leggi e segnala lo scarto.

Questo rende il 1921 meno garantito degli altri anni: **sii particolarmente
scrupoloso** e dichiara esplicitamente quali controlli hai fatto e quali no.

**Nota sulla rettifica**: i dati del 1921 furono in seguito rettificati per le
province meridionali e insulari (Bari, Napoli, Palermo, Messina, Catania). La tavola
riporta la popolazione **rilevata al censimento**, non quella rettificata. Non
tentare correzioni.

## Metodo
Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine).
**Il layer di testo è inaffidabile** (`13437` → `l3437`, `2461` → `246l`, confusioni
0/O e 1/l/I frequenti): serve per NAVIGARE e trovare la pagina, non per trascrivere.
Questi PDF sono stencil **JBIG2**, compressione lossy a dizionario di simboli che
**sostituisce cifre visivamente simili**: renderizzare oltre la risoluzione nativa
(300/600 dpi) non aggiunge informazione, ingrandisce solo l'artefatto. Confusioni
ricorrenti: `8→3`, `6→5`, `0→9`, perdita del separatore delle migliaia.
**L'aritmetica è un arbitro migliore dell'occhio**: se una cifra è ambigua, il residuo
rispetto a `In complesso` o alla colonna `MF` la determina spesso in modo univoco.
Ritaglia con `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H <alt>`,
coordinate da `pdftotext -bbox`. **NON usare `sips --cropOffset`: ritaglia dal centro
dell'immagine e sbaglia riga.** Lavora nella scratchpad con nomi file univoci.

Se una cifra è illeggibile o la fonte si autocontraddice, **dillo**: non inventare un
valore per far quadrare la somma.

## Output
Restituisci SOLO questo JSON (39 valori per sesso, `ignota` come ultimo elemento):
```
{"citta": "<nome>",
 "maschi": {"valori": [39 int], "in_complesso_stampato": int},
 "femmine": {"valori": [39 int], "in_complesso_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "totale_letto": int,
 "scarto_vs_atteso": int,
 "colonna_presa": "<conferma di aver preso COMUNI CAPILUOGHI e non CENTRI, e come l'hai stabilito>"}
```
Non modificare nessun file del repo.
