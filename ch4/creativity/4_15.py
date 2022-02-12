"""
Write a recursive function that will output all the subsets
of a set of n elements (without repeating any subsets).
"""


def subsets(input_set):
    if len(input_set) == 1:
        return [input_set]

    subs = subsets(input_set[1:])
    print(subs)

    return subs + [[input_set[0]] + i for i in subs]


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]

    print(subsets(a))
