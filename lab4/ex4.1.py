
def processData(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2
# Best Case Complexity is O(n): If the list contains no elements greater than 5, it would run n times and then be complete without running inner loop.
# Worst Case Complexity is O(n^2): If the list elements are all greater than 5, outer loops runs n times and the inner loop runs n times.
# Average Case Complexity is 0(n^2): If the list contains a mix of elements, greater and lower than 5, the average case complexity would end up being O(n^2)

# Worst and Average Case Complexity are the same, but not best case. 
# Below is a function where best, worst, and average are the same. (O(n) complexity)
def processData2(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= (2 ** len(li))

