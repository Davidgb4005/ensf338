import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_search(vector, target):
    """Perform a linear search for the target in the vector."""
    for i, item in enumerate(vector):
        if item == target:
            return i
    return -1

def binary_search(vector, target):
    """Perform a binary search for the target in the sorted vector."""
    left, right = 0, len(vector) - 1
    while left <= right:
        mid = (left + right) // 2
        if vector[mid] == target:
            return mid
        elif vector[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Vector sizes to test
vector_sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linear_search_times = []
binary_search_times = []

# Loop over different vector sizes
for size in vector_sizes:
    vector = list(range(size))
    # Timing linear search: we run 100 iterations per repeat and repeat 1000 times.
    linear_times = timeit.repeat(lambda: linear_search(vector, random.choice(vector)), number=100, repeat=1000)
    binary_times = timeit.repeat(lambda: binary_search(vector, random.choice(vector)), number=100, repeat=1000)
    
    linear_search_times.append(np.mean(linear_times))
    binary_search_times.append(np.mean(binary_times))

# Define fitting functions
def linear_fit(x, a, b):
    return a * x + b

def log_fit(x, a, b):
    return a * np.log(x) + b

# Plotting the results
plt.figure(figsize=(12, 6))

# Plot linear search times
plt.subplot(1, 2, 1)
plt.plot(vector_sizes, linear_search_times, 'o-', label='Linear Search', color='blue')
plt.title('Linear Search Performance')
plt.xlabel('Vector Size')
plt.ylabel('Time (seconds)')
plt.xscale('log')
plt.yscale('log')

# Fit linear search data to a linear function (O(n) behavior)
popt_linear, _ = curve_fit(linear_fit, vector_sizes, linear_search_times)
plt.plot(vector_sizes, linear_fit(np.array(vector_sizes), *popt_linear), 'r--', 
         label='Fit: y = {:.2e}x + {:.2e}'.format(*popt_linear))
plt.legend()

# Plot binary search times
plt.subplot(1, 2, 2)
plt.plot(vector_sizes, binary_search_times, 'o-', label='Binary Search', color='red')
plt.title('Binary Search Performance')
plt.xlabel('Vector Size')
plt.ylabel('Time (seconds)')
plt.xscale('log')
plt.yscale('log')

# Fit binary search data to a logarithmic function (O(log n) behavior)
popt_binary, _ = curve_fit(log_fit, vector_sizes, binary_search_times)
plt.plot(vector_sizes, log_fit(np.array(vector_sizes), *popt_binary), 'r--', 
         label='Fit: y = {:.2e} log(x) + {:.2e}'.format(*popt_binary))
plt.legend()

plt.tight_layout()
plt.show()


# 1. Linear Search:
#    - The plot shows that linear search time increases roughly linearly with the vector size,
#      which is consistent with O(n) complexity.
#    - The fitted function is y = a*x + b, where:
#         • 'a' represents the incremental time per element,
#         • 'b' represents the fixed overhead (e.g., loop and function call overhead).
#
# 2. Binary Search:
#    - The binary search plot appears nearly flat. This is because binary search is very fast
#      for these vector sizes, and the measured time is dominated by overhead (the lambda call,
#      random element selection, etc.).
#    - The fitted function is y = a*log(x) + b, which reflects the theoretical O(log n) behavior.
#      However, because the actual execution time is so small, the parameters 'a' and 'b' are not
#      as meaningful; the overhead masks the logarithmic scaling.
#
#
# Threfore , the results are as expected
#    - Linear search shows linear scaling (O(n)) with increasing vector size.
#    - Binary search theoretically scales as O(log n), but its extremely small execution time
#      means that the overhead of the timing mechanism obscures the expected trend in this experiment.