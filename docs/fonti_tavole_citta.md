# Fonti per le 13 grandi città — popolazione per età e sesso

Ricognizione del 2026-07-15 sull'archivio OneDrive UniBo (cartella condivisa
L. Lionello, `Lorenzo Lionello's files - Censimenti/`). Città considerate:
Torino, Milano, Venezia, Genova, Bologna, Firenze, Livorno, Roma, Napoli, Bari,
Palermo, Messina, Catania.

Ogni riga è stata verificata aprendo i PDF e confrontando il totale letto con la
popolazione nota del **comune** — il rischio ricorrente in queste tavole è
scambiare il comune per il circondario o la provincia, che sono molto più grandi.

## Quadro per anno

| Anno | Città | Classi di età nella fonte | Mappabile sui 19 gruppi? |
|------|-------|---------------------------|--------------------------|
| 1861 | ✗ nessuna | — | — |
| 1871 | ✓ 13/13 | mesi nel 1º anno, poi anni singoli → 100, centenari | **esatta** |
| 1881 | ✓ 13/13 | anni singoli → 100 + subtotali quinquennali stampati | **esatta** |
| 1901 | ~ 13/13 | singoli → 15, poi 16-18, 19-21, 22-25, 26-30, 31-35, … | **solo fino a 14**; sopra è sfasata |
| 1911 | ~ 13/13 | **solo 0-15 / 15-65 / 65+** | no — non è una piramide |
| 1921 | ✓ 13/13 | singoli 0-20, poi 21-25, 25-30, … 95-100, 100+ | **esatta** |
| 1931 | ✓ 13/13 | singoli 0-20, poi 21-24, 25-29, … 100+ | **esatta** |
| 1936 | ✓ 13/13 | anni singoli 0-74, poi 75-79, … 100+ | **esatta** |
| 1951 | ✓ 13/13 | 12 classi irregolari (6/10/14/18/21/25/35/45/55/60/65) | serve redistribuzione |
| 1961 | ✓ 13/13 | 15 classi irregolari (6/14/21/25/30/…/75) | serve redistribuzione |
| 1971 | ✓ 13/13 | 16 quinquennali, `<5` e `75+` aperte | serve split dei due estremi |

Legenda: ✓ = dato pieno per età×sesso · ~ = presente ma inservibile o parziale ·
✗ = assente.

## Dettaglio delle fonti

**1861 — non esiste.** Nessuna tavola incrocia età e sesso sotto il livello
provinciale; lo dice l'ISTAT stesso nell'introduzione al VOL2 («ci piacque
presentarne i quadri provincia per provincia»). Il livello più fine con età×sesso
è il circondario (4 sole classi: 0-4/4-12/12-19/19+), e il circondario del
capoluogo eccede il comune di 1,2× (Napoli) fino a 4× (Firenze) — **unica
eccezione Livorno**, il cui circondario è mono-comune e coincide col comune
(96.471). Esiste `Popolazione di fatto e di diritto 1861 (edizione 1865)/popby_sex_fattodiritto_circondiario.pdf`
con tutti i comuni per sesso, **ma senza età**. Per il 1861 si può avere
comune×sesso *oppure* provincia×età×sesso, mai i due insieme.

**1871** — `1871/Censimento generale della popolazione 1871/VOL2/popby_sex_agegroup_ms_edu_comune.pdf`
(123 pp. a doppia facciata ≈ 241 stampate). Tav. II, «Comuni capoluoghi di
provincia». Una tabella per città (`COMUNE DI …`), ordine alfabetico, ~3,5
facciate per città. Età×sesso si legge nelle colonne `TOTALE` M/F; stato civile e
istruzione sono incrociati con l'età, non tabulati a parte. Roma è presente
nonostante l'annessione del 1870. Checksum: riga `Totale..` per città e appendice
a p. 240.

