1. Explain the difference between an array size and capacity

The size of an array is the number of elements currently stored in the array. The capacity is the total number of elements that the array can store before it needs to allocate more memory. Size is always less than or equal to capacity. For example, an array may have a capacity of 8 but only store 3 elements, meaning the size is 3 and there are 5 unused positions.1) Array Size is number of elements -1 and capacity is current memory allocated but not initilized

2. What happens when an array needs to grow beyond its current capacity? Explain and produce a diagram showing the memory layout before and after expansion

When an array reaches its capacity and another element is inserted, the program must increase the amount of memory allocated for the array. This usually involves allocating a larger block of memory and copying the existing elements to the new location.

2.1 Case 1: There is free space in memory after the array
If there is unused memory immediately after the array, the system may extend the array in place without moving it.

2.2 Case 2: Memory after the array is occupied
If another variable occupies the memory immediately after the array, the array cannot grow in place. A new larger block of memory must be allocated elsewhere. The elements from the old array are copied into the new block, and the old memory is released


3. Techniques real-world implementations use to amortize the cost of array expansion

Most real-world dynamic arrays increase their capacity by a multiplicative growth factor, usually doubling the capacity each time expansion occurs.
By doubling the capacity, expansions occur less frequently. Although copying elements during expansion is expensive, the cost is spread across many insert operations, giving an amortized insertion cost of O(1)