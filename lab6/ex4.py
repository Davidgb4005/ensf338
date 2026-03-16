

class Heap:
    def __init__(self):
        self.tree = []
    
    def _sort_down(self, index):
        n = len(self.tree)
        biggest = index
        left_child = 2*index + 1
        right_child = 2*index + 2
        if left_child < n and self.tree[left_child] > self.tree[biggest]:
            biggest = left_child
        if right_child < n and self.tree[right_child] > self.tree[biggest]:
            biggest = right_child
        if biggest != index:
            self.tree[index], self.tree[biggest] = self.tree[biggest], self.tree[index]
            self._sort_down(biggest)

    def heapify(self, arr):
        self.tree = arr
        for i in range(len(self.tree)//2 - 1, -1, -1):
            self._sort_down(i)
    
    def enqueue(self, item):
        self.tree.append(item)
        i = len(self.tree) - 1
        while i > 0:
            parent = (i-1)//2
            if self.tree[i] > self.tree[parent]:
                self.tree[i], self.tree[parent] = self.tree[parent], self.tree[i]
                i = parent
            else:
                return

    def dequeue(self):
        if not self.tree: # empty tree check
            return None
        if len(self.tree) == 1: #if only 1 element no need to do anything else
            return self.tree.pop()
        dequeued_val = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._sort_down(0)
        return dequeued_val



            