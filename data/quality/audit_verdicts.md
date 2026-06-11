# DEMOPAST Plausibility Audit — Verdicts

Date: 2026-06-11 · Auditor: demopast-data-auditor
Input: `data/quality/plausibility_flags.csv` (996 flags: 83 ERROR, 501 WARNING, 412 INFO)
Verdict counts (ERROR flags): **73 DATA ERROR · 6 SOURCE LIMITATION · 4 HISTORICALLY PLAUSIBLE · 0 CHECK ARTIFACT**

---

## ⚠ MOST DAMAGING ISSUE

**The 1861 census file is systematically corrupt for ~15 of its 49 provinces** (file sums to
16,884,986 vs official 21,777,334 — −4.9M). Piedmont/Liguria rows contain *sub-province*
(pre-1859 circondario-level) populations at 1/3–2/3 of the true value; several Lombard/Tuscan
rows are inflated or have scrambled M/F splits. Because every 1862–1871 rate denominator is
interpolated from 1861, this single file corrupts **CBR, CDR and nuptiality for 1863–1866 in
~10 provinces** (e.g. Alessandria CBR 1863 = 82.6, Sondrio CBR 1863 = 14.4). Re-extract the
affected provinces from the official 1861 TAVOLA SECONDA (the procedure already used to fix
Milano).

### Province-by-province: 1861 values that are wrong, and by how much

Expected 1861 ≈ census 1871 / 1.062 (national intercensal growth ≈ +0.6 %/yr).
Implied-CBR test: fertility_panel 1863 CBR (built on 1861-interpolated denominator); a value
far from 35–42 confirms a bad denominator.

| Province | 1861 recorded | 1871 census | Expected 1861 | Factor rec./true | CBR 1863 (implied) |
|---|---:|---:|---:|---:|---:|
| Alessandria | 208,760 | 683,360 | ~645,000 | **0.32** | 82.6 |
| Genova | 219,544 | 715,378 | ~674,000 | **0.33** | 77.3 |
| Novara | 256,023 | 624,985 | ~588,000 | **0.43** | 67.1 |
| Cuneo | 260,671 | 617,860 | ~582,000 | **0.45** | 66.5 |
| Torino | 562,287 | 973,016 | ~916,000 | **0.61** | 51.9 |
| Sondrio | 308,576 | 110,374 | ~104,000 | **2.96** | 14.4 |
| Porto Maurizio | 227,359 | 127,053 | ~120,000 | **1.90** | n/a |
| Como | 647,943 | 477,646 | ~450,000 | **1.44** | 28.0 |
| AbruzzoUlterioreI (Teramo) | 293,870 | 245,881 | ~232,000 | **1.27** | n/a |
| Cremona | 341,170 | 300,593 | ~283,000 | **1.21** | 41.4 (T ok-ish, still suspect) |
| Siena | 231,118 | 206,416 | ~194,000 | **1.19** | 36.0 (suspect) |
| Capitanata (Foggia) | 351,275 | 322,739 | ~304,000 | **1.16** | n/a |
| Bergamo | 384,526 | 367,760 | ~346,000 | **1.11** + sex split corrupt: M=288,041 F=96,485 (M/F = 298.5) | 34.4 |
| Brescia | 376,957 | 455,470 | ~429,000 | **0.88** + sex split corrupt (M/F = 153.8; 50–54 = 17 % of pop; mean age 42.7) | 44.0 |
| Caltanissetta | 190,115 | 230,096 | ~217,000 | **0.88** + sex ratio 113.0 | 50.2 |

Cause hypothesis: for Piedmont/Liguria the extraction picked the **old Sardinian sub-provinces**
(e.g. "provincia di Alessandria" = one of seven units of the Divisione di Alessandria) instead of
the 1871-comparable division totals; the Lombardy/Tuscany anomalies look like row/column
scrambling (Bergamo's F column, Brescia's age distribution). Grosseto's high 1861 sex ratio
(135.4) is, by contrast, plausibly real (de-facto winter population incl. seasonal Maremma
labourers; it persists at 130.3 in 1871 and 129.0 in 1881).

Also: census_1861 has 49 rows (1861 Italy had 59 provinces) and four 1861 names
(AbruzzoUlterioreII, CalabriaUlterioreII, Noto, TerradiBari) have no 1871 match because 1871
uses modern names (AquiladegliAbruzzi, Catanzaro, Siracusa, BaridellePuglie) — these provinces
therefore escape all cross-census checks.

