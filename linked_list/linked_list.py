from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0

    def append(self, value):
        node = Node(value)

        if self.tail:
            self.tail.next = node

        if not self.head:
            self.head = node

        self.tail = node
        self.n += 1
    
    def __iter__(self):
        node = self.head

        while node:
            yield node
            
            node = node.next

    def __len__(self):
        return self.n

    def __str__(self):
        strng = ""
        for i in self:
            strng += ("{0} -> ".format(i))

        return strng

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None

        for _ in range(n):
            self.append(randint(min_value, max_value))
        
        return self

if __name__ == "__main__":
    list = LinkedList().generate(10, 0, 9)

    print(list)




