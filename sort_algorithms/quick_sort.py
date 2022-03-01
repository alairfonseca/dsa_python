def partition(sequence, low, high):
    i = low - 1
    pivot = sequence[high]

    for j in range(low, high):
        if sequence[j] < pivot:
            i += 1
            sequence[i], sequence[j] = sequence[j], sequence[i]
    sequence[i + 1], sequence[high] = sequence[high], sequence[i + 1]
    
    return i + 1    

def quick_sort(sequence, low, high):
    if low < high:
        pindex = partition(sequence, low, high)
        quick_sort(sequence, low, pindex - 1)
        quick_sort(sequence, pindex + 1, high)

    print(sequence)

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    quick_sort(l, 0, len(l) - 1)
    quick_sort(l2, 0, len(l2) - 2)
