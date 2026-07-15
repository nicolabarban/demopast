# Trascrizione riga COMUNE CAPOLUOGO — Tav. 3, censimento 1971

Il PDF contiene la Tav. 3 "Popolazione residente per sesso e classe di età" di una
provincia, con i COMUNI come righe (prima colonna: `Codice dei Comuni`) e una riga
finale `TOTALE PROVINCIA`. Serve la riga del **comune capoluogo**, NON il totale
provinciale.

Tre sezioni: **A-Totale**, **B-Maschi**, **C-Femmine**. Ogni sezione è stampata su
DUE pagine affiancate: la prima ha le classi da "Meno di 5" a "50-54", la seconda
da "55-59" a "75 e più" + la colonna Totale + alcune "particolari classi di età"
(Meno di 6, 6-10, 11-13, 14-18, 19-20) **da ignorare**.

Classi da trascrivere (16, in quest'ordine): Meno di 5, 5-9, 10-14, 15-19, 20-24,
25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75 e più,
più il TOTALE stampato.

## Procedura
1. Leggi il PDF con Read (parametro `pages` obbligatorio se >10 pagine). Individua
   le sezioni B-MASCHI e C-FEMMINE.
2. Trova la riga del comune capoluogo. Nei file grandi (Torino, Milano, Roma,
   Napoli) i comuni sono molti: localizza la riga giusta per nome, e attenzione a
   non prendere per errore la riga `TOTALE PROVINCIA` né un comune omonimo.
3. Trascrivi la riga del capoluogo di B e C: 16 valori + TOTALE, per ciascun sesso.
4. **Verifica 1:** la somma dei 16 valori deve dare il TOTALE stampato, per sesso.
5. **Verifica 2:** M+F deve coincidere col riferimento fornito nel prompt (è la
   popolazione residente ufficiale del comune al censimento 1971).
6. **Verifica 3 (gratis):** la sezione A-Totale dà la stessa riga come M+F. Usala
   per il cross-check classe per classe: è il controllo che intercetta gli errori
   che le somme da sole non prendono.
7. Se qualcosa non torna o una cifra è dubbia, rileggi la riga da immagine.
   **Il layer di testo dei PDF è inaffidabile: le cifre dubbie vanno sempre
   riviste da immagine.** Ricava le coordinate della riga con `pdftotext -bbox`
   (àncora sul codice del comune) e ritaglia in modo deterministico:
   `pdftoppm -f P -l P -r 300 -png -x 0 -y <px> -W <larghezza> -H 90 "<pdf>" <out>`.
   **NON usare `sips -c H W --cropOffset Y 0`: ritaglia dal centro dell'immagine,
   non dall'offset Y, e finisce silenziosamente sulla riga sbagliata.**
   Le pagine sono leggermente storte (la riga può scendere di 2-3 pt da sinistra a
   destra): ritaglia una fascia di ~90 px e riconosci la riga giusta dall'ordine di
   grandezza. Le etichette stanno sulla riga SOPRA le cifre, e le pagine sinistra e
   destra hanno offset verticali diversi. Usa nomi file univoci (prefisso città) e
   lavora nella scratchpad.

## Output
Restituisci SOLO questo JSON:
```
{"citta": "<nome>",
 "maschi": {"valori": [16 int], "totale_stampato": int},
 "femmine": {"valori": [16 int], "totale_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int,
 "cross_check_sezione_A": "ok, 16/16" oppure "<descrizione>"}
```
Non modificare nessun file del repo.