---

## ERROR flags — verdicts

### 1. census · intercensal_jump (8 flags)

| Flag | Verdict | Evidence | Action |
|---|---|---|---|
| Alessandria 1861→71 (×3.27) | DATA ERROR | see 1861 table above | re-extract 1861 |
| Cuneo 1861→71 (×2.37) | DATA ERROR | idem | re-extract 1861 |
| Genova 1861→71 (×3.26) | DATA ERROR | idem | re-extract 1861 |
| Novara 1861→71 (×2.44) | DATA ERROR | idem | re-extract 1861 |
| Torino 1861→71 (×1.73) | DATA ERROR | idem | re-extract 1861 |
| PortoMaurizio 1861→71 (×0.56) | DATA ERROR | idem | re-extract 1861 |
| Sondrio 1861→71 (×0.36) | DATA ERROR | idem | re-extract 1861 |
| Grosseto 1881→1901 (×1.56) | DATA ERROR (in **1901**, not 1881) | raw/census/1901: Grosseto 15–19 = 36,078 vs 10–14 = 16,408 (impossible); 1901 total 178,102 > 1911 total 146,634; true 1901 ≈ 138k. Same corruption in the Tuscany block: Arezzo 15–19 = 56,421 (vs 10–14 = 28,903), 1901 total 309,848 > 1911 283,337; Livorno 15–19 = 24,692 (vs 10–14 = 10,762), 1901 148,469 > 1911 135,612 | fix 15–19/20–24 cells for Grosseto, Arezzo, Livorno in raw 1901 file, rebuild |

### 2. census · internal checksums — 52 flags = 37 corrupted age cells in 21 province-years

Key structural finding: in every census file `total_pop = Σt_age`, `male_pop = Σm_age`,
`female_pop = Σf_age` (verified: Σ−marginal = 0 in all 21 rows). **Every `total!=M+F` flag is
therefore exactly the sum of that row's age-cell errors — 15 of the 52 flags are duplicates of
the other 37.** All are single-cell OCR errors (DATA ERROR); the deviant cell is identified by
the implausible age-specific sex ratio. Proposed corrections (verify against printed volume):

| Province-year | Cell | Stored | Likely true | Evidence |
|---|---|---:|---:|---|
| Napoli 1936 | f_70_74 | 69,128 | **23,763** | f > 3.3×m impossible; t−m = 23,763; row M+F−T = +44,675 ≈ this one cell |
| Catania 1936 | m_1_4 | 24,025 | **32,227** | m < f by 6.8k at age 1–4 impossible; t−f = 32,227 |
| Roma 1931 | f_5_9 | 70,073 | **78,073** | sex ratio 5–9 = 115 impossible; off by exactly 8,000 (OCR 8→0) |
| Cosenza 1936 | f_35_39 | 18,278 | **12,148** | f−m = +5.0k anomalous; t−m = 12,148 |
| PrincipatoUlteriore 1871 | m_5_9 | 13,687 | **20,507** | m≪f at 5–9 impossible; t−f = 20,507 |
| Messina 1871 | t_40_44 | 15,414 | **27,621** | m,f ≈ 13.7k/13.9k consistent with age-40 heaping; t<m alone | 
| Messina 1871 | t_35_39/t_0 etc. | — | — | smaller offsets (−54, +635, +7, +9, −60): several cells, re-read row |
| ReggioCalabria 1911 | one of t/m/f 40_44 | — | — | off exactly +1,000 (thousands digit) |
| Enna 1936 | t/m/f 55_59 | — | — | off +872 |
| Nuoro 1936 | 35_39, 60_64, 65_69 (+50s) | — | — | offs +500/−500/−505 (±50 ×2): multiple cells |
| Imperia 1936 | 8 cells (1_4…60_64) | — | — | offs 60–300 each, total +792: whole row needs re-read |
| Bergamo 1936 | t_5_9 (−900), 15_19 (+90) | — | — | net −767 |
| Genova 1936 | 40_44 (+600), 55_59, 85plus | — | — | net +750 |
| Terni 1936 | 30_34 | — | — | +500 |
| Piacenza 1921 | 10_14 (+600), 35_39 (−10) | — | — | net +590 |
| Pisa 1921 | 60_64 (−630) + 3 small | — | — | net −590 |
| Massa e Carrara 1921 | 5_9 | — | — | +600 |
| Vicenza 1921 | 10_14 | — | — | +500 |
| Venezia 1921 | 10_14 | — | — | +360 |
| Rovigo 1921 | 15_19 | — | — | −180 |
| Siracusa 1921 | 70_74 | — | — | +100 |
| AscoliPiceno 1931 | t_0 (−180) / t_1_4 (+180) | — | — | offsetting pair → 0/1–4 boundary mis-split, marginals unaffected |

