def gcd(a, b):
    a = abs(a)
    b = abs(b)

    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(gcd(20, 50))
    print(gcd(48, 12))
    print(gcd(48, -18))
