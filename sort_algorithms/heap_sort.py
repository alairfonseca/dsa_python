def heapfy(sequence, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and sequence[l] < sequence[smallest]:
        smallest = l
    
    if r < n and sequence[r] < sequence[smallest]:
        smallest = r

    if smallest != i:
        sequence[i], sequence[smallest] = sequence[smallest], sequence[i]
        heapfy(sequence, n, smallest)

def heap_sort(sequence):
    n = len(sequence)
    
    for i in range((n // 2) - 1, -1, -1):
        heapfy(sequence, n, i)

    for i in range(n - 1, 0, -1):
        sequence[i], sequence[0] = sequence[0], sequence[i]
        heapfy(sequence, i, 0)

    print(sequence)

if __name__ == "__main__":
    l = [2, 1, 7, 8, 6, 5, 9, 3, 4]
    l2 = [64, 34, 25, 12, 22, 11, 90]

    heap_sort(l)
    heap_sort(l2)
