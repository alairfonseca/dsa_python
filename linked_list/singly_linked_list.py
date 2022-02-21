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
        self._n = 0
    
    def append(self, value):
        node = Node(value)

        if self._tail:
            self._tail._next = node

        if not self._head:
            self._head = node

        self._tail = node
        self._n += 1

    def insert(self, value, index):
        new_node = Node(value)

        if index >= self._n:
            raise IndexError("Index out of range")
    
        if index == 0:
            if self._head:
                new_node._next = self._head
            self._head = new_node
            self._n += 1
        elif index == -1:
            self.append(value)
        else:
            cursor = self._head
            cursor_count = 1
            
            while cursor:
                if cursor_count == index:
                    new_node._next = cursor._next
                    cursor._next = new_node
                    self._n += 1
                    
                    return
                cursor = cursor._next
                cursor_count += 1

    def search(self, value):
        if not self._head:
            raise Exception("Empty list")

        node = self._head

        while node:
            if node._value == value:
                return node._value
            node = node._next

    def __iter__(self):
        node = self._head

        while node:
            yield node
            node = node._next

    def __str__(self):
        strng = ""
        for i in self:
            strng += ("{0} -> ".format(i))

        return strng

    def __len__(self):
        return self._n


if __name__ == "__main__":
    slinklist = SinglyLinkedList()
    
    slinklist.append(1)
    slinklist.append(2)
    
    print(slinklist)

    slinklist.insert(3, 1)
    print(slinklist)
    
    slinklist.insert(4, 0)
    print(slinklist)

    slinklist.insert(5, 3)
    print(slinklist)

    slinklist.insert(6, 4)
    print(slinklist)

    slinklist.append(7)
    print(slinklist)

    slinklist.insert(8, -1)
    print(slinklist)

    slinklist.insert(9, 2)
    print(slinklist)

    print(slinklist.search(2))
