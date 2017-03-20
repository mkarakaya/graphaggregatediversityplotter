import matplotlib.pyplot as plt
import json
import numpy as np

fname = "../../data/proposed/10/SVD Yahoo Music_precision_individual diversity.json"
with open(fname) as f:
    jsonData = json.load(f)

for lineJson in jsonData["graphItemDataList"]:
    order = np.argsort(lineJson["xAxis"])
    xs = np.array(lineJson["xAxis"])[order]
    ys = np.array(lineJson["yAxis"])[order]
    plt.plot(xs, ys, label=lineJson["displayName"], marker='o')

plt.legend(loc='upper left')
font = {'weight': 'bold', 'size': 13}

plt.rc('font', **font)
plt.suptitle(jsonData["title"])
plt.ylabel(jsonData["yAxisLabel"],fontsize=22)
plt.xlabel(jsonData["xAxisLabel"], fontsize=22)
plt.show()
