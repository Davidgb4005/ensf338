import timeit
import numpy as np
from matplotlib import pyplot as plt
import random as rd

def build_array(n):
    return [rd.randint(0, n) for _ in range(n)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def timer_fn(max_size):
    array_sizes = np.linspace(10, max_size, 20).astype(int)
    bubble_times = []
    quick_times = []

    for size in array_sizes:
        my_array = build_array(size)

        n_repeat = 10 if size < 1000 else 1

        bubble_time = timeit.timeit(lambda: bubble_sort(my_array.copy()), number=n_repeat) / n_repeat
        quick_time = timeit.timeit(lambda: quick_sort(my_array.copy()), number=n_repeat) / n_repeat

        bubble_times.append(bubble_time)
        quick_times.append(quick_time)

    plt.scatter(array_sizes, bubble_times, color="red", label="Bubble Sort")
    plt.scatter(array_sizes, quick_times, color="blue", label="Quick Sort")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title(f"Bubble vs Quick Sort up to {max_size}")
    plt.legend()
    plt.show()

timer_fn(1000)
timer_fn(20000)