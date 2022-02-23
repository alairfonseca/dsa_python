class QueueL:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.capacity = capacity
        self.start = -1
        self.top = -1

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        else:
            self.top = (self.top + 1) % self.capacity
            if self.start < 0:
                self.start = self.top
            self.items[self.top] = item

    def dequeue(self):
        self.start = (self.start + 1) % self.capacity

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        else:
            return self.start == 0 and self.top == self.capacity - 1
    
    def is_empty(self):
        return self.top == -1

    def __str__(self):
        return "".join([str(x) for x in self.items])

if __name__ == "__main__":
    q = QueueL(6)

    print(q.is_empty())
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    print(q.is_empty())
    print(q.is_full())
    
    print(q, q.start, q.top)

    q.dequeue()
    print(q, q.start, q.top)
    q.dequeue()
    print(q, q.start, q.top)

    print(q.is_empty())
    print(q.is_full())
    
    q.enqueue(7)
    print(q, q.start, q.top)
    q.enqueue(8)
    print(q, q.start, q.top)
    
    print(q.is_empty())
    print(q.is_full())