**1881** — `1881/VOL2/popby_sex_agegroup_ms_edu_comune.pdf` (214 pp.). Tav. I,
solo capoluoghi, ordine alfabetico, **3 pagine per città** (Bari 21-23, Bologna
33-35, Catania 51-53, Firenze 75-77, Genova 84-86, Livorno 96-98, Messina
111-113, Milano 114-116, Napoli 120-122, Palermo 129-131, Roma 165-167, Torino
189-191, Venezia 201-203). Ha subtotali quinquennali già stampati, che sono sia
checksum sia scorciatoia per aggregare. Layer OCR presente ma mediocre.

**1901** — `1901/VOL2/popby_sex_yob_comune.pdf` (203 pp.), Tav. III sez. A-1º,
capoluoghi + comuni >15.000. Le città sono **colonne** (7 per pagina), le righe
sono anni di nascita. Pagina stampata = pagina PDF + 138. Tutte e 13 verificate
(Bari p.5, Bologna p.8, Catania p.12, Firenze p.17, Genova p.19, Livorno p.22,
Messina p.24, Milano p.25, Napoli p.26, Palermo p.27, Roma p.33, Torino p.36,
Venezia p.38). **Limite:** singoli solo fino ai nati 1886 (età 15); sopra, i
raggruppamenti 16-18 / 19-21 / 22-25 / 26-30 / 31-35 non si allineano a
15-19 / 20-24 / 25-29. Le classi `0`, `1_4`, `5_9`, `10_14` sono ricostruibili
esattamente, il resto richiede interpolazione. Subtotali M/F/M+F stampati per
colonna.

**1911 — praticamente inservibile.** `1911/VOL6/popby_sex_agegroup_capolouoghi.pdf`
(41 pp.), Tav. IX-A: è una tavola sul **luogo di nascita**, dove l'età è ridotta a
**0-15 / 15-65 / 65+ / ignota**. Confermato che è il comune (Roma 542.123, Milano
599.200, Napoli 678.031). L'alternativa `VOL6/popby_sex_agegroup_religion_comuni.pdf`
ha le stesse 3 classi, richiede di sommare 6 religioni e ha gli «età ignota»
ripartiti congetturalmente (⅓/½/⅙) — peggiore. Il resto del VOL6 non scende sotto
le 3 classi, e in VOL2 l'età dettagliata si ferma al circondario. **Per una
piramide 1911 delle città questi PDF non bastano.**

**1921** — `1921/Popby_sex_agegroup_circondiari/{Regione}_1921.pdf`. Il nome
inganna: è la **Tav. XIV**, che affianca *centri ≥15.000*, *comuni capoluoghi di
circondario*, *circondari*, *province* e *regione*. Va presa la colonna
`COMUNI CAPILUOGHI DI CIRCONDARIO` — **attenzione, centro ≠ comune** (Roma centro
656.266 vs comune 691.661). Dato di popolazione *presente*, non residente.
Pagine: Torino → Piemonte p.9 · Milano → Lombardia pp.9-10 · Venezia → Veneto p.6
· Genova → Liguria pp.1-2 · Bologna → Emilia pp.1-2 · Firenze → Toscana pp.1-3 ·
Livorno → Toscana pp.4-5 · Roma → Lazio p.2 · Napoli → Campania p.9 · Bari →
Puglie pp.4-5 · Catania → Sicilia pp.5-7 · Messina → Sicilia pp.10-11 · Palermo →
Sicilia p.13. La cartella `full_document/` non serve (e mancano Liguria e
Abruzzi). Checksum: riga `In complesso`, e M+F=MF.

**1931** — `1931/popby_sex_age_ms_comune/{Provincia}_1931.pdf`. Tav. IX. Un
blocco per comune, **il capoluogo è sempre il primo blocco di p. 1**. Non ci sono
tutti i comuni: solo capoluoghi di ex circondario e comuni con centro ≥10.000 —
tutte e 13 rientrano. Colonne 2-3-4 (`In complesso` MF/M/F) danno direttamente il
marginale età×sesso senza sommare gli stati civili. **Da verificare prima
dell'uso:** il PDF di Catania annota che i dati del comune si riferiscono al
22 novembre 1931, non alla data del censimento (21 aprile 1931). Layer OCR
inutilizzabile.

