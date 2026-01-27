import json
import numpy as np
from IPython.display import Video
Video("linear.mp4", embed=True)
import math
import timeit
import random as rd
from matplotlib import pyplot as plt


def tree_traversal_and_replace(my_array):
	for i in my_array:	#Handles List Wrapper On Json
		find_size(i) 

def find_size(input_dict):
	if "size" in input_dict:
		input_dict["size"] = 42
		#print(input_dict["size"])
	for i in input_dict:
		if type(input_dict[i]) == dict:
			#print(i)
			find_size(input_dict[i])


f = open("large-file.json", "r")
data = f.read()
json_data = json.loads(data)
f.close()

record_count_array = [1000,2000,5000,10000]
execution_count = 50
execution_time_array =[]
#print(len(json_data))
for i in range(len(record_count_array)):
	count = record_count_array[i]
	test_array = []
	inc = 0
	while inc < count:
		test_array.append(json_data[rd.randint(0,len(json_data))-1])
		inc = inc +1
	#print(len(test_array))
	execution_time_array.append(timeit.timeit(lambda:tree_traversal_and_replace(test_array),number=execution_count)/execution_count)

for i in execution_time_array:
	#print(i)
	pass

plt.rcParams['figure.figsize'] = [10, 5]

print(execution_count)
print(execution_time_array)
slope, intercept = np.polyfit(record_count_array, execution_time_array, 1)
plt.scatter(record_count_array, execution_time_array)
linevalues = [slope * x + intercept for x in record_count_array]
plt.plot(record_count_array, linevalues, 'r')
plt.show()
# Finally, print out the linear relationship between input length and time.
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))