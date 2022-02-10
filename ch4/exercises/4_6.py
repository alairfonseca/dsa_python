"""
Describe a recursive function for computing the nth Harmonic number
"""


def harmonic(n, i=1):
    result = 0

    if i <= n:
        result = 1 / i

        i += 1

        result = result + harmonic(n, i)

    return result


if __name__ == "__main__":
    print(harmonic(5))
    print(harmonic(120))
