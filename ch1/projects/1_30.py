"""
Write a Python program that can take a positive integer greater than 2
as input and write out the number of times one must repeatedly divide
this number by 2 before getting a value less than 2
"""


def count_div(n):
    if n < 2:
        return 0

    result = 0

    while n >= 2:
        n = n / 2
        result += 1

    return result


if __name__ == "__main__":
    print(count_div(2))
    print(count_div(240))
    print(count_div(25))
