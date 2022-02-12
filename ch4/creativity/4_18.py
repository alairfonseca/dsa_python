"""
Use recursion to write a Python function for determining if a string
s has more vowels than consonants.
"""

VOWELS = "aeiou"


def has_more_vowels(s, i=0, vowels_count=0):
    if i == len(s):
        return vowels_count > (len(s) / 2)

    if s[i] in VOWELS:
        vowels_count += 1

    return has_more_vowels(s, i + 1, vowels_count)


if __name__ == "__main__":
    print("alair: ", has_more_vowels("alair"))
    print("teste: ", has_more_vowels("teste"))
