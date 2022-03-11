class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)


    print(has_cycle(head))
    print("===============================")
    
    head.next.next.next.next.next.next = head.next.next
    print(has_cycle(head))
    print("===============================")
    
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
