import json
import numpy as np
import timeit
import matplotlib.pyplot as plt

with open("ex7data.json", "r") as f:
    data = json.load(f)  # sorted array
with open("ex7tasks.json", "r") as f:
    tasks = json.load(f)  # list of numbers to search

data = np.array(data)

def binary_search_custom(arr, target, first_mid=None):
    left, right = 0, len(arr)-1
    if first_mid is None:
        mid = (left + right) // 2
    else:
        mid = first_mid
    first_iteration = True

    while left <= right:
        if first_iteration:
            first_iteration = False
        else:
            mid = (left + right) // 2

        if mid < 0 or mid >= len(arr):
            return -1
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_best_midpoint(arr, target):
    best_time = 0 
    best_mid = None
    for frac in [0.0, 0.1, 0.25, 0.33, 0.5, 0.66, 0.75, 0.9, 1.0]:
        mid = int(frac * (len(arr)-1))
        t = timeit.timeit(lambda: binary_search_custom(arr, target, first_mid=mid), number=100)
        if t < best_time:
            best_time = t
            best_mid = mid
    return best_mid, best_time

best_midpoints = []
for task in tasks:
    best_mid, best_time = find_best_midpoint(data, task)
    best_midpoints.append(best_mid)

plt.scatter(range(len(tasks)), best_midpoints)
plt.xlabel("Task index")
plt.ylabel("Chosen first midpoint index")
plt.title("Best starting midpoint for each search task")
plt.show()

# --- Discussion ---
# The scatterplot shows No Trend.
# After the first iteration, the standard binary search proceeds normally, so only the first step is affected.
# So there is little effect by just changin the starting point as even if you pick the first
# element it will only result 1 more iteration as the second iteration just would perform a regular
# B search if you weighted every split i would have a more noticable effect