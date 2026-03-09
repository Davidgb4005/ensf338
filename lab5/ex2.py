import random as rd
import timeit
import sys
sys.setrecursionlimit(50000)

class PrioQueue:
        def __init__(self):
            self.queue = []
        def enqueue(self, object):
            self.queue.append(object)
            if len(self.queue) > 1:
                self._mergesort(self.queue, 0, len(self.queue)-1)
        def dequeue(self):
            if len(self.queue) == 0:
                return None
            else:
                return self.queue.pop(0)
        def _mergesort(self, list, low, high):
             if low < high:
                mid = (low + high) // 2
                self._mergesort(list, low, mid)
                self._mergesort(list, mid + 1, high)
                self._merge(list, low, mid, high)
        def _merge(self, list, low, mid, high):
            size1 = mid - low + 1
            size2 = high - mid
            tempA = [0] * size1
            tempB = [0] * size2
            for i in range(size1):
                tempA[i] = list[low + i]
            for j in range(size2):
                tempB[j] = list[mid + 1 + j]
            i = j = 0
            index = low
            while i < size1 and j < size2:
                if tempA[i] <= tempB[j]:
                    list[index] = tempA[i]
                    i += 1
                else:
                    list[index] = tempB[j]
                    j += 1
                index += 1
            while i < size1:
                list[index] = tempA[i]
                i += 1
                index += 1
            while j < size2:
                list[index] = tempB[j]
                j += 1
                index += 1

class PrioQueue2:
    def __init__(self):
        self.queue = []
    def dequeue(self):
            if len(self.queue) == 0:
                return None
            else:
                return self.queue.pop(0)
    def enqueue(self, object):
        low = 0
        high = len(self.queue) - 1
        mid = (low + high) // 2
        while low <= high:
            mid = (low + high) // 2
            if self.queue[mid] < object:
                low = mid + 1
            else:
                high = mid - 1
        self.queue.insert(low, object)

def add_tasks(num):
    tasks = []
    for _ in range(num):
        if rd.random() < 0.7:
            tasks.append(("Enqueue", rd.randint(1, 100)))
        else:
            tasks.append(("Dequeue", None))
    return tasks

testinglist = [add_tasks(1000)]

def do_tasks(instance, tasklist):
    for k, v in tasklist:
        if k == "Enqueue":
            instance.enqueue(v)
        elif k == "Dequeue":
            instance.dequeue()

def timer_test(q_class):
    for tasks in testinglist:
        pq = q_class()
        do_tasks(pq, tasks)

PrioQueue1_time = timeit.timeit(lambda: timer_test(PrioQueue), number=1)
PrioQueue2_time = timeit.timeit(lambda: timer_test(PrioQueue2), number=1)

print(f"Mergesort Priority Queue Total Time: {PrioQueue1_time:.4f} seconds")
print(f"Binary Search Priority Queue Total Time: {PrioQueue2_time:.4f} seconds")

# The second priority queue implemntation is faster
# because enqueuing is done using binary search, which has an average complexity of O(logn)
# Meanwhile, the mergesort priority queue has to sort the queue every time an item is added,
# and mergesort has a complexity of O(nlogn), which is much slower.