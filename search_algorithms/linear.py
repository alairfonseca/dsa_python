def linear_search(sequence, target):
    for i in range(len(sequence)):
        if sequence[i] == target:
            return i
    return -1

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]
    
    print(linear_search(l, 9))
    print(linear_search(l2, 22))
