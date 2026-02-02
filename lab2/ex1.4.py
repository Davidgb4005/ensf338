#QUESITONS
#1 - Fib sequnce x_n = x_n-1+x_n-2
#2 - no as we never split the input set and we indivually 
#       compute every value from the entire set before it for each element
#3 - time complex O(2^n)
#4 - time complex O(n) you only calculate n-(k-1) and n-(k-2) once to find n(k)
import timeit
from matplotlib import pyplot as plt
my_array = [0,0]

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def fib(my_array,len):
    print(len)
    if len <= 1:
        my_array = [0,1]
        return my_array
    my_array = fib(my_array,len - 1)
    n1 = my_array[0]
    my_array = [my_array[1],my_array[1]+n1]
    return my_array
    


my_array = fib(my_array,10)
print(my_array)
execution_time = [[],[]]
execution_count = 1
execution_number = 35
x_axis = []
for k in range(execution_number):
    x_axis.append(k)
    execution_time[0].append(timeit.timeit(lambda:func(k),number=execution_count))
for k in range(execution_number):
    execution_time[1].append(timeit.timeit(lambda:fib(my_array,k),number= execution_count))


for j in range(execution_number):
    print(execution_time[0][j],"  ",execution_time[1][k])

plt.plot(x_axis,execution_time[0])
plt.savefig("lab2/ex1.6.2.png")
plt.show()
plt.plot(x_axis,execution_time[1])
plt.savefig("lab2/ex1.6.1.png")
plt.show()