class BinaryHeap:
    def __init__(self, size, heap_type="min"):
        self.max_size = size + 1
        self.items = [None] * self.max_size
        self.heap_size = 0
        self.heap_type = heap_type

    def insert_heapfy(self, index):
        parent_index = index // 2
        if index <= 1:
            return
        if self.heap_type == "min":
            if self.items[index] < self.items[parent_index]:
                self._swap_nodes(index, parent_index)
        elif self.heap_type == "max":
            if self.items[index] > self.items[parent_index]:
                self._swap_nodes(index, parent_index)
        self.insert_heapfy(parent_index)

    def insert(self, value):
        if self.heap_size + 1 == self.max_size:
            return "Heap is full"
        self.items[self.heap_size + 1] = value
        self.heap_size += 1

        self.insert_heapfy(self.heap_size)

    def peek(self):
        return self.items[1]

    def _swap_nodes(self, index, parent_index):
        temp = self.items[parent_index]

        self.items[parent_index] = self.items[index]
        self.items[index] = temp
    
    def __len__(self):
        return self.heap_size

    def __iter__(self):
        for i in range(1, self.heap_size + 1):
            yield self.items[i]

def levelorder_traversal(heap):
    if not heap:
        return
    for i in heap:
        print(i)

if __name__ == "__main__":
    bh = BinaryHeap(5)

    bh.insert(4)
    bh.insert(5)
    bh.insert(3)
    bh.insert(2)
    bh.insert(1)

    print("--------------------")
    print(len(bh))
    print("--------------------")
    print(levelorder_traversal(bh))
    print("--------------------")
    print(bh.items)
    print("--------------------")
    print("--------------------")
    print("--------------------")
    print("--------------------")
    print("--------------------")

