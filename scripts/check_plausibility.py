#!/usr/bin/env python3
"""
Plausibility audit of all published DEMOPAST datasets.

Checks census files (internal consistency, age structure, sex ratio,
intercensal growth, missing provinces) and the four vital-statistics
panels (rate ranges, year-over-year jumps, duplicates, cross-series
births vs deaths). Emits:

  data/quality/plausibility_report.md   human-readable report
  data/quality/plausibility_flags.csv   one row per flag

Severities: ERROR  = almost certainly a data error, fix before use
            WARNING = outside plausible historical range, inspect source
            INFO    = unusual but historically possible (crisis years &c.)
"""

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / "data"
OUTDIR = DATA / "quality"

CENSUS_YEARS = [1861, 1871, 1881, 1901, 1911, 1921, 1931, 1936, 1951, 1961, 1971]
AGE_KEYS = (["0", "1_4"] + [f"{lo}_{lo + 4}" for lo in range(5, 85, 5)]
            + ["85plus"])

# panel: (rate field, count field, soft range, hard range)
PANELS = {
    "fertility":  ("cbr", "births", (20, 55), (10, 70)),
    "marriages":  ("nuptiality", "marriages", (4.5, 12), (3, 16)),
    "mortality":  ("cdr", "deaths", (15, 40), (10, 60)),
    "migration":  ("emig_rate", "emigrants", (0, 40), (0, 80)),
}
EXTRA_RATES = {"mortality": {"imr": (60, 350), "e0": (25, 60)}}

GROWTH_SOFT = (-1.5, 3.5)        # annualized intercensal growth, %/yr
RATIO_HARD = (0.67, 1.5)         # intercensal pop ratio, any gap
YOY_JUMP = 0.35                  # relative change between adjacent years

flags: list[dict] = []


def flag(sev: str, dataset: str, where: str, check: str, detail: str) -> None:
    flags.append({"severity": sev, "dataset": dataset, "where": where,
                  "check": check, "detail": detail})


def fnum(r: dict, k: str) -> float | None:
    v = r.get(k, "")
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


