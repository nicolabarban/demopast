# Trascrizione riga COMUNE CAPOLUOGO — Tav. 4, censimento 1951

Il PDF (Vol. I, "Dati sommari per comune") contiene la Tav. 4 "Popolazione
residente, per sesso e classi di età" di una provincia, con i COMUNI come righe in
ordine alfabetico e una riga finale `Provincia`. Serve la riga del **comune
capoluogo**, NON il totale provinciale.

Layout: **maschi sulla pagina sinistra, femmine sulla pagina destra**, ciascuna con
le 12 classi + la propria colonna `TOTALE`; a destra c'è anche
`TOTALE POPOLAZIONE RESIDENTE` (M+F).

## Classi di età — 12, IRREGOLARI
In quest'ordine: `fino a 6`, `da 6 a 10`, `da 10 a 14`, `da 14 a 18`, `da 18 a 21`,
`da 21 a 25`, `da 25 a 35`, `da 35 a 45`, `da 45 a 55`, `da 55 a 60`, `da 60 a 65`,
`da 65 in poi`. Più il **TOTALE** stampato per sesso.

Attenzione: classi a estremi irregolari e di ampiezza diseguale (25-35 e 35-45 sono
decennali). Trascrivi esattamente quello che è stampato, senza convertire.

## Procedura
1. Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine).
2. Trova la riga del comune capoluogo. Attenzione a non prendere la riga
   `Provincia` né un comune omonimo.
3. Trascrivi la riga del capoluogo: 12 valori + TOTALE, per ciascun sesso.
4. **Verifica 1:** la somma dei 12 valori deve dare il TOTALE stampato, per sesso.
5. **Verifica 2:** M+F deve coincidere col riferimento fornito nel prompt (è la
   popolazione residente ufficiale del comune al censimento 1951). Se la pagina
   stampa anche `TOTALE POPOLAZIONE RESIDENTE`, quella colonna è un terzo controllo.
6. **Se una riga non chiude, usa il TEST DI CHIUSURA PER COLONNA.** È il controllo
   più potente e va preferito alla sola rilettura visiva: la riga `Provincia` è
   stampata, quindi per ogni colonna vale
   `capoluogo = Provincia − somma degli altri comuni`.
   Ricostruisci la colonna sospetta e ricava il valore implicito del capoluogo.
   Verifica prima che la riga `Provincia` chiuda a sua volta (somma 12 classi =
   suo totale), come controllo del controllo. Questo test ha già smascherato casi
   in cui gli errori erano DUE e la rilettura visiva ne aveva concluso uno solo.
7. **Il layer di testo dei PDF è inaffidabile**: le cifre dubbie vanno sempre
   riviste da immagine. Ricava le coordinate con `pdftotext -bbox` e ritaglia in
   modo deterministico:
   `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H 90 "<pdf>" <out>`.
   **NON usare `sips -c H W --cropOffset Y 0`: ritaglia dal centro dell'immagine,
   non dall'offset Y, e finisce silenziosamente sulla riga sbagliata.**
   Confusioni ricorrenti in questi PDF ricompressi: `8→3`, `6→5`, e la perdita del
   separatore delle migliaia (1.152 letto 152). Le pagine possono essere storte.
   Usa nomi file univoci (prefisso città) e lavora nella scratchpad.
8. Se una cifra è davvero illeggibile o la fonte si autocontraddice, **dillo**: non
   inventare un valore per far quadrare la somma. Distingui sempre fra errore di
   lettura ed errore di stampa, e porta l'evidenza.

## Output
Restituisci SOLO questo JSON:
```
{"citta": "<nome>",
 "maschi": {"valori": [12 int], "totale_stampato": int},
 "femmine": {"valori": [12 int], "totale_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int}
```
Non modificare nessun file del repo.
