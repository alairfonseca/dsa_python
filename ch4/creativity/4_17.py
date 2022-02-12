"""
Write a short recursive Python function that determines if a string
s is a palindrome, that is, it is equal to its reverse. For example,
'racecar' and 'gohangasalamiimalasagnahog' are palindromes.
"""


def is_palindrome(s):
    if len(s) <= 1:
        return True

    return (s[0] == s[-1]) & is_palindrome(s[1:len(s) - 1])


if __name__ == "__main__":
    print("racecar: ", is_palindrome("racecar"))
    print("alair: ", is_palindrome("alair"))
    print("tenet: ", is_palindrome("tenet"))
    print("pato: ", is_palindrome("pato"))
    print("gohangasalamiimalasagnahog: ", is_palindrome("gohangasalamiimalasagnahog"))
