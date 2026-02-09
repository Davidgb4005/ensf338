import timeit
import numpy as np
from matplotlib import pyplot as plt
import random as rd
def build_array(n):
    my_array = np.empty(n)
    #my_array = []
    for i in range(n):
        #my_array.append(rd.randint(0,n))
        my_array[i] = (rd.randint(0,n))
    return my_array

def linear_search(arr, target):
    """Perform a linear search for the target in the vector."""
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

def binary_search(arr, target):
    """Perform a binary search for the target in the sorted vector."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)

def quick_search_and_sort(arr,target):
    arr = quick_sort(arr)
    binary_search(arr,target)


def timer_fn(n):
    binary_search_times = []
    linear_search_times = []

    array_sizes = np.linspace(1, n, 40).astype(int)

    for size in array_sizes:
        my_array = build_array(size)
        search_value = my_array[rd.randint(0, size - 1)]

        sorted_array = quick_sort(my_array.copy())

        binary_search_times.append(
            timeit.timeit(lambda: binary_search(sorted_array, search_value), number=100) / 100
        )

        linear_search_times.append(
            timeit.timeit(lambda: linear_search(my_array, search_value), number=100) / 100
        )

    plt.scatter(array_sizes, binary_search_times, label="binary search")
    plt.legend()
    plt.show()

    plt.scatter(array_sizes, linear_search_times, label="linear search")
    plt.legend()
    plt.show()
timer_fn(10000)