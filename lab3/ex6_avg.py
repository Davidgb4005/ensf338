import timeit
import numpy as np
from matplotlib import pyplot as plt
import random as rd

def build_array(n):
    my_array = np.empty(n)
    for i in range(n):
        my_array[i] = rd.randint(0, n)
    return my_array

def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def sort_and_binary_search(arr, target):
    arr_sorted = quick_sort(arr)
    return binary_search(arr_sorted, target)

array_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_times = []
sort_bin_times = []

for size in array_sizes:
    linear_avg = 0
    sort_bin_avg = 0
    for _ in range(100):
        arr = build_array(size)
        target = arr[rd.randint(0, size-1)]
        sorted_arr = quick_sort(arr.copy())

        linear_avg += timeit.timeit(lambda: linear_search(arr, target), number=1)
        sort_bin_avg += timeit.timeit(lambda: sort_and_binary_search(arr.copy(), target), number=1)

    linear_times.append(linear_avg/100)
    sort_bin_times.append(sort_bin_avg/100)

plt.scatter(array_sizes, linear_times, label="Linear Search", color="red")
plt.scatter(array_sizes, sort_bin_times, label="Sort + Binary Search", color="blue")
plt.xlabel("Array size")
plt.ylabel("Time per search (s)")
plt.title("Average-case Search Performance")
plt.legend()
plt.show()


#discussion
#Linear Search is faster for finding a singular element once, as everytime we ran the test we also unordered
#the test array it meant that the binary search never had the advantage that would occur if we had to search
#the same test data for multiple values where we would see the benefit of sort come into play
#instead of restarting the test with a unorder array always meant it was wasting time sorting for no
#advatnage