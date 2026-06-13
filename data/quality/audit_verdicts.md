# DEMOPAST Mortality Audit — Decennial Compartmental Life Tables (1871–1936)

Auditor run: 2026-06-13. Scope: `data/processed/mortality_extraction/csv/`
Datasets: e0_comp_decennial, lifetables_comp_decennial, deaths_comp_agesex_{1901,1911,1931,1936},
e0_province_1881/1921, REPORT_lifetables_decennial.md.

## MOST DAMAGING ISSUE
**`deaths_comp_agesex_{1901,1911,1931,1936}.csv` are sex-corrupted (~2x inflated).**
The "M" column actually holds the source **"Totale"** (both sexes); the "F" column holds a
near-total, NOT "di cui Femmine". REGNO M+F ≈ 2× true Italian deaths in every year
(1901: 1,430,072 vs ~715k actual; 1911: 1,485,622 vs ~707k; 1931: 1,218,810 vs ~609k;
1936: 1,179,272 vs ~594k). These files are mislabeled and unusable for sex-specific work.
Mitigating fact: the PUBLISHED life tables were NOT built from these files (q0 and e0 are all
historically accurate), so e0_comp_decennial / lifetables_comp_decennial are unaffected.

---

## ERROR severity

| flag | verdict | evidence | recommended action |
|---|---|---|---|
| deaths_comp_agesex_1931 "M" col = Totale, F ≠ Femmine | DATA ERROR | Source TAVOLA XXI uses "Totale / di cui Femm." For PIEMONTE all-age source Totale=48,987, Femm=24,373 (trueM=24,614). CSV: M=50,504, F=48,100 → F≈Totale, M>Totale. REGNO M+F=1,218,810 ≈ 2× actual 609k deaths | Re-extract: F_true = "di cui Femm." column; M_true = Totale − Femm. Relabel columns. |
| deaths_comp_agesex_1901/1911/1936 same corruption | DATA ERROR | REGNO M alone ≈ true total deaths each year (726,834 / 748,012 / 607,442); M+F ≈ 2×. Pattern identical across all 4 files | Same fix as above; the bug is in the shared comp-deaths extractor. |
| deaths_comp_agesex_1931 LAZIO M=0, T=0 (only F=29,852) | DATA ERROR | LAZIO present in source block 2 (lines 58–73) with Totale & Femm columns, but extractor dropped its non-Femm column. 0 M rows | Re-extract LAZIO 1931 from source; supplies the missing LAZIO 1931 M/T life table. |
| deaths_comp_agesex_1931 MARCHE & PUGLIE absent | SOURCE LIMITATION (partial) | MARCHE IS in the source (block 2, lines 58–73). PUGLIE not located in extracted markdown blocks. Currently both absent from CSV | MARCHE 1931 is recoverable from source → re-extract. Verify PUGLIE page exists in volume; if printed, extract; else document as true source gap. |
| e0_comp_decennial LAZIO 1931 e0_T='', e0_M='' (F=57.73 only) | DATA ERROR (downstream of LAZIO extraction gap) | Propagated from LAZIO M=0 rows above; lifetables_comp_decennial has only sex=F for LAZIO 1931 | Fixed automatically once LAZIO 1931 M is re-extracted. |

## WARNING severity

| flag | verdict | evidence | recommended action |
|---|---|---|---|
| TOSCANA 1931→1936 e0 DROP 60.34→58.41 | CHECK / mild source issue | Both M (59.04→56.63, −2.4y) and F (61.69→60.28, −1.4y) fall while ALL other Centre-North comps rise 1931→1936. Coherent same-direction shift = real data feature, not single OCR cell. Toscana 1936 falls below Piemonte/Emilia/Umbria/Veneto, breaking the otherwise stable rank | Verify Toscana 1931 & 1936 deaths vs source in lifetables_comp.csv build. Likely 1931 slightly high or 1936 over-counted. Not a gross error (both e0 plausible). |
| TOSCANA 1931 e0_T=60.34 "suspect" (flagged in task) | HISTORICALLY PLAUSIBLE — NOT isolated | Sits in a tight top cluster: LIGURIA 60.03, UMBRIA 58.85, VENETO 58.54. Only +0.31 over Liguria. Toscana was genuinely low-mortality | No action. Re-direct attention to the 1936 dip instead. |
| M > F e0 inversions, 1871–1911 (Umbria, Sicilia 1911 +1.5y, Umbria 1901 +2.4y, etc.) | HISTORICALLY PLAUSIBLE | Female mortality disadvantage in childhood/childbearing was real in 19th–early-20th c. Italy. Inversions vanish by 1921+ (modern pattern). Magnitudes small except Umbria 1901 (+2.44) / Sicilia 1911 (+1.49) | No correction. Optionally annotate Umbria 1901 & Sicilia 1911 as larger-than-typical for review. |
| e0 decreases 1871→1881 (Calabrie, Sicilia, Umbria) | HISTORICALLY PLAUSIBLE | Report V4 documents rising CDR (Calabrie 26.8→29.2‰) = improving death registration in early Mezzogiorno civil registry; 1871 e0 over-stated | Already explained in REPORT_lifetables_decennial.md. No action. |
| e0 dips 1901→1911 (Campania, Sicilia) | HISTORICALLY PLAUSIBLE | Pre-existing in lifetables_comp.csv; 1911 cholera + summer infant mortality in South | No action. |

