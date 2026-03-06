import sys
sys.setrecursionlimit(20000)
import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

# Bubble sort implementation that stops early if no swaps occur.
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

#  recursive quicksort using the first element as pivot.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left  = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Helper for quicksort best case (pivot = first element)
# Generates a balanced order by recursively choosing the median as pivot.
def generate_quicksort_best_case(sorted_arr):
    if not sorted_arr:
        return []
    mid = len(sorted_arr) // 2
    # The pivot is the median; then recursively process the left and right halves.
    return [sorted_arr[mid]] + generate_quicksort_best_case(sorted_arr[:mid]) + generate_quicksort_best_case(sorted_arr[mid+1:])


def measure_time(func, arr, number=5):
    timer = timeit.Timer(lambda: func(arr))
    total_time = timer.timeit(number=number)
    return total_time / number

# Input sizes to test
sizes = np.linspace(10, 300, 20, dtype=int)

# Prepare dictionaries to store measured times.
# For each algorithm, we will record times for best, worst, and average cases.
results = {
    'bubble': {'best': [], 'worst': [], 'average': []},
    'quick':  {'best': [], 'worst': [], 'average': []}
}

# For each size, create the appropriate input arrays.
for n in sizes:
    # Create a sorted list of n elements.
    sorted_arr = list(range(n))
    
    # Bubble sort inputs:
    arr_bubble_best    = sorted_arr                          # Already sorted
    arr_bubble_worst   = list(range(n, 0, -1))                 # Reverse sorted
    arr_bubble_avg     = sorted_arr.copy()
    random.shuffle(arr_bubble_avg)                              # Random order

    # Quicksort inputs:
    arr_quick_worst    = sorted_arr                          # Already sorted: worst-case for our quicksort.
    arr_quick_avg      = sorted_arr.copy()
    random.shuffle(arr_quick_avg)                               # Random order
    # For best-case, generate a balanced ordering from the sorted list.
    arr_quick_best     = generate_quicksort_best_case(sorted_arr)
    
    # Measure execution times (averaged over a few runs using timeit).
    results['bubble']['best'].append(measure_time(bubble_sort, arr_bubble_best))
    results['bubble']['worst'].append(measure_time(bubble_sort, arr_bubble_worst))
    results['bubble']['average'].append(measure_time(bubble_sort, arr_bubble_avg))
    
    results['quick']['best'].append(measure_time(quicksort, arr_quick_best))
    results['quick']['worst'].append(measure_time(quicksort, arr_quick_worst))
    results['quick']['average'].append(measure_time(quicksort, arr_quick_avg))


# Plotting the performance results
cases = ['best', 'worst', 'average']
for case in cases:
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, results['bubble'][case], marker='o', label='Bubble Sort')
    plt.plot(sizes, results['quick'][case],  marker='s', label='Quick Sort')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title(f'Sorting Performance: {case.capitalize()} Case')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'bubble_vs_quick_{case}.png')
    plt.show()
