# write a method to rotate a NxN matrix


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]

            matrix[i][j] = matrix[-j - 1][i]

            matrix[-j -1][i] = matrix[-i - 1][-j - 1]

            matrix[-i - 1][-j - 1] = matrix[j][-i - 1]

            matrix[j][-i - 1] = tmp

    return matrix

        



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(matrix))
