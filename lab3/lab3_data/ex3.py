import random

# Question 2
def bubble_sort(arr):
    swaps = comps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comps +=1
            if arr[j] > arr[j+1]:
                swaps +=1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return comps, swaps

# Question 3

def test_bubble_sort(input_sizes):
    for size in input_sizes:
        array = random.sample(range(1, size*10), size)
        comps, swaps = bubble_sort(array)
        list_comps.append(comps)
        list_swaps.append(swaps)
        print(f'Array Size = {size}, Comparisons = {comps}, Swaps = {swaps}')

input_sizes = [10, 50, 100, 200, 400, 800, 1000]

list_comps = []
list_swaps = []
test_bubble_sort(input_sizes)

# Question 4 (Commented out since slide said separately)
"""
import matplotlib.pyplot as plt
import numpy as np

sizes = np.array(input_sizes)
comparisons = np.array(list_comps)
swaps = np.array(list_swaps)

plt.subplot(1, 2, 1)
plt.plot(sizes, comparisons, color='orange')
plt.title('Number of Comparisons vs. Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Comparisons')
plt.ylim(0, 500000)
plt.grid(True)

# Plot swaps with interpolation
plt.subplot(1, 2, 2)
plt.plot(sizes, swaps, color='blue')
plt.title('Number of Swaps vs. Input Size')
plt.xlabel('Input Size')
plt.ylim(0, 500000)
plt.ylabel('Number of Swaps')
plt.grid(True)

plt.tight_layout()
plt.show()
"""
