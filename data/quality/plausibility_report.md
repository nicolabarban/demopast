# DEMOPAST data plausibility report

Flags: **36 ERROR**, 465 WARNING, 314 INFO

## ERROR (36)

| dataset | where | check | detail |
|---|---|---|---|
| census | Palermo 1861->1871 | intercensal_jump | 384,526 -> 617,618 (x1.61) |
| census | AscoliPiceno 1931 | t_0!=m+f | 7,641 != 3,765+3,696 (off 180) |
| census | Piacenza 1921 | t_10_14!=m+f | 32,152 != 16,871+15,881 (off 600) |
| census | Venezia 1921 | t_10_14!=m+f | 58,411 != 29,590+29,181 (off 360) |
| census | Vicenza 1921 | t_10_14!=m+f | 66,074 != 33,580+32,994 (off 500) |
| census | Rovigo 1921 | t_15_19!=m+f | 30,248 != 15,184+14,884 (off 180) |
| census | AscoliPiceno 1931 | t_1_4!=m+f | 27,610 != 14,286+13,504 (off 180) |
| census | Catania 1936 | t_1_4!=m+f | 63,096 != 24,025+30,869 (off 8,202) |
| census | Terni 1936 | t_30_34!=m+f | 13,024 != 6,708+6,816 (off 500) |
| census | Cosenza 1936 | t_35_39!=m+f | 25,459 != 13,311+18,278 (off 6,130) |
| census | ReggioCalabria 1911 | t_40_44!=m+f | 22,375 != 10,818+12,557 (off 1,000) |
| census | Enna 1936 | t_55_59!=m+f | 7,278 != 4,422+3,728 (off 872) |
| census | Massa e Carrara 1921 | t_5_9!=m+f | 25,559 != 13,271+12,888 (off 600) |
| census | PrincipatoUlteriore 1871 | t_5_9!=m+f | 40,436 != 13,687+19,929 (off 6,820) |
| census | Siracusa 1921 | t_70_74!=m+f | 9,870 != 5,028+4,942 (off 100) |
| census | Catania 1936 | total!=M+F | 713,108 != 343,463+361,443 (off 8,202) |
| census | Cosenza 1936 | total!=M+F | 580,763 != 280,256+306,637 (off 6,130) |
| census | Enna 1936 | total!=M+F | 216,240 != 110,509+106,603 (off 872) |
| census | Massa e Carrara 1921 | total!=M+F | 223,346 != 110,053+113,893 (off 600) |
| census | Piacenza 1921 | total!=M+F | 280,483 != 142,209+138,864 (off 590) |
| census | PrincipatoUlteriore 1871 | total!=M+F | 377,207 != 179,187+191,200 (off 6,820) |
| census | ReggioCalabria 1911 | total!=M+F | 443,611 != 212,964+231,647 (off 1,000) |
| census | Terni 1936 | total!=M+F | 191,547 != 97,260+94,787 (off 500) |
| fertility | Fiume 1931 | cbr_implausible | cbr=5.8 |
| fertility | Mantova 1865 | cbr_implausible | cbr=5.16 |
| marriages | Ferrara 1866 | nuptiality_implausible | nuptiality=1.68 |
| marriages | Fiume 1931 | nuptiality_implausible | nuptiality=1.93 |
| marriages | Girgenti 1866 | nuptiality_implausible | nuptiality=2.53 |
| marriages | Mantova 1865 | nuptiality_implausible | nuptiality=1.2 |
| marriages | Pesaro e Urbino 1866 | nuptiality_implausible | nuptiality=2.94 |
| marriages | Roma 1872 | nuptiality_implausible | nuptiality=2.98 |
| migration | Belluno 1911 | emig_rate_implausible | emig_rate=87.24 |
| migration | Belluno 1912 | emig_rate_implausible | emig_rate=87.25 |
| migration | Belluno 1913 | emig_rate_implausible | emig_rate=94.07 |
| migration | Belluno 1914 | emig_rate_implausible | emig_rate=82.21 |
| mortality | Trapani 1881 | cdr_implausible | cdr=0.95 |

## WARNING (465)

