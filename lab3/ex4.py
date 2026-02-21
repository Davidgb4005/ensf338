import numpy as np
from matplotlib import pyplot as plt
import timeit
import random as rd
import sys
np.set_printoptions(threshold=np.inf)
sys.setrecursionlimit(50000)

#Optimised Quick Sort
def quicks_sort_optimize(my_array):
    size = len(my_array)
    if size < 2:
        return
    j = size-1
    i = 0
    pivot = my_array[size//2]
    pre_sort = 0
    pre_sort_left = 0
    pre_sort_right = 0
    while j > i:
        while my_array[i] < pivot:
            if my_array[i] < my_array[i+1]:
                pre_sort_left = pre_sort_left + 1
            else:
                pre_sort_left = 0
            i = i + 1
        while my_array[j] > pivot:
            if my_array[j-1] < my_array[j]:
                pre_sort_right = pre_sort_right + 1
            else:
                pre_sort_right = 0
            j = j - 1
        if j > i:
            my_array_i = my_array[i]
            while my_array[j] == my_array_i and j > i:
                j = j - 1 
                pre_sort = pre_sort + 1
            if my_array[j]<my_array[i]:
                pre_sort_right = 0
                pre_sort_left = 0
            tmp = my_array[j]
            my_array[j] = my_array_i 
            my_array[i] = tmp
    if pre_sort > size-1:
        #print("Pre Sorted Length: ",size-1," ", my_array)
        return
    if pre_sort_left < size -1:
        quicks_sort_optimize(my_array[:i])
    else:
        pass
        #print("LHS Already Sorted :", i ," ",my_array[:i])
    if pre_sort_right < size - (i+1):
        quicks_sort_optimize(my_array[i+1:])
    else:
        pass
        #print("RHS Already Sorted :", i ," ",my_array[i+1:])


#Base Quick Sort
def quicks_sort(my_array):
    size = len(my_array)
    if size < 2:
        return
    j = size-1
    i = 0
    pivot = my_array[size//2]
    while j > i:
        while my_array[i] < pivot:
            i = i + 1
        while my_array[j] > pivot:
            j = j - 1
        if j > i:
            if my_array[j] == my_array[i] and j > i:
                j = j - 1 
            tmp = my_array[j]
            my_array[j] = my_array[i]
            my_array[i] = tmp
    quicks_sort(my_array[:i])
    quicks_sort(my_array[i+1:])
    
if False:
    for i in range(1000):
        dummy_array = []
        for i in range(1000):
            dummy_array.append(rd.randint(0,10000000))
        dummy_np_array = np.array(dummy_array)
        dummy_array_2 = dummy_np_array.copy()
        quicks_sort_optimize(dummy_array_2)
        print(np.equal(np.sort(dummy_np_array),dummy_array_2).all())
    exit()
#######################################
##ALL TESTING/PLOTTING CODE PAST HERE##
######################################

set_size = (400,800,1200,1600,2000,2500,3000)
set_span = (0,1,2,3,4,10,1000000)

optimized_array_2d = []
unoptimized_array_2d = []

for span_idx, span in enumerate(set_span):
    optimized_times = []
    unoptimized_times = []

    for size in set_size:
        dummy_array = [rd.randint(0, span) for test in range(size)]
        my_array = np.array(dummy_array)

        optimized_times.append(timeit.timeit(lambda: quicks_sort_optimize(my_array.copy()), number=10)/10)
        unoptimized_times.append(timeit.timeit(lambda: quicks_sort(my_array.copy()), number=10)/10)
        print(size ," SIZE DONE")
    optimized_array_2d.append(optimized_times)
    unoptimized_array_2d.append(unoptimized_times)
    print(span," SPAN DONE")
fig, axs = plt.subplots(1, 2, figsize=(14,5))


for i, span in enumerate(set_span):
    axs[0].scatter(set_size,optimized_array_2d[i], label=f"Span={span}")

axs[0].set_ylabel("Time (s)")
axs[0].set_xlabel("Set size")
axs[0].set_title("Optimized Quicksort")
#axs[0].set_xlim(x_min, x_max)
#axs[0].set_ylim(y_min, y_max)
axs[0].legend()

coeffs = np.polyfit(set_size, unoptimized_array_2d[0], 2)
x_smooth = np.linspace(min(set_size), max(set_size), 200)
y_smooth = np.polyval(coeffs, x_smooth)
eqn_ins = f"{coeffs[0]:.1e}x² + {coeffs[1]:.1e}x + {coeffs[2]:.1e}"
axs[1].plot(x_smooth, y_smooth, color='blue',label=f"Insertion Sort Fit: {eqn_ins}")
for i, span in enumerate(set_span):
    axs[1].scatter(set_size, unoptimized_array_2d[i], label=f"Span={span}")

axs[1].set_ylabel("Time (s)")
axs[1].set_xlabel("Set size")
axs[1].set_title("Unoptimized Quicksort")
#axs[1].set_xlim(x_min, x_max)
#axs[1].set_ylim(y_min, y_max)
axs[1].legend()

plt.show()


set_size = (100,500,1000,1500,3000,4000,5000,6000)
set_span = (0,1,2,4,8,16,32,100000)

optimized_array_2d = []

for span_idx, span in enumerate(set_span):
    optimized_times = []

    for size in set_size:
        dummy_array = [rd.randint(0, max(1, span)) for test in range(size)]
        my_array = np.array(dummy_array)

        t = timeit.timeit(lambda: quicks_sort_optimize(my_array.copy()), number=10)/10
        optimized_times.append(t)
        print(size ,"SIZE DONE")

    optimized_array_2d.append(optimized_times)
    print(span,"SPAN DONE")

# Plot
fig, axs = plt.subplots(1, 1, figsize=(10,6))

for i, span in enumerate(set_span):
    axs.scatter(set_size, optimized_array_2d[i], label=f"Span={span}")

axs.set_xlabel("Set size")
axs.set_ylabel("Time (s)")
axs.set_title("Optimized Quicksort Timing")
axs.legend()
plt.show()