from typing import Sequence

def selection_sort(sequence):
     for i in range(len(sequence)):
        min_index = i
        for j in range(i + 1, len(sequence)):
            if sequence[min_index] > sequence[j]:
                min_index = j
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]

    print(sequence)

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    selection_sort(l)
    selection_sort(l2)
