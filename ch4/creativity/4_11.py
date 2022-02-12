"""
Describe an efficient recursive function for solving the element
uniqueness problem, which runs in time that is at most O(n2) in
the worst case without using sorting.
"""


def uniqueness(sequence):
    if (len(sequence) == 1):
        return True
    elif sequence[0] in sequence[1:]:
        return False
    else:
        return uniqueness(sequence[1:])


if __name__ == "__main__":
    print(uniqueness([1, 2, 3, 4, 5, 6, 7, 8]))
    print(uniqueness([1, 2, 3, 4, 5, 6, 2, 8]))
    print(uniqueness(list(range(1, 1000))))
    list1 = list(range(1, 900))
    list1.append(899)
    print(uniqueness(list1))