# ---------------------------------------------------------------- census
def check_census() -> dict[int, dict[int, dict]]:
    panel: dict[int, dict[int, dict]] = {}
    for cy in CENSUS_YEARS:
        f = DATA / f"census/census_{cy}.csv"
        if not f.exists():
            flag("ERROR", "census", str(cy), "missing_file", f.name)
            continue
        panel[cy] = {}
        for r in csv.DictReader(f.open()):
            cod = int(r["COD_PROV"])
            where = f"{r['DEN_PROV']} {cy}"
            panel[cy][cod] = r
            tot, m, fe = (fnum(r, k) for k in
                          ("total_pop", "male_pop", "female_pop"))
            if None in (tot, m, fe):
                flag("ERROR", "census", where, "missing_totals", str(r)[:80])
                continue
            if m + fe != tot:
                diff = abs(m + fe - tot)
                sev = "INFO" if diff <= max(10, 0.001 * tot) else "ERROR"
                flag(sev, "census", where, "total!=M+F",
                     f"{tot:,.0f} != {m:,.0f}+{fe:,.0f} (off {diff:,.0f})")
            tsum = sum(fnum(r, f"t_{k}") or 0 for k in AGE_KEYS)
            if abs(tsum - tot) > max(1, 0.003 * tot):
                flag("ERROR", "census", where, "age_sum!=total",
                     f"sum ages {tsum:,.0f} vs total {tot:,.0f}")
            for k in AGE_KEYS:
                tm, tf, tt = (fnum(r, f"{s}_{k}") for s in "mft")
                if None not in (tm, tf, tt) and tm + tf != tt:
                    d = abs(tm + tf - tt)
                    sev = "INFO" if d <= max(5, 0.005 * (tt or 1)) else "ERROR"
                    flag(sev, "census", where, f"t_{k}!=m+f",
                         f"{tt:,.0f} != {tm:,.0f}+{tf:,.0f} (off {d:,.0f})")
            sr = m / fe * 100 if fe else None
            if sr and not 88 <= sr <= 112:
                flag("WARNING", "census", where, "sex_ratio",
                     f"M/F = {sr:.1f} per 100")
            sh85 = (fnum(r, "t_85plus") or 0) / tot * 100
            if sh85 > 2.5:
                flag("WARNING", "census", where, "share_85plus",
                     f"{sh85:.2f}% of population aged 85+")
            sh0 = (fnum(r, "t_0") or 0) / tot * 100
            # the post-war fertility decline pushes the age-0 share well below
            # what is plausible for the pre-war censuses
            sh0_min = 0.9 if cy >= 1961 else 1.2
            if not sh0_min <= sh0 <= 5:
                flag("WARNING", "census", where, "share_age0",
                     f"{sh0:.2f}% of population aged 0")
            for k in AGE_KEYS[2:]:
                sh = (fnum(r, f"t_{k}") or 0) / tot * 100
                if sh > 16:
                    flag("WARNING", "census", where, f"share_{k}",
                         f"{sh:.1f}% in one 5-year group")
            ma = fnum(r, "mean_age")
            # ageing lifts the ceiling: the 1971 median province sits at 35.1
            ma_max = 42 if cy >= 1961 else 38
            if ma is not None and not 22 <= ma <= ma_max:
                flag("WARNING", "census", where, "mean_age", f"{ma:.1f}")

    # intercensal growth + provinces vanishing between censuses
    for prev, cur in zip(CENSUS_YEARS, CENSUS_YEARS[1:]):
        if prev not in panel or cur not in panel:
            continue
        gap = cur - prev
        for cod, r in panel[cur].items():
            if cod not in panel[prev]:
                continue
            p0 = fnum(panel[prev][cod], "total_pop")
            p1 = fnum(r, "total_pop")
            if not p0 or not p1:
                continue
            ratio = p1 / p0
            growth = (ratio ** (1 / gap) - 1) * 100
            where = f"{r['DEN_PROV']} {prev}->{cur}"
            # 1927/1935 province redraws; 1968 Pordenone and 1970 Isernia splits
            boundary = cur in (1931, 1936, 1971)
            if not RATIO_HARD[0] <= ratio <= RATIO_HARD[1]:
                sev = "WARNING" if boundary else "ERROR"
                note = " (possible boundary change)" if boundary else ""
                flag(sev, "census", where, "intercensal_jump",
                     f"{p0:,.0f} -> {p1:,.0f} (x{ratio:.2f}){note}")
            elif not GROWTH_SOFT[0] <= growth <= GROWTH_SOFT[1]:
                flag("WARNING", "census", where, "intercensal_growth",
                     f"{growth:+.2f}%/yr ({p0:,.0f} -> {p1:,.0f})")
    for i, cy in enumerate(CENSUS_YEARS[1:-1], 1):
        prev, nxt = CENSUS_YEARS[i - 1], CENSUS_YEARS[i + 1]
        if any(y not in panel for y in (prev, cy, nxt)):
            continue
        for cod in set(panel[prev]) & set(panel[nxt]):
            if cod not in panel[cy]:
                flag("WARNING", "census", f"COD_PROV {cod} {cy}",
                     "province_missing",
                     f"present in {prev} and {nxt}, absent in {cy} "
                     f"({panel[prev][cod]['DEN_PROV']})")
    return panel


