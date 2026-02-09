# Question 1: A profiler is a method in python that is used to record a set of statistics used to determine 
# individual time measurements for varies parts of a program and how often they are executed.

# Question 2: The difference between profiling and benchmarking is that profiling is the process of determining
# how often and how long different componetents of the program are executed, whereas benchmarking
# only records the total time the entire program takes to execute fully with the timeit module.

# Question 3: 

import timeit
import cProfile
import re

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
        return data

def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

def main():
    test_function()
    third_function()

# ensures cProfile only measures the execution time of main and not the defining the functions
cProfile.run('main()')

# Question 4
# 
# using the output data from cProfile.run('main()'):
# 
# 8 function calls in 5.797 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.797    5.797 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 ex3.py:14(sub_function)
#         1    0.000    0.000    0.000    0.000 ex3.py:21(test_function)
#         1    4.976    4.976    4.976    4.976 ex3.py:27(third_function)
#         1    0.821    0.821    5.797    5.797 ex3.py:31(main)
#         1    0.000    0.000    5.797    5.797 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# The total execution time of main was 5.797 seconds, and based on the output, we can see that the 
# majority of the execution time comes from third_function, which took 4.976 seconds and was only called 
# once when looking at its seconds-per-call ratio. main took a small 0.821 seconds as per the tottime 
# (total time), but we can see it was executed last when looking at the cumtime (cumulative time) of 5.797 seconds.
# All the other functions took negligible amounts of time and have values of zero in tottime.