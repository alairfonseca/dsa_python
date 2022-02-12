"""
Write a short recursive Python function that takes a character
string s and outputs its reverse. For example, the reverse of
'pots&pans' would be 'snap&stop'.
"""


def reverse_recursively(s):
    if len(s) == 1:
        return s

    result = list(s)

    aux = result[0]
    result[0] = result[-1]
    result[-1] = aux

    return "".join(result[0] + reverse_recursively(s[1:len(result) - 1]) + result[-1])


if __name__ == "__main__":
    print(reverse_recursively("pots&pans"))
    print(reverse_recursively("alair"))
