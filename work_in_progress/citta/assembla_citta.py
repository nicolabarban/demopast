"""Assembla downloads/citta/data_census_citta.csv dalle trascrizioni per citta'.

Porta le classi di eta' originali di ciascun censimento sui 19 gruppi standard
DEMOPAST. Cinque anni (1871, 1881, 1921, 1931, 1936) hanno gli anni singoli e si
aggregano ESATTAMENTE. Tre (1951, 1961, 1971) hanno classi che non si allineano ai
19 gruppi e vanno redistribuiti: come donatore di forma si usa il profilo per eta'
della PROVINCIA della citta' nello stesso anno (che i 19 gruppi ce li ha), con
largest-remainder per mantenere i totali esatti.
"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

AGES = ['0', '1_4', '5_9', '10_14', '15_19', '20_24', '25_29', '30_34', '35_39',
        '40_44', '45_49', '50_54', '55_59', '60_64', '65_69', '70_74', '75_79',
        '80_84', '85plus']
LABEL = {'0': '0', '1_4': '1-4', '5_9': '5-9', '10_14': '10-14', '15_19': '15-19',
         '20_24': '20-24', '25_29': '25-29', '30_34': '30-34', '35_39': '35-39',
         '40_44': '40-44', '45_49': '45-49', '50_54': '50-54', '55_59': '55-59',
         '60_64': '60-64', '65_69': '65-69', '70_74': '70-74', '75_79': '75-79',
         '80_84': '80-84', '85plus': '85+'}
# estremi [a, b) di ciascuno dei 19 gruppi; l'ultimo e' troncato a 100
BOUNDS = [(0, 1), (1, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35),
          (35, 40), (40, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70),
          (70, 75), (75, 80), (80, 85), (85, 100)]

# codice della provincia di cui ogni citta' e' capoluogo: e' anche la chiave di join
COD = {'Torino': 1, 'Genova': 10, 'Milano': 15, 'Venezia': 27, 'Bologna': 37,
       'Firenze': 48, 'Livorno': 49, 'Roma': 58, 'Napoli': 63, 'Bari': 72,
       'Palermo': 82, 'Messina': 83, 'Catania': 87}

# classi originali [a, b) degli anni che vanno redistribuiti
CLASSI_1951 = [(0, 6), (6, 10), (10, 14), (14, 18), (18, 21), (21, 25), (25, 35),
               (35, 45), (45, 55), (55, 60), (60, 65), (65, 100)]
CLASSI_1961 = [(0, 6), (6, 14), (14, 21), (21, 25), (25, 30), (30, 35), (35, 40),
               (40, 45), (45, 50), (50, 55), (55, 60), (60, 65), (65, 70), (70, 75),
               (75, 100)]


def largest_remainder(count, shares):
    """Ripartisce `count` interi secondo `shares`, mantenendo la somma esatta."""
    if count == 0 or not shares:
        return [0] * len(shares)
    tot = sum(shares)
    if tot <= 0:                       # donatore vuoto: ripartizione uniforme
        shares = [1.0] * len(shares)
        tot = float(len(shares))
    raw = [count * s / tot for s in shares]
    out = [int(x) for x in raw]
    resto = count - sum(out)
    for i in sorted(range(len(raw)), key=lambda i: raw[i] - out[i], reverse=True)[:resto]:
        out[i] += 1
    return out


def profilo_annuale(riga, sesso):
    """Profilo per singolo anno di eta' (0..99) implicito nei 19 gruppi di una riga
    provinciale: ogni gruppo e' spalmato uniformemente sui propri anni."""
    prof = [0.0] * 100
    for a, (lo, hi) in zip(AGES, BOUNDS):
        v = float(riga[f'{sesso}_{a}'])
        for eta in range(lo, hi):
            prof[eta] += v / (hi - lo)
    return prof


