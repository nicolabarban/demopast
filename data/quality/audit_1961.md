# Audit censimento 1961 — verifica errori del sorgente

*Verifica del 2026-07-13. Metodo: (1) coerenza interna `male+female == total` su ogni riga;
(2) confronto dei totali provinciali (somma delle 19 classi di età) con la popolazione
residente ufficiale al censimento del 15/10/1961 (fonte: tuttitalia.it su dati ISTAT,
solo province con confini invariati dal 1961).*

Il file sorgente (`downloads/1961/data_census_1961_adjusted_age.csv`) ha **161 righe
incoerenti** (M+F≠T) concentrate in 26 province. Il confronto esterno mostra che il
danno reale è più esteso dei flag interni: in alcune province anche le righe
internamente coerenti sono sbagliate.

## Classe A — corruzione grave, ri-estrazione necessaria (9 province)

Entrambe le colonne (T e M+F) sono lontane dal totale ufficiale: la digitalizzazione
è inaffidabile su tutta la tabella, non solo nelle righe flaggate.

| COD | Provincia | Ufficiale 1961 | sum(T) | Δ% | sum(M+F) | Δ% | righe M+F≠T |
|----:|-----------|---------------:|-------:|---:|---------:|---:|----:|
| 006 | Alessandria | 478.613 | 438.961 | −8,3% | 445.495 | −6,9% | 13 |
| 012 | Varese      | 581.528 | 532.766 | −8,4% | 519.617 | −10,6% | 13 |
| 017 | Brescia     | 882.949 | 866.162 | −1,9% | 824.465 | −6,6% | 9 |
| 023 | Verona      | 667.517 | 611.195 | −8,4% | 643.433 | −3,6% | 10 |
| 024 | Vicenza     | 615.507 | 536.469 | −12,8% | 552.876 | −10,2% | 13 |
| 036 | Modena      | 511.355 | 473.060 | −7,5% | 462.737 | −9,5% | 13 |
| 038 | Ferrara     | 403.218 | 359.964 | −10,7% | 354.276 | −12,1% | 14 |
| 056 | Viterbo     | 263.862 | 243.693 | −7,6% | 245.439 | −7,0% | 11 |
| 064 | Avellino    | 463.671 | 432.918 | −6,6% | 422.037 | −9,0% | 13 |

Sul sito: per queste province **tutto è inattendibile** (choropleth, piramide, indici).

## Classe B — totale (T) corretto, M/F corrotti (3 province)

sum(T) coincide (quasi) esattamente con l'ufficiale; gli errori stanno nelle colonne
per sesso. Esempio diagnostico: Palermo età 0 ha T=23.390 e M+F=2.339 — M e F hanno
perso l'ultima cifra (11.930+11.460=23.390).

| COD | Provincia | Ufficiale 1961 | sum(T) | Δ% | sum(M+F) | Δ% | righe M+F≠T |
|----:|-----------|---------------:|-------:|---:|---------:|---:|----:|
| 082 | Palermo | 1.111.397 | 1.111.397 | 0,0% | 1.025.114 | −7,8% | 8 |
| 073 | Taranto | 468.713 | 468.713 | 0,0% | 456.086 | −2,7% | 4 |
| 010 | Genova  | 1.031.091 | 1.030.835 | −0,0% | 1.015.418 | −1,5% | 4 |

Sul sito: choropleth per totali e indici basati su T (old_dep, struct_dep, mean_age)
sostanzialmente ok; **piramidi e CWR sbagliati** nelle classi di età colpite.

## Classe C — scarti minimi, verosimilmente arrotondamenti (14 province)

Torino (+0,4%), Cuneo (+0,8%), Trapani (−0,3%) verificate contro l'ufficiale; Vercelli,
Novara, Valle d'Aosta, Imperia, Treviso, Parma, Ravenna, Forlì, Macerata, Chieti,
Brindisi hanno delta interni piccoli (da ±1 a ±5.247). Le righe con delta ≤ ~200 sono
compatibili con arrotondamenti della ridistribuzione per età ("adjusted age"); quelle
con delta in migliaia (es. Vercelli 80-84: T=66 vs M+F=6.600) sono refusi puntuali di
digitalizzazione, in gran parte ricostruibili dalla riga stessa.

## Classe D — errori nascosti (province internamente coerenti)

Il check M+F=T non basta: **Padova** è internamente coerente ma supera l'ufficiale di
esattamente +2.000 (694.017 vs 696.017), **Napoli** di +932. Errori di battitura
compensati su tutte e tre le colonne. Venezia e Bologna invece coincidono (0 / −18).

## Raccomandazioni

1. Le 9 province di classe A vanno ri-estratte dal volume originale ISTAT 1961
   (approccio "print-exact" già usato per 1861 e 1901), oppure rimosse dal CSV finché
   non corrette (renderebbero come province senza dati, già previsto per le 6 mancanti).
2. Per la classe B basta ri-estrarre le colonne M/F delle righe flaggate.
3. `data/quality/riferimento_1961_totali_ufficiali.csv` contiene i 19 totali ufficiali
   raccolti, utilizzabili come vincolo di verifica dopo le correzioni.
