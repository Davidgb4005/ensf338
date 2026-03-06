Exercise 6 – Back to arrays and lists
1. Advantages and disadvantages of arrays vs linked lists

Arrays (Python lists)

Advantages:

O(1) random access to any element using an index.

Better cache locality because elements are stored contiguously in memory.

Efficient for reading and iterating through elements.

Disadvantages:

Insertion and deletion in the middle require shifting elements, giving O(n) complexity.

May require reallocation and copying when capacity is exceeded.

Requires contiguous memory.

Linked Lists

Advantages:

Insertion and deletion are O(1) if the node position is known.

No need for contiguous memory.

Size can grow without reallocating the entire structure.

Disadvantages:

O(n) access time because elements must be traversed sequentially.

Extra memory overhead for storing pointers.

Poor cache locality compared to arrays.

2. Efficient implementation of a replace function in an array

A replace operation can be viewed as a deletion followed by an insertion at the same index. To minimize the cost:

Instead of performing a full delete and insert operation separately, simply overwrite the value at the given index.

Example conceptually:

replace(array, index, value):
    array[index] = value


This avoids shifting elements and results in O(1) complexity instead of O(n) for separate delete and insert operations.

3. Feasibility of sorting a doubly linked list
Insertion Sort

Feasibility:
Insertion sort is well suited for linked lists.

Reason:
Insertion sort repeatedly removes elements from the list and inserts them into their correct position in a sorted portion. In a doubly linked list, inserting a node only requires updating a few pointers and does not require shifting elements as in arrays.

Complexity:

Time complexity: O(n²)

Space complexity: O(1)

Comparison with arrays:
Insertion sort on arrays also has O(n²) time complexity, but insertion requires shifting elements, while linked lists only require pointer updates.

Merge Sort

Feasibility:
Merge sort works very well for doubly linked lists and is commonly used.

Reason:
Linked lists allow efficient splitting and merging because nodes can be reconnected using pointers without copying data. This avoids the element copying required when merging arrays.

Complexity:

Time complexity: O(n log n)

Space complexity: O(1) additional space when implemented using pointer manipulation.

Comparison with arrays:
Merge sort on arrays also has O(n log n) time complexity, but typically requires O(n) additional memory for temporary arrays. Linked lists avoid this extra memory by relinking nodes.

4. Complexity comparison summary
Algorithm	Data Structure	Time Complexity	Reason
Insertion Sort	Array	O(n²)	Requires shifting elements during insertion
Insertion Sort	Doubly Linked List	O(n²)	Only pointer updates are needed
Merge Sort	Array	O(n log n)	Requires additional memory for merging
Merge Sort	Doubly Linked List	O(n log n)	Nodes can be merged by changing pointers
Insertion sort benefits slightly from linked lists due to easier insertion operations, while merge sort is particularly efficient on linked lists because merging can be performed without additional memory allocation.