import numpy as np
import matplotlib.pyplot as plt
import json

# load json manually
with open("internetdata.json") as f:
    my_file = json.load(f)

income = []
internet = []

for row in my_file:
    inc = row["incomeperperson"]
    net = row["internetuserate"]
    income.append(inc)
    internet.append(net)

income = np.array(income)
internet = np.array(internet)

over_10000 = internet[income > 10000]
under_10000 = internet[income < 10000]


plt.hist(over_10000)
plt.savefig("hist2.png")
plt.show()

plt.hist(under_10000)
plt.savefig("hist1.png")
plt.show()