def redistribuisci(valori, classi, prof):
    """Da classi irregolari a 19 gruppi, usando `prof` come forma entro ogni classe.
    Ogni classe originale e' ripartita sui suoi anni singoli in proporzione al
    donatore, poi gli anni si riaggregano nei 19 gruppi. I totali restano esatti:
    nessun individuo entra o esce da una classe originale."""
    per_eta = [0] * 100
    for v, (lo, hi) in zip(valori, classi):
        quote = largest_remainder(v, prof[lo:hi])
        for i, q in enumerate(quote):
            per_eta[lo + i] += q
    return [sum(per_eta[lo:hi]) for lo, hi in BOUNDS]


def carica_provincia(anno):
    with open(f'{ROOT}/data/census/census_{anno}.csv') as f:
        return {int(r['COD_PROV']): r for r in csv.DictReader(f)}


# --- aggregazioni esatte, una per anno --------------------------------------

def agg_1871(d):
    """12 righe mensili + 99 anni singoli + centenari. Esatta."""
    mesi, sing, cent = d['mesi'], d['singoli'], d['centenari']
    per_eta = [sum(mesi)] + list(sing)          # indice = eta', 0..99
    per_eta[99] += cent                         # i centenari confluiscono in 85+
    return [sum(per_eta[lo:hi]) for lo, hi in BOUNDS]


def agg_1881(d):
    """eta' 0 stampata + subtotali quinquennali stampati + centenari. Esatta."""
    sub = d['subtotali']                        # [0]=0-4, [1]=5-9, ... [19]=95-99
    eta0 = d['singoli_0_4'][0]
    out = [eta0, sub[0] - eta0] + sub[1:16]     # 0, 1-4, 5-9 ... 75-79
    out.append(sub[16])                         # 80-84
    out.append(sub[17] + sub[18] + sub[19] + d['centenari'])   # 85+
    return out


def agg_1921(d):
    """21 anni singoli (0..20) + quinquenni sfalsati + oltre 100. Esatta:
    la classe stampata 21-25 copre gli anni 21-24, quindi 20-24 = eta'20 + 21-25."""
    v = d['valori']
    out = [v[0], sum(v[1:5]), sum(v[5:10]), sum(v[10:15]), sum(v[15:20]),
           v[20] + v[21]]                       # 20-24 = anno 20 + classe 21-25
    out += v[22:34]                             # 25-29 ... 80-84
    out.append(v[34] + v[35] + v[36] + v[37])   # 85+ = 85-90, 90-95, 95-100, oltre 100
    return out


def agg_1931(d):
    """21 anni singoli (0..20) + classi 21-24, 25-29 ... + 100 e oltre. Esatta."""
    v = d['valori']
    out = [v[0], sum(v[1:5]), sum(v[5:10]), sum(v[10:15]), sum(v[15:20]),
           v[20] + v[21]]                       # 20-24 = anno 20 + classe 21-24
    out += v[22:34]                             # 25-29 ... 80-84
    out.append(v[34] + v[35] + v[36] + v[37])   # 85+ = 85-89 ... 100 e oltre
    return out


def agg_1936(d):
    """75 anni singoli (0..74) + classi terminali. Esatta."""
    v = d['valori']
    out = [v[0], sum(v[1:5])]
    out += [sum(v[i:i + 5]) for i in range(5, 75, 5)]   # 5-9 ... 70-74
    out += [v[75], v[76]]                                # 75-79, 80-84
    out.append(v[77] + v[78] + v[79] + v[80])            # 85+
    return out


