# Trascrizione riga COMUNE CAPOLUOGO — Tav. 4, censimento 1961

Il PDF (Vol. III, "Dati sommari per comune") contiene la Tav. 4 "Popolazione
residente per sesso e classe di età" di una provincia, con i COMUNI come righe e
una riga finale `PROVINCIA`. Serve la riga del **comune capoluogo**, NON il
totale provinciale.

Gli estratti contengono **solo le sezioni B-MASCHI e C-FEMMINE** (la sezione
A-Totale non è inclusa: il totale si ottiene per somma). Nei file piccoli B e C
possono stare sulla stessa pagina.

## Classi di età — 15, NON quinquennali
In quest'ordine: `Fino a 6`, `6-14`, `14-21`, `21-25`, `25-30`, `30-35`, `35-40`,
`40-45`, `45-50`, `50-55`, `55-60`, `60-65`, `65-70`, `70-75`, `oltre 75`.
Più il **TOTALE** stampato.

Attenzione: sono classi a estremi irregolari (tagli a 6, 14, 21), diverse dalle
quinquennali. Trascrivi esattamente quello che è stampato, senza convertire.

## Procedura
1. Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine).
   Individua le sezioni B-MASCHI e C-FEMMINE.
2. Trova la riga del comune capoluogo. Attenzione a non prendere la riga
   `PROVINCIA` né un comune omonimo.
3. Trascrivi la riga del capoluogo di B e C: 15 valori + TOTALE, per sesso.
4. **Verifica 1:** la somma dei 15 valori deve dare il TOTALE stampato, per sesso.
5. **Verifica 2:** M+F deve coincidere col riferimento fornito nel prompt (è la
   popolazione residente ufficiale del comune al censimento 1961).
6. Se qualcosa non torna o una cifra è dubbia, rileggi la riga da immagine.
   **Il layer di testo dei PDF è inaffidabile: le cifre dubbie vanno sempre
   riviste da immagine.** Ricava le coordinate della riga con `pdftotext -bbox`
   (àncora sul nome o codice del comune) e ritaglia in modo deterministico:
   `pdftoppm -f P -l P -r 300 -png -x 0 -y <px> -W <larghezza> -H 90 "<pdf>" <out>`.
   **NON usare `sips -c H W --cropOffset Y 0`: ritaglia dal centro dell'immagine,
   non dall'offset Y, e finisce silenziosamente sulla riga sbagliata.**
   Le pagine possono essere storte; ritaglia una fascia di ~90 px e riconosci la
   riga giusta dall'ordine di grandezza. Usa nomi file univoci (prefisso città) e
   lavora nella scratchpad.

## Output
Restituisci SOLO questo JSON:
```
{"citta": "<nome>",
 "maschi": {"valori": [15 int], "totale_stampato": int},
 "femmine": {"valori": [15 int], "totale_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int}
```
Non modificare nessun file del repo.
