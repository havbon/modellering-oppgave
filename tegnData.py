import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import json
import time

extremePath = "./ekstremvær"


def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print(f"{end - start}s")

    return wrapper


# @timeit
def simplify():
    files: list[str] = [os.path.join(extremePath, a)
                        for a in os.listdir(extremePath)]
    data = {}

    def addOne(year: str, eventType: str):
        if not year in list(data.keys()):
            data[year] = {}

        if not eventType in list(data[year].keys()):
            data[year][eventType] = 0

        data[year][eventType] += 1

    for i, file in enumerate(files):
        print(file.removeprefix(extremePath), round((i * 100) / len(files), 2))
        assert os.path.isfile(file)

        df = pd.read_excel(file)

        for a in df.iloc[:, [11, 13, 15, 28]].to_numpy():
            magnitude = a[3]
            if magnitude > 51:
                if a[2] in [149, 92, 77, 43, 39, 17, 71]:
                    addOne(a[0], a[1])

        del df

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Done!")


def draw():
    obj = {}
    with open("data.json", "r") as file:
        obj = json.load(file)

    # first get all the different types
    differentTypes = set()
    for year in obj:
        for eventType in obj[year]:
            differentTypes.add(eventType)

    # make a new dict with eventtype: list[int] occurence per year
    newFormat = {}
    for eventType in differentTypes:
        newFormat[eventType] = []

    # add occurence to each list
    for year in obj:
        for eventType in obj[year]:
            occurances = obj[year][eventType]
            newFormat[eventType].append(occurances)

    # pad with zeroes at start
    # get longest record
    longest = -1
    for data in newFormat.values():
        longest = max(longest, len(data))

    # pad everything with zeroes until it has len longest
    for eventType in newFormat:
        while len(newFormat[eventType]) < longest:
            newFormat[eventType].insert(0, None)
    assert all([len(a) == longest for a in newFormat.values()])

    xData = np.array([1950 + i for i in range(longest)])[:39]
    for label, ydata in list(newFormat.items()):
        ydata = ydata[:39]
        if label.lower() in ["thunderstorm wind"]:
            plt.plot(xData, ydata, label=label)

            [print(a) for a in (xData)]
            print("-"*25)
            [print(a) for a in ydata]

    font = {"family": "sans serif", "color": "black", "size": 11}
    h1 = {"family": "sans serif", "color": "black", "size": 15}

    plt.grid()
    plt.title("registrert ekstremvær", fontdict=h1)
    plt.xlabel("år", fontdict=font)
    plt.ylabel("ekstremvær", fontdict=font)
    plt.legend()
    plt.show()


# simplify()
draw()
