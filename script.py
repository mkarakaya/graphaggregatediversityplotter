import matplotlib.pyplot as plt
import json

fname = "data.json"
with open(fname) as f:
    lineJsonList = json.load(f)

for lineJson in lineJsonList:
    plt.plot(lineJson["xAxis"], [1, 2, 3, 4], label=lineJson["label"])

plt.legend()
plt.ylabel('some numbers')
plt.show()
