import random as rd
import math

def build_array(n):
    my_array=[]
    for i in range(n):
        my_array.append(rd.randint(0,n**3))
    my_array.sort()
    return my_array

def linear_search(my_array,search_value):

    for i in my_array:
        if i == search_value:
            print("Found ",search_value)
            return
    print("Does Not Exist")

def binary_search(my_array,search_value):

    if len(my_array)<= 0:
        print("Does not exist in array")
        return
    if my_array[math.floor(len(my_array)/2)] > search_value:
        binary_search(my_array[0:math.floor(len(my_array)/2)],search_value)
    elif my_array[math.floor(len(my_array)/2)] < search_value:
        binary_search(my_array[math.floor(len(my_array)/2+1):len(my_array)],search_value)
    else:
        print("Found ",my_array[math.floor(len(my_array)/2)])




my_array = build_array(100)
search_value = my_array[rd.randint(0,len(my_array))]
print(search_value)
linear_search(my_array,search_value)
binary_search(my_array,search_value)