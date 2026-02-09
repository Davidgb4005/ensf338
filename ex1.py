import random as rnd

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr, low, mid, high):
    # Create left and right subarrays
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]

    i = j = 0
    k = low

    # Merge both halves into original array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any elements from left array that were missed
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any elements from right array that were missed
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


x = [rnd.randint(1, 100) for _ in range(10)]

print(f'Original array : {x}')
print(f'Sorted array   : {merge_sort(x, 0, len(x)-1)}')

