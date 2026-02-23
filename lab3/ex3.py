import numpy as np
import matplotlib.pyplot as plt
import random as rd

def build_array(n):
    return [rd.randint(0, n) for test in range(n)]

def bubble_sort(arr):
    comps = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comps, swaps

def timer_fn(max_size):
    bubble_sort_comps = []
    bubble_sort_swaps = []

    array_sizes = np.linspace(10, max_size, 20).astype(int)

    for size in array_sizes:
        comp_array = []
        swap_array = []

        for _ in range(10):  
            my_array = build_array(size)
            comps, swaps = bubble_sort(my_array)
            comp_array.append(comps)
            swap_array.append(swaps)

        bubble_sort_comps.append(np.mean(comp_array))
        bubble_sort_swaps.append(np.mean(swap_array))

    plt.scatter(array_sizes, bubble_sort_comps, color="red", label="Comparisons")
    plt.scatter(array_sizes, bubble_sort_swaps, color="blue", label="Swaps")

    coeffs_comps = np.polyfit(array_sizes, bubble_sort_comps, 2)
    x_smooth = np.linspace(min(array_sizes), max(array_sizes), 200)
    y_comps_smooth = np.polyval(coeffs_comps, x_smooth)
    plt.plot(x_smooth, y_comps_smooth, color="red", linestyle="--",
             label=f"Comparisons fit: {coeffs_comps[0]:.3e}x² + {coeffs_comps[1]:.3e}x + {coeffs_comps[2]:.3e}")

    coeffs_swaps = np.polyfit(array_sizes, bubble_sort_swaps, 2)
    y_swaps_smooth = np.polyval(coeffs_swaps, x_smooth)
    plt.plot(x_smooth, y_swaps_smooth, color="blue", linestyle="--",
             label=f"Swaps fit: {coeffs_swaps[0]:.3e}x² + {coeffs_swaps[1]:.3e}x + {coeffs_swaps[2]:.3e}")

    print(comp_array)
    print(swap_array)
    plt.xlabel("Array Size")
    plt.ylabel("Count")
    plt.title("Bubble Sort Comparisons and Swaps")
    plt.legend()
    plt.show()

timer_fn(2000)