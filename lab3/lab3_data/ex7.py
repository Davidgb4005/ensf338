import json
import matplotlib.pyplot as plt
import timeit
import numpy as np
import random as rd
with open("/home/esp/ensf338/lab3/lab3_data/ex7data.json", 'r', encoding='UTF-8') as infile:
    data = json.load(infile)

with open("/home/esp/ensf338/lab3/lab3_data/ex7tasks.json", 'r', encoding='UTF-8') as infile:
    search_tasks = json.load(infile)

#Modified Binary Search
def binarySearch(arr, first, last, key, mid):
    global rec_count
    rec_count += 1
    if first <= last:
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binarySearch(arr, first, mid - 1, key, (first + mid - 1) // 2)
        else:
            return binarySearch(arr, mid + 1, last, key, (mid + 1 + last) // 2)
    return -1 

#Time Performace of Each Search Task
def timerForBinarySearch(arr, last, key, mid):
    global rec_count
    rec_count = 0
    timer = timeit.Timer(lambda: binarySearch(arr, 0, last, key, mid))
    return timer.timeit(number=1)


print(len(data))
time = []
midpoints = []
time_2 = []
midpoints_2 = []
last_index = len(data) - 1
rec_count_1 = []
rec_count_2 = []
rate = max(data)-min(data)
for key in search_tasks:

    best_time = float("inf")
    best_mid = None
    best_time_2 = float("inf")
    best_mid_2 = None
    for i in range(0,1,1):
        #ind = i/500
        ind = key/rate
        rec_count = 0
        time_taken = timerForBinarySearch(data, last_index, key, round(len(data)*ind))
        if best_time > time_taken:
            best_time = time_taken
            best_mid = round(len(data)*ind)
            best_rec_1 = rec_count

        rec_count = 0
        start_point = rd.randint(0,len(data))
        time_taken_2 = timerForBinarySearch(data, last_index, key, round(len(data)//2))

        if best_time_2 > time_taken_2:
            best_time_2 = time_taken_2
            best_mid_2 = round(len(data)//2)
            best_rec_2 = rec_count

    midpoints.append(best_mid)
    time.append(best_time)
    midpoints_2.append(best_mid_2)
    time_2.append(best_time_2)
    rec_count_1.append(best_rec_1)
    rec_count_2.append(best_rec_2)
#Scatterplot using relavant data
print(np.mean(rec_count_1))
print(np.mean(rec_count_2))
plt.figure(figsize=(10, 5))
plt.hist(data,bins=1000)
plt.show()
plt.scatter(search_tasks, midpoints, color='red', label='Midpoint')
plt.scatter(search_tasks, midpoints_2, color='blue', label='Midpoint')
plt.xlabel('Search Task (Target Number)')
plt.ylabel('Best Initial Midpoint')
plt.title('Effect of Initial Midpoint on Binary Search Performance')
plt.grid(True)
plt.legend()
plt.savefig('output.7.png')
plt.show()

#The intial midpoint does indeed effeect the preformance of the binary search, if the intial midpoint is closer
# to the target of the search the faster it will run