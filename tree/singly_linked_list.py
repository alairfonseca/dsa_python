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
        
        for i in self:
            if i._value == value:
                return i._value

        return None

    def delete(self, index):
        if not self._head:
            raise Exception("Empty list")
        
        if index == 0:
            if self._head == self._tail:
                self._head = None
                self._tail = None
            else:
                self._head = self._head._next
            self._n -= 1
            return

        cursor = self._head
        cursor_count = 1
        
        while cursor:
            if cursor_count == index:
                if (cursor._next is not None) & (not cursor._next._next):
                    cursor._next = None
                    self._tail = cursor
                elif cursor._next._next:
                    cursor._next = cursor._next._next
                else:
                    cursor._next = None

            cursor_count += 1
            cursor = cursor._next
        

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
    print(slinklist.search(11))

    print("deleting...")
    slinklist.delete(1)
    print(1, "-", slinklist)

    slinklist.delete(6)
    print(6, "-", slinklist)
    
    slinklist.delete(1)
    print(1, "-", slinklist)

    slinklist.delete(0)
    print(0, "-", slinklist)
