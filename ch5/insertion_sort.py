def insertion_sort(A):
    print(A)
    for i in range(1, len(A)):
        curr = A[i]
        j = i

        while j > 0 and A[j - 1] > curr:
            A[j] = A[j - 1]
            j -= 1
        A[j] = curr

        print(A)
    return A


if __name__ == "__main__":
    a = [9, 2, 4, 8, 5, 7, 1, 3, 6]
    print(insertion_sort(a))