### 3. fertility · cbr_implausible (5 flags)

| Flag | Verdict | Evidence | Action |
|---|---|---|---|
| Alessandria 1863 (82.55), 1864 (70.35) | DATA ERROR (denominator) | births plausible; 1861 pop = 0.32× true | fix census 1861 |
| Genova 1863 (77.25) | DATA ERROR (denominator) | idem (0.33×) | fix census 1861 |
| Fiume 1931 (5.8) | DATA ERROR (denominator) | births = 2,021 ✓ matches official `datalab_1931_prov.md` (Fiume pop **106,775**, births 2,021). census_1931 row `32,Fiume,348405` actually holds **Trieste's** population (official Trieste 1931 = 348,494); true CBR = 18.9 | relabel 1931 row 32 → Trieste; add real Fiume row |
| Mantova 1865 (5.16) | SOURCE LIMITATION | births 1865 = 1,486 vs 5,888 (1864) / 6,148 (1866); Mantova was Austrian until Oct 1866, Italian registration covers a fragment of the province; series only completes by 1869 (10,809 births, CBR 37.5) | annotate, do not "fix" |

### 4. marriages · nuptiality_implausible (13 flags)

| Flag | Verdict | Evidence | Action |
|---|---|---|---|
| Alessandria 1863–65 (17.1–19.6), Genova 1863–65 (16.7–19.7), Novara 1865 (16.3) | DATA ERROR (denominator) | counts plausible; 1861 census denominators 1/3–2/5 of true | fix census 1861 |
| Fiume 1931 (1.93) | DATA ERROR (denominator) | 671 marriages ✓ = official count for Fiume (pop 106,775 → true rate 6.3); denominator is Trieste's 348,405 | same census_1931 fix |
| Mantova 1865 (1.20) | SOURCE LIMITATION | 347 marriages vs 1,430 (1864) / 1,385 (1866) — partial territory under Austria | annotate |
| Ferrara 1866 (1.68), Girgenti 1866 (2.92), Pesaro e Urbino 1866 (2.94) | SOURCE LIMITATION (+ real war effect) | obligatory **civil** marriage introduced 1 Jan 1866; church-only marriages vanish from the statistics — trough deepest and most persistent in ex-Papal provinces (Pesaro stays 3.2–4.1 until 1871); 1866 war adds a genuine dip nationwide | annotate; do not flag 1866–71 lows as errors |
| Roma 1872 (2.98) | SOURCE LIMITATION | same civil-registration resistance after 1870 annexation; Roma 1873 = 3.72, 1874 = 4.45, slow normalisation | annotate |

### 5. migration · emig_rate_implausible (4 flags)

| Flag | Verdict | Evidence |
|---|---|---|
| Belluno 1911–1914 (82.2–94.1‰) | HISTORICALLY PLAUSIBLE | 16,700–18,800 expatriations/yr on ~195k pop; Belluno was Italy's top emigration province (overwhelmingly *temporary/seasonal* migration to Austria-Hungary/Germany, counted as expatriations in ASI); Udine shows the same regime (58–80‰); series collapses to 15.1‰ in 1915 exactly when the border closed — internally coherent |

### 6. mortality · cdr_implausible (1 flag)

| Flag | Verdict | Evidence | Action |
|---|---|---|---|
| Trapani 1881 (cdr 0.95, deaths 269) | DATA ERROR | TAVOLA VI printed row 1881: marriages 2,780; births 11,989; **stillbirths 269 (152/117); deaths 7,339 (3,775/3,564)**. The panel stored the stillbirth triple as deaths. Worse: the whole Trapani deaths series is shifted one year from 1874 on (panel 1874 = printed 1875 … panel 1880 = printed 1881) because the printed 1874 row (6,186) was skipped | re-extract Trapani deaths 1874–1881 |

---

## WARNING clusters — verdicts

