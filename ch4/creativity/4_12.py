"""
Give a recursive algorithm to compute the product of two positive
integers, m and n, using only addition and subtraction.
"""


def recursive_product(m, n):
    if n == 1:
        return m
    return m + recursive_product(m, n - 1)


if __name__ == "__main__":
    print(recursive_product(2, 4))
    print(recursive_product(3, 4))
    print(recursive_product(9, 8))
    print(recursive_product(2.5, 2))
