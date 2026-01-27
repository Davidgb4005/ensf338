import matplotlib.pyplot as plt
import pandas as pd
import math


data = pd.read_json("internetdata.json")

over_10000_series = data[data["incomeperperson"]>10000]
under_10000_series = data[data["incomeperperson"]<10000]
#print(over_10000_series)
plt.xticks(rotation=90)
plt.hist(over_10000_series["internetuserate"])
plt.savefig("hist2.png")
plt.show()
plt.hist(under_10000_series["internetuserate"])
plt.savefig("hist1.png")
plt.show()
#print(data)