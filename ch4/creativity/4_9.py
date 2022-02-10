"""
Write a short recursive Python function that finds the minimum
and maximum values in a sequence without using any loops.
"""


def find_min_and_max(sequence, n=0):
    lowest = sequence[n]
    highest = sequence[n]

    if n < len(sequence) - 1:
        x = find_min_and_max(sequence, n + 1)

        lowest = min(sequence[n], x[0])
        highest = max(sequence[n], x[1])

    return(lowest, highest)


if __name__ == "__main__":
    s = [3, 2, 5, 9, 10, 4, 8, 1, 0, 7, 6]
    print(find_min_and_max(s))
    s = [20, 31, 47, 46, 45, 48, 18, 11, 20, 17, 16]
    print(find_min_and_max(s))
    s = [20, 31, 47, 46, 45, 48, 18, 11, 20, 17, 49]
    print(find_min_and_max(s))
