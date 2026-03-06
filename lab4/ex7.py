import timeit
import matplotlib.pyplot as plt
import random as rd

sizes = [1000, 2000, 3000, 4000]

slow_times = []
fast_times = []


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self, head, size):
        self.head = head
        self.size = size

    def get_size(self):
        return self.size

    def get_element_at_pos(self, i):
        node = self.head
        while i > 0 and node is not None:
            node = node.next
            i -= 1
        return node

    def reverse_new(self):
        prev = None
        curr = self.head

        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev

    def reverse_old(self):
        newhead = None
        prevNode = None

        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)

            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode

            prevNode = currNewNode

        self.head = newhead


def build_list(size):
    head = Node(rd.randint(0, 1000))
    prev = head

    for _ in range(size - 1):
        node = Node(rd.randint(0, 1000))
        prev.next = node
        prev = node

    return LinkedList(head, size)


for n in sizes:

    slow = timeit.timeit(
        stmt=lambda: build_list(n).reverse_old(),
        number=100
    )

    fast = timeit.timeit(
        stmt=lambda: build_list(n).reverse_new(),
        number=100
    )

    slow_times.append(slow / 100)
    fast_times.append(fast / 100)


plt.plot(sizes, slow_times, marker='o', label='Original O(n^2)')
plt.xlabel("List Size")
plt.ylabel("Average Time (seconds)")
plt.title("Reverse List Performance Comparison")

plt.legend()
plt.show()

plt.plot(sizes, fast_times, marker='o', label='Optimized O(n)')

plt.xlabel("List Size")
plt.ylabel("Average Time (seconds)")
plt.title("Reverse List Performance Comparison")

plt.legend()
plt.show()