## INFO / confirmed-clean

| check | result |
|---|---|
| Life-table identities (all 6,745 rows × comp/year/sex) | PASS: qx∈[0,1] (0 violations), lx monotone (0), Σdx=l0 within 50 (0), open interval qx=1 (0), ex=Tx/lx within 0.05 (0) |
| e0 in plausible range [18,68] | PASS: all values in range, no spurious zeros/totals in age cells |
| Declared gap MARCHE/PUGLIE 1931 absent (not zero/spurious) | CONFIRMED truly absent from e0 & lifetables (not substituted by 0 or junk) |
| REGNO e0 vs official Italian series | PASS: q0 1901≈165‰, 1911≈159‰, 1931≈108‰, 1936≈95‰ — match official IMR; e0 43.4/44.4/54.9/56.8 all historically correct |
| North–South gradient 1881 | CONFIRMED: 7 lowest e0 all Southern (Basilicata 28.7, Lazio 28.5, Calabrie 30.4, Campania 30.6, Puglie 30.7); Sardegna high (35.6) is real (Sardinian longevity) |
| VENEZIA TRIDENTINA only 1931/1936 | CORRECT (post-WWI annexation) |
| REPORT V1/V2 checksums (e0 comp vs pop-weighted prov) | PASS as reported (max |diff|=0.18y) |

---

## PRIORITIZED FIX LIST (max 10)
1. **[CRITICAL]** Fix the shared comp-deaths extractor: source columns are "Totale / di cui Femmine", so F_true = Femm col, M_true = Totale − Femm. Re-build deaths_comp_agesex_{1901,1911,1931,1936}.csv (all 4 currently ~2x inflated & sex-swapped).
2. **[HIGH]** Re-extract LAZIO 1931 (M/Totale dropped → currently F-only); will restore LAZIO 1931 M & T life table + e0_T.
3. **[HIGH]** Re-extract MARCHE 1931 (present in source block 2, wrongly absent from CSV).
4. **[MEDIUM]** Verify whether PUGLIE 1931 is printed in the volume; extract if present, else document as genuine source gap (do not impute).
5. **[MEDIUM]** Investigate TOSCANA 1931↔1936 (~2y drop both sexes while all neighbours rise) against lifetables_comp.csv source deaths; flag in metadata.
6. **[LOW]** Add a header note to deaths_comp_agesex_*.csv clarifying they are NOT the source of the published life tables (the task brief assumes they are).
7. **[LOW]** Annotate larger-than-typical M>F e0 gaps (Umbria 1901 +2.44, Sicilia 1911 +1.49) for reviewer awareness.
8. **[LOW]** Update REPORT V4 to redirect the Toscana note from "1931→1936 verify there" to a concrete 1936 deaths check.

## SYNTHETIC VERDICT
The **published decennial life tables (lifetables_comp_decennial.csv, e0_comp_decennial.csv) are
sound**: every internal identity passes, REGNO e0/q0 match official Italian series, the
North–South gradient and M/F patterns are historically faithful, and declared gaps
(Marche/Puglie 1931) are honestly empty. The **TOSCANA 1931 e0=60.3 is plausible, not an
outlier** — the real anomaly is the unexplained 1931→1936 Toscana dip.
The serious problem is in the **intermediate `deaths_comp_agesex_*.csv` files**: all four are
sex-mislabeled and ~2x inflated (M holds the Totale), and 1931 additionally drops LAZIO-M and
MARCHE. These are extraction bugs, not source defects, and must be re-extracted before any
sex-specific use — but they do NOT contaminate the life tables that ship to the atlas.
