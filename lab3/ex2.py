import timeit
import numpy as np
from matplotlib import pyplot as plt
import random as rd
import sys
sys.setrecursionlimit(20000)
def build_array(n):
    return [rd.randint(0, n) for _ in range(n)]

def build_array_sort(n):
    return list(range(n))
def build_array_sort_rev(n):
    arr = list(range(n))
    arr.reverse()
    return arr
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

def timer_fn(max_size,sort):
    array_sizes = np.linspace(10, max_size, 20).astype(int)
    bubble_times = []
    quick_times = []

    for size in array_sizes:
        bubble = []
        quick = []
        for i in range(5):
            if sort == 'Decending Sorted':
                my_array = build_array_sort_rev(size)
                bub_sort = "O(n^2)"
                q_sort = "O(n^2)"
            elif sort == 'Ascending Sorted':
                my_array = build_array_sort(size)
                bub_sort = "O(n^2)"
                q_sort = "O(n^2)"
            else:
                my_array = build_array(size)
                bub_sort = "O(n^2)"
                q_sort = "O(n Log(n))"
            n_repeat = 100 if size < 1000 else 5 

            bubble.append(timeit.timeit(lambda: bubble_sort(my_array.copy()), number=n_repeat) / n_repeat)
            quick.append(timeit.timeit(lambda: quick_sort(my_array.copy()), number=n_repeat) / n_repeat)

        bubble_times.append(np.mean(bubble))
        quick_times.append(np.mean(quick))

    plt.scatter(array_sizes, bubble_times, color="red", label=f"Bubble Sort {bub_sort}")
    plt.scatter(array_sizes, quick_times, color="blue", label=f"Quick Sort {q_sort}")
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title(f"Bubble vs Quick Sort up to {max_size} : Array is {sort}")
    plt.legend()
    plt.savefig(f"ex2_{sort}_{max_size}.png")
    plt.show()

timer_fn(300,'Decending Sorted')
timer_fn(300,'Ascending Sorted')
timer_fn(300,'Unsorted')

timer_fn(50,'Decending Sorted')
timer_fn(50,'Ascending Sorted')
timer_fn(50,'Unsorted')