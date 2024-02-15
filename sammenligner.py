from matplotlib import pyplot as plt

ekstremværFrekvensDel1 = {
    1970: 36,
    1971: 36,
    1972: 37,
    1973: 27,
    1974: 46,
    1975: 79,
    1976: 44,
    1977: 47,
    1978: 62,
    1979: 62,
    1980: 54,
    1981: 61,
    1982: 66,
    1983: 93,
    1984: 96,
    1985: 80,
    1986: 79,
    1987: 88,
    1988: 69,
}
ekstremværFrekvensDel2 = {
    1989: 161,
    1990: 381,
    1991: 377,
    1992: 525,
    1993: 369,
    1994: 460,
    1995: 594,
    1996: 593,
    1997: 774,
    1998: 800,
    1999: 904,
    2000: 856,
    2001: 914,
    2002: 1120,
    2003: 941,
    2004: 1031,
    2005: 1410,
    2006: 1075,
    2007: 997,
    2008: 961,
    2009: 975,
    2010: 1072,
    2011: 1162,
    2012: 1071,
    2013: 1261,
    2014: 1367,
    2015: 1161,
    2016: 1190,
    2017: 1464,
}
utslipp = {
    1970: 24497.54442,
    1971: 24582.92091,
    1972: 25521.45404,
    1973: 26733.85934,
    1974: 26742.38412,
    1975: 26798.4541,
    1976: 27950.65593,
    1977: 28635.10984,
    1978: 29238.85235,
    1979: 29941.62626,
    1980: 29642.26003,
    1981: 29136.69345,
    1982: 28937.98432,
    1983: 29175.19007,
    1984: 29979.63329,
    1985: 30299.72311,
    1986: 30794.84987,
    1987: 31544.22126,
    1988: 32508.28813,
    1989: 33095.73799,
    1990: 33268.12071,
    1991: 33373.19073,
    1992: 33301.23401,
    1993: 33402.78703,
    1994: 33747.71846,
    1995: 34631.79795,
    1996: 35262.13061,
    1997: 35724.02634,
    1998: 35812.31496,
    1999: 36051.3277,
    2000: 36991.70704,
    2001: 37316.89534,
    2002: 37807.18338,
    2003: 39354.85102,
    2004: 40981.84826,
    2005: 42318.4285,
    2006: 43539.56655,
    2007: 44859.86746,
    2008: 45168.46503,
    2009: 44750.39493,
    2010: 46991.56672,
    2011: 48409.21681,
    2012: 49068.90143,
    2013: 49875.67509,
    2014: 50242.99751,
    2015: 50134.38376,
    2016: 50343.04445,
    2017: 51195.41911,
}

def normaliser(data: dict):
    # finn høyeste verdi
    høyest = -1
    for d in data.values():
        høyest = max(d, høyest)

    # del alle verdiene på høyeste verdi
    resultat = {}
    for k, v in data.items():
        resultat[k] = v / høyest

    return resultat


## først normaliser dataen
ekstremværFrekvensDel1 = normaliser(ekstremværFrekvensDel1)
ekstremværFrekvensDel2 = normaliser(ekstremværFrekvensDel2)
utslipp = normaliser(utslipp)

# slå sammen begge frekvensene
ekstremvær = {}
for k, v in ekstremværFrekvensDel1.items():
    ekstremvær[k] = v

# vi må forskyve alt med den høyeste fra del 1
# for at det skal bli kontinuerlig
for v in ekstremværFrekvensDel1.values():
    høyeste = max(v, høyeste)
for k, v in ekstremværFrekvensDel2.items():
    ekstremvær[k] = v + høyeste

# deretter normaliser den igjen for at den skal gå til maks 1 igjen
ekstremvær = normaliser(ekstremvær)
plt.plot(utslipp.keys(), utslipp.values(), label="utslipp drivhusgasser")
plt.plot(ekstremvær.keys(), ekstremvær.values(), label="registrert ekstremvær")
plt.legend()
plt.grid()
plt.show()