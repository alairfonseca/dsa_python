class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def append(self, value):
        node = Node(value)
        node.next = self.head
        
        if not self.head:
            self.head = node

        if self.tail:
            self.tail.next = node
        
        self.tail = node
        self.n += 1

    def insert(self, value, index):
        if index > self.n:
            raise IndexError("Index out of range")

        index = index % self.n
        
        new_node = Node(value)
        
        if index == 0:
            if self.head:
                new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.n += 1

            return

        cursor = self.head
        cursor_count = 1
        
        while cursor:
            if cursor_count == index:
                new_node.next = cursor.next
                cursor.next = new_node
                self.n += 1
                
                return
            cursor = cursor.next
            cursor_count += 1

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next
    
    def __str__(self):
        strng = ""
        for i in self:
            strng += ("{0} -> ".format(i))

        return strng
    
    def __len__(self):
        return self.n

if __name__ == "__main__":
    list = CircularSinglyLinkedList()

    list.append(1)
    print(list)
    list.append(2)
    print(list)
    list.append(3)
    print(list)


    list.insert(4, 1)
    print(list)
    list.insert(5, 0)
    print(list)
    list.insert(6, 3)
    print(list)
    list.insert(7, -2)
    print(list)
    list.insert(8, -7)
    print(list)

    print("tail next:", list.tail.next)

