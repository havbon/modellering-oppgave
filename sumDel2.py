import numpy as np


def f(x):
    return 660.36 / (1 + (30.72 * np.exp(-0.71 * x)))


s = np.array(range(11))
yListe = [f(a) for a in s]
print(round(sum(yListe), 2))


