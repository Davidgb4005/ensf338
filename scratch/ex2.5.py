
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
execution_count = 10
execution_time_array = []
execution_time_array.append(timeit.timeit(lambda:tree_traversal_and_replace(json_data),number=execution_count)/execution_count)
print(execution_time_array)