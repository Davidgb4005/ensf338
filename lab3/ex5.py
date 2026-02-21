import numpy as np
import random as rd
import timeit
from matplotlib import pyplot as plt

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def binary_insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i-1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        j = i - 1
        while j >= left:
            arr[j+1] = arr[j]
            j -= 1
        arr[left] = key
    return arr

array_sizes = [10, 50, 100, 200, 500, 1000, 2000]
num_trials = 10

insertion_times = []
binary_insertion_times = []

for size in array_sizes:
    arr_list = [rd.randint(0, size) for _ in range(size)]
    
    t_insertion = timeit.timeit(lambda: insertion_sort(np.array(arr_list)), number=num_trials) / num_trials
    insertion_times.append(t_insertion)
    
    t_binary = timeit.timeit(lambda: binary_insertion_sort(np.array(arr_list)), number=num_trials) / num_trials
    binary_insertion_times.append(t_binary)

plt.scatter(array_sizes, insertion_times, label="Insertion Sort", color="red")
plt.scatter(array_sizes, binary_insertion_times, label="Binary Insertion Sort", color="blue")

coeffs_ins = np.polyfit(array_sizes, insertion_times, 2)
x_smooth = np.linspace(min(array_sizes), max(array_sizes), 200)
y_ins_smooth = np.polyval(coeffs_ins, x_smooth)
plt.plot(x_smooth, y_ins_smooth, color="red", linestyle="--")

# Quadratic interpolation for binary insertion sort
coeffs_bin = np.polyfit(array_sizes, binary_insertion_times, 2)
y_bin_smooth = np.polyval(coeffs_bin, x_smooth)
plt.plot(x_smooth, y_bin_smooth, color="blue", linestyle="--")

plt.xlabel("Array Size")
plt.ylabel("Average Time per Sort (s)")
plt.title("Insertion Sort vs Binary Insertion Sort Performance")
plt.legend()
plt.show()

# Discussion:
# Binary insertion sort is generally faster than traditional insertion sort on larger arrays.
# The binary search reduces the number of comparisons to find the insertion point (O(log n)),
# whereas traditional insertion sort always performs linear search (O(n)) for each insertion.
# However, shifting elements still takes O(n) time in both algorithms, so for very small arrays,
# the difference may not be noticeable. For larger arrays, binary insertion sort tends to outperform.