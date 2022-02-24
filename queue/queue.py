from singly_linked_list import SinglyLinkedList
from singly_linked_list import Node

class Queue:
    def __init__(self):
        self.items = SinglyLinkedList()

    def enqueue(self, item):
        new_item = Node(item)

        self.items.append(new_item)

    def dequeue(self):
        self.items.delete(0)

    def peek(self):
        if len(self.items):
            return self.items._head._value
        else:
            raise Exception("Queue is empty")
    
    def is_empty(self):
        return len(self.items) > 0

    def delete(self):
        self.items = SinglyLinkedList()

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)

    print(q)
    
    print(q.is_empty())
    
    print(q)

    q.dequeue()
    print(q)
    q.dequeue()
    print(q)

    print(q.is_empty())
    
    q.enqueue(7)
    print(q)
    q.enqueue(8)
    print(q)
    
    print(q.is_empty())

    print("peek", q.peek())

    q.delete()
    print(q)
