"""Assembla downloads/1971 dalle trascrizioni Tav.3 (16 classi quinquennali).
Split degli estremi: <5 -> 0/1-4 e 75+ -> 75-79/80-84/85+ con le proporzioni
1961 della stessa provincia (largest remainder, totali esatti)."""
import csv, json
from collections import defaultdict

S = '/private/tmp/claude-501/-Users-nicolabarban-Dropbox-demopasta/a01aba59-e75d-40e3-b7ba-c10937ca1f04/scratchpad'
RES = json.load(open(f'{S}/trascrizioni_1971.json'))
REF = json.load(open(f'{S}/ref_1971.json'))

AGES = ['0','1_4','5_9','10_14','15_19','20_24','25_29','30_34','35_39','40_44',
        '45_49','50_54','55_59','60_64','65_69','70_74','75_79','80_84','85plus']
LABEL = {'0':'0','1_4':'1-4','5_9':'5-9','10_14':'10-14','15_19':'15-19','20_24':'20-24',
         '25_29':'25-29','30_34':'30-34','35_39':'35-39','40_44':'40-44','45_49':'45-49',
         '50_54':'50-54','55_59':'55-59','60_64':'60-64','65_69':'65-69','70_74':'70-74',
         '75_79':'75-79','80_84':'80-84','85plus':'85+'}
# le 16 classi Tav.3: indice -> classi 19 di destinazione
MID = ['5_9','10_14','15_19','20_24','25_29','30_34','35_39','40_44','45_49','50_54','55_59','60_64','65_69','70_74']

def lr_split(count, shares):
    raw = [count * s for s in shares]
    flo = [int(x) for x in raw]
    for i in sorted(range(len(raw)), key=lambda i: raw[i]-flo[i], reverse=True)[:count - sum(flo)]:
        flo[i] += 1
    return flo

# proporzioni 1961 per gli split, dalla stessa provincia
c61 = {int(r['COD_PROV']): r for r in csv.DictReader(open('/Users/nicolabarban/Dropbox/demopasta/data/census/census_1961.csv'))}
# nomi provincia dal geojson 1971
import json as j2
gj = j2.load(open('/Users/nicolabarban/Dropbox/demopasta/data/geojson/province_1971.geojson'))
geo_names = {f['properties']['COD_PROV']: f['properties']['DEN_PROV'] for f in gj['features']}
NAME2COD = {v: k for k, v in geo_names.items()}
ALIAS = {"Valle d'Aosta": 7, "L'Aquila": 66, "Ascoli Piceno": 44, "Bolzano": 21,
         "Reggio di Calabria": 80, "Reggio nell'Emilia": 35, "Pesaro e Urbino": 41,
         "Massa-Carrara": 45, "Forlì": 40, "La Spezia": 11, "Monza"[:0]: None}

rows_out = []
report = []
for name, res in sorted(RES.items()):
    cod = NAME2COD.get(name) or ALIAS.get(name)
    if cod is None:
        cand = [k for n, k in NAME2COD.items() if n.replace(' ','').lower() == name.replace(' ','').lower()]
        cod = cand[0] if cand else None
    assert cod, f"provincia non mappata: {name}"
    out = {}
    for s, key in (('m','maschi'), ('f','femmine')):
        vals = res[key]['valori']
        tot = res[key]['totale_stampato']
        assert len(vals) == 16 and sum(vals) == tot, (name, s)
        d = {}
        # split <5 con proporzioni 1961 (fallback: provincia 1961 stessa; per Pordenone/Isernia usa madre)
        base = cod if cod in c61 else {93: 30, 94: 70}[cod]
        r61 = c61[base]
        p0 = int(r61[f'{s}_0']); p14 = int(r61[f'{s}_1_4'])
        d['0'], d['1_4'] = lr_split(vals[0], [p0/(p0+p14), p14/(p0+p14)])
        for i, a in enumerate(MID):
            d[a] = vals[1+i]
        p75 = int(r61[f'{s}_75_79']); p80 = int(r61[f'{s}_80_84']); p85 = int(r61[f'{s}_85plus'])
        tp = p75+p80+p85
        d['75_79'], d['80_84'], d['85plus'] = lr_split(vals[15], [p75/tp, p80/tp, p85/tp])
        assert sum(d.values()) == tot, (name, s)
        out[s] = d
    grand = sum(out['m'].values()) + sum(out['f'].values())
    delta = grand - REF[str(cod)]
    report.append((cod, name, grand, delta))
    for a in AGES:
        rows_out.append({'code': f"{cod:03d}", 'province': geo_names[cod], 'age_class': LABEL[a],
                         'male': out['m'][a], 'female': out['f'][a], 'total': out['m'][a]+out['f'][a]})

rows_out.sort(key=lambda r: (r['code'], AGES.index(next(k for k,v in LABEL.items() if v==r['age_class']))))
dst = '/Users/nicolabarban/Dropbox/demopasta/downloads/1971/data_census_1971_adjusted_age.csv'
import os
os.makedirs(os.path.dirname(dst), exist_ok=True)
with open(dst, 'w', newline='') as f:
    w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    w.writerow(['code','province','age_class','male','female','total'])
    for r in rows_out:
        w.writerow([r['code'], r['province'], r['age_class'], r['male'], r['female'], r['total']])
print(f"scritte {len(rows_out)} righe ({len(rows_out)//19} province)")
bad = [(c,n,g,d) for c,n,g,d in report if abs(d) > 200]
print(f"province con |delta| > 200 vs riferimento: {len(bad)}")
for c,n,g,d in sorted(bad, key=lambda x: -abs(x[3])):
    print(f"  {c:>3} {n:<20} {g:>10,} ({d:+,})")
