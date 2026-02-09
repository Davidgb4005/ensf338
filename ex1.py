import timeit
import matplotlib.pyplot as plt


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
# 1.The following code takes an input integer of n and then checks to see
#   if the value is ethier 0 or 1 if not it creates subproblems where it adds the
#   values of n-1 and n-2 after going throught the function again so it will continue
#   to create subproblems until the numbers are broken down to 1 or 0, at which point
#   all those values will be summed together

# 2.Yes, the previous code is an example of a "Divide and Conquer" algoritm.
#   The problem is divided into many differnt subproblems take for example if n = 5,
#   we break that down into 4 and 3 and check those against the if statment if not
#   divide them into new subproblems. Once the problems are divided suffecintly
#   enough the problems are conquered in a straight forward fashion of adding 0s and
#   1s and as explained previously this is done in a recursive manner

# 3. O(2^n)

# 4.
def memo(n, memo_dict={}):
    if n == 0 or n == 1:
        return n
    if n in memo_dict:
        return memo_dict[n]
    else:
        memo_dict[n] = memo(n-1, memo_dict) + memo(n-2, memo_dict)
    return memo_dict[n]

# 5. O(n)

# 6. 

times_func = []
values_func = []

for i in range(35):
    time_taken = timeit.timeit(lambda: func(i), number=10)/10
    times_func.append(time_taken)
    values_func.append(i)

plt.figure(figsize=(10, 5))
plt.scatter(values_func, times_func, color='blue', label="Measured times")
plt.xlabel("Value of the Function")
plt.ylabel("Time to Excute")
plt.title("Time to Excute vs Value of the Function")
plt.grid(True)
plt.savefig("ex1.6.1.jpg")
plt.show()
plt.close()

times_memo = []
values_memo = []

for j in range(35):
    memo_dc = {}
    time_taken = timeit.timeit(lambda: memo(j, memo_dc), number=10)/10
    times_memo.append(time_taken)
    values_memo.append(j)

plt.figure(figsize=(10, 5))
plt.scatter(values_memo, times_memo, color='red', label="Measured times")
plt.xlabel("Value of the Memoization")
plt.ylabel("Time to Excute")
plt.title("Time to Excute vs Value of the Memoization")
plt.grid(True)
plt.savefig("ex1.6.2.jpg")
plt.show()
plt.close()
