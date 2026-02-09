import numpy as np 
from matplotlib import pyplot as plt
import random as rd
import math
import timeit
import threading
from scipy import optimize as op
binary_search_array_outer = []
linear_search_array_outer = []
execution_count = 100 #100 timit number
execution_amount = 1000 #1000 For loop
element_count = [1000,2000,8000,16000,32000]

"""1. Implement linear search and binary search
Linear search was implemented by iterating through each element in the sorted array until the target value was found. Binary search was implemented recursively by repeatedly dividing the array in half, comparing the middle element to the target, and continuing the search in the appropriate half until the value was found or the subarray was empty.

2. Measure the performance of each on sorted vectors
For each array size (1000, 2000, 4000, 8000, 16000, 32000 elements), a random element was selected 1000 times. The time to find the element was measured using timeit with 100 iterations per measurement. The average runtime for each search method was computed across all measurements. This process allows comparison of the performance of linear and binary search as the array size increases.

3. Interpolate the data points

Linear search data was fitted with a linear function 
t(n)=mn+c
t(n)=mn+c, reflecting its expected 
O(n)
O(n) time complexity.

Binary search data was fitted with a logarithmic function 
t(n)=aln⁡(bn)+c
t(n)=aln(bn)+c, reflecting its expected 
O(log⁡n)
O(logn) complexity.
Curve fitting was performed using scipy.optimize.curve_fit(). The fits provide a visual and quantitative confirmation of the theoretical complexity of each algorithm.

4. Discuss the results
Linear Search: The interpolating function is linear, with slope m representing the time added per additional element and intercept c representing fixed overhead. Runtime increases proportionally with array size, matching expectations.
Binary Search: The interpolating function is logarithmic, with parameters a (scales the growth of log(n)), b (horizontal scaling), and c (constant overhead). Runtime grows slowly as array size increases, consistent with 
O(log⁡n)
O(logn) complexity. The results match theoretical expectations, although small overheads from recursion."""

def build_array(n):
    my_array = np.empty(n)
    #my_array = []
    for i in range(n):
        #my_array.append(0)
        my_array[i] = (rd.randint(0,n))
    my_array.sort()
    return my_array

def linear_search(my_array,search_value):

    for i in range(len(my_array)):
        if my_array[i] == search_value:
            #print("Found ",search_value)
            return
    print("Does Not Exist")

def binary_search(my_array, search_value, low=0, high=None):
    if high is None:
        high = len(my_array) - 1

    if low > high:
        return None

    mid = (low + high) // 2

    if my_array[mid] > search_value:
        return binary_search(my_array, search_value, low, mid - 1)
    elif my_array[mid] < search_value:
        return binary_search(my_array, search_value, mid + 1, high)
    else:
        return mid

def b_search_timeit():
    binary_search_array = []
    global binary_search_array_outer
    binary_search_array_outer = []
    global element_count
    global execution_count
    global execution_amount
    for k in range(len(element_count)):
        my_array = build_array(element_count[k])
        print("b search at: ",k)
        for i in range(execution_amount):
            search_value = my_array[rd.randint(0,len(my_array))-1]
            binary_search_array.append(timeit.timeit(lambda:binary_search(my_array,search_value),number= execution_count)/execution_count)
        binary_search_array_outer.append(binary_search_array)
        binary_search_array = []
    print("B search Done")

def l_search_timeit():
    linear_search_array = []
    global linear_search_array_outer
    linear_search_array_outer = []
    global element_count
    global execution_count
    global execution_amount
    for k in range(len(element_count)):
        print("L search at: ",k)
        my_array = build_array(element_count[k])
        for i in range(execution_amount):
            search_value = my_array[rd.randint(0,len(my_array))-1]
            linear_search_array.append(timeit.timeit(lambda:linear_search(my_array,search_value),number= execution_count)/execution_count)
        linear_search_array_outer.append(linear_search_array)
        linear_search_array = []
    print("l search done")
"""
ThreadIt = False 
if ThreadIt:
    b_search_thread = threading.Thread(target= b_search_timeit)
    l_search_thread = threading.Thread(target= l_search_timeit)
    b_search_thread.start()
    l_search_thread.start()
    b_search_thread.join()
    l_search_thread.join()
"""
b_search_timeit()
l_search_timeit()

linear_search_array_avg = []
binary_search_array_avg = []
linear_search_values = []
binary_search_values = []
element_count_values = []

#Binary Serach
avg = 0
for k in range(len(binary_search_array_outer)):
    for i in binary_search_array_outer[k]:
        avg =+ i;
        binary_search_values.append(i)
        element_count_values.append(element_count[k])
        #print(element_count[k])
    binary_search_array_avg.append(avg)
    #print("B search avg: ",avg)
    avg = 0

#Linear Search
avg = 0
for k in linear_search_array_outer:
    for i in k:
        avg =+ i
        linear_search_values.append(i)
    linear_search_array_avg.append(avg)    
    #print("Lin search avg: ",avg)
    avg = 0

#Graphing And Curve Fitting
p0 = [2,0, 0] 
plt.rcParams['figure.figsize'] = [10, 5]
ln = lambda x,a,b,c:(a * np.log(b * x) + c)
popt, pcov = op.curve_fit(
    ln,
    element_count_values,
    binary_search_values,
    p0=p0,
    bounds=([-np.inf, 0, -np.inf], [np.inf, np.inf, np.inf])
)
xfit = np.linspace(
    np.min(element_count_values),
    np.max(element_count_values),
    200
)
yfit = ln(xfit, *popt)

plt.scatter(element_count_values, binary_search_values, label="Data")
plt.plot(xfit, yfit, color="red", label="Log fit")
plt.legend()
plt.show()
popt, pcov = op.curve_fit(
    ln,
    element_count,
    binary_search_array_avg,
    p0=p0,
    bounds=([-np.inf, 0, -np.inf], [np.inf, np.inf, np.inf])
)
xfit = np.linspace(
    np.min(element_count),
    np.max(element_count),
    200
)
yfit = ln(xfit, *popt)
plt.scatter(element_count, binary_search_array_avg, label="Data")
plt.plot(xfit, yfit, color="red", label="Log fit")
plt.legend()
plt.show()

slope1, intercept1 = np.polyfit(element_count_values, linear_search_values, 1)
slope2, intercept2 = np.polyfit(element_count_values, binary_search_values, 1)
plt.scatter(element_count_values,linear_search_values, label="Linear Search")
plt.scatter(element_count_values,binary_search_values, label="Binary Search")
linevalues1 = [slope1 * x + intercept1 for x in element_count_values]
linevalues2 = [slope2 * x + intercept2 for x in element_count_values]
plt.plot(element_count_values, linevalues1, 'r', label="Linear Search")
plt.plot(element_count_values, linevalues2, 'b',label="Binary Search")
plt.legend()
plt.show()
# Finally, print out the linear relationship between input length and time.
print("The linear model is: t = %.2e * n + %.2e" % (slope1, intercept1))
print("The linear model is: t = %.2e * n + %.2e" % (slope2, intercept2))