### cdr_range (85)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| 1921/1931/1936 lows, cdr 10.7–15 (~75 flags: Roma 1931 11.5, Firenze 1936 11.9, Padova 1936 11.1 …) | HISTORICALLY PLAUSIBLE / CHECK ARTIFACT | real secular mortality decline (national CDR 1936 ≈ 13.7). Spot-check: Firenze 1936 cdr 11.9 = exactly the printed 11,9 in PROSPETTO 7 (`datalab_1936_cdr.md`). Lower the check's bound for 1921+ |
| 1871/1881 lows: Pisa (13.1/12.0), Treviso (14.3/12.3), Udine (13.5/12.2), Ravenna 1881 (11.9), Venezia 1881 (12.7), Cagliari 1881 (14.7) | **DATA ERROR — male-only deaths stored as totals** | TAVOLA VI OCR dropped one column for these provinces, so deaths_T = printed deaths_M (≈½). Proof: Pisa 1871 printed deaths 6,726 = 3,495M + 3,231F; panel stores T=3,495, M=3,231, F=264 (residual). Udine 1881 panel F = **−111** (negative). Systematic scan of `deaths_province_panel.csv` (rows with F < 0.5·M): **164 rows, 13 provinces** — Imperia 1863–81 (19 yrs), Potenza 1863–81 (19), Treviso/Udine/Venezia/Vicenza 1865–81 (17 each), Cagliari/Pisa/Ravenna 1866–81 (16 each), Verona 1865–71 (7), Bergamo 1863, Pavia 1868, Sondrio 1881. Plus 38 further rows fail M+F=T (worst: Lecce 1867 12,964 ≠ 9,505+9,759; Foggia 1866 M=537) | 

### nuptiality_range (83)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| 1921 highs, 12.1–14.6 (~35 flags, everywhere) | HISTORICALLY PLAUSIBLE | classic post-WWI marriage boom (recovery of postponed marriages 1919–21); exempt 1919–21 in the rule |
| 1866–1871 lows, 3.0–4.5 (~30 flags) + Roma 1873–74 | SOURCE LIMITATION | civil-marriage transition (see ERROR §4); gradual convergence 1867→1872 visible in Caltanissetta 3.86→5.64→8.09→11.09 |
| Piedmont 1863–65 highs (Cuneo 14.1–15.7, Novara 13.9–14.8, Torino 12.4–12.6) | DATA ERROR (denominator) | 1861 census deficits (factors 0.43–0.61) |
| Sondrio 1863–67 lows (3.1–4.4) | DATA ERROR (denominator) | 1861 Sondrio = 2.96× true |

### cbr_range (41)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| 1931 lows 14.6–19.7 (N/C Italy, 22 flags) + Torino/Pavia/Novara/PortoMaurizio 1921 (18.6–19.7) | HISTORICALLY PLAUSIBLE | fertility transition: official Italian CBR 1931 = 24.9 with Liguria/Piedmont ≪ 20 (PROSPETTO 7 confirms e.g. Firenze 1936 natalità 14.6) |
| Alessandria/Cuneo/Genova/Novara 1863–66 highs (55–67) | DATA ERROR (denominator) | 1861 census (see top table) |
| Sondrio 1863–66 lows (14.4–19.6) | DATA ERROR (denominator) | idem (2.96×) |
| Sondrio 1881 (18.56) | **DATA ERROR (numerator)** | printed TAVOLA VI Sondrio 1881: births **4,333** (M 2,270, F 2,063); panel stored the *male* column 2,270 as total (true CBR ≈ 35). The same row's deaths parse is garbage (1,607/1,527/80 vs printed 3,134/1,607/1,527) |

### sex_ratio (29)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| Bergamo 1861 (298.5), Brescia 1861 (153.8) | DATA ERROR | M/F split corrupt (Bergamo F = 96,485 on T = 384,526); Brescia also mean_age 42.7 and 17 % in 50–54 → whole age/sex panel scrambled |
| Siena 1861 (114.9), Caltanissetta 1861 (113.0) | DATA ERROR (suspect) | part of 1861 problem; siblings 1871 are normal |
| Grosseto 1861/71/81 (129–135), 1901 (113) | HISTORICALLY PLAUSIBLE (except 1901) | de-facto winter census population incl. seasonal male Maremma labourers; persistence across 3 censuses is the tell. 1901 additionally contaminated by the corrupt 15–19/20–24 cells |
| Roma 1871/1881 (115.9/113.6) | HISTORICALLY PLAUSIBLE | male in-migration to the new capital |
| South + Belluno/Udine/Lucca 1901–1931 lows (81.8–87.8) | HISTORICALLY PLAUSIBLE | mass male emigration (matches the emigration panel: Belluno 87‰ in 1911) |
| Firenze 1936 (85.4) | DATA ERROR (consequence) | this is the *city* of Florence row — see intercensal section |
| Cremona 1931 (80.9) | CHECK | lowest non-city value in the whole panel; no extreme emigration history → verify against printed 1931 volume |

