
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





def timer_fn(n):
    global comps
    global swaps

    bubble_sort_comps = []
    bubble_sort_swaps = []

    array_sizes = np.linspace(0, n, 20).astype(int)

    for size in array_sizes:
        comp_array = []
        swap_array = []

        for _ in range(10):
            my_array = build_array(size)
            comps = 0
            swaps = 0
            bubble_sort(my_array)
            comp_array.append(comps)
            swap_array.append(swaps)

        bubble_sort_comps.append(np.mean(comp_array))
        bubble_sort_swaps.append(np.mean(swap_array))

    plt.scatter(array_sizes, bubble_sort_comps, label="comparisons")
    plt.scatter(array_sizes, bubble_sort_swaps, label="swaps")
    plt.legend()
    plt.show()

timer_fn(10000)