def power(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n
    return n * power(n, p - 1)


if __name__ == "__main__":
    print(power(2, 3))
    print(power(4, 6))
    print(power(2, 0))