| dataset | where | check | detail |
|---|---|---|---|
| census | Catania 1921->1931 | intercensal_growth | -2.35%/yr (869,684 -> 685,369) |
| census | Como 1921->1931 | intercensal_growth | -2.52%/yr (628,980 -> 487,186) |
| census | Cremona 1931->1936 | intercensal_growth | -1.62%/yr (400,834 -> 369,466) |
| census | Firenze 1921->1931 | intercensal_growth | -2.07%/yr (1,035,968 -> 840,043) |
| census | Genova 1921->1931 | intercensal_growth | -3.38%/yr (1,171,838 -> 831,269) |
| census | Girgenti 1861->1871 | intercensal_growth | -2.66%/yr (376,957 -> 287,763) |
| census | MassaCarrara 1921->1931 | intercensal_growth | -1.62%/yr (223,346 -> 189,622) |
| census | Napoli 1921->1931 | intercensal_growth | +3.56%/yr (1,461,112 -> 2,073,825) |
| census | Perugia 1921->1931 | intercensal_growth | -3.48%/yr (733,696 -> 514,830) |
| census | Potenza 1921->1931 | intercensal_growth | -2.83%/yr (467,098 -> 350,618) |
| census | Teramo 1921->1931 | intercensal_growth | -3.40%/yr (319,988 -> 226,401) |
| census | Trieste 1931->1936 | intercensal_growth | +5.74%/yr (348,405 -> 460,596) |
| census | Alessandria 1931->1936 | intercensal_jump | 755,968 -> 494,688 (x0.65) (possible 1927/1935 boundary change) |
| census | Caltanissetta 1921->1931 | intercensal_jump | 382,444 -> 245,476 (x0.64) (possible 1927/1935 boundary change) |
| census | Firenze 1931->1936 | intercensal_jump | 840,043 -> 322,526 (x0.38) (possible 1927/1935 boundary change) |
| census | Lecce 1921->1931 | intercensal_jump | 877,583 -> 487,029 (x0.55) (possible 1927/1935 boundary change) |
| census | Livorno 1921->1931 | intercensal_jump | 143,190 -> 245,707 (x1.72) (possible 1927/1935 boundary change) |
| census | Novara 1921->1931 | intercensal_jump | 723,269 -> 389,312 (x0.54) (possible 1927/1935 boundary change) |
| census | Siracusa 1921->1931 | intercensal_jump | 526,953 -> 284,193 (x0.54) (possible 1927/1935 boundary change) |
| census | Girgenti 1861 | mean_age | 42.7 |
| census | COD_PROV 14 1881 | province_missing | present in 1871 and 1901, absent in 1881 (Sondrio) |
| census | Aquila 1881 | sex_ratio | M/F = 87.0 per 100 |
| census | Aquila 1901 | sex_ratio | M/F = 87.9 per 100 |
| census | Aquila 1911 | sex_ratio | M/F = 86.9 per 100 |
| census | AquiladegliAbruzzi 1871 | sex_ratio | M/F = 87.8 per 100 |
| census | Belluno 1911 | sex_ratio | M/F = 81.8 per 100 |
| census | Belluno 1931 | sex_ratio | M/F = 86.9 per 100 |
| census | Caltanissetta 1861 | sex_ratio | M/F = 113.0 per 100 |
| census | Campobasso 1901 | sex_ratio | M/F = 88.0 per 100 |
| census | Campobasso 1911 | sex_ratio | M/F = 83.8 per 100 |
| census | Campobasso 1931 | sex_ratio | M/F = 87.5 per 100 |
| census | Catanzaro 1911 | sex_ratio | M/F = 85.3 per 100 |
| census | Chieti 1911 | sex_ratio | M/F = 85.5 per 100 |
| census | Chieti 1931 | sex_ratio | M/F = 83.9 per 100 |
| census | Cosenza 1901 | sex_ratio | M/F = 84.8 per 100 |
| census | Cosenza 1911 | sex_ratio | M/F = 84.1 per 100 |
| census | Cosenza 1931 | sex_ratio | M/F = 87.8 per 100 |
| census | Cremona 1931 | sex_ratio | M/F = 80.9 per 100 |
| census | Firenze 1936 | sex_ratio | M/F = 85.4 per 100 |
| census | Girgenti 1861 | sex_ratio | M/F = 153.8 per 100 |
| census | Grosseto 1861 | sex_ratio | M/F = 135.4 per 100 |
| census | Grosseto 1871 | sex_ratio | M/F = 130.3 per 100 |
| census | Grosseto 1881 | sex_ratio | M/F = 129.0 per 100 |
| census | Grosseto 1901 | sex_ratio | M/F = 120.1 per 100 |
| census | Lucca 1911 | sex_ratio | M/F = 87.6 per 100 |
| census | Lucca 1931 | sex_ratio | M/F = 87.8 per 100 |
| census | Novara 1911 | sex_ratio | M/F = 85.9 per 100 |
| census | Palermo 1861 | sex_ratio | M/F = 298.5 per 100 |
| census | Roma 1871 | sex_ratio | M/F = 115.9 per 100 |
| census | Roma 1881 | sex_ratio | M/F = 113.6 per 100 |
| census | Udine 1911 | sex_ratio | M/F = 83.0 per 100 |
| census | Girgenti 1861 | share_50_54 | 17.0% in one 5-year group |
| census | Campobasso 1936 | share_age0 | 5.02% of population aged 0 |
| census | Firenze 1936 | share_age0 | 1.20% of population aged 0 |
| fertility | Alessandria 1931 | cbr_range | cbr=15.21 |
| fertility | Aosta 1931 | cbr_range | cbr=17.81 |
| fertility | Bologna 1931 | cbr_range | cbr=18.51 |
| fertility | Firenze 1931 | cbr_range | cbr=16.76 |
| fertility | Genova 1931 | cbr_range | cbr=14.61 |
| fertility | La Spezia 1931 | cbr_range | cbr=18.31 |
| fertility | Livorno 1931 | cbr_range | cbr=18.01 |
| fertility | Lucca 1931 | cbr_range | cbr=19.59 |
| fertility | Milano 1931 | cbr_range | cbr=19.68 |
| fertility | Novara 1921 | cbr_range | cbr=18.76 |
| fertility | Novara 1931 | cbr_range | cbr=16.54 |
| fertility | Parma 1931 | cbr_range | cbr=19.45 |
| fertility | Pavia 1921 | cbr_range | cbr=19.68 |
| fertility | Pavia 1931 | cbr_range | cbr=16.12 |
| fertility | Pisa 1931 | cbr_range | cbr=18.44 |
| fertility | Pistoia 1931 | cbr_range | cbr=18.79 |
| fertility | Porto Maurizio 1921 | cbr_range | cbr=19.04 |
| fertility | Porto Maurizio 1931 | cbr_range | cbr=15.78 |
| fertility | Ravenna 1931 | cbr_range | cbr=15.84 |
| fertility | Savona 1931 | cbr_range | cbr=16.71 |
| fertility | Sondrio 1881 | cbr_range | cbr=19.67 |
| fertility | Torino 1921 | cbr_range | cbr=18.62 |
| fertility | Torino 1931 | cbr_range | cbr=15.07 |
| fertility | Varese 1931 | cbr_range | cbr=17.87 |
| fertility | Vercelli 1931 | cbr_range | cbr=14.63 |
| fertility | Benevento 1880->1881 | yoy_jump | cbr 30.49 -> 41.87 |
| fertility | Mantova 1864->1865 | yoy_jump | cbr 20.44 -> 5.16 |
| fertility | Mantova 1865->1866 | yoy_jump | cbr 5.16 -> 21.35 |
| fertility | Mantova 1868->1869 | yoy_jump | cbr 21.8 -> 37.53 |
| fertility | Sondrio 1880->1881 | yoy_jump | cbr 36.82 -> 19.67 |
| marriages | Alessandria 1921 | nuptiality_range | nuptiality=13.45 |
| marriages | Ancona 1866 | nuptiality_range | nuptiality=4.1 |
| marriages | Ancona 1868 | nuptiality_range | nuptiality=4.19 |
| marriages | Ancona 1921 | nuptiality_range | nuptiality=12.26 |
| marriages | Arezzo 1866 | nuptiality_range | nuptiality=3.76 |
| marriages | Arezzo 1921 | nuptiality_range | nuptiality=13.39 |
| marriages | Ascoli Piceno 1866 | nuptiality_range | nuptiality=3.33 |
| marriages | Ascoli Piceno 1867 | nuptiality_range | nuptiality=3.87 |
| marriages | Ascoli Piceno 1868 | nuptiality_range | nuptiality=3.77 |
| marriages | Ascoli Piceno 1870 | nuptiality_range | nuptiality=3.78 |
| marriages | Ascoli Piceno 1871 | nuptiality_range | nuptiality=3.33 |
| marriages | Avellino 1921 | nuptiality_range | nuptiality=12.18 |
| marriages | Belluno 1921 | nuptiality_range | nuptiality=13.12 |
| marriages | Benevento 1921 | nuptiality_range | nuptiality=12.24 |
| marriages | Bergamo 1921 | nuptiality_range | nuptiality=12.77 |
| marriages | Bologna 1866 | nuptiality_range | nuptiality=4.49 |
| marriages | Brescia 1921 | nuptiality_range | nuptiality=12.34 |
| marriages | Cagliari 1866 | nuptiality_range | nuptiality=3.63 |
| marriages | Caltanissetta 1866 | nuptiality_range | nuptiality=3.86 |
| marriages | Campobasso 1921 | nuptiality_range | nuptiality=12.27 |
| marriages | Catania 1866 | nuptiality_range | nuptiality=3.37 |
| marriages | Catania 1867 | nuptiality_range | nuptiality=3.74 |
| marriages | Como 1921 | nuptiality_range | nuptiality=12.48 |
| marriages | Cosenza 1921 | nuptiality_range | nuptiality=14.16 |
| marriages | Cremona 1921 | nuptiality_range | nuptiality=12.43 |
| marriages | Cuneo 1921 | nuptiality_range | nuptiality=12.38 |
| marriages | Firenze 1921 | nuptiality_range | nuptiality=12.5 |
| marriages | Forlì 1866 | nuptiality_range | nuptiality=3.13 |
| marriages | Forlì 1867 | nuptiality_range | nuptiality=3.67 |
| marriages | Forlì 1868 | nuptiality_range | nuptiality=4.35 |
| marriages | Forlì 1871 | nuptiality_range | nuptiality=4.33 |
| marriages | Girgenti 1867 | nuptiality_range | nuptiality=3.92 |
| marriages | Grosseto 1866 | nuptiality_range | nuptiality=3.36 |
| marriages | Grosseto 1921 | nuptiality_range | nuptiality=13.15 |
| marriages | Lucca 1866 | nuptiality_range | nuptiality=3.77 |
| marriages | Lucca 1921 | nuptiality_range | nuptiality=12.07 |
| marriages | Macerata 1870 | nuptiality_range | nuptiality=4.42 |
| marriages | Macerata 1921 | nuptiality_range | nuptiality=12.59 |
| marriages | Massa e Carrara 1866 | nuptiality_range | nuptiality=3.85 |
| marriages | Massa e Carrara 1921 | nuptiality_range | nuptiality=12.95 |
| marriages | Novara 1921 | nuptiality_range | nuptiality=13.49 |
| marriages | Palermo 1866 | nuptiality_range | nuptiality=3.76 |
| marriages | Pavia 1921 | nuptiality_range | nuptiality=12.9 |
| marriages | Pesaro e Urbino 1867 | nuptiality_range | nuptiality=3.25 |
| marriages | Pesaro e Urbino 1868 | nuptiality_range | nuptiality=3.23 |
| marriages | Pesaro e Urbino 1869 | nuptiality_range | nuptiality=3.83 |
| marriages | Pesaro e Urbino 1870 | nuptiality_range | nuptiality=4.02 |
| marriages | Pesaro e Urbino 1871 | nuptiality_range | nuptiality=4.09 |
| marriages | Pesaro e Urbino 1921 | nuptiality_range | nuptiality=12.75 |
| marriages | Pisa 1866 | nuptiality_range | nuptiality=4.37 |
| marriages | Pisa 1921 | nuptiality_range | nuptiality=12.74 |
| marriages | Potenza 1921 | nuptiality_range | nuptiality=12.6 |
| marriages | Ravenna 1866 | nuptiality_range | nuptiality=3.53 |
| marriages | Ravenna 1867 | nuptiality_range | nuptiality=4.03 |
| marriages | Ravenna 1868 | nuptiality_range | nuptiality=4.44 |
| marriages | Roma 1873 | nuptiality_range | nuptiality=3.72 |
| marriages | Roma 1874 | nuptiality_range | nuptiality=4.45 |
| marriages | Salerno 1921 | nuptiality_range | nuptiality=12.23 |
| marriages | Sassari 1866 | nuptiality_range | nuptiality=3.63 |
| marriages | Siena 1921 | nuptiality_range | nuptiality=14.62 |
| marriages | Siracusa 1866 | nuptiality_range | nuptiality=3.97 |
| marriages | Siracusa 1867 | nuptiality_range | nuptiality=3.47 |
| marriages | Trapani 1866 | nuptiality_range | nuptiality=3.88 |
| marriages | Treviso 1921 | nuptiality_range | nuptiality=13.35 |
| marriages | Udine 1921 | nuptiality_range | nuptiality=12.16 |
| marriages | Umbria 1921 | nuptiality_range | nuptiality=13.04 |
| marriages | Verona 1921 | nuptiality_range | nuptiality=12.37 |
| marriages | Vicenza 1921 | nuptiality_range | nuptiality=13.15 |
| marriages | Alessandria 1865->1866 | yoy_jump | nuptiality 10.68 -> 5.93 |
| marriages | Ancona 1865->1866 | yoy_jump | nuptiality 8.12 -> 4.1 |
| marriages | Aquila degli Abruzzi 1865->1866 | yoy_jump | nuptiality 8.35 -> 5.18 |
| marriages | Arezzo 1865->1866 | yoy_jump | nuptiality 9.19 -> 3.76 |
| marriages | Ascoli Piceno 1865->1866 | yoy_jump | nuptiality 7.32 -> 3.33 |
| marriages | Ascoli Piceno 1871->1872 | yoy_jump | nuptiality 3.33 -> 4.84 |
| marriages | Benevento 1880->1881 | yoy_jump | nuptiality 6.62 -> 10.57 |
| marriages | Bergamo 1865->1866 | yoy_jump | nuptiality 9.54 -> 5.64 |
| marriages | Bologna 1865->1866 | yoy_jump | nuptiality 7.97 -> 4.49 |
| marriages | Brescia 1865->1866 | yoy_jump | nuptiality 10.17 -> 5.77 |
| marriages | Brescia 1866->1867 | yoy_jump | nuptiality 5.77 -> 8.01 |
| marriages | Cagliari 1865->1866 | yoy_jump | nuptiality 10.04 -> 3.63 |
| marriages | Caltanissetta 1865->1866 | yoy_jump | nuptiality 7.93 -> 3.86 |
| marriages | Caltanissetta 1866->1867 | yoy_jump | nuptiality 3.86 -> 5.64 |
| marriages | Caltanissetta 1867->1868 | yoy_jump | nuptiality 5.64 -> 8.09 |
| marriages | Caltanissetta 1868->1869 | yoy_jump | nuptiality 8.09 -> 11.09 |
| marriages | Campobasso 1880->1881 | yoy_jump | nuptiality 8.0 -> 11.13 |
| marriages | Caserta 1865->1866 | yoy_jump | nuptiality 9.36 -> 6.02 |
| marriages | Catania 1865->1866 | yoy_jump | nuptiality 7.1 -> 3.37 |
| marriages | Catania 1867->1868 | yoy_jump | nuptiality 3.74 -> 5.83 |
| marriages | Catania 1868->1869 | yoy_jump | nuptiality 5.83 -> 8.62 |
| marriages | Catanzaro 1865->1866 | yoy_jump | nuptiality 10.44 -> 6.14 |
| marriages | Catanzaro 1868->1869 | yoy_jump | nuptiality 5.41 -> 8.98 |
| marriages | Catanzaro 1880->1881 | yoy_jump | nuptiality 6.57 -> 8.99 |
| marriages | Como 1865->1866 | yoy_jump | nuptiality 9.1 -> 5.39 |
| marriages | Cosenza 1865->1866 | yoy_jump | nuptiality 10.13 -> 6.33 |
| marriages | Cosenza 1868->1869 | yoy_jump | nuptiality 6.59 -> 9.11 |
| marriages | Cremona 1865->1866 | yoy_jump | nuptiality 10.94 -> 6.46 |
| marriages | Cremona 1866->1867 | yoy_jump | nuptiality 6.46 -> 9.36 |
| marriages | Cuneo 1865->1866 | yoy_jump | nuptiality 10.16 -> 6.45 |
| marriages | Ferrara 1865->1866 | yoy_jump | nuptiality 10.08 -> 1.68 |
| marriages | Ferrara 1866->1867 | yoy_jump | nuptiality 1.68 -> 5.5 |
| marriages | Firenze 1865->1866 | yoy_jump | nuptiality 10.21 -> 5.07 |
| marriages | Forlì 1865->1866 | yoy_jump | nuptiality 7.27 -> 3.13 |
| marriages | Forlì 1878->1879 | yoy_jump | nuptiality 5.22 -> 7.15 |
| marriages | Genova 1865->1866 | yoy_jump | nuptiality 11.46 -> 4.82 |
| marriages | Genova 1866->1867 | yoy_jump | nuptiality 4.82 -> 7.13 |
| marriages | Girgenti 1865->1866 | yoy_jump | nuptiality 5.9 -> 2.53 |
| marriages | Girgenti 1866->1867 | yoy_jump | nuptiality 2.53 -> 3.92 |
| marriages | Girgenti 1867->1868 | yoy_jump | nuptiality 3.92 -> 6.74 |
| marriages | Girgenti 1868->1869 | yoy_jump | nuptiality 6.74 -> 9.45 |
| marriages | Girgenti 1880->1881 | yoy_jump | nuptiality 7.35 -> 9.94 |
| marriages | Grosseto 1865->1866 | yoy_jump | nuptiality 9.25 -> 3.36 |
| marriages | Grosseto 1866->1867 | yoy_jump | nuptiality 3.36 -> 5.5 |
| marriages | Lecce 1874->1875 | yoy_jump | nuptiality 6.37 -> 9.92 |
| marriages | Livorno 1865->1866 | yoy_jump | nuptiality 10.27 -> 6.26 |
| marriages | Lucca 1865->1866 | yoy_jump | nuptiality 9.72 -> 3.77 |
| marriages | Lucca 1866->1867 | yoy_jump | nuptiality 3.77 -> 5.21 |
| marriages | Macerata 1865->1866 | yoy_jump | nuptiality 7.08 -> 4.58 |
| marriages | Mantova 1864->1865 | yoy_jump | nuptiality 4.97 -> 1.2 |
| marriages | Mantova 1865->1866 | yoy_jump | nuptiality 1.2 -> 4.81 |
| marriages | Mantova 1868->1869 | yoy_jump | nuptiality 5.55 -> 8.91 |
| marriages | Mantova 1870->1871 | yoy_jump | nuptiality 8.22 -> 4.75 |
| marriages | Mantova 1871->1872 | yoy_jump | nuptiality 4.75 -> 7.36 |
| marriages | Massa e Carrara 1865->1866 | yoy_jump | nuptiality 9.45 -> 3.85 |
| marriages | Massa e Carrara 1878->1879 | yoy_jump | nuptiality 4.95 -> 6.82 |
| marriages | Messina 1865->1866 | yoy_jump | nuptiality 7.44 -> 4.61 |
| marriages | Messina 1880->1881 | yoy_jump | nuptiality 5.68 -> 8.01 |
| marriages | Milano 1865->1866 | yoy_jump | nuptiality 9.13 -> 5.68 |
| marriages | Modena 1865->1866 | yoy_jump | nuptiality 8.77 -> 4.9 |
| marriages | Napoli 1865->1866 | yoy_jump | nuptiality 8.66 -> 5.38 |
| marriages | Novara 1865->1866 | yoy_jump | nuptiality 11.01 -> 6.83 |
| marriages | Palermo 1865->1866 | yoy_jump | nuptiality 8.54 -> 3.76 |
| marriages | Palermo 1866->1867 | yoy_jump | nuptiality 3.76 -> 5.76 |
| marriages | Pavia 1865->1866 | yoy_jump | nuptiality 10.16 -> 6.25 |
| marriages | Pesaro e Urbino 1865->1866 | yoy_jump | nuptiality 7.25 -> 2.94 |
| marriages | Pisa 1865->1866 | yoy_jump | nuptiality 9.64 -> 4.37 |
| marriages | Porto Maurizio 1865->1866 | yoy_jump | nuptiality 10.93 -> 4.7 |
| marriages | Porto Maurizio 1866->1867 | yoy_jump | nuptiality 4.7 -> 6.4 |
| marriages | Ravenna 1865->1866 | yoy_jump | nuptiality 7.71 -> 3.53 |
| marriages | Reggio di Calabria 1865->1866 | yoy_jump | nuptiality 8.89 -> 5.2 |
| marriages | Reggio di Calabria 1868->1869 | yoy_jump | nuptiality 5.3 -> 8.56 |
| marriages | Reggio di Calabria 1872->1873 | yoy_jump | nuptiality 7.09 -> 9.67 |
| marriages | Reggio di Calabria 1880->1881 | yoy_jump | nuptiality 6.43 -> 8.97 |
| marriages | Reggio nell'Emilia 1865->1866 | yoy_jump | nuptiality 7.96 -> 4.93 |
| marriages | Roma 1880->1881 | yoy_jump | nuptiality 5.73 -> 7.77 |
| marriages | Salerno 1864->1865 | yoy_jump | nuptiality 6.52 -> 9.2 |
| marriages | Sassari 1865->1866 | yoy_jump | nuptiality 11.07 -> 3.63 |
| marriages | Sassari 1866->1867 | yoy_jump | nuptiality 3.63 -> 5.9 |
| marriages | Sassari 1873->1874 | yoy_jump | nuptiality 6.6 -> 9.13 |
| marriages | Siena 1865->1866 | yoy_jump | nuptiality 9.95 -> 5.4 |
| marriages | Siena 1880->1881 | yoy_jump | nuptiality 6.18 -> 8.49 |
| marriages | Siracusa 1865->1866 | yoy_jump | nuptiality 7.6 -> 3.97 |
| marriages | Siracusa 1867->1868 | yoy_jump | nuptiality 3.47 -> 5.6 |
| marriages | Siracusa 1868->1869 | yoy_jump | nuptiality 5.6 -> 9.65 |
| marriages | Sondrio 1865->1866 | yoy_jump | nuptiality 9.25 -> 5.92 |
| marriages | Torino 1865->1866 | yoy_jump | nuptiality 9.6 -> 5.89 |
| marriages | Trapani 1865->1866 | yoy_jump | nuptiality 7.46 -> 3.88 |
| marriages | Trapani 1867->1868 | yoy_jump | nuptiality 4.73 -> 6.81 |
| marriages | Venezia 1866->1867 | yoy_jump | nuptiality 6.38 -> 11.66 |
| migration | Aquila degli Abruzzi 1913 | emig_rate_range | emig_rate=51.34 |
| migration | Aquila degli Abruzzi 1920 | emig_rate_range | emig_rate=40.09 |
| migration | Caltanissetta 1913 | emig_rate_range | emig_rate=44.35 |
| migration | Campobasso 1913 | emig_rate_range | emig_rate=40.26 |
| migration | Catanzaro 1913 | emig_rate_range | emig_rate=41.34 |
| migration | Cosenza 1920 | emig_rate_range | emig_rate=44.98 |
| migration | Girgenti 1913 | emig_rate_range | emig_rate=50.7 |
| migration | Siracusa 1913 | emig_rate_range | emig_rate=43.27 |
| migration | Sondrio 1911 | emig_rate_range | emig_rate=46.29 |
| migration | Sondrio 1912 | emig_rate_range | emig_rate=47.94 |
| migration | Sondrio 1913 | emig_rate_range | emig_rate=51.25 |
| migration | Teramo 1913 | emig_rate_range | emig_rate=45.72 |
| migration | Trapani 1913 | emig_rate_range | emig_rate=70.8 |
| migration | Udine 1911 | emig_rate_range | emig_rate=58.17 |
| migration | Udine 1912 | emig_rate_range | emig_rate=66.08 |
| migration | Udine 1913 | emig_rate_range | emig_rate=68.26 |
| migration | Udine 1914 | emig_rate_range | emig_rate=79.63 |
| migration | Alessandria 1911->1912 | yoy_jump | emig_rate 9.05 -> 14.36 |
| migration | Alessandria 1920->1921 | yoy_jump | emig_rate 10.05 -> 4.78 |
| migration | Ancona 1911->1912 | yoy_jump | emig_rate 14.35 -> 22.55 |
| migration | Ancona 1920->1921 | yoy_jump | emig_rate 14.34 -> 4.58 |
| migration | Aquila degli Abruzzi 1911->1912 | yoy_jump | emig_rate 23.59 -> 35.8 |
| migration | Aquila degli Abruzzi 1912->1913 | yoy_jump | emig_rate 35.8 -> 51.34 |
| migration | Aquila degli Abruzzi 1920->1921 | yoy_jump | emig_rate 40.09 -> 4.65 |
| migration | Arezzo 1920->1921 | yoy_jump | emig_rate 5.28 -> 1.27 |
| migration | Ascoli Piceno 1911->1912 | yoy_jump | emig_rate 12.81 -> 28.31 |
| migration | Ascoli Piceno 1920->1921 | yoy_jump | emig_rate 20.43 -> 4.77 |
| migration | Avellino 1920->1921 | yoy_jump | emig_rate 35.24 -> 7.33 |
| migration | Bari delle Puglie 1912->1913 | yoy_jump | emig_rate 18.41 -> 29.05 |
| migration | Bari delle Puglie 1920->1921 | yoy_jump | emig_rate 30.78 -> 4.76 |
| migration | Belluno 1920->1921 | yoy_jump | emig_rate 31.81 -> 9.56 |
| migration | Benevento 1920->1921 | yoy_jump | emig_rate 29.19 -> 6.39 |
| migration | Bergamo 1920->1921 | yoy_jump | emig_rate 24.17 -> 9.53 |
| migration | Bologna 1920->1921 | yoy_jump | emig_rate 2.76 -> 0.91 |
| migration | Brescia 1920->1921 | yoy_jump | emig_rate 5.7 -> 1.62 |
| migration | Cagliari 1911->1912 | yoy_jump | emig_rate 5.2 -> 7.39 |
| migration | Cagliari 1912->1913 | yoy_jump | emig_rate 7.39 -> 10.38 |
| migration | Cagliari 1920->1921 | yoy_jump | emig_rate 6.3 -> 1.28 |
| migration | Caltanissetta 1911->1912 | yoy_jump | emig_rate 14.61 -> 30.99 |
| migration | Caltanissetta 1912->1913 | yoy_jump | emig_rate 30.99 -> 44.35 |
| migration | Caltanissetta 1920->1921 | yoy_jump | emig_rate 26.43 -> 3.08 |
| migration | Campobasso 1920->1921 | yoy_jump | emig_rate 33.73 -> 8.39 |
| migration | Caserta 1911->1912 | yoy_jump | emig_rate 20.57 -> 30.87 |
| migration | Caserta 1920->1921 | yoy_jump | emig_rate 36.18 -> 6.34 |
| migration | Catania 1911->1912 | yoy_jump | emig_rate 10.59 -> 19.9 |
| migration | Catania 1920->1921 | yoy_jump | emig_rate 17.07 -> 4.78 |
| migration | Catanzaro 1911->1912 | yoy_jump | emig_rate 19.99 -> 32.84 |
| migration | Catanzaro 1920->1921 | yoy_jump | emig_rate 31.51 -> 11.21 |
| migration | Chieti 1911->1912 | yoy_jump | emig_rate 19.95 -> 29.6 |
| migration | Chieti 1920->1921 | yoy_jump | emig_rate 33.65 -> 10.49 |
| migration | Como 1920->1921 | yoy_jump | emig_rate 24.03 -> 11.94 |
| migration | Cosenza 1920->1921 | yoy_jump | emig_rate 44.98 -> 16.57 |
| migration | Cremona 1920->1921 | yoy_jump | emig_rate 2.81 -> 0.7 |
| migration | Cuneo 1912->1913 | yoy_jump | emig_rate 13.64 -> 20.09 |
| migration | Cuneo 1920->1921 | yoy_jump | emig_rate 24.83 -> 11.03 |
| migration | Ferrara 1920->1921 | yoy_jump | emig_rate 1.53 -> 0.91 |
| migration | Firenze 1920->1921 | yoy_jump | emig_rate 5.29 -> 3.26 |
| migration | Foggia 1911->1912 | yoy_jump | emig_rate 11.07 -> 20.34 |
| migration | Foggia 1920->1921 | yoy_jump | emig_rate 20.39 -> 2.39 |
| migration | Forlì 1920->1921 | yoy_jump | emig_rate 8.06 -> 1.21 |
| migration | Genova 1920->1921 | yoy_jump | emig_rate 8.21 -> 3.2 |
| migration | Girgenti 1911->1912 | yoy_jump | emig_rate 18.69 -> 34.07 |
| migration | Girgenti 1912->1913 | yoy_jump | emig_rate 34.07 -> 50.7 |
| migration | Girgenti 1920->1921 | yoy_jump | emig_rate 37.46 -> 7.69 |
| migration | Grosseto 1911->1912 | yoy_jump | emig_rate 5.02 -> 8.01 |
| migration | Grosseto 1912->1913 | yoy_jump | emig_rate 8.01 -> 11.9 |
| migration | Grosseto 1920->1921 | yoy_jump | emig_rate 2.85 -> 0.33 |
| migration | Lecce 1912->1913 | yoy_jump | emig_rate 4.14 -> 6.0 |
| migration | Lecce 1920->1921 | yoy_jump | emig_rate 2.45 -> 0.64 |
| migration | Livorno 1920->1921 | yoy_jump | emig_rate 5.69 -> 2.12 |
| migration | Lucca 1920->1921 | yoy_jump | emig_rate 27.88 -> 10.89 |
| migration | Macerata 1911->1912 | yoy_jump | emig_rate 11.79 -> 33.24 |
| migration | Mantova 1912->1913 | yoy_jump | emig_rate 10.15 -> 14.33 |
| migration | Mantova 1920->1921 | yoy_jump | emig_rate 2.7 -> 1.02 |
| migration | Massa e Carrara 1920->1921 | yoy_jump | emig_rate 24.06 -> 6.42 |
| migration | Messina 1911->1912 | yoy_jump | emig_rate 16.94 -> 27.5 |
| migration | Messina 1912->1913 | yoy_jump | emig_rate 27.5 -> 39.45 |
| migration | Messina 1920->1921 | yoy_jump | emig_rate 27.4 -> 7.09 |
| migration | Milano 1911->1912 | yoy_jump | emig_rate 4.96 -> 7.35 |
| migration | Milano 1920->1921 | yoy_jump | emig_rate 3.78 -> 1.66 |
| migration | Modena 1920->1921 | yoy_jump | emig_rate 7.0 -> 3.27 |
| migration | Napoli 1920->1921 | yoy_jump | emig_rate 13.09 -> 1.97 |
| migration | Novara 1920->1921 | yoy_jump | emig_rate 26.39 -> 13.09 |
| migration | Padova 1920->1921 | yoy_jump | emig_rate 7.86 -> 1.72 |
| migration | Palermo 1911->1912 | yoy_jump | emig_rate 13.33 -> 18.65 |
| migration | Palermo 1912->1913 | yoy_jump | emig_rate 18.65 -> 29.18 |
| migration | Palermo 1920->1921 | yoy_jump | emig_rate 30.27 -> 6.03 |
| migration | Parma 1920->1921 | yoy_jump | emig_rate 12.9 -> 4.57 |
| migration | Pavia 1911->1912 | yoy_jump | emig_rate 6.7 -> 14.06 |
| migration | Pavia 1920->1921 | yoy_jump | emig_rate 6.69 -> 3.95 |
| migration | Pesaro e Urbino 1911->1912 | yoy_jump | emig_rate 24.35 -> 35.68 |
| migration | Pesaro e Urbino 1920->1921 | yoy_jump | emig_rate 20.65 -> 3.41 |
| migration | Piacenza 1920->1921 | yoy_jump | emig_rate 12.76 -> 3.42 |
| migration | Pisa 1911->1912 | yoy_jump | emig_rate 7.53 -> 10.72 |
| migration | Pisa 1912->1913 | yoy_jump | emig_rate 10.72 -> 14.75 |
| migration | Pisa 1920->1921 | yoy_jump | emig_rate 7.51 -> 2.07 |
| migration | Porto Maurizio 1920->1921 | yoy_jump | emig_rate 23.37 -> 2.73 |
| migration | Potenza 1911->1912 | yoy_jump | emig_rate 22.2 -> 31.67 |
| migration | Potenza 1920->1921 | yoy_jump | emig_rate 26.37 -> 11.98 |
| migration | Ravenna 1920->1921 | yoy_jump | emig_rate 1.57 -> 0.31 |
| migration | Reggio di Calabria 1911->1912 | yoy_jump | emig_rate 15.66 -> 32.11 |
| migration | Reggio di Calabria 1920->1921 | yoy_jump | emig_rate 28.86 -> 6.66 |
| migration | Reggio nell'Emilia 1912->1913 | yoy_jump | emig_rate 9.5 -> 13.93 |
| migration | Reggio nell'Emilia 1920->1921 | yoy_jump | emig_rate 5.06 -> 1.17 |
| migration | Roma 1911->1912 | yoy_jump | emig_rate 6.96 -> 13.45 |
| migration | Roma 1912->1913 | yoy_jump | emig_rate 13.45 -> 19.27 |
| migration | Roma 1920->1921 | yoy_jump | emig_rate 7.5 -> 1.42 |
| migration | Rovigo 1911->1912 | yoy_jump | emig_rate 7.05 -> 11.58 |
| migration | Rovigo 1920->1921 | yoy_jump | emig_rate 2.5 -> 0.72 |
| migration | Salerno 1920->1921 | yoy_jump | emig_rate 21.91 -> 7.85 |
| migration | Sassari 1911->1912 | yoy_jump | emig_rate 8.02 -> 15.96 |
| migration | Sassari 1920->1921 | yoy_jump | emig_rate 10.02 -> 1.3 |
| migration | Siena 1920->1921 | yoy_jump | emig_rate 1.25 -> 0.45 |
| migration | Siracusa 1911->1912 | yoy_jump | emig_rate 13.68 -> 32.27 |
| migration | Siracusa 1920->1921 | yoy_jump | emig_rate 29.32 -> 4.51 |
| migration | Teramo 1911->1912 | yoy_jump | emig_rate 20.78 -> 33.02 |
| migration | Teramo 1912->1913 | yoy_jump | emig_rate 33.02 -> 45.72 |
| migration | Teramo 1920->1921 | yoy_jump | emig_rate 31.36 -> 5.95 |
| migration | Torino 1920->1921 | yoy_jump | emig_rate 14.46 -> 8.27 |
| migration | Trapani 1911->1912 | yoy_jump | emig_rate 13.13 -> 24.14 |
| migration | Trapani 1912->1913 | yoy_jump | emig_rate 24.14 -> 70.8 |
| migration | Trapani 1920->1921 | yoy_jump | emig_rate 30.55 -> 7.37 |
| migration | Treviso 1920->1921 | yoy_jump | emig_rate 11.74 -> 7.54 |
| migration | Udine 1920->1921 | yoy_jump | emig_rate 37.52 -> 21.81 |
| migration | Umbria 1920->1921 | yoy_jump | emig_rate 7.46 -> 1.97 |
| migration | Venezia 1920->1921 | yoy_jump | emig_rate 2.45 -> 0.65 |
| migration | Verona 1920->1921 | yoy_jump | emig_rate 9.12 -> 1.4 |
| migration | Vicenza 1911->1912 | yoy_jump | emig_rate 22.31 -> 34.68 |
| migration | Vicenza 1920->1921 | yoy_jump | emig_rate 16.79 -> 3.24 |
| mortality | Alessandria 1921 | cdr_range | cdr=14.41 |
| mortality | Alessandria 1931 | cdr_range | cdr=14.66 |
| mortality | Alessandria 1936 | cdr_range | cdr=13.1 |
| mortality | Ancona 1931 | cdr_range | cdr=11.63 |
| mortality | Ancona 1936 | cdr_range | cdr=12.1 |
| mortality | Arezzo 1936 | cdr_range | cdr=12.6 |
| mortality | Ascoli Piceno 1936 | cdr_range | cdr=13.0 |
| mortality | Bologna 1921 | cdr_range | cdr=14.9 |
| mortality | Bologna 1936 | cdr_range | cdr=12.5 |
| mortality | Cagliari 1881 | cdr_range | cdr=14.66 |
| mortality | Cagliari 1931 | cdr_range | cdr=14.17 |
| mortality | Cagliari 1936 | cdr_range | cdr=14.5 |
| mortality | Catania 1931 | cdr_range | cdr=13.51 |
| mortality | Catania 1936 | cdr_range | cdr=14.6 |
| mortality | Chieti 1931 | cdr_range | cdr=14.0 |
| mortality | Como 1936 | cdr_range | cdr=13.8 |
| mortality | Cosenza 1936 | cdr_range | cdr=13.5 |
| mortality | Cremona 1936 | cdr_range | cdr=14.3 |
| mortality | Cuneo 1936 | cdr_range | cdr=14.4 |
| mortality | Ferrara 1936 | cdr_range | cdr=12.4 |
| mortality | Firenze 1921 | cdr_range | cdr=14.87 |
| mortality | Firenze 1936 | cdr_range | cdr=11.9 |
| mortality | Forlì 1936 | cdr_range | cdr=12.1 |
| mortality | Genova 1921 | cdr_range | cdr=14.28 |
| mortality | Genova 1931 | cdr_range | cdr=13.82 |
| mortality | Genova 1936 | cdr_range | cdr=12.3 |
| mortality | Grosseto 1936 | cdr_range | cdr=10.7 |
| mortality | Livorno 1936 | cdr_range | cdr=11.9 |
| mortality | Lucca 1921 | cdr_range | cdr=14.47 |
| mortality | Lucca 1936 | cdr_range | cdr=12.3 |
| mortality | Macerata 1931 | cdr_range | cdr=11.88 |
| mortality | Macerata 1936 | cdr_range | cdr=13.1 |
| mortality | Mantova 1936 | cdr_range | cdr=12.3 |
| mortality | Messina 1931 | cdr_range | cdr=12.29 |
| mortality | Messina 1936 | cdr_range | cdr=13.6 |
| mortality | Milano 1936 | cdr_range | cdr=12.6 |
| mortality | Modena 1936 | cdr_range | cdr=12.4 |
| mortality | Napoli 1931 | cdr_range | cdr=14.67 |
| mortality | Novara 1921 | cdr_range | cdr=14.88 |
| mortality | Novara 1936 | cdr_range | cdr=13.9 |
| mortality | Padova 1936 | cdr_range | cdr=11.1 |
| mortality | Palermo 1931 | cdr_range | cdr=13.47 |
| mortality | Palermo 1936 | cdr_range | cdr=14.6 |
| mortality | Parma 1936 | cdr_range | cdr=12.9 |
| mortality | Pavia 1921 | cdr_range | cdr=13.86 |
| mortality | Pavia 1936 | cdr_range | cdr=12.8 |
| mortality | Pesaro e Urbino 1936 | cdr_range | cdr=13.4 |
| mortality | Piacenza 1936 | cdr_range | cdr=12.7 |
| mortality | Pisa 1871 | cdr_range | cdr=13.14 |
| mortality | Pisa 1881 | cdr_range | cdr=12.04 |
| mortality | Pisa 1921 | cdr_range | cdr=14.36 |
| mortality | Pisa 1936 | cdr_range | cdr=12.1 |
| mortality | Ravenna 1881 | cdr_range | cdr=11.92 |
| mortality | Ravenna 1936 | cdr_range | cdr=12.1 |
| mortality | Roma 1931 | cdr_range | cdr=11.52 |
| mortality | Roma 1936 | cdr_range | cdr=11.6 |
| mortality | Rovigo 1936 | cdr_range | cdr=11.5 |
| mortality | Salerno 1936 | cdr_range | cdr=14.5 |
| mortality | Sassari 1931 | cdr_range | cdr=13.25 |
| mortality | Sassari 1936 | cdr_range | cdr=14.0 |
| mortality | Siena 1936 | cdr_range | cdr=12.7 |
| mortality | Siracusa 1931 | cdr_range | cdr=12.3 |
| mortality | Siracusa 1936 | cdr_range | cdr=13.9 |
| mortality | Sondrio 1936 | cdr_range | cdr=14.9 |
| mortality | Teramo 1931 | cdr_range | cdr=14.9 |
| mortality | Teramo 1936 | cdr_range | cdr=14.4 |
| mortality | Torino 1931 | cdr_range | cdr=14.43 |
| mortality | Torino 1936 | cdr_range | cdr=13.3 |
| mortality | Trapani 1931 | cdr_range | cdr=11.29 |
| mortality | Trapani 1936 | cdr_range | cdr=13.3 |
| mortality | Treviso 1871 | cdr_range | cdr=14.26 |
| mortality | Treviso 1881 | cdr_range | cdr=12.33 |
| mortality | Treviso 1921 | cdr_range | cdr=13.7 |
| mortality | Treviso 1936 | cdr_range | cdr=11.1 |
| mortality | Udine 1871 | cdr_range | cdr=13.47 |
| mortality | Udine 1881 | cdr_range | cdr=12.17 |
| mortality | Udine 1936 | cdr_range | cdr=12.9 |
| mortality | Umbria 1936 | cdr_range | cdr=13.0 |
| mortality | Venezia 1881 | cdr_range | cdr=12.73 |
| mortality | Venezia 1936 | cdr_range | cdr=14.5 |
| mortality | Verona 1871 | cdr_range | cdr=14.74 |
| mortality | Verona 1936 | cdr_range | cdr=12.2 |
| mortality | Vicenza 1871 | cdr_range | cdr=14.95 |
| mortality | Vicenza 1881 | cdr_range | cdr=13.42 |
| mortality | Vicenza 1936 | cdr_range | cdr=12.4 |
| mortality | Alessandria 1936 | imr_range | imr=58.0 |
| mortality | Firenze 1936 | imr_range | imr=55.0 |
| mortality | Genova 1936 | imr_range | imr=59.0 |
| mortality | Livorno 1936 | imr_range | imr=48.0 |
| mortality | Lucca 1936 | imr_range | imr=56.0 |
| mortality | Pisa 1931 | imr_range | imr=58.0 |
| mortality | Pisa 1936 | imr_range | imr=54.0 |
| mortality | Ravenna 1936 | imr_range | imr=56.0 |
| mortality | Sondrio 1881 | imr_range | imr=370.0 |

