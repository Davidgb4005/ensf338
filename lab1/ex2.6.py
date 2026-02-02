import math
import timeit

def pow2(n):
    return 1<<n
def pow2_for_loop(n):
    pow2 = 1
    for i in range(n):
        pow2 = pow2<<1
    return pow2
def pow2_list_comp(n):
    pow2  = [1<<i+1 for i in range(n)]
    return pow2



#Timit Code
n = 10000
execution_count=10000
execution_time = timeit.timeit(lambda:pow2(n))
print(execution_time/execution_count)
n2 = 1000
execution_count2 = 1000
execution_time = timeit.timeit(lambda: pow2_for_loop(n2), number= execution_count2)
print(execution_time/execution_count2)
execution_time = timeit.timeit(lambda: pow2_list_comp(n2), number= execution_count2)
print(execution_time/execution_count2)