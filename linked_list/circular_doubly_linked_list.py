class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def append(self, value):
        new_node = Node(value)
        
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
        else:
            self.head = new_node
            new_node.prev = new_node

        new_node.next = self.head
        self.tail = new_node
        self.n += 1

    def insert(self, value, index):
        if index >= self.n and index != 0:
            raise IndexError("Index out of range")
        
        if index != 0:
            index = index % self.n
        
        new_node = Node(value)

        if index == 0:
            if self.head:
                new_node.next = self.head
                new_node.prev = self.tail
                
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node

                self.n += 1
                return
            else:
                self.append(value)
                return

        cursor = self.head
        cursor_count = 1
        
        while cursor:
            if cursor_count == index:
                new_node.prev = cursor
                new_node.next = cursor.next
                cursor.next.prev = new_node
                cursor.next = new_node

                self.n += 1
                return
            
            cursor = cursor.next
            cursor_count += 1

    def delete(self, index):
        if index >= self.n:
            raise IndexError("Index out of range")

        index = index % self.n

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            self.n -= 1
            return

        cursor = self.head
        cursor_count = 1

        while cursor.next != self.head:
            if cursor_count == index:
                cursor.next.next.prev = cursor
                cursor.next = cursor.next.next
                
                if cursor.next == self.head:
                    self.tail = cursor
                    self.head.prev = self.tail

                self.n -= 1
                return
            cursor = cursor.next
            cursor_count += 1
 
    def search(self, value):
        if not self.head:
            raise Exception("Empty list")
        
        for i in self:
            if i.value == value:
                return i.value

        return None

    def reverse_iter(self):
        node = self.tail

        while node:
            yield node

            if node.prev == self.tail:
                break

            node = node.prev

    def __iter__(self):
        node = self.head

        while node.next:
            yield node
            
            if node.next == self.head:
                break

            node = node.next

    def __str__(self):
        strng = ""
        for i in self:
            if i.next != self.head:
                strng += ("{0} <=> ".format(i))
            else:
                strng += "{0} -> {1}".format(i, i.next)

        return strng

    def __len__(self):
        return self.n


if __name__ == "__main__":
    list = CircularDoublyLinkedList()

    list.insert(0, 0)
    print(list)
    list.append(1)
    print(list)
    list.append(2)
    print(list)
    list.append(3)
    print(list)

    list.insert(4,0)
    print(list)
    list.insert(5, 2)
    print(list)
    list.insert(6, -1)
    print(list)

    list.append(7)
    print(list)
    list.insert(8, 0)
    print(list)
    
    for i in list.reverse_iter():
        print(i, end="")
    
    print("\n search:")
    print(list.search(4))
    print(list.search(7))

    list.delete(-1)
    print(list)
    list.delete(0)
    print(list)
    list.delete(5)
    print(list)
    
    for i in list.reverse_iter():
        print(i, end="")
    print("")

    list.delete(2)
    print(list)
    list.delete(1)
    print(list)
    
    for i in list.reverse_iter():
        print(i, end="")
    print("")
