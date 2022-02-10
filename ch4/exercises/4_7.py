"""
Describe a recursive function for converting a string of
digits into the integer it represents. For example, ‘13531’
represents the integer 13,531.
"""


def to_int(digit):
    zero = ord('0')

    return ord(digit) - zero


def convert_to_int(digits):
    b = to_int(digits[0])

    if len(digits) == 1:
        return b

    a = convert_to_int(digits[1:])

    b = b * (10 ** (len(digits) - 1)) + a

    return b


if __name__ == "__main__":
    print(convert_to_int("13531"))
