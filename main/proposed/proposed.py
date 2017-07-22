import json
import matplotlib.pyplot as plt
import numpy as np
from os import listdir

path = "../../data/proposed/"
folder = "20"
save_dir = "/home/mokarakaya/Documents/graphaggregatediversitytex/"
marker_dict = {'SVD-based': 'o', 'Graph-based': 'v', 'Popularity': '*', 'AverageRating': 's'}

files = [f for f in listdir(path + folder)]
for file_name in files:
    print file_name
    with open(path + folder + '/' + file_name) as f:
        jsonData = json.load(f)
    plt.figure()
    for lineJson in jsonData["graphItemDataList"]:
        order = np.argsort(lineJson["xAxis"])
        xs = np.array(lineJson["xAxis"])[order]
        ys = np.array(lineJson["yAxis"])[order]
        plt.plot(xs, ys, label=lineJson["displayName"],
                 marker=marker_dict[lineJson["displayName"]], markersize=10)

    ax = plt.gca()
    min_y, max_y = ax.get_ylim()
    min_x, max_x = ax.get_xlim()

    if "yMin" in jsonData:
        min_y = float(jsonData['yMin'])

    if "xMin" in jsonData:
        min_x = float(jsonData['xMin'])

    if "xMax" in jsonData:
        max_x = float(jsonData['xMax'])

    plt.ylim(min_y, float(jsonData['yMax']))
    plt.xlim(min_x, max_x)
    plt.legend(loc='upper ' + jsonData['legend'])
    font = {'weight': 'bold', 'size': 13}

    plt.rc('font', **font)
    plt.suptitle(jsonData["title"])
    plt.ylabel(jsonData["yAxisLabel"], fontsize=22)
    plt.xlabel(jsonData["xAxisLabel"], fontsize=22)
    plt.savefig(save_dir + folder + file_name.replace('.json', '.eps'))

