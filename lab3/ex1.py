import sys
sys.setrecursionlimit(20000)
merges = 0
splits = 0
def merge_sort(arr, low, high):
    global splits
    if len(arr[low:high])>1:
        splits += 1
    if low < high:
        mid = (low + high) // 2
        if (len(arr[low:mid+1]) > 1 and len(arr[mid+1:high+1]))>1:
            print("Left Array: ",arr[low:mid+1], " - Right Array: ",arr[mid+1:high+1])
        elif (len(arr[mid+1:high+1]))>1:
            print("Left Array: []", " - Right Array: ",arr[mid+1:high+1])
        elif (len(arr[low:mid+1]) > 1):
            print("Left Array: ",arr[low:mid+1]," - Right Array: []")
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
        print(f"After merging indices {low}-{mid} and {mid+1}-{high}: {arr}")

def merge(arr, low, mid, high):
    global merges
    merges += 1
    size1 = mid - low + 1
    size2 = high - mid
    tempA = [0] * size1
    tempB = [0] * size2
    for i in range(size1):
        tempA[i] = arr[low + i]
    for j in range(size2):
        tempB[j] = arr[mid + 1 + j]
    
    i = j = 0
    index = low
    while i < size1 and j < size2:
        if tempA[i] <= tempB[j]:
            arr[index] = tempA[i]
            i += 1
        else:
            arr[index] = tempB[j]
            j += 1
        index += 1
    
    while i < size1:
        arr[index] = tempA[i]
        i += 1
        index += 1
    while j < size2:
        arr[index] = tempB[j]
        j += 1
        index += 1

array = [8, 42, 25, 3, 3, 2, 27, 3]
print("Original array:", array)
merge_sort(array, 0, len(array) - 1)
print("Sorted array:", array)
print("Splits: ",splits," - Merges: " ,merges)