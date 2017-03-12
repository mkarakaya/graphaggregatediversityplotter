import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json
import operator
import math
# the histogram of the data

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.5       # the width of the bars
fig, ax = plt.subplots()
fname = "../../data/analyse/Movielens# of Ratings VS Average Recommendation Count_# of Ratings_Average Recommendation Count.json"
with open(fname) as f:
    jsonData = json.load(f)

rects_list= []
labels=[]
xaxisSortedValues=[]
xaxisSortedKeys=[]
for lineJson in jsonData["graphItemDataList"]:
    xaxis=lineJson["xAxis"]
    xaxisSortedTuples=sorted(xaxis.items(), key=lambda x: x[1])
    for k, v in xaxisSortedTuples:
        xaxisSortedValues.append(v)
        xaxisSortedKeys.append(k)
    rects = ax.bar(ind, xaxisSortedValues, width)
    rects_list.append(rects[0])
    labels.append(lineJson["displayName"])


# add some text for labels, title and axes ticks
ax.set_ylabel(jsonData["yAxisLabel"])
ax.set_xlabel(jsonData["xAxisLabel"])
ax.set_title(jsonData["title"])
ax.set_xticks(ind + width / 2)
low = min(xaxisSortedValues)
high = max(xaxisSortedValues)
plt.ylim([0, math.ceil(high+0.5*(high-low))])
ax.set_xticklabels(xaxisSortedKeys)
displayNames=[]
displayNames.append(lineJson["displayName"])
ax.legend((rects_list), displayNames)



plt.show()