### intercensal_growth / intercensal_jump WARNINGs (14 + 7)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| 1921→31 drops: Caltanissetta (→Enna), Siracusa (→Ragusa), Lecce (→Brindisi, Ionio), Novara (→Vercelli), Como (→Varese), Perugia (→Terni), Teramo (→Pescara), Potenza (→Matera), Firenze (→Pistoia), Genova 1921→31 (→La Spezia 1923), Catania (→Enna share) | HISTORICALLY PLAUSIBLE | 1923–1927 province redraws (known history) |
| Napoli 1921→31 (+3.56 %/yr) | HISTORICALLY PLAUSIBLE | absorbed most of abolished Caserta province (1927) |
| Livorno 1921→31 (143,190→245,707) | HISTORICALLY PLAUSIBLE | province enlarged 1925 with circondari from Pisa/Genova |
| Alessandria 1931→36 (→494,688) | HISTORICALLY PLAUSIBLE | Asti split, 1935 |
| MassaCarrara 1921→31 (−1.6 %/yr) | HISTORICALLY PLAUSIBLE | Garfagnana ceded to Lucca, 1923 |
| Cremona 1931→36 (−1.62 %/yr) | CHECK / plausible | no boundary change; rural out-migration was real but −1.6 %/yr is steep — verify 369,466 against the printed VIII censimento |
| **Firenze 1931→36 (840,043→322,526)** | **DATA ERROR** | see below |
| **Trieste 1931→36 (+5.74 %/yr)** | **DATA ERROR** | see below |
| Como, AbruzzoUlterioreI 1861→71 declines | DATA ERROR | 1861 problem (factors 1.44 / 1.27) |
| Grosseto 1901→11 (−1.93 %/yr) | DATA ERROR (in 1901) | corrupt Tuscany 1901 cells (see ERROR §1) |

### Firenze 1931→1936 (840,043 → 322,526): NOT a boundary change — DATA ERROR

- No Firenze boundary change between 1931 and 1936 (Pistoia split already in 1927).
- The 1936 source file `downloads/1936/data_census_1936_adjusted_age.csv` itself contains the
  bad data: rows `048,Firenze` sum to exactly 322,526 — this is the **comune (city) of
  Florence** (official 1936 city pop ≈ 322.5k), with a city signature: age 0 = 1.20 % of pop
  (flagged share_age0), sex ratio 85.4 (flagged), F surplus concentrated at ages 20–54
  (domestic service).
- Official province values: mid-1931 pop 840,287 (`datalab_1931_prov.md`) ✓ census 840,043;
  province CBR/CDR 1936 = 14.6/11.9 (PROSPETTO 7, col. a) — both consistent with a province of
  ~890k, *not* 322k.
- **Action**: re-extract the Firenze *province* row from the VIII censimento volume and rebuild
  census_1936.

### Venezia Giulia block (1931 + 1936) — DATA ERROR cluster

- census_1931 row `32,Fiume,348405`: 348,405 is **Trieste** (official 348,494); the real Fiume
  (106,775) is absent. Trieste, Pola, Zara absent from census_1931 (89 rows).
- census_1936 row `32,Trieste,460596`: ≈ +112k above any plausible Trieste value
  (1931 = 348k); 460,596 ≈ Trieste (~354k expected) + Fiume (~107k) → rows likely merged in
  extraction. Fiume, Pola, Zara absent from census_1936.
- These two errors jointly produced the Fiume 1931 CBR/nuptiality ERRORs and the Trieste
  intercensal WARNING.

### yoy_jump, non-war (fertility 5, marriages ~15, migration ~30)

