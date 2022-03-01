import math
from bubble_sort import bubble_sort

def bucket_sort(sequence):
    seq_len = len(sequence)
    
    buckets_number = round(math.sqrt(seq_len))
    max_value = max(sequence)
    arr = []
    
    for _ in range(buckets_number):
        arr.append([])

    for j in sequence:
        index_b = math.ceil(j * buckets_number / max_value)

        arr[index_b - 1].append(j)

    for i in range(buckets_number):
        arr[i] = bubble_sort(arr[i])

    k = 0
    for i in range(buckets_number):
        for j in range(len(arr[i])):
            sequence[k] = arr[i][j]
            k += 1

    print(sequence)
    return sequence

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    bucket_sort(l)
    bucket_sort(l2)
