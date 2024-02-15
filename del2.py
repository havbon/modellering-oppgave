from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np


år = np.array([2008, 2010, 2012, 2014, 2016, 2018])
strømming = np.array([7, 70, 246, 456, 582, 655])

startår = 2008
x = år - år[0]


def logistisk(x, a, b, c):
    return c / (1 + a * np.exp(-b * x))


c0 = max(strømming)
a0 = c0 / strømming[0] - 1
xm = np.median(x)
ym = np.median(strømming)
b0 = -np.log((c0/ym - 1) / a0) / xm

a0, b0, c0 = curve_fit(logistisk, x, strømming, [a0, b0, c0])[0]
print(f"{c0} / (1 + {a0} * exp(-{b0} * x))")

plt.plot(x, logistisk(x, a0, b0, c0), color="grey")
plt.scatter(x, strømming)
plt.show()
