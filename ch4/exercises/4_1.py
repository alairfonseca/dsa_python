"""
Describe a recursive algorithm for finding the maximum element
in a sequence, S, of n elements. What is your running time and
space usage?
"""


def find_maximum(sequence, i):
    highest = sequence[i]

    if i < len(sequence) - 1:
        highest = max(sequence[i], find_maximum(sequence, i + 1))

    return highest


if __name__ == "__main__":
    s = [3, 2, 5, 9, 10, 4, 8, 1, 0, 7, 6]
    print(find_maximum(s, 0))
    s = [20, 31, 47, 46, 45, 48, 18, 11, 20, 17, 16]
    print(find_maximum(s, 0))
