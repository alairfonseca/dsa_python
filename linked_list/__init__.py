from linked_list import LinkedList

def remove_dup(list):
    if not list.head:
        return
    else:
        elements = []
        cursor = list.head

        while cursor.next:
            if cursor.next.value in elements:
                if cursor.next.next:
                    cursor.next = cursor.next.next
                else:
                    cursor.next = None
                    list.tail = cursor
            else:
                elements.append(cursor.value)
                cursor = cursor.next

def nth_to_last(list, n):
    cursor1 = list.head
    cursor2 = list.head

    for _ in range(n):
        if not cursor2:
            return None
        cursor2 = cursor2.next

    while cursor2:
        cursor2 = cursor2.next
        cursor1 = cursor1.next

    return cursor1.value

def partition(list, value):
    cursor = list.head
    list.tail = list.head

    while cursor:
        next_node = cursor.next
        cursor.next = None

        if cursor.value < value:
            cursor.next = list.head
            list.head = cursor
        else:
            list.tail.next = cursor
            list.tail = cursor
        cursor = next_node

    if list.tail.next:
        list.tail.next = None

def sum_linked_lists(lista, listb):
    a = lista.head
    b = listb.head
    carry = 0
    result = LinkedList()

    while a or b:
        res = carry

        if a:
            res += a.value
            a = a.next
        if b:
            res += b.value
            b = b.next

        carry = res // 10
        
        result.append(int(res % 10))

    return result


if __name__ == "__main__":
    list = LinkedList().generate(10, 0, 9)

    print(list)
    
    remove_dup(list)
    print(list)

    list2 = LinkedList().generate(10, 0, 9)
    print(list)

    print(nth_to_last(list, 5))
    print(nth_to_last(list, 2))
    print(nth_to_last(list, 1))

    print("partition...")
    list3 = LinkedList().generate(10, 0, 99)
    print(list3)
    partition(list3, 40)
    print(list3)


    print("sum...")
    lista = LinkedList()
    lista.append(7)
    lista.append(1)
    lista.append(6)

    listb = LinkedList()
    listb.append(5)
    listb.append(9)
    listb.append(2)
    print(lista)
    print(listb)
    print(sum_linked_lists(lista, listb))

