import math

def binary_search(sequence, target):
    start = 0
    end = len(sequence) - 1
    mid = math.floor((start + end) / 2)
    
    while not sequence[mid] == target and start <= end:
        if target < sequence[mid]:
            end = mid - 1
        else:
            start = mid + 1

        mid = math.floor((start + end) / 2)

    if sequence[mid] == target:
        return mid
    else:
        return -1

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print(binary_search(l, 7))
    print(binary_search(l, 10))
    print(binary_search(l2, 100))
