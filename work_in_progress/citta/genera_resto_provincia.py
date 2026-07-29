#!/usr/bin/env python3
"""Genera downloads/citta/data_census_resto_provincia.csv.

Per ogni (anno, città) del pannello città sottrae la città dalla sua
provincia, classe per classe: resto = provincia − comune capoluogo.
Copre gli anni presenti in ENTRAMBE le fonti (i 10 anni del pannello città).

Vincoli verificati riga per riga:
- la cella città non può superare la cella provincia (nessun negativo);
- male + female = total sia negli input sia nell'output.

Avvertenze ereditate dalle fonti (vedi work_in_progress/citta/README.md):
- concetto di popolazione: presente 1871-1931, residente 1936-1971, coerente
  tra città e provincia dello stesso anno;
- i confini comunali cambiano (annessioni anni '20-'30): il "resto provincia"
  eredita quelle discontinuità;
- classi stimate (1951/1961/1971 e confine 15-19/20-24 del 1901) combinano
  due stime nella sottrazione.
"""
import csv
from pathlib import Path

HERE = Path(__file__).parent
REPO = HERE.parent.parent
CITTA = REPO / 'downloads' / 'citta' / 'data_census_citta.csv'
OUT = REPO / 'downloads' / 'citta' / 'data_census_resto_provincia.csv'

CLASSES = ['0', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34',
           '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69',
           '70-74', '75-79', '80-84', '85+']


def main():
    citta = list(csv.DictReader(CITTA.open()))
    years = sorted({r['year'] for r in citta})

    out_rows, errors, warnings = [], [], []
    for year in years:
        prov = {}
        src = REPO / 'downloads' / year / f'data_census_{year}_adjusted_age.csv'
        for r in csv.DictReader(src.open()):
            key = (r['code'].zfill(3), r['age_class'])
            prov[key] = (r['province'], int(r['male']), int(r['female']),
                         int(r['total']))

        for r in (x for x in citta if x['year'] == year):
            key = (r['code'].zfill(3), r['age_class'])
            if key not in prov:
                errors.append(f'{year} {r["city"]} {r["age_class"]}: '
                              'classe assente nella provincia')
                continue
            pname, pm, pf, pt = prov[key]
            cm, cf, ct = int(r['male']), int(r['female']), int(r['total'])
            rm, rf, rt = pm - cm, pf - cf, pt - ct
            if min(rm, rf, rt) < 0:
                errors.append(f'{year} {r["city"]} {r["age_class"]}: '
                              f'resto negativo ({rm},{rf},{rt})')
                continue
            if rm + rf != rt:
                # incoerenza m+f != total gia' presente nella FONTE provinciale
                # (politica del progetto: si tiene com'e' e si segnala)
                warnings.append(f'{year} {r["city"]} {r["age_class"]}: '
                                f'{rm}+{rf} != {rt} (delta {rt-rm-rf:+}, '
                                'ereditato dalla fonte provinciale)')
            out_rows.append([year, r['code'].zfill(3), pname, r['city'],
                             r['age_class'], rm, rf, rt])

    if errors:
        print(f'{len(errors)} errori bloccanti:')
        for e in errors[:20]:
            print(' ', e)
        raise SystemExit(1)
    for wmsg in warnings:
        print('AVVISO:', wmsg)

    out_rows.sort(key=lambda x: (int(x[0]), x[1], CLASSES.index(x[4])))
    with OUT.open('w', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(['year', 'code', 'province', 'city_excluded', 'age_class',
                    'male', 'female', 'total'])
        for row in out_rows:
            w.writerow(row[:5] + [int(v) for v in row[5:]])

    print(f'{OUT}: {len(out_rows)} righe, anni {years}')
    for year in years:
        tot = sum(r[7] for r in out_rows if r[0] == year)
        print(f'  {year}: resto provincia (13 province) = {tot:,}')


if __name__ == '__main__':
    main()
