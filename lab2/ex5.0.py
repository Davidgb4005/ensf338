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

def binary_search(my_array,search_value):
    if len(my_array)<= 0:
        print("Does not exist in array")
        return
    split_point = len(my_array)//2
    split_value = my_array[split_point]
    if split_value > search_value:
        binary_search(my_array[0:split_point],search_value)
    elif split_value < search_value:
        binary_search(my_array[split_point+1:len(my_array)],search_value)
    else:
        pass
        #print(search_value," Was Found At ",my_array[split_point])

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

ThreadIt = False 
if ThreadIt:
    b_search_thread = threading.Thread(target= b_search_timeit)
    l_search_thread = threading.Thread(target= l_search_timeit)
    b_search_thread.start()
    l_search_thread.start()
    b_search_thread.join()
    l_search_thread.join()
else:
    b_search_timeit()
    l_search_timeit()

linear_search_array_avg = []
binary_search_array_avg = []
linear_search_values = []
binary_search_values = []
element_count_values = []
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

#print(element_count_values)
avg = 0
for k in linear_search_array_outer:
    for i in k:
        avg =+ i
        linear_search_values.append(i)
    linear_search_array_avg.append(avg)    
    #print("Lin search avg: ",avg)
    avg = 0


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