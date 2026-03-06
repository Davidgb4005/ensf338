import numpy as np
import timeit
import matplotlib.pyplot as plt
import random

#Implement both algorithms
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 

def quicksort(arr, low, high):
    if low < high: 
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

def binary_search(arr, key, first, last):
    if (first <= last):
        mid = (first + last) // 2  
        if arr[mid] == key:
            return mid      
        elif key < arr[mid]:
            return binary_search(arr, key, first, mid - 1) 
        else:
            return binary_search(arr, key, mid + 1, last)
    return -1

def quicksort_binary_search(arr, key, size):
    first = 0
    last = size - 1
    quicksort(arr, first, last)
    binary_search(arr, key, first, last)

def create_array(size):
    arr = np.random.randint(1, size, size=size)  
    return arr

def time_linear_search(arr, tasks=100, key=30): 
    times = []
    for i in range(tasks):
        random.shuffle(arr) 
        time = timeit.timeit(lambda: linear_search(arr, key), number=10)
        times.append(time / 10)
    avg = sum(times) / len(times)
    print(f"Linear Search time for {len(arr)}: {avg}")
    return avg   

def time_quicksort_binary_search(arr, size, tasks=100, key=30): 
    times = []
    for i in range(tasks):
        random.shuffle(arr) 
        time = timeit.timeit(lambda: quicksort_binary_search(arr, key, size), number=1)
        times.append(time / 1)
    avg = sum(times) / len(times)
    print(f"Quicksort then Binary Search time for {len(arr)}: {avg}")
    return avg

def create_reverse_sorted_array(size):
    arr = np.random.randint(1, size, size=size)
    arr = sorted(arr) 
    reversed_arr = np.flip(arr) 
    return reversed_arr

#Run Preformance on first 100 random task
arr = create_array(1000)
time_linear_search(arr)
time_quicksort_binary_search(arr, 1000)

#Redo on the Following array
sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
sizes = np.array(sizes)

linear_times = []
quick_binary_times = []

print("\n\nrunning tests: ")
for size in sizes:
    arr_0 = create_reverse_sorted_array(size)
    arr_1 = arr_0.copy()
    linear_times.append(time_linear_search(arr_0))
    quick_binary_times.append(time_quicksort_binary_search(arr_1, size=size))

#Graph
plt.figure(figsize=(10, 5))
plt.scatter(sizes, linear_times, color='red', label='Linear Search')
plt.scatter(sizes, quick_binary_times, color='blue', label=' Quicksort Binary Search')

plt.xlabel('Array Size')
plt.ylabel('Time')
plt.title('Linear Search vs. Quicksort Binary Search')
plt.legend()
plt.grid(True)
plt.savefig('output.6_worst.png')


# Liner search is faster because of the fact that we have to first sort then we can search when using the
# second algorithm thus causing the time complexity to rise way more than a simple linear search
