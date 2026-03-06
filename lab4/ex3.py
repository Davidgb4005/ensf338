# Q1
# Python lists grow using the resizing strategy implemented in list_resize().
# The key line in the code is:
#
# new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
#
# Explanation:
# - (newsize >> 3) adds approximately newsize / 8 extra space.
# - +6 adds a small constant padding.
# - & ~(size_t)3 rounds the allocation down to a multiple of 4.
#
# This means Python over-allocates extra space whenever the list grows.
# The purpose is to reduce the number of reallocations when repeatedly
# appending elements.
#
# The comment in the code states the resulting growth pattern:
#
# 0, 4, 8, 16, 24, 32, 40, 52, 64, 76, ...
#
# Therefore the growth factor is approximately 1.125 (an increase of about
# 12.5% each time the list must expand).
#
# The resize operation only occurs when the new size exceeds the currently
# allocated capacity. Otherwise, if:
#
# allocated >= newsize && newsize >= (allocated >> 1)
#
# the list simply updates its size without reallocating memory.
#
# This strategy provides amortized O(1) time for append operations.
# ex3.py
#


import sys
import time
import matplotlib.pyplot as plt


# Q2
# Grow a list from 0 to 63 elements and print when capacity changes

print("Capacity changes while growing list:")

lst = []
prev_size = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    current_size = sys.getsizeof(lst)

    if current_size != prev_size:
        print("Length:", len(lst), " New memory size:", current_size, "bytes")
        prev_size = current_size


# Find S (largest size <= 64 that triggers resize on append)
lst = []
prev_size = sys.getsizeof(lst)
S = None

for i in range(64):
    lst.append(i)
    current_size = sys.getsizeof(lst)

    if current_size != prev_size:
        S = len(lst) - 1
        prev_size = current_size

print("S (largest size before expansion):", S)



times_expand = []

for _ in range(1000):
    lst = list(range(S))
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    times_expand.append(end - start)


# Q4
# Measure time to grow from S-1 -> S (no resize)

times_normal = []

for _ in range(1000):
    lst = list(range(S - 1))
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    times_normal.append(end - start)


# Q5
# Plot distributions

plt.hist(times_expand, bins=500)
plt.title("Append causing resize (S -> S+1)")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.xlim(0.00000018, .0000006)
plt.show()

plt.hist(times_normal, bins=500)
plt.title("Append without resize (S-1 -> S)")
plt.xlabel("Time (seconds)")
plt.xlim(.00000018, .0000006)
plt.ylabel("Frequency")
plt.show()


# Q5 Discussion
#
# The append operation that causes a resize (S -> S+1) is slower than the
# append operation that does not trigger a resize (S-1 -> S). This occurs
# because resizing requires allocating a new block of memory and copying
# all existing elements into the new array. When no resize occurs, the
# append operation simply places the element into the already allocated
# space, which is much faster. This difference appears in the histogram,
# where the resize times typically show a larger spread and slightly
# higher average time.
