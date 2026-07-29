#!/usr/bin/env python3
"""Assembla le tavole città 1901 e 1911 nei 19 gruppi di età standard.

1911 (Tav. IV, Vol. II): anni singoli 0-21 + quinquennali perfettamente
allineati -> mappatura ESATTA. Età ignota scartata (convenzione del pannello).

1901 (Tav. III, Vol. II): righe per anno di nascita. Conversione coorte->età
al censimento (10 feb 1901): nati 1901+1900 -> età 0, 1899-1896 -> 1-4, ecc.
I gruppi di coorte 1885-83 (età 15-17) e 1879-76 (età 21-24) cadono dentro i
quinquennali; SOLO il gruppo 1882-80 (età 18-19-20) va diviso tra 15-19 e
20-24: la quota di 18-19 è stimata con le proporzioni per anno singolo della
stessa città al 1911 (largest-remainder, per sesso). Età ignota scartata.
"""
import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
OUT = REPO / 'downloads' / 'citta' / 'data_census_citta.csv'

CITY_CODE = {'Torino': '001', 'Genova': '010', 'Milano': '015', 'Venezia': '027',
             'Bologna': '037', 'Firenze': '048', 'Livorno': '049', 'Roma': '058',
             'Napoli': '063', 'Bari': '072', 'Palermo': '082', 'Messina': '083',
             'Catania': '087'}

CLASSES = ['0', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34',
           '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69',
           '70-74', '75-79', '80-84', '85+']


def check_1911(rows):
    """rows: 40 x [mf, m, f]; ultima riga Totale, penultima Ignota."""
    body, tot = rows[:-1], rows[-1]
    for i, (mf, m, f) in enumerate(body):
        if m is not None and m + f != mf:
            raise SystemExit(f'riga {i}: {m}+{f} != {mf}')
    for col in range(3):
        vals = [r[col] for r in body if r[col] is not None]
        if len(vals) == len(body) and sum(vals) != tot[col]:
            raise SystemExit(f'colonna {col}: somma {sum(vals)} != totale {tot[col]}')


def harmonize_1911(rows):
    """40 righe -> dict classe -> (m, f). Scarta ignota (indice 38)."""
    r = rows
    def add(idx):
        return (sum(r[i][1] for i in idx), sum(r[i][2] for i in idx))
    return dict(zip(CLASSES, [
        add([0]), add(range(1, 5)), add(range(5, 10)), add(range(10, 15)),
        add(range(15, 20)), add([20, 21]), add([22]), add([23]), add([24]),
        add([25]), add([26]), add([27]), add([28]), add([29]), add([30]),
        add([31]), add([32]), add([33]), add(range(34, 38)),
    ]))


def check_1901(rows):
    body, tot = rows[:-1], rows[-1]
    for col in range(2):
        s = sum(r[col] for r in body)
        if s != tot[col]:
            raise SystemExit(f'1901 colonna {col}: somma {s} != totale {tot[col]}')


def split_1882_80(group, ref):
    """Divide il gruppo di coorte 1882-80 (età 18,19,20) in (18-19, 20).

    group: valore per un sesso; ref: (n18, n19, n20) dal 1911 stessa città.
    Ritorna (quota_18_19, quota_20) con arrotondamento che conserva il totale.
    """
    n18, n19, n20 = ref
    share = (n18 + n19) / (n18 + n19 + n20)
    a = round(group * share)
    return a, group - a


def harmonize_1901(rows, ref1911):
    r = rows
    def add(idx, col):
        return sum(r[i][col] for i in idx)
    out = {}
    for col, sesso in ((0, 'm'), (1, 'f')):
        ref = (ref1911[18][col + 1], ref1911[19][col + 1], ref1911[20][col + 1])
        a18_19, a20 = split_1882_80(r[17][col], ref)
        vals = [
            add([0, 1], col),            # 0 = nati 1901 + 1900
            add(range(2, 6), col),       # 1-4 = 1899-1896
            add(range(6, 11), col),      # 5-9 = 1895-1891
            add(range(11, 16), col),     # 10-14 = 1890-1886
            add([16], col) + a18_19,     # 15-19 = 1885-83 + eta' 18-19
            a20 + add([18], col),        # 20-24 = eta' 20 + 1879-76
            add([19], col), add([20], col), add([21], col), add([22], col),
            add([23], col), add([24], col), add([25], col), add([26], col),
            add([27], col), add([28], col), add([29], col), add([30], col),
            add(range(31, 35), col),     # 85+ = 1815-11 ... 1800
        ]
        out[sesso] = vals
    return {c: (out['m'][i], out['f'][i]) for i, c in enumerate(CLASSES)}


def main():
    t1911 = json.loads((HERE / 'trascrizioni_1911_citta.json').read_text())
    t1901 = json.loads((HERE / 'trascrizioni_1901_citta.json').read_text())

    new_rows = []
    for city, code in CITY_CODE.items():
        rows11 = t1911['dati'][city]
        check_1911(rows11)
        h11 = harmonize_1911(rows11)

        rows01 = t1901['dati'][city]
        check_1901(rows01)
        h01 = harmonize_1901(rows01, rows11)

        for year, h in (('1901', h01), ('1911', h11)):
            for cls in CLASSES:
                m, f = h[cls]
                new_rows.append({'year': year, 'code': code, 'city': city,
                                 'age_class': cls, 'male': m, 'female': f,
                                 'total': m + f})

    existing = list(csv.DictReader(OUT.open()))
    if any(r['year'] in ('1901', '1911') for r in existing):
        existing = [r for r in existing if r['year'] not in ('1901', '1911')]
    merged = existing + new_rows
    merged.sort(key=lambda r: (int(r['year']), r['code'], CLASSES.index(r['age_class'])))

    with OUT.open('w', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(['year', 'code', 'city', 'age_class', 'male', 'female', 'total'])
        for r in merged:
            w.writerow([r['year'], r['code'], r['city'], r['age_class'],
                        int(r['male']), int(r['female']), int(r['total'])])

    years = sorted({r['year'] for r in merged})
    print(f'{OUT}: {len(merged)} righe, anni {years}')
    for city in CITY_CODE:
        for y in ('1901', '1911'):
            tot = sum(int(r['total']) for r in merged
                      if r['city'] == city and r['year'] == y)
            print(f'  {y} {city}: {tot:,}')


if __name__ == '__main__':
    main()
