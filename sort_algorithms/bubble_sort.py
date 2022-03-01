def bubble_sort(sequence):
    for i in range(len(sequence) - 1):
        for j in range(len(sequence) - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]

    return sequence

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    bubble_sort(l)
    bubble_sort(l2)
