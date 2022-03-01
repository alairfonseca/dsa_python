def merge(sequence, i, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = sequence[l+i]
    
    for i in range(n2):
        R[i] = sequence[m + i + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            sequence[k] = L[i]
            i += 1
        else:
            sequence[k] = R[j]
            j += 1

        k += 1

    while i < n1:
        sequence[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        sequence[k] = R[j]
        j += 1
        k += 1

def merge_sort(sequence, l, r):
    if l < r:
        m = (l + (r - 1)) // 2
        merge_sort(sequence, l, m)
        merge_sort(sequence, m + 1, r)
        merge(sequence, l, m, r)
    
    print(sequence)

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    merge_sort(l, 0, len(l) - 1)
    merge_sort(l2, 0, len(l2) - 1)
