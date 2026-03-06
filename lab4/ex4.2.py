import numpy as np
from matplotlib import pyplot as plt
import timeit
import random as rd



def sorted_linear_search(li,target):
    for i in range(len(li)):
        if li[i] ==target:
            #print("Found Target")
            return(i)
    #print("Target DNE")
    return (-1)
# Worst Case N

def sorted_binary_search(li, target):
    low = 0
    high = len(li) - 1
    mid = (low + high) // 2
    while low <= high:
        mid = (low + high) // 2
        if li[mid] == target:
            #print("Target Found")
            return mid
        elif target < li[mid]:
            high = mid - 1
        else:
            low = mid + 1

    #print("Target DNE")
    return -1
#Worst Case Log(N) assuming Sorted Data


array_sizes = [1000, 3000,5000,10000,20000,30000,40000,50000,60000]
num_trials = 100

linear_times = []
binary_times = []

for size in array_sizes:
    arr_list = [rd.randint(0, size) for _ in range(size)]
    target = size+1
    t_insertion = timeit.timeit(lambda: sorted_linear_search(np.array(arr_list),target), number=num_trials) / num_trials
    linear_times.append(t_insertion)
    
    t_binary = timeit.timeit(lambda: sorted_binary_search(np.array(arr_list),target), number=num_trials) / num_trials
    binary_times.append(t_binary)
    print("Trail Done")

plt.scatter(array_sizes, linear_times, label="Linear", color="red")
plt.scatter(array_sizes, binary_times, label="Binary", color="blue")
plt.show()