import timeit
import random
import matplotlib.pyplot as plt
import numpy as np



# Q4: Although binary search on an array runs in O(log n) time because we can directly access the middle element,
# binary search on a linked list ends up being O(n) overall. This is because finding the middle element in a linked
# list requires traversing from the head node each time, which takes O(n) time in the worst case. Even though the
# search interval is halved with each iteration, the cumulative cost of repeatedly finding the middle makes the
# overall complexity linear.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def get_middle_node(self, start, end):
        if start is None:
            return None

        slow = start
        fast = start
        # When fast reaches end or fast.next reaches end, slow will be at the middle.
        while fast != end and fast.next != end:
            fast = fast.next.next if fast.next and fast.next.next != end else fast.next
            slow = slow.next
        return slow

    def get_index(self, node):
        index = 0
        curr = self.head
        while curr:
            if curr is node:
                return index
            index += 1
            curr = curr.next
        return -1

    def binary_search(self, target):
        start = self.head
        end = None

        while start != end:
            mid = self.get_middle_node(start, end)
            if mid is None:
                return -1
            if mid.value == target:
                return self.get_index(mid)
            elif mid.value < target:
                start = mid.next
            else:
                end = mid
        return -1

    def to_list(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.value)
            curr = curr.next
        return lst


class ArrayClass:
    def __init__(self, data=None):
        self.array = data if data is not None else []

    def append(self, value):
        self.array.append(value)
        self.array.sort()  # Keep sorted (or, ideally, insert in sorted order)

    def binary_search(self, target):

        low = 0
        high = len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# Define input sizes and number of trials per measurement
sizes = [1000, 2000, 4000, 8000]
trials = 1000
ll_times = []   # Average time per search for LinkedList binary search
arr_times = []  # Average time per search for Array binary search

for n in sizes:
    data = list(range(n))
    
    # Build and populate the linked list
    ll = LinkedList()
    for num in data:
        ll.append(num)
    
    # Build the array-based structure
    arr = ArrayClass(data.copy())
    
    # Measure average time for linked list binary search using timeit
    t_ll = timeit.timeit(lambda: ll.binary_search(random.choice(data)), number=trials)
    ll_avg = t_ll / trials
    ll_times.append(ll_avg)
    
    # Measure average time for array binary search using timeit
    t_arr = timeit.timeit(lambda: arr.binary_search(random.choice(data)), number=trials)
    arr_avg = t_arr / trials
    arr_times.append(arr_avg)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# --- LinkedList Binary Search Plot ---
ax1.plot(sizes, ll_times, 'o-', label='LinkedList Binary Search')

ll_coef = np.polyfit(sizes, ll_times, 1)
ll_fit = np.poly1d(ll_coef)
ll_fit_vals = ll_fit(sizes)
ax1.plot(sizes, ll_fit_vals, '--', label=f'Fit: {ll_coef[0]:.2e}*n + {ll_coef[1]:.2e}')
ax1.set_title('LinkedList Binary Search Performance')
ax1.set_xlabel('Input Size (n)')
ax1.set_ylabel('Avg Time per Search (sec)')
ax1.legend()
ax1.grid(True)

# --- Array Binary Search Plot ---
ax2.plot(sizes, arr_times, 's-', label='Array Binary Search')

log_sizes = np.log(sizes)
a, b = np.polyfit(log_sizes, arr_times, 1)
arr_fit_vals = a * np.log(sizes) + b
ax2.plot(sizes, arr_fit_vals, '--', label=f'Fit: {a:.2e}*log(n) + {b:.2e}')
ax2.set_title('Array Binary Search Performance')
ax2.set_xlabel('Input Size (n)')
ax2.set_ylabel('Avg Time per Search (sec)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()