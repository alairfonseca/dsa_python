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

        new_node.next = self.head
        self.tail = new_node
        self.n += 1
 
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

    list.append(1)
    print(list)
    list.append(2)
    print(list)
    list.append(3)
    print(list)