def main() -> None:
    tr = {a: json.load(open(f'{HERE}/trascrizioni_{a}_citta.json'))
          for a in (1871, 1881, 1921, 1931, 1936, 1951, 1961, 1971)}
    prov = {a: carica_provincia(a) for a in (1951, 1961, 1971)}

    righe, report, errori = [], [], []
    for anno in (1871, 1881, 1921, 1931, 1936, 1951, 1961, 1971):
        for citta, cod in sorted(COD.items(), key=lambda x: x[1]):
            d = tr[anno].get(citta)
            if d is None:
                errori.append(f'{anno}/{citta}: trascrizione assente')
                continue
            out, stimate, ignote = {}, False, 0
            for s, key in (('m', 'maschi'), ('f', 'femmine')):
                dd = d[key]
                # persone senza eta' dichiarata: non appartengono ad alcuna classe,
                # quindi restano fuori dai 19 gruppi. Le contiamo per trasparenza.
                ign = {1871: dd.get('eta_ignote', 0),
                       1881: dd.get('eta_ignota', 0),
                       1921: dd['valori'][38] if anno == 1921 else 0,
                       1931: dd['valori'][38] if anno == 1931 else 0,
                       1936: dd['valori'][81] if anno == 1936 else 0,
                       1951: 0, 1961: 0, 1971: 0}[anno]
                ignote += ign
                if anno == 1871:
                    g = agg_1871(dd)
                elif anno == 1881:
                    g = agg_1881(dd)
                elif anno == 1921:
                    g = agg_1921(dd)
                elif anno == 1931:
                    g = agg_1931(dd)
                elif anno == 1936:
                    g = agg_1936(dd)
                else:
                    stimate = True
                    p = profilo_annuale(prov[anno][cod], s)
                    if anno == 1971:
                        # 16 quinquennali: solo <5 e 75+ sono aperte
                        v = dd['valori']
                        g0 = largest_remainder(v[0], p[0:5])
                        g75 = largest_remainder(v[15], p[75:100])
                        g = [g0[0], sum(g0[1:5])] + list(v[1:15]) + \
                            [sum(g75[0:5]), sum(g75[5:10]), sum(g75[10:25])]
                    else:
                        classi = CLASSI_1951 if anno == 1951 else CLASSI_1961
                        g = redistribuisci(dd['valori'], classi, p)
                # nessun individuo con eta' nota deve perdersi in aggregazione
                atteso = dd.get('totale_stampato', dd.get('in_complesso_stampato',
                                dd.get('complesso_stampato'))) - ign
                if sum(g) != atteso:
                    errori.append(f'{anno}/{citta}/{key}: aggregato {sum(g)} != '
                                  f'atteso {atteso} (stampato meno {ign} di eta\' ignota)')
                out[s] = g
            tot = sum(out['m']) + sum(out['f'])
            report.append((anno, citta, tot, stimate, ignote))
            for i, a in enumerate(AGES):
                righe.append({'year': anno, 'code': f'{cod:03d}', 'city': citta,
                              'age_class': LABEL[a], 'male': out['m'][i],
                              'female': out['f'][i], 'total': out['m'][i] + out['f'][i]})

    if errori:
        print('BLOCCATO — non scrivo:')
        for e in errori:
            print(' ', e)
        raise SystemExit(1)

    dst = f'{ROOT}/downloads/citta/data_census_citta.csv'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'w', newline='') as f:
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(['year', 'code', 'city', 'age_class', 'male', 'female', 'total'])
        for r in righe:
            w.writerow([r['year'], r['code'], r['city'], r['age_class'],
                        r['male'], r['female'], r['total']])
    print(f'scritte {len(righe)} righe -> {dst}')
    print(f'{len(report)} coppie citta-anno (13 citta x 8 anni = 104)\n')
    for anno in (1871, 1881, 1921, 1931, 1936, 1951, 1961, 1971):
        tot = sum(t for a, _, t, _, _ in report if a == anno)
        ign = sum(i for a, _, _, _, i in report if a == anno)
        st = 'STIMATA ' if any(s for a, _, _, s, _ in report if a == anno) else 'esatta  '
        nota = f'  (+{ign:,} di eta\' ignota, fuori dalle classi)' if ign else ''
        print(f'  {anno}: 13 citta\' = {tot:>10,}   armonizzazione {st}{nota}')


if __name__ == '__main__':
    main()