| Sub-cluster | Verdict | Evidence |
|---|---|---|
| Marriages/births 1880→1881 jumps (Benevento CBR 30.5→41.9; Campobasso, Catanzaro, Girgenti nuptiality +35–50 %) | HISTORICALLY PLAUSIBLE | 1880 was a genuine national trough: panel national births 1879 = 1,063,823 → **1880 = 957,600 (−10 %)** → 1881 = 1,078,392; Benevento births printed 9,846→7,250→9,982 — extraction faithful to source |
| Mantova 1864→65→66 and 1868→69 (births 6,279→10,809) | SOURCE LIMITATION | Austrian→Italian transition; registration completes by 1869 |
| Migration 1911→12→13 surges (~30 flags, all provinces) | HISTORICALLY PLAUSIBLE | 1911–12 Libyan-war conscription depressed emigration; 1913 = all-time national record (~873k expatriations); Trapani 70.8‰ and Sicily 40–50‰ in 1913 documented |
| Migration 1914–1920 collapse/rebound (~80 flags) | HISTORICALLY PLAUSIBLE | WWI border closure (Belluno 82.2‰→15.1‰ in 1915) and 1920 rebound — known history |
| Sondrio 1880→81 CBR | DATA ERROR | male-births-as-total (see cbr_range) |

### Other census WARNINGs
- `share_15_19` Arezzo/Grosseto/Livorno 1901 (16.6–20.3 %) → DATA ERROR, corrupt 1901 Tuscany cells (above).
- `province_missing` Sondrio 1881 → known history (already documented).
- `share_age0` Firenze 1936 (1.20 %) → consequence of the city-row error. Campobasso 1936 (5.02 %) → plausible (high-fertility Molise), borderline.
- census_1871 contains a **duplicate Catanzaro row** (code 79, 412,236 twice) — harmless for rates but should be deduped.

---

## PRIORITIZED FIX LIST

1. **Census 1861 — re-extract ~15 provinces from TAVOLA SECONDA** (Alessandria, Genova, Novara,
   Cuneo, Torino, Sondrio, Porto Maurizio, Como, Bergamo, Brescia, Cremona, Siena, Teramo,
   Capitanata, Caltanissetta; factors 0.32×–2.96×). Unblocks all 1863–66 rate denominators.
2. **deaths_province_panel (dati_ISTAT) — re-parse TAVOLA VI with M+F=T validation**: 164 rows /
   13 provinces store male-only deaths as totals (Imperia & Potenza full 1863–81 series; Veneto
   block 1865–81; Cagliari/Pisa/Ravenna 1866–81); + 38 other checksum failures; + Trapani
   one-year shift 1874–81 with stillbirths-as-deaths in 1881; + Sondrio 1881 garbage row.
3. **census_1931/1936 Venezia Giulia**: relabel row 32 (Fiume→Trieste, 348,405), add true Fiume
   1931 = 106,775; fix Trieste 1936 = 460,596 (likely Trieste+Fiume merged); add missing
   Fiume/Pola/Zara rows in both years.
4. **census_1936 Firenze**: replace city row (322,526) with the province (~890k) in
   `downloads/1936/data_census_1936_adjusted_age.csv` and rebuild.
5. **raw/census/1901 Tuscany block**: re-read 15–19 (and 20–24) cells for Grosseto (total
   −~40k), Arezzo (−~38k), Livorno (−~13k); rebuild census_1901.
6. **37 single-cell OCR errors in census age tables** (21 province-years; apply the proposed
   corrections table, re-reading Imperia 1936, Nuoro 1936 and Messina 1871 rows in full).
7. **Rebuild derived panels** (fertility, marriages, mortality rates) after items 1–5; the
   1863–66 ERROR/WARNING rate flags should disappear without touching counts.
8. **Dedupe census_1871 Catanzaro**; harmonize 1861 province names (AbruzzoUlterioreII→
   AquiladegliAbruzzi, CalabriaUlterioreII→Catanzaro, Noto→Siracusa, TerradiBari→
   BaridellePuglie) so cross-census checks cover all provinces.
9. **Audit Sondrio 1881 and all "last row of block" TAVOLA VI parses** in
   births_province_panel (male-as-total signature: births_T ≈ 0.5 × sibling years).
10. **Recalibrate the checker**: period-dependent CDR (lower bound ≈ 10 for 1921+) and CBR
    bounds; exempt nuptiality 1919–21 (boom) and 1866–71 (civil-registration transition);
    add an automatic "F < 0.5·M or F < 0" test on every T/M/F triple (it catches items 2 and 9
    deterministically).
