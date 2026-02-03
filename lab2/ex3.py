import timeit
import cProfile as cp
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

profiler = cp.Profile()
profiler.enable()
test_function()
third_function()
profiler.disable()
profiler.print_stats(sort="tottime")

"""
Question 1: What is a profiler, and what does it do?
A profiler measures aspects of program execution, 
such as the time spent in each function, the number of calls to functions, 
and memory usage. It identifys performance bottlenecks in code.

Question 2: How does profiling differ from benchmarking?
Benchmarking measures the total time it takes for a program or function 
to execute, typically for performance comparison. Profiling, on the other hand, 
provides detailed insights about **which parts** of the program consume time 
or resources, function by function.


   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    9.060    9.060    9.060    9.060 ex3.py:16(third_function)
    55/10    0.000    0.000    0.000    0.000 ex3.py:5(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:11(test_function)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

    a large majority was spent in "third_function" Which makes sens as it had to go through 10000000
    iterations as opposed to sub 100 for the others even with significantly more calls on sub function
    
"""