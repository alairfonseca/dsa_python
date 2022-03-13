class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
def reverse(head):
    current = head
    previous = None
    next = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous

# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
def reverse_sub_list(head, p, q):
    start = None
    end = None

    cursor = head
    while not start or not end:
        if cursor.next.value == p:
            start = cursor

        if cursor.value == q:
            end = cursor.next
        
        cursor = cursor.next

    current = start.next
    previous = None
    next = None
    while current.value <= q:
        next = current.next

        if not previous:
            current.next = end
            previous = current
        else:
            current.next = previous
            previous = current
        
        current = next

    start.next = previous

    return head


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

main()