**1936** — `1936/Popby_sex_agegroup_provincia/{Provincia}_1936.pdf`, Tav. X. Il
nome inganna: ogni fascicolo ha sezione **A) Provincia** (p.1) e **B) Comune di
{capoluogo}** (p.2), più eventuali C) per altri comuni grandi. Ha anche lo stato
civile per età e sesso a livello comunale. **Esistono già trascrizioni parziali**
in `1936/csv_in_complesso/` (schema `arquivo_original,pagina,eta,in_complesso_mf,maschi,femmine`;
`pagina` CSV = pagina PDF − 1), per 12 città su 13 (**manca Livorno**) — ma sono
marcate `_INCOMPL`, si fermano prima della riga `Complesso` e contengono errori
OCR verificati (Catania età 0: 6285 nel CSV vs 6.235 stampato; Torino età 21: MF
e M sbagliati). Vanno riconciliate riga per riga, non usate così. Check
indipendente: i «gruppi speciali» stampati (15-64, 65-ω).

**1951** — `1951/popby_sex_age_comune/{Provincia}_1951.pdf`, Tav. 4 (Vol. I,
«Dati sommari per comune»). Il capoluogo è una riga ordinaria in ordine
alfabetico; la riga `Provincia` è distinta. M e F su pagine affiancate.
**Manca `Messina_1951.pdf`** (la cartella ha 90 file, non 91; nota anche il
refuso `Sicarusa_1951.pdf` = Siracusa): il dato è recuperabile da
`Full_document_1951/Messina.pdf`, Tav. 4 alle pp. 30-33. Pagine capoluogo: Torino
9-10 · Milano 5-6 · Roma 3-4 · Napoli 3-4 · Palermo 3-4 · Venezia, Genova,
Catania, Bari, Bologna, Firenze, Livorno 1-2.

**1961** — `1961/popby_sex_age_provincia/{Provincia}_1961.pdf`, Tav. 4 (Vol. III).
Il nome inganna: i comuni sono righe, con riga finale `PROVINCIA`. Gli estratti
contengono **solo le sezioni B-Maschi e C-Femmine** (il totale si ottiene per
somma). Stessa griglia irregolare 0-6/6-14/14-21/… già incontrata per le sei
province ricostruite del 1961 (cfr. `data/quality/audit_1951_1961.md`).

**1971** — `1971/popby_sex_agegroup_provincia/{Provincia}_1971.pdf`, Tav. 3.
Comuni come righe (colonna `Codice dei Comuni`), riga finale `TOTALE PROVINCIA`,
sezioni A/B/C. Ogni tavola è spezzata su due pagine affiancate (sinistra `<5`→
`50-54`, destra `55-59`→`75+` + Totale). Gli stessi PDF sono già archiviati nel
repo in `downloads/sources/1971/provinces/`. Checksum: A = B + C, e colonna
`Totale` per riga.

## Se si volesse costruire il pannello città

Il carico di trascrizione è modesto (poche pagine per città per anno) e ogni
tavola porta con sé i propri checksum stampati. Gli ostacoli veri sono altri due.

**Il layer di testo dei PDF è inaffidabile in tutti gli anni** — è lo stesso
problema incontrato con le province 1971, dove 6 province su 18 avevano cifre
sbagliate nell'OCR. Vale la stessa procedura: rilettura da ritaglio a 300-400 dpi
e verifica a tre livelli (somma classi = totale stampato, M+F = totale, confronto
con una fonte indipendente).

**L'armonizzazione delle classi è il lavoro principale, non la trascrizione.**
Cinque anni (1871, 1881, 1921, 1931, 1936) mappano esattamente sui 19 gruppi
perché hanno gli anni singoli. Tre (1951, 1961, 1971) richiedono la stessa
redistribuzione già usata per le province. **1901 è armonizzabile solo fino ai 14
anni**, e **1911 non è armonizzabile affatto**: con 0-15/15-65/65+ non si ricava
una piramide. Una serie città completa e coerente sui 19 gruppi copre quindi
**8 anni su 11** (1871, 1881, 1921, 1931, 1936, 1951, 1961, 1971); 1901 entra solo
per le classi giovani; 1861 e 1911 restano fuori.
