"""
1.29 Write a Python program that outputs all possible strings formed by using
thecharacters characters ‘c’, ‘a’, ‘t’, ‘d’, ‘o’, and ‘g’ exactly once.
"""


def permutations(sequence):
    permut = []

    if len(sequence) == 1:
        permut.append(sequence)
    else:
        for (i, s) in enumerate(sequence):
            for permutation in permutations(sequence[:i] + sequence[i+1:]):
                permut.append(s + permutation)

    return permut


if __name__ == "__main__":
    s = "catdog"

    perms = permutations(s)

    for i in perms:
        print(i)
