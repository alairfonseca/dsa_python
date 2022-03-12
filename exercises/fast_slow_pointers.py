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

# happy number
def find_happy_number(num):
    slow, fast = num, num

    while True:
        slow = square_sum(slow)
        fast = square_sum(square_sum(fast))

        if slow == fast:
            break

    return slow == 1

def square_sum(num):
    result = 0

    while num > 0:
        digit = num % 10
        result += digit ** 2
        num //= 10
  
    return result

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
    print(find_happy_number(23))
    print(find_happy_number(12))
    
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
    print("===============================")
