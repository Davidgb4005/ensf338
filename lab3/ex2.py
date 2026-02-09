import timeit
import numpy as np
from matplotlib import pyplot as plt
import random as rd
def build_array(n):
    #my_array = np.empty(n)
    my_array = []
    for i in range(n):
        my_array.append(rd.randint(0,n))
        #my_array[i] = (rd.randint(0,n))
    return my_array

# Bubble Sort
comps =  0
swaps = 0
def bubble_sort(arr):
    global comps
    global swaps
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps = swaps + 1
            comps = comps + 1
    return arr




# Quick Sort
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

def timer_fn(n):
    quick_sort_times = []
    bubble_sort_times = []
    array_sizes = np.linspace(0,n,20)
    for i in range(len(array_sizes)):
        array_sizes[i]=  array_sizes[i]
        my_array = build_array(i)
        bubble_sort_times.append(timeit.timeit(lambda: bubble_sort(my_array.copy()),number= 100)/100)
        quick_sort_times.append(timeit.timeit(lambda: quick_sort(my_array.copy()),number= 100)/100)
    
    plt.scatter(array_sizes, quick_sort_times, label="quick")
    plt.scatter(array_sizes, bubble_sort_times, label="Bubble")
    plt.legend()
    plt.show()
timer_fn(100000)
timer_fn(100)