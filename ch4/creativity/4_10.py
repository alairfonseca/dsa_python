"""
Describe a recursive algorithm to compute the integer part
of the base-two logarithm of n using only addition and integer division.
"""


def log(logarithm):
    base = 2

    if logarithm <= base:
        return 0

    return 1 + log(logarithm / base)


if __name__ == "__main__":
    print(log(1000000000))
    print(log(2232321312))
