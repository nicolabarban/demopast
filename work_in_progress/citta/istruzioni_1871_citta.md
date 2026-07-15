# Trascrizione COMUNE CAPOLUOGO — Tav. II, censimento 1871

File unico per tutte le città:
`1871/Censimento generale della popolazione 1871/VOL2/popby_sex_agegroup_ms_edu_comune.pdf`
(123 pagine PDF, ma ogni pagina è una **scansione a doppia facciata** → ~241 facciate
stampate)

Tav. II, «Comuni capoluoghi di provincia: popolazione per età, sesso, stato civile e
istruzione». **Una tabella dedicata per città**, intestata `COMUNE DI <NOME>`, in
ordine alfabetico, ~3,5 facciate per città (le grandi 5-6). Il nome della città
compare nel *running header* di ogni pagina — **usalo per confermare di essere sulla
città giusta**, perché le tabelle scorrono di continuo e una nuova città può iniziare
a metà facciata.

## Colonne
`TOTALE` (complessivo, **M**, **F**) | `STATO CIVILE` (Celibi M/F, Coniugati M/F,
Vedovi M/F) | `ISTRUZIONE` (Sanno leggere M/F, Non sanno leggere M/F).
**Servono solo le colonne `TOTALE` M e F.** Stato civile e istruzione NON servono.
La colonna `TOTALE` complessivo serve come verifica: deve valere M+F su ogni riga.

## Righe da trascrivere (112 per sesso)
1. **Primo anno di vita, per MESI** (12 righe): `da 0 mesi a 1`, `1 a 2`, `2 a 3`, …
   `11 a 12`.
2. **Anni singoli** (99 righe): `1 anno a 2`, `2 a 3`, `3 a 4`, … `99 a 100`.
3. `Centenari` (1 riga).
4. **`Età ignote`, SE presente** (1 riga). ⚠️ Non tutte le città ce l'hanno — Venezia
   sì (M 25 / F 16), Firenze no. Quando c'è, **è inclusa nel `Totale..` stampato ma
   sta fuori dalle 112 righe di età**: registrala nel campo apposito, e ricorda che
   allora `somma 112 righe = Totale.. − Età ignote`. Se non c'è, metti 0.

Più il valore della riga `Totale..` (il totale della città), per sesso.

⚠️ **Nota sul `Totale..` con richiamo**: se la riga finale è stampata `Totale (1)` o
simile, **cerca la nota a piè di facciata**: può dichiarare persone escluse dal
totale. Livorno è il caso noto — 49 maschi «dei quali non si conoscono l'età, nè lo
stato civile, nè l'istruzione» sono esclusi dal totale della tavola ma inclusi nei
riepiloghi generali del Regno, per cui il totale stampato (97.047) sta 49 sotto il
riferimento ufficiale (97.096). **Non è un errore: riportalo e spiegalo.**

**Se la tavola stampa anche dei subtotali quinquennali, DILLO subito**: cambierebbe
il metodo (sarebbe molto meglio prendere quelli). Da una ricognizione preliminare
NON risultano, ma verificalo.

## ⚠️ Attenzione a due insidie
- **Le facciate destre sono spesso più sbiadite** delle sinistre: la stessa città può
  avere metà tabella nitida e metà no.
- Una ricognizione preliminare, su Roma, ha letto un totale di **50.657**, che è
  palesemente sbagliato (Roma nel 1871 aveva ~244.000 abitanti): probabilmente aveva
  letto una sola facciata di una tabella che ne occupa diverse, o una colonna
  parziale. **Assicurati di aver coperto TUTTE le facciate della città** e che la
  riga `Totale..` sia quella finale della città, non un totale di colonna intermedio.

## Verifiche (in ordine di forza)
1. **M+F = riferimento** fornito nel prompt. Per il 1871 il riferimento **è
   ufficiale** (popolazione presente ai confini dell'epoca, dal volume ISTAT), quindi
   è un checksum vero — a differenza del 1881 e del 1921. Deve tornare all'unità.
2. **Somma delle 112 righe = `Totale..` stampato**, per ciascun sesso.
3. **La colonna `TOTALE` complessivo = M+F** su ogni riga.
4. **Appendice a p. 121 (facciata 240)**: `APPENDICE ALLA TAVOLA PER ETÀ` riporta i
   totali dei nati nel primo anno per ciascun capoluogo → verifica indipendente della
   somma delle tue 12 righe mensili. Usala.

## Metodo
Leggi il PDF con Read (il parametro `pages` è obbligatorio: 123 pagine).
**Il layer di testo è inaffidabile.** Questi PDF sono stencil **JBIG2**, compressione
lossy a dizionario di simboli che **sostituisce cifre visivamente simili**:
renderizzare oltre la risoluzione nativa non aggiunge informazione, ingrandisce solo
l'artefatto. Confusioni ricorrenti: `8→3`, `6→5`, `0→9`, perdita del separatore delle
migliaia. **L'aritmetica è un arbitro migliore dell'occhio.**
Ritaglia con `pdftoppm -f P -l P -r 600 -png -x 0 -y <px> -W <larghezza> -H <alt>`,
coordinate da `pdftotext -bbox`. **NON usare `sips --cropOffset`: ritaglia dal centro
dell'immagine e sbaglia riga.** Lavora nella scratchpad con nomi file univoci.

Se una cifra è illeggibile o la fonte si autocontraddice, **dillo**: non inventare un
valore per far quadrare la somma. Distingui errore di lettura, glifo danneggiato dalla
compressione ed errore di stampa, e porta l'evidenza.

## Output
Restituisci SOLO questo JSON:
```
{"citta": "<nome>",
 "maschi": {"mesi": [12 int], "singoli": [99 int], "centenari": int,
            "eta_ignote": int, "totale_stampato": int},
 "femmine": {"mesi": [12 int], "singoli": [99 int], "centenari": int,
             "eta_ignote": int, "totale_stampato": int},
 "nota_totale": "<testo della nota a piè di pagina se il Totale ha un richiamo, altrimenti null>",
 "verifica_somme": "ok" oppure "problemi: <descrizione>",
 "delta_vs_ref": int,
 "check_appendice": "<esito del confronto con l'appendice di p. 121, o perche' non fatto>",
 "subtotali_quinquennali": "<presenti? se si', dillo>",
 "pagine": "<facciate usate>"}
```
`singoli[0]` è l'età 1 (riga «1 anno a 2»), `singoli[98]` è l'età 99.
Non modificare nessun file del repo.
