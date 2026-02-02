import numpy as np 
from matplotlib import pyplot as plt
import random as rd
import math
import timeit
import threading
binary_search_array_outer = []
linear_search_array_outer = []


def build_array(n):
    my_array=[]
    for i in range(n):
        my_array.append(rd.randint(0,n))
    my_array.sort()
    return my_array

def linear_search(my_array,search_value):

    for i in my_array:
        if i == search_value:
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
        binary_search(my_array[0:split_point-1],search_value)
    elif split_value < search_value:
        binary_search(my_array[split_point+1:len(my_array)-1],search_value)
    else:
        pass
        #print("Found ",my_array[math.floor(len(my_array)/2)])

def b_search_timeit():
    binary_search_array = []
    global binary_search_array_outer
    binary_search_array_outer = []
    element_count = [1000,2000,8000,16000,32000]
    execution_count = 100;
    execution_amount = 1000;
    for k in range(len(element_count)):
        my_array = build_array(element_count[k])
        print("b search at: ",k)
        for i in range(execution_amount):
            search_value = my_array[rd.randint(0,len(my_array))-1]
            binary_search_array.append(timeit.timeit(lambda:binary_search(my_array,search_value),number= execution_count)/execution_count)
        binary_search_array_outer.append(binary_search_array)
        binary_search_array = []
    return binary_search_array_outer

def l_search_timeit():
    linear_search_array = []
    global linear_search_array_outer
    linear_search_array_outer = []
    element_count = [1000,2000,8000,16000,32000]
    execution_count = 100;
    execution_amount = 1000;
    for k in range(len(element_count)):
        print("L search at: ",k)
        my_array = build_array(element_count[k])
        for i in range(execution_amount):
            search_value = my_array[rd.randint(0,len(my_array))-1]
            linear_search_array.append(timeit.timeit(lambda:linear_search(my_array,search_value),number= execution_count)/execution_count)
        linear_search_array_outer.append(linear_search_array)
        linear_search_array = []
    return linear_search_array_outer



b_search_thread = threading.Thread(target= b_search_timeit)
l_search_thread = threading.Thread(target= l_search_timeit)


b_search_thread.start()
l_search_thread.start()

b_search_thread.join()
l_search_thread.join()


linear_search_array_avg = []
binary_search_array_avg = []
element_count = [1000,2000,8000,16000,32000]
avg = 0
for k in binary_search_array_outer:
    for i in k:
        avg =+ i;
    binary_search_array_avg.append(avg)
    print("B search avg: ",avg)
    avg = 0
avg = 0
for k in linear_search_array_outer:
    for i in k:
        avg =+ i;
    linear_search_array_avg.append(avg)    
    print("Lin search avg: ",avg)
    avg = 0




plt.rcParams['figure.figsize'] = [10, 5]

slope1, intercept1 = np.polyfit(element_count, linear_search_array_avg, 1)
slope2, intercept2 = np.polyfit(element_count, binary_search_array_avg, 1)
plt.scatter(element_count,linear_search_array_avg)
plt.scatter(element_count,binary_search_array_avg)
linevalues1 = [slope1 * x + intercept1 for x in element_count]
linevalues2 = [slope2 * x + intercept2 for x in element_count]
plt.plot(element_count, linevalues1, 'r')
plt.plot(element_count, linevalues2, 'r')
plt.show()
# Finally, print out the linear relationship between input length and time.
print("The linear model is: t = %.2e * n + %.2e" % (slope1, intercept1))
print("The linear model is: t = %.2e * n + %.2e" % (slope2, intercept2))