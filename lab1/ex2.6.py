import math
import timeit

def its_just_a_bit_shift(n):
    return 1<<n
def its_just_a_bit_shift_in_a_loop(n):
    pow2 = 1
    for i in range(n):
        pow2 = pow2<<1
    return pow2
def its_just_a_bit_shift_in_list_comp(n):
    pow2  = [1<<i+1 for i in range(n)]
    return pow2

n = 10000
execution_count=10000
execution_time = timeit.timeit(lambda:its_just_a_bit_shift(n))
print(execution_time/execution_count)
n2 = 1000
execution_count2 = 1000
execution_time = timeit.timeit(lambda: its_just_a_bit_shift_in_a_loop(n2),number= execution_count2)
print(execution_time/execution_count2)
execution_time = timeit.timeit(lambda: its_just_a_bit_shift_in_list_comp(n2),number= execution_count2)
print(execution_time/execution_count2)