## INFO (314)

| dataset | where | check | detail |
|---|---|---|---|
| census | Aquila 1881 | t_0!=m+f | 10,107 != 5,180+4,972 (off 45) |
| census | Cuneo 1931 | t_0!=m+f | 12,733 != 6,436+6,267 (off 30) |
| census | Como 1881 | t_10_14!=m+f | 49,812 != 24,821+24,961 (off 30) |
| census | Foggia 1936 | t_10_14!=m+f | 59,166 != 29,827+29,348 (off 9) |
| census | Reggionell'Emilia 1936 | t_10_14!=m+f | 41,453 != 20,616+20,842 (off 5) |
| census | Siena 1911 | t_10_14!=m+f | 23,520 != 11,999+11,516 (off 5) |
| census | Catanzaro 1936 | t_15_19!=m+f | 48,611 != 24,870+23,738 (off 3) |
| census | Trapani 1921 | t_15_19!=m+f | 39,677 != 19,856+19,823 (off 2) |
| census | Cuneo 1931 | t_1_4!=m+f | 47,452 != 23,881+23,601 (off 30) |
| census | Sassari 1921 | t_20_24!=m+f | 27,315 != 12,877+14,538 (off 100) |
| census | Ravenna 1931 | t_30_34!=m+f | 18,595 != 9,387+9,207 (off 1) |
| census | Grosseto 1881 | t_35_39!=m+f | 7,641 != 4,615+2,996 (off 30) |
| census | Piacenza 1921 | t_35_39!=m+f | 15,900 != 7,586+8,304 (off 10) |
| census | Ravenna 1931 | t_35_39!=m+f | 17,112 != 8,571+8,540 (off 1) |
| census | ReggiodiCalabria 1936 | t_40_44!=m+f | 26,558 != 10,396+16,164 (off 2) |
| census | Chieti 1936 | t_45_49!=m+f | 16,665 != 6,643+10,016 (off 6) |
| census | Foggia 1936 | t_45_49!=m+f | 23,685 != 10,466+13,210 (off 9) |
| census | Salerno 1881 | t_45_49!=m+f | 24,360 != 11,259+13,111 (off 10) |
| census | Asti 1936 | t_50_54!=m+f | 14,209 != 6,903+7,305 (off 1) |
| census | Ravenna 1931 | t_50_54!=m+f | 13,475 != 6,802+6,672 (off 1) |
| census | Sassari 1921 | t_50_54!=m+f | 15,182 != 7,785+7,373 (off 24) |
| census | Ancona 1936 | t_55_59!=m+f | 14,313 != 6,754+7,564 (off 5) |
| census | Grosseto 1936 | t_55_59!=m+f | 7,205 != 3,871+3,333 (off 1) |
| census | Firenze 1921 | t_5_9!=m+f | 98,983 != 49,760+49,423 (off 200) |
| census | Latina 1936 | t_60_64!=m+f | 5,874 != 2,843+3,022 (off 9) |
| census | Parma 1921 | t_65_69!=m+f | 7,164 != 3,639+3,515 (off 10) |
| census | Bergamo 1881 | t_70_74!=m+f | 5,137 != 2,838+2,279 (off 20) |
| census | Macerata 1881 | t_70_74!=m+f | 5,775 != 2,846+2,925 (off 4) |
| census | Napoli 1911 | t_70_74!=m+f | 25,639 != 12,051+13,581 (off 7) |
| census | Benevento 1936 | t_75_79!=m+f | 5,288 != 2,475+2,808 (off 5) |
| census | Forlì 1881 | t_75_79!=m+f | 1,863 != 1,065+800 (off 2) |
| census | Cuneo 1931 | t_80_84!=m+f | 3,853 != 1,928+1,924 (off 1) |
| census | Ravenna 1881 | t_80_84!=m+f | 773 != 384+385 (off 4) |
| census | Ancona 1881 | t_85plus!=m+f | 453 != 203+252 (off 2) |
| census | Benevento 1936 | t_85plus!=m+f | 1,071 != 499+571 (off 1) |
| census | Bergamo 1881 | t_85plus!=m+f | 171 != 110+63 (off 2) |
| census | Chieti 1936 | t_85plus!=m+f | 1,364 != 633+725 (off 6) |
| census | Cremona 1936 | t_85plus!=m+f | 597 != 249+352 (off 4) |
| census | Cuneo 1931 | t_85plus!=m+f | 1,284 != 633+650 (off 1) |
| census | Ferrara 1936 | t_85plus!=m+f | 121 != 43+81 (off 3) |
| census | Grosseto 1931 | t_85plus!=m+f | 248 != 97+153 (off 2) |
| census | Matera 1936 | t_85plus!=m+f | 330 != 139+194 (off 3) |
| census | Potenza 1936 | t_85plus!=m+f | 1,044 != 460+589 (off 5) |
| census | Reggio nell'Emilia 1921 | t_85plus!=m+f | 648 != 255+395 (off 2) |
| census | Ancona 1881 | total!=M+F | 267,335 != 130,939+136,398 (off 2) |
| census | Ancona 1936 | total!=M+F | 372,226 != 180,621+191,610 (off 5) |
| census | Aquila 1881 | total!=M+F | 352,993 != 164,251+188,787 (off 45) |
| census | Asti 1936 | total!=M+F | 241,704 != 121,914+119,789 (off 1) |
| census | Benevento 1936 | total!=M+F | 349,695 != 169,769+179,920 (off 6) |
| census | Bergamo 1881 | total!=M+F | 390,768 != 196,889+193,861 (off 18) |
| census | Catanzaro 1936 | total!=M+F | 606,286 != 289,935+316,348 (off 3) |
| census | Chieti 1936 | total!=M+F | 374,719 != 178,414+196,293 (off 12) |
| census | Como 1881 | total!=M+F | 515,046 != 256,444+258,572 (off 30) |
| census | Cremona 1936 | total!=M+F | 369,466 != 182,999+186,471 (off 4) |
| census | Cuneo 1931 | total!=M+F | 619,708 != 314,804+304,902 (off 2) |
| census | Ferrara 1936 | total!=M+F | 381,293 != 190,014+191,282 (off 3) |
| census | Firenze 1921 | total!=M+F | 1,035,968 != 511,493+524,675 (off 200) |
| census | Forlì 1881 | total!=M+F | 251,081 != 128,609+122,474 (off 2) |
| census | Grosseto 1881 | total!=M+F | 114,289 != 64,367+49,892 (off 30) |
| census | Grosseto 1931 | total!=M+F | 176,975 != 91,567+85,410 (off 2) |
| census | Grosseto 1936 | total!=M+F | 185,799 != 96,145+89,653 (off 1) |
| census | Latina 1936 | total!=M+F | 227,158 != 114,802+112,347 (off 9) |
| census | Macerata 1881 | total!=M+F | 239,652 != 116,572+123,076 (off 4) |
| census | Matera 1936 | total!=M+F | 166,770 != 82,697+84,076 (off 3) |
| census | Napoli 1911 | total!=M+F | 1,302,007 != 641,314+660,686 (off 7) |
| census | Parma 1921 | total!=M+F | 343,394 != 172,295+171,089 (off 10) |
| census | Potenza 1936 | total!=M+F | 376,482 != 184,150+192,337 (off 5) |
| census | Ravenna 1881 | total!=M+F | 225,757 != 115,138+110,615 (off 4) |
| census | Ravenna 1931 | total!=M+F | 271,666 != 136,151+135,512 (off 3) |
| census | Reggio nell'Emilia 1921 | total!=M+F | 344,532 != 172,508+172,026 (off 2) |
| census | ReggiodiCalabria 1936 | total!=M+F | 578,127 != 278,686+299,443 (off 2) |
| census | Reggionell'Emilia 1936 | total!=M+F | 375,261 != 187,469+187,797 (off 5) |
| census | Rovigo 1921 | total!=M+F | 286,688 != 141,941+144,567 (off 180) |
| census | Salerno 1881 | total!=M+F | 550,157 != 266,129+284,038 (off 10) |
| census | Sassari 1921 | total!=M+F | 330,548 != 165,097+165,527 (off 76) |
| census | Siena 1911 | total!=M+F | 241,535 != 124,795+116,735 (off 5) |
| census | Siracusa 1921 | total!=M+F | 526,953 != 267,126+259,927 (off 100) |
| census | Trapani 1921 | total!=M+F | 405,743 != 200,457+205,288 (off 2) |
| census | Venezia 1921 | total!=M+F | 517,970 != 257,222+261,108 (off 360) |
| census | Vicenza 1921 | total!=M+F | 545,991 != 269,010+277,481 (off 500) |
| cross | Cuneo 1931 | cdr>cbr | deaths exceed births: CDR 20.85 > CBR 20.73 |
| cross | Padova 1931 | cdr>cbr | deaths exceed births: CDR 26.8 > CBR 20.85 |
| cross | Ravenna 1931 | cdr>cbr | deaths exceed births: CDR 16.46 > CBR 15.84 |
| migration | Alessandria 1913->1914 | yoy_jump | emig_rate 17.21 -> 7.73 (WWI disruption) |
| migration | Alessandria 1914->1915 | yoy_jump | emig_rate 7.73 -> 3.91 (WWI disruption) |
| migration | Alessandria 1919->1920 | yoy_jump | emig_rate 5.87 -> 10.05 (WWI disruption) |
| migration | Ancona 1913->1914 | yoy_jump | emig_rate 22.82 -> 9.71 (WWI disruption) |
| migration | Ancona 1914->1915 | yoy_jump | emig_rate 9.71 -> 2.59 (WWI disruption) |
| migration | Ancona 1919->1920 | yoy_jump | emig_rate 5.62 -> 14.34 (WWI disruption) |
| migration | Aquila degli Abruzzi 1913->1914 | yoy_jump | emig_rate 51.34 -> 21.98 (WWI disruption) |
| migration | Aquila degli Abruzzi 1914->1915 | yoy_jump | emig_rate 21.98 -> 6.95 (WWI disruption) |
| migration | Aquila degli Abruzzi 1915->1916 | yoy_jump | emig_rate 6.95 -> 10.0 (WWI disruption) |
| migration | Aquila degli Abruzzi 1919->1920 | yoy_jump | emig_rate 10.05 -> 40.09 (WWI disruption) |
| migration | Arezzo 1913->1914 | yoy_jump | emig_rate 22.26 -> 14.43 (WWI disruption) |
| migration | Arezzo 1914->1915 | yoy_jump | emig_rate 14.43 -> 1.79 (WWI disruption) |
| migration | Ascoli Piceno 1913->1914 | yoy_jump | emig_rate 32.08 -> 11.13 (WWI disruption) |
| migration | Ascoli Piceno 1914->1915 | yoy_jump | emig_rate 11.13 -> 3.36 (WWI disruption) |
| migration | Ascoli Piceno 1919->1920 | yoy_jump | emig_rate 4.16 -> 20.43 (WWI disruption) |
| migration | Avellino 1913->1914 | yoy_jump | emig_rate 34.44 -> 18.17 (WWI disruption) |
| migration | Avellino 1914->1915 | yoy_jump | emig_rate 18.17 -> 6.12 (WWI disruption) |
| migration | Avellino 1915->1916 | yoy_jump | emig_rate 6.12 -> 8.62 (WWI disruption) |
| migration | Avellino 1919->1920 | yoy_jump | emig_rate 7.84 -> 35.24 (WWI disruption) |
| migration | Bari delle Puglie 1913->1914 | yoy_jump | emig_rate 29.05 -> 11.72 (WWI disruption) |
| migration | Bari delle Puglie 1914->1915 | yoy_jump | emig_rate 11.72 -> 4.18 (WWI disruption) |
| migration | Bari delle Puglie 1915->1916 | yoy_jump | emig_rate 4.18 -> 7.82 (WWI disruption) |
| migration | Bari delle Puglie 1919->1920 | yoy_jump | emig_rate 6.78 -> 30.78 (WWI disruption) |
| migration | Belluno 1914->1915 | yoy_jump | emig_rate 82.21 -> 15.12 (WWI disruption) |
| migration | Belluno 1915->1916 | yoy_jump | emig_rate 15.12 -> 2.08 (WWI disruption) |
| migration | Belluno 1919->1920 | yoy_jump | emig_rate 10.37 -> 31.81 (WWI disruption) |
| migration | Benevento 1913->1914 | yoy_jump | emig_rate 36.52 -> 19.09 (WWI disruption) |
| migration | Benevento 1914->1915 | yoy_jump | emig_rate 19.09 -> 5.72 (WWI disruption) |
| migration | Benevento 1919->1920 | yoy_jump | emig_rate 6.45 -> 29.19 (WWI disruption) |
| migration | Bergamo 1914->1915 | yoy_jump | emig_rate 25.54 -> 8.58 (WWI disruption) |
| migration | Bergamo 1919->1920 | yoy_jump | emig_rate 9.34 -> 24.17 (WWI disruption) |
| migration | Bologna 1913->1914 | yoy_jump | emig_rate 9.99 -> 6.07 (WWI disruption) |
| migration | Bologna 1914->1915 | yoy_jump | emig_rate 6.07 -> 1.5 (WWI disruption) |
| migration | Bologna 1919->1920 | yoy_jump | emig_rate 1.71 -> 2.76 (WWI disruption) |
| migration | Brescia 1914->1915 | yoy_jump | emig_rate 15.15 -> 3.26 (WWI disruption) |
| migration | Brescia 1915->1916 | yoy_jump | emig_rate 3.26 -> 0.93 (WWI disruption) |
| migration | Brescia 1919->1920 | yoy_jump | emig_rate 2.11 -> 5.7 (WWI disruption) |
| migration | Cagliari 1913->1914 | yoy_jump | emig_rate 10.38 -> 4.91 (WWI disruption) |
| migration | Cagliari 1914->1915 | yoy_jump | emig_rate 4.91 -> 0.88 (WWI disruption) |
| migration | Cagliari 1919->1920 | yoy_jump | emig_rate 2.7 -> 6.3 (WWI disruption) |
| migration | Caltanissetta 1913->1914 | yoy_jump | emig_rate 44.35 -> 11.87 (WWI disruption) |
| migration | Caltanissetta 1914->1915 | yoy_jump | emig_rate 11.87 -> 3.16 (WWI disruption) |
| migration | Caltanissetta 1915->1916 | yoy_jump | emig_rate 3.16 -> 4.3 (WWI disruption) |
| migration | Caltanissetta 1919->1920 | yoy_jump | emig_rate 6.06 -> 26.43 (WWI disruption) |
| migration | Campobasso 1913->1914 | yoy_jump | emig_rate 40.26 -> 15.58 (WWI disruption) |
| migration | Campobasso 1914->1915 | yoy_jump | emig_rate 15.58 -> 7.25 (WWI disruption) |
| migration | Campobasso 1915->1916 | yoy_jump | emig_rate 7.25 -> 14.86 (WWI disruption) |
| migration | Campobasso 1919->1920 | yoy_jump | emig_rate 6.96 -> 33.73 (WWI disruption) |
| migration | Caserta 1913->1914 | yoy_jump | emig_rate 38.47 -> 19.01 (WWI disruption) |
| migration | Caserta 1914->1915 | yoy_jump | emig_rate 19.01 -> 6.38 (WWI disruption) |
| migration | Caserta 1919->1920 | yoy_jump | emig_rate 11.46 -> 36.18 (WWI disruption) |
| migration | Catania 1913->1914 | yoy_jump | emig_rate 25.17 -> 7.24 (WWI disruption) |
| migration | Catania 1914->1915 | yoy_jump | emig_rate 7.24 -> 2.19 (WWI disruption) |
| migration | Catania 1919->1920 | yoy_jump | emig_rate 5.42 -> 17.07 (WWI disruption) |
| migration | Catanzaro 1913->1914 | yoy_jump | emig_rate 41.34 -> 17.33 (WWI disruption) |
| migration | Catanzaro 1914->1915 | yoy_jump | emig_rate 17.33 -> 4.43 (WWI disruption) |
| migration | Catanzaro 1919->1920 | yoy_jump | emig_rate 6.37 -> 31.51 (WWI disruption) |
| migration | Chieti 1913->1914 | yoy_jump | emig_rate 36.2 -> 14.92 (WWI disruption) |
| migration | Chieti 1914->1915 | yoy_jump | emig_rate 14.92 -> 5.85 (WWI disruption) |
| migration | Chieti 1919->1920 | yoy_jump | emig_rate 7.04 -> 33.65 (WWI disruption) |
| migration | Como 1914->1915 | yoy_jump | emig_rate 25.34 -> 11.52 (WWI disruption) |
| migration | Como 1919->1920 | yoy_jump | emig_rate 16.36 -> 24.03 (WWI disruption) |
| migration | Cosenza 1913->1914 | yoy_jump | emig_rate 39.44 -> 18.28 (WWI disruption) |
| migration | Cosenza 1914->1915 | yoy_jump | emig_rate 18.28 -> 5.69 (WWI disruption) |
| migration | Cosenza 1919->1920 | yoy_jump | emig_rate 12.52 -> 44.98 (WWI disruption) |
| migration | Cremona 1913->1914 | yoy_jump | emig_rate 9.96 -> 5.55 (WWI disruption) |
| migration | Cremona 1914->1915 | yoy_jump | emig_rate 5.55 -> 1.31 (WWI disruption) |
| migration | Cremona 1915->1916 | yoy_jump | emig_rate 1.31 -> 0.76 (WWI disruption) |
| migration | Cuneo 1913->1914 | yoy_jump | emig_rate 20.09 -> 11.36 (WWI disruption) |
| migration | Cuneo 1915->1916 | yoy_jump | emig_rate 8.06 -> 12.44 (WWI disruption) |
| migration | Ferrara 1913->1914 | yoy_jump | emig_rate 5.69 -> 3.33 (WWI disruption) |
| migration | Ferrara 1914->1915 | yoy_jump | emig_rate 3.33 -> 1.12 (WWI disruption) |
| migration | Ferrara 1915->1916 | yoy_jump | emig_rate 1.12 -> 0.49 (WWI disruption) |
| migration | Firenze 1913->1914 | yoy_jump | emig_rate 14.62 -> 8.83 (WWI disruption) |
| migration | Firenze 1914->1915 | yoy_jump | emig_rate 8.83 -> 2.58 (WWI disruption) |
| migration | Foggia 1913->1914 | yoy_jump | emig_rate 23.46 -> 7.16 (WWI disruption) |
| migration | Foggia 1914->1915 | yoy_jump | emig_rate 7.16 -> 2.55 (WWI disruption) |
| migration | Foggia 1915->1916 | yoy_jump | emig_rate 2.55 -> 7.39 (WWI disruption) |
| migration | Foggia 1919->1920 | yoy_jump | emig_rate 3.24 -> 20.39 (WWI disruption) |
| migration | Forlì 1913->1914 | yoy_jump | emig_rate 28.97 -> 14.21 (WWI disruption) |
| migration | Forlì 1914->1915 | yoy_jump | emig_rate 14.21 -> 4.01 (WWI disruption) |
| migration | Forlì 1915->1916 | yoy_jump | emig_rate 4.01 -> 1.72 (WWI disruption) |
| migration | Forlì 1919->1920 | yoy_jump | emig_rate 4.51 -> 8.06 (WWI disruption) |
| migration | Genova 1913->1914 | yoy_jump | emig_rate 7.6 -> 4.44 (WWI disruption) |
| migration | Girgenti 1913->1914 | yoy_jump | emig_rate 50.7 -> 15.78 (WWI disruption) |
| migration | Girgenti 1914->1915 | yoy_jump | emig_rate 15.78 -> 3.9 (WWI disruption) |
| migration | Girgenti 1915->1916 | yoy_jump | emig_rate 3.9 -> 6.49 (WWI disruption) |
| migration | Girgenti 1919->1920 | yoy_jump | emig_rate 10.58 -> 37.46 (WWI disruption) |
| migration | Grosseto 1913->1914 | yoy_jump | emig_rate 11.9 -> 5.18 (WWI disruption) |
| migration | Grosseto 1914->1915 | yoy_jump | emig_rate 5.18 -> 0.74 (WWI disruption) |
| migration | Grosseto 1915->1916 | yoy_jump | emig_rate 0.74 -> 0.45 (WWI disruption) |
| migration | Grosseto 1919->1920 | yoy_jump | emig_rate 1.46 -> 2.85 (WWI disruption) |
| migration | Lecce 1913->1914 | yoy_jump | emig_rate 6.0 -> 3.78 (WWI disruption) |
| migration | Lecce 1914->1915 | yoy_jump | emig_rate 3.78 -> 0.38 (WWI disruption) |
| migration | Lecce 1919->1920 | yoy_jump | emig_rate 0.73 -> 2.45 (WWI disruption) |
| migration | Livorno 1913->1914 | yoy_jump | emig_rate 10.38 -> 6.4 (WWI disruption) |
| migration | Livorno 1914->1915 | yoy_jump | emig_rate 6.4 -> 3.52 (WWI disruption) |
| migration | Lucca 1913->1914 | yoy_jump | emig_rate 29.83 -> 16.94 (WWI disruption) |
| migration | Lucca 1914->1915 | yoy_jump | emig_rate 16.94 -> 8.35 (WWI disruption) |
| migration | Lucca 1919->1920 | yoy_jump | emig_rate 18.35 -> 27.88 (WWI disruption) |
| migration | Macerata 1913->1914 | yoy_jump | emig_rate 27.91 -> 11.77 (WWI disruption) |
| migration | Macerata 1914->1915 | yoy_jump | emig_rate 11.77 -> 2.94 (WWI disruption) |
| migration | Macerata 1915->1916 | yoy_jump | emig_rate 2.94 -> 1.66 (WWI disruption) |
| migration | Macerata 1919->1920 | yoy_jump | emig_rate 3.83 -> 16.03 (WWI disruption) |
| migration | Mantova 1913->1914 | yoy_jump | emig_rate 14.33 -> 7.9 (WWI disruption) |
| migration | Mantova 1914->1915 | yoy_jump | emig_rate 7.9 -> 1.73 (WWI disruption) |
| migration | Mantova 1919->1920 | yoy_jump | emig_rate 1.37 -> 2.7 (WWI disruption) |
| migration | Massa e Carrara 1914->1915 | yoy_jump | emig_rate 16.71 -> 7.88 (WWI disruption) |
| migration | Massa e Carrara 1919->1920 | yoy_jump | emig_rate 11.96 -> 24.06 (WWI disruption) |
| migration | Messina 1913->1914 | yoy_jump | emig_rate 39.45 -> 16.04 (WWI disruption) |
| migration | Messina 1914->1915 | yoy_jump | emig_rate 16.04 -> 5.28 (WWI disruption) |
| migration | Messina 1919->1920 | yoy_jump | emig_rate 8.83 -> 27.4 (WWI disruption) |
| migration | Milano 1913->1914 | yoy_jump | emig_rate 9.1 -> 5.73 (WWI disruption) |
| migration | Milano 1914->1915 | yoy_jump | emig_rate 5.73 -> 1.76 (WWI disruption) |
| migration | Milano 1915->1916 | yoy_jump | emig_rate 1.76 -> 0.96 (WWI disruption) |
| migration | Milano 1919->1920 | yoy_jump | emig_rate 2.64 -> 3.78 (WWI disruption) |
| migration | Modena 1914->1915 | yoy_jump | emig_rate 8.55 -> 2.94 (WWI disruption) |
| migration | Napoli 1914->1915 | yoy_jump | emig_rate 4.45 -> 2.06 (WWI disruption) |
| migration | Napoli 1919->1920 | yoy_jump | emig_rate 7.28 -> 13.09 (WWI disruption) |
| migration | Novara 1914->1915 | yoy_jump | emig_rate 26.42 -> 13.28 (WWI disruption) |
| migration | Padova 1914->1915 | yoy_jump | emig_rate 14.12 -> 1.7 (WWI disruption) |
| migration | Padova 1915->1916 | yoy_jump | emig_rate 1.7 -> 0.45 (WWI disruption) |
| migration | Padova 1919->1920 | yoy_jump | emig_rate 2.55 -> 7.86 (WWI disruption) |
| migration | Palermo 1913->1914 | yoy_jump | emig_rate 29.18 -> 11.35 (WWI disruption) |
| migration | Palermo 1914->1915 | yoy_jump | emig_rate 11.35 -> 4.78 (WWI disruption) |
| migration | Palermo 1919->1920 | yoy_jump | emig_rate 9.85 -> 30.27 (WWI disruption) |
| migration | Parma 1913->1914 | yoy_jump | emig_rate 20.49 -> 11.75 (WWI disruption) |
| migration | Parma 1914->1915 | yoy_jump | emig_rate 11.75 -> 4.89 (WWI disruption) |
| migration | Pavia 1913->1914 | yoy_jump | emig_rate 15.88 -> 5.45 (WWI disruption) |
| migration | Pavia 1914->1915 | yoy_jump | emig_rate 5.45 -> 1.76 (WWI disruption) |
| migration | Pavia 1919->1920 | yoy_jump | emig_rate 4.49 -> 6.69 (WWI disruption) |
| migration | Pesaro e Urbino 1913->1914 | yoy_jump | emig_rate 34.99 -> 16.58 (WWI disruption) |
| migration | Pesaro e Urbino 1914->1915 | yoy_jump | emig_rate 16.58 -> 3.34 (WWI disruption) |
| migration | Pesaro e Urbino 1919->1920 | yoy_jump | emig_rate 7.77 -> 20.65 (WWI disruption) |
| migration | Piacenza 1914->1915 | yoy_jump | emig_rate 13.57 -> 6.11 (WWI disruption) |
| migration | Pisa 1913->1914 | yoy_jump | emig_rate 14.75 -> 7.83 (WWI disruption) |
| migration | Pisa 1914->1915 | yoy_jump | emig_rate 7.83 -> 2.62 (WWI disruption) |
| migration | Pisa 1915->1916 | yoy_jump | emig_rate 2.62 -> 4.78 (WWI disruption) |
| migration | Porto Maurizio 1915->1916 | yoy_jump | emig_rate 8.58 -> 18.37 (WWI disruption) |
| migration | Porto Maurizio 1919->1920 | yoy_jump | emig_rate 39.75 -> 23.37 (WWI disruption) |
| migration | Potenza 1913->1914 | yoy_jump | emig_rate 34.43 -> 14.0 (WWI disruption) |
| migration | Potenza 1914->1915 | yoy_jump | emig_rate 14.0 -> 5.34 (WWI disruption) |
| migration | Potenza 1919->1920 | yoy_jump | emig_rate 8.65 -> 26.37 (WWI disruption) |
| migration | Ravenna 1913->1914 | yoy_jump | emig_rate 9.35 -> 4.74 (WWI disruption) |
| migration | Ravenna 1914->1915 | yoy_jump | emig_rate 4.74 -> 1.15 (WWI disruption) |
| migration | Reggio di Calabria 1913->1914 | yoy_jump | emig_rate 38.23 -> 15.55 (WWI disruption) |
| migration | Reggio di Calabria 1914->1915 | yoy_jump | emig_rate 15.55 -> 3.49 (WWI disruption) |
| migration | Reggio di Calabria 1919->1920 | yoy_jump | emig_rate 6.07 -> 28.86 (WWI disruption) |
| migration | Reggio nell'Emilia 1913->1914 | yoy_jump | emig_rate 13.93 -> 6.21 (WWI disruption) |
| migration | Reggio nell'Emilia 1914->1915 | yoy_jump | emig_rate 6.21 -> 1.65 (WWI disruption) |
| migration | Roma 1913->1914 | yoy_jump | emig_rate 19.27 -> 7.05 (WWI disruption) |
| migration | Roma 1914->1915 | yoy_jump | emig_rate 7.05 -> 2.71 (WWI disruption) |
| migration | Roma 1919->1920 | yoy_jump | emig_rate 1.92 -> 7.5 (WWI disruption) |
| migration | Rovigo 1913->1914 | yoy_jump | emig_rate 12.65 -> 6.61 (WWI disruption) |
| migration | Rovigo 1914->1915 | yoy_jump | emig_rate 6.61 -> 0.59 (WWI disruption) |
| migration | Rovigo 1919->1920 | yoy_jump | emig_rate 1.46 -> 2.5 (WWI disruption) |
| migration | Salerno 1913->1914 | yoy_jump | emig_rate 28.82 -> 13.85 (WWI disruption) |
| migration | Salerno 1914->1915 | yoy_jump | emig_rate 13.85 -> 4.82 (WWI disruption) |
| migration | Salerno 1915->1916 | yoy_jump | emig_rate 4.82 -> 2.86 (WWI disruption) |
| migration | Salerno 1919->1920 | yoy_jump | emig_rate 7.59 -> 21.91 (WWI disruption) |
| migration | Sassari 1913->1914 | yoy_jump | emig_rate 20.74 -> 8.43 (WWI disruption) |
| migration | Sassari 1914->1915 | yoy_jump | emig_rate 8.43 -> 1.45 (WWI disruption) |
| migration | Sassari 1915->1916 | yoy_jump | emig_rate 1.45 -> 2.0 (WWI disruption) |
| migration | Sassari 1919->1920 | yoy_jump | emig_rate 6.52 -> 10.02 (WWI disruption) |
| migration | Siena 1914->1915 | yoy_jump | emig_rate 4.11 -> 0.51 (WWI disruption) |
| migration | Siena 1919->1920 | yoy_jump | emig_rate 0.67 -> 1.25 (WWI disruption) |
| migration | Siracusa 1913->1914 | yoy_jump | emig_rate 43.27 -> 12.39 (WWI disruption) |
| migration | Siracusa 1914->1915 | yoy_jump | emig_rate 12.39 -> 3.64 (WWI disruption) |
| migration | Siracusa 1915->1916 | yoy_jump | emig_rate 3.64 -> 6.84 (WWI disruption) |
| migration | Siracusa 1919->1920 | yoy_jump | emig_rate 10.61 -> 29.32 (WWI disruption) |
| migration | Sondrio 1913->1914 | yoy_jump | emig_rate 51.25 -> 31.89 (WWI disruption) |
| migration | Sondrio 1915->1916 | yoy_jump | emig_rate 23.4 -> 5.49 (WWI disruption) |
| migration | Sondrio 1919->1920 | yoy_jump | emig_rate 14.79 -> 25.66 (WWI disruption) |
| migration | Teramo 1913->1914 | yoy_jump | emig_rate 45.72 -> 14.18 (WWI disruption) |
| migration | Teramo 1914->1915 | yoy_jump | emig_rate 14.18 -> 6.06 (WWI disruption) |
| migration | Teramo 1915->1916 | yoy_jump | emig_rate 6.06 -> 9.29 (WWI disruption) |
| migration | Teramo 1919->1920 | yoy_jump | emig_rate 4.17 -> 31.36 (WWI disruption) |
| migration | Torino 1914->1915 | yoy_jump | emig_rate 15.23 -> 7.05 (WWI disruption) |
| migration | Torino 1919->1920 | yoy_jump | emig_rate 9.35 -> 14.46 (WWI disruption) |
| migration | Trapani 1913->1914 | yoy_jump | emig_rate 70.8 -> 17.94 (WWI disruption) |
| migration | Trapani 1914->1915 | yoy_jump | emig_rate 17.94 -> 8.51 (WWI disruption) |
| migration | Trapani 1919->1920 | yoy_jump | emig_rate 16.66 -> 30.55 (WWI disruption) |
| migration | Treviso 1914->1915 | yoy_jump | emig_rate 20.68 -> 2.11 (WWI disruption) |
| migration | Treviso 1915->1916 | yoy_jump | emig_rate 2.11 -> 0.98 (WWI disruption) |
| migration | Treviso 1919->1920 | yoy_jump | emig_rate 4.11 -> 11.74 (WWI disruption) |
| migration | Udine 1914->1915 | yoy_jump | emig_rate 79.63 -> 3.36 (WWI disruption) |
| migration | Udine 1915->1916 | yoy_jump | emig_rate 3.36 -> 0.77 (WWI disruption) |
| migration | Udine 1919->1920 | yoy_jump | emig_rate 6.48 -> 37.52 (WWI disruption) |
| migration | Umbria 1913->1914 | yoy_jump | emig_rate 25.73 -> 12.64 (WWI disruption) |
| migration | Umbria 1914->1915 | yoy_jump | emig_rate 12.64 -> 2.21 (WWI disruption) |
| migration | Umbria 1919->1920 | yoy_jump | emig_rate 5.01 -> 7.46 (WWI disruption) |
| migration | Venezia 1914->1915 | yoy_jump | emig_rate 6.5 -> 2.05 (WWI disruption) |
| migration | Venezia 1915->1916 | yoy_jump | emig_rate 2.05 -> 0.64 (WWI disruption) |
| migration | Venezia 1919->1920 | yoy_jump | emig_rate 0.77 -> 2.45 (WWI disruption) |
| migration | Verona 1913->1914 | yoy_jump | emig_rate 25.27 -> 14.57 (WWI disruption) |
| migration | Verona 1914->1915 | yoy_jump | emig_rate 14.57 -> 3.16 (WWI disruption) |
| migration | Verona 1915->1916 | yoy_jump | emig_rate 3.16 -> 0.69 (WWI disruption) |
| migration | Verona 1919->1920 | yoy_jump | emig_rate 3.7 -> 9.12 (WWI disruption) |
| migration | Vicenza 1914->1915 | yoy_jump | emig_rate 29.39 -> 3.1 (WWI disruption) |
| migration | Vicenza 1915->1916 | yoy_jump | emig_rate 3.1 -> 0.7 (WWI disruption) |
| migration | Vicenza 1919->1920 | yoy_jump | emig_rate 4.14 -> 16.79 (WWI disruption) |
| mortality | Ascoli Piceno 1871 | missing_rate | deaths present, cdr empty |
| mortality | Ascoli Piceno 1881 | missing_rate | deaths present, cdr empty |
| mortality | Ascoli Piceno 1901 | missing_rate | deaths present, cdr empty |
| mortality | Ascoli Piceno 1911 | missing_rate | deaths present, cdr empty |
| mortality | Ascoli Piceno 1931 | missing_rate | deaths present, cdr empty |
| mortality | Avellino 1871 | missing_rate | deaths present, cdr empty |
| mortality | Campobasso 1871 | missing_rate | deaths present, cdr empty |
| mortality | Campobasso 1931 | missing_rate | deaths present, cdr empty |
| mortality | Caserta 1871 | missing_rate | deaths present, cdr empty |
| mortality | Chieti 1871 | missing_rate | deaths present, cdr empty |
| mortality | Cosenza 1871 | missing_rate | deaths present, cdr empty |
| mortality | Foggia 1871 | missing_rate | deaths present, cdr empty |
| mortality | Forlì 1881 | missing_rate | deaths present, cdr empty |
| mortality | Forlì 1901 | missing_rate | deaths present, cdr empty |
| mortality | Forlì 1911 | missing_rate | deaths present, cdr empty |
| mortality | Forlì 1931 | missing_rate | deaths present, cdr empty |
| mortality | Lecce 1871 | missing_rate | deaths present, cdr empty |
| mortality | Pesaro e Urbino 1871 | missing_rate | deaths present, cdr empty |
| mortality | Pesaro e Urbino 1881 | missing_rate | deaths present, cdr empty |
| mortality | Pesaro e Urbino 1901 | missing_rate | deaths present, cdr empty |
| mortality | Pesaro e Urbino 1911 | missing_rate | deaths present, cdr empty |
| mortality | Pesaro e Urbino 1931 | missing_rate | deaths present, cdr empty |
| mortality | Potenza 1871 | missing_rate | deaths present, cdr empty |
| mortality | Salerno 1871 | missing_rate | deaths present, cdr empty |
| mortality | Sondrio 1881 | missing_rate | deaths present, cdr empty |
| mortality | Teramo 1871 | missing_rate | deaths present, cdr empty |
| mortality | Umbria 1881 | missing_rate | deaths present, cdr empty |
| mortality | Umbria 1901 | missing_rate | deaths present, cdr empty |
| mortality | Umbria 1911 | missing_rate | deaths present, cdr empty |
| mortality | Umbria 1931 | missing_rate | deaths present, cdr empty |
