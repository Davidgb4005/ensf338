import sys
sys.setrecursionlimit(10000)

def inefficientSearch(arr, item): #Sequential search
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1
# Worst case complexity is O(n), since it looks through each element of the sorted array one by one.
        

def efficientSearch(arr, left, right, item): #Binary search, initially left starts at 0, right is len of array -1.
    if right >= left:
        mid = (right+left)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            return efficientSearch(arr, mid+1, right, item)
        else:
            return efficientSearch(arr, left, mid-1, item)
    else: 
        return -1
# Worst case complexity is O(logn) since the amount of elements being looked at gets divided in half each time recursive function call