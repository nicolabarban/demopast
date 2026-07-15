# Trascrizione riga provinciale — Tav. 3, censimento 1971 (Vol. II, dati comunali)

Il PDF contiene la Tav. 3 "Popolazione residente per sesso e classe di età" di una
provincia: tre sezioni (A-Totale, B-Maschi, C-Femmine), comuni per righe. Ogni
sezione è stampata su DUE pagine affiancate: la prima ha le classi da "Meno di 5"
a "50-54", la seconda le classi da "55-59" a "75 e più" + la colonna Totale +
alcune "particolari classi di età" (Meno di 6, 6-10, 11-13, 14-18, 19-20) DA IGNORARE.
L'ultima riga di ogni sezione è il totale provinciale (etichettata col NOME DELLA
PROVINCIA in maiuscolo, es. "VALLE D'AOSTA").

Classi da trascrivere (16, in quest'ordine): Meno di 5, 5-9, 10-14, 15-19, 20-24,
25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75 e più,
più il TOTALE stampato.

1. Leggi il PDF con Read (parametro pages se >10 pagine). Individua le sezioni
   B-MASCHI e C-FEMMINE (ignora la sezione A-Totale).
2. Trascrivi la riga provinciale di B e C: 16 valori + TOTALE, per ciascun sesso.
3. Verifica: la somma dei 16 valori DEVE dare il TOTALE stampato, per ciascun sesso.
4. Se non torna o una cifra è dubbia: renderizza la pagina con
   `pdftoppm -f P -l P -r 300 -png "<pdf>" <out>` e ritaglia la fascia della riga
   provinciale con `sips -c ALTEZZA LARGHEZZA --cropOffset Y 0 file.png --out crop.png`,
   poi rileggi il ritaglio con Read. USA NOMI FILE UNIVOCI (prefisso provincia).
5. Restituisci SOLO questo JSON:
{"provincia": "<nome>",
 "maschi": {"valori": [16 int], "totale_stampato": int},
 "femmine": {"valori": [16 int], "totale_stampato": int},
 "verifica_somme": "ok" oppure "problemi: <descrizione>"}
