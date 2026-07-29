#!/usr/bin/env python3
"""Applica un registro di correzioni ai CSV adjusted_age in downloads/.

Uso: python3 scripts/apply_corrections.py <correzioni.json>

Formato del registro: {anno: {code: {age_class: {campo: valore, ...}}}}
dove campo è male/female/total. Ogni correzione è applicata alla riga
(age_class, code) di downloads/{anno}/data_census_{anno}_adjusted_age.csv;
lo script verifica che il valore precedente fosse incoerente (m+f != t) e
che quello nuovo chiuda la riga, e stampa un report.
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent


def main(ledger_path):
    ledger = json.loads(Path(ledger_path).read_text())
    for year, provs in sorted(ledger.items()):
        path = REPO / 'downloads' / year / f'data_census_{year}_adjusted_age.csv'
        rows = list(csv.DictReader(path.open()))
        fields = rows[0].keys()
        n = 0
        for r in rows:
            fix = provs.get(r['code'], {}).get(r['age_class'])
            if not fix:
                continue
            old = {k: int(r[k]) for k in ('male', 'female', 'total')}
            for k, v in fix.items():
                r[k] = str(v)
            new = {k: int(r[k]) for k in ('male', 'female', 'total')}
            status = 'OK' if new['male'] + new['female'] == new['total'] else 'ANCORA INCOERENTE'
            print(f"{year} {r['province']:18s} {r['age_class']:6s} "
                  f"{old} -> {new}  [{status}]")
            n += 1
        expected = sum(len(c) for c in provs.values())
        if n != expected:
            raise SystemExit(f'{year}: applicate {n} correzioni, attese {expected}')
        numeric = ('male', 'female', 'total')
        with path.open('w', newline='') as fh:
            w = csv.writer(fh, quoting=csv.QUOTE_NONNUMERIC)
            w.writerow(fields)
            for r in rows:
                w.writerow([int(r[k]) if k in numeric else r[k] for k in fields])
        print(f'{year}: {n} correzioni scritte in {path.name}')


if __name__ == '__main__':
    main(sys.argv[1])
