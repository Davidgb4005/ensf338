import timeit
import random
import numpy as np
import matplotlib.pyplot as plt


def insertion_sort(arr):
    #traditional insertion sort
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

def binary_insertion_sort(arr):
   #Binary Insertion Sort using binary search to find insertion point
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        # Binary search to find the index where key should be inserted
        left, right = 0, i - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        # Shift elements to make space for key
        a[left+1:i+1] = a[left:i]
        a[left] = key
    return a


def measure_time(func, arr, number=3):
   #Measure average execution time of func on arr over 'number' runs.
    timer = timeit.Timer(lambda: func(arr))
    return timer.timeit(number=number) / number

# Create a range of input sizes for average-case (random) inputs.
sizes = np.linspace(50, 500, 20, dtype=int)

# Dictionaries to store measured times.
times_insertion = []
times_binary = []

for n in sizes:
    # Generate a random array of size n
    arr = [random.randint(0, 1000) for _ in range(n)]
    
    # Measure execution time for traditional insertion sort
    t_insertion = measure_time(insertion_sort, arr)
    times_insertion.append(t_insertion)
    
    # Measure execution time for binary insertion sort
    t_binary = measure_time(binary_insertion_sort, arr)
    times_binary.append(t_binary)



plt.figure(figsize=(8, 5))
plt.plot(sizes, times_insertion, marker='o', label='Traditional Insertion Sort')
plt.plot(sizes, times_binary, marker='s', label='Binary Insertion Sort')

# Fit quadratic functions to the data (since both are O(n^2))
coeffs_insertion = np.polyfit(sizes, times_insertion, 2)
poly_insertion = np.poly1d(coeffs_insertion)
coeffs_binary = np.polyfit(sizes, times_binary, 2)
poly_binary = np.poly1d(coeffs_binary)

# Generate smooth curves for interpolation
sizes_smooth = np.linspace(sizes.min(), sizes.max(), 200)
plt.plot(sizes_smooth, poly_insertion(sizes_smooth), linestyle='--', color='blue', alpha=0.5)
plt.plot(sizes_smooth, poly_binary(sizes_smooth), linestyle='--', color='orange', alpha=0.5)

plt.xlabel('Input Size (n)')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average-case Performance: Insertion Sort vs. Binary Insertion Sort')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('ex5_performance.png')
plt.show()

# 4. Discussion (Answer to Question 4)

# In our experiments, binary insertion sort consistently outperforms traditional insertion sort.
# This is because binary insertion sort uses binary search to locate the correct insertion position,
# reducing the number of comparisons needed. Although both algorithms have an O(n^2) worst-case time
# complexity due to the cost of shifting elements, the reduced number of comparisons gives binary insertion
# sort a constant-factor advantage, especially as the input size increases.