# ---------------------------------------------------------------- panels
def check_panel(name: str) -> dict[tuple[int, int], dict]:
    rate_f, count_f, soft, hard = PANELS[name]
    f = DATA / name / f"{name}_panel.csv"
    if not f.exists():
        flag("ERROR", name, "-", "missing_file", f.name)
        return {}
    rows, seen = {}, set()
    for r in csv.DictReader(f.open()):
        cod, year = int(r["COD_PROV"]), int(r["year"])
        where = f"{r['DEN_PROV']} {year}"
        if (cod, year) in seen:
            flag("ERROR", name, where, "duplicate_row", "")
            continue
        seen.add((cod, year))
        rows[(cod, year)] = r
        cnt = fnum(r, count_f)
        if cnt is not None and cnt <= 0:
            flag("ERROR", name, where, "nonpositive_count",
                 f"{count_f}={cnt:,.0f}")
        rate = fnum(r, rate_f)
        if rate is None:
            if cnt:
                flag("INFO", name, where, "missing_rate",
                     f"{count_f} present, {rate_f} empty")
        elif not hard[0] <= rate <= hard[1]:
            flag("ERROR", name, where, f"{rate_f}_implausible",
                 f"{rate_f}={rate}")
        elif not soft[0] <= rate <= soft[1]:
            flag("WARNING", name, where, f"{rate_f}_range",
                 f"{rate_f}={rate}")
        for xf, (lo, hi) in EXTRA_RATES.get(name, {}).items():
            xv = fnum(r, xf)
            if xv is not None and not lo <= xv <= hi:
                flag("WARNING", name, where, f"{xf}_range", f"{xf}={xv}")
    # year-over-year jumps on adjacent years only
    by_prov: dict[int, list[tuple[int, float]]] = {}
    for (cod, year), r in rows.items():
        rate = fnum(r, rate_f)
        if rate:
            by_prov.setdefault(cod, []).append((year, rate))
    for cod, series in by_prov.items():
        series.sort()
        for (y0, v0), (y1, v1) in zip(series, series[1:]):
            if y1 - y0 == 1 and v0 and abs(v1 - v0) / v0 > YOY_JUMP:
                den = rows[(cod, y1)]["DEN_PROV"]
                war = name == "migration" and 1914 <= y1 <= 1920
                flag("INFO" if war else "WARNING", name,
                     f"{den} {y0}->{y1}", "yoy_jump",
                     f"{rate_f} {v0} -> {v1}" +
                     (" (WWI disruption)" if war else ""))
    return rows


# ------------------------------------------------------------ cross-series
def check_cross(fert: dict, mort: dict) -> None:
    for key, fr in fert.items():
        mr = mort.get(key)
        if not mr:
            continue
        cbr, cdr = fnum(fr, "cbr"), fnum(mr, "cdr")
        if cbr and cdr and cdr > cbr:
            flag("INFO", "cross", f"{fr['DEN_PROV']} {key[1]}",
                 "cdr>cbr", f"deaths exceed births: CDR {cdr} > CBR {cbr}")


# ---------------------------------------------------------------- report
def write_report() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    flags.sort(key=lambda x: (order[x["severity"]], x["dataset"],
                              x["check"], x["where"]))
    with (OUTDIR / "plausibility_flags.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["severity", "dataset", "where",
                                           "check", "detail"])
        w.writeheader(); w.writerows(flags)

    counts = {s: sum(1 for x in flags if x["severity"] == s)
              for s in ("ERROR", "WARNING", "INFO")}
    lines = ["# DEMOPAST data plausibility report", "",
             f"Flags: **{counts['ERROR']} ERROR**, "
             f"{counts['WARNING']} WARNING, {counts['INFO']} INFO", ""]
    for sev in ("ERROR", "WARNING", "INFO"):
        sel = [x for x in flags if x["severity"] == sev]
        if not sel:
            continue
        lines += [f"## {sev} ({len(sel)})", "",
                  "| dataset | where | check | detail |",
                  "|---|---|---|---|"]
        lines += [f"| {x['dataset']} | {x['where']} | {x['check']} "
                  f"| {x['detail']} |" for x in sel]
        lines.append("")
    (OUTDIR / "plausibility_report.md").write_text("\n".join(lines))
    print(f"{len(flags)} flags -> {OUTDIR / 'plausibility_report.md'}")
    for s, n in counts.items():
        print(f"  {s}: {n}")


def main() -> None:
    check_census()
    fert = check_panel("fertility")
    check_panel("marriages")
    mort = check_panel("mortality")
    check_panel("migration")
    check_cross(fert, mort)
    write_report()


if __name__ == "__main__":
    main()
