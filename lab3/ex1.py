import sys
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    #idea/steps: create two temporary arrays. 
    #each array should be the size of the two subarrays to be merged. 
    #then compare the values of the two temp arrays by iterating through range of the two arrays.
    #prob some way to optimize this using list comprehension but idk how i'll figure it out later
    size1 = mid - low + 1 #the +1 is added or else tempA straight up won't take values when size1 is 0
    size2 = high - mid
    tempA = [0] * size1 #can't make it empty list like [] or else an error comes up
    tempB = [0] * size2
    index = low
    for i in range(size1):
        tempA[i] = arr[low+i]
    for j in range(size2):
        tempB[j] = arr[mid+j+1] #added +1 or else tempB might end up the same as tempA
    i = 0
    j = 0
    while i < size1 and j < size2: #looks through values of the two arrays, then compares
        if tempA[i] <= tempB[j]:
            arr[index] = tempA[i]
            i +=1
        else:
            arr[index] = tempB[j]
            j += 1
        index += 1
    # list ain't merging properly (2nd half would just be a repeat of mid index value)
    # add following two loops to make sure all values are properly added and don't get truncated
    while i < size1:
        arr[index] = tempA[i]
        i += 1
        index += 1
    while j < size2:
        arr[index] = tempB[j]
        j += 1
        index += 1
    # at this point, array merges but isn't sorted properly?
    # fixed, just a bunch of random issues with list indexes. now fully functional!


array = [8,42,25,3,3,2,27,3]
#practice_array = [5,3,2,8,1]
#merge_sort(practice_array, 0, len(practice_array))
#print(practice_array)
merge_sort(array, 0, len(array)-1) #add -1 or else IndexError will occur
print(array)