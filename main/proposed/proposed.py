import json
import matplotlib.pyplot as plt
import numpy as np
from os import listdir

path = "../../data/proposed/"
folder = "10"
save_dir = "/home/mokarakaya/Documents/latex/"
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

    plt.legend(loc='upper left')
    font = {'weight': 'bold', 'size': 13}

    plt.rc('font', **font)
    plt.suptitle(jsonData["title"])
    plt.ylabel(jsonData["yAxisLabel"], fontsize=22)
    plt.xlabel(jsonData["xAxisLabel"], fontsize=22)
    plt.savefig(save_dir + folder + file_name.replace('.json', '.eps'))

