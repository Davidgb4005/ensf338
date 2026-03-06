Exercise 7 – Reversing list
1. Time complexity of the given reverse() implementation

The provided implementation reverses the list by iterating through positions from size-1 down to 0 and retrieving elements using get_element_at_pos(i).

Step-by-step analysis:

The loop runs:

for i in range(self.get_size()-1, -1, -1)


This loop executes n times, where n is the number of elements in the list.

The function get_element_at_pos(i) is called inside the loop.
In a singly linked list, accessing a position requires traversal from the head.

Therefore:

get_element_at_pos(i) = O(n)


Since this call occurs inside the loop:

Total cost = n * O(n)


Thus the total complexity is:

O(n²)


Creating new nodes and pointer assignments are constant-time operations and do not affect the overall complexity.

Final complexity:

O(n²)


The quadratic complexity arises because the algorithm repeatedly traverses the list to access elements by index.

2. Optimized implementation

A better approach is to reverse the list in place by updating the next pointers of the nodes while traversing the list once.

Optimized algorithm:

def reverse(self):
    prev = None
    curr = self.head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    self.head = prev


Changes made:

Removed calls to get_element_at_pos()

Traversed the list once

Reversed links directly instead of creating new nodes

Complexity:

O(n)


Reason:

Each node is visited exactly once and only constant-time pointer operations are performed.

This improves performance from O(n²) → O(n).