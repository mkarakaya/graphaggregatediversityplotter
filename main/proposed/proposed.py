import matplotlib.pyplot as plt
import json
import numpy as np

fname = "../../data/proposed/SVD Movielens100K_precision_aggregate.json"
with open(fname) as f:
    jsonData = json.load(f)

for lineJson in jsonData["graphItemDataList"]:
    order = np.argsort(lineJson["xAxis"])
    xs = np.array(lineJson["xAxis"])[order]
    ys = np.array(lineJson["yAxis"])[order]
    plt.plot(xs, ys, label=lineJson["displayName"], marker='o')

plt.legend(loc='upper left')
plt.suptitle(jsonData["title"])
plt.ylabel(jsonData["yAxisLabel"])
plt.xlabel(jsonData["xAxisLabel"])
plt.show()
