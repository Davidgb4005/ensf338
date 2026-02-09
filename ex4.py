import sys
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Increase recursion limit to handle deep recursion in worst-case quicksort.
sys.setrecursionlimit(10000)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def measure_time(func, arr, number=3):
    timer = timeit.Timer(lambda: func(arr))
    return timer.timeit(number=number) / number

# Function to generate worst-case input for quicksort (already sorted array).
def worst_case_input(n):
    return list(range(n))

# Test quicksort on worst-case inputs of increasing size.
sizes = np.linspace(10, 500, 20, dtype=int)  # 20 sizes between 10 and 500
times = []

for n in sizes:
    arr = worst_case_input(n)
    t = measure_time(quicksort, arr)
    times.append(t)