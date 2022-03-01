def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        current = sequence[i]
        j = i - 1

        while j >= 0 and key < sequence[j]:
            sequence[j + 1] = sequence[j]
            j -= 1

        sequence[j] = current

    print(sequence)

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    insertion_sort(l)
    insertion_sort(l2)
