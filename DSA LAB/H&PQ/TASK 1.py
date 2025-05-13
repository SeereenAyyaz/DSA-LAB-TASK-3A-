class Heap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type

    def _compare(self, child, parent):
        if self.heap_type == "min":
            return child < parent
        else:  
            return child > parent

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def extract_root(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest_or_largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self._compare(self.heap[left], self.heap[smallest_or_largest]):
            smallest_or_largest = left
        if right < len(self.heap) and self._compare(self.heap[right], self.heap[smallest_or_largest]):
            smallest_or_largest = right

        if smallest_or_largest != index:
            self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            self._heapify_down(smallest_or_largest)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def heapify(self, array):
        self.heap = array
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self._heapify_down(i)

# Test Cases
print("Min-Heap:")
min_heap = Heap("min")
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(20)
min_heap.insert(2)
print(min_heap.extract_root())  
print("\nMax-Heap:")
max_heap = Heap("max")
max_heap.insert(10)
max_heap.insert(5)
max_heap.insert(20)
max_heap.insert(2)
print(max_heap.extract_root())  
