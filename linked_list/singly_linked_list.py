class Node:
    def __init__(self, value=None):
        self._value = value
        self._next = None

    def __str__(self):
        return str(self._value)

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def append(self, value):
        node = Node(value)

        if self._tail:
            self._tail._next = node

        if not self._head:
            self._head = node

        self._tail = node
        

    def __iter__(self):
        node = self._head

        while node:
            yield node
            node = node._next



if __name__ == "__main__":
    slinklist = SinglyLinkedList()
    
    slinklist.append(1)
    slinklist.append(2)

    print(slinklist._head._next, slinklist._head._next._next)

    for i in slinklist:
        print(i)
