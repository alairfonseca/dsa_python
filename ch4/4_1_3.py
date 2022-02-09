# Binary search
def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    list1 = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ]
    list2 = list(range(133, 2000))
    print(binary_search(list1, 13, 0, len(list1) - 1))
    print(binary_search(list1, 21, 0, len(list1) - 1))
    print(binary_search(list2, 1971, 0, len(list2) - 1))
    print(binary_search(list2, 131, 0, len(list2) - 1))
