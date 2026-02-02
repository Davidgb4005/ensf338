import json
import numpy as np
from IPython.display import Video
import math
import timeit
import random as rd
from matplotlib import pyplot as plt
Video("linear.mp4", embed=True)

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

if __name__ == "__main__":
	f = open("large-file.json", "r", encoding="utf-8")
	data = f.read()
	json_data = json.loads(data)
	f.close()


record_count_array = [1000]
execution_count = 1000
execution_time_array =[]
#print(len(json_data))
for i in range(1):
	count = record_count_array[0]
	test_array = []
	inc = 0
	while inc < count:
		test_array.append(json_data[rd.randint(0,len(json_data))-1])
		inc = inc +1

	execution_time_array.append(timeit.repeat(lambda:tree_traversal_and_replace(test_array),number=1,repeat=execution_count))


plt.rcParams['figure.figsize'] = [10, 5]
plt.hist(execution_time_array,bins=60)
plt.savefig("output.3.3.png")
plt.show()